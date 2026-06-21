# THD Calculator UI — Operator Guide

## What it does

Opens a window where you choose which NVGate spectrum to analyse and how many
harmonics to include. Click **Run THD** to calculate the Total Harmonic
Distortion — the result appears as a new scalar window inside NVGate. Once the
calculation is done you can click **Export to Excel** to save a full report
containing the spectrum values and chart, the harmonic table, the THD formula,
and measurement metadata.

Python must be installed on this PC (see First-time setup below).

---

## Before each use

- NVGate is open and **in connected mode**.
- At least one window in NVGate is showing an **FFT spectrum**.

---

## First-time setup (run these steps once, in order)

**Step 1 — Install Python packages**

Double-click **`setup.bat`**.
A black window opens and installs the packages the app needs (openpyxl,
python-dateutil). This takes about 30 seconds and only needs to be done once.
When it says "Done", close the window.

> If the window closes with an error, Python may not be installed on this PC.
> Download it from https://python.org (choose the Windows installer, tick
> "Add Python to PATH"), then try again.

**Step 2 (optional) — Add the tool to NVGate's Automation menu**

If you want to launch the tool from inside NVGate without leaving it:

1. Double-click **`install_to_nvgate.bat`** from this folder.
2. It creates a shortcut in NVGate automatically.
3. The tool then appears under **NVGate → Automation → Execute →
   "THD Calculator UI"**.

> Run `install_to_nvgate.bat` again if you ever move this folder to a
> different location.

---

## How to run

Either:
- **Double-click `launch_thd_ui.bat`** from this folder, or
- Use **NVGate → Automation → Execute → THD Calculator UI** (after Step 2
  above).

A window appears:

```
┌─────────────────────────────────────────┐
│  NVGate window:  [ Window2      ▼ ] [ ↺ ]│
│  Number of harmonics:  [ 5 ]            │
│  [ ▶  Run THD                         ] │
├─────────────────────────────────────────┤
│  Ready — 3 window(s): Window1, Window2… │
└─────────────────────────────────────────┘
```

1. **NVGate window** — select the window showing the spectrum you want to
   analyse. Click **↺** to refresh the list if you opened a new window in
   NVGate after launching this tool.

2. **Number of harmonics** — how many harmonics to include (H1 = fundamental,
   then H2, H3 … up to this number). Default is 5. Enter any whole number ≥ 2.

3. Click **▶ Run THD**.

The log area shows each step. When finished it shows the result, for example:

```
  * THD = 46.45 %

Window 'THD' opened in layout 'Layout1'.
Done.  THD = 46.45 %  — result visible in NVGate.
Click 'Export to Excel' to save the full report.
```

4. **(Optional) Click Export to Excel.**
   A file browser opens — choose where to save the file (the default name
   includes the window name). The file has three sheets:
   - **Metadata** — NVGate version, project, signal, frequency range, unit,
     measurement date, global level, and more.
   - **Spectrum** — every frequency bin and its amplitude, plus a chart
     showing the FFT line with harmonic positions marked.
   - **THD Analysis** — harmonics table, formula written out with actual
     values, and the final result in %.

---

## What you will see in NVGate

- **In the selected window** — a Harmonic marker appears at the highest peak,
  with one line per harmonic (H1 through Hn).
- **New scalar window "THD"** — opens in your current layout and displays the
  distortion value in percent, for example **46.45 %**.

You can run the tool again at any time (e.g. after changing the signal) and the
THD window will update.

---

## If something goes wrong

| What you see | What to do |
|---|---|
| setup.bat closes with an error | Python may not be installed — download from https://python.org (tick "Add Python to PATH"), then run setup.bat again |
| "Could not reach NVGate" at startup | Start NVGate, set it to connected mode, then click ↺ |
| Dropdown is empty after clicking ↺ | NVGate is not reachable — check it is running and connected |
| "is empty — open a spectrum there first" | Display a spectrum in the selected window first |
| "does not contain a spectrum" | The window shows something other than an FFT — select a different window |
| "Number of harmonics must be ≥ 2" | Enter a whole number of 2 or more in the harmonics field |
| "Warning: marker not added" | The THD is still calculated; the visual marker is optional |
| "Export to Excel" button is greyed out | Run THD first; the button activates after a successful calculation |
| "Export failed: …" in log | The file may be open in Excel — close it and try again |

---

## Formula

> **THD = √(H2² + H3² + … + Hn²) / H1 × 100**

H1 is the amplitude at the dominant peak. H2 … Hn are the amplitudes at its
harmonics, read directly from the spectrum.
