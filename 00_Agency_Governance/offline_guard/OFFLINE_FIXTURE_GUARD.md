# OFFLINE-FIXTURE-GUARD-1 — Offline Fixture Network Guard

**Owner decision:** 2026-10-01, in writing — *"I approve designing and implementing the smallest
durable repository-level offline guard required before a fixture may carry URL-shaped identifiers."*

**Status:** ✅ **Implemented and tested.** Inert until explicitly activated.

**What it is for.** To prevent **repository-operated offline fixture tests** from performing network
activity. It was built because the SYNCO-02 proposal (decision **D8**) found that the only network
blocks in existence were temporary files in a session scratchpad — and the Python half had already
vanished — so a future fixture carrying URL-shaped identifiers would have had no mechanical backstop
at all.

> ## 🔴 This is a prerequisite, not an authorization
>
> Implementing this guard **does not authorize creating or running any fixture.** It does not approve
> SYNCO-02, its sandbox, its records, any URL-bearing fixture file, `SECTOR-T2`, `SECTOR-PK2`, an S10
> run or a fixture-authorisation row. Each of those still needs its own owner decision. The guard
> only removes one blocker from the SYNCO-02 proposal's precondition list.

---

## 1. Architecture

Activation travels by **environment, not by in-process patching**, because a monkey-patch cannot
cross a process boundary. Three variables are set by the wrapper and inherited by children *and
grandchildren*, so `npm test` → `node --test` and `python -m unittest` → subprocess are both covered.

| File | Role |
|---|---|
| `offline_guard.py` | the Python guard. Patches nothing on import; `activate()` installs, `deactivate()` restores. |
| `sitecustomize.py` | the Python activation hook. CPython auto-imports a module of this name at startup **only if it is importable** — which happens only when this directory is on `PYTHONPATH`. |
| `offline_guard.mjs` | the Node guard, loaded by `--import`. Auto-activates **only** when the flag is set. |
| `run_offline.py` | the documented wrapper. Sets the three variables, runs one command, returns its exit code. |
| `test_offline_guard.py` | 31 Python tests. |
| `offline_guard.test.mjs` | 15 Node tests. |

**Two conditions must both hold before anything is patched:** the hook must be reachable
(`PYTHONPATH` / `NODE_OPTIONS`), **and** `ARIKA_OFFLINE_FIXTURE=1`. **The guard fails closed on
network use and fails *open* on activation — it never switches itself on.**

---

## 2. Activation commands

```bash
# Sector contract suite, guarded
python 00_Agency_Governance/offline_guard/run_offline.py -- \
    python -m unittest discover -s 01_Sector/contracts -p "test_skill_fixture.py"

# The guard's own Node suite, guarded
python 00_Agency_Governance/offline_guard/run_offline.py -- \
    node --test 00_Agency_Governance/offline_guard/offline_guard.test.mjs

# Runtime suite, guarded (npm test builds first, then runs node --test)
python 00_Agency_Governance/offline_guard/run_offline.py -- npm --prefix arika-runtime test

# In-process, for a Python evaluator that imports it directly
#   import offline_guard; offline_guard.activate()
```

**Environment set by the wrapper**

| Variable | Value |
|---|---|
| `ARIKA_OFFLINE_FIXTURE` | `1` — both guards require exactly this |
| `PYTHONPATH` | this directory, prepended (existing entries preserved) |
| `NODE_OPTIONS` | `--import file:///…/offline_guard.mjs`, as a **percent-encoded file URI** — `NODE_OPTIONS` splits on whitespace and does not honour quoting, so a bare path through *The Agency Drafts* would be parsed as several flags |

---

## 3. Exact coverage

Every entry below is asserted by a test that proves the call throws **before the underlying
transport function is reached**, using a tripwire in place of the real transport.

### Python — always patched (standard library)

