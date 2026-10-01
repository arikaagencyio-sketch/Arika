# -*- coding: utf-8 -*-
"""OFFLINE-FIXTURE-GUARD-1 - Python half.

Fails closed on network use inside a process that has EXPLICITLY enabled it. Inert otherwise: this
module patches nothing on import, so importing it can never change production behaviour.

Activation (either one):
  * set ARIKA_OFFLINE_FIXTURE=1 and put this directory on PYTHONPATH, so the sibling
    `sitecustomize.py` is auto-imported at interpreter startup and calls activate(); or
  * call offline_guard.activate() directly in-process.

The wrapper `run_offline.py` does the first for a child command and its descendants.

WHAT THIS DOES NOT CONTROL - see OFFLINE_FIXTURE_GUARD.md section 5. It guards THIS Python process
only. It does not control Claude Code tools, MCP servers, browsers, connectors, desktop
applications, shell commands launched outside the guarded entry point, privileged processes, or a
transport that reaches the network without passing through the APIs listed below.

It adds no dependency, makes no network call, needs no administrator access and reads no secret.
"""
import importlib
import importlib.util
import os
import sys

ENV_FLAG = "ARIKA_OFFLINE_FIXTURE"
ERROR_TOKEN = "OFFLINE_FIXTURE_NETWORK_BLOCKED"


class OfflineFixtureNetworkBlocked(RuntimeError):
    """Raised instead of touching the network. Carries an API CATEGORY and nothing else.

    It deliberately never carries a host, address, URL, header, token, payload or request body -
    the blocker discards every argument it was called with before raising.
    """


_STATE = {"active": False, "restore": [], "categories": []}

# ---------------------------------------------------------------- stdlib targets (always patched)
# (module_or_class_path, attribute, reported category)
_STDLIB = [
    ("socket:socket", "connect", "socket.connect"),
    ("socket:socket", "connect_ex", "socket.connect_ex"),
    ("socket", "create_connection", "socket.create_connection"),
    ("socket", "getaddrinfo", "dns.getaddrinfo"),
    ("socket", "gethostbyname", "dns.gethostbyname"),
    ("socket", "gethostbyname_ex", "dns.gethostbyname_ex"),
    ("socket", "gethostbyaddr", "dns.gethostbyaddr"),
    ("http.client:HTTPConnection", "connect", "http.client.HTTPConnection.connect"),
    ("http.client:HTTPSConnection", "connect", "http.client.HTTPSConnection.connect"),
    ("urllib.request", "urlopen", "urllib.request.urlopen"),
]

# ------------------------------------------- optional clients: patched ONLY if already installed.
# Nothing is installed, downloaded or added. A missing module is skipped silently - the stdlib
# patches above already close the underlying transport, so coverage does not depend on these.
_OPTIONAL = [
    ("requests.sessions:Session", "request", "requests.Session.request"),
    ("urllib3.connectionpool:HTTPConnectionPool", "urlopen", "urllib3.HTTPConnectionPool.urlopen"),
    ("httpx:Client", "send", "httpx.Client.send"),
    ("httpx:AsyncClient", "send", "httpx.AsyncClient.send"),
]


def _resolve(spec):
    """'socket' -> module; 'socket:socket' -> the class inside it. Returns None if unavailable."""
    mod_name, _, attr = spec.partition(":")
    root = mod_name.split(".")[0]
    if importlib.util.find_spec(root) is None:
        return None
    try:
        mod = importlib.import_module(mod_name)
    except Exception:
        return None
    if not attr:
        return mod
    return getattr(mod, attr, None)


def _make_blocker(category):
    def _denied(*_args, **_kwargs):
        # Every argument is discarded on purpose: no host, URL, token or body can leak into the
        # message, the traceback or a log.
        raise OfflineFixtureNetworkBlocked("%s: %s" % (ERROR_TOKEN, category))
    _denied.__name__ = "offline_guard_blocked"
    _denied.__qualname__ = "offline_guard_blocked"
    _denied.__doc__ = "Blocked by OFFLINE-FIXTURE-GUARD-1 (%s)." % category
    _denied._offline_guard_category = category
    return _denied


def _apply(targets):
    applied = []
    for spec, attr, category in targets:
        owner = _resolve(spec)
        if owner is None or not hasattr(owner, attr):
            continue
        original = getattr(owner, attr)
        if getattr(original, "_offline_guard_category", None) is not None:
            continue  # already guarded; do not double-wrap or lose the real original
        try:
            setattr(owner, attr, _make_blocker(category))
        except (AttributeError, TypeError):
            continue  # immutable target - skipped, and reported as not covered
        _STATE["restore"].append((owner, attr, original))
        applied.append(category)
    return applied


def activate(optional_clients=True):
    """Install the guard in THIS process. Idempotent. Returns the covered categories."""
    if _STATE["active"]:
        return list(_STATE["categories"])
    covered = _apply(_STDLIB)          # primitives first: closure must not depend on the extras
    if optional_clients:
        covered += _apply(_OPTIONAL)
    _STATE["active"] = True
    _STATE["categories"] = covered
    return list(covered)


def deactivate():
    """Restore every patched attribute, most recent first. Used by the guard's own tests."""
    for owner, attr, original in reversed(_STATE["restore"]):
        try:
            setattr(owner, attr, original)
        except Exception:
            pass
    _STATE["restore"] = []
    _STATE["active"] = False
    _STATE["categories"] = []


def is_active():
    return _STATE["active"]


def covered_categories():
    return list(_STATE["categories"])


def activation_requested():
    """True only when the environment explicitly asks for the guard."""
    return os.environ.get(ENV_FLAG) == "1"


if __name__ == "__main__":
    # Self-report only. Patches nothing, calls nothing, resolves nothing.
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    print("OFFLINE-FIXTURE-GUARD-1 (Python)")
    print("  activation flag   : %s=1" % ENV_FLAG)
    print("  flag set now      : %s" % activation_requested())
    print("  active in this pid: %s" % is_active())
    print("  stdlib targets    : %d" % len(_STDLIB))
    print("  optional targets  : %d (patched only when already installed)" % len(_OPTIONAL))
    print("  error token       : %s" % ERROR_TOKEN)
