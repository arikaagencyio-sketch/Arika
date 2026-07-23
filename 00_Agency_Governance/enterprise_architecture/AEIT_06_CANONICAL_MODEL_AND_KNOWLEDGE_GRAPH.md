# AEIT_06 — Canonical Entity Model & Knowledge Graph (Blueprint)

**Version:** v0.1
**Last updated:** 2026-07-22
**Owner:** Mary Thuo (Agency Governance, 00)
**Fills:** `REGISTRY_TAXONOMY_REFERENCE.md` future-state registries **Semantic/Ontology** and
**Relationship (entity graph)**. Extends `CRM_SCHEMA.md` (6 objects) to the whole enterprise.
**Depends on:** ratified `AEIT_05` R1 (Sector sets `ICP_fit_score`), R2 (glossary).
**Status:** Blueprint. Specifies the model; does not populate instances (deferred to post-activation).

> **Governing rule (the whole point):** *departments consume canonical entities; they do not
> reinvent them.* The CRM schema exists precisely because departments "independently reinvented a
> slightly different model" (`CRM_SCHEMA.md:12`). This document generalizes that fix from CRM to the
> entire agency, so IntOS (`AEIT_07`) has one object model to write into.

---

## 1. Modeling principles

1. **Roles, not duplicate types.** A `Company` is one entity; *prospect, client, partner,
   competitor* are **roles/relationships** it holds — not separate tables. This is what prevents the
   client/customer/account sprawl (`AEIT_04 §B1`).
2. **One owner per entity.** Every canonical entity has exactly one owning department (the
   Architecture Review Checklist enforces this on anything new).
3. **Every entity carries knowledge-state attributes** (`confidence`, `trust`, `freshness`,
   `source_id`, `version`) so nothing is treated as more certain than it is (SM4, `AEIT_05`).
4. **Existing before new.** Each entity below is tagged **[CRM]** (already in `CRM_SCHEMA.md`),
   **[EXT]** (extends a CRM concept), or **[NEW]**.

---

## 2. Canonical entity catalogue

### Party domain
| Entity | Tag | Owner | Key fields | Notes |
|---|---|---|---|---|
| **Company** | [NEW] | Sector (01) for market data; Governance for identity | legal_name, domain, sector_id, size, ARR_band, roles[] | The master org entity. Prospect/Client/Partner/Competitor are **roles**, not types. |
| **Person** | [NEW] | dept holding the relationship | name, company_id, role, contact, decision_authority | Decision-Maker/Contact are role flags. |
| **Client** (role) | [CRM] | Client Success (07) | lifecycle_stage, relationship_status, health_score, account_owner | SM1. "Account" = billing sense only (R2). |
| **Partner** (role) | [CRM] | ClientPartner Acq (06) | partner_type, stage, fit_score, trust_score | SM2. |
| **Competitor** (role) | [NEW] | Sector (01) | positioning, overlap | Feeds market intelligence. |

### Market domain
| Entity | Tag | Owner | Key fields | Notes |
|---|---|---|---|---|
| **Sector / Sub-sector** | [NEW] | Sector (01) | taxonomy_id, GTM_motion, ICP_tier, value_prop | The 22-sector SaaS taxonomy (`SECTOR_OS.md:58`). |
| **ICP Classification** | [EXT] | **Sector (01)** *(ratified R1)* | tier (1/2/3/Anti), `ICP_fit_score`, rationale | **Sector SETS; Sales CONSUMES.** Amends `CRM_SCHEMA.md:23`. |
| **Prospect Signal Score** | [EXT] | Sector (01) | 6×0–15, priority P1–P4 (R3) | 90-pt scorecard; "priority" not "Critical" (R3). |

### Commercial domain
| Entity | Tag | Owner | Key fields | Notes |
|---|---|---|---|---|
| **Offer** | [NEW] | Offer (02) | registry_id, pricing, ascension_stage | Index of record = Offer Engineering Registry. |
| **Lead** | [CRM] | Sales (05) *(gen: 03/04/06)* | source, ICP_fit_score (from Sector), touch_history | SM3. |
| **Opportunity** | [CRM] | Sales (05) | stage, value, probability | SM3. |
| **Campaign** | [NEW] | Marketing (03) | channel, offer_id, audience, budget | Demand generation. |
| **Invoice / Payment** | [CRM] | Finance (09) | amount (USD priced/KES invoiced), status | Conversion calculator = roadmap gap. |

