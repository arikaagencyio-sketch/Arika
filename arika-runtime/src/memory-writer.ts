import { appendFileSync, mkdirSync } from "node:fs";
import { dirname, isAbsolute, join } from "node:path";
import { repoRoot } from "./paths.js";
import type { AgentSpec } from "./spec-schema.js";

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
 */
export function writeMemory(spec: AgentSpec, entry: MemoryEntry): string | null {
  if (!spec.memory_stream) return null;
  const target = isAbsolute(spec.memory_stream)
    ? spec.memory_stream
    : join(repoRoot, spec.memory_stream);
  mkdirSync(dirname(target), { recursive: true });
  const stream = spec.memory_stream.split(/[\\/]/).pop()?.replace(/\.jsonl$/, "") ?? "runtime";
  const line = JSON.stringify({
    timestamp: new Date().toISOString(),
    agent: spec.name,
    department: spec.department,
    stream,
    event_type: "agent_run",
    source: "arika-runtime",
    payload: entry,
  });
  appendFileSync(target, line + "\n", "utf8");
  return target;
}
