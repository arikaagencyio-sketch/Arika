# Arika Runtime — Design

One canonical agent format + one executor that runs every department's agents
from four trigger types. This document is the contract; the code implements it.

## 1. Where agents live

Every agent is ONE markdown file at `.claude/agents/{dept-slug}-{agent}.md` at the
repo root — the same location and naming the Design (19) and Experience
Engineering (20) agents already use. The runtime reads this directory at boot.

## 2. The spec (frontmatter)

```yaml
---
name: sales-lead-qualification     # required, unique; matches the filename stem
department: "05"                    # required; two-digit department number as a string
description: <one line>             # required
model: claude-opus-4-8             # optional; default claude-opus-4-8
execution: prompt                  # optional; prompt | finos-plugin | bois | design-plugin (default: prompt)
finos_id: cfo-agent                # required when execution == finos-plugin
risk_class: 1                      # required; Constitution §5, integer 0–4 (SUPREME)
requires_human_approval: false     # optional; auto-forced true when risk_class >= 3
triggers:                          # required; at least one
  - { type: manual }
  - { type: schedule, cron: "0 9 * * 1-5" }
  - { type: event, on: LEAD_CREATED }
  - { type: webhook, source: clickup }
inputs:                            # optional; documents expected input fields
  lead_id: { type: string, from: event.payload.lead_id }
output_schema:                     # optional but recommended; a JSON Schema object
  type: object
  additionalProperties: false
  required: [summary, recommendedActions, requiresHumanApproval, approvalReasons, riskLevel]
  properties: { ... }
memory_stream: 05_Sales/.../runtime.jsonl   # optional; repo-relative JSONL path
emits: [LEAD_QUALIFIED]            # optional; events published after a run
handoff_to: [sales-sales-execution]# optional; downstream agents (documentation for now)
citations: [SD-044-ASKINGTH:P0436] # optional; Sales agents carry SourceId:ParagraphId
---

# System Prompt
…the agent's system-prompt prose (untouched from its original spec)…
```

The frontmatter is validated by `src/spec-schema.ts` (zod). The markdown body
below the frontmatter becomes the Claude `system` prompt for `execution: prompt`
agents.

## 3. The base output envelope

Every advisory agent returns at least these five fields, copied verbatim from
finos-plugin's proven `recommendationSchema` (`09_Finance/finos-plugin/src/ai-agents/runtime.ts`):

- `summary: string`
- `recommendedActions: string[]`
- `requiresHumanApproval: boolean`
- `approvalReasons: string[]`
- `riskLevel: "low" | "medium" | "high" | "critical"`

Agents may extend the schema with their own fields (e.g. `icp_fit_score`,
`qualification_stage`). If a spec omits `output_schema`, the runtime enforces the
base envelope alone.

## 4. Executor lifecycle — `runAgent(name, context)`

1. Look the spec up in the registry (throw if unknown).
2. Compute governance: `requiresHumanApproval = risk_class >= 3 || spec.requires_human_approval`.
3. Dispatch by `execution`:
   - `prompt` → call Claude with the body as `system`, the context as the user
     message, and the spec's `output_schema` (or the base envelope) enforced via
     `output_config.format = { type: "json_schema" }`. Generalizes finos's
     `ClaudeAgentRuntime.run()` exactly (same model default `claude-opus-4-8`,
     `thinking:{type:"adaptive"}`, `effort:"medium"`, first-text-block JSON parse).
   - `finos-plugin` → delegate to finos's own `ClaudeAgentRuntime` via
     `src/wrappers/finos.ts` (dynamic import of finos's built `dist/`).
   - `bois` / `design-plugin` → not wired this session (reserved).
4. Write one JSONL line to the spec's `memory_stream` (§6).
5. Emit each `emits` event on the in-process event bus (chaining is logged this
   session; downstream auto-dispatch is a later step).
6. Return the parsed recommendation.

**Advisory-first:** the executor never performs a state-changing action. Declared
`tools` are not invoked; agents only read the input context and return a
recommendation. Any real action stays a human step until an approval-queue lands.

## 5. Triggers → one execution path

Every trigger assembles a `context` and calls `runAgent`:

| Trigger   | Fires from                        | context source                         |
|-----------|-----------------------------------|----------------------------------------|
| manual    | `arika run <name> --input=<json>` | CLI `--input` JSON                     |
| schedule  | node-cron (local) / cloud routine | empty payload; agent decides scope     |
| event     | in-process event bus              | event payload                          |
| webhook   | Fastify `POST /webhook/:source`   | request body mapped to an event        |

## 6. Memory format (bois-compatible JSONL)

Append-only, one JSON object per line, matching the only live machine-written log
in the repo (`12_Branding/bois/core/memory/store.py`):

```json
{"timestamp":"<ISO-8601>","agent":"sales-lead-qualification","department":"05",
 "stream":"runtime","event_type":"agent_run","source":"arika-runtime",
 "payload":{"trigger":"manual","input":{...},"recommendation":{...},
            "requiresHumanApproval":false,"riskClass":1}}
```

## 7. Reconciliations (the runtime's authority rules)

- **Risk model:** the Constitution's Class 0–4 (`00_Agency_Governance/AGENCY_OPERATING_CONSTITUTION.md` §5)
  is supreme. The finos/Sales `low/medium/high/critical` labels map to it:
  low→1, medium→2, high→3, critical→4. `requires_human_approval` is forced true at
  class ≥ 3 regardless of what the frontmatter says.
- **No automation fires without an approval-matrix row.** Advisory recommendations
  are Class 0–1 (informational); executing any recommended action requires a row in
  `00_Agency_Governance/AUTOMATION_APPROVAL_MATRIX.md` + human sign-off for Class 3+.
- **Events** reuse finos's SCREAMING_SNAKE names and add cross-department ones
  (`LEAD_CREATED`, `LEAD_QUALIFIED`, `DEAL_CLOSED_WON`, …).

## 8. Not in this session (reserved)

Approval-queue + matrix enforcement for auto-executable actions; the bois LLM
bridge; Sales/Marketing bulk migration; the cloud-routine mirror of `schedule`
triggers. All slot into the same substrate without architectural change.