| Category reported | Patched target |
|---|---|
| `socket.connect` | `socket.socket.connect` |
| `socket.connect_ex` | `socket.socket.connect_ex` |
| `socket.create_connection` | `socket.create_connection` |
| `dns.getaddrinfo` | `socket.getaddrinfo` |
| `dns.gethostbyname` | `socket.gethostbyname` |
| `dns.gethostbyname_ex` | `socket.gethostbyname_ex` |
| `dns.gethostbyaddr` | `socket.gethostbyaddr` |
| `http.client.HTTPConnection.connect` | `http.client.HTTPConnection.connect` |
| `http.client.HTTPSConnection.connect` | `http.client.HTTPSConnection.connect` |
| `urllib.request.urlopen` | `urllib.request.urlopen` |

### Python — patched only if already installed (no dependency is added)

| Category reported | Patched target | Present here |
|---|---|---|
| `requests.Session.request` | `requests.sessions.Session.request` | ✅ |
| `urllib3.HTTPConnectionPool.urlopen` | `urllib3.connectionpool.HTTPConnectionPool.urlopen` | ✅ |
| `httpx.Client.send` | `httpx.Client.send` | ✅ |
| `httpx.AsyncClient.send` | `httpx.AsyncClient.send` | ✅ |

A missing module is skipped silently. **Coverage does not depend on these** — the stdlib patches
already close the underlying transport; these exist so the error names the right layer.

### Node

| Category reported | Patched target |
|---|---|
| `net.Socket.connect` | `net.Socket.prototype.connect` |
| `net.connect` · `net.createConnection` | `net.connect`, `net.createConnection` |
| `tls.connect` · `tls.TLSSocket.connect` | `tls.connect`, `tls.TLSSocket.prototype.connect` |
| `dns.lookup` · `dns.resolve` · `dns.resolve4` · `dns.resolve6` | the `node:dns` callback API |
| `dns.promises.lookup` · `dns.promises.resolve` | `dns.promises` |
| `dns.Resolver.resolve` | `dns.Resolver.prototype.resolve` |
| `http.request` · `http.get` | `node:http` |
| `https.request` · `https.get` | `node:https` |
| `globalThis.fetch` | the global `fetch` |

**Runtime SDK transport.** The installed Anthropic SDK transports over global `fetch`, so patching
`globalThis.fetch` closes that path. A test asserts the global's identity rather than importing any
SDK or constructing a request.

**The `fetch` blocker throws synchronously** rather than returning a rejected promise. That is
deliberate: a floating promise can swallow a rejection, and a guard must not be silently
ignorable. `await fetch(...)` inside `try`/`catch` still catches it, and a test asserts an
*unhandled* block fails the process.

---

## 4. Error contract

```
OFFLINE_FIXTURE_NETWORK_BLOCKED: <api.category>
```

- Python: `offline_guard.OfflineFixtureNetworkBlocked` (a `RuntimeError`).
- Node: `OfflineFixtureNetworkBlocked`, with `.code = "OFFLINE_FIXTURE_NETWORK_BLOCKED"` and
  `.category`.

**The blocker discards every argument it was called with before raising.** No host, address, URL,
header, token, payload or request body can reach the message, the traceback or a log. Tests assert a
probe host, URL and fake secret appear in none of them.

**The wrapper banner prints the program name and the argument *count* only — never argument values**,
because a command line can legitimately contain a URL or a token. A test asserts this.

Neither guard reads or prints `.env` or any secret, and no file in this directory mentions a
credential variable name. Tests assert that too.

---

## 5. Explicit exclusions — what this guard does NOT control

**It guards the Python or Node process it was activated in, and that process' descendants via the
inherited environment. Nothing else.** It is not a firewall and must never be described as one.

It does **not** control:

1. **Claude Code MCP tools** — connector calls made by the assistant, not by a guarded process.
2. **Browser tools** — any web fetch or browse capability.
3. **Connectors** — ClickUp, Notion, Google Drive, Zoho and every other MCP server.
4. **External desktop applications.**
5. **Shell commands not launched through the wrapper**, including anything run directly in a
   terminal.
6. **Privileged processes** and anything that bypasses user-space Python or Node.
7. **Separately implemented transports** that reach the network without passing through the APIs in
   §3 — a native addon, a raw `_socket` call against a saved reference obtained before activation,
   or a child process in another language.

