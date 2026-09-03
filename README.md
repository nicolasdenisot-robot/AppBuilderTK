# OROS NVGate App Builder

Build your own custom NVGate / OROS analyzer applications — **without writing code
yourself.** You describe what you want; Claude builds it.

> **📊 Workspace overview deck** (a visual tour of what this is and what you can build):
> <https://chaorandu-ai.github.io/oros-nvgate-app-builder-overview/>

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

## Improving an app you already have

You don't have to start from scratch. If you already have an app — one built here
before, or code you bring in from elsewhere — Claude can help you understand and
change it. Just ask in plain words ("help me improve my pass/fail test"), or use
these commands:

- **`/explore-codebase`** — Claude reads an existing app and explains, in plain
  language, what it does and how it's built. (If you're bringing in code from
  elsewhere, drop it into a folder under `apps/` first and Claude will set up the
  rest.)
- **`/scope-feature`** — describe a change you want; Claude tells you what it would
  take, what can be reused, and what's tricky, then asks a few questions to pin it down.
- **`/frontend-design`** — Claude designs or refines the on-screen part of an app.

You still never touch code — Claude does the work and shows you a plan first.

## Requirements

- **NVGate** installed (and running, for any app that controls the analyzer live).
- **Python** on the machine where apps are built (Claude will guide installation if
  needed). Any recent version is fine. Finished `.exe` apps do **not** need Python on
  the operator's machine.

  > **One exception worth knowing up front.** Two kinds of app — reading *saved*
  > signal/result files without NVGate, and reacting automatically when the operator
  > changes something — use an OROS library that is only published for **Python 3.12
  > and below**. If you expect to build either, install **Python 3.12**. If you
  > already have something newer, nothing is lost: Claude can add 3.12 alongside it
  > later, without disturbing anything. Everything else — driving the analyzer,
  > measuring, pass/fail, reports, Excel — works on any version.
- **The OROS Framework SDK** in `resources/Framework/` — see first-time setup below.

## First-time setup: add the OROS Framework SDK

This repo does **not** include the OROS SDK (it's large and you already have access
to it from OROS). Add it once:

1. Download the **Framework** zip from
   <https://my.oros.com/categories/software/nvgate/>.
2. Unzip it. You'll get a folder named **`Framework`**.
3. Copy that whole `Framework` folder into the **`resources/`** folder of this
   project, so the path becomes **`resources/Framework/`**
   (you should then see `resources/Framework/Python/pynvdrive/`, the PDFs, etc.).

That's it — the apps and helpers expect the SDK at that path.

4. Ask Claude to **check the reference kit against your SDK** (it runs
   `python tools/verify_kit.py`). This confirms the shortcuts in `resources/AI/`
   really match the library you downloaded, and lists a few commands that exist
   but are missing from the manual. It takes a second and saves a dead end later.

> OROS's machine-readable reference kit is already in `resources/AI/` — every NVDrive
> command, setting, error code and notification as structured data, plus searchable
> versions of four manuals. It's part of this repo, so Claude can look things up
> even before you add the SDK, and doesn't have to guess.

## Building something big — saving progress and going back

A complicated app can take more than one work session to build — that's normal, and
Claude won't lose its place. It saves progress as it goes (and automatically before a
session gets too full), writing down exactly where things stand. To continue another
time, just start a new session and say *"continue building my-app"* — Claude reads its
notes and picks up where it left off.

Two commands put you in control:

- **`/checkpoint`** — save the current progress now, as a recoverable point. Handy
  before you stop for the day, or before trying something you might want to undo.
- **`/restore`** — go back to an earlier save point. Claude shows you a plain list of
  your save points (*"Excel export working"*, *"pass/fail logic done"*, …); you pick
  one and it rolls the app back — **saving your current version first**, so going back
  is always undoable.

These work whether or not you use GitHub.

## Backing up your work to GitHub

Use the **`/sync-github`** command any time to save your work to a private GitHub
repository (it commits your changes and pushes them).

- **First run** also creates the private repo and sets up the connection. You'll
  need the GitHub CLI: `winget install --id GitHub.cli`, then `gh auth login`.
  Claude walks you through it.
- The SDK in `resources/Framework/` is **not** backed up (it's excluded on purpose);
  re-add it with the first-time setup above after cloning onto a new machine.
- `/sync-github` again later just saves your latest changes.

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
