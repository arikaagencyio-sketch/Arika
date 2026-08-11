# Sector — Notion Data Model (Schema Spec)

**Department:** Sector (01) · **Status:** Design spec (Phase 1) — build-ready, not yet built in Notion (connector authorization pending).
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
**Primary entity:** one top-level sector. **AEIT_06:** `Sector`. **Backing:** xlsx Sheet 02, 11. **Rows (initial):** B2B SaaS (primary) + the Tier-3 verticals (Healthcare Multi-Location, Real Estate Brokerages, Franchise Systems).

| Field | Type | Purpose | Notes |
|---|---|---|---|
| Sector Name | Title | ID | e.g. "B2B SaaS" |
| Sector ID | Text (unique) | ID | slug, e.g. `sec-b2b-saas` — the cross-platform join key |
| Category | Select | RET | Horizontal SaaS · Vertical SaaS · AI-Native · Multi-Location Vertical |
| Definition | Text | ID | Draft 3 one-liner: "exists to __ by enabling __ for __" |
| Strategic Priority | Select | EXE | Primary · Secondary · Tertiary (maps ICP tiers, `SECTOR_OS.md` §1) |
| Readiness | Select | EXE | 🟢 Ready Now · 🟡 In Progress · 🔴 Asleep (xlsx Sheet 11) |
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
| Category | Select | RET | Structure · Economics · Value Chain · Buying Psychology · Decision Dynamics · Trust · Governance/Power · Infrastructure · Risk/Fragility · Strategic Node (Draft 13 layers + xlsx Sheets 03–07) |
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

### DB 7 — Sector Calendar (Market Events)
**Primary entity:** one market timing event. **AEIT_06:** `Calendar/Event`. **Backing:** Draft 8 + xlsx Sheet 10.
> ⚠️ **Named distinctly** from Operations (08)'s **7 Cognitive Calendars** (`AGENCY_REVENUE_TARGETS.md`). This is the *sector/market* time dimension, not the agency's operating calendars.

| Field | Type | Purpose | Notes |
|---|---|---|---|
| Event | Title | ID | conference, buying window, fiscal moment |
| Sub-Sector | Relation → Sub-Sectors | REL | |
| Calendar Type | Select | RET | Demand · Event · Operational · Financial · Content/Media · Regulatory · Innovation/Trend (Draft 8) |
| Date / Window | Date (range) | RET/EXE | |
| Sales / Marketing / Content Relevance | Select ×3 | EXE | Low/Med/High |
| Preparation Deadline | Date | EXE | lead time |
| Community / Entry Strategy | Text | EXE | xlsx Sheet 10 |

### DB 8 — Agency Opportunity Map
**Primary entity:** one sub-sector-level agency opportunity. **Backing:** xlsx Sheet 08. **Distinct from** the CRM deal-level `Opportunity` (ClickUp) — this is the *market* opportunity, which *generates* CRM opportunities.

| Field | Type | Purpose | Notes |
|---|---|---|---|
| Opportunity | Title | ID | |
| Sub-Sector | Relation → Sub-Sectors | REL | required |
| Primary Opportunity | Text | ID | xlsx Sheet 08 |
| Entry-Point Service | Text | EXE | + illustrative price (hypothesis) |
| Retainer Upsell Path | Text | EXE | + illustrative range (hypothesis) |
| Revenue Potential / Urgency / Confidence | Select ×3 | EXE/GOV | |
| Offer Fit (Offer 02) | Text (ID) | REL | Offer Engineering Registry reference |
| CRM Opportunities generated | Text (ID list) | REL | ClickUp `Opportunity` ids |

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
- ⏳ **Still to load:** Sector Intelligence (Sheets 03–07: problems, struggles, revenue intelligence, strategic nodes), Sector Calendar (Sheet 10: events & communities), Sector Linguistics, Audience Roles.
- **Intentionally empty:** `ICP Classification` + `Prospect Signal Scores` — written by the `sector-icp-fit` / `sector-signal-scorer` agents at runtime, not seeded.
- Extraction: `scratchpad/xlsx_to_csv.py` (pure-stdlib) → per-sheet CSVs; loaders `gen_subsectors.py` + `gen_loads.py`.

## 5. Coverage check (nothing missed)

Draft 7's 5 DBs → Sectors/Sub-Sectors + Opportunity Map (2,8) · Offers/Clients/Execution now referenced in CRM (§3). Draft 3 mapping template + Draft 5 infra layers + Draft 13 layers 5/6/7/11 → DB 3 `Category` enum. Draft 8 → DB 7. Draft 9/14 → DB 6. Draft 11 → DB 9. Draft 15/16/17 → DB 4 + DB 5 + DB 10. Layers 4 (Journey), 9 (Memory) live outside Notion (repo doctrine + `runtime.jsonl`) per the plan's Part 1 table.
