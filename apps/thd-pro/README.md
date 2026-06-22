# THD Analyzer

Calculates the Total Harmonic Distortion of a signal displayed in NVGate,
and shows the results directly in the application window.

---

## What it does

1. Reads the FFT spectrum from a NVGate window you choose.
2. Finds the fundamental frequency (H1) — the highest peak.
3. Measures the amplitude of each harmonic (H2, H3, …, up to the number you set).
4. Computes THD using the standard formula.
5. Displays four results on screen:

   | Result | What it means |
   |--------|---------------|
   | **THD (%)** | How much distortion as a percentage of the fundamental |
   | **THD (dB)** | The same distortion expressed in decibels |
   | **H1 — Fundamental frequency** | The frequency of the main peak (Hz) |
   | **H1 — Fundamental amplitude** | The amplitude of the main peak |

6. Places a harmonic marker on the NVGate spectrum (shows H1, H2, H3… visually).
7. Lets you export a full Excel report with one click.

---

## Before you start

- NVGate must be **open and in connected mode** (the analyzer is connected).
- The spectrum window you want to analyse must be **visible in NVGate** and
  contain a live or paused FFT spectrum.

---

## How to use it

1. **Launch the app** — double-click `THD Analyzer.exe` (or launch from
   NVGate → Automation → Execute).
2. The app connects to NVGate automatically. The window list is filled in.
3. **Select the NVGate window** that contains the FFT spectrum you want to
   analyse. If you don't see the right window, click **↺** to refresh the list.
4. **Set the number of harmonics** — how many harmonic peaks to include in the
   THD calculation (minimum 2, default 5).
5. Click **▶ Run THD**. The status bar at the bottom shows progress.
6. Results appear in the four boxes. A harmonic marker is added to the NVGate
   spectrum.
7. Click **Export to Excel** to save a detailed report. Choose where to save
   the file. The report has three sheets:
   - **Metadata** — NVGate version, project, signal details, FFT parameters,
     THD result.
   - **Spectrum** — full frequency/amplitude table with a chart showing the
     spectrum and the harmonic positions.
   - **THD Analysis** — harmonic table, formula, THD in % and dB.

---

## If the app cannot connect to NVGate

The status bar will say *"Could not reach NVGate"*. Check that:

- NVGate is open.
- NVGate is in **connected mode** (not standalone / demo mode).
- The analyzer is connected to the PC.

Then click **↺** to try again — you do not need to restart the app.

---

## Notes

- The app finds the fundamental automatically by looking for the highest-amplitude
  bin in the spectrum. Make sure the signal is clean and the dominant peak is
  the fundamental.
- If a harmonic frequency falls outside the spectrum range, the app warns you
  in the status bar but still completes the calculation with the harmonics that
  are within range.
- Running THD again clears the previous results and starts fresh.
