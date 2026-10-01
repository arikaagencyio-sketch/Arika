# -*- coding: utf-8 -*-
"""OFFLINE-FIXTURE-GUARD-1 - focused tests for the Python half.

NO TEST CONTACTS THE NETWORK - not an external address, not DNS, not localhost. Coverage is proved
with TRIPWIRES: the real transport function is replaced by a recorder BEFORE the guard is installed,
so the guard wraps the recorder. If a blocked call ever reached the underlying transport the
recorder would fire, and the test asserts it never does.

    python -m unittest discover -s 00_Agency_Governance/offline_guard -p "test_offline_guard.py"
"""
import io
import os
import pathlib
import subprocess
import sys
import unittest

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import offline_guard  # noqa: E402
import run_offline  # noqa: E402

# Values that must never appear in an error, a message or a traceback.
FAKE_HOST = "guard-probe-host.invalid"
FAKE_URL = "https://guard-probe-host.invalid/secret-path"
FAKE_SECRET = "sk-ant-GUARDPROBE-NOT-A-REAL-KEY"


class Tripwire:
    """Stands in for a real transport function and records whether it was ever reached."""

    def __init__(self):
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        return "TRIPWIRE_REACHED"


class GuardTestBase(unittest.TestCase):
    """Leaves the process exactly as it was found, whether or not the guard was already active."""

    def setUp(self):
        self._was_active = offline_guard.is_active()
        offline_guard.deactivate()
        self._restore = []

    def tearDown(self):
        offline_guard.deactivate()
        for owner, attr, original in reversed(self._restore):
            setattr(owner, attr, original)
        if self._was_active:
            offline_guard.activate()

    def install_tripwire(self, owner, attr):
        original = getattr(owner, attr)
        self._restore.append((owner, attr, original))
        wire = Tripwire()
        setattr(owner, attr, wire)
        return wire


class GuardInactive(GuardTestBase):
    def test_importing_the_guard_patches_nothing(self):
        import socket
        wire = self.install_tripwire(socket, "getaddrinfo")
        self.assertFalse(offline_guard.is_active())
        # Ordinary (mocked) transport behaviour is unchanged while the guard is off.
        self.assertEqual(socket.getaddrinfo(FAKE_HOST, 443), "TRIPWIRE_REACHED")
        self.assertEqual(wire.calls, 1)

    def test_the_guard_never_switches_itself_on(self):
        self.assertFalse(offline_guard.is_active())
        self.assertEqual(offline_guard.covered_categories(), [])

    def test_deactivate_restores_the_original_callables(self):
        import socket
        wire = self.install_tripwire(socket, "getaddrinfo")
        offline_guard.activate()
        self.assertIsNot(socket.getaddrinfo, wire)
        offline_guard.deactivate()
        self.assertIs(socket.getaddrinfo, wire, "deactivate must restore the exact original")


