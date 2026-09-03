# How to drive NVGate from Python

A short, practical guide. The reference files in this folder tell you *what exists*;
this one tells you *how it is actually done*, and which mistakes cost the most time.

Everything below uses **`pynvdrive`**, the Python library for NVDrive. It ships with
this kit, at `Framework/Python/pynvdrive/pynvdrive/`, alongside its documentation and
its own examples in `Framework/Python/pynvdrive/examples/`. Nothing to install: put
that folder on your `sys.path`, or run from it.

Twenty-one worked examples sit next to it in `Framework/Python/pynvdrive/examples/` —
`example_setsettings.py`, `example_getresult.py`, `example_markers.py` and others.
When in doubt about a call, read the example before the prose.

A second library, `orostk`, is also included, but **it is not ready to use**: it ships
as installable archives in `Framework/Python/NVFileManager/Packages/`, one per Python
version (`OROSPythonToolkit_Python312_x64_bdist.zip` and so on). Install the one that
matches your interpreter before importing it. Its two halves are easy to confuse:
`orostk.file` works offline on saved files, while `orostk.nvdrive` is a **live**
client — and it is `orostk.nvdrive` that carries the notification framework used in
section 7.

---

## 1. Before anything

NVGate must be **running and in connected mode**. NVDrive is a TCP link: host
`127.0.0.1`, port `3000`. If NVGate is closed, `connect()` returns `False` — it does
not raise.

```python
import pynvdrive

with pynvdrive.Client() as client:          # ('127.0.0.1', 3000) by default
    if not client.is_connected():
        raise SystemExit("NVGate is not running, or not in connected mode")
```

`Client` is a context manager: entering connects, leaving disconnects.

## 2. Actions — run, stop, pause

```python
from pynvdrive.commands.actions import Run, Stop, Pause, Autorange, ManualTrigger

client.send_command(Run())
client.send_command(Stop())
```

Every command follows the same shape: build the object, pass it to `send_command`,
then read the result off the object. Nothing is returned by `send_command` itself.

You never have to guess how to call one. Each record in `nvdrive_commands.json` carries
a `pynvdrive` block with the exact call:

```json
"pynvdrive": {
  "import": "from pynvdrive.commands.settingsstates import SetSettingValue",
  "class": "SetSettingValue",
  "arguments": ["idn", "value"],
  "result_attributes": ["value"]
}
```

`arguments` are the constructor parameters in order; `result_attributes` are where the
reply lands once `send_command` returns. When `pynvdrive` is `null`, jump to section
7bis.

## 3. Settings — read and write

```python
from pynvdrive.commands.settingsstates import GetSettingValue, SetSettingValue

cmd = GetSettingValue(idn="frontEnd.input3.label")
client.send_command(cmd)
print(cmd.value)                             # the value lands on the object

client.send_command(SetSettingValue(idn="frontEnd.input3.label", value="Bearing"))
```

A setting is addressed by an **IDN**. Two forms work:

```
frontEnd.input3.label      the text form, recommended
1.3.1                      the legacy numeric form, limited to 32 channels
```

**Find an IDN** by pressing **Shift + right-click** on the setting in NVGate's
Analyzer Setting Browser: both forms are shown.

The catalogue lists one member of each numbered family — `frontEnd.input1`, not
`input3`. For the **text** form you can simply change the number. Do not do the same
with the legacy triplet: the numbering of family members is not always regular, so
read it off NVGate rather than computing it.

To list the accepted values of an enumerated setting, use `GetSettingValues` (plural).

> **The trap that costs the most time:** a setting does not always take effect
> immediately. Some apply on the fly, others require the analysis to be restarted. If
> you change a setting and the result does not move, that is why — send `Run()` again.

## 4. Results — find them, then read them

A result is addressed by four numbers: **module, process, channel, reference channel**.

