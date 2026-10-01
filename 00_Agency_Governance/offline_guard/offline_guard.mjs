// OFFLINE-FIXTURE-GUARD-1 - Node half.
//
// Fails closed on network use inside a process that has EXPLICITLY enabled it. Loaded via
//   NODE_OPTIONS=--import file:///<this file>
// which `run_offline.py` sets for a child command and its descendants. It auto-activates ONLY when
// ARIKA_OFFLINE_FIXTURE=1, so importing it without that flag patches nothing.
//
// WHAT THIS DOES NOT CONTROL - see OFFLINE_FIXTURE_GUARD.md section 5. It guards THIS Node process
// only: not Claude Code tools, MCP servers, browsers, connectors, desktop applications, shell
// commands launched outside the guarded entry point, privileged processes, or a native transport
// that reaches the network without passing through the APIs below.
//
// It adds no dependency, makes no network call, needs no administrator access and reads no secret.

import net from "node:net";
import tls from "node:tls";
import http from "node:http";
import https from "node:https";
import dns from "node:dns";

export const ENV_FLAG = "ARIKA_OFFLINE_FIXTURE";
export const ERROR_TOKEN = "OFFLINE_FIXTURE_NETWORK_BLOCKED";

export class OfflineFixtureNetworkBlocked extends Error {
  constructor(category) {
    // Carries the API CATEGORY and nothing else. Every argument the blocked call was made with is
    // discarded before this is constructed, so no host, URL, header, token or body can leak.
    super(`${ERROR_TOKEN}: ${category}`);
    this.name = "OfflineFixtureNetworkBlocked";
    this.category = category;
    this.code = ERROR_TOKEN;
  }
}

const state = { active: false, restore: [], categories: [] };

const blocker = (category) => {
  const denied = function offline_guard_blocked() {
    throw new OfflineFixtureNetworkBlocked(category);
  };
  denied.offlineGuardCategory = category;
  return denied;
};

function patch(owner, key, category) {
  if (!owner || typeof owner[key] === "undefined") return false;
  const original = owner[key];
  if (original && original.offlineGuardCategory) return false; // already guarded
  try {
    owner[key] = blocker(category);
  } catch {
    return false; // non-writable target - skipped, and reported as not covered
  }
  state.restore.push([owner, key, original]);
  state.categories.push(category);
  return true;
}

/** Install the guard in THIS process. Idempotent. Returns the covered categories. */
export function activate() {
  if (state.active) return [...state.categories];

  // Connection primitives first: closure must not depend on the higher-level wrappers.
  patch(net.Socket.prototype, "connect", "net.Socket.connect");
  patch(net, "connect", "net.connect");
  patch(net, "createConnection", "net.createConnection");
  patch(tls, "connect", "tls.connect");
  if (tls.TLSSocket && tls.TLSSocket.prototype) {
    patch(tls.TLSSocket.prototype, "connect", "tls.TLSSocket.connect");
  }

  // DNS
  patch(dns, "lookup", "dns.lookup");
  patch(dns, "resolve", "dns.resolve");
  patch(dns, "resolve4", "dns.resolve4");
  patch(dns, "resolve6", "dns.resolve6");
  if (dns.promises) {
    patch(dns.promises, "lookup", "dns.promises.lookup");
    patch(dns.promises, "resolve", "dns.promises.resolve");
  }
  if (dns.Resolver && dns.Resolver.prototype) {
    patch(dns.Resolver.prototype, "resolve", "dns.Resolver.resolve");
  }

  // HTTP / HTTPS standard clients
  patch(http, "request", "http.request");
  patch(http, "get", "http.get");
  patch(https, "request", "https.request");
  patch(https, "get", "https.get");

  // Global fetch. This is also the transport the installed Anthropic SDK ultimately uses, so
  // blocking it here closes that path without naming or importing any SDK.
  patch(globalThis, "fetch", "globalThis.fetch");

  state.active = true;
  return [...state.categories];
}

/** Restore every patched property, most recent first. Used by the guard's own tests. */
export function deactivate() {
  for (let i = state.restore.length - 1; i >= 0; i -= 1) {
    const [owner, key, original] = state.restore[i];
    try {
      owner[key] = original;
    } catch {
      /* best effort */
    }
  }
  state.restore = [];
  state.categories = [];
  state.active = false;
}

export const isActive = () => state.active;
export const coveredCategories = () => [...state.categories];
export const activationRequested = () => process.env[ENV_FLAG] === "1";

// Auto-activate ONLY on explicit request. Never switches itself on.
if (activationRequested()) activate();
