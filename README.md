# OROS NVGate App Builder

Build your own custom NVGate / OROS analyzer applications — **without writing code
yourself.** You describe what you want; Claude builds it.

## How to use this

1. **Open this folder in Claude Code.**
2. **Tell Claude what you want**, in plain words. For example:
   - *"I want an end-of-line test: start a measurement, run a pass/fail check, and
     export the results to Excel automatically."*
   - *"Read all my saved measurements in a folder and convert them to CSV."*
   - *"Show me loudness and sharpness for a recorded sound."*
3. **Answer Claude's questions.** It will ask a few things (who runs the app, where
   results should appear, etc.) and show you a plan before building anything.
4. **Get your app.** Claude builds it, tests it, and can package it as a
   double-click `.exe` for an operator, or a simple folder you run yourself.

You never need to touch Python, a terminal, or any code. Claude handles all of it.

## What you can build

Automated test sequences, pass/fail stations, custom configuration & results
screens, Excel/report exports, data collectors, signal/result converters, and
turbomachinery or sound-quality analysis tools. See `docs/app-archetypes.md`.

## Requirements

- **NVGate** installed (and running, for any app that controls the analyzer live).
- **Python** on the machine where apps are built (Claude will guide installation if
  needed). Finished `.exe` apps do **not** need Python on the operator's machine.

## What's in this folder

| Folder | What it is |
|--------|-----------|
| `CLAUDE.md` | Claude's operating manual (how it builds apps for you) |
| `resources/Framework/` | The official OROS SDK and manuals (do not edit) |
| `docs/` | Plain-language guides and ready-made patterns |
| `shared/` | Reusable building blocks Claude uses across apps |
| `apps/` | Your applications — one folder each |
| `tools/` | The packaging tool that makes shippable apps |

> Your applications live in `apps/`. Everything else supports building them.
