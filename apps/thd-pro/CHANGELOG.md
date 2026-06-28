# Changelog — THD Analyzer (thd-pro)

Version history for this app. Newest first. Dates are when the version was packaged.
Operator-facing summaries also ship inside each delivery folder as `WHATS-NEW.txt`.

## v1.1 — 2026-06-28

**New — optional pass/fail check.** The operator can enter a **THD limit (%)**.
After Run, the app shows a large green **PASS** / red **FAIL** banner — PASS when
the measured THD is at or below the limit. Leaving the limit blank keeps the v1.0
behaviour (THD number only, no verdict).

**New — limit & verdict in the Excel report.** When a limit is set, the THD limit
and the PASS/FAIL verdict are added to the Metadata and THD Analysis sheets (the
verdict is colour-coded on the THD Analysis sheet).

**Unchanged / compatibility.** No breaking changes. With no limit entered, v1.1 is
identical to v1.0.

**Docs corrected (internal).** The spec said the harmonics input was a QSpinBox;
it is actually a custom +/− stepper clamped 2–20. Corrected via `/explore-codebase`.

## v1.0 — initial release

Modern PySide6/Qt THD calculator (customer-facing, light theme). Operator picks an
NVGate FFT spectrum window and a number of harmonics, clicks Run, and sees THD %,
THD dB, H1 frequency and H1 amplitude in the app window. Places a harmonic marker
on the NVGate spectrum and exports a 3-sheet Excel report (Metadata, Spectrum,
THD Analysis). Same THD calculation as `thd-ui`.