### Creative / delivery domain
| Entity | Tag | Owner | Key fields | Notes |
|---|---|---|---|---|
| **Project** | [CRM] | Operations (08) | scope, status, client_id | Delivery unit. |
| **Brand / Brand Genome** | [NEW] | Branding (12) | positioning, voice, identity | Consumed by Content/Design/Experience. |
| **Content** | [NEW] | Content (04) | type, brief_id, narrative, status | The content asset. |
| **Creative Asset** | [NEW] | Design (19) | asset_type, source_tool, brand_check | Asset Library. |
| **Experience** | [NEW] | Experience Eng (20) | spec_id, scenes, tech_stack | Interactive builds. |

### Knowledge / operations domain (the IntOS substrate)
| Entity | Tag | Owner | Key fields | Notes |
|---|---|---|---|---|
| **Source** | [NEW] | IntOS *(Governance until IntOS exists)* | source_id, trust, coverage, cadence, legal | Full schema in `AEIT_08`. |
| **Knowledge Object** | [NEW] | IntOS | claim, entity_ref, confidence, trust, freshness, source_id, state | SM4 lifecycle. The atomic intelligence unit. |
| **Signal / Event** | [NEW] | IntOS | type, entity_ref, timestamp | Triggers refresh/action. |
| **Document / Conversation / Meeting** | [NEW] | dept of origin | content, participants, entity_refs | Raw material for knowledge extraction. |
| **Workflow / Automation / Agent / Skill** | [CRM-adjacent] | owning dept + Automation (16) | trigger, risk_class, matrix_row | Governed by Approval Matrix. |
| **Calendar** | [NEW] | Operations (08) | one of the 7 Cognitive Calendars | Already defined; entity-ized here. |

---

## 3. Glossary (ratified R2–R4)

| Term | Canonical meaning | Deprecated / disambiguated |
|---|---|---|
| **Client** | a Company in the client relationship (SM1) | ~~customer~~ (deprecated) |
| **Account** | billing/finance sense only | not a synonym for Client |
| **Risk class** | Constitution's 5-class numeric | ~~Low/Med/High/Critical for risk~~ |
| **Priority** | prospect band P1–P4 | ~~"Critical" as a priority~~ |
| **Pipeline** | always qualified: "Pipeline Calendar" / "Sales pipeline" / "Acquisition pipeline" | bare "pipeline" |
| **CRM** | "Agency CRM" (canonical) vs "client-CRM deliverable" vs (deleted) dead template | bare "CRM" |

---

## 4. Knowledge graph — the relationship layer

The agency must understand **relationships**, not isolated records. The knowledge graph is the set
of typed edges over the entities in §2.

### Core edge types
```
Person        —[works_at]→          Company
Company       —[belongs_to]→        Sector
Company       —[has_role]→          {Prospect | Client | Partner | Competitor}
Company       —[competes_with]→     Company
Company       —[classified_as]→     ICP Classification        (set by Sector)
Lead          —[derived_from]→      Company + Signal Score
Opportunity   —[for]→               Company + Offer
Campaign      —[targets]→           Sector | Audience
Content       —[expresses]→         Brand
Content       —[generated_by]→      Agent | Design
Knowledge Obj —[about]→             {any entity}
Knowledge Obj —[sourced_from]→      Source
Knowledge Obj —[supersedes]→        Knowledge Obj   (versioning)
Invoice       —[bills]→             Client (as Account)
```

### Every node carries (per the future-state "Relationship" registry)
`parent · children · dependencies · consumers · ownership · lifecycle_state · confidence · trust ·
freshness(last_verified) · version_history · supersedes/superseded_by`

### Why this matters
- **Entity resolution** (one of the missing capabilities, `AEIT_03 §2`) becomes possible: the same
  Company observed from three sources resolves to one node instead of three Leads.
- **The supersession edge** generalizes the discipline the repo already uses for tool inventory and
  automations (last-verified, not activation date) to *all* knowledge.
- It gives IntOS (`AEIT_07`) a single write target and gives every department one place to read
  relationships instead of re-deriving them.

---

## 5. What is NOT built here (deferred)
- **Instances.** This is the schema/ontology, not populated data. Real Company/Knowledge-Object
  instances arrive when IntOS is activated and real clients exist.
- **A graph database.** Whether the graph lives in ClickUp relations, `bois`' vector store, or a
  dedicated graph DB is a Tech Stack decision sequenced in `AEIT_10` — not pre-decided here.

## 6. Decision Log
- **2026-07-22 — Canonical model + knowledge graph blueprinted.** Role-not-type modeling adopted;
  ICP Classification owned by Sector per ratified R1; glossary per R2–R4; knowledge-graph edge model
  defined as the IntOS write target. — Claude Code (Opus 4.8)

## 7. Changelog
- **v0.1 (2026-07-22):** Created. — Claude Code (Opus 4.8)
