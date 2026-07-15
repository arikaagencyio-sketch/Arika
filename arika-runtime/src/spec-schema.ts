import { z } from "zod";

/**
 * The canonical agent spec. Every agent in the repo is one markdown file at
 * `.claude/agents/{dept-slug}-{agent}.md` whose YAML frontmatter validates
 * against `frontmatterSchema` and whose body is the system prompt.
 */

export const triggerSchema = z
  .object({
    type: z.enum(["manual", "schedule", "event", "webhook"]),
    cron: z.string().optional(),
    on: z.string().optional(),
    source: z.string().optional(),
  })
  .superRefine((t, ctx) => {
    if (t.type === "schedule" && !t.cron) {
      ctx.addIssue({ code: z.ZodIssueCode.custom, message: "schedule trigger requires `cron`" });
    }
    if (t.type === "event" && !t.on) {
      ctx.addIssue({ code: z.ZodIssueCode.custom, message: "event trigger requires `on`" });
    }
  });

export type Trigger = z.infer<typeof triggerSchema>;

export const frontmatterSchema = z
  .object({
    name: z.string().min(1),
    // Accept "05" or 5; always normalise to a two-ish-char string.
    department: z.union([z.string(), z.number()]).transform((v) => String(v)),
    description: z.string().min(1),
    model: z.string().default("claude-opus-4-8"),
    execution: z.enum(["prompt", "finos-plugin", "bois", "design-plugin"]).default("prompt"),
    finos_id: z.string().optional(),
    /** Which BOIS pipeline mode a Branding agent runs (see bois/executions/run_brand_task.py). */
    bois_mode: z.enum(["define", "audit", "govern"]).optional(),
    risk_class: z.number().int().min(0).max(4),
    requires_human_approval: z.boolean().default(false),
    triggers: z.array(triggerSchema).min(1),
    inputs: z.record(z.unknown()).optional(),
    // A JSON Schema object; kept permissive on purpose.
    output_schema: z.record(z.unknown()).optional(),
    memory_stream: z.string().optional(),
    emits: z.array(z.string()).optional(),
    handoff_to: z.array(z.string()).optional(),
    citations: z.array(z.string()).optional(),
  })
  .superRefine((spec, ctx) => {
    if (spec.execution === "finos-plugin" && !spec.finos_id) {
      ctx.addIssue({
        code: z.ZodIssueCode.custom,
        message: "execution: finos-plugin requires a `finos_id`",
        path: ["finos_id"],
      });
    }
    if (spec.execution === "bois" && !spec.bois_mode) {
      ctx.addIssue({
        code: z.ZodIssueCode.custom,
        message: "execution: bois requires a `bois_mode` (define | audit | govern)",
        path: ["bois_mode"],
      });
    }
  });

export type Frontmatter = z.infer<typeof frontmatterSchema>;

/** A fully-loaded agent: validated frontmatter + its body + where it came from. */
export interface AgentSpec extends Frontmatter {
  /** The markdown body below the frontmatter — the Claude `system` prompt. */
  systemPrompt: string;
  /** Absolute path to the source `.md` file. */
  filePath: string;
}

/**
 * The base output envelope every advisory agent returns, copied from finos's
 * proven `recommendationSchema`. Used when a spec omits its own `output_schema`.
 */
export const baseOutputSchema = {
  type: "object",
  additionalProperties: false,
  required: ["summary", "recommendedActions", "requiresHumanApproval", "approvalReasons", "riskLevel"],
  properties: {
    summary: { type: "string" },
    recommendedActions: { type: "array", items: { type: "string" } },
    requiresHumanApproval: { type: "boolean" },
    approvalReasons: { type: "array", items: { type: "string" } },
    riskLevel: { type: "string", enum: ["low", "medium", "high", "critical"] },
  },
} as const;
