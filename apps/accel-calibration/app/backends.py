"""
Measurement backends.

A backend knows how to set up, measure one frequency point, and tear down. There
are two interchangeable implementations:

- SimulationBackend: produces realistic sensitivity values with NO hardware, so
  the whole app (screen + report) can be exercised before going to the bench.
- NVGateBackend: the real thing — drives the OROS sine generator, holds a
  constant acceleration with a closed loop on the reference channel, and reads
  the sensitivity from NVGate's FRF (no signal math is reimplemented in Python).

Both return a PointMeasurement. All of this is plain, deterministic code — there
is no AI at runtime (CLAUDE.md section 3).
"""

import hashlib
import math
import time
from dataclasses import dataclass

from .config import CONFIG


@dataclass
class PointMeasurement:
    freq_hz: float
    sensitivity_mv_per_ms2: float
    phase_deg: float
    achieved_level_ms2: float
    level_reached: bool
    note: str = ""


class BackendError(Exception):
    """A measurement could not be completed (with a plain-language message)."""


class MeasurementBackend:
    is_simulation = False

    def setup(self, model):
        raise NotImplementedError

    def measure_point(self, freq_hz):
        raise NotImplementedError

    def teardown(self):
        pass


# ── Simulation ────────────────────────────────────────────────────────────────

class SimulationBackend(MeasurementBackend):
    """Fake but realistic measurements. Repeatable for a given serial."""

    is_simulation = True

    def __init__(self, serial="SIM"):
        self._serial = serial or "SIM"
        self._model = None

    def setup(self, model):
        self._model = model

    def measure_point(self, freq_hz):
        time.sleep(0.12)  # give the UI the feel of a real measurement
        base = self._model.nominal_mv_per_ms2
        # gentle, smooth frequency trend (~+1% per decade) + tiny repeatable jitter
        trend = 0.010 * math.log10(max(freq_hz, 1.0) / 160.0)
        jitter = self._jitter(f"{self._serial}|{freq_hz}|mag", 0.012)
        sens = base * (1.0 + trend + jitter)
        phase = (-0.8 * math.log10(max(freq_hz, 1.0) / 16.0)
                 + self._jitter(f"{self._serial}|{freq_hz}|ph", 0.6))
        return PointMeasurement(
            freq_hz=freq_hz,
            sensitivity_mv_per_ms2=sens,
            phase_deg=phase,
            achieved_level_ms2=CONFIG.target_level_ms2,
            level_reached=True,
        )

    @staticmethod
    def _jitter(seed, spread):
        h = int(hashlib.md5(seed.encode("utf-8")).hexdigest(), 16)
        return ((h % 10000) / 10000.0 - 0.5) * 2 * spread


# ── Live NVGate ───────────────────────────────────────────────────────────────

