# -*- coding: utf-8 -*-
"""OFFLINE-FIXTURE-GUARD-1 - the documented offline test wrapper.

Runs ONE command with the guard enabled for that command and its descendants, then exits with the
command's own exit code.

    python 00_Agency_Governance/offline_guard/run_offline.py -- <command> [args...]

Examples (the two suites this repository actually runs):

    python 00_Agency_Governance/offline_guard/run_offline.py -- \
        python -m unittest discover -s 01_Sector/contracts -p "test_skill_fixture.py"

    python 00_Agency_Governance/offline_guard/run_offline.py -- \
        node --test 00_Agency_Governance/offline_guard/offline_guard.test.mjs

How activation reaches the child AND its descendants - by environment, not by in-process patching,
because a monkey-patch cannot cross a process boundary:

  * ARIKA_OFFLINE_FIXTURE=1   both guards require this; neither switches itself on.
  * PYTHONPATH                gains this directory, so CPython auto-imports the sibling
                              `sitecustomize.py` at startup, which calls offline_guard.activate().
  * NODE_OPTIONS              gains `--import file://<offline_guard.mjs>`, as a percent-encoded
                              file URI so a repository path containing spaces cannot break the
                              whitespace-separated NODE_OPTIONS parsing.

All three are inherited by grandchildren, so `npm test` -> `node --test` is covered too.

This wrapper never reads `.env`, never prints an environment value, and makes no network call.
"""
import os
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
NODE_GUARD = HERE / "offline_guard.mjs"
ENV_FLAG = "ARIKA_OFFLINE_FIXTURE"
USAGE = "usage: python run_offline.py -- <command> [args...]"


def build_env(base=None):
    """The guarded environment. Pure - returned, not applied, so it is unit-testable."""
    env = dict(os.environ if base is None else base)
    env[ENV_FLAG] = "1"

    py_path = env.get("PYTHONPATH", "")
    parts = [p for p in py_path.split(os.pathsep) if p]
    if str(HERE) not in parts:
        parts.insert(0, str(HERE))
    env["PYTHONPATH"] = os.pathsep.join(parts)

    # A file URI keeps spaces percent-encoded; NODE_OPTIONS splits on whitespace and does not
    # honour quoting, so a bare Windows path with spaces would be parsed as several flags.
    flag = "--import %s" % NODE_GUARD.as_uri()
    node_opts = env.get("NODE_OPTIONS", "")
    if NODE_GUARD.as_uri() not in node_opts:
        env["NODE_OPTIONS"] = (node_opts + " " + flag).strip() if node_opts else flag
    return env


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if "--" in argv:
        cmd = argv[argv.index("--") + 1:]
    else:
        cmd = argv
    if not cmd:
        print(USAGE, file=sys.stderr)
        return 2
    if not NODE_GUARD.exists():
        print("missing guard file: %s" % NODE_GUARD.name, file=sys.stderr)
        return 2

    env = build_env()
    # The banner names the PROGRAM and the argument COUNT only. It deliberately does not echo the
    # argument values: a command line can legitimately contain a URL, a hostname or a token, and a
    # guard that exists to keep those out of its own error messages must not print them here.
    print("OFFLINE-FIXTURE-GUARD-1 active for this command (%s=1)" % ENV_FLAG)
    print("  python hook : sitecustomize.py via PYTHONPATH")
    print("  node hook   : --import offline_guard.mjs via NODE_OPTIONS")
    print("  program     : %s (%d argument(s), not echoed)"
          % (os.path.basename(cmd[0]), len(cmd) - 1))
    print("  note        : guards these processes only - not Claude Code tools, MCP servers,")
    print("                browsers, connectors or commands launched outside this wrapper.")
    print("-" * 78)
    # Flush before spawning: this process' stdout is block-buffered when it is not a terminal,
    # while the child writes straight to the inherited handle. Without this the child's output can
    # appear ABOVE the banner, which makes the transcript misleading to read.
    sys.stdout.flush()
    sys.stderr.flush()
    try:
        return subprocess.call(cmd, env=env)
    except FileNotFoundError:
        print("command not found: %s" % cmd[0], file=sys.stderr)
        return 127


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
