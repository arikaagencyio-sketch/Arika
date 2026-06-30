# Sales — Department OS

**Department:** Sales (05)
**Position in flow:** Receives qualified demand from Marketing (03)/Content (04) and ClientPartner Acquisition (06); converts to closed deals; hands off to Client Success (07).
**Mandate:** Own pipeline, conversion, deal execution, and the agency's sales-side AI operations.
**Owner:** *(unassigned — placeholder)*

> See [`GLOBAL_OS.md`](../GLOBAL_OS.md) for how this file fits into the whole system. Read that first if you haven't.

---

## 1. Identity

Sales is responsible for converting qualified opportunities (from Marketing and ClientPartner Acquisition) into signed, paying clients, and handing them off cleanly to Client Success. Per its own constitution (`06_AI_OPERATIONS/01_System_Prompts/Master_AI_Operating_Constitution.md`), this department explicitly frames itself as "a revenue and commercial intelligence system" — not a writing or content-generation function — operating a 7-step execution cycle: Analyze → Route → Plan → Execute → Verify → Report → Memorize.

## 2. Status

**Most mature department in the repo — content migration complete (2026-06-30), high confidence.** Unlike every other department processed so far, this one's existing `06_AI_OPERATIONS/` layer was independently quality-checked: 7 of 7 sampled agent-registry citations were verified against `Master_Source_Paragraph_Index.csv` and checked out exactly, and the underlying agent/subagent framing was confirmed to originate in this department's own raw "Draft N.md" files (not imposed by a generic external template) — `06_AI_OPERATIONS/` is a genuine consolidation of ~20 overlapping agent visions already present across 78 separate source documents. This is meaningfully more trustworthy than the draft/unvalidated content found in other departments (e.g. Offer, 02) — see §13 for full detail. The one caveat: the Skill Library (§6) has no citations and should be treated as coherent synthesis, not paragraph-verified fact, and all three AI Memory Logs (§8) are confirmed empty templates, not real operating history.

## 3. Capability Registry

| Capability | Description | Status |
|---|---|---|
| Strategic prioritization & revenue intelligence | Executive-level sequencing of what moves revenue now | Citation-backed (Executive Intelligence Agent, Revenue Strategy Agent) |
| Market/competitor/sector intelligence | Turning external signals into commercial intelligence | Citation-backed (Market Intelligence Agent) |
| Buyer psychology & power mapping | Pain, objections, trust gaps, stakeholder power dynamics | Citation-backed (Customer Psychology Agent, Power Navigation Agent) |
| Offer & pricing architecture | Value props, pricing logic, risk reducers | Citation-backed (Offer Architecture Agent) — cross-reference Offer (02)'s own Capability Registry |
| Demand generation | Outbound, paid, referral/partnership channels | Citation-backed (Demand Generation Agent) — cross-reference Marketing (03) / ClientPartner Acquisition (06) |
| Lead qualification & discovery | Fit/urgency/authority/timing assessment | Citation-backed (Lead Qualification and Discovery Agent); cross-department reconciliation (2026-06-30) also reassigned a /25 pre-sale scoring model originally drafted under Client Success to this capability — see `07_Client_Success/CLIENTSUCCESS_OS.md` §10 |
| Sales execution & closing | Conversation, objection navigation, negotiation | Citation-backed (Sales Execution and Closing Agent) |
| Follow-up & stalled-deal recovery | Prevents revenue leakage via structured re-engagement | Citation-backed (Follow-Up and Recovery Agent) — see §4's 7-touch cadence |
| Customer onboarding/expansion/retention | Post-close account growth | Citation-backed (Customer Success and Expansion Agent) — cross-reference Client Success (07) |
| RevOps (CRM, KPIs, forecasting, dashboards) | Pipeline/data infrastructure | Citation-backed (Revenue Operations and Performance Agent) — see §7, no concrete formulas defined yet |
| Risk, compliance & governance | Approval gates, audit, ethics | Citation-backed (Risk Trust and Governance Agent) — see §10 |
| SOP/playbook/training generation | Enablement content | Citation-backed (Enablement and Playbooks Agent) |
| AI orchestration | Multi-agent routing, memory, handoffs, reflection/QA | Citation-backed (AI Orchestration, Planning, Tool-Use, Reflection and Quality, Multi-Agent Orchestration Agents) |

