# Sector — Notion Data Model (Schema Spec)

**Department:** Sector (01) · **Status:** **Built & live** in Notion (2026-08-11) — all 10 databases exist with two-way relations (IDs in §6); loaded with the reference xlsx taxonomy. **Operating mode is manual-apply** (see §7): the DBs are live, but nothing writes to them unattended.
**Purpose:** The build specification for the Sector Layer's operational control plane in Notion — the ~10 Sector-owned databases, their fields, relations, and the purpose each field serves. This is the "databases in Notion, active, with the right relations, every field with a purpose" deliverable.

> Read `SECTOR_OS.md` first, then `SECTOR_ACTIVATION_CONTRACT.md`. This file is the *what to build*; the contract is the *how to operate it*.

---

## 0. Design laws (read before building)

1. **Conform to the canonical model, don't reinvent it.** Every entity here maps to `00_Agency_Governance/enterprise_architecture/AEIT_06_CANONICAL_MODEL_AND_KNOWLEDGE_GRAPH.md` — which already names `Sector/Sub-sector`, `ICP Classification`, and `Prospect Signal Score` as Sector-owned. Rule: *"departments consume canonical entities; they do not reinvent them."*
2. **Reference, never duplicate.** CRM (`Lead/Opportunity/Client/Project/Invoice/Partner`) is **live in ClickUp** (`00_Agency_Governance/CRM_SCHEMA.md`). Offer mapping → Offer (02); Competitor → Marketing (03); Content Intelligence → Content (04); agency operating calendars → Operations (08). Sector links to these **by ID reference** (cross-platform Notion↔ClickUp), it does not re-store them.
3. **Every field earns its place.** Each field is tagged with a **purpose**: `identity` · `retrieval` · `relation` · `governance` (confidence/source/freshness/status) · `execution`. A field with no purpose tag does not get built (Draft 7 discipline: "everything must be linked; if anything is not connected, it's noise").
4. **Notion API constraint:** the native `Status` property type cannot have its options set via the API. Use a **`Select`** for every lifecycle/status field (the same fix Content 04 applied — `04_Content/CONTENT_OS.md`).
5. **Data provenance:** rows are loaded from the real 13-sheet `Other Source Reference/Arika_B2B_SaaS_Intelligence_Database.xlsx`. This model **formalizes existing data**; it does not invent it. Pricing figures in the xlsx are hypotheses (see `SECTOR_OS.md` §1).

---

## 0.1 — Sector Universe & the anti-duplication map *(Kernel, 2026-08-16)*

**Sector Universe is now multi-vertical (owner decision 2026-08-16).** A **Sector = any market Arika sells into**, not only a SaaS category. **B2B SaaS becomes one branch** of the universe (its 22 sub-sectors / 52 rows intact); Hospitality, Healthcare (Multi-Location), Real Estate Brokerages, Franchise Systems, etc. are **real verticals** in *Sectors Master*. This supersedes the earlier "B2B SaaS is the only sector" / "Hospitality is illustrative only" framing — the data is kept, the universe is widened. `Sectors Master` already anticipated this (it holds B2B SaaS **plus** 3 non-SaaS verticals; `Category` includes "Multi-Location Vertical").

> **Migration note (SCIC `Sector` select):** DB 7's `Sector` select currently overloads "sector" with SaaS *categories* (MarTech…) **and** one vertical ("Travel & Hospitality"). Harmonize going forward: **verticals** live in *Sectors Master*; **SaaS categories** are *Sub-Sectors*. Existing signal rows are not rewritten in the kernel; new rows follow the harmonized convention.

**This layer is the first live slice of IntOS** (`AEIT_07`), not a parallel intelligence stack: it **conforms to `AEIT_06`**, runs its logic on **`arika-runtime`**, and its stores are **memory only**. The separation is load-bearing — **Notion + `AEIT_06` = memory · `arika-runtime` agents = logic/reasoning · cloud routines under the Approval Matrix = execution.** Do not collapse the OS into "a big Notion database."

**Anti-duplication map — the owner's ~20-DB "Sector OS" reconciles to a small net-new set.** Before feeding sectors, honor this (Rule: `AEIT_06` "departments consume canonical entities; they do not reinvent them"):

| Owner's proposed store | Reality in this repo | Action |
|---|---|---|
| Sector Registry · Industry Registry | **DB 1 Sectors Master + DB 2 Sub-Sectors** | **extend** (multi-vertical + Lifecycle State + Priority Score) |
| Problem · Revenue · Value-Chain · Strategic-Node · Relationship intelligence | **DB 3 Sector Intelligence** `Category` facets (Sheets 03–07) | reuse one DB, many categories; finish Sheets 04–07 |
| Trigger · Market-Event · Sector Calendar | **DB 7 Sector Signals (SCIC)** | reuse |
| Audience Intelligence | **DB 9 Audience Roles** | reuse; enrich |
| Decision-Maker · Company · Acquisition intelligence | **CRM (ClickUp) + CPAROS (06)** — `Company/Lead/Person/Opportunity` | **reference by ID, do NOT rebuild**; DB 10 holds sector-level titles/triggers, resolves to CRM `Person` |
| Competitive Intelligence (store) | **Marketing (03)** owns `Competitor` (`AEIT_06`) | reference; Sector holds pattern-reads only |
| Content Intelligence | **Content (04)** owns it (`CONTENT_INTELLIGENCE_SCHEMA.md`) | Sector **feeds** it; does not own it |
| Sector Sources | **`AEIT_08` Source Registry** (agency-wide) | reference; register sector sources there |
| Offer-Sector Matrix | **DB 8 Agency Opportunity Map** → Offer (02) | reuse |
| Sector State · Forecast · Metrics | **DB 12 + DB 13** (SCIC) + the Priority-Score block on DB 1 | extend |
| Intelligence Updates | `Change Status` + `runtime.jsonl` + IntOS Learning | reuse |
| Geography | **DB 11** (candidate canonical entity) | reuse |

**Net-new in the kernel (only these four):** (1) the multi-vertical hierarchy upgrade; (2) the **Sector Lifecycle State machine**; (3) the **Sector Priority / Attractiveness Score**; (4) the generalized **Intelligence-Object Contract** (`SECTOR_ACTIVATION_CONTRACT.md`). Everything else = **extend or reference**.

---

## 0.2 — Industry Revenue Engine (content model, ADDENDUM 3)

The Sector layer routes each industry through a **land-and-expand ladder** — **Entry** (the easiest pain the industry will pay to solve) → **Expansion** → **Transformation** (operating-system engagement). This ladder **is Offer (02)'s existing Ideal Ascension Model** (Offer Engineering Registry + the Revenue Infrastructure Audit Gateway); Sector **routes**, Offer **owns the offers**. The routing record is **DB 8 → Industry Offer Matrix**.

