# Marketing — Department OS

**Department:** Marketing (03)
**Position in flow:** Receives packaged offers from Offer (02); generates demand (in close partnership with Content, 04); hands off qualified opportunities to Sales (05).
**Mandate:** Own positioning, campaign strategy, channel strategy, and demand generation. Content creation/production and narrative architecture are owned by the sibling Content department (04) — see that department's OS file.
**Owner:** Mary Thuo

> See [`GLOBAL_OS.md`](../GLOBAL_OS.md) for how this file fits into the whole system. Read that first if you haven't.

---

## 1. Identity

Marketing turns packaged offers (from Offer) into market demand and qualified opportunities for Sales, across positioning, SEO/AEO/GEO, campaigns, and channel strategy — working closely with Content (04) on execution. Per its own architecture doc (`Elite_Marketing_Agentic_OS/01_Master_Agentic_Marketing_System.md`), this department runs a 9-stage marketing cycle (Intelligence → Strategy → Production → Distribution → Conversion → Retention → Measurement → Optimization → Scale) through a dual-agent runtime: a Strategic Cognition Layer (analysis, positioning, messaging doctrine) and an Execution Engineering Layer (funnels, automation, tracking, dashboards) — and is governed by 7 stated non-negotiable principles (intelligence-before-execution, narrative coherence, conversion accountability, closed-loop learning, governance-over-activity, channel-as-signal, asset compounding).

## 2. Status

**Second-most mature department — content migration complete (2026-06-30), medium confidence.** `Elite_Marketing_Agentic_OS/` was verified to be genuinely grounded in this department's own raw drafts (its master doc self-declares specific source drafts by number, e.g. "THE MARKETING MECHANISM 101/102, Marketing 201/202..." — not a generic template bolted on top). **Important contrast with Sales (05): this layer has zero citation/paragraph-level sourcing** — confirmed via grep, no CSV or index file maps any claim back to a specific source paragraph. And the underlying raw drafts themselves are confirmed to be generic AI-chat-transcript brainstorming (most open with a literal "You are an elite Marketing Operating System Architect..." prompt), not the agency's lived operating history. So: structurally well-organized and traceable to its sources, but every KPI value, client segment, and tool reference below should be read as a template/aspirational target, not a verified historical figure. One real-world signal surfaced: a reference to the "Kenya Data Protection Act" alongside GDPR/CCPA in one draft — possibly indicates real agency operating geography; added to the owner-input tracker for confirmation rather than assumed.

## 3. Capability Registry

| Capability | Description | Status |
|---|---|---|
| Market/signal intelligence | Signal ingestion and scoring, competitive intelligence, cultural/narrative signal analysis, voice-of-customer mining | Grounded in raw drafts, no real data yet |
| Positioning & offer doctrine | Brand positioning, category design, offer architecture, pricing psychology, messaging doctrine | Grounded; overlaps with Offer (02) and Branding (12) — needs reconciliation |
| Creative production | Storyboard/script engineering, visual language, prompt composition, creative QA | Grounded |
| Content/editorial systems | Topic clustering, platform adaptation, content atomization, publishing cadence | Grounded; overlaps with Content (04) — see §1 mandate split |
| Distribution & demand generation | Paid media, social growth, PR, community growth, influence/partnership | Grounded; overlaps with ClientPartner Acquisition (06) on partnership channel |
| Discoverability (SEO/AEO/GEO) | Search intent mining, semantic structure, answer-engine optimization, generative-citation optimization | Grounded — one of the more concretely detailed agent specs (4-layer discoverability stack: Data/Semantic/Retrieval/Interface) |
| Conversion & funnel engineering | Funnel architecture, landing pages, CTA systems, lead scoring, sales handoff SLA | Grounded |
| Lifecycle/retention | Onboarding acceleration, retention/loyalty, expansion/upsell, churn recovery | Grounded |
| Measurement & attribution | Tracking systems, attribution/incrementality, experimentation program management, executive dashboards | Grounded; no real formulas/values defined |
| Marketing ops & automation | SOP architecture, workflow automation, integration/connector engineering, incident response | Grounded; see §12 — connector blueprint is entirely aspirational, no confirmed real integrations |

All "grounded" = traceable to this department's own raw drafts per the spot-check in §14, but not citation-verified the way Sales's Agent Registry is, and not backed by real performance data.

