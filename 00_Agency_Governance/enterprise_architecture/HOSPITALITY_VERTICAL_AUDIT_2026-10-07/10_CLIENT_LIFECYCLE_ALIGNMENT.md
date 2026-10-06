# 10 — Client Lifecycle Alignment: prospect → client → retention

**Protocol §15:** for every stage of *prospect → qualification → discovery → audit → strategy → proposal → negotiation → contract → onboarding → strategy → campaign → production → distribution → reporting → review → renewal → expansion*, identify owner, input, output, approval, system record, SLA, decision gate and next stage — and the missing handoffs.

The Hospitality offer already engineers a **17-stage client journey** (Draft 41 §6) that maps almost one-to-one onto the protocol's list. This file uses it as the spine and marks where the rest of the OS does or does not support each stage.

---

## 1. Stage-by-stage

`Owner` = the functional role (all resolve to Mary Thuo today — Constitution §4). `Record` = the system of record that would prove the stage happened.

| # | Protocol stage | Draft 41 stage | Owner | Input | Output | Approval | System record | SLA | Decision gate | State |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Prospect | (pre-1) | Sector (observe) → Sales | Public evidence | `ORG-*` tree + ID-only queue | Owner reviews each exact message (Class 3 to send) | Outside-Git queue → CRM `Company`/`Lead` (**not written**) | none | `prospecting_cycle.validate()`; PG1 stop rules | `LIVE` once |
| 2 | Qualification | 2 Qualification | Sales decides; Sector sets fit (R1) | Archetype, destination, H-band, website, booking path, group structure | Fit verdict + `offer_route` | — (Class 1) | Queue `fit`; CRM Lead description (Hospitality fields not mapped) | none | Stop rules (overlay §2) | Applied by code |
| 3 | Discovery | 1 Discovery | Sales / owner | S2 conversation guide (overlay §4) | S2 answers | **ID3** — owner decision to approach | Client folder intake file; Opportunity `discovery` | none | *Buyer acknowledges OTA dependency worth diagnosing* | `DESIGNED` |
| 4 | Audit | 3 Audit | Audit Analyst → Senior Diagnostic Reviewer | MD1–MD8 (client exports, interview) | M1 snapshot, M2 (a)–(d) verdict, M7 redirect | Senior review (QG1); client readout | **none designated** (client folder) | duration **open** (#13) | QG1 + data-sufficiency rule (MD1 & MD4 required) | ⛔ **BLOCKED** — S3 needs a signed engagement, a legal path (G5) and an NDA answer |
| 5 | Strategy | 4 Strategy | Revenue-Content Strategist | Signed verdict | Per-client target + narrative (D2 / M3) | Client sign-off | none | none | Only if (a) or messaging-(b) dominant | `DESIGNED` |
| 6 | Proposal | 5 Proposal | Sales / owner | Scope + price | Proposal | Class 3 | CRM Opportunity `proposal` | none | **QG5 — no price exists** | ⛔ **BLOCKED** (Phase 11) |
| 7 | Negotiation | — (implicit) | Sales (`sales-execution-closing`) | Proposal | Agreed terms | Class 3 | Opportunity `negotiation` | none | Credit policy, risk reversal — **unapproved** | `DESIGNED` (enum only) |
| 8 | Contract | 6 Agreement | Legal → owner | MSA/SOW/DPA | Signed instrument | **Class 4** (Constitution §5) | `Client.contract_id` | none | Counsel-reviewed templates | ⛔ **BLOCKED** (item 59) |
| 9 | Onboarding | 7 Onboarding + 8 Asset Collection | Client Success → Operations | Signed scope | Named approver + data owner; communication charter; verified access; consent status per list | Client | `Client.onboarding_status`; `SCOPE_DEFINED` | none | Access verified live; consent known | `DESIGNED`; S4 blocked |
| 10 | Strategy (delivery) | 9 Implementation (planning) | Strategist | D2 | D3 revenue-year calendar | Client | **none** — Content DB 4/7 cannot hold a client (`HV-11`) | none | Measurement window + seasonal baseline agreed *before build* | `DESIGNED` |
| 11 | Campaign | 9 Implementation | Strategist / Content | D3 | Need-date campaigns | Client per piece | **none** (same) | none | QG2/QG3/QG7 | `DESIGNED` |
| 12 | Production | 9 Implementation | Content Producer / Copywriter / Design | D3, brand assets | D4 content (**excluded from MVP**), D5 / M4 blueprint with sample copy | Client per piece | Design Canva (agency-only structure) | none | QG2, QG3, QG7; Design AI-artifact gate | `DESIGNED` |
| 13 | Distribution | 12 Delivery | the client (MVP has no implementation) | Approved assets | Live assets on the client's channels | Client | — | none | Delivery QA | Out of MVP scope |
| 14 | Reporting | 13 Reporting | Reporting Analyst | Client system data | D7 monthly pack — **retainer deferred**; MVP has M6 plan only | Account Lead | **no store** | monthly (D7) | QG6 — client-system data only | `DESIGNED`; S5 blocked |
| 15 | Review | 10 Review · QBR | Account Lead | Deliverables | Approved/revised deliverables | Client within window | **none** (`HV-09`) | **windows open** | One included revision round per M1–M7 (MVP policy) | `DESIGNED` |
| 16 | Renewal | 15 Retention | Client Success | Health, measured value | Renewal decision | Owner / client | `Client.lifecycle_stage`, `relationship_status` | none | Value recap from **measured** data only | `DESIGNED` |
| 17 | Expansion | 17 Expansion | Client Success → Sales | Re-audit | Qualified expansion opportunity | — | New Opportunity | none | **Re-audit only**; expansion rungs **unengineered** | `DESIGNED` |
| (+) | Offboarding | 14 Offboarding | Client Success | Contract end / churn | Handover, access revoked, data returned/deleted | Owner | `churn_reason`, `offboarding_type` | none | 10-step offboarding | `DESIGNED` |
| (+) | Referral | 16 Referral | Client Success | Consented, measured evidence | Testimonial / case evidence | Client consent; Legal for claims | — | none | Proof method **BLOCKED** | `DESIGNED` |

**SLA column:** empty everywhere. Draft 41 §9 #14 records *"SLA durations, approval windows, min/ideal/aggressive timelines"* as open; only the MVP revision policy is decided. Operations records *"SLA templates remain theory-only"* (`OPERATIONS_OS.md` §15). → part of `HV-26`.

## 2. Missing handoffs

| From → To | Why it is missing | Class | Priority |
|---|---|---|---|
| Audit → Proposal | No price (Phase 11) | DATA GAP (human input) | P1 |
| Proposal → Contract | No counsel-reviewed contract; s.48 transfers undocumented | GOVERNANCE GAP (external) | **P0** for any client-data stage |
| Approval → system of record | No deliverable approval record | WORKFLOW GAP | P1 |
| Strategy/Campaign/Production → a client | Content and Design stores carry no client | DATA GAP | P1 |
| Reporting → anything | No performance store; S5 blocked | METRIC GAP | P2 (P1: M6 in the client folder) |
| Audit redirect → an offer | (c)/(d)/technical-(b) destinations unengineered | WORKFLOW GAP | P1 (honest redirect text) / P2 (offers) |
| Expansion → an offer | P11 Expansion 1/2/Transformation unengineered | NEW (OEOS) | P3 |
| Group → property → outlet engagement | No group/portfolio offer; union operator unbuilt | WORKFLOW GAP + decision | **P0 decision** (`HD-01`) |

## 3. Competing lifecycle models — a crosswalk, not a deletion

At least seven lifecycle or journey models are live in the repository. Client Success declared one canonical on 2026-06-30, but later documents introduced others without mapping them. None is wrong; they operate at different altitudes. What is missing is the **crosswalk**, so an agent or a person can translate between them. → `HV-22`.

| Protocol (17) | Draft 41 journey (17) | Client Success canonical (9) | CRM SM3 → SM1 states | Company profile lifecycle (11) | Intake stage | Sector engagement model (7, Tier 1 SaaS) |
|---|---|---|---|---|---|---|
| Prospect | — | Awareness | observed → scored → ICP-classified | Awareness | S1 | — |
| Qualification | 2 Qualification | Interest/Consideration | lead → qualified | Interest · Engagement · Qualification | S1 | Pain Discovery |
| Discovery | 1 Discovery | Interest/Consideration | opportunity | Engagement | S2 | Pain Discovery |
| Audit | 3 Audit | Conversion | opportunity | Qualification | S3 | Revenue Audit |
| Strategy | 4 Strategy | Conversion | opportunity | — | S3 | — |
| Proposal | 5 Proposal | Conversion | proposal | Conversion | — | — |
| Negotiation | — | Conversion | negotiation | Conversion | — | — |
| Contract | 6 Agreement | Conversion | won → Client | Conversion | S4 | — |
| Onboarding | 7 + 8 | Onboarding | `onboarding` | Onboarding | S4 | Quick Win (30 days) |
| Strategy → Production → Distribution | 9 Implementation · 11 Optimization · 12 Delivery | Delivery | `delivery` | Delivery | — | System Install |
| Reporting · Review | 13 Reporting · 10 Review | Delivery / Retention | `delivery` | Delivery | S5 | Optimization Loop |
| Renewal | 15 Retention | Retention | `retention` | Retention | S5 | Ongoing Partnership |
| Expansion | 17 Expansion | Expansion | `expansion` | Expansion | — | Ongoing Partnership |
| (referral) | 16 Referral | Advocacy | `advocacy` | Referral → Partnership | — | Handoff + Training (referrals 2+/12 mo) |
| (exit) | 14 Offboarding | (cross-cutting) | `offboarding` → re-entry | — | — | — |

**Recommendation (`HD-13`):** keep Client Success's 9-stage model as the agency-wide canonical lifecycle, publish this crosswalk beside it, and let offer-level journeys (like Draft 41's) stay as more detailed, offer-specific expansions. Delete nothing.
