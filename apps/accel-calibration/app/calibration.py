"""
Calibration orchestrator — the deterministic flow from DIRECTIVE.md section 4.

Runs the chosen backend across the selected frequencies, judges each point
against the model's tolerance, and returns a CalibrationResult. Reports progress
through a callback so the screen can update live, and can be cancelled.
"""

import datetime as dt
from dataclasses import dataclass, field

from .config import CONFIG, G_TO_MS2
from .backends import PointMeasurement


@dataclass
class PointResult:
    freq_hz: float
    sensitivity_mv_per_ms2: float
    sensitivity_mv_per_g: float
    phase_deg: float
    deviation_pct: float
    verdict: str          # "PASS" / "FAIL" / "CHECK"
    achieved_level_ms2: float
    note: str = ""


@dataclass
class CalibrationResult:
    model: object
    serial: str
    operator: str
    timestamp: dt.datetime
    simulated: bool
    target_level_ms2: float
    reference_sensitivity_mv_per_ms2: float
    method_label: str
    points: list = field(default_factory=list)

    @property
    def overall_verdict(self):
        if not self.points:
            return "N/A"
        return "PASS" if all(p.verdict == "PASS" for p in self.points) else "FAIL"


class CalibrationCancelled(Exception):
    """Raised internally when the operator cancels a run."""


class CalibrationRunner:
    def __init__(self, backend):
        self.backend = backend

    def run(self, model, serial, operator, frequencies,
            progress_cb=None, is_cancelled=None):
        is_cancelled = is_cancelled or (lambda: False)
        progress_cb = progress_cb or (lambda **kw: None)

        result = CalibrationResult(
            model=model,
            serial=serial,
            operator=operator,
            timestamp=dt.datetime.now(),
            simulated=self.backend.is_simulation,
            target_level_ms2=CONFIG.target_level_ms2,
            reference_sensitivity_mv_per_ms2=CONFIG.reference_sensitivity_mv_per_ms2,
            method_label=CONFIG.method_label,
        )

        freqs = sorted({float(f) for f in frequencies})
        total = len(freqs)

        self.backend.setup(model)
        try:
            for i, f in enumerate(freqs, start=1):
                if is_cancelled():
                    raise CalibrationCancelled()
                progress_cb(stage="measuring", index=i, total=total, freq_hz=f, point=None)
                measurement = self.backend.measure_point(f)
                point = self._judge(model, measurement)
                result.points.append(point)
                progress_cb(stage="point_done", index=i, total=total, freq_hz=f, point=point)
        finally:
            self.backend.teardown()

        return result

    @staticmethod
    def _judge(model, m: PointMeasurement):
        nominal = model.nominal_mv_per_ms2
        sens_g = m.sensitivity_mv_per_ms2 * G_TO_MS2
        deviation = ((m.sensitivity_mv_per_ms2 - nominal) / nominal * 100.0
                     if nominal > 0 else float("nan"))
        within = abs(deviation) <= model.tolerance_pct

        if not m.level_reached:
            verdict = "CHECK"
        elif within:
            verdict = "PASS"
        else:
            verdict = "FAIL"

        note = m.note
        if not m.level_reached and not note:
            note = "level target not reached"

        return PointResult(
            freq_hz=m.freq_hz,
            sensitivity_mv_per_ms2=m.sensitivity_mv_per_ms2,
            sensitivity_mv_per_g=sens_g,
            phase_deg=m.phase_deg,
            deviation_pct=deviation,
            verdict=verdict,
            achieved_level_ms2=m.achieved_level_ms2,
            note=note,
        )
