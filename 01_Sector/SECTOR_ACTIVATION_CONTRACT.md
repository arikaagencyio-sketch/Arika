# Sector Activation Contract (SectorOS)

**Department:** Sector (01) · **Status:** Active doctrine. **Audience:** Claude Code (in VS Code) and any agent operating the Sector Layer.
**Role of this file:** the "trigger paragraph" — the operating contract Claude Code reads *before* creating, modifying, querying, or executing anything in the Sector Layer. It makes the runtime read the whole repository, the whole sector, and the cross-department relations before acting. Built from the SectorOS architecture in `Sector Layer Architecture. Draft 13.md`, grounded in the real repository.

> Precedence: this contract is **subordinate** to `00_Agency_Governance/AGENCY_OPERATING_CONSTITUTION.md` and `GLOBAL_OS.md`, and **authoritative** for Sector work below them. Read `SECTOR_OS.md` (what), `SECTOR_NOTION_SCHEMA.md` (data model), and [`SECTOR_OS_ARCHITECTURE.md`](SECTOR_OS_ARCHITECTURE.md) (core-vs-plugin boundary + the Resolution Engine, §16) alongside it.

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
1. Read the Sector Layer: `SECTOR_OS.md`, this contract, `SECTOR_NOTION_SCHEMA.md`, [`SECTOR_WRITE_CONTRACT.md`](SECTOR_WRITE_CONTRACT.md) (before any write), the **5** agents (`.claude/agents/sector-*.md`), and the relevant raw drafts.
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
Homes: **Notion** (Identity, Linguistic, Calendar, Intelligence, Opportunity, Evolution, Audience, ICP, Signal, Decision-Makers — see `SECTOR_NOTION_SCHEMA.md`); **repo doctrine** (Journey, Governance); **runtime** (Runtime layer = 5 agents + event bus); **`01_Sector/_memory/runtime.jsonl`** (Memory).
> **Layer 3 (Calendar) is operated as the Sector Signal / Commercial Intelligence Calendar (SCIC) — see §12.** Layer 12 (Evolution) is home to **Sector Forecast** and Layer 6 synthesis to **Sector State** (`SECTOR_NOTION_SCHEMA.md` DB 12/13).

## 6. The Sector Cognition Runtime Loop (Draft 13, 14 steps)

Any non-trivial Sector task follows: **1** identify sector → **2** read this contract → **3** map linguistics → **4** map infrastructure → **5** analyze calendars → **6** analyze journeys → **7** identify governance/power → **8** model runtime → **9** identify cross-dept dependencies → **10** detect opportunities → **11** detect risks → **12** update memory (`runtime.jsonl`) → **13** generate intelligence → **14** report state. Never skip a step silently.

**Freshness rule:** every intelligence/score record carries `source`, `confidence`, `freshness`, `last update`, `next review`. Medium-band prospect scores are **re-scored every 30 days** ("signals decay", Draft 15). Stale intelligence MUST NOT drive downstream execution without revalidation.

## 7. Governance & validation (before activating anything)

Before activating any workflow, VALIDATE that: the schema exists · required DBs + relations exist · a trigger exists · the owning agent/skill exists · the output destination exists · an audit/memory path exists · a feedback path exists. If any is missing, **report it**.

Automation gate: Sector's **5** agents are advisory — **four Class 1 (internal intelligence) and `sector-signal-refresher` Class 2 with `requires_human_approval: true`** — so no approval-matrix row is required while they only recommend. **The same exemption covers the twelve Sector skills** ([`SECTOR_SKILL_MATRIX.md`](SECTOR_SKILL_MATRIX.md)): they are manual-apply by construction, since `arika-runtime` has no Notion client and cannot invoke a skill, so the apply step is a human-invoked Claude Code session (`04_Content/CONTENT_INTELLIGENCE_SCHEMA.md` §7 — "the same doctrine Sector operates under"). A row in `00_Agency_Governance/AUTOMATION_APPROVAL_MATRIX.md` (columns: Trigger · Action · Risk Class · Rollback · Fallback · Log destination · Human gate · Last-verified · Detection) becomes **required** the moment any agent acts externally or is put on a persistent scheduler. Class ≥ 3 requires human sign-off.

## 8. Trigger & routing requirement (reuse the runtime)

Every workflow defines: `TRIGGER → CONTEXT → RETRIEVAL → ANALYSIS → DECISION → MEMORY WRITE → DOWNSTREAM ROUTING → MEASUREMENT → LEARNING`. Triggers use the runtime's five types only (`manual · schedule · event · webhook · join`, `arika-runtime/src/triggers/*`). Routing is via **emitted events on the bus**, not a new router. Sector's canonical events:

| Emit | Meaning | Intended subscriber (target state) |
|---|---|---|
| `PROSPECT_SCORED` | 90-pt score set | Sales (05) qualification + Marketing (03) demand |
| `ICP_CLASSIFIED` | tier set | Sales (05) qualification + Marketing (03) intelligence |
| `SECTOR_MAPPED` | sector map produced | Offer (02) + Marketing (03) + Content (04) |
| `SECTOR_READINESS_SET` | readiness reclassified | Marketing (03) demand generation |
| `CALENDAR_UPDATED` | a signal changed materially | `sector-intelligence-mapper` (01) — **wired, intra-department only.** ⚠️ `content-intelligence-hub` (04) was listed here and **does not subscribe** — see the correction below |
| `REGULATORY_CHANGE` | a regulatory signal moved | `sector-readiness-analyst` (01) — **wired, intra-department only.** ⚠️ `sales-lead-qualification` (05) was listed here and **does not subscribe** — see the correction below |
| `DEMAND_SHIFT` | demand-signal materially changed | Marketing (03) demand + Ops (08) revenue — ⏳ *emitted, not yet subscribed* |
| `COMPRESSION_EVENT` | a compression/event window opens | Sales (05) meetings + Marketing (03) campaign timing — ⏳ *emitted, not yet subscribed* |
| `COMPETITOR_MOVE` | competitor signal detected | Marketing (03) market-intelligence + Sales (05) — ⏳ *emitted, not yet subscribed* |

> ✅ Wired 2026-08-10: the four Sector emits reach live subscribers — `PROSPECT_SCORED`/`ICP_CLASSIFIED` → `sales-lead-qualification` (05); `SECTOR_MAPPED` → `offer-orchestrator` (02); `SECTOR_READINESS_SET` → `marketing-demand-generation` (03) — added **additively** (pre-existing consumers in Ops/ClientPartner/Content preserved; events are multicast). `PROSPECT_IDENTIFIED` is an **external** entry trigger by design (webhook/manual), so it has no internal emitter. `handoff_to` remains documentation-only and is not executed.
> 🔴 **RETIRED FROM THE RUNTIME CONTRACT 2026-08-28 (owner decision 31d), ARCHIVED NOT DELETED.** `DEMAND_SHIFT`, `COMPRESSION_EVENT` and `COMPETITOR_MOVE` have **zero subscribers** across all 115 agent files, and wiring one would not have helped: **`executor.ts` never publishes**, so the edge would have been a second false claim layered on the first. Per [`AEIT_11`](../00_Agency_Governance/enterprise_architecture/AEIT_11_RUNTIME_TRUTH_STANDARD.md) **R5**, their design is preserved in [`contracts/event-catalog.json`](contracts/event-catalog.json) at `reality_state: DESIGNED` and only the operational claim is struck. The ⏳ *“emitted, not yet subscribed”* markers below are the **archived intent**, retained deliberately.
>
> ⏳ Added 2026-08-15 (SCIC Phase D): `sector-signal-refresher` emits the three new SCIC signal events above. `CALENDAR_UPDATED`/`REGULATORY_CHANGE` were recorded as reusing the already-wired subscribers — **this was wrong, see the correction below**; `DEMAND_SHIFT`/`COMPRESSION_EVENT`/`COMPETITOR_MOVE` are **emitted-but-not-yet-subscribed** — their target-department handlers (03/05/08) MUST be registered before these carry weight (anti-dead-event rule, Part 2). Because the refresher is advisory/manual (nothing fires unattended), there is **no live dead event** today; the wiring is a documented extension point, activated when a downstream department adopts it. Verified: `arika list` loads all Sector agents, 0 skipped.
> 🔴 **CORRECTION 2026-08-24 — two dead *edges*, found by regenerating the subscriber map from ground truth.** The 2026-08-15 entry above assumed `CALENDAR_UPDATED` and `REGULATORY_CHANGE` could "reuse the already-wired subscribers." They cannot: the wiring belonged to *different* events. Grepping every `on:` trigger across all 115 agent files shows **`content-intelligence-hub` subscribes to `SECTOR_MAPPED`, `MARKET_SIGNAL_MAPPED`, `OFFER_ENGINEERED`, `ADVOCACY_CAPTURED` and `BUYER_PSYCHOLOGY_MAPPED` — not `CALENDAR_UPDATED`**, and **`sales-lead-qualification` subscribes to `LEAD_CREATED`, `ICP_CLASSIFIED` and `PROSPECT_SCORED` — not `REGULATORY_CHANGE`**. Both events therefore reach only Sector's own agents and **never leave the department**. This makes `SECTOR_OS_ARCHITECTURE.md` §1.1's *"Six reach a live subscriber"* true at the event level but misleading at the edge level. Neither edge appeared in any gap register — the same *"a changelog entry is a record of intent, not proof of state"* failure this contract already names (§1.3 finding 6), which nothing caught because nothing regenerated the list. Ground truth now lives in [`SECTOR_EVENT_CATALOG.md`](SECTOR_EVENT_CATALOG.md) and [`contracts/event-catalog.json`](contracts/event-catalog.json), regenerated by grep rather than copied. **Wiring a real subscriber is a Content (04) / Sales (05) change and is not made here.** The anti-dead-event rule now covers dead edges too: S10 re-reads the catalog before every handoff.

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