class GuardActive(GuardTestBase):
    def test_every_stdlib_category_is_covered(self):
        covered = offline_guard.activate()
        for category in ["socket.connect", "socket.create_connection", "dns.getaddrinfo",
                         "http.client.HTTPConnection.connect",
                         "http.client.HTTPSConnection.connect", "urllib.request.urlopen"]:
            self.assertIn(category, covered)

    def test_socket_connect_fails_closed_before_the_transport(self):
        import socket
        wire = self.install_tripwire(socket.socket, "connect")
        offline_guard.activate()
        sock = socket.socket()
        try:
            with self.assertRaises(offline_guard.OfflineFixtureNetworkBlocked):
                sock.connect((FAKE_HOST, 443))
        finally:
            sock.close()
        self.assertEqual(wire.calls, 0, "the guard must throw BEFORE the transport is reached")

    def test_dns_resolution_fails_closed_before_the_transport(self):
        import socket
        wire = self.install_tripwire(socket, "getaddrinfo")
        offline_guard.activate()
        with self.assertRaises(offline_guard.OfflineFixtureNetworkBlocked):
            socket.getaddrinfo(FAKE_HOST, 443)
        self.assertEqual(wire.calls, 0)

    def test_create_connection_fails_closed_before_the_transport(self):
        import socket
        wire = self.install_tripwire(socket, "create_connection")
        offline_guard.activate()
        with self.assertRaises(offline_guard.OfflineFixtureNetworkBlocked):
            socket.create_connection((FAKE_HOST, 443))
        self.assertEqual(wire.calls, 0)

    def test_stdlib_http_clients_fail_closed_before_the_transport(self):
        import http.client
        import urllib.request
        wires = [self.install_tripwire(http.client.HTTPConnection, "connect"),
                 self.install_tripwire(http.client.HTTPSConnection, "connect"),
                 self.install_tripwire(urllib.request, "urlopen")]
        offline_guard.activate()
        with self.assertRaises(offline_guard.OfflineFixtureNetworkBlocked):
            http.client.HTTPConnection(FAKE_HOST).connect()
        with self.assertRaises(offline_guard.OfflineFixtureNetworkBlocked):
            http.client.HTTPSConnection(FAKE_HOST).connect()
        with self.assertRaises(offline_guard.OfflineFixtureNetworkBlocked):
            urllib.request.urlopen(FAKE_URL)
        self.assertEqual([w.calls for w in wires], [0, 0, 0])

    def test_installed_optional_clients_fail_closed(self):
        """requests / urllib3 / httpx are patched only because they are ALREADY installed."""
        covered = offline_guard.activate()
        checked = 0
        import importlib.util
        if importlib.util.find_spec("requests"):
            self.assertIn("requests.Session.request", covered)
            import requests
            with self.assertRaises(offline_guard.OfflineFixtureNetworkBlocked):
                requests.Session().request("GET", FAKE_URL)
            checked += 1
        if importlib.util.find_spec("urllib3"):
            self.assertIn("urllib3.HTTPConnectionPool.urlopen", covered)
            checked += 1
        if importlib.util.find_spec("httpx"):
            self.assertIn("httpx.Client.send", covered)
            checked += 1
        self.assertGreater(checked, 0, "this environment has at least one optional client")

    def test_a_missing_optional_client_is_skipped_not_fatal(self):
        # aiohttp is absent here; activation must still succeed and simply not list it.
        covered = offline_guard.activate()
        self.assertNotIn("aiohttp", " ".join(covered))
        self.assertIn("socket.connect", covered)

    def test_activation_is_idempotent(self):
        first = offline_guard.activate()
        second = offline_guard.activate()
        self.assertEqual(first, second)


class ErrorHygiene(GuardTestBase):
    def _blocked_text(self):
        """Raise a blocked call with host/URL/secret arguments and return everything emitted."""
        import socket
        import traceback
        offline_guard.activate()
        try:
            socket.getaddrinfo(FAKE_HOST, 443, FAKE_URL, FAKE_SECRET)
        except offline_guard.OfflineFixtureNetworkBlocked as exc:
            return "%s || %s || %s" % (exc, repr(exc), "".join(
                traceback.format_exception(type(exc), exc, exc.__traceback__)))
        self.fail("the call should have been blocked")

    def test_the_error_token_is_present_and_clear(self):
        self.assertIn("OFFLINE_FIXTURE_NETWORK_BLOCKED", self._blocked_text())

    def test_the_error_names_the_api_category(self):
        self.assertIn("dns.getaddrinfo", self._blocked_text())

    def test_no_hostname_or_url_leaks_into_the_error(self):
        text = self._blocked_text()
        self.assertNotIn(FAKE_HOST, text)
        self.assertNotIn(FAKE_URL, text)
        self.assertNotIn("guard-probe-host", text)

    def test_no_secret_value_leaks_into_the_error(self):
        self.assertNotIn(FAKE_SECRET, self._blocked_text())
        self.assertNotIn("GUARDPROBE", self._blocked_text())

    def test_the_guard_sources_never_touch_dotenv_or_secrets(self):
        for name in ["offline_guard.py", "sitecustomize.py", "run_offline.py",
                     "offline_guard.mjs"]:
            with io.open(HERE / name, encoding="utf-8") as fh:
                src = fh.read()
            low = src.lower()
            self.assertNotIn("dotenv", low, name)
            for forbidden in ["os.environ[\"ANTHROPIC", "ANTHROPIC_API_KEY", "CLICKUP_TOKEN",
                              "NOTION_TOKEN", "getenv(\"ANTHROPIC"]:
                self.assertNotIn(forbidden, src, name)

    def test_the_self_report_prints_no_environment_values(self):
        out = subprocess.run([sys.executable, str(HERE / "offline_guard.py")],
                             capture_output=True, text=True, timeout=60)
        self.assertEqual(out.returncode, 0)
        self.assertIn("OFFLINE-FIXTURE-GUARD-1", out.stdout)
        for key in ["ANTHROPIC_API_KEY", "CLICKUP_TOKEN", "NOTION_TOKEN", "PATH="]:
            self.assertNotIn(key, out.stdout)


