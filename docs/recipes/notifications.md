# Recipe: react to NVGate changes (notifications)

**Goal:** have an app respond when the operator changes a setting/state, presses a
control, or saves — instead of polling. **Layer:** live control. **Archetype:** 6.
**Reference:** NVDrive manual §3.9, and the Visual C++ `Notifications` example in
`OR3x_Developer_Toolkit.pdf`.

## How it works
NVGate can push events to a client that has **registered** for them:

- `RegisterSetting` / `UnregisterSetting` — a setting value changed
- `RegisterState` / `UnregisterState` — a state changed
- `RegisterCommand` / `UnregisterCommand` — a control (Run=0, Pause=1, Stop=2…) changed
- `RegisterUINotification` / `ExecUINotification` — UI events (e.g. SaveProject id 48)

You register with the item's **IDN** (SHIFT+right-click in NVGate to find it), then
read pushed updates on the socket.

## In pynvdrive
The notification/registration commands live under
`resources/Framework/Python/pynvdrive/pynvdrive/commands/`. Check there for the
exact classes before coding (e.g. the `others` / `settingsstates` groups), and
verify each signature against its module — the registration API is lower-level
than the simple request/response commands.

## Pattern (pseudostructure)
1. Connect (a dedicated client for notifications).
2. Register the settings/states/commands you care about, by IDN.
3. Loop: receive an event → run your deterministic handler (e.g. auto-export,
   log, update a UI indicator).
4. On shutdown, unregister and disconnect.

## Notes
- Keep the event handler deterministic and fast.
- If you only need a value occasionally, simple polling with `get_setting()` may be
  enough and far simpler — choose deliberately.
- Record which IDNs/events you registered in the app's `DIRECTIVE.md`.
