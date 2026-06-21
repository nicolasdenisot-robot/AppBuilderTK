"""
Connection helpers for NVGate's live-control link (NVDrive over TCP).

NVGate must be launched and in connected mode. It listens on TCP port 3000;
on the same machine use host 127.0.0.1.
"""

from ._bootstrap import ensure_pynvdrive

ensure_pynvdrive()

import pynvdrive


DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 3000


def connect(host=DEFAULT_HOST, port=DEFAULT_PORT):
    """
    Open a connection to NVGate and return a `pynvdrive.Client`.

    Use it as a context manager so it always closes cleanly:

        with connect() as client:
            ...

    Raises ConnectionError with a plain-language message if NVGate is not
    reachable (most often: NVGate is not running, or it is on another machine).
    """
    client = pynvdrive.Client(host_port=(host, port))
    if not client.connect():
        raise ConnectionError(
            f"Could not reach NVGate at {host}:{port}. "
            "Make sure NVGate is running and in connected mode."
        )
    return client


def is_nvgate_available(host=DEFAULT_HOST, port=DEFAULT_PORT):
    """Return True if NVGate is reachable right now, False otherwise."""
    try:
        client = pynvdrive.Client(host_port=(host, port))
        ok = client.connect()
        if ok:
            client.disconnect()
        return bool(ok)
    except Exception:
        return False
