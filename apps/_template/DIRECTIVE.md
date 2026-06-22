---
# ── Build manifest ───────────────────────────────────────────────────────
# Fields read by tools/export_app.py: version, display_name, export_target,
# entry_point, logo. The others below are informational only.
app_name: _template         # informational; the tool uses the folder name
version: 1.0                # bumped for each new delivery; used in folder name
display_name: My App Name   # shown in NVGate Automation menu; used in bat names
export_target: exe          # "exe" (self-contained, no Python on operator PC)
                            # "source" (Python source + launcher; needs Python)
entry_point: app/main.py
logo: oros                  # brand folder under shared/assets/logos/ (see CLAUDE.md §10)
helpers_used:               # informational; the tool always vendors the whole
  - connection              #   oros_helpers package regardless of this list
  - results
# requirements are listed in requirements.txt
---

# DIRECTIVE — <app name>

> The spec AND living memory for this app. Written during the 6-stop interview
> (CLAUDE.md §5) and updated as you learn. **Do not overwrite or discard without
> asking the user** (CLAUDE.md rule #5).

## 1. Objective
_One or two plain sentences: what does this app do, and for whom?_

## 2. Operator & run context
- **Who runs it:** _the engineer themselves / a line operator who just clicks_
- **Live or offline:** _live analyzer (NVGate running) / saved files (offline)_
- **Capability layer:** _live control (pynvdrive) / file access (orostk) / both_
- **UI stack:** _none (console) / Tkinter / PySide6 / Streamlit — see CLAUDE.md §5 stop #5_
- **Delivery form:** _exe (no Python needed) / source (Python required) / both — see CLAUDE.md §5 stop #6_
- **Launch point:** _double-click / NVGate Automation → Execute / scheduled task_

## 3. Inputs
_Settings to apply, channels, files, thresholds, operator entries, etc._

| Name | IDN / source | Value / range |
|------|--------------|---------------|
|      |              |               |

## 4. Steps (the deterministic flow)
_The exact, repeatable sequence the app performs. This is what becomes code._
1.
2.
3.

## 5. Computation
- **NVGate-native (preferred):** _which results are fetched (module/process/channel)_
- **Python library (only if needed):** _name + why NVGate can't do it_

## 6. Outputs
- **Where results appear:** _in NVGate / custom UI_ (decision, with reason)
- **Exports:** _Excel / report / CSV — path & format_

## 7. Pass/fail criteria (if any)
_Exact, deterministic rules. No ambiguity._

## 8. Edge cases & error handling
_NVGate not running, no signal, out-of-range, operator cancels, etc._

## 9. Lessons learned (living)
_Record discoveries here so the next session/app benefits: setting IDNs, quirks
(e.g. "setting X only applies after Run"), timing, fixes for errors you hit._
-
