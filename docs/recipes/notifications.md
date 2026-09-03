# Recipe: react to NVGate changes (notifications)

**Goal:** have an app respond when the operator changes a setting/state, presses a
control, or saves — instead of polling. **Layer:** live control. **Archetype:** 6.

**Reference:** `resources/AI/nvgate_notifications.json` — all 79 notifications, the
properties each one sends, and the three lookup tables that turn those properties from
bare numbers into meanings. Full manual mirrored at
`resources/AI/NVGate_Notification_Mechanism.md` (112 pages), NVDrive manual §3.9.

## Use `orostk`, not `pynvdrive`

This is the one common job `pynvdrive` does **not** cover — it has no `Register*`
class and `Client` exposes no subscribe method. `orostk` does, with a complete
framework: `NotificationReader`, typed notification objects, and callbacks.
Verified in `resources/Framework/Python/NVFileManager/Packages/`.

**Do not hand-roll the raw protocol.** Reach for that only if `orostk` cannot be
installed.

### Two setup traps, both cheap to hit

1. **`orostk` is not ready to use** — unlike `pynvdrive`, it ships as installable
   archives. Install the one matching the interpreter *before* importing:
   `pip install resources/Framework/Python/NVFileManager/Packages/OROSPythonToolkit_Python312_x64_bdist.zip`
2. **The pre-built packages stop at Python 3.12** (3.8–3.12, x64 and one x32).
   The workspace's default interpreter may well be newer — check with
   `python -V` first. If it is, either build the app against a 3.10–3.12
   interpreter or use the `_sdist` archive. Decide this **before** promising the
   feature: it constrains the whole app, including how it is exported.

## How it works

Your process runs a **TCP server that NVGate connects back to** (default
`127.0.0.1:9000`). `NotificationReader` handles that; you subclass it and override
the callback for the events you want.

Subscribe with a notification object (`orostk.nvdrive.notification`):

| Object | Fires when |
|--------|-----------|
| `SettingNotification(module, submodule, setting)` | a setting value changed |
| `StateNotification(module, submodule, setting)` | a state changed |
| `CommandNotification(command)` | a control was pressed (Run=0, Pause=1, Stop=2…) |
| `UINotification(ui_event_id)` | a UI event (e.g. SaveProject id 48) |
| `ResultNotification(module)` | a new result was produced on that module |
| `MeasurementNotification()` | a new measurement was created |

Each has a matching `*_notification_callback` method on the reader to override.

## Pattern

```python
from orostk.nvdrive.nvd_client import NVDClient
from orostk.nvdrive.notification import SettingNotification
from orostk.nvdrive.notification_reader import NotificationReader


class MyReader(NotificationReader):
    def setting_notification_callback(self, notification: SettingNotification):
        # Deterministic handler — no AI, no guessing (CLAUDE.md §3).
        print("Setting changed:", notification.identifier())


client = NVDClient()
client.connect()                      # 127.0.0.1:3000, NVGate must be running

with MyReader(client) as reader:      # opens the callback server, closes it cleanly
    reader.subscribe(SettingNotification(module=1, submodule=1, setting=201))
    while True:
        reader.handle_notification(timeout=5)   # blocks until an event or timeout
```

A complete worked example ships with the SDK, including result channels:
`resources/Framework/Python/NVFileManager/OROSPythonToolkit_examples.zip`
→ `example_notification/example_notification.py`.

> Some notification families ask you to acknowledge before the next one is sent —
> the new-result family needs `UnblockNewResult(module)` in the callback, as the
> official example shows. Check the notification in `nvgate_notifications.json`.

## Notes

- Keep the handler deterministic and fast — it runs inside the receive loop.
- **Consider polling first.** If you only need a value occasionally,
  `get_setting()` in a loop is far simpler and keeps you on `pynvdrive` with no
  extra install and no Python-version constraint. Choose deliberately.
- Find a setting's IDN with SHIFT + right-click in NVGate, or in
  `resources/AI/nvgate_idn_catalog.json`. **The register commands take the legacy
  numeric form only**, not the text form.
- Record which IDNs/events you registered in the app's `DIRECTIVE.md`.
