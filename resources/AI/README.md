# OROS NVGate - AI-readable developer files

Version 1.7, generated 2026-08-25.
Framework version: 17.00.002 113362-061272-240806-1502

## What this is

The NVDrive command specification, the notification mechanism, the DLL API and the
reference manuals, in formats an AI tool can read directly: JSON, CSV and Markdown
instead of PDF and generated HTML.

It is meant for AI-assisted programming (Codex, Copilot, Claude and similar) and for
building your own assistant on top of the OROS documentation. Nothing here replaces the
official manuals - it makes them machine-readable.

## Where to start

Point your AI tool at **`llms.txt`** at the root of this kit. That single page tells it
what to read, in what order, what to trust, and which traps to avoid. Everything else
follows from there.

## What is in this kit

    llms.txt        the entry point described above
    AI/             the machine-readable files listed below
    Framework/      the official OROS Framework, unchanged

**The `Framework/` folder is the official one, copied byte for byte.** Nothing has been
added to it, moved inside it, or removed from it, so it stays interchangeable with the
Framework you receive through the usual channel. Our files live alongside it, never
inside it.

In the `AI/` folder:

- `dll_api.json` (906 KB)
- `DLL_NVDCommand_and_NVDResult_Reference_Manual.md` (181 KB)
- `HOWTO_NVDrive_from_Python.md` (17 KB)
- `nvdrive_commands.csv` (59 KB)
- `nvdrive_commands.json` (849 KB)
- `nvdrive_errors.csv` (110 KB)
- `nvdrive_errors.json` (468 KB)
- `NVDrive_Reference_Manual.md` (393 KB)
- `nvdrive_result_ids.json` (20 KB)
- `nvgate_idn_catalog.csv` (57 KB)
- `nvgate_idn_catalog.json` (171 KB)
- `NVGate_Notification_Mechanism.md` (124 KB)
- `nvgate_notifications.json` (112 KB)
- `OR3x_Developer_Toolkit.md` (24 KB)

The `.json` files are the ones to give an AI tool. The `.csv` versions hold the same
information in a form you can open in a spreadsheet. The `.md` files are the official
manuals, converted so that headings are headings and tables are tables; every passage
carries a `<!-- page N -->` marker so you can find it again in the matching PDF.

## Where to start for writing code

**`HOWTO_NVDrive_from_Python.md`** in this folder is a short practical guide: connect,
run a measurement, read a setting, fetch a result, react to the operator - with
working code and the traps that cost the most time.

`pynvdrive` is ready to use at `Framework/Python/pynvdrive/pynvdrive/`, with 21 worked
examples beside it in `Framework/Python/pynvdrive/examples/` - nothing to install.
`orostk`, used for notifications, ships as installable archives in
`Framework/Python/NVFileManager/Packages/`, one per Python version: install the one
matching your interpreter before importing it.

## The reference files

1. **`nvdrive_commands.json`** is the command specification: syntax, parameters marked
   required or optional, return value, error codes.
2. **`nvdrive_errors.json`** turns any error response into a diagnosis.
3. **`nvgate_notifications.json`** is how you react to the operator. Each notification
   carries its command id and the typed properties of the block you receive.
4. **`nvgate_idn_catalog.json`** is the list of setting identifiers: both forms of
   each IDN, the label NVGate shows for it, and its type. Deliberately short - every
   field in it is something you can check yourself in NVGate.
5. **`nvdrive_result_ids.json`** holds the numbers that address a result: module ids,
   process ids, and a `quantity_map` that goes straight from "averaged spectrum" to
   module 10, process 2. Read it before trying to fetch anything.
6. **`dll_api.json`** is the C++ side: every exported DLL entry point with its typed
   parameters, for driving NVGate from C++, C# or Visual Basic.
7. **The Markdown mirrors** cover everything the structured files do not, with
   `<!-- page N -->` markers back to the official PDFs.

## How the command catalogue helps

Each of the 309 command sections carries its syntax, its parameters marked required or
optional, what it returns, and its error codes. It also carries a field most people are
surprised by:

    "pynvdrive_wrapper": "settingsstates/setsettingvalue.py"

When that field is `null`, **no Python wrapper exists for that command** and it has to
be sent directly - a two-line call, shown in the HOWTO. 164 of the
309 documented commands are in that situation, including 35 of the 43 marker
commands. Without this field an AI tool
invents a Python method that does not exist - which is the most common way generated
NVDrive code fails.

## What is not in this kit yet

We would rather tell you than let you find out:

- **The IDN catalogue lists one member of each numbered family, not every channel.**
  You will find `frontEnd.input1.label`, not `frontEnd.input3.label` - but the third
  input is addressed exactly the same way, only the number changes. How many exist
  depends on your hardware: `GetSubModuleList frontEnd.input1` returns the real list.
- **It lists what the analyzer can expose, not what your project exposes right now.**
  A setting is only reachable when its plug-in is active. If `GetSettingValue`
  reports an unknown setting, check that the module is switched on before suspecting
  the identifier.
- **Not every component has a text name.** When NVGate has none, the component keeps
  its number: `dynamicOperating.674:1.label`, `dynamicOperating.channel1.447`. Those
  identifiers are
  **just as valid** - the manual documents that mixed form, and we checked both forms
  against a running analyzer. They are only less readable, which is what the `name`
  field is for. You can always confirm an identifier in NVGate with Shift +
  right-click on the setting in the Analyzer Setting Browser.
- **Two known defects in the source documentation**, reproduced faithfully rather than
  silently corrected: the NVDrive manual prints `LoaMeasurement` for `LoadMeasurement`
  (p. 191), and a few C++ header comments are in French. The official PDFs and headers
  remain the reference; where our files and the source disagree, the source prevails.

## An honest word on coverage

Four of the Framework's five manuals are mirrored: 694 pages in total. The fifth
covers the MATLAB toolbox and is out of scope here. The structured
catalogues cover the NVDrive command language, the error codes, the notifications and
the DLL entry points. The setting identifiers are now included as well.

## Feedback

Tell us which gap costs you the most time - we would rather deliver the one that
unblocks you than deliver everything late.