class WrapperEnvironment(unittest.TestCase):
    """build_env is pure, so the activation contract is testable without spawning anything."""

    def test_it_sets_the_activation_flag(self):
        env = run_offline.build_env({})
        self.assertEqual(env["ARIKA_OFFLINE_FIXTURE"], "1")

    def test_it_puts_the_guard_directory_on_pythonpath(self):
        env = run_offline.build_env({})
        self.assertIn(str(HERE), env["PYTHONPATH"].split(os.pathsep))

    def test_it_preserves_an_existing_pythonpath(self):
        env = run_offline.build_env({"PYTHONPATH": "/already/there"})
        parts = env["PYTHONPATH"].split(os.pathsep)
        self.assertIn("/already/there", parts)
        self.assertEqual(parts[0], str(HERE))

    def test_it_adds_the_node_import_hook_as_a_percent_encoded_uri(self):
        env = run_offline.build_env({})
        self.assertIn("--import", env["NODE_OPTIONS"])
        self.assertIn("file:///", env["NODE_OPTIONS"])
        # A repository path containing spaces must not split NODE_OPTIONS into stray flags.
        self.assertNotIn(" ", env["NODE_OPTIONS"].split("--import ", 1)[1])

    def test_it_is_idempotent(self):
        once = run_offline.build_env({})
        twice = run_offline.build_env(once)
        self.assertEqual(once["NODE_OPTIONS"], twice["NODE_OPTIONS"])
        self.assertEqual(once["PYTHONPATH"], twice["PYTHONPATH"])

    def test_it_never_copies_a_secret_into_the_child_environment(self):
        env = run_offline.build_env({"ANTHROPIC_API_KEY": FAKE_SECRET})
        # The wrapper passes the parent environment through; it must not ADD or RENAME secrets.
        self.assertEqual(env["ANTHROPIC_API_KEY"], FAKE_SECRET)
        self.assertEqual(sorted(set(env) - {"ANTHROPIC_API_KEY"}),
                         ["ARIKA_OFFLINE_FIXTURE", "NODE_OPTIONS", "PYTHONPATH"])


