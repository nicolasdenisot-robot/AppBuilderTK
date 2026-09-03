# resources/

| Folder / file | What it is | In git? |
|---------------|-----------|---------|
| `Framework/` | The official OROS SDK (pynvdrive, NVFileManager, DLLs, PDFs) | **No** — you add it (see below) |
| `AI/` | Machine-readable reference kit: every NVDrive command, setting, error code and notification as structured data, plus Markdown mirrors of four manuals | Yes |
| `llms.txt` | Map of the kit — what to read, in what order, what to trust | Yes |

## `AI/` — the reference kit (read this before writing NVDrive code)

Produced by OROS from the official manuals and headers (package v1.7, Framework
17.00.002). It exists so an assistant never has to guess a command name, a setting
identifier or a result address. **Where the kit and the official PDF disagree, the
PDF wins.**

| File | Answers |
|------|---------|
| `HOWTO_NVDrive_from_Python.md` | **Start here to write code.** Connect, run, read a setting, fetch a result, react to the operator, and the traps that cost the most time |
| `nvdrive_commands.json` | The 309 NVDrive commands: syntax, typed parameters, return value, error codes — and the exact `pynvdrive` import, class and arguments where a Python class exists (145 do; the other 164 must be sent raw) |
| `nvgate_idn_catalog.json` | 756 setting identifiers, both spellings, the label NVGate shows, and the value type |
| `nvdrive_result_ids.json` | The numbers that address a result, plus a shortcut from "averaged spectrum" straight to module 10 / process 2 |
| `nvdrive_errors.json` | 949 error codes — turns a numeric failure into a diagnosis |
| `nvgate_notifications.json` | 79 notifications and the three lookup tables without which their properties are just numbers |
| `dll_api.json` | 1251 DLL entry points with typed parameters (C++, C#, VB) — for the file-access layer |
| `*.md` (four) | Markdown mirrors of the manuals, 694 pages, headings and tables rebuilt, with `<!-- page N -->` markers back to the PDF |
| `MANIFEST.txt` | Provenance: package version, source PDFs, page counts |

The `.csv` files duplicate three of the `.json` files for spreadsheet use.

**Check it against your SDK:** `python tools/verify_kit.py`. It confirms every
Python-class shortcut the kit names really exists in your `pynvdrive`, and lists the
~20 commands the library exposes that the manual never documented — the kit is built
from the manual, so it cannot describe those.

**How to use them: look things up, don't read them whole.** Several are close to a
megabyte — opening one entirely wastes the context needed to build the app. Grep for
the command or setting name, or load the JSON and filter it.

## Adding the Framework SDK (one-time)

The SDK is not shipped in this repo. Add it once:

1. Download the **Framework** zip from
   <https://my.oros.com/categories/software/nvgate/>.
2. Unzip it — you'll get a folder named **`Framework`**.
3. Copy that whole `Framework` folder into **this `resources/` folder**, so the
   path becomes **`resources/Framework/`**.

You should then see `resources/Framework/Python/pynvdrive/` and the PDF manuals.
The apps and helpers expect the SDK at exactly that path.
