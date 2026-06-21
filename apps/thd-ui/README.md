# THD Calculator — with interface

## What it does

Opens a small window where you choose which NVGate spectrum to analyse and
how many harmonics to include. Click **Run THD** and the tool calculates the
Total Harmonic Distortion and sends the result back into NVGate. Optionally,
click **Export to Excel** to save a full report (spectrum values and chart,
harmonics table, THD formula, and measurement metadata).

---

## First-time setup (do this once)

You have two ways to launch the tool.

### Option A — Double-click directly

No setup needed. Just double-click `launch_thd_ui.bat` from the folder where
you installed the app.

### Option B — Launch from NVGate (Automation → Execute)

This lets you start the tool without leaving NVGate.

**One-time step:** double-click `install_to_nvgate.bat` from the app folder.
It creates a shortcut in NVGate's Links folder automatically.  
After that, the tool appears in NVGate under **Automation → Execute** as
**"THD Calculator UI"**.

> If you ever move the app to a different folder, run `install_to_nvgate.bat` again.

---

## Before each use

- NVGate is open and **in connected mode**.
- At least one window in NVGate is showing an **FFT spectrum**.

---

## How to use it

**Start the tool** (double-click `launch_thd_ui.bat`, or use NVGate's Automation menu).
A window like this appears:

```
┌─────────────────────────────────────────┐
│  NVGate window:  [ Window2      ▼ ] [ ↺ ]│
│  Number of harmonics:  [ 5 ]            │
│  [ ▶   Run THD                        ] │
├─────────────────────────────────────────┤
│  Ready — 3 window(s): Window1, Window2… │
└─────────────────────────────────────────┘
```

1. **NVGate window** — the dropdown lists every window currently open in
   NVGate. Select the one that shows the spectrum you want to analyse.
   Window2 is selected by default.
   Click **↺** at any time to refresh the list (useful if you opened a new
   window in NVGate after launching this tool).

2. **Number of harmonics** — how many harmonics to include in the calculation
   (H1 = fundamental, H2, H3 … up to this number). The default is 5.
   Enter any whole number ≥ 2.

3. Click **▶ Run THD**.

The log area below shows each step as it runs. When finished it shows the
result, for example:

```
  * THD = 46.45 %

Window 'THD' opened in layout 'Layout1'.
Done.  THD = 46.45 %  — result visible in NVGate.
Click 'Export to Excel' to save the full report.
```

4. (Optional) Click **Export to Excel** to save a full report.

A file browser opens. Choose where to save the file — the default name is
`THD_Window2.xlsx` (or whatever window you used). The file is ready in a
few seconds.

---

## What is in the Excel file

When you click "Export to Excel" after a successful run, the file has three sheets:

The file opens on the **Metadata** sheet, which gives the full context of the
measurement. From there, two more sheets hold the data and the analysis.

**Sheet "Metadata"** — everything about the measurement, collected automatically
from NVGate at the moment you click Export:
- NVGate version and hardware (type, serial number)
- Project name and database location
- Signal and channel name, analysis type (e.g. FFT1: AvgSpc)
- Physical quantity and unit (e.g. Acceleration, m/s²)
- Spectral window (e.g. Hann), spectrum type (linear / octave-band)
- Frequency range, number of lines, resolution
- Measurement date, global RMS level, tacho speed (if applicable)
- THD result and export date

**Sheet "Spectrum"** — a table with every frequency bin and its amplitude, plus
a chart showing the full FFT spectrum as a line. The harmonic positions are
marked on the chart as diamond-shaped points.

**Sheet "THD Analysis"** — a summary table:
- Which NVGate window was used, how many harmonics, and the date.
- A table listing H1 (fundamental) through Hn — frequency in Hz and amplitude
  for each harmonic.
- The THD formula written out symbolically, then with the actual numbers
  substituted in.
- The final THD result in %.

---

## What you will see in NVGate

- **In the selected window** — a Harmonic marker appears at the highest peak,
  with one line for each harmonic (H1 through H5 if you used the default).
- **New scalar window "THD"** — opens in your current layout and displays the
  distortion value in percent, for example **46.45 %**.

You can run the tool again at any time (e.g. after changing the signal) and
the THD window will update.

---

## If something goes wrong

| What you see | What to do |
|---|---|
| "Could not reach NVGate" at startup | Start NVGate, set it to connected mode, then click ↺ |
| Dropdown is empty after clicking ↺ | NVGate is not reachable — check it is running and connected |
| "is empty — open a spectrum there first" | The selected window has no trace; display a spectrum in it |
| "does not contain a spectrum" | The window is showing something other than an FFT (e.g. a time signal) |
| "Number of harmonics must be ≥ 2" | Enter a whole number of 2 or more in the harmonics field |
| "Warning: marker not added" | The THD is still calculated; the visual marker is optional |
| "Export to Excel" button is greyed out | Run THD first; the button activates after a successful calculation |
| "Export failed: …" in log | The file may be open in Excel already — close it and try again |

---

## Formula

> **THD = √(H2² + H3² + … + Hn²) / H1 × 100**

H1 is the amplitude at the dominant peak. H2 … Hn are the amplitudes at its
harmonics, read from the same spectrum.
