# CRM Schema (Marketing/Content → Sales → Client Success → Finance)

**Status:** v0.1-draft — structural schema, not yet implemented in any real CRM tool.
**Last updated:** 2026-06-30

> Referenced from [`GLOBAL_OS.md`](../GLOBAL_OS.md) §11 (closes "Required Agency-Wide Closure Systems" item 4). This is the canonical object model every department's tooling should converge toward — it does not assume any specific CRM platform (that selection belongs to Tech Stack, `13_Tech_Stack/TECHSTACK_OS.md`).

---

## Why this exists

Marketing/Content, Sales, Client Success, and Finance all touch the same underlying entities (a prospect becomes a lead becomes an opportunity becomes a client becomes a billing account) but without a shared schema, each department's raw drafts independently reinvented a slightly different model. This file is the single object model all of them should reference.

## Core Objects

### Lead
| Field | Type | Set by | Notes |
|---|---|---|---|
| lead_id | string | System | Unique identifier |
| source | enum | Marketing (03) / Content (04) / ClientPartner Acquisition (06) / Presence (21) | inbound, outbound, referral, partner, event, inreach |
| source_campaign | string | Marketing (03) / Content (04) | Which campaign/content piece generated this lead |
| contact_name, contact_email, company | string | Marketing (03) / Content (04) | Raw capture data |
| ICP_fit_score | number | Sales (05) | Qualification scoring, see Constitution §5 for any automation risk-class implications |
| stage | enum | Sales (05) | new → contacted → qualified → opportunity → closed-won / closed-lost |
| created_at, last_touch_at | datetime | System | |

### Opportunity
| Field | Type | Set by | Notes |
|---|---|---|---|
| opportunity_id | string | System | |
| lead_id | string (FK) | System | Links back to originating Lead |
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
| scope_summary | text | Client Success (07) → Operations (08) handoff | What was agreed |
| status | enum | Operations (08) | scoped → in-delivery → review → complete |
| sla_target_date | date | Operations (08) | |

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
Lead --(converts to)--> Opportunity --(closes won)--> Client --(scopes)--> Project --(bills)--> Invoice
                            ^                            |
                            |                       (governed by)
                     (sources)                            v
                            |                         Contract (Legal, 10)
                       Partner --(parallel pipeline, see ClientPartner_OS §4)
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

**Real implementation, 2026-07-01:** the 5 non-Invoice objects (Lead, Opportunity, Client, Engagement/Project, Partner) now exist as real ClickUp Lists — created via a ClickUp MCP connector in a dedicated "Arika Agency CRM" folder, kept separate from the workspace's pre-existing (unused) "Sales CRM" template. **Every custom field in the Core Objects tables above is now live** on its matching List, built via direct ClickUp REST API calls (owner-provided personal token) — including the cross-object FK relationships (Opportunity→Lead, Client→Opportunity, Engagement/Project→Client, Partner→Sourced Opportunities) as real ClickUp `list_relationship` fields, not just typed text. **Status pipelines now fully live too (2026-07-01).** The personal API token could not write list statuses (confirmed real limitation — a status-update call returned success but silently left them unchanged). Creating a ClickUp OAuth App and completing the authorization flow produced a different token that **could** write statuses, once each list's status array included exactly one `open`-type and one `closed`-type status (a real ClickUp validation rule). All 5 `stage`/`lifecycle_stage` enums above are now real ClickUp status pipelines, independently re-verified via API. Custom-field rename/delete remains blocked under both token types with an identical `"Access denied for updating field api"` error — a hard platform lock, not solved by switching auth methods. Invoice has no ClickUp List by design — it's the object the **accounting platform** owns once the sync (`GO_LIVE_CHECKLIST.md` item 4) is live. **🔴 Corrected 2026-07-15: this read "the object QuickBooks owns"** — a stale reference that survived the 2026-07-01 QuickBooks→Zoho Books reversal *documented two paragraphs above it*, and sat contradicting its own section for 14 days. **The platform is Zoho Books.** ⚠️ **And as of a live `list_organizations` check on 2026-07-15, Zoho Books' Premium Trial has expired** (`is_trial_expired: true`; org created 2026-06-26; `13_Tech_Stack/TECHSTACK_OS.md` §3, §9). **This schema's 6th core object currently sits on a lapsed plan.** Owner decision: downgrade to Zoho's free tier, pay, or re-open the accounting choice. Full detail and List/field IDs: `00_Agency_Governance/GO_LIVE_CHECKLIST.md` Phase 1 items 3 and 5.

*Superseded, 2026-07-01:* ~~Confirmed by owner, 2026-06-30: Zoho CRM. Reason: pairing with Zoho Books for native CRM↔Books sync.~~

*Original entry, superseded same day 2026-06-30:* ~~Confirmed by owner, 2026-06-30: HubSpot.~~

## What this schema deliberately does not specify

- Field-level validation rules, required vs. optional fields in practice, or UI/form design — those follow once ClickUp implementation begins (Tech Stack, 13; see `00_Agency_Governance/GO_LIVE_CHECKLIST.md`).
- Historical/legacy data migration — not applicable until real client data exists to migrate.

## Changelog

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
