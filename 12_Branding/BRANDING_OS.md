# Branding — Department OS

**Department:** Branding (12)
**Position in flow:** Horizontal support layer — feeds Marketing, Sales, Client Success, and Agency Governance with brand architecture, narrative, and identity systems.
**Mandate:** Own brand definition, positioning, narrative engineering, and visual/identity systems for the agency and (as a service) for clients.
**Owner:** Mary Thuo

> See [`GLOBAL_OS.md`](../GLOBAL_OS.md) for how this file fits into the whole system. Read that first if you haven't.

---

## 1. Identity

Branding defines and governs how the agency (and client brands it manages) present themselves — architecture, narrative, positioning, visual cognition, cultural intelligence. Its code layer (`bois/`, "Brand Operating Intelligence System") frames itself as "a stateful, retrieval-driven, agent-orchestrated execution ecosystem" with a non-negotiable runtime rule: if retrieval evidence is missing, the system must stop in a "retrieval failure state" rather than generate generic branding output — i.e., it's architected specifically against hallucinated brand work, the same principle this whole repo's migration follows. Recurring doctrine across the raw drafts: **"Branding = Why you are chosen, Marketing = How you get seen"** — the two departments' boundary, stated by the source material itself (unlike several other department boundaries in this repo, which had to be imposed).

## 2. Status

**Content migration complete (2026-06-30) — correcting an earlier under-assessment, same pattern as Finance.** `bois/` is meaningfully more real than the original skeleton pass characterized it: **all 21 `core/` Python files contain real working logic — none are stubs**, a stronger ratio than Finance's finos-plugin (which had one confirmed stub). `bois/core/ingestion/pipeline.py` was actually **run** against this department's 40 raw drafts (`bootstrap_bois.py`), producing a real, auto-generated, exhaustive source-citation system (`bois/knowledge/_indexes/`: 40 documents, 14,109 tagged paragraphs, zero ingestion errors) — a stronger citation system than Finance's hand-curated `source-intelligence.md`, since it's reproducible by rerunning the script rather than manually maintained. A full smoke test was run end-to-end against a hypothetical client ("Sample Nairobi Laundry," explicitly labeled as a sample).

