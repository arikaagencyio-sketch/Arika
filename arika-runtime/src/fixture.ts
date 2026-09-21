/**
 * TEST_FIXTURE lane — isolation for simulation runs (A001).
 *
 * PREPARED, NOT ENABLED. `FIXTURE_LANE_ENABLED` stays `false` until the owner
 * approves the fixture-lane decision (A001 D21, drafted in
 * `01_Sector/A001_AGENCY_SYSTEMS_TEST_PLAN.md` §6.3 — NOT approved).
 *
 * The lane exists because a simulation run must never be mistakable for a real
 * one. Isolation is enforced two ways, and both fail closed:
 *
 *   1. a fixture run may write ONLY to a sandbox stream;
 *   2. an ordinary run may NEVER write to a sandbox stream.
 *
 * The sandbox stream is identified by filename (`sandbox.jsonl`), not by a flag
 * inside the line, so the separation survives a plain `cat`, a `grep`, or a
 * reader who does not know the marker exists.
 */
import { basename } from "node:path";

/**
 * Master switch. While `false`, `--fixture` is refused and the lane cannot run.
 * Flipping this is part of enacting the owner decision, not a code change on
 * its own.
 */
export const FIXTURE_LANE_ENABLED = false;

/** A memory stream is a sandbox stream if, and only if, it is named this. */
export const SANDBOX_BASENAME = "sandbox.jsonl";

/** Stamped at the top level of a fixture line, beside `source`. */
export const FIXTURE_CLASSIFICATION = "TEST_FIXTURE";

export interface FixtureOptions {
  fixture?: boolean;
  memoryStreamOverride?: string;
}

export function isSandboxStream(streamPath: string): boolean {
  return basename(streamPath.replace(/\\/g, "/")) === SANDBOX_BASENAME;
}

/**
 * The fail-closed guard. Throws before anything is written when the run mode
 * and the destination disagree — in either direction.
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
 * Maps CLI options onto run-context fields. Kept here, out of `cli.ts`, so it
 * can be tested without importing the CLI (which parses argv on import).
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
    throw new Error(`--fixture requires --memory-stream pointing at a ${SANDBOX_BASENAME} file.`);
  }
  return { fixture: true, memoryStreamOverride: opts.memoryStream };
}