```python
from pynvdrive.commands.signalresult import GetResultList, CreateResultEx, GetResultEx

# 1. what results exist right now
listing = GetResultList()
client.send_command(listing)
for row in listing.list_result_format_and_description:
    print(row.module_id, row.process_id, row.channel_number)

# 2. register the one you want, then fetch it
client.send_command(CreateResultEx(module=2, process=10, channel=1))

fetch = GetResultEx(module=2, process=10, channel=1)
client.send_command(fetch)

result = fetch.result
print(result.scal.value)      # a scalar, e.g. an overall level
print(result.to_dict())       # everything the block contains
```

Two steps, always: **`CreateResultEx` then `GetResultEx`**. Fetching without
registering first returns nothing. Add `waterfall_flag=1` for a waterfall.

**Where the numbers come from.** `nvdrive_result_ids.json` holds the tables: 20
modules, 128 processes, plus the unit and operator codes. It also carries a
`quantity_map` for the common cases, so you can go straight from what you want to an
address:

| You want | Module | Process |
|---|---|---|
| averaged spectrum | FFT1 = 10 | AVERAGE SPECTRUM = 2 |
| instantaneous spectrum | FFT1 = 10 | INSTANT SPECTRUM = 4 |
| time waveform | FRONT END = 1 | INSTANT TRIGGER = 1 |
| overall level | MONITOR = 2 | RMS = 10 |
| 1/n octave spectrum | 1/N OCTAVE = 12 | AVERAGE SPECTRUM = 2 |
| order spectrum | SYNCHRONOUS ORDER 1 = 14 | AVERAGE SPECTRUM = 2 |

Even so, prefer not to hard-code: `GetResultList()` tells you what actually exists on
the connected analyzer right now, which depends on the project and the licence.
`GetWindowTraces` does the same for a window already open in NVGate.

**Reading a spectrum, not just a number.** `result.scal.value` only works for a
scalar. A spectrum is a vector, and it lives in different blocks of the same result:

```python
fetch = GetResultEx(module=10, process=2, channel=1)   # FFT1 / AVERAGE SPECTRUM
client.send_command(fetch)
result = fetch.result

amplitudes = result.rvec.data          # one value per spectral line
start = result.xreg.start              # frequency of the first line
stop = result.xreg.stop                # frequency of the last line
unit = result.xreg.unit_label          # e.g. "Hz"

n = len(amplitudes)
step = (stop - start) / (n - 1) if n > 1 else 0
frequencies = [start + i * step for i in range(n)]
```

`rvec` is the real vector; `xreg` is the regularly-spaced X axis that goes with it,
given as `start` and `stop` rather than a step — compute the spacing from the number
of points. `xreg` also carries `physical_quantity`, `unit_name` and `unit_label`, so
you never have to assume the unit.

A complex result (cross-spectrum, FRF) carries `cvec` instead of `rvec`. Waterfalls
use `rwtf` / `cwtf`. **`result.to_dict()` shows every block a given result actually
contains** — run it once when exploring a new address rather than guessing.

Reference for the block layout: `NVDrive_Reference_Manual.md`, section 3.10.

## 5. Show something in NVGate

The simplest custom interface is often no interface: display the result in NVGate
itself and let the operator look at the screen they already know.

```python
from pynvdrive.commands.graphics import AddWindowResult, SetLayout, AutoscaleAllWnd

client.send_command(SetLayout("MyLayout"))
client.send_command(AddWindowResult(...))     # see nvdrive_commands.json for the parameters
```

## 6. Errors

```python
try:
    client.send_command(Run())
except pynvdrive.NVDriveCommandError as e:
    print("NVDrive refused the command:", e.error)
```

The error code has the form `013 001 000`. Look it up in **`nvdrive_errors.json`** to
get its meaning and the command that produces it.

Read the first group as the command discriminator: the same message can carry
different codes depending on who raised it. "Setting unknown" is `188 001 000` from
`GetSettingInfo` and `028 001 000` from `SetSettingValue`. A spaced triplet is a
consistency error; an unspaced run like `000008000` is an execution error.

## 7. Reacting to the operator

To respond when the operator changes a setting, presses a control or saves a project,
**register for notifications** rather than polling:

- `RegisterSetting` / `UnregisterSetting` — a setting changed
- `RegisterState` / `UnregisterState` — a state changed
- `RegisterCommand` / `UnregisterCommand` — a control was pressed
- `RegisterUINotification` — a user-interface event

**The part nobody guesses:** registering is not enough. Notifications do not come back
on the socket you sent from. **Your own process must run a TCP server**, and you must
tell NVGate to connect back to it with `ConnectToTCPClient <your IP> <your port>`.
Skip that and you will register successfully, then wait forever.

`pynvdrive` has no class for any of these commands — but you do **not** have to write
socket code. `orostk.nvdrive` ships a framework that handles the whole dance:

```python
from orostk.nvdrive.nvd_client import NVDClient
from orostk.nvdrive.notification import UINotification
from orostk.nvdrive.notification_reader import NotificationReader


class MyReader(NotificationReader):
    def ui_notification_callback(self, notification):
        print("the operator changed the refresh rate")


client = NVDClient()
client.connect()
with MyReader(client) as reader:          # sends ConnectToTCPClient and starts listening
    reader.subscribe(UINotification(ui_event_id=70))   # 70 = WINDOW REFRESH RATE
    reader.handle_notification(timeout=20)
```

A runnable example ships inside
`Framework/Python/NVFileManager/OROSPythonToolkit_examples.zip`, in the
`example_notification/` folder. Remember that `orostk` must be installed first, from
the archives in `Packages/`.

Decode what you receive against **`nvgate_notifications.json`**: it lists 79
notifications, each with its command id and the typed properties of the block.
`ui_event_id=70` above is that command id.

## 7bis. Sending a command that has no Python class

More than half the documented commands — 164 of 309 — have no class in `pynvdrive`.
That does **not** mean writing socket code. The library has a generic command object
for exactly this:

```python
from pynvdrive.command import CommandAction

# AddHarmonicMarker <window name> <Start position> [Number of harmonics]
client.send_command(CommandAction(name="AddHarmonicMarker",
                                  parameters=["Window1", "1000", "5"]))
```

`name` is the command exactly as spelled in `nvdrive_commands.json` — the spelling
matters, `AddSideBandMarker` has a capital B. `parameters` is the list of arguments in
the order the `syntax` field gives them, each one a string. Optional parameters you
want to skip are passed as `""`, so that the ones after them stay in position.

To read a value back rather than just act, subclass `Command` and say how to parse the
reply:

```python
from pynvdrive.command import Command, split_response

class GetSettingInfo(Command):
    def __init__(self, idn):
        super().__init__(name="GetSettingInfo", parameters=[idn, "", ""])
        self.strings = None

    def parse_response(self, response):
        self.strings = [s.decode("utf-8") for s in split_response(response)]

cmd = GetSettingInfo("frontEnd.input1.coupling")
client.send_command(cmd)
print(cmd.strings[0])      # 'Coupling' — the label NVGate displays
```

That is the whole trick. The header, the encoding and the error handling are the
library's job; you only supply the name, the parameters, and — if you want a value —
how to read the answer.

## 8. Where to get calculations — check this first

**If NVGate already computes it, drive NVGate and fetch the result. Do not
reimplement it in Python.** Reimplementing an FFT the analyzer already produced is the
single most common waste of effort.

NVGate natively produces:

- FFT spectra, averaging, overall and RMS levels
- 1/n-octave bands (1/1, 1/3, 1/12, 1/24…)
- order tracking, order spectra, waterfalls, Campbell diagrams
- frequency response functions and coherence
- filtering, weighting, integration and derivation

Only reach for Python libraries for maths NVGate does not do, or for post-processing
of data you fetched: `numpy` and `scipy.signal` for general work, `pandas` and
`openpyxl` for tables and Excel, `matplotlib` for plots. For specialised fields there
are dedicated packages — `mosqito` for psychoacoustics (loudness, sharpness,
roughness), `ross-rotordynamics` for rotor modelling, `PyWavelets` for envelope
analysis in bearing and gear diagnostics.

## 9. What kind of application are you writing?

Naming the shape early saves a lot of redesign:

| Shape | What it does |
|---|---|
| Test sequencer | set parameters, run, wait, stop, fetch — unattended |
| Pass/fail station | measure, judge against fixed limits, show a verdict, export |
| Custom calculation | read a result, compute what NVGate does not |
| Custom screen | a simplified or branded interface for setup or results |
| Data collector | pull results from one or several analyzers over the network |
| Event-driven | react when the operator changes something (section 7) |
| Data injection | push a computed value back into NVGate to display it |
| Exporter / converter | read saved signal and result files, write CSV or Excel |
| Batch post-processing | crunch folders of saved measurements offline |

The last two need no running NVGate: use the `orostk` package
(`Framework/Python/NVFileManager/`) or the DLLs (`dll_api.json`) instead.

## 10. A complete example: measure and judge

Everything above, in one piece. Note that the limit is a constant in the code — a
pass/fail decision must be reproducible, never inferred.

```python
import time
import pynvdrive
from pynvdrive.commands.actions import Run, Stop
from pynvdrive.commands.signalresult import CreateResultEx, GetResultEx

# Module 2 = MONITOR, process 10 = RMS: the broadband level of one input, the same
# figure the monitor bargraph shows. Look these up in nvdrive_result_ids.json.
# Whether it comes back in dB or in physical units depends on how the input is set
# up, so check the value before comparing it to a limit.
LIMIT = 95.0                         # fixed, per product, in the input's own unit
ADDRESS = dict(module=2, process=10, channel=1)


def measure_one(serial, seconds=5):
    with pynvdrive.Client() as client:
        if not client.is_connected():
            raise SystemExit("NVGate is not running, or not in connected mode")

        client.send_command(CreateResultEx(**ADDRESS))
        client.send_command(Run())
        time.sleep(seconds)
        client.send_command(Stop())

        fetch = GetResultEx(**ADDRESS)
        client.send_command(fetch)
        level = fetch.result.scal.value

    verdict = "PASS" if level <= LIMIT else "FAIL"
    return {"serial": serial, "level": round(level, 2),
            "limit": LIMIT, "verdict": verdict}


if __name__ == "__main__":
    print(measure_one("SN-0001"))
```

Before putting anything like this in front of an operator, decide what happens when
NVGate is closed, when there is no signal, and when the value is out of range. A test
station that fails silently is worse than one that refuses to start.

## 11. Traps, in one list

- **NVGate must be running** for anything in sections 1 to 7. `connect()` returns
  `False`, it does not raise.
- **A setting may not apply immediately** — restart the analysis if the result does
  not move.
- **`CreateResultEx` before `GetResultEx`**, always.
- **Not every documented command has a Python class.** 164 of the 309 documented
  commands have none, including most of the marker family and every notification
  registration command. Of the 43 commands in the Marker category, 8 do have a
  wrapper and 35 do not, so check the
  `pynvdrive_wrapper` field in `nvdrive_commands.json` rather than assuming either
  way. When it is `null`, send the command directly — see section 7bis. **Never
  invent a Python method name.**
- **What is visible depends on which plug-ins are active.** A setting can exist and
  still be unreadable because its module is off.
- **The register commands take the legacy numeric IDN only.** `RegisterSetting` wants
  `<Module number> <Sub-module number> <Setting number>` - not the text form. Since
  the catalogue lists only member 1 of each family and the legacy numbering of members
  is not regular, the triplet for channel 3 has to be read off NVGate with Shift +
  right-click. There is no way around that one from the files alone.
- **There is no way to list the settings of a sub-module.** `GetSubModuleList` returns
  sub-module identifiers and `GetSettingInfo` describes one setting at a time, but
  nothing enumerates them all.

---

Where to go next: `llms.txt` for the full map of this kit, `nvdrive_commands.json` for
any command's exact parameters, `nvdrive_result_ids.json` for result addresses, and
the Markdown mirrors of the manuals for everything else. Note that the Framework also
ships a MATLAB toolbox (`Framework/Matlab/MatDrive/`) with its own reference manual;
this kit covers the Python and C++ routes only.