class NVGateBackend(MeasurementBackend):
    """
    Drives NVGate over the live link.

    NOTE: the generator frequency/level IDNs and the FRF result address in
    config.py are placeholders to confirm once on the bench (DIRECTIVE.md
    section 9). The control logic itself is final.
    """

    is_simulation = False

    def __init__(self):
        self._client = None
        self._model = None

    def setup(self, model):
        from oros_helpers import connect
        self._model = model
        self._client = connect()  # raises ConnectionError if NVGate is unreachable

    def measure_point(self, freq_hz):
        from oros_helpers import set_setting, run_measurement, stop_measurement
        c = self._client

        # 1. set sine frequency, enable the sine, start at a low output, run.
        set_setting(CONFIG.gen_frequency_idn, freq_hz, client=c)
        set_setting(CONFIG.gen_sine_state_idn, 1, client=c)
        level = CONFIG.start_generator_level
        set_setting(CONFIG.gen_level_idn, level, client=c)
        run_measurement(client=c)

        # 2. closed loop: nudge the output until the reference reads the target.
        achieved = 0.0
        reached = False
        for _ in range(CONFIG.max_iterations):
            time.sleep(CONFIG.settle_seconds)
            achieved = self._read_reference_level()
            if achieved <= 0:
                continue
            err_pct = abs(achieved - CONFIG.target_level_ms2) / CONFIG.target_level_ms2 * 100.0
            if err_pct <= CONFIG.level_tolerance_pct:
                reached = True
                break
            level = level * (CONFIG.target_level_ms2 / achieved)
            level = max(0.0, min(level, CONFIG.max_generator_level))
            set_setting(CONFIG.gen_level_idn, level, client=c)
            if level >= CONFIG.max_generator_level:
                time.sleep(CONFIG.settle_seconds)
                achieved = self._read_reference_level()
                break

        # 3. settle, then read the sensitivity (magnitude + phase) from the FRF.
        time.sleep(CONFIG.settle_seconds)
        mag_v_per_ms2, phase = self._read_frf_at(freq_hz)

        stop_measurement(client=c)
        set_setting(CONFIG.gen_sine_state_idn, 0, client=c)  # silence between points

        note = "" if reached else "level target not reached"
        return PointMeasurement(
            freq_hz=freq_hz,
            sensitivity_mv_per_ms2=mag_v_per_ms2 * 1000.0,  # V/(m/s^2) -> mV/(m/s^2)
            phase_deg=phase,
            achieved_level_ms2=achieved,
            level_reached=reached,
            note=note,
        )

    def teardown(self):
        if self._client is None:
            return
        try:
            from oros_helpers import set_setting, stop_measurement
            set_setting(CONFIG.gen_sine_state_idn, 0, client=self._client)
            stop_measurement(client=self._client)
        except Exception:
            pass
        try:
            self._client.disconnect()
        except Exception:
            pass
        self._client = None

    # --- internals ---------------------------------------------------------

    def _read_reference_level(self):
        from oros_helpers import get_scalar_result
        m, p, ch, ref = CONFIG.ref_level_result
        try:
            return float(get_scalar_result(
                module=m, process=p, channel=ch,
                reference_channel_number=ref, client=self._client))
        except Exception:
            return 0.0

    def _read_frf_at(self, freq_hz):
        from oros_helpers import get_result
        m, p, ch, ref = CONFIG.frf_result
        result = get_result(module=m, process=p, channel=ch,
                            reference_channel_number=ref, client=self._client)
        return _extract_frf_point(result, freq_hz)


def _extract_frf_point(result, freq_hz):
    """
    Return (magnitude in V/(m/s^2), phase in degrees) at freq_hz from an NVGate
    FRF result. The exact result structure is confirmed on the bench; this reads
    the common shapes and raises a clear error if it sees something unexpected.
    """
    try:
        d = result.to_dict()
    except Exception as e:  # pragma: no cover - depends on live data
        raise BackendError(f"Could not read the FRF result: {e}")

    # locate the frequency axis
    freqs = None
    for key in ("abscissa", "x", "frequencies", "freq", "x_axis"):
        if isinstance(d.get(key), (list, tuple)) and d[key]:
            freqs = list(d[key])
            break
    # locate the values (may be complex, or magnitude, or (re, im))
    values = None
    for key in ("ordinate", "values", "y", "data", "spectrum"):
        if isinstance(d.get(key), (list, tuple)) and d[key]:
            values = list(d[key])
            break

    if freqs is None or values is None:
        raise BackendError(
            "FRF result shape not recognised — confirm the FRF address and "
            "result format on the bench (DIRECTIVE.md section 9). "
            f"Available keys: {sorted(d.keys())}")

    # nearest frequency bin
    idx = min(range(len(freqs)), key=lambda i: abs(freqs[i] - freq_hz))
    v = values[idx]
    if isinstance(v, complex):
        return abs(v), math.degrees(math.atan2(v.imag, v.real))
    if isinstance(v, (list, tuple)) and len(v) == 2:
        re, im = float(v[0]), float(v[1])
        return math.hypot(re, im), math.degrees(math.atan2(im, re))
    # plain magnitude; try to pair with a phase array if present
    mag = float(v)
    phase = 0.0
    for key in ("phase", "phases", "angle"):
        if isinstance(d.get(key), (list, tuple)) and len(d[key]) > idx:
            phase = float(d[key][idx])
            break
    return mag, phase
