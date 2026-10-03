# CRM Schema (Marketing/Content → Sales → Client Success → Finance)

**Status:** v0.2.1 — core CRM live in ClickUp; Company / organization-level and Pilot Engagement extensions specified, not verified live. Public prospect identities can be reserved outside Git; CRM registration requires write/read-back and deduplication. A Pilot Engagement is required for a pilot, not invented for an initial prospect inquiry.
**Last updated:** 2026-10-03


> Referenced from [`GLOBAL_OS.md`](../GLOBAL_OS.md) §11 (closes "Required Agency-Wide Closure Systems" item 4). This is the canonical object model every department's tooling should converge toward — it does not assume any specific CRM platform (that selection belongs to Tech Stack, `13_Tech_Stack/TECHSTACK_OS.md`).

---

## Why this exists

Marketing/Content, Sales, Client Success, and Finance all touch the same underlying entities (a prospect becomes a lead becomes an opportunity becomes a client becomes a billing account) but without a shared schema, each department's raw drafts independently reinvented a slightly different model. This file is the single object model all of them should reference.

## Core Objects

### Company / Organization Level
**Added 2026-10-02** — reconciles `AEIT_06`'s canonical `Company` entity with the Hospitality pilot's real structure. A Company row represents a durable organization identity or a meaningful level inside it: group, property/branch, outlet, shared service, or standalone outlet. **Prospect, Client, Partner and Competitor remain roles, not object types.**

| Field | Type | Set by | Notes |
|---|---|---|---|
| company_id | string | System / Governance (00) | Canonical ID, `ORG-####`. Do not encode structure or status into the ID. |
| display_name, legal_name | string | Governance (00) / CRM owner | Real names live in CRM / owner identity storage; repo markdown may reference the ID only when the identity should stay private. |
| domain | string | Sector (01) / Sales (05) | Website/domain when public and verified. |
| structure_type | enum | Governance (00) + Sector (01) | `SGL` single-site independent; `MBR` multi-branch single brand; `GRP` multi-property group; `HLD` holding/multi-brand; `OUT` standalone outlet. |
| entity_level | enum | Governance (00) + Sector (01) | organization-root, group, shared-service, brand, property, branch, outlet. |
| parent_company_id | string (FK → Company, nullable) | System | Parent group/brand/property. Blank only for root organizations. |
| root_company_id | string (FK → Company) | System | The top of the organization tree; lets a property or outlet roll up without losing its own identity. |
| sector, sub_sector | relation/text | Sector (01) | Set per level. A hotel group may be Hospitality; a restaurant outlet may also carry Food & Beverage; a spa may carry Wellness. |
| roles[] | enum array | Owning department | prospect, client, partner, competitor — roles can coexist and change over time. |
| source_status | enum | Sector (01) / Governance (00) | owner-confirmed, web-verified, CRM-imported, unverified, archived. |
| identity_storage_ref | string | Governance (00) | Pointer to the private identity/CRM record when the repo should not contain the real name. |

**Operating rule:** structure is a mutable field, not identity. If a single hotel becomes a group, or a group sells one property, the `ORG-*` identity history remains intact and the parent/child links change.

### Lead
| Field | Type | Set by | Notes |
|---|---|---|---|
| lead_id | string | System | Unique identifier |
| source | enum | Marketing (03) / Content (04) / ClientPartner Acquisition (06) / Presence (21) | inbound, outbound, referral, partner, event, inreach |
| source_campaign | string | Marketing (03) / Content (04) | Which campaign/content piece generated this lead |
| contact_name, contact_email, company | string | Marketing (03) / Content (04) | Raw capture data |
| company_id | string (FK → Company) | Sales (05) / Sector (01) | Canonical organization identity once resolved. |
| target_company_level_id | string (FK → Company) | Sales (05) / Sector (01) | Exact group/property/branch/outlet/shared-service level the lead belongs to. |
| ICP_fit_score | number | Sales (05) | Qualification scoring, see Constitution §5 for any automation risk-class implications |
| stage | enum | Sales (05) | new → contacted → qualified → opportunity → closed-won / closed-lost |
| created_at, last_touch_at | datetime | System | |