**The 12 capability families (controlled vocabulary; a view over the departments — `AEIT_03`).** The matrix's Entry/Expansion/Transformation stages reference these codes; each has one owning department. Where an industry needs a productized offer that isn't in the registry yet, the matrix records `GAP — needs OEOS` (an Offer (02) decision), never a fabricated offer.

| Code | Capability | Owner dept |
|---|---|---|
| `INT` | Sector & Business Intelligence | Sector (01) + Audits (14) |
| `STR` | Strategy & Revenue Architecture | Offer (02) + Consulting (15) |
| `BR` | Brand Revenue & Positioning | Branding (12) |
| `MKT` | Revenue Marketing | Marketing (03) |
| `CNT` | Content & Experience Production | Content (04) + Design (19) + Experience Eng (20) |
| `SAL` | Revenue / Sales OS | Sales (05) |
| `ACQ` | Client / Partner Acquisition | ClientPartner Acq (06) |
| `OPS` | Operations Engineering | Operations (08) |
| `AUTO` | AI Workflow Infrastructure | Automation (16) |
| `AI-X` | AI Transformation Systems | AI Enablement (17) |
| `FIN` | Financial Intelligence | Finance (09) |
| `SCALE` | Scaling & Expansion | Consulting (15) + Client Success (07) |

**Classification axes** (DB 1 verticals / DB 2 industries): `Atlas Layer` (Established/Growth/Frontier/Deep-Future) · `Portfolio Mode` (Market-Ready = scrape+acquire · Enterprise-Strategic = intelligence-led · Frontier-Intelligence = watchlist) · `Priority Tier` (T1–T4) · `Industry Type` (A Marketing / B Sales / C Ops / D Trust-driven → the entry-offer lead). **Tool-Stack Chaos** is a market-intelligence dimension (DB 2 field-group + DB 3 `Category`): per-industry fragmentation risk that feeds outreach; the **Stack Rationalization offer** is *flagged* to Offer (02), not built here.

---

## 1. The relational spine (Draft 7 + 11 + 13)

```
Sectors Master ──< Sub-Sectors ──< Sector Intelligence
                        │  │  │
      ┌─────────────────┘  │  └─────────────────┐
      ▼                    ▼                     ▼
 ICP Classification   Prospect Signal      Sector Linguistics
      │                Scores │                  │
      │                       ▼                  │
      │              Agency Opportunity Map ─────┼──► Offer (02) registry
      │                       │                  │
      ▼                       ▼                  ▼
 Audience Roles       Sector Calendar    Decision-Maker Registry
      │                (Market Events)          │
      └───────────────────────┬─────────────────┘
                              ▼
             CRM (ClickUp): Company ▸ Lead ▸ Opportunity ▸ Client ▸ Project
                              ▼
                          Result / outcome
                              ▼
                Sector Memory (runtime.jsonl)  ──► back into Sector Intelligence
```

Every Sector-owned row must be able to trace to a Sub-Sector, and every actionable insight must reach the CRM spine or it is "noise" (Draft 7).

---

## 2. The databases

Legend for field **Purpose**: `ID`=identity · `RET`=retrieval/filter · `REL`=relation · `GOV`=governance(confidence/source/freshness/status) · `EXE`=execution/decision.

### DB 1 — Sectors Master
**Primary entity:** one **vertical / market** (multi-vertical universe, §0.1). **AEIT_06:** `Sector`. **Backing:** xlsx Sheet 02, 11 (the B2B SaaS branch) + owner-added verticals. **Rows:** B2B SaaS + the non-SaaS verticals (Healthcare Multi-Location, Real Estate Brokerages, Franchise Systems, Hospitality, …), added as the owner ranks the universe.

| Field | Type | Purpose | Notes |
|---|---|---|---|
| Sector Name | Title | ID | e.g. "B2B SaaS", "Hospitality" |
| Sector ID | Text (unique) | ID | slug, e.g. `sec-b2b-saas` — the cross-platform join key |
| Category | Select | RET | Horizontal SaaS · Vertical SaaS · AI-Native · Multi-Location Vertical · **Industry Vertical** (non-SaaS: Hospitality, Healthcare, Real Estate, Franchise, …) |
| Definition | Text | ID | Draft 3 one-liner: "exists to __ by enabling __ for __" |
| **Status** | Select | GOV | **Engagement lifecycle** (added 2026-08-11) — `Active` (real, a client is served here) · `Target` (pursuing entry) · `Reference` (intelligence only — the **default meaning of every xlsx-loaded row**) · `Dormant` (parked). Distinct from `Readiness` (market buy-state) and `Lifecycle State` (OS build state). The owner sets this as the **exact real sectors + clients** are added; see §7. |
| Strategic Priority | Select | EXE | Primary · Secondary · Tertiary (maps ICP tiers, `SECTOR_OS.md` §1) |
| Readiness | Select | EXE | 🟢 Ready Now · 🟡 In Progress · 🔴 Asleep (xlsx Sheet 11) — *market buy-state* |
| **Lifecycle State** | Select | EXE | **Sector OS state machine** (new 2026-08-16): `Discovered → Mapped → Intelligence-Rich → Validated → Offer-Ready → Acquisition-Ready → Content-Ready → Campaign-Ready → Client-Validated → Authority → Dominance`. **Evidence-gated** (computed by `sector-readiness-analyst`; no self-promotion without the underlying rows). Distinct from `Status` (engagement) + `Readiness` (market). |
| **Sector Priority Score** | Number | EXE | 0–100 composite (new 2026-08-16) — ranks the universe for GTM focus. 8 dimensions (each 0–10, held in the rationale): Revenue Potential · Capability Fit · Market Growth · Pain Intensity · Buying Capacity · DM Accessibility · Competition Gap · Recurring/Expansion Potential. Computed by the analyst; **advisory**. |
| **Priority Band** | Select | EXE | `P1 Pursue now` · `P2 Build` · `P3 Monitor` · `P4 Park` — banded from the score. |
| **Priority Scoring Rationale** | Text | GOV | the 8 sub-scores + a one-line justification each — provenance for the composite (no black-box number). |
| **Atlas Layer** | Select | RET | **Established · Growth · Frontier · Deep-Future** (ADDENDUM 3 — the industry atlas) |
| **Portfolio Mode** | Select | EXE | **Market-Ready · Enterprise-Strategic · Frontier-Intelligence** — how Arika engages this vertical (scrape-and-acquire vs. strategic vs. watchlist) |
| **Priority Tier** | Select | EXE | **T1 Immediate · T2 High-Value · T3 Emerging · T4 Watchlist** |
| **Industry Type** | Select | EXE | **A Marketing-driven · B Sales-driven · C Ops-driven · D Trust-driven** — determines the entry-offer *lead* |
| Intelligence Confidence | Select | GOV | Low · Medium · High |
| Last Intelligence Update | Date | GOV | freshness |
| Next Review | Date | GOV | cadence gate |
| Sub-Sectors | Relation → Sub-Sectors | REL | one-to-many |
| Related Clients (CRM) | Text (ID list) | REL | ClickUp `Client` IDs — cross-platform reference, not a native relation |