class ActivationReachesChildProcesses(unittest.TestCase):
    """The wrapper's central claim. No child makes a network call - each is blocked first."""

    BANNER_END = "-" * 78

    def _run(self, inner, wrapped):
        cmd = [sys.executable, str(HERE / "run_offline.py"), "--"] + inner if wrapped else inner
        return subprocess.run(cmd, capture_output=True, text=True, timeout=180, cwd=str(REPO))

    def _child_output(self, out):
        """Both streams combined.

        Deliberately NOT split on the banner. The wrapper flushes before spawning, but relying on
        interleaving order between two processes writing one handle would be a brittle test. It is
        safe to scan the whole thing because the banner no longer echoes arguments and contains
        none of the probe strings - `test_the_wrapper_banner_does_not_echo_the_command_arguments`
        asserts exactly that, so a match here can only have come from the child.
        """
        return out.stdout + "\n" + out.stderr

    def test_a_python_grandchild_is_guarded(self):
        inner = [sys.executable, "-c",
                 "import socket\n"
                 "try:\n"
                 "    socket.getaddrinfo('%s', 443)\n"
                 "    print('REACHED_RESOLVER')\n"
                 "except Exception as e:\n"
                 "    print(type(e).__name__, e)\n" % FAKE_HOST]
        out = self._run(inner, wrapped=True)
        child = self._child_output(out)
        self.assertIn("OFFLINE_FIXTURE_NETWORK_BLOCKED", child)
        self.assertIn("dns.getaddrinfo", child)
        self.assertNotIn("REACHED_RESOLVER", child)

    def test_the_wrapper_banner_does_not_echo_the_command_arguments(self):
        """A command line may hold a URL or a token; the banner must not reprint it."""
        inner = [sys.executable, "-c", "print('ok')  # %s %s" % (FAKE_URL, FAKE_SECRET)]
        out = self._run(inner, wrapped=True)
        banner = (out.stdout + out.stderr).split(self.BANNER_END, 1)[0]
        self.assertIn("not echoed", banner)
        for leak in [FAKE_URL, FAKE_SECRET, FAKE_HOST, "guard-probe-host", "GUARDPROBE"]:
            self.assertNotIn(leak, banner, "the wrapper banner leaked %r" % leak)

    def test_an_unwrapped_python_child_is_NOT_guarded(self):
        """Production stays behaviourally unchanged. Checked by inspection, not by connecting."""
        inner = [sys.executable, "-c",
                 "import socket; print('FN=' + type(socket.getaddrinfo).__name__)"]
        out = self._run(inner, wrapped=False)
        self.assertIn("FN=", out.stdout)
        self.assertNotIn("offline_guard_blocked", out.stdout)

    def test_a_node_grandchild_is_guarded(self):
        # The fetch blocker throws SYNCHRONOUSLY so a floating promise cannot swallow it, which is
        # why this probe uses try/catch rather than .catch() and why stderr is inspected too.
        inner = ["node", "-e",
                 "try { fetch('%s'); console.log('REACHED_TRANSPORT'); }"
                 " catch (e) { console.log(e.message); }" % FAKE_URL]
        out = self._run(inner, wrapped=True)
        child = self._child_output(out)
        self.assertIn("OFFLINE_FIXTURE_NETWORK_BLOCKED", child)
        self.assertIn("globalThis.fetch", child)
        self.assertNotIn("REACHED_TRANSPORT", child)

    def test_a_node_grandchild_block_is_loud_even_when_unhandled(self):
        """An unhandled block must surface and fail the process, never pass silently."""
        inner = ["node", "-e", "fetch('%s')" % FAKE_URL]
        out = self._run(inner, wrapped=True)
        self.assertNotEqual(out.returncode, 0, "an unhandled block must fail the process")
        self.assertIn("OFFLINE_FIXTURE_NETWORK_BLOCKED", self._child_output(out))

    def test_an_unwrapped_node_child_is_NOT_guarded(self):
        inner = ["node", "-e", "console.log('FETCH=' + typeof fetch)"]
        out = self._run(inner, wrapped=False)
        self.assertIn("FETCH=function", out.stdout)
        self.assertNotIn("OFFLINE_FIXTURE_NETWORK_BLOCKED", out.stdout)

    def test_the_wrapper_returns_the_child_exit_code(self):
        out = self._run([sys.executable, "-c", "raise SystemExit(7)"], wrapped=True)
        self.assertEqual(out.returncode, 7)

    def test_the_wrapper_states_its_own_limits(self):
        out = self._run([sys.executable, "-c", "pass"], wrapped=True)
        self.assertIn("guards these processes only", out.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
