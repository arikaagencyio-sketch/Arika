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
| source | enum | Marketing (03) / Content (04) / ClientPartner Acquisition (06) | inbound, outbound, referral, partner, event |
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

## Object Relationships

```
Lead --(converts to)--> Opportunity --(closes won)--> Client --(scopes)--> Project --(bills)--> Invoice
                                                          |
                                                    (governed by)
                                                          v
                                                       Contract (Legal, 10)
```

## Handoff Points (where this schema enforces accountability)

| Handoff | From | To | What must transfer |
|---|---|---|---|
| Lead → Opportunity | Marketing (03) / Content (04) / ClientPartner Acquisition (06) | Sales (05) | source, ICP_fit_score, all touch history |
| Opportunity → Client | Sales (05) | Client Success (07) | deal_value, scope commitments made during sale, contract_id |
| Client → Project | Client Success (07) | Operations (08) | scope_summary, sla_target_date |
| Project → Invoice | Operations (08) | Finance (09) | completed milestones/deliverables triggering billable events |

This table is the seed of the "Handoff packet standards" item in `GLOBAL_OS.md` §11 (item 6) — each row above should eventually become a fuller handoff packet spec once real workflows are built per department.

## What this schema deliberately does not specify

- Which CRM platform implements it (HubSpot, Pipedrive, Salesforce, etc.) — that's a Tech Stack (13) decision.
- Field-level validation rules, required vs. optional fields in practice, or UI/form design — those follow once a platform is chosen.
- Historical/legacy data migration — not applicable until real client data exists to migrate.

## Changelog

- 2026-06-30 — Initial CRM schema created as part of governance-closure pass: core objects (Lead, Opportunity, Client, Engagement/Project, Invoice), relationships, and handoff points defined. — Claude Code (Sonnet 4.6)
