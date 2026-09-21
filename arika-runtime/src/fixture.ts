/**
 * TEST_FIXTURE lane — isolation for simulation runs (A001).
 *
 * PREPARED, NOT ENABLED. `FIXTURE_LANE_ENABLED` stays `false` until the owner
 * approves the fixture-lane decision (A001 D21, drafted in
 * `01_Sector/A001_AGENCY_SYSTEMS_TEST_PLAN.md` §6.3 — NOT approved).
 *
 * Two layers, deliberately different in strength:
 *
 *   1. `assertStreamMatchesMode` — the coarse, always-on guard inside
 *      `writeMemory`. A fixture line may only land in a file named
 *      `sandbox.jsonl`; an ordinary line may never land in one. Defence in
 *      depth for any caller that reaches the writer directly.
 *
 *   2. `assertFixturePreconditions` — the real gate, called at the top of
 *      `runAgent` BEFORE any model call. It enforces the master switch, the one
 *      approved destination path, the approved agent, the approved unit, and
 *      single use. Nothing here costs an API call to discover.
 *
 * Isolation is carried by the filename, not by a flag inside the line, so the
 * separation survives a plain `cat`, a `grep`, or a reader who has never heard
 * of the marker.
 */
import { existsSync } from "node:fs";
import { join } from "node:path";
import { repoRoot } from "./paths.js";

/**
 * Master switch. While `false`, a fixture run is refused before anything else
 * is checked. Flipping this is part of enacting the owner decision.
 */
// A001 D21 authorised ONE attempt. It was made on 2026-09-21 and the authorisation
// is SPENT, so the lane is closed again. Re-opening needs a fresh owner decision.
// (The existing sandbox.jsonl independently blocks a second run via assertLaneUnused.)
export const FIXTURE_LANE_ENABLED = false;

/** A memory stream is a sandbox stream if, and only if, it is named this. */
export const SANDBOX_BASENAME = "sandbox.jsonl";

/** Stamped at the top level of a fixture line, beside `source`. */
export const FIXTURE_CLASSIFICATION = "TEST_FIXTURE";

/** The ONE destination this first lane may write to. Repo-relative, forward slashes. */
export const APPROVED_FIXTURE_STREAM = "02_Offer/_memory/sandbox.jsonl";

/** The ONE agent this first lane may run. */
export const APPROVED_FIXTURE_AGENT = "offer-orchestrator";

/** The ONE sandbox unit this first lane may carry. */
export const APPROVED_FIXTURE_UNIT = "A001-P07";

export interface FixtureOptions {
  fixture?: boolean;
  memoryStreamOverride?: string;
}

const norm = (p: string): string => p.replace(/\\/g, "/");

export function isSandboxStream(streamPath: string): boolean {
  return norm(streamPath).split("/").pop() === SANDBOX_BASENAME;
}

/**
 * Coarse guard, used by the writer. Fails closed in both directions so a real
 * run cannot pollute the lane and a fixture cannot leak out of it.
 */
export function assertStreamMatchesMode(streamPath: string, fixture: boolean): void {
  const sandbox = isSandboxStream(streamPath);
  if (fixture && !sandbox) {
    throw new Error(
      `fixture run refused: "${streamPath}" is not a sandbox stream (expected a file named ${SANDBOX_BASENAME}). Nothing was written.`,
    );
  }
  if (!fixture && sandbox) {
    throw new Error(
      `ordinary run refused: "${streamPath}" is a sandbox stream, reserved for ${FIXTURE_CLASSIFICATION} runs. Nothing was written.`,
    );
  }
}

/**
 * Exact destination check. A basename match is not enough: an absolute path, a
 * traversal, or another department's `sandbox.jsonl` would all pass that and
 * are all refused here.
 */
export function assertApprovedFixtureStream(streamPath: string): void {
  const p = norm(streamPath);
  if (/^[A-Za-z]:/.test(p) || p.startsWith("/")) {
    throw new Error(
      `fixture run refused: "${streamPath}" is an absolute path. The lane writes only to the repo-relative ${APPROVED_FIXTURE_STREAM}.`,
    );
  }
  if (p.split("/").includes("..")) {
    throw new Error(`fixture run refused: "${streamPath}" contains a path traversal segment.`);
  }
  if (p !== APPROVED_FIXTURE_STREAM) {
    throw new Error(
      `fixture run refused: "${streamPath}" is not the approved destination. This lane may write only to ${APPROVED_FIXTURE_STREAM}.`,
    );
  }
}

/**
 * The brief is a free-text string, so this is a text check, not a schema check —
 * weaker than the path and agent pins, and honest about it. It catches the
 * mistakes worth catching: a missing marker, another sandbox unit, a real pilot ID.
 */
export function assertApprovedFixtureInput(input: unknown): void {
  const brief = (input as { seed_brief?: unknown } | undefined)?.seed_brief;
  if (typeof brief !== "string" || brief.trim() === "") {
    throw new Error('fixture run refused: input must carry a non-empty string "seed_brief".');
  }
  if (!brief.includes(FIXTURE_CLASSIFICATION)) {
    throw new Error(
      `fixture run refused: the brief does not declare ${FIXTURE_CLASSIFICATION}.`,
    );
  }
  if (!brief.includes(APPROVED_FIXTURE_UNIT)) {
    throw new Error(`fixture run refused: the brief does not name ${APPROVED_FIXTURE_UNIT}.`);
  }
  const others = [...new Set((brief.match(/A001-P\d{2}/g) ?? []).filter((u) => u !== APPROVED_FIXTURE_UNIT))];
  if (others.length) {
    throw new Error(
      `fixture run refused: the brief names other sandbox units (${others.join(", ")}). This lane is ${APPROVED_FIXTURE_UNIT} only.`,
    );
  }
  if (/PILOT-H-\d/.test(brief)) {
    throw new Error("fixture run refused: the brief names a real pilot ID. The lane is simulation only.");
  }
}

/**
 * Single-use control: the lane is spent once its destination exists. Cheap,
 * deterministic and file-system-backed — no counter to drift.
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
  opts: { enabled?: boolean; resolve?: (s: string) => string } = {},
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
      "The TEST_FIXTURE lane is prepared but NOT enabled. It stays closed until the owner approves the fixture-lane decision (A001 D21, draft). Nothing was run.",
    );
  }
  if (!ctx.memoryStreamOverride) {
    throw new Error(`fixture run refused: a destination is required (${APPROVED_FIXTURE_STREAM}).`);
  }
  assertApprovedFixtureStream(ctx.memoryStreamOverride);
  if (agentName !== APPROVED_FIXTURE_AGENT) {
    throw new Error(
      `fixture run refused: "${agentName}" is not the approved agent. This lane may run only ${APPROVED_FIXTURE_AGENT}.`,
    );
  }
  assertApprovedFixtureInput(ctx.input);
  assertLaneUnused(ctx.memoryStreamOverride, opts.resolve ?? ((s) => join(repoRoot, s)));
}

/**
 * Maps CLI options onto run-context fields. Kept out of `cli.ts` so it can be
 * tested without importing the CLI, which parses argv on import.
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
      "The TEST_FIXTURE lane is prepared but NOT enabled. It stays closed until the owner approves the fixture-lane decision (A001 D21, draft). Nothing was run.",
    );
  }
  if (!opts.memoryStream) {
    throw new Error(`--fixture requires --memory-stream ${APPROVED_FIXTURE_STREAM}`);
  }
  assertApprovedFixtureStream(opts.memoryStream);
  return { fixture: true, memoryStreamOverride: opts.memoryStream };
}