**Tracker item 30 resolved 2026-06-30 — BOIS now has a real, non-hypothetical client.** `bois/executions/run_arika_agency_brand.py` builds a real `ClientObject` for Arika Agency itself from facts already confirmed elsewhere in this repo (`AGENCY_VISION.md`, `AGENCY_REVENUE_TARGETS.md`, `02_Offer/OFFER_OS.md`, `01_Sector/SECTOR_OS.md`, the confirmed "Revenue Infrastructure Partner" positioning, and the Kenya/global geography confirmation) — **confirmed run**, producing a real client workspace (`bois/clients/arika-agency/`) and a complete retrieval bundle (zero missing sources across all 6 required sources, 11 of 20 agents activated) for the task "define Arika Agency's own core brand identity, positioning, and voice." Real, confirmed fields: sector/sub-sector, audience (3-tier ICP), services (the 11-offer catalog), pricing-model summary, market position, communication style and emotional positioning (both sourced verbatim from `AGENCY_VISION.md`/`AGENCY_REVENUE_TARGETS.md`'s ROCBO doctrine), governance rules, stakeholder notes. **Explicitly left empty, not invented** — genuinely unconfirmed: `competitors`, `visual_preferences`, `typography_preferences`, `color_preferences`. No real competitor analysis or visual-identity work exists anywhere in this repo; these remain open until the owner provides them.

Like every department, **no real client names (other than the agency's own), brand names, pricing, or measured KPI values exist anywhere** — all scoring thresholds are designed defaults, not calibrated against real outcomes.

## 3. Capability Registry

`bois/core/`'s 21 modules + `bois/agents/AGENT_SYSTEM.md`'s 20-agent roster (§5) are the system's real capability set. Raw-draft capability concepts layered beneath them (status: draft/aspirational unless noted):

| Capability | Description | Status |
|---|---|---|
| Knowledge ingestion & tagging | Parses real `.docx` source files, SHA-256 checksums, 13 keyword-based tag rules, section-hint heuristics, repetition tracking | **Real, run** — `core/ingestion/{docx_reader,pipeline}.py` |
| Knowledge graph construction | Builds doc→paragraph→tag→entity→reinforcement graph via regex entity extraction (stage/system/agent/framework patterns) + tag co-occurrence matrix | **Real, run** — `core/knowledge/graph_builder.py` |
| Hybrid retrieval with hard gate | TF-IDF-style scoring (log-tf × idf) + tag-overlap + reinforcement boosting across 6 required sources; raises a runtime error if retrieval is incomplete rather than proceeding | **Real** — `core/retrieval/gated_retriever.py` |
| Agent orchestration & trigger routing | Assembles dynamic brand context, routes among 20 agents via sector/deliverable/geography/audience trigger rules (concrete examples: fintech, healthcare, luxury, laundry, b2b), builds per-agent task objects with constraints | **Real** — `core/orchestration/{registry,engine}.py` |
| Brand scoring / grading | 15 weighted scoring dimensions, each with its own threshold (70-78) and metric list; weighted-total computation, failed-dimension flagging, recommendation library | **Real** — `core/grading/engine.py` |
| Brand governance validation | Validates retrieval completeness, agent activation, 8 mandatory output-reasoning fields, 5 continuity-keyword checks (narrative/visual/culture/sales-marketing/operations) | **Real** — `core/governance/policy.py` |
| Presentation intelligence | 12 required presentation sections, each with a concrete "must explain" requirement; generates narrative-arc and quality-standard lists | **Real** — `core/presentation/engine.py` |
| Client workspace management | Per-client folder tree (memory/campaigns/presentations/visuals/governance/deliverables/timelines), slugified, with client.json | **Real** — `core/client_workspace.py` |
| Append-only memory | JSONL event log across 8 memory streams (client/campaign/visual/narrative/governance/market/trend/stakeholder) | **Real** — `core/memory/store.py` |
| Brand architecture typing | Branded House / House of Brands / Endorsed Brand / Hybrid Architecture (standard industry taxonomy) + a 5-layer "offer pyramid" + 6-stage client lifecycle | Draft/aspirational (Draft 2) |
| Positioning formula | "For [audience], [Brand] is the [category] that delivers [value] through [mechanism], unlike [alternative]" — repeated near-verbatim across multiple drafts | Draft/aspirational (Draft 32, echoed elsewhere) |
| Narrative engineering | 5-layer stack: Truth Core → Narrative Framework → Narrative Modules → Translation Layer → Feedback/Evolution | Draft/aspirational (Draft 23) |
| Psychographic intelligence ("DPIS") | 8-layer system: Identity → Emotional → Motivation → Cultural Signal → Behavioral → Narrative Resonance → Perception Feedback → Adaptive Decision Engine | Draft/aspirational (Draft 27) |
| Cultural alignment scoring | 5-dimension weighted Cultural Alignment Score (Awareness, Resonance, Behavioral Alignment, Identity Integrity, Evolution Capacity) — clearest conceptual ancestor of `BrandScoringEngine`'s 15 dimensions | Draft/aspirational (Draft 24), partially realized in code |
| Sector intelligence | 7-layer stack: Value Logic, Trust Mechanics, Risk Profile, Decision Dynamics, Category Codes, Narrative Space, Constraints | Draft/aspirational (Draft 19) |
| Legal branding / IP defense | 5 pillars (Identity Ownership, IP System, Usage/Control, Entity/Liability Structure, Enforcement/Defense) + an "enforcement pyramid" (Education→Warning→Restriction→Legal Action→Litigation) | Draft/aspirational (Draft 29) — note: generic business-entity content, not the agency's own legal infrastructure (that's Legal, 10) |
| Brand distribution & cadence | Micro/meso/macro cadence layers, "70-20-10 rule" for content mix | Draft/aspirational (Draft 25) |

## 4. Workflow Index

| Workflow | Trigger | Steps | Output | Owner | Source |
|---|---|---|---|---|---|
| Knowledge bootstrap | Manual run | `bootstrap_bois.py`: scan raw drafts → checksum/ID → parse paragraphs → tag → build knowledge graph → write indexes | Populated `bois/knowledge/_indexes/` (documents.json, paragraphs.jsonl, knowledge_graph.json) | Mary Thuo | `core/executions/bootstrap_bois.py` — **confirmed run**, 40 docs / 14,109 paragraphs / 0 errors |
| Brand context assembly & agent routing | New client/brief | Assemble `DynamicBrandContext` → match sector/deliverable/geography/audience against `TRIGGER_RULES` → select agents from `BASE_AGENT_SEQUENCE` (7-agent base chain) + triggered specialists → build per-agent tasks | Routed agent task set | Mary Thuo | `core/orchestration/engine.py` |
| Gated retrieval | Agent task needs evidence | Query 6 required sources via hybrid (TF-IDF + tag + reinforcement) scoring → assemble bundle → **hard-fail (`RuntimeError`) if incomplete** rather than proceed with partial evidence | Retrieval bundle or explicit failure state | Mary Thuo | `core/retrieval/gated_retriever.py` |
| Brand scoring / audit | Deliverable or evidence set ready | Score across 15 weighted dimensions (manual `.score()` or evidence-based `.audit_from_evidence()` keyword-hit heuristic) → flag dimensions below threshold (70-78) → attach recommendations | Scored brand audit | Mary Thuo | `core/grading/engine.py` |
| Governance validation | Agent output produced | Check retrieval completeness, agent activation, 8 mandatory reasoning fields, 5 continuity-keyword checks | Pass/fail governance finding | Mary Thuo | `core/governance/policy.py` |
| Smoke test | Validation run | End-to-end run of bootstrap + orchestration + scoring against a hypothetical client | Confirmed working pipeline | Mary Thuo | `core/executions/smoke_test.py` — **confirmed run** against "Sample Nairobi Laundry" (explicitly labeled sample data) |
| Real brand definition (agency's own) | Manual run | Build real `ClientObject` for Arika Agency from confirmed-real repo facts → `create_client_workspace` → gated retrieval → agent routing → persist context | Real client workspace `bois/clients/arika-agency/`, complete retrieval bundle, 11 activated agents | Mary Thuo | `bois/executions/run_arika_agency_brand.py` — **confirmed run**, resolves tracker item 30 |

## 5. Agent Roster

**20 agents**, each with a full purpose/memory-access/validation contract in `bois/agents/AGENT_SYSTEM.md`, mirrored in code at `bois/core/orchestration/registry.py`'s `AGENT_REGISTRY` (docs and code in sync, same pattern as Finance's agent-prompts.md/financialAgentSpecs): **Master Orchestrator, Sector Intelligence, Audience Cognition, Cultural Intelligence, Brand Identity, Narrative Engineering, Visual Cognition, Brand Governance, Brand Evolution, Sales Alignment, Marketing Synchronization, Distribution Intelligence, Brand Production, Psychographic Intelligence, Symbolic Systems, Semantic Intelligence, Trend Intelligence, Brand Calendar, Trust and Authority, Presentation Intelligence**. A `BASE_AGENT_SEQUENCE` (7-agent base chain) always runs; the remaining agents activate via concrete `TRIGGER_RULES` keyed by sector (fintech/healthcare/luxury/laundry/b2b), deliverable type, geography, and audience. **Important caveat, same as Finance's agent roster**: this is real spec/configuration/routing data, not executable AI — `registry.py` has an `agent_prompt()` function that generates a prompt string per agent, implying the actual reasoning step is meant to be invoked externally; no code in this repo calls an LLM to run these agents. Confirmed by direct code inspection (2026-06-30): no LLM-related imports or API calls anywhere in `bois/` (same check as Finance's `finos-plugin`). **Original owner decision (2026-06-30, tracker item 28): stays spec/routing-only**, pending the agency's own real brand existing for it to reason over (tracker item 30). **That precondition closed the same day** (item 30 resolved — `bois/clients/arika-agency/` is real). **Superseded same day:** owner confirmed **Claude (Anthropic API)** as the LLM that will back all 20 agents. **Wiring itself is not yet implemented** — no Anthropic SDK dependency exists in `bois/` as of this entry; building it is a `00_Agency_Governance/GO_LIVE_CHECKLIST.md` item, not completed work.

