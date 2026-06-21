"""
Display helpers — show results *inside NVGate* instead of building a custom UI.

When the operator already has NVGate open, this is the cheapest, most professional
way to present results: drive NVGate's own windows, layouts and markers. Reach for
a custom UI only when the operator has no NVGate in front of them (CLAUDE.md
stop #4).

These wrap NVDrive graphics commands. See the NVDrive manual section 3.3 for the
full set; add more wrappers here as apps need them.
"""

from ._bootstrap import ensure_pynvdrive

ensure_pynvdrive()

import pynvdrive
from pynvdrive.commands.graphics import (
    AddWindowResult,
    SetLayout,
    AutoscaleAllWnd,
)


def show_result_window(module, process, channel, layout, window,
                       reference_channel_number="", client=None):
    """
    Open an NVGate window (named `window`, in layout `layout`) displaying the
    given result. `layout` and `window` are names you choose / that exist in the
    active project.
    """
    def _do(c):
        cmd = AddWindowResult(
            layout=layout, window=window,
            module=module, process=process, channel=channel,
            reference_channel_number=reference_channel_number,
        )
        c.send_command(cmd)
        return cmd.value
    return _with_client(client, _do)


def set_layout(layout_name, client=None):
    """Switch NVGate to a pre-defined layout (a saved window arrangement)."""
    return _with_client(client, lambda c: (c.send_command(SetLayout(layout_name=layout_name)), True)[1])


def autoscale_layout(layout_name, axis="", client=None):
    """Auto-scale all windows of a layout so traces fit nicely."""
    return _with_client(
        client,
        lambda c: (c.send_command(AutoscaleAllWnd(layout_name=layout_name, axis=axis)), True)[1],
    )


# --- internals -------------------------------------------------------------

def _with_client(client, fn):
    if client is not None:
        return fn(client)
    from .connection import connect
    with connect() as c:
        return fn(c)
