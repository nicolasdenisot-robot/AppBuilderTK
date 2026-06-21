---
app_name: thd-ui
version: 1.0
display_name: THD Calculator UI
export_target: exe
entry_point: app/main.py
helpers_used:
  - connection
---

# DIRECTIVE — thd-ui

> Same THD logic as `thd-bat`, with a Tkinter UI instead of a console script.
> Ships in two delivery forms: standalone `.exe` (no Python needed) and
> `.bat` + Python source (easier to update). Both are built and validated.

## 1. Objective
Open a small window where the user selects which NVGate spectrum window to
analyse and how many harmonics to use, then clicks Run to compute THD.
Results appear in NVGate exactly as in `thd-bat`. Optionally, the user can
click "Export to Excel" to save a 3-sheet report (Metadata, Spectrum with
chart, THD Analysis with formula).

## 2. Operator & run context
- **Who runs it:** engineer or operator. Two delivery forms:
  - **Exe form** (`thd-ui-v1.0-exe/`): double-clicks `thd-ui.exe` — no Python needed.
  - **Source form** (`thd-ui-v1.0-source/`): runs `setup.bat` once, then double-clicks
    `launch_thd_ui.bat`. Easier to update (send changed `.py` file, no rebuild).
  Both forms optionally register in NVGate Automation via `install_to_nvgate.bat`.
- **Live or offline:** live (NVGate must be running and connected)
- **Capability layer:** live control (`pynvdrive`)
- **UI stack:** Tkinter (built into Python, no extra install, packages to `.exe`)

## 3. Inputs
| Name | Source | Default |
|------|--------|---------|
| Spectrum window | Dropdown populated from `GetWindowNameList()` | Window2 |
| Number of harmonics | Integer entry field (≥ 2) | 5 |

## 4. Steps (deterministic flow)
1. On startup: call `GetWindowNameList()` in a background thread, populate
   the dropdown. Disable Run until NVGate is confirmed reachable.
2. User selects window + harmonics → clicks Run.
3. Validate inputs (window not empty, harmonics ≥ 2).
4. Run `run_thd_calculation(window, num_harmonics, log)` in a background thread
   so the UI stays responsive. Progress lines appear in the log area.
5. Same internal pipeline as `thd-bat`: GetWindowTraces → GetResultEx →
   find f0 → AddHarmonicMarker → compute H2…Hn → THD formula → inject scalar
   → AddWindowResult.
6. On completion: re-enable buttons, show final THD value in log area.

## 5. Computation
Identical to `thd-bat`. THD = √(H2²+H3²+…+Hn²) / H1 × 100 %.

## 6. Outputs
- Harmonic marker in the selected NVGate window.
- New scalar window "THD" in the current NVGate layout.
- Progress log visible in the UI while the calculation runs.
- (Optional) Excel report saved on demand via "Export to Excel" button.

## 6a. Excel report structure (3 sheets)
| Sheet | Content |
|-------|---------|
| Metadata (first, active on open) | NVGate version + hardware, project name, database path, layout, signal/channel name, analysis name, result name, physical quantity, unit, spectral window, result type, measurement status, measurement date, global RMS level, A-weighted level, tacho, spectrum type, freq range, number of lines, resolution, peak amplitude, THD result, export date. |
| Spectrum | Columns: Frequency (Hz) / Amplitude / Harmonic Freq / Harmonic Amplitude. ScatterChart with the full spectrum as a line and harmonic positions as diamond markers. Unit from metadata is shown in chart axis label. |
| THD Analysis | Metadata summary (window, date, harmonics), harmonic table (H1…Hn with frequency and amplitude), THD formula (symbolic + numeric substitution), THD result in %. |

## 7. Edge cases & error handling
| Situation | Behaviour |
|-----------|-----------|
| NVGate not running at startup | Run disabled; message in log; ↺ to retry |
| NVGate disconnects mid-run | Error shown in log; buttons re-enabled |
| Selected window has no trace | Error in log |
| Harmonics field empty or < 2 | Validation error before run starts |
| Highest harmonic beyond spectrum | Warning in log; calculation continues |

## 8. Lessons learned (living)
- Inherits all lessons from `thd-bat/DIRECTIVE.md` (TCP scalar injection unit
  pitfall, AddHarmonicMarker custom command, etc.).
- Tkinter is NOT thread-safe: all UI updates from the background worker thread
  must go through `self.after(0, callback)`. The `_safe_log()` method handles this.
- `GetWindowNameList()` (with empty layout argument) returns all open windows
  across all layouts. `cmd.value` is a list of strings.
- The Run button is disabled on startup and re-enabled only after `_on_windows_loaded`
  confirms NVGate is reachable.
- The "Export to Excel" button is disabled until a successful THD run stores results
  in `self._last_calc`. A new Run clears `_last_calc` and disables the button again.
- `run_thd_calculation` now returns `(dict, None)` on success (not just `(float, None)`).
  The dict carries all data needed for the Excel export (amplitudes, freqs, harmonics).
- `graphicalProperties.line.noFill = True` correctly suppresses the connecting line
  between harmonic diamond markers in the ScatterChart (tested with openpyxl 3.1.5).
- `openpyxl` added to requirements.txt.
- Metadata gathered with `_gather_metadata()` inside the existing connected session —
  no second TCP connection. Uses `GetCurrentProjectName`, `GetDatabasePath`, `GetNVGateInfo`
  (all wrapped in try/except; a failure in one does not abort the export).
- `result.head`: name, physical_quantity, unit_name/label, magnitude_key, result_type,
  measure_status, weighting_window, is_complex.
- `result.info`: date (converted from Win32 epoch to local datetime), global_level,
  weighted_global_level, tacho.
- `result.xreg`: n_octave (0=linear FFT), unit_label.
- `trace.analysis_fullname`: human-readable "FFT1: AvgSpc" built from module+process ID maps.
- Coded integer values (result_type, measure_status, weighting_window, n_octave) are decoded
  to human-readable strings via lookup dicts at top of file; raw code shown in parentheses.
- Metadata sheet is set as `wb.active` so it opens first in Excel.
- Rows with empty/zero values (tacho, A-weighted level when unused) are suppressed.
- Unit label applied to chart Y-axis title from metadata.
- Both delivery forms are fully built and validated:
  `python tools/export_app.py thd-ui --target exe` and `--target source`.
  Folder names include the target suffix: `thd-ui-v1.0-exe/`, `thd-ui-v1.0-source/`.
  Both can coexist in `dist/` without overwriting each other.
- Form-specific READMEs are required for this app: `README-exe.md` references
  `thd-ui.exe`; `README-source.md` references `launch_thd_ui.bat` and `setup.bat`.
  Sharing one `README.md` across both forms led to broken instructions (e.g.
  `launch_thd_ui.bat` referenced in a package that only contains an `.exe`).
  The export tool picks `README-<target>.md` first, falls back to `README.md`.
- `pynvdrive/__pycache__` must be excluded from source delivery. Fixed in
  `build_staging()` with `shutil.ignore_patterns("__pycache__", "*.pyc")` applied
  to both `pynvdrive` and `oros_helpers` copies.
