# Accelerometer Calibration

This app checks an accelerometer by shaking it through a range of frequencies and
comparing it to a trusted reference accelerometer. At the end it produces a
**Word calibration certificate** with a pass/fail result.

It is built for one-click use: pick the model, type the serial number, choose the
frequencies, press **Start**.

---

## Before you start (for a real calibration)

1. **NVGate** is open and in **connected mode**.
2. The **shaker amplifier** is switched on.
3. The **reference accelerometer** is on **Input 1**, the **accelerometer under
   test** is on **Input 2**, both mounted together on the shaker.
4. The shaker is driven from the analyzer's signal output (through the amplifier).

If NVGate is not running, the app still opens — but it will offer **Simulation
mode** (see below), which is for practice only, not a real calibration.

---

## How to use it

1. **Open the app** (double-click the icon).
2. **Model** — choose the accelerometer model from the list. Its nominal
   sensitivity and tolerance appear underneath.
3. **Serial number** — type the serial of the unit you are testing. It goes on
   the certificate.
4. **Operator** — type your name (optional, goes on the certificate).
5. **Frequencies** — tick the frequencies to test (all are ticked by default).
   Use **Select all** / **Clear** to change them quickly.
6. **Save report to** — where the certificate will be saved (your Documents
   folder by default). Click **Browse…** to change it.
7. Press **Start calibration**.

You'll see each frequency measured in turn, with its sensitivity and a
**PASS / FAIL** for that point. When it finishes, the overall result is shown and
the certificate is saved. Click **Open report** to view it.

A coloured banner at the top always tells you the mode:
- **LIVE — NVGate connected** — a real calibration.
- **SIMULATION** — practice only; the certificate is clearly marked as such.

---

## What PASS and FAIL mean

- **PASS** — the measured sensitivity is within the model's allowed tolerance
  (for example ±5%) at that frequency.
- **FAIL** — it is outside the tolerance.
- **CHECK** — the shaker could not hold the target level at that frequency, so
  the point needs a second look.

The unit passes overall only if **every** frequency passes.

---

## Adding or changing accelerometer models

The model list is a simple file you can edit. In the app, click **Edit list…**
next to the model dropdown — it opens the file. Each model has:

- a **name**,
- the **nominal sensitivity** and its unit (`mV/g` or `mV/(m/s^2)`),
- the **tolerance** (the allowed ± percentage for a pass),
- the **input type** (`IEPE` or `charge`).

Save the file, then click **Reload** in the app to see your changes. Your edits
do not affect anything else.

---

## First-time live setup (one-time, for the technician)

The app drives NVGate's sine generator and reads the result back. A few analyzer
addresses depend on your exact NVGate project and must be confirmed **once** on
the bench, then they are fixed:

- the generator **frequency** and **level** settings,
- the **FRF** (sensitivity) result address and the reference-level address.

These live in `app/config.py`, each clearly marked. Reveal an address in NVGate
with **SHIFT + right-click** on the setting. Until they are confirmed you can use
Simulation mode to try the whole workflow. The reference sensitivity is already
set to **10.0 mV/(m/s²)** as agreed.

---

## If something goes wrong

- **"NVGate not detected"** — make sure NVGate is open and in connected mode,
  then reopen the app (or use Simulation mode to practise).
- **A point shows CHECK** — the shaker couldn't reach the target level; check the
  amplifier gain and the mounting.
- **The report didn't save** — the app falls back to a `reports` folder next to
  itself and tells you where; check the chosen folder is writable.

The app never changes your measurements, projects, or NVGate settings files. The
certificate is always written as a new, dated file.
