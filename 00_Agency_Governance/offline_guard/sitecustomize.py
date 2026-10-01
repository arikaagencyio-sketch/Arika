# -*- coding: utf-8 -*-
"""OFFLINE-FIXTURE-GUARD-1 - Python activation hook.

CPython imports a module named `sitecustomize` automatically at interpreter startup IF one is
importable. This file is therefore only reachable when THIS directory is on PYTHONPATH, which only
`run_offline.py` arranges. Nothing else in the repository puts it there.

Two independent conditions must BOTH hold before anything is patched:
  1. this directory is on PYTHONPATH (so this file is importable at all), and
  2. ARIKA_OFFLINE_FIXTURE=1.

If either is false this file is never imported or does nothing, so ordinary production execution is
behaviourally unchanged. That is deliberate: the guard fails closed on network use, and fails OPEN
on activation - it never switches itself on.
"""
import os
import sys

if os.environ.get("ARIKA_OFFLINE_FIXTURE") == "1":
    try:
        import offline_guard  # same directory, which is on PYTHONPATH by construction

        offline_guard.activate()
    except Exception as exc:  # pragma: no cover - reported, never silently swallowed
        # A guard that failed to install must be loud. It must NOT be mistaken for a guard that is
        # in place, so this prints and keeps going rather than masking the state.
        sys.stderr.write(
            "OFFLINE_FIXTURE_GUARD_INSTALL_FAILED: %s: %s\n" % (type(exc).__name__, exc)
        )
