// OFFLINE-FIXTURE-GUARD-1 - focused tests for the Node half.
//
// NO TEST CONTACTS THE NETWORK - not an external address, not DNS, not localhost. Coverage is
// proved with TRIPWIRES: the real transport is replaced by a recorder BEFORE the guard is
// installed, so the guard wraps the recorder. If a blocked call ever reached the underlying
// transport the recorder would fire, and each test asserts it never does.
//
//   node --test 00_Agency_Governance/offline_guard/offline_guard.test.mjs

import test from "node:test";
import assert from "node:assert/strict";
import net from "node:net";
import tls from "node:tls";
import http from "node:http";
import https from "node:https";
import dns from "node:dns";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

import {
  activate, deactivate, isActive, coveredCategories, activationRequested,
  ERROR_TOKEN, ENV_FLAG, OfflineFixtureNetworkBlocked,
} from "./offline_guard.mjs";

const HERE = path.dirname(fileURLToPath(import.meta.url));
const FAKE_HOST = "guard-probe-host.invalid";
const FAKE_URL = "https://guard-probe-host.invalid/secret-path";
const FAKE_SECRET = "sk-ant-GUARDPROBE-NOT-A-REAL-KEY";

/** Replace owner[key] with a recorder, returning it plus an undo. */
function tripwire(owner, key) {
  const original = owner[key];
  const wire = function offline_guard_tripwire() {
    wire.calls += 1;
    return "TRIPWIRE_REACHED";
  };
  wire.calls = 0;
  owner[key] = wire;
  return { wire, undo: () => { owner[key] = original; } };
}

/** Run fn with the guard freshly installed over any tripwires, then restore everything. */
function guarded(fn) {
  const wasActive = isActive();
  deactivate();
  try {
    activate();
    fn();
  } finally {
    deactivate();
    if (wasActive) activate();
  }
}

function blockedBy(fn) {
  try {
    fn();
  } catch (e) {
    return e;
  }
  return null;
}

test("the guard never switches itself on", () => {
  const wasActive = isActive();
  deactivate();
  assert.equal(isActive(), false);
  assert.deepEqual(coveredCategories(), []);
  if (wasActive) activate();
});

test("guard inactive: ordinary mocked transport behaviour is unchanged", () => {
  const wasActive = isActive();
  deactivate();
  const t = tripwire(dns, "lookup");
  try {
    assert.equal(dns.lookup(FAKE_HOST, () => {}), "TRIPWIRE_REACHED");
    assert.equal(t.wire.calls, 1);
  } finally {
    t.undo();
    if (wasActive) activate();
  }
});

test("guard active: every required category is covered", () => {
  guarded(() => {
    const covered = coveredCategories();
    for (const c of ["net.Socket.connect", "net.connect", "net.createConnection", "tls.connect",
                     "dns.lookup", "dns.promises.lookup", "http.request", "http.get",
                     "https.request", "https.get", "globalThis.fetch"]) {
      assert.ok(covered.includes(c), `missing category: ${c}`);
    }
  });
});

test("net connection paths fail closed before the transport", () => {
  const wasActive = isActive();
  deactivate();
  const a = tripwire(net.Socket.prototype, "connect");
  const b = tripwire(net, "connect");
  const c = tripwire(net, "createConnection");
  try {
    activate();
    for (const call of [() => new net.Socket().connect(443, FAKE_HOST),
                        () => net.connect(443, FAKE_HOST),
                        () => net.createConnection(443, FAKE_HOST)]) {
      const err = blockedBy(call);
      assert.ok(err instanceof OfflineFixtureNetworkBlocked, "expected a guard error");
      assert.match(err.message, new RegExp(ERROR_TOKEN));
    }
    assert.deepEqual([a.wire.calls, b.wire.calls, c.wire.calls], [0, 0, 0],
      "the guard must throw BEFORE the transport is reached");
  } finally {
    deactivate(); a.undo(); b.undo(); c.undo();
    if (wasActive) activate();
  }
});

test("tls connection path fails closed before the transport", () => {
  const wasActive = isActive();
  deactivate();
  const t = tripwire(tls, "connect");
  try {
    activate();
    assert.ok(blockedBy(() => tls.connect(443, FAKE_HOST)) instanceof OfflineFixtureNetworkBlocked);
    assert.equal(t.wire.calls, 0);
  } finally {
    deactivate(); t.undo();
    if (wasActive) activate();
  }
});

