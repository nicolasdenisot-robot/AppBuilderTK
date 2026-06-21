# App archetypes — which kind am I building?

Pick the closest archetype, copy `apps/_template/`, and start from the listed
recipe / SDK example. Most apps are a blend.

| # | Archetype | What it does | Layer | Start from |
|---|-----------|--------------|-------|-----------|
| 1 | **Test sequencer / automation** | Set params → run → wait → stop → fetch result, automatically | Live | `recipes/run-get-result.md` |
| 2 | **Pass/fail station (end-of-line)** | Measure, judge against limits, show verdict, export & report | Live | `recipes/pass-fail.md` |
| 3 | **Custom calculation tool** | Read a result/marker, compute something NVGate doesn't | Live | `algorithms.md` |
| 4 | **Custom configuration / results UI** | Branded screen to set up and/or show results | Live (+ UI) | stop #5 in CLAUDE.md |
| 5 | **Data collector / monitor** | Pull results from one/many analyzers over the network | Live (TCP) | `recipes/run-get-result.md` |
| 6 | **Event-driven / reactive** | React when a setting/state/save changes | Live (notifications) | `recipes/notifications.md` |
| 7 | **Data injection** | Push computed scalar/spectrum back into NVGate to display | Live | NVDrive manual §3.7 / TCPResultChannel |
| 8 | **Signal/result exporter / converter** | Read saved `.osfh`/`.res` files → CSV/Excel/your format, no NVGate | File | `OR3x_Developer_Toolkit.pdf` (Example_sig_read, NVGateFilesDemo) |
| 9 | **Signal editor / batch post-processing** | Split/erase/remove records & channels, batch crunch folders | File | `OR3x_Developer_Toolkit.pdf` (NVGateSignalEditingDemo) |

## Domain notes
- **Rotating machinery / turbomachinery:** usually archetype 1/2/5 + Tier-1 order
  tracking & Campbell from NVGate, plus `ross` for rotordynamics (`algorithms.md`).
- **Sound quality:** often archetype 2/3/8 + `mosqito` psychoacoustic metrics.

## The two layers (reminder)
- **Live control** (`pynvdrive`): NVGate must be running. Archetypes 1–7.
- **File access** (`orostk`/DLLs): no NVGate needed. Archetypes 8–9.