## 15. Live Sector Event Intelligence (LSEI) doctrine *(added 2026-08-19)*

**Purpose:** operate the sector calendar as a **live, sourced, directional timing backbone** — not a table of dates. **Authority:** subordinate to §1–§14; authoritative for source-registry, market-route, timing-rule, and calendar-sync work. Extends §12 (SCIC); does not replace it. **Inputs:** registered external publishers (DB 14) → Sector Signals (DB 7) × Geography (DB 11) × Market Routes (DB 15). **Outputs:** route-scoped signals with derived activation clocks → interpreted findings → department signals → the 7 Cognitive Calendars. **Full design:** [`CALENDAR_INTELLIGENCE.md`](CALENDAR_INTELLIGENCE.md).

**The governing sentence:** *the agency calendar is not the source of truth — it is a rendered view of live external reality, computed per market route.*

You MUST:
- **trace every dated signal to a registered `Signal Sources` (DB 14) row.** Free-text provenance is no longer sufficient. A signal **inherits** its source's `Authority Level` and may never out-rank its publisher;
- respect the **source hierarchy** (`CALENDAR_INTELLIGENCE.md` §2): a **T4 source may discover but may not confirm**; where an aggregator and the organizer disagree, **the organizer wins** and the aggregator claim is marked `Superseded/Delayed`;
- **register before trusting** — a source enters `State = active` only after a **live verification call proves it answers** (`AEIT_08` §5). Candidates stay `candidate`. Every source names a **`consumers`** destination DB (the §13.3 decision-purpose gate);
- **compute commercial meaning per Market Route, not per event.** Set `Signal Role` (`Destination-side` / `Origin-side` / `Both`) on every signal, and relate it to the routes it actually affects. `Kenya → Dubai` and `Dubai → Kenya` are different rows with different clocks;
- **derive activation dates only from the §5 Timing Rule table** in `CALENDAR_INTELLIGENCE.md`, and label them as **derived planning offsets** — never as facts obtained from the source (extends §12);
- **record a change as a version, never an overwrite.** Write `Previous Signal Date` + `Change Reason`, append a dated line to the page body naming the confirming source and tier, set `Change Status`, and emit the matching event;
- **name what a change invalidates.** When a signal's date moves, the change MUST name the downstream work it breaks — affected **Market Routes**, **Content Opportunities**, **campaign windows**, derived **activation dates**, and any **agency-calendar** entry computed from it. *This is the difference between a database row edit and operating-system behaviour;*
- keep the **calendar-sync separation**: subscribed external calendars (Google Calendar ICS → Notion Calendar) are an **input and a cross-check**; only a signal that has been through the DB 7 lifecycle is actionable intelligence.

You MUST NOT:
- build a calendar per layer, per view, per sector, or per direction — the ~17 proposed layers are **`Signal Type` values and filtered views** on the one canonical DB (§12);
- let a **T4 / unverified / stale** signal drive a route, a clock, a department signal, or an agency-calendar entry (extends §6, §12);
- present a **derived timing offset** as an external fact, or a **compression read** as a forecast of occupancy or price;
- **estimate** a route's booking lead time, air connectivity, visa friction, or currency context to fill a blank — 🟢 web-cited or empty (a blank is a research task, not a defect);
- fabricate a destination's demand numbers or a property's live figures — the property layer stays ⚫ **template** until a client connects a real RMS/PMS;
- add timing-rule rows or register sources for a sector whose cross-loop has not been authored — **depth-first on `Target` sectors** (§14.1);
- create a source, route, or calendar **without a named downstream consumer** (§13.3).

**Failure conditions:** unreachable/moved publisher → mark the source `Needs verification` and the signal unchanged, never guess a new date; a signal whose source row does not exist → REPORT the dependency, do not back-fill free text; a route field with no citation → leave blank; conflict with an Operations `Calendar` or a CRM entity → ESCALATE (§11). A change that flips a sub-sector's readiness or invalidates live client work ESCALATES to the owner.

**Cross-refs:** `CALENDAR_INTELLIGENCE.md` (full design) · `SECTOR_NOTION_SCHEMA.md` DB 7 / 11 / **14** / **15** · `SECTOR_CALENDAR_REFRESH_SPEC.md` (cadence + escalation ladder) · `AEIT_08` §1/§3.2/§4/§5 · `13_Tech_Stack/TECHSTACK_OS.md` §3 (Google Calendar + Notion Calendar) · `08_Operations/OPERATIONS_OS.md` (the market-clock bridge — an **input** to the 7 Cognitive Calendars, never an 8th).

