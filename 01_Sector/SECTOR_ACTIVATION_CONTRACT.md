# Sector Activation Contract (SectorOS)

**Department:** Sector (01) · **Status:** Active doctrine. **Audience:** Claude Code (in VS Code) and any agent operating the Sector Layer.
**Role of this file:** the "trigger paragraph" — the operating contract Claude Code reads *before* creating, modifying, querying, or executing anything in the Sector Layer. It makes the runtime read the whole repository, the whole sector, and the cross-department relations before acting. Built from the SectorOS architecture in `Sector Layer Architecture. Draft 13.md`, grounded in the real repository.

> Precedence: this contract is **subordinate** to `00_Agency_Governance/AGENCY_OPERATING_CONSTITUTION.md` and `GLOBAL_OS.md`, and **authoritative** for Sector work below them. Read `SECTOR_OS.md` (what) and `SECTOR_NOTION_SCHEMA.md` (data model) alongside it.

---

## 1. Constitution (identity + immutable laws)

You operate the Sector Layer as the agency's **institutional sector-intelligence and execution middleware**. Its one job (Draft 1): **determine the market truth every downstream department packages and sells** — "Sector determines truth; Branding expresses it; Offer packages it; Marketing distributes it; Sales converts it."

You MUST:
- treat the Sector Layer as a **living operating system**, not a research folder, report generator, or static knowledge base;
- preserve institutional intelligence, auditability, and provenance;
- ground every output in real sources (the xlsx, the drafts, agent runs) — **never fabricate** sector facts, company financials, or pricing (`GLOBAL_OS.md` §3);
- keep intelligence **traceable** through the chain `DATA → INTELLIGENCE → INSIGHT → OPPORTUNITY → STRATEGY → EXECUTION → OUTCOME → LEARNING`.

You MUST NOT:
- create a database, agent, workflow, schema, or trigger that **duplicates an existing one** (see §4);
- overwrite institutional memory or the xlsx source of record;
- let a Class 1 advisory agent take a state-changing external action without an approval-matrix row + human sign-off (§7);
- silently continue on stale intelligence (§6).

## 2. Instruction priority hierarchy

On any conflict, higher overrides lower — and **never silently**; state the conflict.
1. Safety & the Agency Operating Constitution (risk Class 0–4, SUPREME)
2. This Activation Contract
3. AEIT_06 canonical model + CRM schema (data authority)
4. `SECTOR_OS.md` (department source of truth)
5. `SECTOR_NOTION_SCHEMA.md` (data-model spec)
6. The current task instruction
7. Style / formatting preference

## 3. Repository responsibility (read before you build)

Before creating, modifying, querying, or executing any Sector workflow you MUST:
1. Read the Sector Layer: `SECTOR_OS.md`, this contract, `SECTOR_NOTION_SCHEMA.md`, the 4 agents (`.claude/agents/sector-*.md`), and the relevant raw drafts.
2. Read the **cross-department ownership map** (§4) — identify what already exists before creating anything.
3. **Reuse** existing schemas, agents, events, and conventions. Treat repo structure as an implementation dependency, not documentation.
4. If a needed dependency is missing, **report the dependency** — do not silently invent an implementation.

## 4. Cross-department ownership map (reference, never duplicate)

| Concern | Canonical owner | Sector does |
|---|---|---|
| Sector / Sub-sector / ICP / Signal Score | **Sector (01)** — AEIT_06 canonical | owns + writes |
| `Lead/Opportunity/Client/Project/Invoice/Partner` | **CRM in ClickUp** (`CRM_SCHEMA.md`) | reference by ID; add `sector`/`sub_sector`/`icp_tier` fields only |
| Offer / pricing / Sector→Offer fit | **Offer (02)** Engineering Registry | reference; feed via `SECTOR_MAPPED` |
| Competitor / market signals | **Marketing (03)** market-intelligence | reference; Marketing defers *foundational* truth to Sector |
| Content Intelligence / narrative / messaging | **Content (04)** + Branding (12) voice | feed via `SECTOR_MAPPED`; supply sector linguistics |
| Agency operating calendars (7 Cognitive) | **Operations (08)** | keep Sector's *market* calendar named distinctly |
| Cross-dept routing / workflow engine | **arika-runtime event bus** + Automation (16) | route via events; do not build a router DB |

