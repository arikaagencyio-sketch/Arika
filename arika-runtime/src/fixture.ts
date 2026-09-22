/**
 * TEST_FIXTURE lane — isolation for simulation runs.
 *
 * CLOSED. `FIXTURE_LANE_ENABLED` is `false`, and no authorisation below is
 * `approved`. A fixture run needs BOTH the master switch on AND a matching
 * authorisation marked `approved` — two separate edits, each tied to a written
 * owner decision.
 *
 * Two layers, deliberately different in strength:
 *
 *   1. `assertStreamMatchesMode` — the coarse, always-on guard inside
 *      `writeMemory`. A fixture line may only land in a sandbox-named file; an
 *      ordinary line may never land in one. Defence in depth for any caller that
 *      reaches the writer directly.
 *
 *   2. `assertFixturePreconditions` — the real gate, called at the top of
 *      `runAgent` BEFORE any model call. It resolves the destination to exactly
 *      one registered authorisation and enforces that authorisation's status,
 *      agent, input and single use. Nothing here costs an API call to discover.
 *
 * Isolation is carried by the filename, not by a flag inside the line, so the
 * separation survives a plain `cat`, a `grep`, or a reader who has never heard
 * of the marker.
 */
import { createHash } from "node:crypto";
import { existsSync } from "node:fs";
import { join } from "node:path";
import { repoRoot } from "./paths.js";

/**
 * Master switch. While `false`, every fixture run is refused before anything
 * else is checked. A001 D21 used and SPENT its one attempt on 2026-09-21; the
 * lane has been closed since.
 */
export const FIXTURE_LANE_ENABLED = false; // closed again 2026-09-22 after OFFER-F2's one attempt

/** Stamped at the top level of a fixture line, beside `source`. */
export const FIXTURE_CLASSIFICATION = "TEST_FIXTURE";

/** `sandbox.jsonl` or `sandbox-<id>.jsonl`. Every such name is reserved for fixtures. */
const SANDBOX_NAME = /^sandbox(?:-[a-z0-9]+)*\.jsonl$/;

export type AuthorisationStatus = "draft" | "approved" | "spent";

export interface FixtureAuthorisation {
  /** Stable id, also used as the input marker where one is required. */
  id: string;
  /** Where the owner decision behind this authorisation is recorded. */
  record: string;
  /** Only `approved` may run. `draft` awaits the owner; `spent` has been used. */
  status: AuthorisationStatus;
  /** The ONE agent this authorisation may run. */
  agent: string;
  /** The ONE destination it may write to. Repo-relative, forward slashes. */
  stream: string;
  /** Substrings the brief must contain. */
  requiredMarkers: readonly string[];
  /** Patterns the brief must not contain. Each must carry the `g` flag. */
  forbidden: readonly { pattern: RegExp; reason: string }[];
  /** When set, the brief must match this exactly (sha256 of the UTF-8 seed_brief). */
  inputSha256?: string;
}

/**
 * Every fixture authorisation that has ever existed. Entries are never
 * deleted: a spent one stays so its stream stays reserved and refused.
 */
export const FIXTURE_AUTHORISATIONS: readonly FixtureAuthorisation[] = [
  {
    id: "A001-D21",
    record: "01_Sector/A001_HOSPITALITY_SECTOR_SANDBOX.md §5.1 D21",
    status: "spent", // one attempt made 2026-09-21; returned reject
    agent: "offer-orchestrator",
    stream: "02_Offer/_memory/sandbox.jsonl",
    requiredMarkers: ["TEST_FIXTURE", "A001-P07"],
    forbidden: [
      { pattern: /A001-P(?!07\b)\d{2}/g, reason: "names other sandbox units" },
      { pattern: /PILOT-H-\d+/g, reason: "names a real pilot ID" },
    ],
  },
  {
    id: "OFFER-F2",
    record: "02_Offer/OFFER_OS.md §8 — decision OFFER-F2 (enacted and SPENT 2026-09-22)",
    status: "spent", // one attempt made 2026-09-22; see OFFER_OS §8 attempt record
    agent: "offer-oeos-engineer",
    stream: "02_Offer/_memory/sandbox-offer-f2.jsonl",
    requiredMarkers: ["TEST_FIXTURE", "OFFER-F2", "UNRESOLVED", "PHASE 11: BLOCKED", "NON-PRICING"],
    forbidden: [
      { pattern: /\bA001\b/g, reason: "names an A001 sandbox record — this fixture carries none" },
      { pattern: /PILOT-H-\d+/g, reason: "names a real pilot ID" },
      { pattern: /[$€£]|\b(?:USD|KES|KSh|EUR|GBP)\b/g, reason: "contains a currency figure" },
    ],
    inputSha256: "89c5fde1af9c23cbfad3a81ab53554258aa9530d74e7e21aa211288f561da5b0",
  },
];

