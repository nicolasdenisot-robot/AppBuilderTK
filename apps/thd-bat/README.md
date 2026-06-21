# THD Calculator — Operator Instructions

## What this tool does

This tool reads the spectrum currently displayed in **Window 2** of NVGate,
automatically finds the main frequency (the highest peak), and calculates the
**Total Harmonic Distortion (THD)**.

The result appears directly inside NVGate:
- A **Harmonic marker** is added on the spectrum in Window 2, showing the 5
  harmonics of the main frequency.
- A **new scalar window called "THD"** opens in your current layout, displaying
  the distortion value in percentage (for example: **46.45 %**).

---

## Before you start

Make sure the following conditions are met:

1. **NVGate is open** and the analyzer is in connected mode.
2. **Window 2 contains a spectrum** (FFT) that is already running or has
   already been acquired. The tool reads whatever is currently displayed —
   it does not start or stop the analyzer.
3. **Python is installed** on this computer (it runs automatically when you
   double-click the launcher — you do not need to open Python yourself).

---

## How to run

**Double-click the file:** `launch_thd.bat`

A black console window will open and display the steps as they run:

```
=======================================================
  THD Calculator — thd-bat
=======================================================

Connecting to NVGate...

[1] Reading trace info from 'Window2'...
[2] Downloading spectrum data...
[3] Finding fundamental frequency...
      f0 = 52.50 Hz
[4] Adding Harmonic marker...
[5] Extracting harmonic amplitudes...
[6] Computing THD...

  ★  THD = 46.45 %

[7] Sending THD result to NVGate...
      Window 'THD' opened.

Done.
```

The window stays open after finishing so you can read the result.
Press any key (or click the X) to close it.

---

## What you will see in NVGate

### In Window 2 — the spectrum

A **Harmonic marker** appears at the main frequency peak.
It shows 5 vertical dashed lines: the fundamental (H1) and its 4 harmonics
(H2, H3, H4, H5). This is for visual reference only — the marker was placed
automatically at the frequency with the highest amplitude.

### New window — "THD"

A new scalar window named **THD** opens in your current NVGate layout.
It displays the calculated distortion value in percentage, for example:

> **46.45 %**

This window updates every time you re-run the tool.
If the window already exists from a previous run, it is reused.

---

## If something goes wrong

The console window will display a clear error message explaining what happened.
Common situations:

| Message | What to do |
|---------|-----------|
| *Cannot reach NVGate* | Make sure NVGate is open and in connected mode, then try again. |
| *Window2 is empty — no trace found* | Open a spectrum in Window 2 first, then re-run. |
| *The result in Window2 is not a spectrum* | Make sure Window 2 is showing an FFT spectrum (not a time signal, waterfall, etc.). |
| *Fundamental amplitude is zero* | The spectrum appears flat — check that the signal is active. |
| *WARNING: Could not add Harmonic marker* | The THD value is still calculated and displayed. The marker is optional. |

---

## Formula used

> **THD = √(H2² + H3² + H4² + H5²) / H1 × 100**

where H1 is the amplitude of the main frequency and H2–H5 are the amplitudes
at the 2nd, 3rd, 4th, and 5th harmonics, all read from the spectrum in Window 2.