## 4. Workflow Index

| Workflow | Trigger | Steps | Output | Owner | Source |
|---|---|---|---|---|---|
| Workflow A — Strategy to Market Launch | New campaign/offer needs launching | 7 steps (strategy → production → distribution) | Live campaign | Mary Thuo | `Elite_Marketing_Agentic_OS/03_Skill_Workflow_Rulebook.md` |
| Workflow B — Storyboard to Image Generation Pipeline | Creative asset needed | 10 steps (storyboard → script → prompt package → generation → QA) | Approved creative asset | Mary Thuo | same |
| Workflow C — Weekly Optimization Cycle | Time-based (weekly) | 5 steps (review → diagnose → hypothesize → test → encode) | Updated campaign performance | Mary Thuo | same |
| 30/60/90 Activation Rollout | New department/system activation | Phase 1 (Day 1-30, Foundation & Control) → Phase 2 (Day 31-60, Execution & Learning Velocity) → Phase 3 (Day 61-90, Scale, Reliability, Compounding), each with named owner-agent and gate KPIs (e.g. "≥90% event integrity," "≥95% automation uptime") | Department fully activated | Mary Thuo | `Elite_Marketing_Agentic_OS/07_30_60_90_Activation_Rollout_Plan.md` |
| Execution cadence (daily/weekly/monthly/quarterly/annual) | Time-based | Full operating rhythm with named owner-agent per tier | Ongoing department operations | Mary Thuo | `Elite_Marketing_Agentic_OS/05_Execution_Cadence_Playbooks.md` |

## 5. Agent Roster

**11 Tier-0 "chief" agents** + ~55 named subagents, defined in `Elite_Marketing_Agentic_OS/` (Agent Cards + `02_Agent_Catalog_and_Subagents.yaml`). This section is the summary index **+ runtime migration status**.

**Quality note (still true):** the 11 cards are structurally identical templates (same input/output contract + runtime-prompt wrapper, mission/KPIs/workflows swapped per agent) and — unlike Sales' Agent Registry — carry **no source-paragraph citations**. Grounded in this department's own drafts, but templated, not corpus-verified. The migrated specs flag this: they instruct each agent to mark assumptions and never present a templated figure as measured.

**Runtime status (2026-07-14).** Triaged into the Arika Runtime — 9 Marketing-core agents wired, 2 held for their real departments.