**Those remain procedurally prohibited by each individual fixture decision.** The guard reduces the
chance of an accident inside a guarded test; it does not and cannot replace the prohibition.

---

## 6. Production safety

**Ordinary execution is behaviourally unchanged.** Nothing in the repository imports, references or
preloads these files on any normal path:

- `sitecustomize.py` is reachable only when this directory is on `PYTHONPATH`, which only the
  wrapper arranges.
- `offline_guard.mjs` loads only when `NODE_OPTIONS` names it, which only the wrapper arranges.
- `offline_guard.py` patches nothing on import — `activate()` must be called.
- Even when both hooks are reachable, both require `ARIKA_OFFLINE_FIXTURE=1`.

No agent or skill specification was modified. No publishing, event-bus or runtime behaviour was
added. No dependency was created. `npm test` and the four non-runtime gates are unchanged, and
`arika-runtime/package.json` is untouched.

An installation failure is **printed as `OFFLINE_FIXTURE_GUARD_INSTALL_FAILED`** rather than
swallowed, so a guard that did not install can never be mistaken for one that did.

---

## 7. Tests

**46 tests, all passing: 31 Python + 15 Node.** None contacts the network — not an external address,
not DNS, not localhost.

| Area | What is proved |
|---|---|
| Guard inactive | importing patches nothing; mocked transport behaviour is unchanged; the guard never self-activates |
| Guard active | every category in §3 throws, and a tripwire proves the real transport was never reached |
| Error hygiene | the token and category are present; probe host, URL and fake secret appear in no message, `repr`, stack or traceback |
| Wrapper banner | argument values are not echoed |
| Secrets | no guard file mentions `dotenv` or a credential variable; the self-report prints no environment value |
| Wrapper environment | `build_env` is pure and tested directly: flag set, `PYTHONPATH` prepended and preserved, `NODE_OPTIONS` percent-encoded and space-free, idempotent |
| Child propagation | a guarded Python grandchild and a guarded Node grandchild both fail closed; an **unguarded** child of each is proved *not* guarded, by inspecting the function identity rather than by connecting |
| Loudness | an unhandled Node block fails the process |
| Restoration | `deactivate()` restores the exact original callables |

**Proof that the self-tests made no network attempt.** Coverage is asserted with tripwires: the real
transport function is replaced by a recorder *before* the guard is installed, so the guard wraps the
recorder. Each test asserts the recorder's call count is **0** — if a blocked call had ever reached
the underlying transport, the recorder would have fired and the test would fail. The child-process
tests target a `.invalid` host, which cannot resolve, and are blocked before resolution in any case.
The "not guarded" control tests read a function's type name instead of calling it.

---

## 8. Commands used by this repository, for reference

| Suite / gate | Command |
|---|---|
| Sector contracts | `python -m unittest discover -s 01_Sector/contracts -p "test_skill_fixture.py"` |
| Runtime | `npm --prefix arika-runtime test` (`tsc` build, then `node --test tests/*.test.mjs`) |
| Estate gate | `python 00_Agency_Governance/enterprise_architecture/estate_event_gate.py` |
| Sector truth gate | `python 01_Sector/contracts/sector_truth_gate.py` |
| Skill-run gate | `python 01_Sector/contracts/skill_run_gate.py` |
| P2 coverage gate | `python 01_Sector/contracts/p2_coverage_gate.py` |
| Build | `npm --prefix arika-runtime run build` |

Any of these may be prefixed with the wrapper. None requires it.

---

## 9. Limits of this record

The guard was built and tested against the APIs listed in §3 on this machine — Python 3.12.10, Node
v24.16.0, with `requests`, `urllib3` and `httpx` installed and `aiohttp` absent. A different
interpreter, a newer standard library, or a newly installed HTTP client could introduce a path not
covered here. §3's optional list is the place to extend, and **the stdlib layer is what guarantees
closure** if an extension is missed.

This record states what the guard does. It is **not** evidence that any fixture is safe to create or
run, and it changes no fixture decision, gate, Offer rule or Sector rule.