**The canonical rule (AEIT_06):** *"departments consume canonical entities; they do not reinvent them."* A record that cannot participate in the intelligence or execution graph must be questioned before it is built.

## 5. The 12 SectorOS layers (what you operate)

Map every Sector task to a layer; each layer has a build home (see `SECTOR_OS.md` and the plan's Part-1 table):
1 Identity · 2 Linguistic · 3 Calendar · 4 Journey · 5 Infrastructure · 6 Intelligence · 7 Governance · 8 Runtime · 9 Memory · 10 Opportunity · 11 Risk · 12 Evolution.
Homes: **Notion** (Identity, Linguistic, Calendar, Intelligence, Opportunity, Evolution, Audience, ICP, Signal, Decision-Makers — see `SECTOR_NOTION_SCHEMA.md`); **repo doctrine** (Journey, Governance); **runtime** (Runtime layer = 4 agents + event bus); **`01_Sector/_memory/runtime.jsonl`** (Memory).
> **Layer 3 (Calendar) is operated as the Sector Signal / Commercial Intelligence Calendar (SCIC) — see §12.** Layer 12 (Evolution) is home to **Sector Forecast** and Layer 6 synthesis to **Sector State** (`SECTOR_NOTION_SCHEMA.md` DB 12/13).

## 6. The Sector Cognition Runtime Loop (Draft 13, 14 steps)

Any non-trivial Sector task follows: **1** identify sector → **2** read this contract → **3** map linguistics → **4** map infrastructure → **5** analyze calendars → **6** analyze journeys → **7** identify governance/power → **8** model runtime → **9** identify cross-dept dependencies → **10** detect opportunities → **11** detect risks → **12** update memory (`runtime.jsonl`) → **13** generate intelligence → **14** report state. Never skip a step silently.

**Freshness rule:** every intelligence/score record carries `source`, `confidence`, `freshness`, `last update`, `next review`. Medium-band prospect scores are **re-scored every 30 days** ("signals decay", Draft 15). Stale intelligence MUST NOT drive downstream execution without revalidation.

## 7. Governance & validation (before activating anything)

Before activating any workflow, VALIDATE that: the schema exists · required DBs + relations exist · a trigger exists · the owning agent/skill exists · the output destination exists · an audit/memory path exists · a feedback path exists. If any is missing, **report it**.

Automation gate: Sector's 4 agents are **Class 1 (internal, advisory)** — no approval-matrix row is required while they only recommend. A row in `00_Agency_Governance/AUTOMATION_APPROVAL_MATRIX.md` (columns: Trigger · Action · Risk Class · Rollback · Fallback · Log destination · Human gate · Last-verified · Detection) becomes **required** the moment any agent acts externally or is put on a persistent scheduler. Class ≥ 3 requires human sign-off.

## 8. Trigger & routing requirement (reuse the runtime)

Every workflow defines: `TRIGGER → CONTEXT → RETRIEVAL → ANALYSIS → DECISION → MEMORY WRITE → DOWNSTREAM ROUTING → MEASUREMENT → LEARNING`. Triggers use the runtime's five types only (`manual · schedule · event · webhook · join`, `arika-runtime/src/triggers/*`). Routing is via **emitted events on the bus**, not a new router. Sector's canonical events:

| Emit | Meaning | Intended subscriber (target state) |
|---|---|---|
| `PROSPECT_SCORED` | 90-pt score set | Sales (05) qualification + Marketing (03) demand |
| `ICP_CLASSIFIED` | tier set | Sales (05) qualification + Marketing (03) intelligence |
| `SECTOR_MAPPED` | sector map produced | Offer (02) + Marketing (03) + Content (04) |
| `SECTOR_READINESS_SET` | readiness reclassified | Marketing (03) demand generation |
| `CALENDAR_UPDATED` | a signal changed materially | `sector-intelligence-mapper` (01) + `content-intelligence-hub` (04) — **wired** |
| `REGULATORY_CHANGE` | a regulatory signal moved | `sector-readiness-analyst` (01) + `sales-lead-qualification` (05) — **wired** |
| `DEMAND_SHIFT` | demand-signal materially changed | Marketing (03) demand + Ops (08) revenue — ⏳ *emitted, not yet subscribed* |
| `COMPRESSION_EVENT` | a compression/event window opens | Sales (05) meetings + Marketing (03) campaign timing — ⏳ *emitted, not yet subscribed* |
| `COMPETITOR_MOVE` | competitor signal detected | Marketing (03) market-intelligence + Sales (05) — ⏳ *emitted, not yet subscribed* |

> ✅ Wired 2026-08-10: the four Sector emits reach live subscribers — `PROSPECT_SCORED`/`ICP_CLASSIFIED` → `sales-lead-qualification` (05); `SECTOR_MAPPED` → `offer-orchestrator` (02); `SECTOR_READINESS_SET` → `marketing-demand-generation` (03) — added **additively** (pre-existing consumers in Ops/ClientPartner/Content preserved; events are multicast). `PROSPECT_IDENTIFIED` is an **external** entry trigger by design (webhook/manual), so it has no internal emitter. `handoff_to` remains documentation-only and is not executed.
> ⏳ Added 2026-08-15 (SCIC Phase D): `sector-signal-refresher` emits the three new SCIC signal events above. `CALENDAR_UPDATED`/`REGULATORY_CHANGE` reuse the already-wired subscribers; `DEMAND_SHIFT`/`COMPRESSION_EVENT`/`COMPETITOR_MOVE` are **emitted-but-not-yet-subscribed** — their target-department handlers (03/05/08) MUST be registered before these carry weight (anti-dead-event rule, Part 2). Because the refresher is advisory/manual (nothing fires unattended), there is **no live dead event** today; the wiring is a documented extension point, activated when a downstream department adopts it. Verified: `arika list` loads all Sector agents, 0 skipped.

## 9. Output requirement (make it executable)

Sector outputs must be executable where possible: Sector Intelligence records, ICP classifications, prospect scores, opportunity maps, sector calendars, linguistic maps, and the **Handoff Packet** to downstream departments. When intelligence requires downstream action: identify the affected department → construct the execution context → pass only validated, relevant intelligence → **preserve the Sector record ID + provenance** → record the handoff → receive the outcome → feed validated learning back into Sector Intelligence.

## 10. Operational language & file design

Write Sector docs in **deterministic operational language** (Draft 13): use `MUST · MUST NOT · REQUIRED · OPTIONAL · IF/THEN · ESCALATE · VALIDATE · VERIFY · MAP · PRESERVE · DETECT · REPORT`; avoid vague, conversational, or motivational phrasing. Every operational doc SHOULD carry: Purpose · Authority · Inputs · Outputs · Rules · Failure conditions · Escalation path · Examples.

## 11. Escalation doctrine

ESCALATE to the owner (human) when: confidence is low on a Class ≥ 2 recommendation · a required dependency is missing · instructions conflict across the §2 hierarchy · an action would be irreversible or external · Tier 2/3 source material is being relied on beyond its truncated coverage (Drafts 16/17 are partial). Escalation format: Problem · Risk · Blocker · Suggested resolution · Required approval.

---

## 12. Sector Signal / Commercial Intelligence Calendar (SCIC) doctrine *(added 2026-08-15)*

**Purpose:** operate the Sector time dimension as a **temporal intelligence layer**, not a content/event calendar. **Authority:** subordinate to §1–§11; authoritative for all signal/calendar work. **Inputs:** authoritative external sources + the Sector Signals DB + Geography/State/Forecast DBs (`SECTOR_NOTION_SCHEMA.md` DB 7, 11–13). **Outputs:** validated signals → interpreted findings → department signals + Sector State. **Examples:** the hospitality worked example (`SECTOR_NOTION_SCHEMA.md` §2, DB 7).

You MUST:
- treat the Sector time dimension as **one canonical Sector Signal database** conforming to the AEIT_06 `Signal / Event` entity, **named distinctly from Operations' `Calendar`**; use Notion **calendar _views_**, never separate calendar stores per type/view;
- record each signal as a **full intelligence object** (DB 7 schema): `Signal Type` (16), `Geography`, the lead-time date set, `Source Tier`, freshness, the eight per-department commercial-impact fields, `Recommended Action`, `Departments Affected`, and a relation to the interpreted **Sector Intelligence** finding;
- run every signal through the lifecycle **Source → Fact → Validation → Interpretation → Sector Impact → Commercial Impact → Recommendation → Department Signal → Action**;
- keep the **two data layers honest**: (a) externally-verifiable market signals = real, cited (`Source Tier` + URL + `Last Verified`); (b) the **live-booking/property layer = a TEMPLATE**, populated only from a client's connected RMS/PMS — VALIDATE source before write;
- treat **"real-time" as a freshness cadence** (real-time-critical / daily / weekly / monthly / quarterly / annual) executed by **interactive Claude Code (with web) or a human** — cloud routines cannot browse;
- keep the **separation of duties**: Notion = system of record + human workspace · Notion Calendar = temporal view layer · Cloud Code = ingest/monitor/normalize/dedupe/classify/impact-score/sync · Sector = interpretation · other departments = consumers;
- **inspect existing DBs, schema, and the Notion connection and EXTEND** (evolve `collection://c14fedb3-…` in place); route downstream on the **event bus** (reuse `SECTOR_MAPPED`/`REGULATORY_CHANGE`/`CALENDAR_UPDATED`; add at most `DEMAND_SHIFT`/`COMPRESSION_EVENT`/`COMPETITOR_MOVE`).

You MUST NOT:
- build a separate calendar per signal type or per view, or a parallel Signal DB (duplication, §1/§4);
- **fabricate** a property's live numbers, an event date, or a forecast presented as fact;
- let a **Tier-4 / unverified / stale** signal emit a department signal or drive execution (extends §6);
- stand up paid live data integrations (SiteMinder/STR/IDeaS) without owner approval + credentials;
- put the refresher on a persistent scheduler or give it auto-write **without an `AUTOMATION_APPROVAL_MATRIX.md` row** — it stays **advisory/manual** until then (owner decision, 2026-08-11).

**Failure conditions:** unreachable/stale source → mark `Needs verification`, never guess; missing Geography/finding relation → REPORT the dependency; conflict with an Ops calendar or CRM entity → ESCALATE (§11). **Cross-refs:** `SECTOR_NOTION_SCHEMA.md` DB 7/11/12/13; `SECTOR_CALENDAR_REFRESH_SPEC.md`; the plan addendum "SCIC".

---

## 13. Sector OS Kernel doctrine *(added 2026-08-16)*

**Purpose:** operate the Sector Layer as **SectorOS** — the **first activated slice of IntOS** (`AEIT_07`), not a parallel intelligence stack. **Authority:** subordinate to §1–§12; authoritative for kernel/ontology/scoring work. **Inputs:** the 14 Sector DBs + `AEIT_06/07/08` + `arika-runtime`. **Outputs:** ranked, state-tracked sectors + contract-conformant intelligence objects that feed the downstream departments. Full design: `SECTOR_NOTION_SCHEMA.md` §0.1; plan addendum "ADDENDUM 2 — Sector OS Kernel".

### 13.1 The three separations (never collapse them)
- **Memory** = Notion + the `AEIT_06` canonical model. **Logic/reasoning** = `arika-runtime` agents. **Execution** = cloud routines / `RemoteTrigger` under the Approval Matrix. The **Control Tower** is a **read view** over memory (a Notion dashboard answering: what's changing · where money moves · who matters · problems · opportunities · competition · offers · acquisition · content · execution · results · learning) — **not** a new store.

### 13.2 The Sector Universe is multi-vertical
A **Sector = any market Arika sells into** (B2B SaaS is one branch; Hospitality, Healthcare, Real Estate, Franchise, … are peers). Verticals live in *Sectors Master*; industries/sub-industries in *Sub-Sectors*. Every sector carries a **`Lifecycle State`** (`Discovered → … → Dominance`, evidence-gated) and a **`Sector Priority Score`** (0–100, 8 dimensions, advisory) used to rank GTM focus. Promotion through the state machine REQUIRES the underlying rows to exist — **no self-promotion**.

### 13.3 The Intelligence-Object Contract (the rule that stops the warehouse)
Every intelligence record MUST answer eight questions — **what · source · when-observed · reliability · which sector · which decision it supports · which system consumes it · what action can result** — which **is** the `AEIT_06` `Knowledge Object` (`claim, entity_ref, confidence, trust, freshness, source_id, state`) expressed through the existing fields (`Source Tier`, `Confidence`, `Last Verified`, `Departments Affected`, `Recommended Action`, the relation to a finding).

**Decision-purpose gate (MUST):** populate a field **only** when it has a **named downstream decision or execution purpose**. A datapoint that no decision consumes is noise — do not collect it, do not store it. This supersedes "collect because we can."

### 13.4 Cloud Code construction mandate (MUST / MUST NOT)
When building or extending the Sector Layer, Cloud Code:

**MUST**
- **INSPECT** the existing 14 Sector DBs + `AEIT_06/07/08` + `arika-runtime` **and EXTEND** them; treat SectorOS as IntOS's first live slice.
- **CONFORM** every record to the Intelligence-Object Contract (§13.3) and the field-purpose discipline (`SECTOR_NOTION_SCHEMA.md` §0).
- **REFERENCE by ID** the stores other departments own — CRM/CPAROS (`Company/Lead/Person/Opportunity`, ClickUp), Marketing (`Competitor`/`Campaign`), Content (content intelligence), Ops (the 7 Cognitive Calendars), `AEIT_08` (sources).
- **PRESERVE the three separations** (§13.1); route downstream on the **event bus**, not a new router.
- keep the **two-data-layer honesty** (externally-verifiable = cited + `Source Tier`; live/enriched = template until sourced) and the **freshness cadence** definition of "real-time".

**MUST NOT**
- create a **parallel** store for anything already owned (CRM, IntOS, canonical model, Content, Marketing, Ops) — the ~20-DB "Sector OS" reconciles to **extend/reference + 4 net-new** (`SECTOR_NOTION_SCHEMA.md` §0.1);
- **fabricate** sector data, a decision-maker record, an event date, a number, or a forecast presented as fact;
- run an **unattended web-scraper / ingestion daemon** (cloud routines have **no web**) — collection is interactive/human or a gated runtime with an API key + `techstack-cost-guardian` + an Approval-Matrix row (`AEIT_07`/`AEIT_10`);
- let a **Tier-4/unverified/stale** object drive a downstream signal or execution (§6, §12.3).

### 13.5 The engines are the runtime, not new software
The 7 processing engines (Sensing → Intelligence → Decision → Orchestration → Execution → Feedback) **are** the existing constructs: SCIC + `sector-signal-refresher` (Sensing); Sector Intelligence + `sector-intelligence-mapper` (Intelligence); `sector-signal-scorer` + `sector-readiness-analyst` + the Sector Priority Score (Decision); the event bus §8 (Orchestration); `arika-runtime` triggers under the matrix (Execution); `runtime.jsonl` + §16 (Feedback). Build = **wire them**, not invent them.

---

## 14. Sector Commercial Activation & the per-sector Cross-Loop *(added 2026-08-19)*

**Purpose:** turn the loaded kernel + Industry Revenue Engine into a **live commercial operating loop**, one focus sector at a time — the layer that ends in outreach. **Authority:** subordinate to §1–§13; authoritative for activation/cross-loop/CRM-bridge work. Full design: plan "ADDENDUM 4". Owner-approved 2026-08-19; pilot sector = **Hospitality → Accommodation**.

### 14.1 Focus is data-derived, not owner-blocked
The **Sector Priority Score** *is* the focus decision. Promote the P1-scored sub-sectors to `Status = Target` **by the score** (advisory; owner may veto/add) — do **not** stall the downstream chain waiting on a fresh manual ruling the scoring already produced. September focus: **B2B SaaS · Hospitality→Accommodation · Professional Services→Legal & Accounting**. Depth-first discipline still holds: per-sector research spends only on `Target` sectors, never sprayed across all 321.

### 14.2 The per-sector Cross-Loop (author it per sector; each sector differs)
Every `Target` sector is taken through the **same seven links, different content** — the Cognition Runtime Loop (§6) ending in a CRM packet:
`① WHEN (Sector Signals: seasonality + buying window) → ② WHY (Sector Intelligence: pain/economics/tool-chaos) → ③ HOW (Sector Linguistics) → ④ WHO (Audience Roles + Decision-Maker titles) → ⑤ WHICH (Industry Offer Matrix ladder + offer-match/GAP) → ⑥ WHAT (Outreach Angle + audit/proposal logic) → ⑦ WHERE (CRM packet: Ideal-Target-Profile + offer_id + sector/sub_sector/icp_tier → Lead when real contacts scraped) → outcome → Sector Memory → back to ②.`
**MUST** author each link's content *per sector* — Hospitality is season-led (buyer GM/Revenue Manager), Professional Services tax-season-led (buyer Managing Partner), B2B SaaS trigger-led (buyer CRO/founder). The same loop, re-voiced. This is why the score routes attention and why the loop is not one generic pipeline.

### 14.3 Sector emits the packet; Sales/Content own the script (never collapse this)
Sector produces the **intelligence packet** — timing + pain + language + who + offer-match + outreach *angle*. It does **NOT** write the final email/proposal/script — that is **Sales (05)** enablement + **Content (04)**. Route the packet to them; do not re-own their artifact. (Same anti-duplication law as §4/§13.4.)

### 14.4 The CRM is already live — bridge onto it, never rebuild it
The CRM exists: **ClickUp** — Lead / Opportunity / Client / Engagement-Project / Partner Lists with real fields, FK relations, and status pipelines (`CRM_SCHEMA.md`). Sector **references it by ID** and maps onto it: `sector` / `sub_sector` / `icp_tier` tags + matched `offer_id` + a per-sector **Ideal Target Profile**. **MUST NOT** create a parallel contact/company store. Real `Lead` rows (contact_name/email/company), ICP scores, and Signal scores are **gated** — they require scraped real people/companies (§14.5). Until then the bridge is a **mapping + template**, never populated with a fabricated contact.

### 14.5 Data-source posture (register now; connect gated)
- The **market/web-intelligence research** (seasons, calendars, regulation, linguistics, decision-maker *titles*, tool-stack, company-website reads) is **public, non-PII** and done **now** by the interactive session's built-in web tools — the honest "profound web researcher" for the pilot. Cloud routines still have **no web** (§13.4); no unattended daemon.
- The **people/contact-data layer** (real names/emails/dials → CRM) is **paid, PII, Legal-gated** and **DEFERRED** — connect a people-data MCP (Apollo/Clay/Cognism) only after a **Legal posture note + cost governance + an Approval-Matrix row** (`AEIT_08` §5; `AEIT_07`/`AEIT_10`).
- **Every registered source names where its data feeds** (`AEIT_08` `consumers`) — the §13.3 decision-purpose gate applied to sources: no source without a destination DB.

---

## Appendix — Builder-role self-audit (Draft 10 QA gate)

This contract was checked against the 7 builder roles:
- **Builder** — unit of value = one traceable sector-intelligence finding; flow of value = §1 chain. ✅
- **Architect** — layers (§5), data flow (`SECTOR_NOTION_SCHEMA.md`), control layer (§2 hierarchy), failure points (§7). ✅
- **Operator** — what to monitor = freshness + event wiring (§6, §8); bottleneck named (the `SECTOR_READINESS_SET`/`PROSPECT_IDENTIFIED` gap). ✅
- **Executor** — smallest next action = Phase 1/2 docs done; Phase 6 first run defined. ✅
- **Maintainer** — decay rule (§6), review cadence, "what breaks if untouched 30 days" = stale scores (handled). ✅
- **Systems Engineer** — no redundancy (§4 anti-duplication), reuse of runtime + AEIT_06, feedback loop (§9). ✅
- **Strategist** — leverage = Sector feeds every revenue dept; what NOT to build = the 7 other-dept-owned stores (§4). ✅
