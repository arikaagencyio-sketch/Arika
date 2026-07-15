import { isAbsolute, join } from "node:path";
import { pathToFileURL } from "node:url";
import { repoRoot } from "../paths.js";
import type { AgentSpec } from "../spec-schema.js";
import type { RunContext } from "../executor.js";

/**
 * Wraps Finance's finos-plugin without adding it to this package's tsc graph:
 * finos ships a built `dist/`, so we dynamic-import its compiled output at
 * runtime and delegate `finance-*` agents to its own `ClaudeAgentRuntime`. finos
 * is left completely untouched.
 */

interface FinosAgentSpec {
  id: string;
  name: string;
  mission: string;
  humanApprovalRequiredFor: string[];
  systemPrompt: string;
  [k: string]: unknown;
}

interface FinosEvent {
  id: string;
  type: string;
  entityId: string;
  occurredAt: string;
  source: string;
  payload: Record<string, unknown>;
}

interface FinosRuntime {
  run(spec: FinosAgentSpec, event: FinosEvent, recent?: FinosEvent[]): Promise<Record<string, unknown>>;
}

interface FinosModule {
  financialAgentSpecs: FinosAgentSpec[];
  ClaudeAgentRuntime: new (apiKey?: string) => FinosRuntime;
}

let cached: FinosModule | undefined;

async function loadFinos(): Promise<FinosModule> {
  if (cached) return cached;
  const override = process.env.FINOS_DIST;
  const distBase = override
    ? isAbsolute(override)
      ? override
      : join(repoRoot, override)
    : join(repoRoot, "09_Finance", "finos-plugin", "dist");

  const indexMod = (await import(pathToFileURL(join(distBase, "ai-agents", "index.js")).href)) as {
    financialAgentSpecs: FinosAgentSpec[];
  };
  const runtimeMod = (await import(pathToFileURL(join(distBase, "ai-agents", "runtime.js")).href)) as {
    ClaudeAgentRuntime: new (apiKey?: string) => FinosRuntime;
  };

  cached = {
    financialAgentSpecs: indexMod.financialAgentSpecs,
    ClaudeAgentRuntime: runtimeMod.ClaudeAgentRuntime,
  };
  return cached;
}

export async function runFinosAgent(spec: AgentSpec, ctx: RunContext): Promise<Record<string, unknown>> {
  const finos = await loadFinos();
  const finosSpec = finos.financialAgentSpecs.find((s) => s.id === spec.finos_id);
  if (!finosSpec) {
    throw new Error(`finos agent "${spec.finos_id}" not found in finos-plugin (for agent ${spec.name}).`);
  }

  const input = ctx.input ?? {};
  const event: FinosEvent = {
    id: `arika-${Date.now()}`,
    type: (input.type as string) ?? ctx.eventType ?? "REVENUE_RECEIVED",
    entityId: (input.entityId as string) ?? "manual",
    occurredAt: new Date().toISOString(),
    source: "arika-runtime",
    payload: (input.payload as Record<string, unknown>) ?? input,
  };

  const runtime = new finos.ClaudeAgentRuntime();
  return runtime.run(finosSpec, event);
}
