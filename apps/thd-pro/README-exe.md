# THD Analyzer — Setup Guide (Standalone)

This package contains a single self-contained file: **`thd-pro.exe`**.
No Python installation is needed.

---

## First-time setup (once only)

Run **`install_to_nvgate.bat`** to add the app to NVGate's
Automation → Execute menu.  Right-click → Run as Administrator if prompted.

---

## How to launch

- **Double-click `thd-pro.exe`**, or
- Open NVGate → **Automation → Execute → THD Analyzer**.

NVGate must be **open and in connected mode** before launching.

---

## How to use

1. The app starts and connects to NVGate automatically.
   The window list is filled in.
2. Select the **FFT spectrum window** to analyse from the dropdown.
   Click **↺** to refresh the list if needed.
3. Set the **number of harmonics** (minimum 2, default 5).
   Type a value directly or use the **−** / **+** buttons.
4. Click **▶ Run THD**.
5. Results appear in the four cards:

   | Card | What it shows |
   |------|---------------|
   | **THD (%)** | Total distortion as a percentage |
   | **THD (dB)** | The same distortion in decibels |
   | **H1 — Fundamental frequency** | Main peak frequency (Hz) |
   | **H1 — Fundamental amplitude** | Main peak amplitude (scientific notation) |

   A harmonic marker is also placed on the NVGate spectrum window.
6. Click **Export to Excel** to save a detailed three-sheet report.

---

## If the app cannot connect to NVGate

The status area will say *"Could not reach NVGate"*. Check that:

- NVGate is open and the analyser is connected.
- NVGate is in **connected mode** (not standalone / demo mode).

Then click **↺** to retry — no need to restart the app.

---

## Notes

- The app finds the fundamental automatically by locating the highest peak
  in the spectrum.  Make sure the dominant peak is the fundamental.
- If a harmonic falls outside the spectrum range, the app warns you but
  still completes the calculation using the harmonics that are in range.
