---
app_name: thd-pro
version: 1.1
display_name: THD Analyzer
export_target: exe
entry_point: app/main.py
logo: oros
helpers_used:
  - connection
---

# DIRECTIVE — thd-pro

> Same THD calculation as `thd-ui`, with a modern PySide6/Qt UI (light theme).
> Results are shown in the app window — not in NVGate. A harmonic marker is
> still placed on the NVGate spectrum for visual reference.

## 1. Objective
A modern, customer-facing THD calculator. The operator selects a NVGate
spectrum window and the number of harmonics, then clicks Run. The app computes
THD and displays four results directly in its window:
- THD (%)
- THD (dB)
- H1 fundamental frequency (Hz)
- H1 fundamental amplitude

An "Export to Excel" button saves the full 3-sheet report (same structure as
thd-ui, with THD dB added).

Optionally, the operator can enter a **THD limit (%)**. When set, the app shows a
large green **PASS** / red **FAIL** banner (THD ≤ limit = PASS) and includes the
limit and verdict in the Excel report. Leaving the limit blank keeps the app a
pure calculator with no verdict.

## 2. Operator & run context
- **Who runs it:** customer operator — double-clicks the .exe or launches from
  NVGate Automation → Execute menu.
- **Delivery form:** standalone `.exe` (customer PC, no Python required)
- **Live or offline:** live (NVGate must be running and connected)
- **Capability layer:** live control (`pynvdrive`)
- **UI stack:** PySide6/Qt, light theme (white cards, blue accent #1565c0)

## 3. Inputs
| Name | Source | Default |
|------|--------|---------|
| Spectrum window | Dropdown populated from `GetWindowNameList()` | Window2 |
| Number of harmonics | Custom `HarmonicsSelector` +/− stepper (editable field), clamped 2–20 | 5 |
| THD limit (%) | `QLineEdit#LimitInput` with `QDoubleValidator`; optional — blank = no verdict | (blank) |

## 4. Steps (deterministic flow)
1. On startup: load NVGate window list in a background QThread; disable Run
   until NVGate is confirmed reachable.
2. User selects window + harmonics → clicks Run.
3. Validate inputs.
4. Run calculation in a background QThread (signals/slots keep UI responsive).
   Status bar shows progress messages.
5. Internal pipeline: GetWindowTraces → GetResultEx → find f0 →
   AddHarmonicMarker → compute H2…Hn → THD formula.
6. On completion: display THD%, THD dB, H1 freq, H1 amplitude in result cards.
   Enable "Export to Excel".
7. If a THD limit was entered: compare THD ≤ limit and show the PASS/FAIL banner;
   stamp the limit + verdict onto the result for the Excel report. No limit → no
   banner.

## 5. Computation
THD = √(H2²+H3²+…+Hn²) / H1 × 100 %
THD(dB) = 20 × log₁₀(THD / 100)

## 6. Outputs
- 4 metric cards in the UI showing THD%, THD dB, H1 frequency, H1 amplitude.
- Optional PASS/FAIL verdict banner (green/red) when a THD limit is set.
- Harmonic marker placed on the NVGate spectrum window (visual aid only).
- (Optional) Excel report: 3 sheets — Metadata, Spectrum, THD Analysis.
  THD dB added to both Metadata and THD Analysis sheets. When a limit is set, the
  THD limit (%) and the Verdict are added to both sheets (verdict colored on the
  THD Analysis sheet).

## 7. Pass/fail criteria  (optional — v1.1)
- Single global THD limit only. No per-harmonic or H1 frequency/amplitude limits.
- **PASS when measured THD ≤ limit** (the limit value itself passes); FAIL otherwise.
- The check is purely deterministic Python on the already-computed THD — NVGate has
  no THD-native result, so nothing is reimplemented (Tier-1 rule respected).
- If the limit field is blank/invalid/≤ 0, no verdict is shown (pure calculator mode).

## 8. Edge cases & error handling
| Situation | Behaviour |
|-----------|-----------|
| NVGate not running at startup | Run disabled; status bar message; ↺ to retry |
| NVGate disconnects mid-run | Error shown in status bar; buttons re-enabled |
| Selected window has no trace | Error shown in status bar |
| Harmonics out of range | `HarmonicsSelector` clamps to 2–20 |
| THD calc fails (NVGate down, empty window, error) | No verdict shown — only the error in the status bar; never a false PASS/FAIL |
| Highest harmonic beyond spectrum | Warning in status bar; calculation continues |

## 9. Lessons learned (living)
- PySide6 QThread with Signal/emit is cleaner than threading.Thread for Qt apps:
  `done_signal = Signal(dict)` then `self.done_signal.emit(result)` in run().
- All UI updates from a worker thread must go through signals — never update
  QLabel.setText() directly from a non-main thread.
- QSS `background: transparent` is required on child QLabel inside a styled
  QFrame, otherwise the label inherits the default QWidget background and
  obscures the frame's white background.
- QComboBox drop-down arrow styling needs `QComboBox::drop-down { border: none }`
  to avoid a double-border artefact on Windows.
- Harmonics input is a custom `HarmonicsSelector` (+/− stepper with an editable
  field, clamped 2–20) — NOT a QSpinBox. (Earlier notes/spec said QSpinBox; that
  drifted from the code and was corrected on 2026-06-28 via /explore-codebase.)
- THD dB: 20 * math.log10(thd_pct / 100.0). Guard against thd_pct == 0.
- No scalar injection into NVGate (inject_scalar_percent removed entirely).
  No AddWindowResult call. The harmonic marker (AddHarmonicMarker) is kept.
- Brand logos live in `shared/assets/logos/<brand>/logo_color.png` (light theme)
  and `logo_white.png` (dark theme). Declare the brand with `logo:` in
  DIRECTIVE.md. The export tool copies both files into staging automatically.
  In `main.py`, use `_LOGO_BRAND` / `_LOGO_VARIANT` constants + the `_logo_path()`
  helper (see CLAUDE.md §10 for the canonical pattern).

### Scoping note: pass/fail THD limit — 2026-06-28 (built, v1.1)
- Reused the existing colored-panel idea: the verdict banner uses the same green
  (`#2e7d32`) / red (`#c62828`) family as `_STATUS_STYLES` success/error.
- The verdict is computed on the main thread in `_on_run_success` (the THD number
  already exists there) — no extra worker thread needed.
- Limit + verdict are added to `self._last_calc` so the unchanged export path
  (`export_to_excel`) picks them up via `data.get(...)`; absent keys = no verdict.
- Testing gotcha: a Qt widget's `isVisible()` is False until its top-level window
  is `show()`n. To verify show/hide headless (offscreen), check `isHidden()` instead.
- Reuse opportunity still open (rule #6): `export_to_excel` and result fetching are
  implemented inline; `shared/oros_helpers/{export,results,report}.py` are unused.