> **Live check — `Lead` list, 2026-09-22.** Owner-authorised, read-only schema metadata; target/schema existence only; delivery not tested. Six custom fields exist: `Source` (dropdown), `Source Campaign`, `Contact name`, `Contact Email`, `Company`, `ICP Fit Score`. **`lead_id` and `last_touch_at` are not custom fields** — ClickUp's native task id and update timestamp stand in, a distinction the 2026-07-01 note below (*“every custom field in the Core Objects tables above is now live”*) did not draw. `stage` is a status pipeline, as designed, and `created_at` is native. **The live `Source` options omit `inreach`**, which this table lists: inbound, outbound, referral, partner, event. No task, member, comment or activity was read; nothing was written.

### Opportunity
| Field | Type | Set by | Notes |
|---|---|---|---|
| opportunity_id | string | System | |
| lead_id | string (FK) | System | Links back to originating Lead |
| company_id | string (FK → Company) | System / Sales (05) | Canonical organization identity. |
| target_company_level_id | string (FK → Company) | Sales (05) | Exact level the offer is being sold to; prevents a property opportunity from being mistaken for a group opportunity. |
| offer_id | string (FK) | Offer (02) | Which packaged offer this opportunity is for |
| deal_value | number | Sales (05) | |
| stage | enum | Sales (05) | discovery → proposal → negotiation → closed-won / closed-lost |
| owner | string | Sales (05) | Individual rep, once named owners exist |
| close_date_target, close_date_actual | date | Sales (05) | |

### Client
| Field | Type | Set by | Notes |
|---|---|---|---|
| client_id | string | System | Created on closed-won |
| opportunity_id | string (FK) | System | Links back to the won opportunity |
| onboarding_status | enum | Client Success (07) | not-started → in-progress → complete |
| health_score | number | Client Success (07) | Composite of engagement, NPS, delivery satisfaction — see `AGENCY_KPI_DICTIONARY.md` |
| account_owner | string | Client Success (07) | Individual CSM, once named owners exist |
| contract_id | string (FK) | Legal (10) | Links to the governing contract |
| lifecycle_stage | enum | Client Success (07) | onboarding → delivery → retention → expansion → advocacy → offboarding → re-entry-loop — maps to the 9-stage model, `07_Client_Success/CLIENTSUCCESS_OS.md` §4 |
| relationship_status | enum | Client Success (07) | active → at-risk → offboarding → churned-alumni → churned-do-not-recontact → win-back-candidate — added 2026-06-30 with the offboarding/retention workflow build-out |
| churn_reason | enum (nullable) | Client Success (07) | price, results-not-realized, fit-mismatch, internal-change-at-client, competitor, budget-cut, scope-creep-friction, non-payment, no-reason-given — set only at offboarding, see `CLIENTSUCCESS_OS.md` §10 |
| offboarding_type | enum (nullable) | Client Success (07) | planned (contract end), unplanned (churn/dissatisfaction), involuntary (non-payment/breach) — set only at offboarding |

### Engagement / Project
| Field | Type | Set by | Notes |
|---|---|---|---|
| project_id | string | System | |
| client_id | string (FK) | System | |
| company_id / target_company_level_id | string (FK → Company) | System / Client Success (07) | Carries the exact organization level from the won opportunity into delivery. |
| scope_summary | text | Client Success (07) → Operations (08) handoff | What was agreed |
| status | enum | Operations (08) | scoped → in-delivery → review → complete |
| sla_target_date | date | Operations (08) | |

### Pilot Engagement
**Added 2026-10-02** — a pilot is an engagement record pointing at a Company level. It is not a company, not a prospect type, and not a simulation. This lets the Hospitality pilot be active without putting the real company name into repo markdown.

| Field | Type | Set by | Notes |
|---|---|---|---|
| pilot_id | string | System / Governance (00) | Canonical pilot ID, `PILOT-*` (for example `PILOT-H-*` for Hospitality). |
| company_id | string (FK → Company) | Governance (00) / Sales (05) | Root organization being tested with. |
| target_company_level_id | string (FK → Company) | Sector (01) / Sales (05) | Exact level for the pilot: group, property/branch, outlet, or shared service. |
| offer_id | string (FK → Offer) | Offer (02) / Sales (05) | Offer being tested. |
| pilot_state | enum | Sales (05) / Client Success (07) | active-target → CRM-registered → outreach-ready → discovery-open → pilot-running → validated → closed / archived. |
| proof_required | text | Offer (02) / Sector (01) | What evidence would validate the pilot. |
| identity_storage_ref | string | Governance (00) | Pointer to private identity record. |