test("dns lookup and resolve paths fail closed before the transport", () => {
  const wasActive = isActive();
  deactivate();
  const a = tripwire(dns, "lookup");
  const b = tripwire(dns, "resolve");
  const c = tripwire(dns.promises, "lookup");
  try {
    activate();
    assert.ok(blockedBy(() => dns.lookup(FAKE_HOST, () => {})) instanceof OfflineFixtureNetworkBlocked);
    assert.ok(blockedBy(() => dns.resolve(FAKE_HOST, () => {})) instanceof OfflineFixtureNetworkBlocked);
    assert.ok(blockedBy(() => dns.promises.lookup(FAKE_HOST)) instanceof OfflineFixtureNetworkBlocked);
    assert.deepEqual([a.wire.calls, b.wire.calls, c.wire.calls], [0, 0, 0]);
  } finally {
    deactivate(); a.undo(); b.undo(); c.undo();
    if (wasActive) activate();
  }
});

test("http and https request paths fail closed before the transport", () => {
  const wasActive = isActive();
  deactivate();
  const wires = [tripwire(http, "request"), tripwire(http, "get"),
                 tripwire(https, "request"), tripwire(https, "get")];
  try {
    activate();
    for (const call of [() => http.request(FAKE_URL), () => http.get(FAKE_URL),
                        () => https.request(FAKE_URL), () => https.get(FAKE_URL)]) {
      assert.ok(blockedBy(call) instanceof OfflineFixtureNetworkBlocked);
    }
    assert.deepEqual(wires.map((w) => w.wire.calls), [0, 0, 0, 0]);
  } finally {
    deactivate(); wires.reverse().forEach((w) => w.undo());
    if (wasActive) activate();
  }
});

test("global fetch fails closed before the transport", () => {
  const wasActive = isActive();
  deactivate();
  const t = tripwire(globalThis, "fetch");
  try {
    activate();
    const err = blockedBy(() => globalThis.fetch(FAKE_URL));
    assert.ok(err instanceof OfflineFixtureNetworkBlocked);
    assert.equal(err.category, "globalThis.fetch");
    assert.equal(t.wire.calls, 0);
  } finally {
    deactivate(); t.undo();
    if (wasActive) activate();
  }
});

test("blocking global fetch closes the installed SDK transport path", () => {
  // The Anthropic SDK ultimately transports over global fetch. Asserting the identity of the
  // global is enough - no SDK is imported and no request is constructed.
  guarded(() => {
    assert.equal(globalThis.fetch.offlineGuardCategory, "globalThis.fetch");
  });
});

test("the error names the API category and carries the token", () => {
  guarded(() => {
    const err = blockedBy(() => https.request(FAKE_URL));
    assert.equal(err.code, ERROR_TOKEN);
    assert.equal(err.category, "https.request");
    assert.match(err.message, /^OFFLINE_FIXTURE_NETWORK_BLOCKED: https\.request$/);
  });
});

test("no hostname, URL or secret leaks into the error or its stack", () => {
  guarded(() => {
    const err = blockedBy(() => globalThis.fetch(FAKE_URL, {
      headers: { authorization: `Bearer ${FAKE_SECRET}` },
      body: JSON.stringify({ secret: FAKE_SECRET }),
    }));
    const text = `${err.message} || ${String(err)} || ${err.stack}`;
    for (const leak of [FAKE_HOST, FAKE_URL, FAKE_SECRET, "guard-probe-host", "GUARDPROBE",
                        "Bearer", "authorization"]) {
      assert.ok(!text.includes(leak), `leaked: ${leak}`);
    }
  });
});

test("deactivate restores the exact originals", () => {
  const wasActive = isActive();
  deactivate();
  const t = tripwire(globalThis, "fetch");
  try {
    activate();
    assert.notEqual(globalThis.fetch, t.wire);
    deactivate();
    assert.equal(globalThis.fetch, t.wire, "deactivate must restore the exact original");
  } finally {
    t.undo();
    if (wasActive) activate();
  }
});

test("activation is idempotent", () => {
  guarded(() => {
    const first = coveredCategories().length;
    activate();
    assert.equal(coveredCategories().length, first);
  });
});

test("activation is driven only by the explicit environment flag", () => {
  assert.equal(activationRequested(), process.env[ENV_FLAG] === "1");
  assert.equal(ENV_FLAG, "ARIKA_OFFLINE_FIXTURE");
});

test("the guard source reads no secret and no dotenv", () => {
  for (const name of ["offline_guard.mjs", "offline_guard.py", "sitecustomize.py",
                      "run_offline.py"]) {
    const src = fs.readFileSync(path.join(HERE, name), "utf8");
    assert.ok(!src.toLowerCase().includes("dotenv"), name);
    for (const forbidden of ["ANTHROPIC_API_KEY", "CLICKUP_TOKEN", "NOTION_TOKEN"]) {
      assert.ok(!src.includes(forbidden), `${name} mentions ${forbidden}`);
    }
  }
});