### DB 2 — Sub-Sectors
**Primary entity:** one sub-sector. **AEIT_06:** `Sub-sector`. **Backing:** xlsx Sheet 02 (the 22 SaaS sub-sectors) + Tier-3 sub-segments. This is the hub table most others point to.

| Field | Type | Purpose | Notes |
|---|---|---|---|
| Sub-Sector Name | Title | ID | e.g. "HealthTech", "MarTech" |
| Sub-Sector ID | Text (unique) | ID | `sub-healthtech` |
| Parent Sector | Relation → Sectors Master | REL | required |
| GTM Motion | Select | RET | PLG · Sales-led · Hybrid · Partner-led (xlsx Sheet 02) |
| Revenue Model | Text | RET | subscription/usage/seat/etc. (xlsx Sheet 02) |
| Core Value Prop | Text | ID | xlsx Sheet 02 |
| Ecosystem Dependencies | Text | RET | xlsx Sheet 02 |
| **Industry** | Text | ID | the industry within the vertical (multi-vertical, §0.1) — e.g. "Hotels" (Hospitality), "Marketing SaaS" (B2B SaaS) |
| **Business Model** | Text | RET | e.g. "Independent luxury hotel" · "subscription SaaS" — the owner's hierarchy tail |
| **Company Archetype** | Text | RET | e.g. "30–100 room property" · "Series A, $5–50M ARR" — the scrape/target profile |
| **Industry Type** | Select | EXE | A/B/C/D (inherited from the vertical, overridable) — ADDENDUM 3 |
| **Tool-Stack Chaos Risk** | Select | EXE | 🔴 Extreme · 🟠 High · 🟡 Moderate · 🟢 Lower · ⚫ Strategic/Future (ADDENDUM 3 — fragmentation-risk index) |
| **Typical Tool Stack** | Text | RET | the industry's characteristic systems (e.g. "PMS · CRS · channel-mgr · RMS · CRM · POS · AI") — **transcribed from the atlas, not invented** |
| **Fragmentation Type** | Select | RET | Duplication · Integration · Intelligence (the 3 chaos types) |
| **Status** | Select | GOV | **Engagement lifecycle** (added 2026-08-11): `Active` · `Target` · `Reference` (default for xlsx-loaded rows) · `Dormant`. Distinct from `Readiness` (market buy-state). See §7. |
| Opportunity Score | Select | EXE | Low · Medium · High · Very High |
| Readiness | Select | EXE | 🟢/🟡/🔴 (xlsx Sheet 11) |
| Intelligence Confidence | Select | GOV | Low/Med/High |
| Last Update / Next Review | Date ×2 | GOV | freshness + cadence |
| Sector Intelligence | Relation → Sector Intelligence | REL | one-to-many |
| Personas | Relation → Decision-Maker Registry | REL | |
| Opportunities | Relation → Agency Opportunity Map | REL | |
| Linguistics | Relation → Sector Linguistics | REL | |
| Calendar Events | Relation → Sector Calendar | REL | |

### DB 3 — Sector Intelligence
**Primary entity:** one structured intelligence finding (NOT one big description). **AEIT_06:** `Knowledge Object`. **Backing:** xlsx Sheets 03–07. Carries SectorOS layers 5 (Infrastructure), 6 (Intelligence), 7 (Governance), 11 (Risk) as the `Category` enum.

| Field | Type | Purpose | Notes |
|---|---|---|---|
| Finding | Title | ID | one insight |
| Sub-Sector | Relation → Sub-Sectors | REL | required |
| Category | Select | RET | Structure · Economics · Value Chain · Buying Psychology · Decision Dynamics · Trust · Governance/Power · Infrastructure · Risk/Fragility · Strategic Node · **Tool-Stack Chaos** (ADDENDUM 3) (Draft 13 layers + xlsx Sheets 03–07) |
| Evidence | Text | GOV | what supports it |
| Source | Select/Text | GOV | xlsx sheet · chat · agent run · research |
| Confidence | Select | GOV | Low · Medium · High |
| Impact | Select | EXE | Low · Medium · High |
| Freshness | Select | GOV | Fresh · Aging · Stale |
| Strategic Implication | Text | EXE | the "so what" |
| Recommended Action | Text | EXE | Draft 4 execution layer |
| Routed To (Dept) | Multi-select | REL | Offer/Marketing/Sales/Content/Automation (see contract routing) |

### DB 4 — ICP Classification
**Primary entity:** one company's tier classification. **AEIT_06:** `ICP Classification` (canonical, Sector-owned). **Backing:** `SECTOR_OS.md` §1. **Writer:** agent `sector-icp-fit`.

| Field | Type | Purpose | Notes |
|---|---|---|---|
| Company | Title | ID | |
| Company ID (CRM) | Text | REL | ClickUp `Company`/`Lead` id |
| Tier | Select | EXE | Tier 1 · Tier 2 · Tier 3 · Anti-ICP · Out-of-scope |
| Recommended Action | Select | EXE | pursue_now · nurture · educate_dont_sell · skip |
| Tier Rationale | Text | GOV | |
| Fit Signals / Disqualifiers | Text ×2 | GOV | |
| Sub-Sector | Relation → Sub-Sectors | REL | |
| Signal Score | Relation → Prospect Signal Scores | REL | pair tier with score |
| Classified On | Date | GOV | |

### DB 5 — Prospect Signal Scores
**Primary entity:** one 90-point scoring event. **AEIT_06:** `Prospect Signal Score` (canonical, Sector-owned). **Backing:** Draft 15. **Writer:** agent `sector-signal-scorer`.

| Field | Type | Purpose | Notes |
|---|---|---|---|
| Prospect | Title | ID | |
| Company ID (CRM) | Text | REL | ClickUp id |
| Internal / Market / Behavioral / Stated / Competitive / Predictive | Number ×6 | EXE | 0–15 each (Draft 15) |
| Total Score | Number (rollup/sum) | EXE | 0–90 |
| Priority Band | Select | EXE | Low(0–22) · Medium(23–45) · High(46–67) · Critical(68–90) |
| Matched Service | Select | EXE | Marketing · Sales · Partner/Client Acq · Automation (Draft 15 mapping) |
| Re-score Date | Date | GOV | 30-day decay for Medium band |
| ICP Classification | Relation → ICP Classification | REL | |