export interface FixtureOptions {
  fixture?: boolean;
  memoryStreamOverride?: string;
}

const norm = (p: string): string => p.replace(/\\/g, "/");

export function isSandboxStream(streamPath: string): boolean {
  return SANDBOX_NAME.test(norm(streamPath).split("/").pop() ?? "");
}

/**
 * Registry integrity. Run at load, so a malformed registry fails closed before
 * any run can consult it.
 */
export function validateAuthorisations(auths: readonly FixtureAuthorisation[]): void {
  const ids = new Set<string>();
  const streams = new Set<string>();
  for (const a of auths) {
    const p = norm(a.stream);
    if (/^[A-Za-z]:/.test(p) || p.startsWith("/") || p.split("/").includes("..")) {
      throw new Error(`fixture registry invalid: "${a.id}" stream must be repo-relative with no traversal.`);
    }
    if (!isSandboxStream(p)) {
      throw new Error(`fixture registry invalid: "${a.id}" stream "${p}" is not sandbox-named.`);
    }
    if (ids.has(a.id)) throw new Error(`fixture registry invalid: duplicate id "${a.id}".`);
    if (streams.has(p)) throw new Error(`fixture registry invalid: two authorisations share "${p}".`);
    for (const f of a.forbidden) {
      if (!f.pattern.global) throw new Error(`fixture registry invalid: "${a.id}" forbidden pattern lacks the g flag.`);
    }
    ids.add(a.id);
    streams.add(p);
  }
}
validateAuthorisations(FIXTURE_AUTHORISATIONS);

/**
 * Coarse guard, used by the writer. Fails closed in both directions so a real
 * run cannot pollute a fixture stream and a fixture cannot leak out of one.
 */
export function assertStreamMatchesMode(streamPath: string, fixture: boolean): void {
  const sandbox = isSandboxStream(streamPath);
  if (fixture && !sandbox) {
    throw new Error(
      `fixture run refused: "${streamPath}" is not a sandbox stream (expected sandbox.jsonl or sandbox-<id>.jsonl). Nothing was written.`,
    );
  }
  if (!fixture && sandbox) {
    throw new Error(
      `ordinary run refused: "${streamPath}" is a sandbox stream, reserved for ${FIXTURE_CLASSIFICATION} runs. Nothing was written.`,
    );
  }
}

/**
 * Exact destination check. Resolves the path to the ONE registered
 * authorisation that owns it. A basename match is not enough: an absolute path,
 * a traversal, or an unregistered `sandbox*.jsonl` are all refused.
 */
export function assertApprovedFixtureStream(
  streamPath: string,
  auths: readonly FixtureAuthorisation[] = FIXTURE_AUTHORISATIONS,
): FixtureAuthorisation {
  const p = norm(streamPath);
  if (/^[A-Za-z]:/.test(p) || p.startsWith("/")) {
    throw new Error(
      `fixture run refused: "${streamPath}" is an absolute path. Fixture destinations are repo-relative.`,
    );
  }
  if (p.split("/").includes("..")) {
    throw new Error(`fixture run refused: "${streamPath}" contains a path traversal segment.`);
  }
  const auth = auths.find((a) => a.stream === p);
  if (!auth) {
    throw new Error(
      `fixture run refused: "${streamPath}" is not the approved destination for any fixture authorisation (${auths.map((a) => a.stream).join(", ")}).`,
    );
  }
  return auth;
}

const sha256 = (s: string): string => createHash("sha256").update(s, "utf8").digest("hex");

/**
 * Input check for one authorisation. Where a hash is pinned this is an exact
 * match, not a text heuristic; otherwise it is the weaker marker/pattern check.
 */
