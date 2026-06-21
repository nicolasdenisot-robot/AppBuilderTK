"""
Locates the vendored `pynvdrive` library and puts it on the import path.

Two situations are handled:

1. **Inside this workspace** — pynvdrive lives at
   ``resources/Framework/Python/pynvdrive`` relative to the workspace root.
2. **Inside an exported app bundle** — the export tool vendors pynvdrive next to
   the app, so `import pynvdrive` already works and we do nothing.
"""

import os
import sys


def ensure_pynvdrive():
    """Make `import pynvdrive` work. Safe to call multiple times."""
    try:
        import pynvdrive  # noqa: F401  (already importable, e.g. exported bundle)
        return
    except ImportError:
        pass

    here = os.path.dirname(os.path.abspath(__file__))

    # Candidate locations, in priority order.
    candidates = []

    # 1) Workspace layout: <root>/shared/oros_helpers/_bootstrap.py
    workspace_root = os.path.abspath(os.path.join(here, "..", ".."))
    candidates.append(
        os.path.join(workspace_root, "resources", "Framework", "Python", "pynvdrive")
    )

    # 2) Vendored next to oros_helpers (exported bundle fallback).
    candidates.append(os.path.join(here, "..", "pynvdrive"))
    candidates.append(os.path.join(here, "pynvdrive"))

    for path in candidates:
        path = os.path.abspath(path)
        if os.path.isdir(os.path.join(path, "pynvdrive")):
            if path not in sys.path:
                sys.path.insert(0, path)
            return

    raise ImportError(
        "Could not locate the 'pynvdrive' library. Expected it under "
        "resources/Framework/Python/pynvdrive (in the workspace) or vendored "
        "next to oros_helpers (in an exported app)."
    )