---

## 16. Universal Core / Sector Plugin separation *(added 2026-08-20)*

**Purpose:** keep the Sector Layer a **sector-agnostic operating system** whose first implementation happens to be Hospitality — not a hospitality system with other sectors bolted on. **Authority:** subordinate to §1–§15; authoritative for core-vs-plugin classification and for calendar resolution. **Inputs:** the **16 live Sector DBs** (DB 14/15/16 built 2026-08-20, all three **empty**) + a sector's plugin pack. **Outputs:** resolved, layered calendars per sector × geography × property archetype × client. **Full design:** [`SECTOR_OS_ARCHITECTURE.md`](SECTOR_OS_ARCHITECTURE.md). **Sector #001 = Hospitality** ([`sector_plugins/hospitality/HOSPITALITY_PLUGIN.md`](sector_plugins/hospitality/HOSPITALITY_PLUGIN.md)); activation of #002 onward follows [`SECTOR_ACTIVATION_PROTOCOL.md`](SECTOR_ACTIVATION_PROTOCOL.md).

**The governing sentence:** *the calendar is not a store of content — it is a resolved view of live external reality, computed per sector, per geography, per property archetype, per client.*

You MUST:
- classify every element as **universal** (core, never re-authored), **plugin** (re-authored per sector), or **configurable rule** (core field, plugin-supplied value) — and **state the class** when adding or moving one;
- author a sector as a **plugin pack** filling the **14-slot Plugin Interface** (`SECTOR_OS_ARCHITECTURE.md` §3), one directory under `01_Sector/sector_plugins/{sector}/`; leave an unresearched slot **empty**, never plausible;
- **produce calendars by resolution, not by authoring rows** — `Sector → Regional → Property-Type` are *views* over the one canonical DB 7; the **Client Calendar is step 5 of the resolution algorithm**, not a store; the **Execution Calendar is Content (04)'s Briefs**. A 365-day calendar is an **output** of `resolve(...)`, recomputed on change;
- run the resolution **gates** — `Timeliness · Destination Fit · Client Fit` — as pass/fail *conditions of applicability* **upstream** of Content DB 5's scoring. They are **not** score dimensions: `content-opportunity-mapper`'s published `output_schema` and DB 5's tier formula are a live contract and are not rewritten to accommodate them;
- add **Destination Profile** (DB 16) and **Market Routes** (DB 15) to the set a material change must **name as invalidated** (extends §15) — alongside Content Opportunities, campaign windows, derived activation dates and agency-calendar entries;
- **reference by ID** the Entity Registry that already exists: properties, groups, parents and subsidiaries are CRM `Company` rows in **ClickUp** (`AEIT_06`: *roles, not types*). A Sector-side property store is the parallel-company-store ban of §14.4.

You MUST NOT:
- let a plugin **create a database, field, agent, or event** — if a sector appears to need one, that is a Tier-1 architecture change requiring owner ratification + an `AEIT_06` entry: **ESCALATE**, do not edit the plugin;
- let a **universal file carry a sector's rule values** — timing offsets, source lists, demand vocabularies, property typologies and destination themes are plugin content wherever they currently sit;
- build a **calendar per layer** (sector / regional / property-type / client) — restates and extends §15;
- **replicate a validated sector's database** into a new sector: extract the pattern, author the slots;
- promote a sector through the **Lifecycle State machine** without the underlying rows (no self-promotion, §13.2);
- treat a **derived resolution** as an external fact, or a destination's demand character as measured data when it is an owner hypothesis;
- fabricate a destination's demand numbers or a property's live figures — the property layer stays ⚫ **template** until a client connects a real RMS/PMS.

**Failure conditions:** a validation run returning **identical calendar shapes** across structurally different destinations → the destination/property-type layers are inert; **STOP** and fix the model before loading data. A slot filled with a plausible unsourced value → constitutional breach (`AGENCY_OPERATING_CONSTITUTION.md`), revert it to empty. Removing a sector's plugin breaking the core → the system is that sector's, not a Sector OS; **ESCALATE**.

**Cross-refs:** `SECTOR_OS_ARCHITECTURE.md` (full design) · `SECTOR_ACTIVATION_PROTOCOL.md` (gates + slot classification) · `SECTOR_NOTION_SCHEMA.md` §0.4 + DB 16 · `CALENDAR_INTELLIGENCE.md` §5.2/§12 (rule schemas; values live in the plugin) · `04_Content/CONTENT_INTELLIGENCE_SCHEMA.md` (the three gates as upstream filters) · `08_Operations/OPERATIONS_OS.md` §12a (resolver output is an input to the 7 Calendars, never an 8th).

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