### Invoice / Revenue Event
| Field | Type | Set by | Notes |
|---|---|---|---|
| invoice_id | string | Finance (09) | |
| client_id | string (FK) | Finance (09) | |
| project_id | string (FK, nullable) | Finance (09) | Null for retainer-only billing not tied to a specific project |
| amount, currency | number, string | Finance (09) | |
| status | enum | Finance (09) | draft → sent → paid → overdue → written-off |
| revenue_recognition_date | date | Finance (09) | |

### Partner
**Added 2026-06-30** — gap found during ClientPartner Acquisition (06) content migration: that department's source material defines a full parallel Partner pipeline with no analog in the original 5-object schema above (which only models client-side flow). A partner is fundamentally not a Lead/Opportunity/Client — it's a distribution/leverage relationship, not a revenue-extraction one (see `06_ClientPartner_Acquisition/CLIENTPARTNER_OS.md` §1 for the full client-vs-partner distinction this schema follows).

| Field | Type | Set by | Notes |
|---|---|---|---|
| partner_id | string | System | |
| partner_type | enum | ClientPartner Acquisition (06) | distribution, capability, credibility, strategic, capital, ecosystem |
| stage | enum | ClientPartner Acquisition (06) | ecosystem-mapping → relationship-initiated → strategic-assessment → capability-validation → co-value-modeling → integration-planning → pilot-engagement → active-partnership → expansion / dormant / terminated |
| fit_score | number | ClientPartner Acquisition (06) | Composite of audience alignment, trust level, distribution strength, incentive compatibility, operational compatibility, brand alignment, strategic value |
| incentive_model | enum | ClientPartner Acquisition (06) | referral, affiliate, strategic-alliance, joint-venture, white-label |
| revenue_share_terms | text | ClientPartner Acquisition (06) + Finance (09) | Not a fixed schema field — terms vary by incentive model; governed by Legal (10) once real |
| sourced_opportunity_ids | array (FK → Opportunity) | System | Tracks which Opportunities this partner sourced, for attribution |
| trust_score | number | ClientPartner Acquisition (06) | Distinct from Client `health_score` — partner trust is relationship-based, not delivery-satisfaction-based |

## Object Relationships

```
Company --(parent_of / contains_unit)--> Company
Company --(has role)--> Lead / Client / Partner / Competitor
Lead --(converts to)--> Opportunity --(closes won)--> Client --(scopes)--> Project --(bills)--> Invoice
                            ^                            |
                            |                       (governed by)
                     (sources)                            v
                            |                         Contract (Legal, 10)
                       Partner --(parallel pipeline, see ClientPartner_OS §4)
Pilot Engagement --(tests offer with)--> Company + Offer
```

A Partner doesn't move through the Lead→Opportunity→Client chain itself — it sits alongside it and can *source* Opportunities (tracked via `sourced_opportunity_ids`), distinct from being one.

## Handoff Points (where this schema enforces accountability)

| Handoff | From | To | What must transfer |
|---|---|---|---|
| Lead → Opportunity | Marketing (03) / Content (04) / ClientPartner Acquisition (06) | Sales (05) | source, ICP_fit_score, all touch history |
| Opportunity → Client | Sales (05) | Client Success (07) | deal_value, scope commitments made during sale, contract_id |
| Client → Project | Client Success (07) | Operations (08) | scope_summary, sla_target_date |
| Project → Invoice | Operations (08) | Finance (09) | completed milestones/deliverables triggering billable events |
| Partner → sourced Opportunity | ClientPartner Acquisition (06) | Sales (05) | partner_id attribution, incentive_model (for later revenue-share calculation) |

This table is the seed of the "Handoff packet standards" item in `GLOBAL_OS.md` §11 (item 6) — each row above should eventually become a fuller handoff packet spec once real workflows are built per department.

## Platform selection