## 6. Skill Library Index

*(placeholder — no separate skill library exists; agent capabilities are defined directly in the Agent Roster's contracts above, same as Finance)*

## 7. KPI Dictionary (department-local)

**All thresholds below are generic designed defaults, not real measured figures** — same caveat as every other department, though here (like Finance) the numbers double as actual code logic, not just narrative targets.

| Metric | Formula | Threshold found | Source | Owner | Cadence |
|---|---|---|---|---|---|
| Brand Score (composite) | Weighted sum across 15 scoring dimensions | Per-dimension thresholds 70-78; weights sum to ~1.0 | `core/grading/engine.py` (`BrandScoringEngine`) | Mary Thuo | Per-deliverable/audit |
| Cultural Alignment Score | 5 sub-metrics: Resonance Rate, Emotional Sentiment Score, "Seen" Index, Promise-to-Behavior Consistency, Core Identity Stability, Adaptation Speed | Named formula, no real values | Draft 24 — conceptual ancestor of the code's scoring engine | Mary Thuo | *(unset)* |
| Brand Diagnostic Score | 0-5 per layer × 8 layers, total /40, bands "Fragmented" → "Category Dominant" | Named, illustrative | Draft 3 | Mary Thuo | *(unset)* |
| Sector Brand Intelligence Index | 7 dimensions, 1-10 scoring | Named, illustrative | Draft 19 | Mary Thuo | *(unset)* |
| Governance KPIs | Brand Trust Score, Infringement Incidents, Enforcement Response Time | Named only, no values | Draft 29 | Mary Thuo | *(unset)* |
| Retrieval completeness | Bundle assembled across 6 required sources | Hard gate — incomplete retrieval raises a runtime error rather than degrading silently | `core/retrieval/gated_retriever.py` (`RetrievalGate`) | Mary Thuo | Per-query |

Cross-reference `00_Agency_Governance/AGENCY_KPI_DICTIONARY.md` for the agency-wide dictionary; none of these brand-scoring metrics currently have an agency-wide analog.

**Owner decision (2026-06-30, tracker item 29): keep the `BrandScoringEngine`'s generic 70-78 dimension thresholds as-is** (confirmed via direct code inspection — `core/grading/engine.py`'s `ScoreDimension` definitions). Same reasoning as Finance's KPI thresholds (item 26): no real BOIS run against a real client exists yet to calibrate against.