## 4. Workflow Index

| Workflow | Trigger | Steps | Output | Owner | Source |
|---|---|---|---|---|---|
| Daily Sales Command Run | "Move revenue today" | 7-agent sequence: Executive Intelligence → RevOps → Demand Gen → Lead Qualification → Sales Execution → Follow-Up → Reflection | Top 5 revenue actions, deal risks, follow-ups due, new pipeline actions, approvals needed, memory updates | *(unassigned)* | `06_AI_OPERATIONS/07_Runtime_Examples/Daily_Sales_Command_Run.md` |
| Client Sales System Build Run | "Build/reconstruct a client sales OS" | 10-agent sequence: Planning → Market Intelligence → Customer Psychology → Offer Architecture → RevOps → Enablement → AI Orchestration → Risk/Governance → Multi-Agent Orchestration → Reflection | Sales OS blueprint, agent map, SOP backlog, CRM/KPI structure, governance rules, implementation sequence | *(unassigned)* | `06_AI_OPERATIONS/07_Runtime_Examples/Client_Sales_System_Build_Run.md` |
| Pipeline Build Runbook | New pipeline needed | 9-step agent route + daily pipeline action loop (10 steps) + 7-touch follow-up cadence (Day 0/2/5/9/14/21/30, each with purpose and message type) | 12-item output contract; the most execution-ready workflow in this folder | *(unassigned)* | `06_AI_OPERATIONS/07_Runtime_Examples/Pipeline_Build_Runbook.md` |
| Intent → agent routing | Any incoming task | 18-row intent→agent lookup table; routing rule: smallest capable agent first, multi-agent only when >3 agents needed or cross-domain, reflection before trusting high-impact output, governance check before external/irreversible action | Correct agent assignment | *(unassigned)* | `06_AI_OPERATIONS/04_Routing/Task_Routing_Matrix.md` |

## 5. Agent Roster

**20 canonical agents** (each with 4 named subagents = 80 total), fully cited against source paragraphs in `Master_Source_Paragraph_Index.csv`. Full detail (inputs/outputs, human boundary, escalation triggers, subagents) lives in `06_AI_OPERATIONS/02_Agent_Roles/Agent_Registry.md` — this is a summary index only, not a duplicate:

Executive Intelligence · Revenue Strategy · Market Intelligence · Customer Psychology · Offer Architecture · Demand Generation · Audience and Community · Lead Qualification and Discovery · Sales Execution and Closing · Follow-Up and Recovery · Customer Success and Expansion · Revenue Operations and Performance · Power Navigation and Partnership · Risk Trust and Governance · Enablement and Playbooks · AI Orchestration · Planning · Tool-Use · Reflection and Quality · Multi-Agent Orchestration.

## 6. Skill Library Index

**18 skills** in `06_AI_OPERATIONS/03_Skills/Skill_Library.md`, each with a 5-step procedure and defined standard output, names mirroring the 20 agents above 1:1. **Caveat: zero source citations** — coherent and clearly corpus-derived by naming/structure, but not individually paragraph-verified the way the Agent Registry is. Treat as reasonable synthesis, not verbatim-sourced fact.

## 7. KPI Dictionary (department-local)

| Metric | Formula | Source | Owner | Cadence | Threshold |
|---|---|---|---|---|---|
| *(placeholder — RevOps Agent's mandate covers CRM/KPI/forecasting/dashboards, but no concrete formulas, real figures, or thresholds were found anywhere in this department's source material)* | | | | | |

This is a genuine gap, not just unmigrated content — the department's own gap backlog (`00_Workspace_Intelligence_Inventory/WORKSPACE_GAP_RESOLUTION_BACKLOG.csv`) confirms no formal KPI dictionary exists as a standalone artifact. Cross-reference `00_Agency_Governance/AGENCY_KPI_DICTIONARY.md` for the agency-wide acquisition/revenue formulas (CAC, conversion rate, sales cycle length, pipeline velocity) that this department should own real values for once data exists.

