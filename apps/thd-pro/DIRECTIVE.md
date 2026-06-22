---
app_name: thd-pro
version: 1.0
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
| Number of harmonics | QSpinBox, integer ≥ 2 | 5 |

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

## 5. Computation
THD = √(H2²+H3²+…+Hn²) / H1 × 100 %
THD(dB) = 20 × log₁₀(THD / 100)

## 6. Outputs
- 4 metric cards in the UI showing THD%, THD dB, H1 frequency, H1 amplitude.
- Harmonic marker placed on the NVGate spectrum window (visual aid only).
- (Optional) Excel report: 3 sheets — Metadata, Spectrum, THD Analysis.
  THD dB added to both Metadata and THD Analysis sheets.

## 7. Edge cases & error handling
| Situation | Behaviour |
|-----------|-----------|
| NVGate not running at startup | Run disabled; status bar message; ↺ to retry |
| NVGate disconnects mid-run | Error shown in status bar; buttons re-enabled |
| Selected window has no trace | Error shown in status bar |
| Harmonics field < 2 | QSpinBox minimum enforces ≥ 2 |
| Highest harmonic beyond spectrum | Warning in status bar; calculation continues |

## 8. Lessons learned (living)
- PySide6 QThread with Signal/emit is cleaner than threading.Thread for Qt apps:
  `done_signal = Signal(dict)` then `self.done_signal.emit(result)` in run().
- All UI updates from a worker thread must go through signals — never update
  QLabel.setText() directly from a non-main thread.
- QSS `background: transparent` is required on child QLabel inside a styled
  QFrame, otherwise the label inherits the default QWidget background and
  obscures the frame's white background.
- QComboBox drop-down arrow styling needs `QComboBox::drop-down { border: none }`
  to avoid a double-border artefact on Windows.
- `QSpinBox.setMinimum(2)` enforces the ≥ 2 constraint without a separate
  validator — simpler than the Tkinter validatecommand approach in thd-ui.
- THD dB: 20 * math.log10(thd_pct / 100.0). Guard against thd_pct == 0.
- No scalar injection into NVGate (inject_scalar_percent removed entirely).
  No AddWindowResult call. The harmonic marker (AddHarmonicMarker) is kept.
- Brand logos live in `shared/assets/logos/<brand>/logo_color.png` (light theme)
  and `logo_white.png` (dark theme). Declare the brand with `logo:` in
  DIRECTIVE.md. The export tool copies both files into staging automatically.
  In `main.py`, use `_LOGO_BRAND` / `_LOGO_VARIANT` constants + the `_logo_path()`
  helper (see CLAUDE.md §10 for the canonical pattern).