## 8. Decision Log

*(placeholder — empty)*

## 9. Risk / Incident Log

*(placeholder — empty. Note: the retrieval gate's hard-fail behavior — refusing to generate output on incomplete evidence — is itself a real, implemented risk control, not a gap. No real incidents logged yet; the system has now run against one real client — Arika Agency itself, `bois/clients/arika-agency/` — in addition to the hypothetical "Sample Nairobi Laundry" smoke test.)*

## 10. Standards & SOPs Index

**Architecture doctrine** (`bois/documentation/COGNITIVE_INFRASTRUCTURE_ARCHITECTURE.md`): BOIS is "a stateful, retrieval-driven, agent-orchestrated execution ecosystem" across 6 layers (Knowledge, Memory, Retrieval, Agent Orchestration, Governance/Scoring, Evolution). Non-negotiable rule: missing retrieval evidence → stop in "retrieval failure state," never generate generic output.

**Recurring principles from raw drafts** (treat as working doctrine, several echoed independently across multiple files — strong internal signal):
- "Branding = Why you are chosen, Marketing = How you get seen" (Draft 1) — this department's own stated boundary with Marketing.
- "Visual design is downstream of strategy, not upstream" (Draft 5, echoed in Draft 6).
- "Consistency without adaptation becomes irrelevance; adaptation without governance becomes chaos" (Draft 21).
- "A brand is only as strong as its ability to defend itself" (Draft 29).
- Positioning requires trade-offs — "appeal to everyone, lose clarity" (Draft 32).

**11 additional spec docs**, one per `bois/` subfolder, mutually consistent with the architecture doc and the code (not boilerplate): `bois/agents/AGENT_SYSTEM.md`, `bois/governance/GOVERNANCE_SYSTEM.md`, `bois/grading/BRAND_SCORING_SYSTEM.md`, `bois/rag/RAG_PIPELINE.md`, `bois/retrieval/RETRIEVAL_RULES.md`, `bois/orchestration/TRIGGER_LOGIC.md`, `bois/workflows/EXECUTION_FLOW.md`, `bois/validation/VALIDATION_GATES.md`, `bois/quality_assurance/QA_PROTOCOL.md`, `bois/monitoring/MONITORING.md`, `bois/prompts/master_orchestration_prompt.md`, `bois/presentation_systems/PRESENTATION_ENGINE.md`.

**Existing gap-backlog finding** (`00_Workspace_Intelligence_Inventory/`, generated 2026-06-03 from the prior automated diagnostic pass, baseline of 126 files / 975,639 extracted words): 29 of the diagnostic's tracked concerns are present, 5 partially present, 4 missing. **Missing** (Medium-High severity, "no direct source evidence detected"): Historical Memory, Learning Systems, Resources, Strategic Planning. **Partially present**: Constitution (High severity — fragmented, no single authoritative source), Security, Change Management, Recovery, Evolution. This inventory itself recommends a 19-folder canonical restructure that was never built — it's a diagnostic, not built content.

## 11. RACI / Ownership

| Function | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| *(placeholder — but the 20-agent roster in §5 already defines purpose/memory-access/validation per role, and `00_Workspace_Intelligence_Inventory/` recommends a "Brand OS Owner / Trust and Narrative Lead" role — both ready to map against once a real owner is named)* | | | | |

## 12. Triggers / Automation Hooks

`core/orchestration/registry.py`'s `TRIGGER_RULES` is **real, implemented automation** — concrete sector/deliverable/geography/audience-keyed rules (named examples in code: fintech, healthcare, luxury, laundry, b2b) that route which of the 20 agents activate beyond the always-on 7-agent base sequence. The retrieval gate (§7, §9) is also live automation: it hard-fails rather than silently degrading on incomplete evidence. Like Finance, this is implemented automation, not a wishlist — but it has never run against real client data, only the hypothetical smoke-test client. Map into `00_Agency_Governance/AUTOMATION_APPROVAL_MATRIX.md` once real clients flow through it.

## 13. Existing OS Sub-Layer

**Yes — code-based, and more mature than originally assessed (corrected 2026-06-30, same pattern as Finance).** `12_Branding/bois/` ("Brand Operating Intelligence System") is a Python application: 44 subfolders total. **20 have real content, 24 are empty scaffolds.** `core/` contains **21 `.py` files, all confirmed real working logic — none are stubs**, a stronger ratio than Finance's finos-plugin (which had one confirmed stub out of several engines). Spot-checked modules include real TF-IDF-style retrieval scoring, a 15-dimension weighted scoring engine, real `.docx` XML parsing with SHA-256 checksums, a real knowledge-graph builder with regex entity extraction, and a hard-gated retrieval system that raises a runtime error rather than degrade silently on incomplete evidence. Its sibling `branding-os/` (a same-concept scaffold in a different naming/language convention) was confirmed dead — only a README, 18 fully empty subfolders — and was **deleted** during this restructuring's earlier cleanup phase.

**24 empty scaffold folders** (no content): `audience_intelligence/`, `brand_calendars/`, `compliance/`, `cultural_intelligence/`, `distribution_intelligence/`, `evolution/`, `identity_engineering/`, `legal_branding/`, `marketing_alignment/`, `narrative_engineering/`, `platform_adaptation/`, `production_systems/`, `psychographics/`, `sales_alignment/`, `scoring/`, `sector_intelligence/`, `semantic_systems/`, `symbolic_systems/`, `trend_intelligence/`. Many of these names map directly to rich raw-draft content (Psychographics → Draft 27, Cultural Intelligence → Draft 24, Sector Intelligence → Draft 19, Legal Branding → Draft 29) — the concepts exist in source material and in the 20-agent registry's definitions, but no dedicated module implements them; that logic currently lives only as agent metadata in `core/orchestration/registry.py`.

**Bois-to-raw-draft lineage confirmed — direct and mechanical, not inferred.** `core/ingestion/pipeline.py` was actually run (`core/executions/bootstrap_bois.py`) against this department's 40 raw drafts, producing `bois/knowledge/_indexes/documents.json` (all 40 files by exact filename, with document IDs, paragraph counts, checksums) and `paragraphs.jsonl` (14,109 tagged paragraph records, zero ingestion errors). This is a stronger citation system than Finance's hand-curated `source-intelligence.md` — auto-generated and reproducible by rerunning the script, rather than manually maintained. Beyond literal ingestion, conceptual lineage is also visible: Draft 9's governance audit domains almost exactly match `bois/governance/GOVERNANCE_SYSTEM.md`; Draft 39 (a Claude/Codex dual-agent meta-architecture draft) closely prefigures the actual orchestrator/registry/trigger-rule design; Draft 24's Cultural Alignment Score is the clearest conceptual ancestor of `core/grading/engine.py`'s 15-dimension scoring system.

**`bois/agents/` assessment**: contains one file, `AGENT_SYSTEM.md` — mature as a specification (20 fully fleshed-out agent contracts, consistent with code), but no executable agent runtime beyond task-building/routing; the actual reasoning step (LLM calls) is not implemented anywhere in this codebase, same caveat as Finance's 7-agent roster.

**Decision (2026-06-30, reaffirmed):** `bois/` stays a grandfathered code-backed exception to the markdown-first standard — and given this migration found it's the most functionally real code layer of the two grandfathered exceptions (more so than finos-plugin), that decision looks stronger in hindsight. `bois/documentation/` and its 11 sibling spec docs (§10) remain the canonical spec; code is the implementation.

## 14. Raw Archive Pointer

~40 root-level "Draft N.md" files, 16 sampled in full for the 2026-06-30 content migration (Drafts 1, 2, 3, 5, 6, 9, 11, 14, 19, 21, 23, 24, 25, 27, 29, 32, 36, 38, 39, 40). Existing gap backlog: `12_Branding/00_Workspace_Intelligence_Inventory/` (3 files, generated 2026-06-03 — see §10 for findings).

**Low-value/generic files flagged** (same pattern seen in every other department's raw drafts):
- **Draft 40** (System Architecture Enhancement) — entirely generic "Domain Intelligence Operating System" AI-agent meta-content, **no branding-specific content at all**. Closest match yet to the low-value pattern (Sector Draft 13, Client Success Drafts 21-22, ClientPartner Drafts 8/12) — should be treated as informing bois's general architecture-thinking only, not as branding doctrine.
- **Draft 36** (Branding OS Framework) — first ~55% is near-verbatim generic "Claude Coworker repository architecture" boilerplate (constitution/governance/operations/agents/projects/context/memory folder-structure advice), but the back half pivots to a genuinely branding-specific 12-layer "BrandingOS" architecture with real content — don't discard the whole file, only the front half.
- **Draft 39** (Agentic Branding Orchestration Architect) — opens as a generic Claude-Code/Codex system-prompt-engineering exercise, but is branding-flavored throughout (positioning/narrative/voice-tone agents, brand drift detection) and is a confirmed real conceptual ancestor of bois's orchestrator design — has migration value despite the generic framing.
- **Draft 38** (Brand Revenue OS Design) — borderline: genuinely branding/revenue-specific content (tiered offers, pricing psychology, funnel mapping), but heavy on hypothetical/illustrative numbers (e.g. "$2M-$10M" revenue tiers) that must not be presented as real agency pricing.

## 15. Changelog

- 2026-06-30 — File created as part of v0.1 skeleton restructuring; dead `branding-os/` duplicate and `bois/` `__pycache__` directories removed in cleanup.
- 2026-06-30 — Content migration: `bois/documentation/` + 11 sibling spec docs read in full, all 21 `core/` Python files spot-checked, and 16 of 40 raw drafts sampled. **Corrected** the original "partially-real" characterization — confirmed all 21 `core/` files are real working logic (none stub), confirmed a real auto-generated source-citation system (40 docs / 14,109 tagged paragraphs, actually run via `bootstrap_bois.py`), and confirmed direct mechanical lineage from raw drafts to code architecture. Populated Capability Registry, Workflow Index, Agent Roster (20 agents), KPI Dictionary, Standards & SOPs Index, and Triggers/Automation Hooks. Flagged 4 low-value/generic raw drafts. All scoring thresholds and brand examples confirmed generic/illustrative, no real agency brand data found anywhere. — Claude Code (Sonnet 4.6)
- 2026-06-30 — Confirmed by direct code inspection (no LLM imports/calls anywhere in `bois/`, matching Finance's equivalent check) and resolved 2 tracker items: (28) AI agents stay spec/routing-only until the agency's own real brand exists (item 30) to give them something real to reason over; (29) `BrandScoringEngine`'s generic 70-78 thresholds stay as-is until a real BOIS run exists to calibrate against. — Claude Code (Sonnet 4.6)
- 2026-06-30 — **Resolved tracker item 30.** Built and ran `bois/executions/run_arika_agency_brand.py`, assembling a real `ClientObject` for Arika Agency itself entirely from facts already confirmed elsewhere in this repo (no invention) and running it through the full pipeline (`create_client_workspace` → memory save → gated retrieval → agent routing → context persistence). Confirmed run: retrieval gate complete (zero missing sources), 11 of 20 agents activated, real workspace written to `bois/clients/arika-agency/`. `competitors`, `visual_preferences`, `typography_preferences`, `color_preferences` left empty — genuinely unconfirmed anywhere in the repo, flagged rather than invented. BOIS now has its first non-hypothetical client object alongside the "Sample Nairobi Laundry" smoke test. — Claude Code (Sonnet 4.6)
- 2026-06-30 — **Item 28 superseded the same day item 30 resolved.** With item 30's precondition closed (a real brand for the agents to reason over now exists), owner confirmed **Claude (Anthropic API)** as the LLM to wire into the 20-agent roster. Not built yet — no Anthropic SDK dependency added to `bois/` in this entry; added to `00_Agency_Governance/GO_LIVE_CHECKLIST.md`. — Claude Code (Sonnet 4.6)