### DB 6 — Sector Linguistics
**Primary entity:** one sub-sector's language map. **AEIT_06:** `Knowledge Object`. **Backing:** Drafts 9/13/14 (the crown-jewel IP, `SECTOR_OS.md` §14). Feeds Content (04) + Branding (12).

| Field | Type | Purpose | Notes |
|---|---|---|---|
| Language Map | Title | ID | e.g. "HealthTech — RevOps buyer" |
| Sub-Sector | Relation → Sub-Sectors | REL | required |
| Role Lens | Select | RET | Operator · Buyer · Amplifier · Enabler (Draft 11) / or functional role (Draft 9) |
| Surface (terms/jargon) | Text | RET | Draft 9 layer 1 |
| Functional (role language) | Text | RET | layer 2 |
| Cognitive (how they think) | Text | ID | layer 3 |
| Incentive (what they optimize) | Text | EXE | layer 4 |
| Cultural (tone/identity) | Text | ID | layer 5 |
| Words to use / avoid | Text ×2 | EXE | |
| Decision-language patterns | Text | EXE | "patterns > words" (Draft 9) |
| Confidence / Source | Select/Text | GOV | |

### DB 7 — Sector Signals (Commercial Intelligence Calendar) — *evolved 2026-08-15 (SCIC)*
**Primary entity:** one **market signal** — an event, deadline, demand shift, competitor move, regulation, aviation/tech change, etc. — carrying its **commercial interpretation over time**. **AEIT_06:** conforms to the canonical **`Signal / Event`** entity (`type, entity_ref, timestamp → triggers refresh/action`). **Backing:** Draft 8 + xlsx Sheet 10 + web-verified sources. **Live DB:** `collection://c14fedb3-6048-4bc5-8a40-6558cc985f57` — **evolved in place** from "Sector Calendar (Market Events)"; the 24 event/regulatory entries become the first signals.
> ⚠️ **Named distinctly** from Operations (08)'s canonical **`Calendar`** (the 7 Cognitive Calendars). This is the *market / temporal-intelligence* dimension, not an agency operating calendar. It is a **Signal database with calendar _views_** — Notion Calendar is the visualization layer (§4/§8), not a second store.
> 🔒 **Honesty gate (the anti-gibberish rule):** every dated record traces to an authoritative source (`Source Tier` + `Source URL` + `Last Verified`); **"real-time" = a freshness cadence, not a live stream** (cloud routines can't browse — ingestion is interactive Claude Code / human on cadence); the **live-booking/property layer is a TEMPLATE** (empty until a client connects RMS/PMS) — **never fabricate a property's numbers**; a **Tier-4 / unverified / stale** signal MUST NOT drive downstream execution.

| Field | Type | Purpose | Notes |
|---|---|---|---|
| Signal | Title | ID | the event / deadline / shift / move |
| **Signal Type** | Select | RET | **the classifier (supersedes `Calendar Type`):** Demand · Event/Compression · Seasonality · Holiday/Cultural · Sales/MICE · Travel-Trade · Distribution · Competitor · Regulatory · Economic · Aviation/Connectivity · Technology · Consumer-Behaviour · Risk/Disruption · Supplier/Cost · Industry-Knowledge |
| Sector | Select | RET | color-coded (multi-sector overlay) |
| Sub-Sector | Relation → Sub-Sectors | REL | one signal ↦ many sub-sectors allowed |
| **Geography** | Relation → Geography (DB 11) | REL/geo | Global→Region→Country→City (Property = template level) |
| Recurrence | Select | RET | annual · seasonal · one-off · uncertain |
| Change Status | Select | GOV | new · changed · cancelled · unchanged |
| **Signal Date** | Date (range) | temporal | the event/window (primary calendar view) |
| Announcement / Source Date | Date | temporal | when the market learned |
| Strategic Planning Date | Date | temporal | lead-time |
| Sales Activation Date | Date | temporal | lead-time |
| Marketing Activation Date | Date | temporal | lead-time |
| Offer Activation Date | Date | temporal | lead-time |
| Revenue Watch Date | Date | temporal | lead-time |
| Execution Deadline | Date | temporal | last sensible action |
| Last Verified | Date | GOV | freshness |
| Next Verification | Date | GOV | cadence gate |
| Review Date | Date | GOV | |
| Authoritative Source | Text | GOV | the body that runs/owns it |
| Source URL | URL | GOV | |
| **Source Tier** | Select | GOV | T1 Primary · T2 Institutional · T3 Commercial-intel · T4 Secondary (T4/unverified can't drive downstream) |
| Refresh Status | Select | GOV | Confirmed · Annual-recurring · Needs verification · Superseded/Delayed |
| Confidence | Select | GOV | Low/Med/High |
| Demand / Revenue / Sales / Marketing / Offer / Distribution / Competitive / Regulatory-Risk Impact | Select ×8 | EXE | Low/Med/High — the commercial interpretation per function |
| Commercial Priority | Select | EXE | Low/Med/High/Critical |
| Audience / Market Segment | Text | EXE | leisure/corporate/group/international/etc. |
| Recommended Action | Text | EXE | |
| Action Deadline | Date | EXE | **drives a 2nd calendar view** (proves multi-date/lead-time) |
| Departments Affected | Multi-select | REL | Sales/Marketing/Revenue(Ops)/Offer/Content/Branding/ClientPartner |
| Status | Select | GOV | monitoring · active · closed |
| Sector Intelligence | Relation → Sector Intelligence (DB 3) | REL | the interpreted **finding** (calendar→intelligence loop) |

**Migration mapping (existing 24 rows → signals, no data loss):** `Event → Signal` (title) · `Calendar Type → Signal Type` (Demand/Event/Regulatory carry over; the rest map to the nearest of the 16) · `Date/Window → Signal Date` · `Preparation Deadline → Marketing/Sales Activation Date` · `Sales/Marketing/Content Relevance → Sales/Marketing Impact` (Content Relevance retained as informational) · `Community/Entry Strategy → Recommended Action` context · `Authoritative Source / Source URL / Last Verified / Refresh Status / Sector / Sub-Sector` all carry over unchanged. New fields default empty (`Source Tier` back-filled from the existing citations).

### DB 8 — Agency Opportunity Map → **Industry Offer Matrix** *(extended ADDENDUM 3)*
**Primary entity:** one industry's **land-and-expand routing record** (the "which offer, in which order, for this industry" layer other departments consume). **Backing:** xlsx Sheet 08 (SaaS) + the Industry Revenue Engine atlas. **Distinct from** the CRM deal-level `Opportunity` (ClickUp) — this is the *market* routing intelligence, which *generates* CRM opportunities. **Routes onto Offer (02)'s ascension model; it does not own the offers.**

| Field | Type | Purpose | Notes |
|---|---|---|---|
| Opportunity | Title | ID | |
| Sub-Sector | Relation → Sub-Sectors | REL | required — the industry |
| Primary Opportunity | Text | ID | xlsx Sheet 08 |
| Entry-Point Service | Text | EXE | + illustrative price (hypothesis) |
| Retainer Upsell Path | Text | EXE | + illustrative range (hypothesis) |
| Revenue Potential / Urgency / Confidence | Select ×3 | EXE/GOV | |
| Offer Fit (Offer 02) | Text (ID) | REL | Offer Engineering Registry reference |
| CRM Opportunities generated | Text (ID list) | REL | ClickUp `Opportunity` ids |
| **Industry Type** | Select | EXE | A/B/C/D — the entry-offer lead |
| **Portfolio Mode** / **Priority Tier** | Select ×2 | EXE | Market-Ready/Enterprise/Frontier · T1–T4 |
| **Entry Capability** | Multi-select | EXE | the capability families that lead (e.g. `MKT`,`CNT`) — §0.2 vocab |
| **Expansion Capability** | Multi-select | EXE | the adjacent families (e.g. `SAL`,`AUTO`) |
| **Transformation Capability** | Multi-select | EXE | the OS-level families (e.g. `AI-X`,`OPS`) |
| **Ladder Offer Refs / OEOS Gap** | Text | REL | per stage: a real Offer registry ref, **or** `GAP — needs OEOS` where an industry-specific offer doesn't exist yet |
| **Target Decision-Maker** | Relation → Decision-Maker Registry | REL | who to approach (not IT) |
| **Pain Points** | Relation → Sector Intelligence | REL | the interpreted problems that route the entry |
| **Buying Triggers / Demand Signals** | Relation → Sector Signals | REL | reuse the SCIC layer |
| **Outreach Angle** | Text | EXE | the industry-specific opening line |
| **Scraping Fields** | Text | EXE | the intelligence-profile checklist for this industry |
| **Cross-sell / Scale Pathway** | Text | EXE | the expansion + replication route |
| **KPIs** | Text | EXE | outcomes the engagement should move |

### DB 9 — Audience Roles
**Primary entity:** one audience-role profile within a sub-sector. **Backing:** Draft 11 (Audience = Sector × Signal × Access). Relates sub-sector → CRM Lead/Person + Content persona.

| Field | Type | Purpose | Notes |
|---|---|---|---|
| Audience Profile | Title | ID | |
| Sub-Sector | Relation → Sub-Sectors | REL | required |
| Role | Select | RET | Operator · Buyer · Amplifier · Enabler (Draft 11) |
| Wants / Fears / Beliefs / Rejects | Text ×4 | ID | Draft 11 psychographic engine |
| Primary Signal Type | Select | EXE | Authority · Market · Conversion (Draft 11 signal→role map) |
| Access Paths | Text | EXE | content→DM→call, etc. |
| CRM Lead/Person | Text (ID) | REL | ClickUp reference |
| Content Persona | Text | REL | Content 04 Notion `Persona` reference |

### DB 10 — Decision-Maker Registry
**Primary entity:** one buyer title profile per sub-sector. **Backing:** xlsx Sheet 09. Sector-level titles/triggers — **references** CRM `Person`, does not replace it (AEIT_06 "roles not types").

| Field | Type | Purpose | Notes |
|---|---|---|---|
| Buyer Title | Title | ID | e.g. "VP RevOps" |
| Sub-Sector | Relation → Sub-Sectors | REL | required |
| Buying-Trigger Signals | Text | EXE | xlsx Sheet 09 |
| Outreach Intelligence | Text | EXE | LinkedIn/channel (xlsx Sheet 09) |
| Incentives / Fears / KPIs | Text ×3 | ID | Draft 16 stakeholder-map fields |
| CRM Person | Text (ID) | REL | ClickUp reference |

### DB 11 — Geography *(new 2026-08-15, SCIC — lean, agency-reused)*
**Primary entity:** one place at one level. **AEIT_06:** proposed **candidate canonical entity** (do not silently canonize — flag for owner/architecture review). Reused by any department that needs a shared geo model; the Sector Signals DB relates to it.

| Field | Type | Purpose | Notes |
|---|---|---|---|
| Name | Title | ID | e.g. "Kenya", "Nairobi" |
| Level | Select | RET | Global · Region · Country · City · **Property (template level)** |
| Parent | Relation → Geography (self) | REL | Nairobi→Kenya→East Africa→Africa→Global |
| ISO / Code | Text | ID | ISO-3166 where applicable |
| Notes | Text | — | source-market vs. destination, etc. |

### DB 12 — Sector State *(new 2026-08-15, SCIC — the "what's happening now")*
**Primary entity:** the **current condition** of one sector (× geography). Read **first** by downstream departments. Distilled from the Sector Signals + Intelligence, dated + confidence-gated. Maps SectorOS layer 6/synthesis.

| Field | Type | Purpose | Notes |
|---|---|---|---|
| State | Title | ID | e.g. "B2B SaaS — Global — 2026-Q3" |
| Sector | Select | RET | |
| Geography | Relation → Geography | REL | optional scope |
| Demand Direction | Select | EXE | ↑ · → · ↓ (by segment in Notes) |
| ADR / Price Pressure | Select | EXE | Low/Med/High (sector-appropriate metric) |
| Competition | Select | EXE | Low/Med/High |
| Connectivity / Access | Select | EXE | sector-appropriate (aviation for hospitality, distribution for SaaS) |
| Tech Disruption | Select | EXE | Low/Med/High |
| Regulatory Risk | Select | EXE | Low/Med/High |
| Top Opportunities / Threats | Text ×2 | EXE | |
| Next 30 / 90-day Critical Signals | Relation → Sector Signals | REL | the signals driving this state |
| As-of Date | Date | GOV | freshness — the whole point |
| Confidence | Select | GOV | Low/Med/High |

### DB 13 — Sector Forecast *(new 2026-08-15, SCIC — SectorOS layer 12 "Evolution")*
**Primary entity:** the **forward trajectory** of one sector. Explicitly probabilistic; never presented as fact.

| Field | Type | Purpose | Notes |
|---|---|---|---|
| Forecast | Title | ID | |
| Sector | Select | RET | |
| Geography | Relation → Geography | REL | |
| Horizon | Select | RET | 30d · 90d · 12mo · 3yr |
| Likely Trajectory | Text | EXE | the call |
| Key Drivers | Relation → Sector Signals | REL | what would confirm/break it |
| Confidence | Select | GOV | Low/Med/High |
| As-of / Review Date | Date ×2 | GOV | |

### Worked example (depth-proof) — Hospitality *(illustrative only; not a live sector)*
Hospitality is the reference that sets the depth bar; the schema above must hold **all** of it. Coverage check against the owner's hospitality spec:
- **The 6-calendar commercial fusion** (Demand · Compression/Event · Sales/MICE · Travel-Trade · Marketing-Demand · Seasonality/Destination) → `Signal Type` values (one DB, filtered views — not 6 DBs).
- **"It is in which country / property"** → `Geography` relation (Global→Africa→Kenya→Nairobi; Property = template).
- **Lead-time** (12-mo awareness → 9-mo sales → 90-day marketing → 30-day conversion → 7-day RM) → the 6 activation date fields.
- **Kenya 2026 public holidays + travel-trade dates** (WTM Africa 13–15 Apr, Indaba 12–14 May, AviaDev 9–10 Sep, WTM London 3–5 Nov, HSMAI MEA 16–18 Nov, etc.) → real signals, `Source Tier` T1/T2, `Signal Type = Holiday/Cultural` or `Travel-Trade`.
- **The live forecast layer** (pickup, occupancy, ADR, RevPAR, comp-set, SiteMinder/STR/IDeaS) → the **template/property layer** — fields exist, populated only from a client's connected RMS/PMS; **never fabricated**.
- **Sector State** ("demand ↑, MICE ↑↑, connectivity ↑, ADR pressure ↑…") → DB 12, one dated row.
- **Signal → department action** (conference announced → occupancy/ADR/MICE/F&B → Revenue/Sales/Marketing/Offer/Content signals) → the 8 impact fields + `Departments Affected` + the event emit.

---

## 3. CRM changes (ClickUp — reference, minimal)

The only additions to the live CRM (do **not** create Sector copies of these objects):

| Object (ClickUp) | New field | Type | Points at |
|---|---|---|---|
| `Company` / `Client` | `sector` | relation/text | Sectors Master `Sector ID` |
| `Company` / `Client` | `sub_sector` | relation/text | Sub-Sectors `Sub-Sector ID` |
| `Company` / `Lead` | `icp_tier` | select | ICP Classification `Tier` (written by `sector-icp-fit`) |

`Lead.ICP_fit_score` already exists (`CRM_SCHEMA.md`) → maps to DB 5 Total Score / DB 4 Tier.

---

## 4. Build notes (for Phase 3, when the connector is authorized)

1. Create DBs in dependency order: **Sectors Master → Sub-Sectors → (all others)**, so relation targets exist first.
2. All lifecycle/status fields are **`Select`** (API cannot set native `Status` options).
3. Cross-platform links (→ ClickUp) are **text ID fields**, not native Notion relations. Keep IDs stable.
4. Load rows from the xlsx via CSV extraction (no `pandas`/`openpyxl` in-env — a lightweight script or manual export). Start with one sub-sector end-to-end (HealthTech) to validate every relation resolves.
5. Register the Notion DB IDs back into `13_Tech_Stack/TECHSTACK_OS.md` and this file once created.

## 6. Live Notion IDs (built 2026-08-11)

Workspace **Arika Agency's Space** (`dac21e15-eb93-8125-ba65-0003e8debaf5`). Parent page **SectorOS — Sector Intelligence Layer**: <https://app.notion.com/p/3b921e15eb9381b781f5c85525cef272>. All 10 databases built with two-way relations; spine validated (B2B SaaS → HealthTech → VP RevOps + one intelligence finding all resolve).

| Database | Data source (collection://) | DB page |
|---|---|---|
| Sectors Master | `68a5d070-58de-4b4d-8293-0fab0849a4b9` | `2f6cef12fda5452b8a8da461a9e4b43b` |
| Sub-Sectors (hub) | `dbe10a8b-5c67-4602-9108-12feb540995c` | `80ff8ce36f36431a91dea98056ca3f00` |
| Sector Intelligence | `72f90a0f-e34e-4c54-9fcd-9af2e108527e` | `97d250a755a9440c8154ecd1c29b9f8e` |
| ICP Classification | `e557b7a9-9af7-491d-97ad-edc55aa5c455` | `7eda3779949747fca7d62053026615ef` |
| Prospect Signal Scores | `19d44ea0-09cf-4b08-9e28-4277601c54f4` | `ca06347c9ce141b19c706ab52b0f8709` |
| Sector Linguistics | `172efe6d-08b5-4c85-b24a-fa7065b3e721` | `224b50cf492c485a8b369be012982aeb` |
| Sector Calendar (Market Events) | `c14fedb3-6048-4bc5-8a40-6558cc985f57` | `051988c2851f423ead134d5ab83360be` |
| Agency Opportunity Map | `efd6319c-081e-4a6b-b930-a362ef2bc1b2` | `e6c26dd192fd4dfc93c1f5d3528f4038` |
| Audience Roles | `e0513cc9-682f-4dd4-965c-e0292abe86e4` | `2ec588347eca435785ad366ea164aab3` |
| Decision-Maker Registry | `5566c27c-d5db-4a22-9587-e57d0ce5fbbe` | `5e58fae996b143528c249cef56844c64` |

**Data load status (2026-08-11):**
- ✅ **Sub-Sectors** — all **52** (22 SaaS categories × products) from xlsx Sheet 02, each with GTM motion, revenue model, value prop, ecosystem deps, readiness (Sheet 11): **23 Ready Now · 21 In Progress · 8 Asleep**; each linked to the B2B SaaS sector.
- ✅ **Agency Opportunity Map** — all **52** (Sheet 08): primary opportunity + entry-point service (with price) + retainer upsell path (with range), each linked to its sub-sector.
- ✅ **Decision-Maker Registry** — all **52** (buyer titles from Sheet 02 ICP; buying triggers + outreach intel from Sheet 09), each linked to its sub-sector.
- ✅ **Cleanup done** — the placeholder "HealthTech" validation seed was de-parented + relabeled; its two validation rows (VP RevOps, predictive-signal finding) re-pointed to the real `CRM (MarTech)` sub-sector.
- ✅ **Sector Calendar** — schema enhanced (Sector color-coding for overlay, Calendar Type = 7 Draft-8 layers, Authoritative Source, Source URL, Last Verified, Refresh Status). **24 web-verified entries (2026-08-11):** the original 12 + **12 new sector-anchor events** so **every one of the 20 sectors now has at least one real, future-dated anchor** (Aug-2026 → Mar-2027), each color-coded, source-cited (org + Source URL + `Last Verified`), linked to a representative sub-sector, with the Sheet-10 community/entry-strategy captured. All `Confirmed` (VERGE + HIMSS27 upgraded from `Needs verification`). Anchors chosen to be *future* as of Aug 2026 (e.g. Travel/Hosp → The Hospitality Show Nov, not the past June HITEC; BioTech → JPM Jan-2027). *No invented dates* — every date traces to the organizer. Engine spec: [`SECTOR_CALENDAR_REFRESH_SPEC.md`](SECTOR_CALENDAR_REFRESH_SPEC.md).
- ✅ **Sector Intelligence — Sheet 03 (Problems) loaded (2026-08-11):** **52 findings** (one per sub-sector), `Category = Buying Psychology`, `Evidence` = the sheet's financial-impact range, `Impact` = urgency (High/Medium), `Strategic Implication` = the emotional/business buying-pressure, `Routed To = Marketing + Sales + Offer`, `Confidence = Medium` (the $ figures are owner-curated ranges/hypotheses, not validated — §1 honesty caveat), each linked to its sub-sector. Loader: `scratchpad/gen_intel03.py`.
- ⏳ **Still to load:** Sector Intelligence **Sheets 04–07** (internal struggles, revenue intelligence, strategic nodes, cross-sector relationship map) — same pattern, next; **Sector Linguistics**; **Audience Roles**. Calendar: the **secondary** Sheet-10 events (each sub-sector lists 2–3; only the anchor is loaded) + the 5 non-Event layers — deliberately not dumped undated (no-fabrication + signal); add via the manual refresh sweep as dates verify.
- **Intentionally empty:** `ICP Classification` + `Prospect Signal Scores` — written by the `sector-icp-fit` / `sector-signal-scorer` agents at runtime, not seeded.
- **`Status` field added (2026-08-11)** to Sectors Master + Sub-Sectors — engagement lifecycle (`Active`/`Target`/`Reference`/`Dormant`). All current rows are **`Reference`** (empty reads as Reference) until the owner marks the exact real sectors/clients. See §7 for the convention. Not back-filled row-by-row (write-light; the owner is about to curate the real set).
- Extraction: `scratchpad/xlsx_to_csv.py` (pure-stdlib) → per-sheet CSVs; loaders `gen_subsectors.py` + `gen_loads.py`.
- 🟢 **SCIC evolution — Phase A + Phase B COMPLETE (2026-08-15):** DB 7 evolved in place into **Sector Signals (Commercial Intelligence Calendar)** (`collection://c14fedb3-…`, renamed) — full signal-object schema live (Signal Type ×16, Geography + Sector Intelligence relations, the 6 lead-time activation dates + Announcement/Next-Verification/Review, Source Tier, the 8 impact fields, Commercial Priority, Confidence, Audience/Market Segment, Recommended Action, Action Deadline, Departments Affected, Status, Recurrence, Change Status). New DBs created: **Geography** `collection://e095c661-86cd-4f45-9149-eca1c7195e71` (self-parent hierarchy) · **Sector State** `collection://4a9b8ca5-f042-4938-85af-e0706ee9e1ff` (→ Sectors Master + Geography + Signals) · **Sector Forecast** `collection://920781ae-fabd-4c9f-8045-42b40abf3cda` (→ Sectors Master + Geography + Signals). Doctrine + honesty gate in `SECTOR_ACTIVATION_CONTRACT.md` §12.
- 🟢 **Phase B — back-fill + views DONE (2026-08-15):** all **24 rows' `Signal Type` back-filled** from `Calendar Type` (22 `Event/Compression` + 2 `Regulatory`; verified 0 nulls). `Calendar Type` retained as a legacy shadow column (harmless; can be dropped later). **12 views built** on `collection://c14fedb3-…`: two calendars — **📅 Master Signal Calendar** (by `Signal Date`) + **⏰ Activation Deadlines** (by `Action Deadline`, proves the multi-date/lead-time model) — plus **🗓️ Upcoming — Chronological** (list, sort `Signal Date` ASC), **🔺 High Commercial Impact**, **💰 Sales**, **📢 Marketing**, **📈 Revenue / Pricing**, **🥊 Competitor Movement**, **⚖️ Regulatory / Risk**, **✈️ Travel-Trade**, **🔍 Unverified / Needs Research**, and **🗂️ By Sector** (board). **Note — rolling windows:** "next 7 / 30 / 90 days" are *not* built as separate views because the create-view DSL only supports absolute ISO dates; they are a one-click **native relative-date filter** ("is within the next week/month") added on the Upcoming view in the Notion UI. Six lead-time date columns + `Action Deadline` are empty until Phase C fills a depth slice.
- 🟢 **Phase C — depth-proof on real data DONE (2026-08-15):** three real signals upgraded to the **full signal object** — **Money20/20 USA 2026** (FinTech compression event → 🇺🇸 USA, six lead-time offsets T-120→event, 8 impact fields, `Departments Affected`, `Source Tier` T1, High priority), **CSRD Wave-2 delay** (→ 🇪🇺 EU, repositioning timeline to the ESRS H1-2026 milestone, linked to an interpreted **Sector Intelligence finding**), **FSMA 204 delay** (→ 🇺🇸 USA, re-time to 2028, linked finding). Geography DB seeded with **Global → EU / USA** (hierarchy live). Two interpreted findings created in the Sector Intelligence DB (`72f90a0f-…`) — proving the **calendar→intelligence loop**. **Honesty:** findings carry only verified regulatory facts (`Confidence: High`, `Source: research`); lead-time dates are **derived planning offsets** (per Contract §12), not invented external dates; no property/booking numbers fabricated.
- ⏳ **SCIC remaining (Phase C-breadth / D / E):** add a web-verified **economic + technology + competitor** example (fresh sourcing required — no fabrication); evolve the refresher → `sector-signal-refresher` (advisory) + wire the small downstream event set (`DEMAND_SHIFT`/`COMPRESSION_EVENT`/`COMPETITOR_MOVE`); flag Geography as an `AEIT_06` candidate canonical entity; generalize across sectors + distil `Sector State` per active sector.
- 🟢 **Sector OS Kernel — K1 (Ontology + Registry) DONE (2026-08-16):** universe is now **multi-vertical** (§0.1) — B2B SaaS is one branch. **DB 1 Sectors Master** extended live with `Lifecycle State` (11-state machine), `Sector Priority Score` (number), `Priority Band` (P1–P4), `Priority Scoring Rationale`; **DB 2 Sub-Sectors** extended live with `Industry` / `Business Model` / `Company Archetype`. The anti-duplication reconciliation map is §0.1. (Fetch confirmed Sub-Sectors is **already relation-wired** to Marketing `Campaigns`, Content `Content Briefs`/`Content Opportunities`, Offer `Offers`, Branding `Narrative Positions`, plus Decision-Makers/ICP/Signal-Scores — the spine is cross-department already; extend, don't rebuild.) Remaining kernel: **K2** Intelligence-Object Contract + Control-Tower spec + construction mandate (`SECTOR_ACTIVATION_CONTRACT.md`); **K3** scoring/state agent + Sheets 04–07 load; **K4** engine↔agent↔event doc; **K5** AEIT ratification. Plan: `plans/from-the-chat-from-dreamy-moth.md` ADDENDUM 2.
- 🟢 **Industry Revenue Engine — P1 (schema) DONE (2026-08-19):** the content model for the multi-vertical universe (§0.2). **DB 1 Sectors Master** extended live with `Atlas Layer` · `Portfolio Mode` · `Priority Tier` · `Industry Type` (A/B/C/D). **DB 2 Sub-Sectors** extended with `Industry Type` + the Tool-Stack field-group (`Tool-Stack Chaos Risk` · `Typical Tool Stack` · `Fragmentation Type`). **DB 8 Agency Opportunity Map → Industry Offer Matrix** (the routing layer) extended live with `Industry Type`/`Portfolio Mode`/`Priority Tier`, the `Entry`/`Expansion`/`Transformation Capability` multi-selects (the 12 families), `Ladder Offer Refs / OEOS Gap`, `Outreach Angle`, `Scraping Fields`, `Cross-sell / Scale Pathway`, `KPIs`, + relations `Target Decision-Maker`→DB 10, `Pain Points`→DB 3, `Buying Triggers / Demand Signals`→DB 7. **DB 3 Sector Intelligence** `Category` gains `Tool-Stack Chaos`. The Entry→Expansion→Transformation **ladder routes onto Offer (02)'s ascension model** (capability-routing + `GAP — needs OEOS` where an industry-specific offer doesn't exist). Remaining: **P2** verticals + Tier-1 industries · **P3** full established economy (~88) · **P4** Growth thinner + Frontier watchlist · **P5** score/rank + OEOS-gap list. Plan: ADDENDUM 3.
- 🟢 **Industry Revenue Engine — P2 → P5 DONE (2026-08-19):** **P2/P3** loaded the **21 established-economy verticals** + **88 division-level industries** as Sub-Sectors (each with Industry Type + Tool-Stack Chaos read) + **87 Industry Offer Matrix rows** (Entry→Expansion→Transformation capability ladder + `Ladder Offer Refs / OEOS Gap`). **P4** added 3 grouping verticals (Growth / Transformation Economy · Frontier Industries · Deep-Future Watchlist) + **48 Growth overlay rows** (thin, transcribed ladder coding, SaaS-branch overlaps cross-referenced not duplicated) + **14 watchlist rows** — Frontier as the source's **10 named clusters** + Deep-Future as **4 thematic rows**, every member enumerated in-body, `Tool-Stack Chaos Risk = Strategic/Future` (clustered per the source's "maintain Watchlists" doctrine + lean preference; explodable to per-industry rows later). **P5** ran the `sector-readiness-analyst` scoring framework (8 dims → 0–100, P1–P4; advisory, Confidence Medium) and wrote `Sector Priority Score`/`Priority Band`/`Priority Scoring Rationale` to the **10 decision-critical verticals** (B2B SaaS + 9 T1). **September focus (P1): B2B SaaS 88 · Hospitality 78 · Professional Services 76.** OEOS entry-offer gap list + flagged Stack Rationalization offer → `02_Offer/OFFER_OS.md` §3; 12-family alias → `AEIT_03`. **Totals: 25 verticals · 202 Sub-Sectors** (52 SaaS + 88 established + 48 Growth + 14 Frontier/Deep-Future) · matrix rows unchanged at 87 (Growth/Frontier deliberately carry no matrix rows). No fabricated offers/prices/data; per-company scoring + scraping deferred/gated (Part E). **ADDENDUM 3 complete.**

## 5. Coverage check (nothing missed)

Draft 7's 5 DBs → Sectors/Sub-Sectors + Opportunity Map (2,8) · Offers/Clients/Execution now referenced in CRM (§3). Draft 3 mapping template + Draft 5 infra layers + Draft 13 layers 5/6/7/11 → DB 3 `Category` enum. Draft 8 → DB 7. Draft 9/14 → DB 6. Draft 11 → DB 9. Draft 15/16/17 → DB 4 + DB 5 + DB 10. Layers 4 (Journey), 9 (Memory) live outside Notion (repo doctrine + `runtime.jsonl`) per the plan's Part 1 table.

---

## 7. Operating mode & status convention — *read this before trusting a row*

**Operating mode = MANUAL APPLY, by design (2026-08-11).** These 10 databases are **live**, but nothing writes to them automatically. Every row, relation, and status you see was placed by a human or by Claude Code **applying a change on request** — reading the xlsx / an agent's advisory output / a web-verified source, then writing it in. The Sector agents (`sector-*`) are **advisory**: they *recommend* what should be written; they do not perform the write. This is deliberate and matches `00_Agency_Governance/AUTOMATION_APPROVAL_MATRIX.md` doctrine — **we do not document an intention as an automation.** When (and only when) a database gets a real unattended writer, it gets a matrix row first, and this section names it. Until then: *if a row exists, a human/Claude-Code put it there this way.*

**Status convention (the real-vs-reference line).** `Status` (on Sectors Master + Sub-Sectors) is the **engagement lifecycle**, and it is what makes the operational picture honest as the owner adds the *exact* sectors and clients:

| Status | Meaning | Applies to |
|---|---|---|
| `Reference` | Intelligence only — no real engagement. **The default for every currently-loaded row** (the 52 xlsx sub-sectors + B2B SaaS are all reference data). | the xlsx taxonomy |
| `Target` | We are actively pursuing entry / a named prospect exists. | set by owner |
| `Active` | Real — a client is currently served in this sector/sub-sector (a ClickUp `Client` ID sits in `Related Clients (CRM)`). | set by owner |
| `Dormant` | Was active/target, now parked. | set by owner |

- **An empty `Status` reads as `Reference`** until explicitly set — so the loaded taxonomy is never mistaken for real engagement.
- **Clients live in the CRM (ClickUp), not here.** When the owner adds an exact client, the client *record* is a ClickUp `Client`; its ID goes into the sector's `Related Clients (CRM)` text field and the sector flips to `Active`. Sector's Notion **references** the client by ID — it does not store a second copy (§0 law 2, §3).
- **`Readiness` ≠ `Status`.** `Readiness` (🟢/🟡/🔴) is the *market's* buy-state from xlsx Sheet 11; `Status` is *our* engagement state. A sub-sector can be `Ready Now` (market) but `Reference` (we have no client there yet).
