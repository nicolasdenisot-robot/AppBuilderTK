# `orostk` setup — the one Python-version trap in this kit

**Read this at interview stop #2 (capability layer) whenever the answer involves
file access or notifications — before promising the app.**

## Who needs this

| You are building… | Library | Anything to install? |
|---|---|---|
| Live control — drive the analyzer, read live results (archetypes 1–5, 7) | `pynvdrive` | **No.** Pure Python, works on any version, already wired up by `oros_helpers` |
| File access — read/edit saved signals & results with no NVGate (archetypes 8, 9) | `orostk` | **Yes** — see below |
| Event-driven — react when the operator changes something (archetype 6) | `orostk` | **Yes** — see below |

Most apps never touch `orostk`. But when one does, the setup has to happen *first*,
because it constrains the interpreter the whole app is built and exported with.

## The trap

`orostk` ships as pre-built archives in
`resources/Framework/Python/NVFileManager/Packages/`, one per Python version:

- **3.8** (x32 and x64), **3.9**, **3.10**, **3.11**, **3.12** (x64) — pre-compiled,
  drop straight in.
- **`_sdist`** (x32/x64) — source only. It carries Cython sources and C headers, so
  installing it needs a working C compiler. **Not a practical route** for this kit's
  users; treat it as unavailable.

**There is no package for Python 3.13 or newer.** A machine set up recently will very
likely have one, since that is what python.org offers today. `pynvdrive` does not care
— but `orostk` cannot be installed there at all.

## What to do

**1. Check the interpreter before promising anything.**

```
python -V
py -0p          # lists every Python installed, with its path
```

**2. If it is 3.8–3.12**, install the matching archive and carry on:

```
pip install resources/Framework/Python/NVFileManager/Packages/OROSPythonToolkit_Python312_x64_bdist.zip
```

**3. If it is 3.13 or newer**, say so in plain language and offer to install Python
3.12 alongside. This is safe and reversible — a second Python does not disturb the
existing one, nothing already built stops working, and `py -3.12` selects it
explicitly. Confirm before installing (CLAUDE.md §1), then build that app with 3.12.

## The consequence people forget

An app that imports `orostk` must **run** on that interpreter — so its `.exe` must be
**built** with it too. Run PyInstaller from the 3.12 interpreter, not the default one:

```
py -3.12 tools/export_app.py <app-name>
```

Record the interpreter in the app's `DIRECTIVE.md` so a later session rebuilds it the
same way instead of producing an exe that fails on the operator's machine.

## Worked example

The SDK ships one, including result channels and notifications:
`resources/Framework/Python/NVFileManager/OROSPythonToolkit_examples.zip`
→ `example_notification/example_notification.py`.
For notifications specifically, `recipes/notifications.md` has the pattern.
