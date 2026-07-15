import Anthropic from "@anthropic-ai/sdk";
import type { AgentSpec } from "./spec-schema.js";
import { baseOutputSchema } from "./spec-schema.js";
import { requiresHumanApproval } from "./governance.js";
import { writeMemory } from "./memory-writer.js";
import { runFinosAgent } from "./wrappers/finos.js";
import { runBoisAgent } from "./wrappers/bois.js";

export interface RunContext {
  /** manual | schedule | event | webhook */
  trigger: string;
  input?: Record<string, unknown>;
  eventType?: string;
  recentContext?: string[];
}

export interface RunResult {
  agent: string;
  execution: string;
  requiresHumanApproval: boolean;
  riskClass: number;
  recommendation: Record<string, unknown>;
  memoryPath: string | null;
  emitted: string[];
}

let client: Anthropic | undefined;
function getClient(): Anthropic {
  if (!client) {
    const apiKey = process.env.ANTHROPIC_API_KEY;
    if (!apiKey) {
      throw new Error(
        "ANTHROPIC_API_KEY is not set — cannot invoke agents. Add it to arika-runtime/.env or your shell environment.",
      );
    }
    client = new Anthropic({ apiKey });
  }
  return client;
}

/**
 * The single execution path. Every trigger (manual/schedule/event/webhook)
 * assembles a `RunContext` and calls this. Advisory-first: it returns a
 * recommendation and writes memory; it never performs a state-changing action.
 */
export async function runAgent(spec: AgentSpec, ctx: RunContext): Promise<RunResult> {
  const humanGate = requiresHumanApproval(spec.risk_class, spec.requires_human_approval);

  let recommendation: Record<string, unknown>;
  switch (spec.execution) {
    case "prompt":
      recommendation = await runPromptAgent(spec, ctx);
      break;
    case "finos-plugin":
      recommendation = await runFinosAgent(spec, ctx);
      break;
    case "bois":
      recommendation = await runBoisAgent(spec, ctx);
      break;
    default:
      throw new Error(`execution: "${spec.execution}" is not wired in this session (agent ${spec.name}).`);
  }

  const memoryPath = writeMemory(spec, {
    trigger: ctx.trigger,
    input: ctx.input ?? null,
    recommendation,
    requiresHumanApproval: humanGate,
    riskClass: spec.risk_class,
  });

  return {
    agent: spec.name,
    execution: spec.execution,
    requiresHumanApproval: humanGate,
    riskClass: spec.risk_class,
    recommendation,
    memoryPath,
    emitted: spec.emits ?? [],
  };
}

/**
 * Calls Claude for a `prompt` agent, generalizing finos's
 * `ClaudeAgentRuntime.run()` (09_Finance/finos-plugin/src/ai-agents/runtime.ts):
 * the spec body is the system prompt, the context is the user message, and the
 * spec's `output_schema` (or the base envelope) is enforced as structured output.
 */
async function runPromptAgent(spec: AgentSpec, ctx: RunContext): Promise<Record<string, unknown>> {
  const schema = spec.output_schema ?? baseOutputSchema;

  const contextBlock = ctx.recentContext?.length
    ? `\n\nRecent related events:\n${ctx.recentContext.map((e) => `- ${e}`).join("\n")}`
    : "";

  const userMessage = [
    `Department: ${spec.department}`,
    ctx.eventType ? `Triggering event: ${ctx.eventType}` : `Trigger: ${ctx.trigger}`,
    `Input: ${JSON.stringify(ctx.input ?? {})}`,
    contextBlock,
    "\nAnalyze this within your mandate and respond with a structured recommendation matching the required schema.",
  ].join("\n");

  // `thinking`, `output_config`, and the `claude-opus-4-8` id are ahead of the
  // pinned SDK types; the cast matches finos's proven call shape exactly.
  const response = await getClient().messages.create({
    model: spec.model,
    max_tokens: 2048,
    system: spec.systemPrompt,
    thinking: { type: "adaptive" },
    output_config: {
      effort: "medium",
      format: { type: "json_schema", schema },
    },
    messages: [{ role: "user", content: userMessage }],
  } as Anthropic.MessageCreateParamsNonStreaming);

  const textBlock = response.content.find(
    (block): block is Anthropic.TextBlock => block.type === "text",
  );
  if (!textBlock) {
    throw new Error(`Agent ${spec.name} returned no text content.`);
  }
  return JSON.parse(textBlock.text) as Record<string, unknown>;
}
