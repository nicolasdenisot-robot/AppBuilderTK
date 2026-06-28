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

## Not wrapped in pynvdrive — raw protocol only
**Important:** the names above are NVDrive *protocol* commands (text sent over the
TCP link, manual §3.9). They are **not** available as Python classes in pynvdrive —
there is no `RegisterSetting` class, and `Client` exposes no subscribe/notify
method. A scan of `resources/Framework/Python/pynvdrive/pynvdrive/commands/` (and
the `toolbox/`) confirms no registration commands exist there.

So building an event-driven app (archetype 6) means working **below** the helper
layer: send the raw register-command bytes yourself and read the asynchronous
notification frames off the socket. This is advanced and **not helper-supported** —
budget extra time, and verify everything against manual §3.9 and the Visual C++
`Notifications` example. For most needs, prefer the simpler polling approach below.

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
