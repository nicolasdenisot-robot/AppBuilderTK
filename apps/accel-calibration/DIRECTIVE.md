---
# ── Build manifest ───────────────────────────────────────────────────────
# Fields read by tools/export_app.py: version, display_name, export_target,
# entry_point, logo.
app_name: accel-calibration
version: 1.0
display_name: Accelerometer Calibration
export_target: exe          # confirm with user at export time (stop #6)
entry_point: app/main.py
logo: oros
helpers_used:
  - connection
  - settings
  - results
# requirements are listed in requirements.txt
---

# DIRECTIVE — Accelerometer Calibration

> The spec AND living memory for this app. Do not overwrite or discard without
> asking the user (CLAUDE.md rule #5). Update the Lessons section as we learn.

## 1. Objective
A one-click station that calibrates an accelerometer under test by the
**comparison method** (ISO 16063-21): the analyzer drives a shaker through a
range of frequencies, holds a constant acceleration at each, measures the
sensitivity (magnitude + phase) of the unit under test against a reference
accelerometer, judges each point against the model's tolerance, and produces a
**Word calibration certificate**.

## 2. Operator & run context
- **Who runs it:** a line operator who just clicks a desktop icon.
- **Live or offline:** live analyzer (NVGate running, connected mode).
- **Capability layer:** live control (pynvdrive).
- **UI stack:** PySide6 desktop window.
- **Delivery form:** exe (to confirm at export — CLAUDE.md stop #6).
- **Launch point:** double-click desktop icon (optionally also NVGate Automation).
- **Simulation mode:** the app runs fully WITHOUT NVGate/shaker for UI + report
  testing. It auto-detects NVGate; if absent it offers simulation. A checkbox
  also forces simulation. There is no AI anywhere in the runtime (CLAUDE.md §3).

## 3. Inputs

### Operator entries (in the UI)
| Name | Notes |
|------|-------|
| Accelerometer model | dropdown from the editable models file (§ models) |
| Serial number (DUT) | free text, goes on the certificate |
| Operator name | free text, goes on the certificate |
| Frequencies | tick from the standard set (editable in config) |
| Simulation checkbox | force simulation even if NVGate is present |

### Fixed configuration (`app/config.py`, editable, not in NVGate data)
| Name | Value |
|------|-------|
| Reference accelerometer sensitivity | 10.0 mV/(m/s²), IEPE |
| Reference input channel | Input 1 |
| DUT input channel | Input 2 |
| Target acceleration level | 10.0 m/s² (held constant per frequency) |
| Default pass/fail tolerance | ±5 % deviation from nominal sensitivity (per model) |
| Report sensitivity unit | mV/g (1 g = 9.80665 m/s²) |
| Standard frequency set (Hz) | 16, 31.5, 63, 80, 125, 160, 250, 500, 1000, 2000, 5000 |

### NVGate setting IDNs (generator = module 7)  -- CONFIRM ON BENCH
The activation IDN is documented (`generator 225:1 state`). The exact
**frequency** and **level** setting IDNs of the Advanced Sine Generator must be
confirmed once on the analyzer with SHIFT + right-click (manual §3.6.1) and
pasted into `app/config.py`. Until confirmed, the live backend uses placeholder
named IDNs and the app still runs fully in simulation. See Lessons §9.

## 4. Steps (the deterministic flow)
For the whole run:
1. Operator selects model, enters serials, ticks frequencies, clicks **Start**.
2. Connect to NVGate (or enter simulation).
3. Configure inputs: reference (Input 1) reads acceleration via its 10 mV/(m/s²)
   transducer sensitivity; DUT (Input 2) reads raw voltage (IEPE on). Enable the
   FFT analyzer with the FRF (transfer DUT/ref) and the channel autospectra.

For each selected frequency f:
4. Set the sine generator to f; activate it; Run.
5. **Closed-loop level**: read the reference acceleration; step the generator
   level up/down until the reference reads the target (within tolerance) or the
   iteration cap is reached; respect a max output for shaker safety.
6. Let it settle / average, then read the FRF magnitude & phase at f.
7. Sensitivity = FRF magnitude (V/(m/s²)) -> convert to mV/(m/s²) and mV/g.
8. Deviation = (measured - nominal) / nominal x 100 %. PASS if |deviation| <=
   model tolerance, else FAIL.
9. Append the point to the live results table; update progress.

After the last frequency:
10. Stop the generator and analyzer.
11. Overall verdict = PASS only if every point passes.
12. Write the Word certificate to a NEW dated file; show its path; offer to open.

## 5. Computation
- **NVGate-native (preferred):** FFT autospectra (per channel level for the
  closed loop) and the FRF (transfer function DUT/ref -> sensitivity magnitude &
  phase). No FFT is reimplemented in Python (Tier-1 rule).
- **Python library (only where NVGate can't):**
  - `python-docx` — writes the Word certificate.
  - `matplotlib` — renders the sensitivity-vs-frequency curve embedded in the doc.
  - (numpy pulled in by matplotlib; used only for light array work.)

## 6. Outputs
- **Where results appear:** the app's own PySide6 screen (live table + progress),
  because the operator has no NVGate window in front of them.
- **Exports:** Word calibration certificate
  `Calibration_<model>_<serial>_<YYYY-MM-DD>.docx` written to the operator's
  Documents (or a chosen folder). Original measurements/projects are never
  modified (CLAUDE.md rule #5).

## 7. Pass/fail criteria
Per frequency: PASS if |(measured sensitivity - nominal) / nominal| <= model
tolerance % (default +/-5 %). Overall: PASS iff all points PASS. Phase is
reported but not part of the verdict unless a model defines a phase tolerance.

## 8. Edge cases & error handling
- NVGate not running -> offer simulation or a clear "launch NVGate" message.
- Closed loop can't reach target (shaker limit / no signal) -> mark the point
  "level not reached", keep its measured value, flag it, continue.
- No signal on a channel / zero reference -> flag the point, do not divide by zero.
- Operator cancels mid-run -> stop generator + analyzer cleanly, no report.
- Report folder not writable -> fall back to the app's `.tmp/` and tell the user.

## 9. Lessons learned (living)
- Generator is **module 7**. Sine submodule activates via
  `SetSettingValue generator 225:1 state 1` (text IDN) or `7 225 2 1` (numeric).
  Frequency status readable via `GetStateValue 7 209 330`.
- Still to confirm on the bench: exact **frequency** and **level** setting IDNs
  of the Advanced Sine Generator, and the FRF result address
  (module/process/channel/reference). Centralised in `app/config.py` so only that
  file changes after the first live session.
- Reference channel set to 10 mV/(m/s²) makes it read acceleration directly, so
  the FRF (DUT raw V / ref m/s²) IS the sensitivity in V/(m/s²) — no separate
  acceleration calc needed. x1000 -> mV/(m/s²); x9.80665 -> mV/g.