export function assertApprovedFixtureInput(input: unknown, auth: FixtureAuthorisation): void {
  const brief = (input as { seed_brief?: unknown } | undefined)?.seed_brief;
  if (typeof brief !== "string" || brief.trim() === "") {
    throw new Error('fixture run refused: input must carry a non-empty string "seed_brief".');
  }
  for (const marker of auth.requiredMarkers) {
    if (!brief.includes(marker)) {
      throw new Error(`fixture run refused: the brief does not declare ${marker} (${auth.id}).`);
    }
  }
  for (const f of auth.forbidden) {
    const hits = [...new Set(brief.match(f.pattern) ?? [])];
    if (hits.length) {
      throw new Error(`fixture run refused: the brief ${f.reason} (${hits.join(", ")}).`);
    }
  }
  if (auth.inputSha256 && sha256(brief) !== auth.inputSha256) {
    throw new Error(
      `fixture run refused: the brief does not match the approved input for ${auth.id} (sha256 mismatch). Only the exact recorded input may run.`,
    );
  }
}

/**
 * Single-use control: an authorisation is spent once its destination exists.
 * This guards against a SECOND COMPLETED WRITE. It cannot count API attempts —
 * an attempt that fails before the write leaves no file — so attempt-counting
 * stays an owner procedure (see the decision record).
 */
export function assertLaneUnused(streamPath: string, resolve: (s: string) => string): void {
  if (existsSync(resolve(streamPath))) {
    throw new Error(
      `fixture run refused: "${streamPath}" already exists, so this one-run lane is spent. A second run needs a new owner decision.`,
    );
  }
}

/**
 * The gate. Called at the top of `runAgent`, before any model or API call, so a
 * misconfigured fixture run costs nothing. An ordinary run returns immediately
 * and is completely unaffected.
 */
export function assertFixturePreconditions(
  agentName: string,
  ctx: { fixture?: boolean; memoryStreamOverride?: string; input?: Record<string, unknown> },
  opts: {
    enabled?: boolean;
    resolve?: (s: string) => string;
    authorisations?: readonly FixtureAuthorisation[];
  } = {},
): void {
  if (!ctx.fixture) {
    if (ctx.memoryStreamOverride) {
      throw new Error("memoryStreamOverride requires fixture mode.");
    }
    return;
  }
  const enabled = opts.enabled ?? FIXTURE_LANE_ENABLED;
  if (!enabled) {
    throw new Error(
      "The TEST_FIXTURE lane is prepared but NOT enabled. It stays closed until the owner approves a fixture decision and the switch is set. Nothing was run.",
    );
  }
  if (!ctx.memoryStreamOverride) {
    throw new Error("fixture run refused: a destination is required (a registered sandbox stream).");
  }
  const auth = assertApprovedFixtureStream(ctx.memoryStreamOverride, opts.authorisations ?? FIXTURE_AUTHORISATIONS);
  if (auth.status === "draft") {
    throw new Error(
      `fixture run refused: ${auth.id} is a DRAFT authorisation — not approved by the owner (${auth.record}).`,
    );
  }
  if (auth.status === "spent") {
    throw new Error(`fixture run refused: ${auth.id} is SPENT — its one attempt has been used (${auth.record}).`);
  }
  if (agentName !== auth.agent) {
    throw new Error(
      `fixture run refused: "${agentName}" is not the approved agent for ${auth.id}. It may run only ${auth.agent}.`,
    );
  }
  assertApprovedFixtureInput(ctx.input, auth);
  assertLaneUnused(ctx.memoryStreamOverride, opts.resolve ?? ((s) => join(repoRoot, s)));
}

/**
 * Maps CLI options onto run-context fields. Kept out of `cli.ts` so it can be
 * tested without importing the CLI, which parses argv on import. Status, agent
 * and input are left to the gate, which sees the agent name.
 */
export function buildFixtureOptions(
  opts: { fixture?: boolean; memoryStream?: string },
  enabled: boolean = FIXTURE_LANE_ENABLED,
): FixtureOptions {
  if (!opts.fixture) {
    if (opts.memoryStream) {
      throw new Error("--memory-stream requires --fixture.");
    }
    return {};
  }
  if (!enabled) {
    throw new Error(
      "The TEST_FIXTURE lane is prepared but NOT enabled. It stays closed until the owner approves a fixture decision and the switch is set. Nothing was run.",
    );
  }
  if (!opts.memoryStream) {
    throw new Error("--fixture requires --memory-stream <a registered sandbox stream>");
  }
  assertApprovedFixtureStream(opts.memoryStream);
  return { fixture: true, memoryStreamOverride: opts.memoryStream };
}
