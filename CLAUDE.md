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
5. **Protect the user's original data above everything else.** Their
   **measurements, signals, workbook, NVGate projects, NVGate settings, and user settings**
   — stored in the NVGate data folder (e.g. `C:\OROS\NVGate data\`, or wherever
   NVGate keeps projects/measurements) — are irreplaceable and must **never** be
   deleted, overwritten, or edited in place. When a task needs to change such a
   file, **write a NEW copy with the date in its name** (e.g.
   `myproject_2026-06-21`) and leave the original untouched. If a destructive
   change seems unavoidable, **stop and ask first.** Likewise, never modify
   `resources/Framework/` (READ-ONLY SDK reference) without explicit confirmation.
6. **Reuse before you write.** Check `shared/oros_helpers/`, `shared/assets/`,
   and `docs/recipes/` first; only write new code if nothing fits (section 6).
7. **When an app works end-to-end, create `README.md` in the app folder.**
   Write it in plain language — no Python, no jargon. The content depends on the
   app: adapt it to who will use it and what they need to know. Do this automatically
   — do not wait for the user to ask. See section 6 for guidance.

---

## 3. The reliability principle

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
├── resources/
│   ├── Framework/            ← OROS SDK + manuals (READ-ONLY; NOT in git — added by user, see README)
│   │   ├── NVDrive_Reference_Manual.pdf  (live control, 386 pages)
│   │   ├── OR3x_Developer_Toolkit.pdf    (toolkit overview)
│   │   └── Python/pynvdrive/             (the live-control library you import)
│   └── manuals-text/        ← plain-text mirror of the PDFs (committed; read THESE,
│                              since PDFs may not render — e.g. NVDrive_Reference_Manual.txt)
├── docs/                     ← distilled guidance — READ THIS, not the 386-page PDF
│   ├── nvdrive-cheatsheet.md     top ~30 commands with examples
│   ├── algorithms.md             where to get calculations (turbomachinery, sound quality)
│   ├── app-archetypes.md         app types → which example to copy
│   └── recipes/                  proven copy-adapt patterns
├── shared/
│   ├── oros_helpers/         ← reusable Python helpers (reuse these!)
│   └── assets/
│       └── logos/            ← brand logos for app UIs (never store in app/ folders)
│           ├── oros/         ← OROS brand: logo_color.png (light) · logo_white.png (dark)
│           └── <customer>/   ← add a folder here for each customer brand
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
| **1** | **Goal & operator** | What outcome do you want? Who runs the finished app — you, or an operator who just clicks an icon? Live analyzer (real-time) or saved files (offline)? **And: from where will they invoke it** — double-clicking a file on the desktop, from NVGate's Automation menu, a scheduled task, something else? |
| **2** | **Capability layer** | Live control / file access / both. Usually you can infer it — confirm in plain words. |
| **3** | **Computation source** | When custom math is needed: NVGate-native (preferred) vs a Python library. See `docs/algorithms.md` and the Tier-1 rule below. |
| **4** | **Where results appear** | **Always ask, never assume:** show results *in NVGate* (drive windows/layouts/markers — nothing to build, but operator needs NVGate open) vs a *custom UI* (needed when no NVGate is in front of the operator, or for a branded/simplified screen). |
| **5** | **UI stack** *(only if custom UI)* | **Ask per app**, proposing options with pros/cons so the user can choose well — e.g. PySide6/Qt desktop (packages to `.exe`, best for operators), Streamlit (browser dashboard, fast to build), Tkinter (built-in, simplest, dated). Do not default. |
| **6** | **Export form** | Two options — standalone `.exe` or `.bat` + Python source. **Always ask**, explain both with pros/cons, and let the user choose. Never default silently. See note below. |

**Tier-1 computation rule:** If NVGate already computes it (FFT, 1/n-octave, order
tracking, FRF, overall/RMS, waterfall/Campbell…), **drive NVGate and fetch the
result — do not reimplement it in Python.** Only reach for Python libraries
(`docs/algorithms.md`) for math NVGate does not do, or for post-processing.

**NVGate Automation / integration layer.** An app's own launcher (e.g.
`launch_xyz.bat`) uses paths relative to its own folder and must stay there.
If the operator wants to invoke the app from **NVGate's Automation → Execute
menu**, they cannot simply copy that launcher to the NVGate Links folder
(`C:\OROS\NVGate data\Links\`) — it will break because relative paths no longer
resolve. A separate entry-point file that references the real launcher by its
**full absolute path** is required in the Links folder.

The right form for that entry point depends entirely on context: who installs
the app, where it lives, whether it will be redistributed to other machines.
There is no fixed recipe. What is fixed is the question — **always ask the user
where and how the operator will invoke the app before you consider delivery
complete**, and design the entry point accordingly. Do not assume a
double-click launcher is the only thing needed.

**Export form — what to offer and how to explain it.** Present both options with
their trade-offs so the user can make an informed choice. Both forms work equally
well with NVGate's Automation → Execute menu — that is *not* the differentiator.

*Option A — Standalone `.exe`*
PyInstaller bundles Python, all libraries, and the app into a single file. The
operator needs **nothing pre-installed** — no Python, no pip, no setup.
- Pros: truly zero-dependency; one file to hand over; no IT involvement needed.
- Cons: the `.exe` is large (50–150 MB); Windows Defender or company antivirus
  sometimes flags unknown executables (even clean ones); every bug fix requires a
  full rebuild and re-delivery.
- Best when: the operator is a production-line worker or someone outside your
  company; you have no control over their PC; or IT policy forbids installing Python.

*Option B — `.bat` + Python source*
The operator runs the Python code directly. They need **Python installed once**
(done via `setup.bat`); after that, launches are instant.
- Pros: tiny package (a few KB of text files); no antivirus issues; a bug fix is
  just editing a `.py` file and sending it — no rebuild; easier to diagnose when
  something breaks (the terminal shows the exact error).
- Cons: Python must be installed on the operator's PC; if it is not (or is the
  wrong version), IT help is needed before the app runs.
- Best when: the operator is an engineer in the same organisation; IT can install
  Python once; you expect to update the app regularly; or you are still iterating.

---

## 6. Working inside an app

Each app is a **self-contained folder** under `apps/` so it can be exported and
shipped on its own.

```
apps/<app-name>/
├── DIRECTIVE.md      ← the app's spec + build manifest (see below)
├── README.md         ← plain-language guide for whoever will use this app
├── app/              ← the app's deterministic Python (UI + logic) = the runtime
├── requirements.txt  ← PyPI packages this app needs (numpy, openpyxl, …)
├── .tmp/             ← scratch / intermediate files — gitignored, NEVER exported
└── dist/             ← generated operator package (built by tools/export_app.py)
```

**`DIRECTIVE.md` is the heart of each app.** It has YAML frontmatter (read by the
export tool) and a body (the spec). Treat it as a **living document**:

- Write it during the section-5 interview.
- When you learn something while building (a setting only applies after Run, a
  specific result/setting IDN, a quirk), **record it in the "Lessons learned"
  section** so the next session and the next app benefit.
- **Do not overwrite or discard a DIRECTIVE.md without asking** (rule #5). Improve
  it over time; never use it ad hoc and throw it away.

**`README.md` is the plain-language guide** (rule #7). Write it once the app
runs successfully end-to-end, without being asked. Ask yourself: *who will use
this app, and what do they need to know to use it confidently?* The answer shapes
the content — there is no fixed template. A self-service tool for an engineer needs
different information than a one-click app for a production-line operator or a
deliverable sent to a customer. Use your judgement: include what is genuinely
useful, leave out what is obvious. Always write in plain language with no jargon.

**Self-correction loop.** When something breaks: read the error, fix the code,
re-test to confirm, then add the cause + fix to `DIRECTIVE.md`. Each failure should
make the app and the docs stronger.

**Starting a new app:** copy `apps/_template/` to `apps/<app-name>/`, fill in its
`DIRECTIVE.md`, and build inside `app/`. Reuse `shared/oros_helpers/` rather than
re-writing connection / result / export boilerplate.

---

## 7. Exporting (delivering the app)

Use `tools/export_app.py`. Run it once when the app is ready to ship:

```
python tools/export_app.py <app-name>
```

It produces a **versioned, operator-ready folder** at:

```
apps/<name>/dist/<name>-v<version>-<target>/
```

For example: `apps/thd-ui/dist/thd-ui-v1.0-exe/` or `apps/thd-ui/dist/thd-ui-v1.0-source/`.
Both forms can exist side by side in `dist/` without overwriting each other.

After the tool runs, show the user the folder path. **The user** inspects the
contents, then zips and sends it — the tool stops after producing the folder
and does not zip automatically. Its contents depend on the delivery form:

| Exe delivery | Source / bat delivery |
|---|---|
| `<name>.exe` | `app/` + `pynvdrive/` + `oros_helpers/` |
| `install_to_nvgate.bat` | `launch_<name>.bat` |
| `README.txt` | `setup.bat` (pip install, run once) |
| | `install_to_nvgate.bat` |
| | `requirements.txt` · `README.txt` |

The README in the app folder is `README.md` (Markdown, for reading in the editor
during development). The export tool copies it into the delivery package as
**`README.txt`** so any operator can open it with a double-click — no special app
needed.

When the two delivery forms need different instructions (different files, different
setup steps), create form-specific READMEs alongside `README.md`:

```
apps/<app-name>/
    README.md           ← development reference, covers the app overall
    README-exe.md       ← delivery README for exe form (if different)
    README-source.md    ← delivery README for source form (if different)
```

The export tool picks `README-<target>.md` first if it exists, and falls back to
`README.md`. Write form-specific READMEs whenever the two forms would otherwise
reference files that don't exist in that package (e.g. `launch_*.bat` in an exe
delivery, or `setup.bat` in a source delivery that isn't mentioned anywhere).

Both delivery forms include a **generated `install_to_nvgate.bat`** that
registers the app in NVGate's Automation → Execute menu (see section 5,
integration layer note). It uses the exe / launcher bat's absolute path,
captured at package time from the folder where the operator unzips.

**Required DIRECTIVE.md frontmatter fields for this tool:**

```yaml
version: 1.0                # becomes part of the folder name
display_name: My App Name   # shown in NVGate Automation (derived from app_name if absent)
export_target: exe|source
entry_point: app/main.py
logo: oros                  # brand folder under shared/assets/logos/ (default: oros)
```

**Workflow for updates:** modify the app in `apps/<name>/`, bump `version` in
`DIRECTIVE.md`, run the export tool again. The user zips the new folder and
sends it to the operator; the operator unzips it and, if needed, re-runs
`install_to_nvgate.bat` (only when the install location changes).

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
| Any NVDrive command detail not in the cheatsheet | `resources/manuals-text/NVDrive_Reference_Manual.txt` (searchable text mirror of the PDF) |

---

## 10. Logo convention

App UIs show a brand logo in the header. Logos are **shared assets** — never
store them inside an app's `app/` folder. They live in `shared/assets/logos/<brand>/`.

**Which variant to use:**

| File | When to use |
|------|-------------|
| `logo_color.png` | Light-theme UI — **default for all apps unless told otherwise** |
| `logo_white.png` | Dark-theme UI only |

**To add a logo to an app:**

1. Set `logo: oros` (or the customer brand name) in `DIRECTIVE.md`.
   The export tool reads this and copies the right files automatically — nothing
   else to do for delivery.

2. In `main.py`, use this exact pattern (copy-paste; change `_LOGO_BRAND` and
   `_LOGO_VARIANT` as needed):

   ```python
   _LOGO_BRAND   = "oros"   # must match a folder under shared/assets/logos/
   _LOGO_VARIANT = "color"  # "color" for light themes · "white" for dark themes

   def _logo_path() -> str:
       fname = f"logo_{_LOGO_VARIANT}.png"
       if hasattr(sys, '_MEIPASS'):           # running as a PyInstaller exe
           return os.path.join(sys._MEIPASS, fname)
       _here = Path(__file__).resolve()
       for candidate in (
           _here.parents[3] / "shared" / "assets" / "logos" / _LOGO_BRAND,
           _here.parent,                      # local override next to main.py
       ):
           p = candidate / fname
           if p.exists():
               return str(p)
       return ""
   ```

**For a customer-branded app:** create `shared/assets/logos/<customer-name>/`
and place `logo_color.png` and `logo_white.png` inside it. Then set
`logo: <customer-name>` in `DIRECTIVE.md` and `_LOGO_BRAND = "<customer-name>"`
in `main.py`. No other changes needed.
