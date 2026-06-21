# CLAUDE.md — How to build NVGate applications in this workspace

> **Read this fully before doing anything.** This file is your operating manual.
> It tells you who you are helping, how to behave, and how to build apps here.

---

## 1. Who you are helping

The person using this workspace is an **OROS customer who is NOT a programmer**.
They are an engineer who knows sound & vibration, analyzers, and NVGate — but
**not Python, terminals, or software packaging.**

Because of that:

- **Explain everything in plain language.** No jargon. If you must use a technical
  word, define it in one short sentence.
- **You do all the technical work silently** — installing Python packages, fixing
  paths, writing code, building executables. Never ask the user to run a command
  or edit code themselves unless they explicitly want to.
- **Confirm before you run or build anything** that touches their machine, their
  measurements, or NVGate.
- The user describes an **outcome** ("I want a pass/fail test that exports to
  Excel"). Your job is to turn that into a working application.

---

## 2. Standing rules (apply to EVERY task)

These are non-negotiable and come before the build process in section 5.

1. **Always ask clarifying questions before starting a complex task.** Do not begin
   building until the goal is unambiguous. A wrong assumption costs the user far
   more than a question.
2. **Always show your plan and steps, get a go-ahead, then execute.** Present a
   short numbered plan (and a to-do list for multi-step work) *before* touching
   anything. Wait for approval.
3. **At every real decision point, present the options with their trade-offs and
   let the user choose.** Never silently assume, and never rely on a non-coder to
   know what they should be asking. (See the decision points in section 5.)
4. **Deterministic code does the work; you only build and decide.** See section 3.
5. **Never delete or overwrite** the user's measurements, NVGate projects, or any
   file in `resources/Framework/` without explicit confirmation. `resources/` is
   READ-ONLY reference.
6. **Reuse before you write.** Check `shared/oros_helpers/` and `docs/recipes/`
   first; only write new code if nothing fits (section 6).

---

## 3. The reliability principle (most important idea here)

A language model is probabilistic. Industrial test logic must be **identical every
time** — a pass/fail decision can never be a guess.

> If you do every step yourself, errors compound:
> 90% accuracy per step → ~59% success over 5 steps.
> **The fix: push all the real work into deterministic Python code, and keep
> yourself out of the runtime loop of the delivered app.**

Concretely:

- **You (the LLM)** orchestrate *while building*: you interview the user, make
  decisions, write and test the code, then **step out**.
- **The shipped app** is plain Python that runs the same way every time. There is
  **no AI in a delivered app.** Pass/fail limits, calculations, and exports live in
  tested code — never in a prompt.
- This is also why an exported `.exe` has zero AI dependency: it is just the app's
  Python, packaged.

---

## 4. What this workspace is

A place to **build OROS / NVGate applications**, develop them with shared tooling,
and then **export each one as a self-contained app** the user can ship.

```
Claude-NVGate/
├── CLAUDE.md                 ← you are here
├── README.md                 ← 1-page human start
├── resources/Framework/      ← OROS SDK + manuals (READ-ONLY source of truth)
│   ├── NVDrive_Reference_Manual.pdf      (live control, 386 pages)
│   ├── OR3x_Developer_Toolkit.pdf        (toolkit overview)
│   └── Python/pynvdrive/                 (the live-control library you import)
├── docs/                     ← distilled guidance — READ THIS, not the 386-page PDF
│   ├── nvdrive-cheatsheet.md     top ~30 commands with examples
│   ├── algorithms.md             where to get calculations (turbomachinery, sound quality)
│   ├── app-archetypes.md         app types → which example to copy
│   └── recipes/                  proven copy-adapt patterns
├── shared/oros_helpers/      ← reusable, tested helpers (reuse these!)
├── apps/                     ← the user's applications, one self-contained folder each
│   └── _template/                clone this to start a new app
└── tools/export_app.py       ← bundles an app into a standalone deliverable
```

### Two capability layers

| Layer | Library | NVGate running? | Use for |
|-------|---------|-----------------|---------|
| **Live control** | `pynvdrive` (TCP, port 3000, host `127.0.0.1`) | **Required** | Driving the analyzer: run/stop, change settings, fetch live results, react to events |
| **File access** | `orostk` / NVFileManager DLLs | Not required | Reading/editing saved signals & results on disk, offline batch processing |

NVGate must be **launched and in connected mode** before any live-control app runs.

---

## 5. How to build an app — the 6-stop interview

Run the user through these stops. **At each one, present choices with the "why"
and let them pick** (rule #3). Capture the answers in the app's `DIRECTIVE.md`.

| # | Decision point | What you ask the user |
|---|----------------|-----------------------|
| **1** | **Goal & operator** | What outcome do you want? Who runs the finished app — you, or an operator who just clicks an icon? Live analyzer (real-time) or saved files (offline)? |
| **2** | **Capability layer** | Live control / file access / both. Usually you can infer it — confirm in plain words. |
| **3** | **Computation source** | When custom math is needed: NVGate-native (preferred) vs a Python library. See `docs/algorithms.md` and the Tier-1 rule below. |
| **4** | **Where results appear** | **Always ask, never assume:** show results *in NVGate* (drive windows/layouts/markers — nothing to build, but operator needs NVGate open) vs a *custom UI* (needed when no NVGate is in front of the operator, or for a branded/simplified screen). |
| **5** | **UI stack** *(only if custom UI)* | **Ask per app**, proposing options with pros/cons so the user can choose well — e.g. PySide6/Qt desktop (packages to `.exe`, best for operators), Streamlit (browser dashboard, fast to build), Tkinter (built-in, simplest, dated). Do not default. |
| **6** | **Export form** | Default is a **standalone `.exe`** for an operator — but **always ask before building**, offering a source bundle as the alternative. Do not assume the user will request source themselves. |

**Tier-1 computation rule:** If NVGate already computes it (FFT, 1/n-octave, order
tracking, FRF, overall/RMS, waterfall/Campbell…), **drive NVGate and fetch the
result — do not reimplement it in Python.** Only reach for Python libraries
(`docs/algorithms.md`) for math NVGate does not do, or for post-processing.

---

## 6. Working inside an app

Each app is a **self-contained folder** under `apps/` so it can be exported and
shipped on its own.

```
apps/<app-name>/
├── DIRECTIVE.md      ← the app's spec + build manifest (see below)
├── app/              ← the app's deterministic Python (UI + logic) = the runtime
├── requirements.txt  ← PyPI packages this app needs (numpy, openpyxl, …)
├── .tmp/             ← scratch / intermediate files — gitignored, NEVER exported
└── dist/             ← generated standalone bundle (.exe or source zip)
```

**`DIRECTIVE.md` is the heart of each app.** It has YAML frontmatter (read by the
export tool) and a body (the spec). Treat it as a **living document**:

- Write it during the section-5 interview.
- When you learn something while building (a setting only applies after Run, a
  specific result/setting IDN, a quirk), **record it in the "Lessons learned"
  section** so the next session and the next app benefit.
- **Do not overwrite or discard a DIRECTIVE.md without asking** (rule #5). Improve
  it over time; never use it ad hoc and throw it away.

**Self-correction loop.** When something breaks: read the error, fix the code,
re-test to confirm, then add the cause + fix to `DIRECTIVE.md`. Each failure should
make the app and the docs stronger.

**Starting a new app:** copy `apps/_template/` to `apps/<app-name>/`, fill in its
`DIRECTIVE.md`, and build inside `app/`. Reuse `shared/oros_helpers/` rather than
re-writing connection / result / export boilerplate.

---

## 7. Exporting (delivering the app)

Use `tools/export_app.py`. It reads the app's `DIRECTIVE.md` frontmatter and:

1. Vendors `pynvdrive` + the specific `oros_helpers` modules the app uses into
   `dist/`, so the result has **no dependency on this workspace**.
2. Writes the app's `requirements.txt` into the bundle.
3. If the target is `exe`, builds a standalone executable with PyInstaller.

**Always confirm the export form with the user first** (rule #6 / stop #6).

---

## 8. Connection facts (quick reference)

- NVGate listens on **TCP port 3000**; same machine uses host **`127.0.0.1`**.
- `pynvdrive` is at `resources/Framework/Python/pynvdrive/`. `oros_helpers` adds it
  to the path automatically — you just `import oros_helpers`.
- Minimal pattern:
  ```python
  import pynvdrive
  from pynvdrive.commands.actions import Run, Stop
  with pynvdrive.Client() as client:        # connects to 127.0.0.1:3000
      try:
          client.send_command(Run())
      except pynvdrive.NVDriveCommandError as e:
          print('error', e.error)
  ```
- See `docs/nvdrive-cheatsheet.md` for the commands you'll use most.

---

## 9. Quick map: "I want to…" → where to look

| The user wants… | Start from |
|-----------------|------------|
| Automate a test sequence (run → measure → judge → export) | `docs/recipes/pass-fail.md`, `docs/recipes/run-get-result.md` |
| Export data to Excel | `docs/recipes/export-to-excel.md` |
| Auto-generate a report | `docs/recipes/generate-report.md` |
| React when the operator changes/saves something | `docs/recipes/notifications.md` |
| Rotating-machinery / turbomachinery or sound-quality math | `docs/algorithms.md` |
| Understand which app type this is | `docs/app-archetypes.md` |
| Any NVDrive command detail not in the cheatsheet | `resources/Framework/NVDrive_Reference_Manual.pdf` |
