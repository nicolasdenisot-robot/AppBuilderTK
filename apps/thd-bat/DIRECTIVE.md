---
# ── Build manifest (read by tools/export_app.py) ─────────────────────────
app_name: thd-bat
export_target: source       # .bat launcher — no exe needed for this variant
entry_point: app/main.py
helpers_used:
  - connection
# requirements are listed in requirements.txt
---

# DIRECTIVE — thd-bat

> THD calculator delivered as a `.bat` file. A companion app (`thd-exe`) will
> deliver the same logic as a standalone `.exe`.

## 1. Objective
Connect to a running NVGate session, read the spectrum from Window2, find
the dominant frequency (fundamental), place a Harmonic marker in NVGate for
visual reference, compute Total Harmonic Distortion (THD) from the first 5
harmonics, and display the result in a new scalar window inside NVGate.

## 2. Operator & run context
- **Who runs it:** line operator — double-clicks `launch_thd.bat`
- **Live or offline:** live analyzer (NVGate must be running and in connected mode)
- **Capability layer:** live control (`pynvdrive` TCP port 3000)

## 3. Inputs
| Name | IDN / source | Value / range |
|------|--------------|---------------|
| Spectrum source | Window2 (first trace) | FFT spectrum, linear frequency axis |
| Number of harmonics | hard-coded constant | 5 |

## 4. Steps (the deterministic flow)
1. Check NVGate is reachable (port 3000); exit with a plain message if not.
2. Call `GetWindowTraces('Window2')` → get module/process/channel of the spectrum.
3. Call `CreateResultEx` + `GetResultEx` to download the spectrum data.
4. Parse `result.xreg` (frequency axis: start, stop) and `result.rvec.data`
   (amplitudes). If CVEC, compute magnitude per bin.
5. Find the bin with the maximum amplitude → fundamental frequency f0.
6. Call `GetWindowDisplayZone('Window2')` to get the display-zone type.
7. Send custom `AddHarmonicMarker` command to Window2 at f0, 5 harmonics.
8. Compute harmonic amplitudes H1–H5 from the spectrum data at f0, 2f0 … 5f0
   (nearest-bin lookup).
9. THD = √(H2²+H3²+H4²+H5²) / H1 × 100 %
10. Create a TCP scalar result channel (module=498, process=182 / NVC SCALAR)
    with the THD value in %, inject it into NVGate.
11. Open a new NVGate window named "THD" in the current layout to show the value.

## 5. Computation
- **NVGate-native:** spectrum data fetched via `GetResultEx` (no recomputation).
- **Python:** find-max, nearest-bin lookup, THD formula — all deterministic maths.
  NVGate does not expose a THD function, so Python is the correct place for this.

## 6. Outputs
- **Harmonic marker** visible in Window2 at f0 (5 harmonics shown).
- **New scalar window "THD"** in the current NVGate layout, displaying e.g. `5.32 %`.
- **Console printout** with f0, H1–H5, and THD value.

## 7. Pass/fail criteria
None — this is a calculation and display tool, not a pass/fail station.

## 8. Edge cases & error handling
| Situation | Behaviour |
|-----------|-----------|
| NVGate not running | Exit with plain error message, no crash |
| Window2 empty / no trace | Exit with plain error message |
| Result has no frequency axis (XREG) | Exit with plain error message |
| 5th harmonic beyond spectrum range | Warning printed; THD computed with bins within range |
| Fundamental amplitude = 0 | Exit with plain error message |
| Marker command fails (e.g. no Harmonic licence) | Warning only; THD calculation continues |
| THD window already open | Reuses existing window (not an error) |

## 9. Lessons learned (living)
- `AddHarmonicMarker` and `SetHarmonicMarkerParameters` are in the NVDrive
  manual (§3.2.9 / §3.2.30) but NOT yet wrapped as Python classes in pynvdrive.
  They are implemented here as local `CommandAction` subclasses.
- `CreateTCPResultChannel` (process=182 = NVC SCALAR, module=498) is the correct
  path to inject a computed scalar back into NVGate for display.
- The `Percentage` / `Percent` magnitude key exists in orosunit.ini and is the
  correct one for a % value injected via TCP result channel.
- `GetWindowTraces` returns `cmd.list_result_format_and_description`; individual
  fields: `.module_id`, `.process_id`, `.channel_number`, `.reference_channel_number`.
- `GetResultEx` returns `cmd.result`; spectrum is in `result.rvec.data` (linear
  amplitudes) with frequency axis in `result.xreg` (start/stop in Hz).
- **TCP scalar injection — unit pitfall:** `check_unit_exist` in TCPRESULT calls
  `get_unit(magnitude_key=..., magnitude_name=physical_quantity, unit_name=..., unit_label=...)`.
  If BOTH magnitude info AND unit_name are provided, it tries to look up the unit_name
  string in NVGate's live unit list — and the string NVGate uses (e.g., `"Percent"`)
  may not match what `orosunit.ini` section names suggest. Safe pattern: set
  `physical_quantity=''`, `unit_name=None`, `unit_label=None` and only provide
  `magnitude_key`. This hits the "SI unit" code path: no lookup, no crash.
  Pass the value in the display unit (e.g., 46.45 for 46.45%) — pynvdrive converts
  to SI (÷100) before sending; NVGate then re-displays correctly in %.