**🟢 Live in the Arika Runtime — 9 Marketing-core agents** (`.claude/agents/marketing-*.md`, advisory-first, memory → `03_Marketing/_memory/runtime.jsonl`; output = the cards' 7-part contract — situation / decision / directives / kpi_forecast / risks / escalation / memory):

| Chief agent | Runtime spec | Class |
|---|---|---|
| Marketing OS Orchestrator | `marketing-orchestrator` | 1 |
| Market Intelligence Lead | `marketing-market-intelligence` | 1 |
| Chief Marketing Strategist | `marketing-chief-strategist` | 1 |
| Demand Generation Strategist | `marketing-demand-generation` | 2 |
| SEO / AEO / GEO Architect | `marketing-seo-aeo-geo` | 1 |
| Funnel Architect | `marketing-funnel-architect` | 1 |
| Lifecycle Marketing Architect | `marketing-lifecycle` | 2 |
| Attribution & Modeling Architect | `marketing-attribution-modeling` | 1 |
| Marketing Ops Governor | `marketing-ops-governor` | 1 |

**Cross-department event chain now wired end-to-end:** `marketing-funnel-architect` emits `LEAD_CREATED` → `sales-lead-qualification` (05) already listens; `sales-execution-closing`'s `DEAL_CLOSED_WON` → `marketing-lifecycle` picks up the post-conversion journey. Marketing ↔ Sales are connected.

**🟠 Held for their real departments — 2 cross-dept agents** (mandate belongs elsewhere; cards preserved, not duplicated):
- **Creative Director Agent** → Design (19) + Experience Engineering (20) already run creative-director agents (asset production + interactive experiences); Marketing hands campaign creative to them rather than running a third.
- **Content Strategy Director** → Content (04) is its own department.

The ~55 subagents remain as reasoning lenses inside each chief's system prompt, not separate runtime agents. Boundary notes baked into the specs: Chief Strategist's offer/pricing subagents defer to Offer (02); Market Intelligence is scoped to campaign/demand intelligence (Sector 01 owns foundational sector truth); SEO/AEO/GEO coordinates with EE (20)'s web-build discoverability pillar; Lifecycle coordinates with Client Success (07) on delivery.

## 6. Skill Library Index

~20 named skills in `Elite_Marketing_Agentic_OS/03_Skill_Workflow_Rulebook.md`, each with Owner/Intent/Outputs/Quality-gates (e.g. `signal_ingestion_and_scoring`, `positioning_doctrine_builder`, `storyworld_architecture`, `script_engineering`, `prompt_package_generation`, `funnel_friction_diagnostics`, `lead_scoring_intelligence_model`, `attribution_and_incrementality`). Uncited, same caveat as the Agent Roster.

## 7. KPI Dictionary (department-local)

**All values below are template/industry-standard benchmarks, not this agency's historical figures** — no real campaign results, dollar figures, or named-client data were found anywhere in the sampled raw drafts.

| Metric | Formula | Draft value(s) found | Source | Owner | Cadence | Threshold |
|---|---|---|---|---|---|---|
| LTV:CAC ratio | See `AGENCY_KPI_DICTIONARY.md` | 3:1 healthy, 4-5:1 strong, <3:1 inefficient | Elite_Marketing_Agentic_OS rollout plan | Mary Thuo | *(unset)* | *(unset)* |
| CAC payback period | Months to recover CAC | <6mo aggressive-viable, 6-12mo stable, >12mo risk | same | Mary Thuo | *(unset)* | *(unset)* |
| Event tracking integrity (rollout gate) | % of expected events correctly tracked | ≥90% | `07_30_60_90_Activation_Rollout_Plan.md` | Mary Thuo | *(unset)* | *(unset)* |
| Automation uptime (rollout gate) | % uptime of marketing automations | ≥95% | same | Mary Thuo | *(unset)* | *(unset)* |
| Funnel stage improvement (rollout gate) | % improvement in a core funnel stage | ≥15% | same | Mary Thuo | *(unset)* | *(unset)* |
| Named-but-undefined agent KPIs | Portfolio ROMI, Signal Confidence Score, Message-Market Fit, Creative Resonance Score | No formulas or baselines given anywhere | Agent Cards | Mary Thuo | *(unset)* | *(unset)* |

Client segmentation thresholds also appear (Startup <$2M, Growth $2M-$10M, Scale/Enterprise $10M+) — template tiers, not verified real client data; cross-reference `00_Agency_Governance/CRM_SCHEMA.md` if a real segmentation model gets adopted.

## 8. Decision Log

- **2026-06-30 — Confirmed Kenya as a real operating geography**, plus broader confirmation the agency serves clients globally and must comply with each jurisdiction's real advertising/copyright/data-protection laws as engagements happen. See §14.
- **2026-07-04 — Social Ecosystem platform-role model added** (§10), elaborating the existing Distribution & Demand Generation capability (§3) with a real per-platform role/KPI table and repurposing flow, sourced from the owner's pasted social-ecosystem plan for the Arika website project (`20_Experience_Engineering/ARIKA_WEBSITE_PROJECT.md`). Explicitly reconciled against Content (04)'s existing pillar/house/Story Architecture structures rather than inventing a competing content taxonomy. Zero social accounts exist yet — planning-only.

## 9. Risk / Incident Log

*(placeholder — empty)*

## 10. Standards & SOPs Index

**Escalation doctrine** (appears in both the master doc and skill rulebook): 3-tier severity (SEV-1/2/3).

**Mandatory global rules**: "No skill runs on ambiguous objective"; "No campaign scale decision without measurement confidence."

**Memory and Learning Flywheel**: 5-layer model (Doctrine / Market / Experiment / Campaign / Incident memory) with an Observe → Classify → Hypothesize → Test → Decide → Encode → Reuse cycle. Currently a designed pattern, not populated with real entries (same status as Sales's empty Memory Logs).

**Quality rubrics**: Creative QA, Funnel QA, Data QA — named but not detailed with specific pass/fail criteria in what was sampled.

**Social Ecosystem — platform architecture (added 2026-07-04, alongside the Arika website project, `20_Experience_Engineering/ARIKA_WEBSITE_PROJECT.md`).** Elaborates the Distribution & Demand Generation capability (§3) with a real platform-role model, per the owner's pasted social-ecosystem plan. **Flag up front: zero social media accounts exist yet** (`00_Agency_Governance/GO_LIVE_CHECKLIST.md` item 23, still an open owner action) — everything below is planning-only until accounts are created; it does not change §12's "none of the 7 connector layers are in use yet" status.

*Platform roles* (primary role + KPI per platform, not a flat channel list):

| Platform | Primary role | KPI |
|---|---|---|
| LinkedIn | Executive authority & B2B lead generation | Qualified leads |
| Instagram | Brand storytelling & visual education | Engagement |
| YouTube | Long-form education & SEO | Watch time, subscribers |
| TikTok | Discovery & reach | Views, shares |
| X (Twitter) | Real-time insights & conversations | Impressions, discussions |
| Facebook | Community & retargeting | Community growth |
| Threads | Thought leadership | Engagement |
| Pinterest | Visual discovery | Website traffic |
| Newsletter/Substack | Owned audience | Subscribers |

Every platform is a **distribution endpoint**, not a separate content strategy — content itself is owned by Content (04), tagged by pillar/house (`04_Content/CONTENT_OS.md` §10), not reinvented per-platform here.

*Repurposing flow* (one flagship asset → many formats, not separate production per channel): `Research → Flagship Article → Video → Podcast → LinkedIn Article → Instagram Carousel → Reel → Short-form (TikTok/Shorts) → Newsletter → Website Resource`. This is the same "content multiplication" idea already named in Content's own Capability Registry (`04_Content/CONTENT_OS.md` §3) — this section is the distribution-side view of that same real capability, not a competing one.

*Social conversion path* (every platform should support the same progression, not invent its own funnel): `Discovery → Educational content → Framework → Free resource → Email list → Assessment → Strategy session → Proposal → Client → Case study → Referral` — matches Content's existing Story Architecture sequencing (`04_Content/CONTENT_OS.md` §10) at the experience-distribution level, and feeds the same Assessments/Book-a-Strategy-Session pages in the website sitemap (`20_Experience_Engineering/ARIKA_WEBSITE_PROJECT.md` §3).

## 11. RACI / Ownership

| Function | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| *(placeholder)* | | | | |

## 12. Triggers / Automation Hooks

`04_MCP_API_Connector_Blueprint.md` defines 7 connector-class layers (Intelligence, Strategy/Knowledge, Creative Production, Distribution, Discoverability, Conversion/Lifecycle, Measurement/Ops) naming connector types per layer (e.g. paid media platform APIs, image generation API, email automation API, LLM citation observation connector) with an owner agent per layer. **Confirmed entirely aspirational** — no API keys, account IDs, or evidence of actually-configured integrations; this is a connector taxonomy/wishlist, not a working integration inventory. **Owner-confirmed (2026-06-30, tracker item 14): none of the 7 layers are actually in use yet** — same pattern as Finance's integrations (items 25-27) and Branding's agent wiring (item 28). Treat as the target shape for `00_Agency_Governance/AUTOMATION_APPROVAL_MATRIX.md` rows once any of these are actually built, not as live automation today.

**Update (2026-07-01) — the "Creative Production" and "Distribution" layers are no longer generic placeholders.** The new Design (19) department gives the Creative Production layer's "image generation API" a concrete home: Canva is confirmed connected as the Creative Assembly platform (`19_Design/DESIGN_OS.md` §3), and the AI generation/enhancement vendor chain feeding it is documented (though vendor-undecided) as Design's Production Engine. The Distribution layer's engagement/DM-automation piece is now documented as Automation (16)'s new Engagement Layer workflow (`16_Automation/AUTOMATION_OS.md` §4) — ManyChat proposed but no account exists yet. Both remain **not live** — this update only replaces vague placeholders with a real cross-reference, it does not change the "none of the 7 layers are actually in use yet" status.

## 13. Existing OS Sub-Layer

**Yes — verified grounded but uncited (2026-06-30).** `03_Marketing/Elite_Marketing_Agentic_OS/` (19 files: 7 root + `Agent_Cards/` with 11 cards) contains a master architecture document, an agent catalog YAML, 11 Agent Cards, skill/workflow rulebooks, MCP connector blueprints, execution cadence playbooks, and a 30/60/90 rollout plan — all generated in one pass (dated 2026-05-19). This is a markdown-only design (no code, unlike Finance/Branding) — closer in spirit to the markdown-first standard than those two.

**Verified finding**: the master doc self-declares its source drafts by number, and spot-checking confirmed the dual-agent architecture and the SEO/AEO/GEO 4-layer discoverability stack are genuinely derived from this department's own raw material (Drafts 110, 111, 62), not an externally-imposed generic template. **Gap vs. Sales (05)**: zero citation/paragraph-level sourcing exists anywhere in this layer — confirmed via grep, no CSV/index file maps any specific claim to a specific source paragraph. All 11 Agent Cards are also structurally identical templates with only mission/KPI/workflow content swapped, rather than individually distinct documents.

**Known maintenance issue (not fixed in this pass):** `06_Agent_Cards_Index.md` contains stale absolute file paths referencing the pre-restructuring folder name (`C:\...\Marketing Drafts\Elite_Marketing_Agentic_OS\...` instead of `03_Marketing\...`) — broken links, left as-is consistent with this pass not editing existing OS-sub-layer source content directly (same treatment as finos-plugin/bois).

## 14. Raw Archive Pointer

~122 root-level "Draft N.md" files (largest single folder in the repo) — not all individually read; 9 were spot-checked for the 2026-06-30 content migration (`Agentic Marketing Orchestration Architect. Draft 111`, `Elite System Architecture. Draft 115`, `360 Marketing System Roles. Draft 39`, `CAC and ROI Analysis in Marketing. Draft 50`, `SEO AEO GEO Architecture. Draft 62`, `Marketing Operating System Architect. Draft 110`, `Marketing Legal Structures. Draft 32`, `Marketing Payment Sytem. Draft 34`, `Social Media Marketing. Draft 58`). Existing gap backlog: `03_Marketing/00_Workspace_Intelligence_Inventory/` (confirms 0 CSV registries/indexes, 0 JSON assets at baseline — consistent with the no-citation finding above). One confirmed exact-duplicate file (`CAC and ROI Analysis in arketing.md`) was already deleted during cleanup — its canonical twin `CAC and ROI Analysis in Marketing. Draft 50.md` remains.

**Finding:** nearly every sampled raw draft is an AI-chat-transcript brainstorm (opens with a literal "You are an elite Marketing Operating System Architect..." prompt) — confirms the underlying source material is generic AI-generated strategy theory, not the agency's lived operating history, even though `Elite_Marketing_Agentic_OS/` is faithfully derived from it. One real-world signal: `Marketing Legal Structures. Draft 32.md` references the "Kenya Data Protection Act" alongside GDPR/CCPA.

**Confirmed by owner, 2026-06-30:** Kenya is real — Arika Agency operates in/serves Kenya. More broadly, the owner confirmed the agency operates globally and must comply with the relevant advertising, copyright, and data-protection laws of every jurisdiction it serves, not just Kenya/GDPR/CCPA. Treat compliance content in this department as needing a genuinely multi-jurisdictional posture (jurisdiction list not yet enumerated — add real countries/regions as real engagements happen, don't pre-build a speculative global list).

## 15. Changelog

- 2026-06-30 — File created as part of v0.1 skeleton restructuring; one confirmed duplicate file removed.
- 2026-06-30 — `360 Agency Content`, briefly merged in as a subfolder, corrected back out to its own standalone department (`04_Content/`) per owner feedback; Sales department reference updated from (04) to (05) following the resulting renumbering.
- 2026-06-30 — Content migration: `Elite_Marketing_Agentic_OS/` extracted and spot-verified as genuinely grounded in this department's raw drafts, but confirmed to have no citation system (gap vs. Sales) and no real historical KPI data. Capability Registry, Workflow Index, Agent Roster, Skill Library Index, KPI Dictionary, Standards & SOPs Index, and Triggers/Automation Hooks populated, all marked template/aspirational where applicable. Kenya jurisdiction signal flagged for owner confirmation. — Claude Code (Sonnet 4.6)
- 2026-06-30 — Owner confirmed (tracker item 14): none of the 7 MCP/connector-class layers in §12 are actually in use yet. — Claude Code (Sonnet 4.6)
- 2026-07-01 — Added §16 Memory/Feedback Loop/Cadence per the go-live plan in `00_Agency_Governance/GO_LIVE_CHECKLIST.md`. — Claude Code (Sonnet 5)
- 2026-07-01 — Cross-linked §12's aspirational MCP connector blueprint to the new Design (19) department (Creative Production layer → Canva/Production Engine) and Automation (16)'s new Engagement Layer (Distribution layer → ManyChat/DM automation). Status unchanged — still none of the 7 layers are actually in use. — Claude Code (Sonnet 5)
- 2026-07-04 — **Added Social Ecosystem platform-role model** (§10, §8) for the new Arika website project (`20_Experience_Engineering/ARIKA_WEBSITE_PROJECT.md`) — platform-role/KPI table, repurposing flow, and social conversion path, reconciled against Content (04)'s existing pillar/house/Story Architecture structures. Zero social accounts exist yet (`GO_LIVE_CHECKLIST.md` item 23) — flagged explicitly as planning-only. — Claude Code (Sonnet 5)
- 2026-07-14 — **Marketing got a live execution layer — 9 of 11 chief agents wired into the Arika Runtime.** Triaged the roster (not migrated wholesale): authored the **9 Marketing-core chiefs** as advisory-first `.claude/agents/marketing-*.md` specs, each grounded in its Agent Card + `02_Agent_Catalog_and_Subagents.yaml` (Orchestrator, Market Intelligence, Chief Strategist, Demand Generation, SEO/AEO/GEO, Funnel Architect, Lifecycle, Attribution & Modeling, Ops Governor), using the cards' 7-part output contract as the structured schema. **Wired the Marketing↔Sales chain**: `marketing-funnel-architect` emits `LEAD_CREATED` (→ `sales-lead-qualification`); `sales-execution-closing`'s `DEAL_CLOSED_WON` → `marketing-lifecycle`. **Held 2 cross-dept agents** — Creative Director (→ Design 19 / EE 20, which already run creative directors) and Content Strategy Director (→ Content 04) — rather than duplicating. The ~55 subagents stay as reasoning lenses inside each chief's prompt. Baked in boundary notes (offer/pricing → Offer 02; foundational market truth → Sector 01; web-build discoverability → EE 20; delivery → Client Success 07) and the standing honesty caveat that these specs are templated/uncited. Advisory-only; Class 2 on Demand Gen + Lifecycle (spend/client-facing). §5 Agent Roster updated with the migration-status map. 30 agents now register in `arika list`; `npm test` 8/8; live model calls pending `ANTHROPIC_API_KEY`. — Claude Code (Opus 4.8)

## 16. Memory / Feedback Loop / Cadence

**Memory**: 5-layer "Memory and Learning Flywheel" (Doctrine/Market/Experiment/Campaign/Incident, §10) with an Observe→Classify→Hypothesize→Test→Decide→Encode→Reuse cycle — a designed pattern, not yet instantiated as real files (unlike Sales' `06_AI_Memory_Logs/`, `05_Sales/SALES_OS.md` §16). Gap: recommend mirroring Sales' Decision/Learning/Prompt-Evolution log structure under a new `Elite_Marketing_Agentic_OS/06_AI_Memory_Logs/` once this roster is wired to Claude. **Update 2026-07-14:** the machine-memory substrate now exists — the 9 wired chief agents append JSONL to `03_Marketing/_memory/runtime.jsonl` (the runtime's bois-compatible envelope) on every run; distill the 5-layer Flywheel rollups from that stream as real runs accumulate.

**Feedback Loop**: Already documented and real as a workflow — Workflow C, the Weekly Optimization Cycle (§4: review→diagnose→hypothesize→test→encode), is the feedback loop that fires when a rollout-gate KPI misses (§7: event tracking integrity <90%, automation uptime <95%, funnel stage improvement <15%). Output should be encoded into the Memory Flywheel's Experiment/Campaign layers once real logs exist.

**Cadence**: Full daily/weekly/monthly/quarterly/annual rhythm already exists (`05_Execution_Cadence_Playbooks.md`) — Weekly Optimization Cycle = Revenue + Opportunity Calendar, weekly; 30/60/90 Activation Rollout (§4) = Strategic Calendar, one-time-per-activation.