**Confirmed by owner, 2026-07-01: ClickUp** (supersedes the Zoho CRM selection below). Reason given: free tier. ClickUp implements the object model in this file via Lists, custom fields, and pipeline views — the schema's objects (Lead, Opportunity, Client, Partner) map to ClickUp Lists; custom fields carry all the typed field values; stages map to ClickUp statuses or a dropdown field.

**Accounting platform: Zoho Books (re-confirmed and connected 2026-07-01)** — supersedes QuickBooks, which briefly superseded Zoho Books earlier the same day. Reason for the reversal: attempting the real QuickBooks connection confirmed a genuine paid subscription and business registration are required before any integration can even authenticate — no free/trivial tier exists, unlike ClickUp. The owner reverted to Zoho Books and connected it via claude.ai's Zoho Books connector — `list_organizations` confirmed a **real, pre-existing organization** (created 2026-06-26, before this session): ID `929138528`, "Arika Agency," Kenya, base currency **KES**, Premium Trial plan — **⚠️ which has since EXPIRED (`is_trial_expired: true`, live-verified 2026-07-15). The owner reverted here for a free tier; the org is not on the free tier, it is on a lapsed trial.** Note `isOrgActive: true` still reads true alongside it — do not read "active" as "fine." See `13_Tech_Stack/TECHSTACK_OS.md` §9. This connector exposes direct MCP tools (`create_invoice`, `create_contact`, etc.), so the Opportunity-closed-won → Invoice handoff can call Zoho Books directly rather than needing a native ClickUp↔Zoho app or Zapier. **Real currency decision**: offers stay priced in USD (`02_Offer/OFFER_OS.md`'s catalog), but invoices are issued in KES via a conversion calculator at invoice time (not yet built — exchange-rate source undecided, see `GO_LIVE_CHECKLIST.md` item 9). See `13_Tech_Stack/TECHSTACK_OS.md` and `00_Agency_Governance/GO_LIVE_CHECKLIST.md` items 2, 4, 9 for the full history.

**Real implementation, 2026-07-01:** the 5 non-Invoice objects that existed at the time (Lead, Opportunity, Client, Engagement/Project, Partner) now exist as real ClickUp Lists — created via a ClickUp MCP connector in a dedicated "Arika Agency CRM" folder, kept separate from the workspace's pre-existing (unused) "Sales CRM" template. **Every custom field in those 5 Core Objects tables is live** on its matching List, built via direct ClickUp REST API calls (owner-provided personal token) — including the cross-object FK relationships (Opportunity→Lead, Client→Opportunity, Engagement/Project→Client, Partner→Sourced Opportunities) as real ClickUp `list_relationship` fields, not just typed text. **Status pipelines now fully live too (2026-07-01).** The personal API token could not write list statuses (confirmed real limitation — a status-update call returned success but silently left them unchanged). Creating a ClickUp OAuth App and completing the authorization flow produced a different token that **could** write statuses, once each list's status array included exactly one `open`-type and one `closed`-type status (a real ClickUp validation rule). All 5 `stage`/`lifecycle_stage` enums from the 2026-07-01 build are real ClickUp status pipelines, independently re-verified via API. **2026-10-02 extension:** `Company / Organization Level` and `Pilot Engagement` are now canonical schema objects, but their ClickUp Lists/relations are **not yet confirmed live**; create/verify them before claiming a real active pilot record exists. Custom-field rename/delete remains blocked under both token types with an identical `"Access denied for updating field api"` error — a hard platform lock, not solved by switching auth methods. Invoice has no ClickUp List by design — it's the object the **accounting platform** owns once the sync (`GO_LIVE_CHECKLIST.md` item 4) is live. **🔴 Corrected 2026-07-15: this read "the object QuickBooks owns"** — a stale reference that survived the 2026-07-01 QuickBooks→Zoho Books reversal *documented two paragraphs above it*, and sat contradicting its own section for 14 days. **The platform is Zoho Books.** ⚠️ **And as of a live `list_organizations` check on 2026-07-15, Zoho Books' Premium Trial has expired** (`is_trial_expired: true`; org created 2026-06-26; `13_Tech_Stack/TECHSTACK_OS.md` §3, §9). **This schema's accounting-owned Invoice object currently sits on a lapsed plan.** Owner decision: downgrade to Zoho's free tier, pay, or re-open the accounting choice. Full detail and List/field IDs: `00_Agency_Governance/GO_LIVE_CHECKLIST.md` Phase 1 items 3 and 5.

