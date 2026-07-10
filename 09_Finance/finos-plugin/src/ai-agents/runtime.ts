import Anthropic from "@anthropic-ai/sdk";
import type { FinancialAgentSpec } from "./index.js";
import type { FinancialEvent } from "../shared/types.js";

export interface AgentRecommendation {
  agentId: string;
  agentName: string;
  summary: string;
  recommendedActions: string[];
  requiresHumanApproval: boolean;
  approvalReasons: string[];
  riskLevel: "low" | "medium" | "high" | "critical";
}

const recommendationSchema = {
  type: "object",
  properties: {
    summary: { type: "string" },
    recommendedActions: { type: "array", items: { type: "string" } },
    requiresHumanApproval: { type: "boolean" },
    approvalReasons: { type: "array", items: { type: "string" } },
    riskLevel: { type: "string", enum: ["low", "medium", "high", "critical"] }
  },
  required: ["summary", "recommendedActions", "requiresHumanApproval", "approvalReasons", "riskLevel"],
  additionalProperties: false
} as const;

/**
 * Calls Claude for one financial agent spec, given the event that triggered it.
 * Constructed even when no API key is present so `createFinOsApplication()` never
 * fails to build the app; `.run()` throws only when actually invoked without a key,
 * and callers (the workflow orchestrator) catch that into the audit log rather than
 * crashing event dispatch.
 */
export class ClaudeAgentRuntime {
  private readonly client?: Anthropic;

  constructor(apiKey: string | undefined = process.env.ANTHROPIC_API_KEY) {
    if (apiKey) {
      this.client = new Anthropic({ apiKey });
    }
  }

  async run(
    spec: FinancialAgentSpec,
    event: FinancialEvent,
    recentContext: FinancialEvent[] = []
  ): Promise<AgentRecommendation> {
    if (!this.client) {
      throw new Error("ANTHROPIC_API_KEY is not set — cannot invoke agent " + spec.id);
    }

    const contextBlock = recentContext.length
      ? `\n\nRecent related events:\n${recentContext
          .map((e) => `- ${e.type} at ${e.occurredAt}: ${JSON.stringify(e.payload)}`)
          .join("\n")}`
      : "";

    const userMessage = [
      `Mission: ${spec.mission}`,
      `Triggering event: ${event.type}`,
      `Entity: ${event.entityId}`,
      `Occurred at: ${event.occurredAt}`,
      `Payload: ${JSON.stringify(event.payload)}`,
      `Actions requiring human approval for this agent: ${spec.humanApprovalRequiredFor.join(", ")}`,
      contextBlock,
      "\nAnalyze this event within your mandate and respond with a structured recommendation."
    ].join("\n");

    const response = await this.client.messages.create({
      model: "claude-opus-4-8",
      max_tokens: 2048,
      system: spec.systemPrompt,
      thinking: { type: "adaptive" },
      output_config: {
        effort: "medium",
        format: { type: "json_schema", schema: recommendationSchema }
      },
      messages: [{ role: "user", content: userMessage }]
    } as Anthropic.MessageCreateParamsNonStreaming);

    const textBlock = response.content.find(
      (block): block is Anthropic.TextBlock => block.type === "text"
    );
    if (!textBlock) {
      throw new Error(`Agent ${spec.id} returned no text content for event ${event.id}`);
    }

    const parsed = JSON.parse(textBlock.text) as Omit<AgentRecommendation, "agentId" | "agentName">;

    return {
      agentId: spec.id,
      agentName: spec.name,
      ...parsed
    };
  }
}
