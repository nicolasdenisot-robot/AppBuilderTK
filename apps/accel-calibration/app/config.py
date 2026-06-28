"""
Configuration for the Accelerometer Calibration app.

These are plain values an engineer can safely edit. Nothing here touches NVGate's
data files. The only values that may need a one-time update after the first live
session are the IDNs marked "CONFIRM ON BENCH" (see DIRECTIVE.md sections 3 and 9).
"""

from dataclasses import dataclass, field

# 1 g expressed in m/s^2 (exact, ISO 80000).
G_TO_MS2 = 9.80665

# Standard calibration frequencies (Hz). The operator ticks a subset of these.
STANDARD_FREQUENCIES_HZ = [16, 31.5, 63, 80, 125, 160, 250, 500, 1000, 2000, 5000]


@dataclass
class Config:
    # --- Reference accelerometer (the calibrated standard) -------------------
    reference_sensitivity_mv_per_ms2: float = 10.0
    reference_is_iepe: bool = True
    reference_channel: int = 1          # NVGate Input number for the reference
    dut_channel: int = 2               # NVGate Input number for the unit under test

    # --- Closed-loop level control (hold a constant acceleration) -----------
    target_level_ms2: float = 10.0      # acceleration to hold at each frequency
    level_tolerance_pct: float = 5.0    # acceptable band around the target
    max_iterations: int = 12            # control-loop attempts per frequency
    settle_seconds: float = 1.5         # wait after a level change before reading
    start_generator_level: float = 0.05 # initial generator output before adjusting
    max_generator_level: float = 1.0    # generator output ceiling (shaker safety)

    # --- Default pass/fail tolerance (a model can override this) -------------
    default_tolerance_pct: float = 5.0

    # --- Report ------------------------------------------------------------
    report_sensitivity_unit: str = "mV/g"   # "mV/g" or "mV/(m/s^2)"
    method_label: str = "Comparison method (ISO 16063-21)"

    # --- NVGate IDNs --- CONFIRM ON BENCH (see DIRECTIVE.md section 9) -------
    # Generator is module 7. The sine submodule activates via the documented IDN
    # below. The frequency/level IDNs are placeholders to confirm on the analyzer
    # with SHIFT + right-click. Until confirmed, run the app in simulation.
    gen_sine_state_idn: str = "generator 225:1 state"      # documented
    gen_frequency_idn: str = "generator 225:1 frequency"   # PLACEHOLDER - confirm
    gen_level_idn: str = "generator 225:1 level"           # PLACEHOLDER - confirm

    # Result addresses: (module, process, channel, reference_channel_number).
    # Confirm with oros_helpers.list_results() once on the bench.
    frf_result: tuple = (10, 0, 2, 1)        # FRF transfer DUT/ref  - confirm
    ref_level_result: tuple = (10, 0, 1, 0)  # reference overall accel - confirm

    # Optional NVGate transducer/channel setup IDNs (left empty = skip; the
    # operator can pre-configure the project instead). Confirm if you automate it.
    setup_inputs_automatically: bool = False


CONFIG = Config()