*Superseded, 2026-07-01:* ~~Confirmed by owner, 2026-06-30: Zoho CRM. Reason: pairing with Zoho Books for native CRM↔Books sync.~~

*Original entry, superseded same day 2026-06-30:* ~~Confirmed by owner, 2026-06-30: HubSpot.~~

## Sector (01) → CRM bridge (reference; no new object) — *added 2026-08-19*

Sector's commercial-activation loop (`01_Sector/SECTOR_ACTIVATION_CONTRACT.md` §14) ends **in this CRM**, not in a parallel store. Sector does **not** create a contact/company object — it **tags and routes onto the objects above**:

- **On `Company`:** `structure_type`, `entity_level`, parent/child links, `sector`, `sub_sector`, and `roles[]`.
- **On `Lead`:** `company_id`, `target_company_level_id`, `sector`, `sub_sector`, `icp_tier` (from Sector's ICP Classification), and the matched entry-`offer_id` — so a scraped decision-maker lands already classified and offer-matched. `ICP_fit_score` stays Sales-set.
- **On `Opportunity`:** `company_id`, `target_company_level_id`, and `offer_id` — the Industry-Offer-Matrix entry offer for that sub-sector (the land-and-expand ladder's first rung).
- **Per-sector Ideal Target Profile** (firmographics + trigger + entry-offer + outreach angle) is assembled by Sector as the "who we'd approach and with what" spec that seeds outreach — the actual script/proposal is owned by **Sales (05) + Content (04)**, not Sector.

> ✅ **Created and verified 2026-09-29.** All four — `sector`, `sub_sector`, `icp_tier` (dropdown: Tier 1 · Tier 2 · Tier 3 · Anti-ICP · Out-of-scope) and `offer_id` — now exist on the live `Lead` list, optional and empty, created under authorisation `CRM-PROV-1` with an audit record. **Round-trip verified 2026-09-29, twice:** SECTOR-CW2 by a direct connector call, then SECTOR-SF2 with **Sector's S10 skill performing the write itself** — each on one disposable task that was tagged, read back and deleted. The mechanism works. **No real `Lead` has ever been tagged**, so no hand-off has been observed arriving and delivery stays unproven. *(Was, 2026-09-22: none of the four existed, so the route had no target field at all.)* S10's route table is corrected to match (`DESIGNED`, not `CONNECTED`). Creating the four fields is a write and needs its own decision. `ICP Fit Score` exists but is **not** Sector's `icp_tier`: it is a number (the DB 5 prospect score), while `icp_tier` is a DB 4 classification that requires a rationale, and a score cannot express `Anti-ICP` or `Out-of-scope`. *(Corrected 2026-09-22: an earlier note here called it “Sales-set”, repeating line 23 above — **AEIT_05 R1, ratified 2026-07-22, puts Sector (01) as the setter and Sales as the consumer.** That line stays as written; its fix is queued under `AEIT_10` Phase Zero.)* A drafted, unenacted proposal for the four fields is in `SECTOR_OS.md` §8, SECTOR-CRM1. Target/schema existence only; delivery not tested.

**Honesty gate:** real `Lead` rows (contact_name/email/company) are **gated on scraping** (paid people-data MCP + Legal + cost governance + Approval-Matrix row — `AEIT_08` §3.1/§5). Until then the bridge is a **field mapping + template**; no contact is ever fabricated.

**2026-10-03 source-specific clarification:** the named-person scraping/enrichment gate above stays closed. The owner-requested public-company cycle uses official websites and published company routing channels only, with evidence and exact draft messages outside Git. A public channel is not consent, a qualified lead or verified authority. No API/CRM write is claimed: locally reserved `ORG-*` identities remain pending CRM deduplication and the existing bridge's live mapping must be read before use. Do not copy Hospitality's legacy SaaS `out_of_scope` transport value to `icp_tier`; retain the Hospitality verdict/route in a reviewed Lead description until fields are verified. See `05_Sales/PROSPECTING_CYCLE.md` for the owner's drafts-only decision and actual outcome.

### Hospitality pilot activation rule — added 2026-10-02

Owner direction authorizes pursuing real Hospitality targets, not fictional companies. A target is not thereby an agreed or running pilot. The repo still must not store real target names or contact details in markdown. The activation path for a specific pilot is:

1. Create / verify the root `Company` in CRM or private identity storage (`ORG-*`, `structure_type = GRP` if the target is the hotel group).
2. Create child `Company` rows only as needed and only when sourced: properties/branches (`entity_level = property` or `branch`), shared services (`central reservations`, loyalty, group revenue/marketing), and outlets (`restaurant`, `bar`, `spa`, `MICE/conference`).
3. Create a `Pilot Engagement` (`PILOT-*`) that points at the exact level being tested: group-level, one property/branch, or one outlet/service.
4. Attach each `Person` to the Company level they decide for. A group revenue director, a property GM, and an outlet manager are separate decision scopes.
5. Preserve namespaces: `SIM-*` for simulations, `ORG-*` for organizations, `PER-*` for people, `PILOT-*` for pilot engagements. A simulation can inform a pilot, but it never becomes the pilot record.

**Qualification rule:** a group or central brand/revenue team is not an automatic stop. It qualifies when the buyer level is explicit and the offer routes to that level. A property can be a client while the group remains a prospect elsewhere; an outlet can carry a different sector/sub-sector tag from its parent.

## What this schema deliberately does not specify

- Field-level validation rules, required vs. optional fields in practice, or UI/form design — those follow once ClickUp implementation begins (Tech Stack, 13; see `00_Agency_Governance/GO_LIVE_CHECKLIST.md`).
- Historical/legacy data migration — not applicable until real client data exists to migrate.

## Changelog

- 2026-10-03: Separated a sourced prospect identity, verified CRM registration and an agreed pilot engagement. Recorded the public-company preparation route without opening the named-person scraping gate; Hospitality fit is not the SaaS dropdown. The actual batch remains drafts-only by owner direction, with no verified CRM delivery.

- 2026-10-02 — **Company / Organization Level and Pilot Engagement added for active pilot work.** The Hospitality pilot is now represented as a real organization structure in CRM terms without naming the target in repo markdown. Added `ORG-*` / `PER-*` / `PILOT-*` / `SIM-*` namespace discipline, group/property/outlet parent-child modeling, and exact target-level fields on Lead, Opportunity, and Project. — Codex
- 2026-09-29 — **S10 itself exercised the `Lead` tag write (SECTOR-SF2).** One disposable fixture task took all four governed tags, returned them unchanged on read-back and was deleted, with its absence confirmed. Recorded under the fixture-only outcome `delivered_fixture_verified`, never `delivered`. Three of the four values were explicit `TEST_FIXTURE` placeholders, because Sector's pinned record carries names rather than ids and no ICP tier; `icp_tier` was `Out-of-scope`. **No real `Lead` was tagged**, CRM readiness is unchanged and `offer_id`'s production format is still undefined. — Claude Code (Opus 5)
- 2026-09-29 — **The `Lead` tag mechanism is round-trip verified (SECTOR-CW2).** One synthetic task took all four values — including `icp_tier` resolving to the approved `Out-of-scope` option — and returned them unchanged; it was deleted and its absence confirmed, and the list schema is untouched. **S10 was not run**, so nothing has been delivered. **Correction worth keeping:** the list-scope custom-field endpoint does **not** return `list_relationship` fields — the task view shows an `Opportunity` relationship this file already documents from 2026-07-01 — so field counts taken from that endpoint under-report the schema. — Claude Code (Opus 5)
- 2026-09-29 — **The four Sector bridge fields now exist on the live `Lead` list**, created by the governed provisioner under `CRM-PROV-1` and verified by a separate connector call: three text fields plus `icp_tier` as a dropdown carrying DB 4's exact five values. The six pre-existing fields are unchanged and none of the four is required. Field existence only — no value has been written, and the Sector-to-CRM route stays `HANDOFF_FAILURE` until a round-trip test passes. `offer_id`'s content stays an Offer (02) decision. — Claude Code (Opus 5)
- 2026-09-23 — **Field provisioning moved onto a governed path.** Adding a CRM custom field is now declared in `crm_provisioning/clickup-field-spec.json` (with the contract that authorises it) and created by `provision_clickup_fields.py` under a per-run owner authorisation, with an audit record and an Automation Approval Matrix row. The same file is where **any** department's CRM fields belong — Sales (05), ClientPartner (06), Client Success (07), Operations (08) and Finance included — each needing its own contract citation and its own owner decision. Only Sector's four bridge fields are declared so far, and none has been created yet. — Claude Code (Opus 5)
- 2026-09-22 — **`Lead`'s live custom fields read and recorded (owner-authorised, one read-only schema call).** Six exist: Source, Source Campaign, Contact name, Contact Email, Company, ICP Fit Score. **Corrections:** `lead_id` and `last_touch_at` are **not** custom fields (native ClickUp id and timestamp), so the 2026-07-01 claim that every Core-Objects field is live on its List is too broad for `Lead`; the live `Source` dropdown **omits `inreach`**; and **none of the four Sector bridge tag fields exists**, so that bridge stays a mapping and S10's CRM route has no target. Target/schema existence only; delivery not tested. Only `Lead` was read — the other four Lists are unverified. — Claude Code (Opus 5)

- 2026-07-01 — **Zoho Books confirmed real and connected** — pre-existing org (created 2026-06-26), ID `929138528`, Kenya, KES base currency, Premium Trial. Real decision: USD offer pricing, KES invoicing via conversion calculator. — Claude Code (Sonnet 5)
- 2026-07-01 — **QuickBooks reverted to Zoho Books.** Real QuickBooks connection attempt confirmed a paid subscription/business registration is required before authentication is even possible — no free tier. Owner reverted to Zoho Books, re-superseding the same-day QuickBooks decision. — Claude Code (Sonnet 5)
- 2026-07-01 — **All 5 status pipelines built and verified**, via a ClickUp OAuth App token (personal token could not do this — confirmed). Field rename/delete confirmed blocked under both token types — hard platform limitation. — Claude Code (Sonnet 5)
- 2026-07-01 — **All custom fields built** across all 5 Lists via direct ClickUp REST API calls, including cross-object FK relationship fields. Confirmed (by direct API test) that ClickUp does not support status-workflow editing via API — remains the one genuine manual step. — Claude Code (Sonnet 5)
- 2026-07-01 — **Real ClickUp Lists created** for Lead, Opportunity, Client, Engagement/Project, and Partner via a ClickUp MCP connector — see "Platform selection" above and `GO_LIVE_CHECKLIST.md` Phase 1 item 3 for List IDs. Statuses/custom fields still pending (owner action, UI-only). — Claude Code (Sonnet 5)
- 2026-06-30 — Initial CRM schema created as part of governance-closure pass: core objects (Lead, Opportunity, Client, Engagement/Project, Invoice), relationships, and handoff points defined.
- 2026-06-30 — Added Partner object and the Partner→sourced-Opportunity handoff, following a gap found during ClientPartner Acquisition (06) content migration: that department's source material (`CRM System Architure. raft 13.md`) defines an 11-stage Partner pipeline that had no home in the original client-only schema.
- 2026-06-30 — Owner confirmed CRM platform: HubSpot (tracker item 5, resolved). — Claude Code (Sonnet 4.6)
- 2026-07-01 — **ClickUp supersedes Zoho CRM** as the CRM platform — owner decision, free tier. Consequence: Zoho Books' native-sync rationale no longer holds; accounting platform re-opened as a gap. See "Platform selection" above. — Claude Code (Sonnet 4.6)
- 2026-06-30 — **Superseded the same day**: owner switched CRM platform from HubSpot to **Zoho CRM**, to pair with **Zoho Books** for Finance. See "Platform selection" above. — Claude Code (Sonnet 4.6)
- 2026-06-30 — Added `lifecycle_stage`, `relationship_status`, `churn_reason`, and `offboarding_type` fields to the Client object, supporting Client Success's new Retention/Expansion/Advocacy/Offboarding/Re-entry workflow build-out (`07_Client_Success/CLIENTSUCCESS_OS.md` §4, §10). Resolves tracker item 24. — Claude Code (Sonnet 4.6)
