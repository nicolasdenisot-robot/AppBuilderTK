# NVDrive cheat-sheet (most-used commands)

For everyday work use this, not the 386-page PDF. Full reference:
`resources/Framework/NVDrive_Reference_Manual.pdf`. The Python command classes live
in `resources/Framework/Python/pynvdrive/pynvdrive/commands/`.

## Connect
```python
import pynvdrive
with pynvdrive.Client() as client:        # 127.0.0.1:3000, NVGate must be running
    ...
```
Or via helpers: `from oros_helpers import connect` → `with connect() as client:`

## Actions (`pynvdrive.commands.actions`)
| Command | Does |
|---------|------|
| `Run()` | Start analysis / acquisition |
| `Stop()` | Stop |
| `Pause()` | Pause |
| `Autorange()` | Auto-range inputs |
| `ManualTrigger()` | Fire a manual trigger |

```python
from pynvdrive.commands.actions import Run, Stop
client.send_command(Run())
```

## Settings & states (`pynvdrive.commands.settingsstates`)
| Command | Does |
|---------|------|
| `GetSettingValue(idn=...)` → `cmd.value` | Read a setting |
| `SetSettingValue(idn=..., value=...)` | Write a setting |
| `GetSettingValues(idn=...)` → `cmd.value` | List choices of an enumerated setting |
| `GetAnalyzerState(module=...)` → `cmd.state` | Run/record/trigger state (see `TriggerState`) |

> A setting **IDN** identifies a setting, e.g. `'001.001.201'` or
> `'frontEnd.inputSettings.inputSampling'`. Reveal it in NVGate with
> **SHIFT + right-click** on the setting (manual §3.6.1).

## Results (`pynvdrive.commands.signalresult`)
| Command | Does |
|---------|------|
| `GetResultList()` → `cmd.list_result_format_and_description` | What results exist now (each item exposes `.module_id/.process_id/.channel_number`; `cmd.list` holds the same rows as plain lists). Helper: `list_results()` |
| `CreateResultEx(module, process, channel, reference_channel_number=0, waterfall_flag=0)` | Register a result before reading it |
| `GetResultEx(...)` → `cmd.result` | Fetch it; scalar via `result.scal.value`; inspect via `result.to_dict()` |
| `DeleteAllResultEx()` | Clear created results |

A result address is **(module, process, channel, reference_channel_number)**.
Helpers wrap this: `from oros_helpers import list_results, get_result, get_scalar_result`.

## Graphics (`pynvdrive.commands.graphics`) — show results in NVGate
| Command | Does |
|---------|------|
| `AddWindowResult(layout, window, module, process, channel, ...)` | Open a window on a result |
| `SetLayout(layout_name)` | Switch to a saved layout |
| `AutoscaleAllWnd(layout_name, axis='')` | Auto-scale a layout's windows |

Helpers: `from oros_helpers import nvgate_display`.

## Projects (`pynvdrive.commands.project`)
`LoadProject`, `OpenProject`, `GetProjectList`, `GetMeasureList`, `LoadWorkbook`,
`SaveWorkbook`, … — load a prepared project/workbook to set the analyzer up fast.
(Browse `pynvdrive/commands/project/` for the full set; there is no `SaveProject`
or `LoadMeasurement` class.)

## Notifications (manual §3.9) — react to changes
Subscribe to setting/state/command/UI events so an app responds when the operator
changes something. See `recipes/notifications.md`.

## Error handling pattern
```python
from pynvdrive.commands.actions import Run
try:
    cmd = Run()
    client.send_command(cmd)
except pynvdrive.NVDriveCommandError as e:
    print('NVDrive error:', e.error)
```
