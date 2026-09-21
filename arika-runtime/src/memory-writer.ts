import { appendFileSync, mkdirSync } from "node:fs";
import { dirname, isAbsolute, join } from "node:path";
import { repoRoot } from "./paths.js";
import type { AgentSpec } from "./spec-schema.js";
import {
  assertStreamMatchesMode,
  FIXTURE_CLASSIFICATION,
  type FixtureOptions,
} from "./fixture.js";

/** The payload of one memory line. Extra keys are allowed. */
export interface MemoryEntry {
  trigger: string;
  input: unknown;
  recommendation: unknown;
  requiresHumanApproval: boolean;
  riskClass: number;
  [k: string]: unknown;
}

/**
 * Append one JSONL line to the spec's `memory_stream`, in the bois-compatible
 * envelope (the only live machine-written log format in the repo — see
 * 12_Branding/bois/core/memory/store.py). Returns the resolved path, or null if
 * the spec declares no memory stream.
 *
 * `opts` carries the TEST_FIXTURE lane (see fixture.ts). It is inert unless a
 * caller passes it: with no options the resolved path, the envelope and its key
 * order are exactly what they were before the lane existed, so ordinary runs are
 * byte-identical. When `fixture` is set, the destination is guarded first and a
 * `classification` key is stamped beside `source`.
 */
export function writeMemory(
  spec: AgentSpec,
  entry: MemoryEntry,
  opts: FixtureOptions = {},
): string | null {
  const stream = opts.memoryStreamOverride ?? spec.memory_stream;
  if (!stream) return null;

  // Fail closed BEFORE any directory or file is touched.
  assertStreamMatchesMode(stream, opts.fixture === true);

  const target = isAbsolute(stream) ? stream : join(repoRoot, stream);
  mkdirSync(dirname(target), { recursive: true });
  const name = stream.split(/[\\/]/).pop()?.replace(/\.jsonl$/, "") ?? "runtime";
  const line = JSON.stringify({
    timestamp: new Date().toISOString(),
    agent: spec.name,
    department: spec.department,
    stream: name,
    event_type: "agent_run",
    source: "arika-runtime",
    ...(opts.fixture ? { classification: FIXTURE_CLASSIFICATION } : {}),
    payload: entry,
  });
  appendFileSync(target, line + "\n", "utf8");
  return target;
}
