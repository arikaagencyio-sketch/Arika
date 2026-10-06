# 04 — Entity and Data Model

**Protocol §20:** a complete entity map. **§21:** for every important object, *"where is the single source of truth?"* — and flag competing ones.

The canonical model is `AEIT_06_CANONICAL_MODEL_AND_KNOWLEDGE_GRAPH.md` (v0.3, a **blueprint**: *"specifies the model; does not populate instances"*). Its implemented slices are `CRM_SCHEMA.md` (ClickUp), `SECTOR_NOTION_SCHEMA.md` (16 Notion databases), `CONTENT_INTELLIGENCE_SCHEMA.md` (8 Notion databases) and the `finos-plugin` SQL schema. Tags below: **[CRM]** live in ClickUp · **[SEC]** live Sector Notion DB · **[CNT]** live Content Notion DB · **[AEIT]** blueprint only · **[DOC]** markdown document only · **[—]** absent.

---

## 1. Entity map (protocol §20)

| # | Entity | Exists? | Where (tag) | Source of truth | Connects to | Duplicated / ambiguous? | Missing | Class |
|---|---|---|---|---|---|---|---|---|
| 1 | **Agency** | ✅ | Company profile [DOC]; `finos.entities` (legal entity); BOIS workspace `clients/arika-agency` | `ARIKA_GROWTH_COMPANY_PROFILE.md` + BRS/KRA records (external) | Every department | Identity restated in `GLOBAL_OS.md` §1 and Constitution §2 (contact line stale) | — | EXISTING |
| 2 | **Client** | ✅ role | `Client` list [CRM]; `AEIT_06` Client role; **`finos.clients` table**; BOIS client workspaces | ClickUp `Client` (per `CRM_SCHEMA.md`) | Opportunity, Project, Invoice, Contract | **Yes** — `finos.clients` has no foreign key to the CRM; BOIS writes client workspaces inside the repo (A001 AG-15) | Live rows (0 clients) | EXISTING · `HV-32` |
| 3 | **Prospect** | ◐ role | `Company.roles[]` [CRM, not live]; Sector DB 4/5 [SEC, empty by design]; prospecting queue (outside Git) | **Today: the outside-Git queue**; designed: CRM Company | Lead, ICP classification | Three places, one designed SoT | CRM registration (`HV-05`) | EXTEND |
| 4 | **Contact** | ◐ | `Lead.contact_name/contact_email` text fields [CRM]; `AEIT_06` `Person` (`PER-*`) [AEIT]; DB 10 `CRM Person` text ID — **empty on all 57 rows**, gated | none built | Company, Lead | — | `Person` object; consent basis per contact | EXTEND |
| 5 | **Decision maker** | ◐ | DB 10 titles [SEC]; `Person.decision_authority / decision_scope` [AEIT]; Draft 41 §2.2 buyer table [DOC] | DB 10 (titles only) | DB 9 roles, DB 6 language | — | Person-level authority record | EXTEND |
| 6 | **Market** | ✅ | DB 1 Sectors · DB 2 Sub-Sectors · DB 12 State · DB 13 Forecast [SEC]; DB 15 *origin market* [SEC] | DB 1/2 | Everything Sector | **"Market" means a sector, a route origin, and a place** | Glossary entry | EXISTING |
| 7 | **Vertical** | ✅ | DB 1 (25 verticals, scored) [SEC] | DB 1 | DB 2, plugins | — | — | EXISTING |
| 8 | **Property** | ◐ | CRM `Company` `entity_level = property/branch` [CRM, not live]; DB 11 `Property (template level)` [SEC]; plugin P2 archetype | **Undecided** — A001 AG-10 / T1-1: *"property is a Company, a Geography place, or both"* | Group, outlets, destination | Two candidate homes | The decision; live rows | EXTEND · decision `HD-11` |
| 9 | **Destination** | ✅ | DB 16 Destination Profile (3 rows) [SEC]; DB 11 place | DB 16 | DB 7, 9, 15, Content DB 5 (relation unbuilt, 31l) | — | Mombasa profile; universality open (31b) | EXISTING |
| 10 | **Audience** | ◐ | DB 9 roles (Plane A) [SEC]; **Content DB 6 `Audience Role` select = CEO · CMO · Sales Leader · COO · Investor · Founder** [CNT]; DB 15 text; DB 16 relation → DB 9 | DB 9 (Plane A) | Content, DB 16 | **Three audience vocabularies**; Content's is SaaS-executive-only (`HV-43`); DB 16 points Plane B at Plane A rows (`HV-17`) | A Plane B segment model | REFACTOR |
| 11 | **Segment** | ◐ | H-bands (hotel size, Decision 71); Client Success 5-type post-sale segmentation; Marketing template client tiers | per context | — | Different meanings, no conflict | **Guest segments** | EXTEND (P3) |
| 12 | **Experience** | ❌ in the hospitality sense | `AEIT_06` `Experience` = an EE interactive build [AEIT] | — | — | **Name collision** (`HV-39`) | A guest-offering concept | NEW (other name) |
| 13 | **Occasion** | ◐ | DB 7 signal types; P5 themes | DB 7 | Resolution Engine | — | Personal/corporate occasions | EXTEND (P3) |
| 14 | **Season** | ✅ | DB 7 `Seasonality` signals; plugin P13 | DB 7 | Activation dates | — | — | EXISTING (by design not an entity) |
| 15 | **Calendar** | ✅ | `AEIT_06` `Calendar` = the 7 Cognitive Calendars (Operations) [AEIT]; DB 7 Sector Signals [SEC] (named distinctly on purpose); Content DB 7 `Target Publish Date` view [CNT]; Google → Notion Calendar | per layer (file 06) | — | `AEIT_08` §4 calls its refresh rhythm an "8th" (`HV-23`) | — | EXISTING |
| 16 | **Revenue centre** | ❌ | CRM outlet levels only | — | — | — | Vocabulary + measure | NEW/EXTEND (`HV-12`) |
| 17 | **Offer** | ✅ | Offer Engineering Registry [DOC] (canonical); Content DB 8 thin mirror [CNT]; Sector DB 8 Industry Offer Matrix (routing) [SEC]; `Opportunity.offer_id` [CRM]; `finos.profitability_metrics.service_id` | `OFFER_OS.md` §3 | Opportunity, Campaign, Brief | By design: mirror + routing. **`offer_id`'s production format is still undefined** (`CRM_SCHEMA.md` 2026-09-29 entry) | ID format | EXISTING · minor |
| 18 | **Proposition** | ◐ | Content DB 2 Narrative Positions [CNT] (`[CANDIDATE]` entity); offer positioning | DB 2 (agency's) | Campaign, Content | — | A client's propositions (outside repo) | EXISTING |
| 19 | **Campaign** | ✅ | Content DB 4 [CNT] — owner Content (ratified 2026-08-16) | DB 4 | Offer, Platform, Narrative, Brief | — | **Status field; client reference** (`HV-08`, `HV-11`) | EXTEND |
| 20 | **Strategy** | ◐ | Documents (Vision, Doctrine, OEOS phases, `AEIT_10`) [DOC] | per document | — | — | Per-client strategy record | EXISTING (doc) |
| 21 | **Brief** | ✅ | Content DB 7 Briefs v2 [CNT]; **old brief DB superseded but not deleted** | DB 7 v2 | Opportunity (required), Campaign, Design | Old DB still exists pending routine re-point | Client reference | EXTEND |
| 22 | **Asset** | ✅ | Design asset library; Canva; `AEIT_06` `Creative Asset` [AEIT] | Design (19) | Brief, Campaign | Word also used for physical facilities | Approval state; client tier | EXTEND |
| 23 | **Channel** | ◐ | Content DB 1 Platform Registry [CNT] + PIL [DOC]; Marketing §10; Presence layers; `Lead.source` enum; booking channels (MD1) | PIL (platform behaviour) | Translation, Distribution | **"Channel" = social platform · acquisition source · booking channel** | Hospitality platforms (`HV-19`) | EXTEND |
| 24 | **Lead** | ✅ | `Lead` list [CRM] — 6 custom fields + 4 Sector bridge fields (verified 2026-09-29) | ClickUp | Company, Opportunity | — | Real rows | EXISTING |
| 25 | **Opportunity** | ✅ | CRM deal [CRM]; Content DB 5 content opportunity [CNT]; Sector DB 8 market opportunity [SEC] | each, by owner | — | **Deliberately three concepts, three owners** (`CONTENT_INTELLIGENCE_SCHEMA.md` DB 5 note) | — | EXISTING |
| 26 | **Sales stage** | ✅ | Lead/Opportunity statuses [CRM]; `AEIT_05` SM3; `pilot_state`; prospecting `touch_state` | ClickUp statuses | — | Several state machines, consistent | — | EXISTING |
| 27 | **Ticket** | ❌ | — | — | — | Work is held in ≥10 registers (file 13) | — | `HV-10` |
| 28 | **Task** | ◐ | `GO_LIVE_CHECKLIST.md` items; ClickUp tasks (Project list); agent `recommendedActions` | none canonical | — | — | Owner/priority/due/dependency standard | REFACTOR |
| 29 | **Approval** | ◐ | Authorisation registers (system actions); `finos.approvals` (money); runtime `awaiting_review`; content-gate layers | none canonical | — | — | Client/creative approval record (`HV-09`) | EXTEND |
| 30 | **Decision** | ✅ (prose) | Department §8 Decision Logs; `OWNER_INPUT_NEEDED.md`; AEIT decision logs | each Decision Log | — | ≥15 ID namespaces (`HV-10`); tracker lags (`HV-07`) | Enactment tracking (`HV-21`) | EXISTING |
| 31 | **Deliverable** | ◐ | Draft 41 D1–D7, MVP M1–M7 [DOC]; ClickUp `Project.scope_summary` | none | Project | — | Deliverable register (per engagement) | EXTEND |
| 32 | **Metric** | ✅ | `AGENCY_KPI_DICTIONARY.md`; department §7; plugin P14 | KPI dictionary | — | — | Thresholds; data | EXISTING |
| 33 | **KPI** | ✅ | as Metric | as Metric | — | Same concept | — | EXISTING |
| 34 | **Revenue** | ◐ | `Invoice / Revenue Event` [CRM — owned by Zoho Books]; finos journal; targets [DOC] | Zoho Books (plan lapsed at last check) | Client, Project | finos ledger parallel | Any real revenue | EXISTING |
| 35 | **Report** | ❌ | Draft 41 D7 design; internal readiness reports | — | — | — | Client reporting template + data | NEW (P2) |
| 36 | **Learning** | ◐ designed | `AEIT_07` §3.5 [AEIT]; memory files; changelog lessons; Sales `Learning_Loop_Log.md` (**empty template**) | none | — | — | Queryable learning register (`HV-33`) | OWNED-UNBUILT |
| 37 | **Experiment** | ◐ | Fixture authorisations (mechanism experiments); Marketing "experiment memory" (designed) | authorisation files | — | — | Market experiments | EXTEND (P2) |
| 38 | **Issue** | ◐ | Department §9 Risk/Incident logs (mostly empty); Automation incident record | each §9 | — | — | — | EXISTING |
| 39 | **Risk** | ✅ | Constitution risk *classes* (of actions); `AEIT_10` RK-1…8; delivery-risk register (agent) | context-dependent | — | **"Risk" = an action's class and a register entry** | — | EXISTING |
| 40 | **Dependency** | ◐ | `AEIT_02` matrix [DOC]; Campaign `Dependencies` text | `AEIT_02` | — | — | Machine-readable dependencies | EXISTING (doc) |

**Count (40 entities):** 18 exist (✅) · 18 exist partially (◐) · 4 absent (❌ — Experience-as-offering, Revenue centre, Ticket, Report) · 3 ambiguous by name (Market, Channel, Risk). Within the partial "Segment" row, **guest segments specifically are absent**. **Every absence except Ticket and Report is on Plane B.**

## 2. Relationships as they exist today

```
Company ─parent_of/contains_unit─► Company            [CRM, designed 2026-10-02; not live]
Company ─has role─► Prospect | Client | Partner | Competitor
Lead ─► Opportunity ─► Client ─► Project ─► Invoice     [CRM, live lists, 0 real rows]
Partner ─sources─► Opportunity                           [CRM]
Pilot Engagement ─tests offer with─► Company + Offer     [CRM, designed]
Sub-Sector ─► Signals ─► Geography ─► Routes ─► Destination   [SEC, live]
Destination ─audiences─► Audience Roles (Plane A rows)   [SEC — HV-17]
Opportunity(content) ─► Translation ─► Brief ─► (Design)  [CNT, live]
Campaign ─► Offer · Platform · Narrative                 [CNT]
Lead.source_campaign  = free text  ── no FK to Campaign Code   [HV-18]
finos.clients         = no FK to CRM Client                    [HV-32]
Campaign / Brief      = no Company/Client reference            [HV-11]
```

**The edges that matter for the protocol's loop and do not exist:** `Campaign → Lead` (keyed), `Lead/Client → Revenue` by campaign, `Client → Campaign/Brief/Asset`, `Booking → anything`, `Outcome → Learning → Signal/Finding`.

## 3. Sources of truth (protocol §21)

| Object | Single source of truth today | Competing / shadow sources | Verdict |
|---|---|---|---|
| **Client information** | ClickUp `Client` (0 rows) | `finos.clients`; BOIS client workspaces (inside the repo); intake answers in the client folder; identity maps (below) | ⚠️ **competing** — `HV-32`, `HV-44` |
| **Real identity of prospects / pilot** | *none single* | `C:\Users\USER\.codex\visualizations\…\identities` (prospecting run, `PROSPECTING_CYCLE.md`); `C:\Users\USER\Arika_Pilots\PILOT-H-001` (RD2); Drive `ARIKA_CLIENT_IDENTITIES` (tracker 2026-09-21 header; memory) | 🔴 **split across three locations, one of them a tool's scratch folder** — `HV-44` |
| **Strategy** | Per-offer OEOS documents | — | ✅ single for offers; none for clients |
| **Campaign status** | **none** — DB 4 has no status field | — | ❌ `HV-08` |
| **Calendar** | DB 7 (market); the 7 Cognitive Calendars are reasoned by an agent, not stored | Content `Target Publish Date`; Google/Notion Calendar (view) | ✅ by design (views over one store) |
| **Prospect** | outside-Git queue (2026-10-03) | Sector DB 4/5 (empty); CRM (not written) | ⚠️ transitional |
| **Contact** | none (gated) | `Lead` text fields | ❌ intentionally gated |
| **Decision maker** | DB 10 (titles) | Draft 41 buyer table (consistent) | ✅ for titles |
| **Revenue target** | `AGENCY_REVENUE_TARGETS.md` | Content DB 4 `Revenue Target` per campaign; daily vs monthly figures disagree by ~23–24 % (`OPERATIONS_OS.md` §7) | ⚠️ known inconsistency |
| **Campaign objective** | Content DB 4 (six objective fields) | — | ✅ |
| **Approved messaging** | Content DB 2 Narrative Positions (agency); plugin P10 / DB 6 use-avoid (sector); company profile §9–§15 (voice, claims) | Layered by altitude — consistent | ✅ for agency messaging · ❌ for a client's approved messaging |
| **Approved assets** | Design asset library / Canva `Brand System` | — | ◐ no approval state on an asset |
| **Tickets** | none | ≥10 registers | ❌ `HV-10` |
| **Approvals** | none canonical | 3 authorisation registers; `finos.approvals`; runtime gate; Decision Logs | ❌ `HV-09` |
| **Performance data** | none | — | ❌ `HV-18` |
| **Sector truth (which sectors Arika serves)** | `ARIKA_GROWTH_COMPANY_PROFILE.md` §8 (2026-10-06) | `GLOBAL_OS.md:24`, `SECTOR_OS.md` §1, website, LinkedIn files, claims policy | 🔴 **contradictory** — `HV-02` |
| **Organisation level vocabulary** | `CRM_SCHEMA.md` `entity_level` | `prospecting_cycle.py:12` `LEVELS`; plugin; intake overlay | ⚠️ **drifting** — `HV-06` |
| **Decision status** | each department's §8 Decision Log | `OWNER_INPUT_NEEDED.md` (lags); worksheet (frozen) | ⚠️ `HV-07` |

## 4. Proposed minimal extension — for decision, not applied

Following `AEIT_00` §5 (*canonical fit → ownership → contract → dependencies → governance → reality → logged*), the smallest model that would let Hospitality's Plane B exist **without a new store**:

| Need | Smallest sufficient form | Where | Tier |
|---|---|---|---|
| Guest segments, occasions, relationship pathways, revenue centres | **Controlled vocabularies** authored into plugin **P3** (and P2 for revenue-centre/outlet archetypes) | `HOSPITALITY_PLUGIN.md` + sidecar | Tier 2 — plugin values only |
| Which plane an audience row describes | One `Plane` select on DB 9 (`Agency market` / `Client market`), **or** retarget DB 16 audiences to the P3 segment vocabulary | Sector DB 9 / DB 16 | **Tier 1 — needs ratification** (`HD-09`) |
| A client's offerings (packages, experiences, day passes…) | Intake rows answered in the client folder; **no canonical entity yet** | Intake overlay (new `H-` rows) | Tier 3 (client instance) |
| Client separation in Content/Design | A `Client Company ID` **text** field on Content DB 4 and DB 7 (cross-platform links are text IDs by design law 2); a `Clients/{ORG-ID}/` tier in Canva | Content, Design | Tier 1 field — ratification |
| Approval record per deliverable | Extend the existing authorisation-register shape, or four fields on ClickUp `Project` tasks (`approved_by`, `approved_at`, `version`, `evidence_ref`) | Governance / Operations | EXTEND (`HD-06`) |
| Campaign → lead → revenue keying | `Lead.source_campaign` constrained to a DB 4 `Campaign Code` | CRM field rule | EXTEND |

**Deliberately not proposed:** a Property store, an Experience store, an Occasion store, a Season store, an Audience-calendar store, a separate B2B2C CRM, or a ticketing platform. Each would duplicate an existing owner (file 15 §6).