## 8. Decision Log

Live decision log already exists: `06_AI_OPERATIONS/06_AI_Memory_Logs/Decision_Log.md` — use that file going forward rather than duplicating entries here. **Confirmed empty** (one-line template only) — same for `Learning_Loop_Log.md` and `Prompt_Evolution_Log.md`. This is a designed-but-unused capability: the format exists (`AI_Memory_Log_Template.md`), real entries do not yet.

## 9. Risk / Incident Log

*(placeholder — no incidents logged yet)*. Risk classification framework already exists and is mature — see `06_AI_OPERATIONS/05_Escalations_Approvals/Escalation_Rules.md` and §10 below for the 4-tier risk model this log should use once populated.

## 10. Standards & SOPs Index

**Constitution non-negotiables** (`06_AI_OPERATIONS/01_System_Prompts/Master_AI_Operating_Constitution.md`): preserve source lineage; separate evidence from inference; never fabricate CRM/market/customer/pricing/legal/historical data; never externalize messages, change financial terms, make legal claims, or take destructive action without human approval; use smallest capable agent route; state reasons when confidence is low.

**Human-owned decisions** (cannot be delegated to AI agents): strategy, pricing, legal exposure, financial commitments, hiring, compensation, customer-facing promises, sensitive relationship moves, irreversible system changes.

**Evidence standard**: cite source IDs from `Master_Source_Paragraph_Index.csv`; label multi-source synthesis explicitly as synthesis with its source cluster — not as a single verified fact.

**Escalation risk classes** (`06_AI_OPERATIONS/05_Escalations_Approvals/Escalation_Rules.md`):
| Class | Action | Examples |
|---|---|---|
| Low | Proceed, report assumptions | Routine internal tasks |
| Medium | Reflection check + state assumptions | Moderate-ambiguity tasks |
| High | **Human approval required before execution** | Pricing, negotiation, legal, external messaging, budget, data changes, strategy shifts |
| Critical | **Human approval + audit log required** | Contracts, destructive actions, compliance, sensitive data, financial commitments, irreversible customer commitments |

This maps closely onto `AGENCY_OPERATING_CONSTITUTION.md` §5's agency-wide risk classes (Low≈Class 1, Medium≈Class 2, High≈Class 3, Critical≈Class 4) — worth formally reconciling the two frameworks in a future pass rather than running them as parallel systems.

Approval packets (for High/Critical) require: proposed action, reason, evidence, risk class, options, recommendation, downside, rollback plan. Human override wins unless it conflicts with the constitution/evidence/safety/prior approval — in that case the system must stop and ask rather than comply.

## 11. RACI / Ownership

| Function | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| *(placeholder)* | | | | |

## 12. Triggers / Automation Hooks

Triggers are well-defined structurally (the 18-row intent→agent table in `Task_Routing_Matrix.md`, §4 above) but **not connected to any real automation** — every "trigger" today fires a documented agent-routing decision for a human or an LLM session to follow manually, not a live webhook/scheduler. The "Always escalate" list from `Escalation_Rules.md` is the closest thing to a real automation-safety rule already defined: legal/compliance/privacy/payment risk, all external communication, pricing/discount/comp/refund/guarantee decisions, destructive CRM/automation/data changes, low confidence with material impact, and unresolved conflicting evidence — all of these should map directly into `00_Agency_Governance/AUTOMATION_APPROVAL_MATRIX.md` rows whenever real automation is built for this department.

## 13. Existing OS Sub-Layer

