"""
Run the analyzer and retrieve results over the live link.

These wrap the most common NVDrive result flow:
  Run -> (wait) -> Stop -> CreateResultEx -> GetResultEx.

A result is addressed by (module, process, channel, reference_channel_number).
Use `list_results()` to discover what is currently available and their ids.
"""

import time

from ._bootstrap import ensure_pynvdrive

ensure_pynvdrive()

import pynvdrive
from pynvdrive.commands.actions import Run, Stop
from pynvdrive.commands.signalresult import (
    CreateResultEx,
    GetResultEx,
    GetResultList,
    DeleteAllResultEx,
)


def run_measurement(duration_s=None, client=None):
    """
    Start the analyzer. If `duration_s` is given, wait that long then stop.
    Otherwise it returns immediately while NVGate keeps running.
    """
    def _do(c):
        c.send_command(Run())
        if duration_s is not None:
            time.sleep(duration_s)
            c.send_command(Stop())
        return True
    return _with_client(client, _do)


def stop_measurement(client=None):
    """Stop the analyzer."""
    return _with_client(client, lambda c: (c.send_command(Stop()), True)[1])


def list_results(client=None):
    """
    Return the list of currently available results. Each item is a
    ResultFormatAndDescription object exposing `.module_id`, `.process_id`,
    `.channel_number`, `.reference_channel_number` and `.input_name`
    (and `.to_dict()` / `.to_list()`).
    """
    def _do(c):
        cmd = GetResultList()
        c.send_command(cmd)
        return cmd.list_result_format_and_description
    return _with_client(client, _do)


def get_result(module, process, channel, reference_channel_number=0,
               waterfall=False, client=None):
    """
    Fetch a full result object for the given address.
    Returns the parsed result (use `.to_dict()` to inspect it).
    """
    def _do(c):
        wtf = 1 if waterfall else 0
        c.send_command(CreateResultEx(
            module=module, process=process, channel=channel,
            reference_channel_number=reference_channel_number,
            waterfall_flag=wtf,
        ))
        cmd = GetResultEx(
            module=module, process=process, channel=channel,
            reference_channel_number=reference_channel_number,
            waterfall_flag=wtf,
        )
        c.send_command(cmd)
        return cmd.result
    return _with_client(client, _do)


def get_scalar_result(module, process, channel, reference_channel_number=0,
                      client=None):
    """
    Convenience wrapper that returns a single scalar value (e.g. an overall /
    RMS level) for the given result address.

    Raises ValueError if the addressed result is not a scalar (e.g. a spectrum
    or other vector) — use get_result(...) to read those.
    """
    result = get_result(module, process, channel, reference_channel_number,
                         waterfall=False, client=client)
    if getattr(result, "scal", None) is None:
        raise ValueError(
            f"Result at (module={module}, process={process}, channel={channel}) "
            "is not a scalar; use get_result(...) to read a spectrum/vector."
        )
    return result.scal.value


def clear_results(client=None):
    """Remove all results previously created with CreateResultEx."""
    return _with_client(client, lambda c: (c.send_command(DeleteAllResultEx()), True)[1])


# --- internals -------------------------------------------------------------

def _with_client(client, fn):
    if client is not None:
        return fn(client)
    from .connection import connect
    with connect() as c:
        return fn(c)