**Yes — most mature in the repo, and independently quality-verified (2026-06-30).** `05_Sales/06_AI_OPERATIONS/` contains:
- `00_Index/` — AI Operations Index, Source Agent Mention Registry (515 rows), Build Summary, Human Operator Guide
- `01_System_Prompts/` — Master AI Operating Constitution, Agent Runtime Template, Multi-Agent Handoff Template
- `02_Agent_Roles/Agent_Registry.md` — 20 agents, 80 subagents, fully cited
- `03_Skills/Skill_Library.md` — 18 skills, uncited synthesis
- `04_Routing/Task_Routing_Matrix.md`
- `05_Escalations_Approvals/Escalation_Rules.md`
- `06_AI_Memory_Logs/` — Decision Log, Prompt Evolution Log, Learning Loop Log (all confirmed empty templates)
- `07_Runtime_Examples/` — Daily Sales Command Run, Client Sales System Build Run, Pipeline Build Runbook

This sub-layer also has its own source-citation lineage (`Master_Source_Registry.csv`: 79 source documents; `Master_Source_Paragraph_Index.csv`: 67,310-line full paragraph index) mapping synthesized claims back to specific source paragraphs. **Verified, not just claimed**: 7 of 7 sampled `Agent_Registry.md` citations were checked against the paragraph index and confirmed accurate (e.g. "Executive Intelligence Agent" → `SD-044-ASKINGTH:P0436` → paragraph reads "1. EXECUTIVE INTELLIGENCE AGENT"). This is the strongest anti-hallucination pattern anywhere in this repo, and is itself generated by a real, rerunnable tool (`generate_blueprint.ps1`, see §14) rather than hand-typed. **Recommend other departments adopt this citation pattern once they reach a similar maturity stage**, and recommend extending citations to the currently-uncited Skill Library (§6).

## 14. Raw Archive Pointer

~68 root-level "Draft N.md" files plus `Master_Source_Registry.csv`, `Master_Source_Paragraph_Index.csv`, `Master_Revenue_Commercial_Operating_System_Blueprint.md` (a separate 614-line institutional architecture doc, also generated by the script below — distinct from `06_AI_OPERATIONS/`), and `generate_blueprint.ps1` live at this department's root. Existing gap backlog: `05_Sales/00_Workspace_Intelligence_Inventory/` — confirms genuine (not just unmigrated) gaps: no standalone Constitution-as-single-source, no historical memory log, no formal resource/capacity model, no change-management protocol.

**Spot-check finding (2026-06-30):** sampled raw drafts (`Asking the right questions. Draft 44.md`, `360 Sales System Map. Draft 42.md`, `Sales Operating System Roles. Draft 49.md`, and others) already contain fully fleshed-out "Agent X — [Name]" sections that map almost verbatim onto `06_AI_OPERATIONS/Agent_Registry.md`'s consolidated agents/subagents — confirming the agent framing originated in this department's own brainstorm material, not a template imposed from outside.

**`generate_blueprint.ps1` provenance note:** the script reads `.docx` files from the *original* pre-restructuring location (`Sales Drafts/`, now `05_Sales/`) plus a hardcoded list of 11 "companion" `.docx` files from the parent directory — some of which (e.g. `HE SALES OS_2024.docx`, `Sales Mechanism 102.docx`, `Nikolaus Luhmann_ Sales.docx`) are **not present as `.md` files anywhere in this folder**, meaning some sources cited in `Master_Source_Registry.csv` are not directly readable today. Re-running this script (after fixing its hardcoded paths for the new folder structure) would be the correct way to regenerate the citation system if those companion files are ever located.

## 15. Changelog

- 2026-06-30 — File created as part of v0.1 skeleton restructuring.
- 2026-06-30 — Content migration: `06_AI_OPERATIONS/` extracted and independently quality-verified (7/7 sampled citations checked out against `Master_Source_Paragraph_Index.csv`; agent framing confirmed to originate in this department's own raw drafts). Capability Registry, Workflow Index, Agent Roster, Skill Library Index, Standards & SOPs Index, and Triggers/Automation Hooks populated. KPI Dictionary and Risk/Incident Log confirmed as genuine gaps (not just unmigrated) per the department's own existing gap backlog.
- 2026-06-30 — Cross-department reconciliation pass: noted in §3 that Client Success (07)'s pre-sale qualification scoring model was reassigned here as part of that department's boundary reconciliation. — Claude Code (Sonnet 4.6)
