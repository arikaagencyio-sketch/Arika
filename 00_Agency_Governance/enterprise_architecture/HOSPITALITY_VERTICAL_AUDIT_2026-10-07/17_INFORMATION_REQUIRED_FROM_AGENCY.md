# 17 — Information Required from Agency

**Protocol §28:** *"Do not invent missing agency information… write UNKNOWN — HUMAN INPUT REQUIRED, then explain exactly why it matters."* Every item below is something this audit could not discover from the repository. Where the repository already holds a partial answer, it is cited so the owner is not asked twice.

**How to use this:** answer in any order; each answer that is a decision should be recorded as a dated entry (file 18 lists the decisions). Items marked ★ block the pilot.

---

# INFORMATION REQUIRED FROM AGENCY

## A. Constitution

| ID | Question | Why it matters | Blocks | Already in repo |
|---|---|---|---|---|
| IR-A1 | Should the constitution be re-adopted now that the company is incorporated (it is still `v0.1-draft`, 2026-06-30, with a pre-launch contact line)? | It is the supreme document every agent reads | — | Constitution header, §2 |
| IR-A2 | Should *decide ≠ apply* and *runnable gates must pass before commit* become constitutional non-negotiables? | Both are practised but unwritten; their absence let HV-01 and HV-46 happen | HD-14, HD-17 | `AEIT_05`; memory |
| IR-A3 | Will anyone other than the owner ever sign off a Class 3 action during the pilot? | Approval records need a named approver | HD-06 | Constitution §4 (owner only) |

## B. Governance

| ID | Question | Why it matters | Blocks | Already in repo |
|---|---|---|---|---|
| ★ IR-B1 | Was the 2026-10-02 group/property/outlet reconciliation meant to be **applied** (it was, on 2026-10-03)? | It changed qualification rules used for real outreach | HD-17 | `GLOBAL_OS.md` v0.29.0 |
| IR-B2 | Should failing gates **block** the auto-sync push or only **warn**? | A red gate is on master now | HD-14 | `.claude/hooks/` |
| IR-B3 | Who keeps `OWNER_INPUT_NEEDED.md` current — and may sessions add items directly when they record a decision? | The tracker is three weeks behind | HV-07 | memory note: roll-up is manual |
| IR-B4 | Where should client-deliverable approvals be recorded — ClickUp Project fields or a register in the client folder? | Draft 41 requires approvals in a system of record | HD-06 | Draft 41 Phase 8 |

## C. Agency structure

| ID | Question | Why it matters | Blocks | Already in repo |
|---|---|---|---|---|
| ★ IR-C1 | Will anyone besides the owner work on the pilot (designer, videographer, copywriter, revenue-management adviser)? If so, as employee or contractor? | Capacity; the HR engagement-classification gate; approvals; data access | HD-01 | HR doctrine: next two people are counsel and an accountant |
| IR-C2 | What hospitality-specific experience does the owner bring (revenue management, hotel marketing, hotel operations)? | The audit verdict is *"senior-expert-only"* | HD-01 | Draft 41 Phase 12 |
| IR-C3 | Which department should own Pre-Experience (recommended: Content 04, with Design 19 producing)? | One owner per capability | HD-10 | file 11 §5 |

## D. Commercial model

| ID | Question | Why it matters | Blocks | Already in repo |
|---|---|---|---|---|
| ★ IR-D1 | Is the first hospitality engagement **paid**, an **unpaid design partnership**, or **discovery only**? | Determines whether Phase 11, a contract and an invoice are needed now | HD-04 | Draft 41 §5; worksheet §1.5 |
| ★ IR-D2 | If paid: the price band and commercial shape for audit + blueprint, and the audit-fee credit policy | Phase 11's missing inputs | HD-04 | item 71; worksheet §12 (hours bands, no money) |
| IR-D3 | Is Pre-Experience **sold** (a deliverable or its own offer), **demonstrated** only, or both? | Decides whether OEOS engineering is needed | HD-10 | — |
| IR-D4 | Should the Hospitality offer cover non-room revenue (F&B, spa, MICE, weddings, packages) during the pilot? | Decides whether P3 vocabularies and non-room measures are P1 or P2 | HD-08 | Draft 41 is rooms/direct-booking only |
| IR-D5 | Group/portfolio offer: engineer now, or after one property MVP is delivered? | The intended pilot is a group | HD-01 | A001 AG-7 |

## E. Client lifecycle

| ID | Question | Why it matters | Blocks | Already in repo |
|---|---|---|---|---|
| IR-E1 | Confirm Client Success's 9-stage model as the agency canonical, with a crosswalk to the others | Seven lifecycle models exist | HD-13 | `CLIENTSUCCESS_OS.md` §4 |
| IR-E2 | Pilot service levels: response time, review windows, turnaround per deliverable | SLAs are blank everywhere | HV-26 | Draft 41 §9 #14 (MVP revision policy only) |
| IR-E3 | At pilot end, what happens to the client's data and to generated assets (return, delete, retain)? | Offboarding and DPA terms | HD-05 | Draft 41 stage 14 |
| IR-E4 | On the client side, which role approves at group vs property vs outlet level? | Decision scope per level | HD-06 | `AEIT_06` `Person.decision_scope` (blueprint) |

## F. Prospecting

| ID | Question | Why it matters | Blocks | Already in repo |
|---|---|---|---|---|
| ★ IR-F1 | Release conditions for the three drafted first touches (edits, sender, DKIM, timing) — and may the website be linked once reconciled? | The only live acquisition path | HD-03 | `PROSPECTING_CYCLE.md` release table |
| IR-F2 | For the intended group: approach at group level, property level, or both in sequence? | Routes and decision scope differ | HD-01 | prospecting routes |
| IR-F3 | May a public-data desk profile (intake S1) be shared with a prospect as an outreach asset, and with what labelling? | Strongest honest proof available pre-engagement | HD-12 | claims policy Class D |
| IR-F4 | Which travel-trade or hospitality events, if any, will the owner attend in the next 12 months? | Plugin P7 already carries Arika's own attendance clock | — | plugin P7; DB 14 trade sources |
| IR-F5 | Confirm the named-person data gate stays closed for the pilot | Default is closed | — | `CRM_SCHEMA.md` honesty gate |

## G. Strategy

| ID | Question | Why it matters | Blocks | Already in repo |
|---|---|---|---|---|
| ★ IR-G1 | The exact sector statement for `GLOBAL_OS.md`, `SECTOR_OS.md` and the website (e.g. the company profile's *"B2B SaaS — founding sector; Hospitality — first activated sector; others mapped, not open"*) | Root and public surfaces contradict live strategy | HD-02 | company profile §8 |
| IR-G2 | Official positioning string: "Revenue Infrastructure Partner" vs the BRS "360° Growth Revenue Agency" | Open as LinkedIn decision L10 | — | company profile §17 |
| IR-G3 | Which hospitality types are in scope for the next six months: glamping, clubs, wedding venues, standalone restaurants, spas, conference venues? | Archetype vocabulary and P2 rules | HD-18 | plugin P2 |
| IR-G4 | Geography: Kenya-inbound only, or also domestic, regional (East Africa), outbound or diaspora markets? | Route scope; calendar clocks | — | owner decision 2026-08-19 (Kenya-inbound) |

## H. Marketing operations

| ID | Question | Why it matters | Blocks | Already in repo |
|---|---|---|---|---|
| IR-H1 | Which channels will carry agency self-marketing into hospitality (recommended: direct outreach + LinkedIn authority)? | Avoid opening channels for their own sake | — | file 09 §5 |
| IR-H2 | What publishing cadence can the owner sustain? | Solo capacity | — | — |
| IR-H3 | Who owns client-campaign measurement until a performance store exists? | Marketing owns measurement and has no store | HV-18 | `MARKETING_OS.md` §3 |
| IR-H4 | Who should own the Sector → Marketing / Operations route (item 31k)? | Two departments have no route from Sector | HV-20 | item 31k |

## I. Sales

| ID | Question | Why it matters | Blocks | Already in repo |
|---|---|---|---|---|
| IR-I1 | Discovery meeting format and the owner's real availability (which calendar tool?) | The cycle books from *"the owner's actual availability"* | — | `AEIT_04` D2 (no calendar/transcription tool) |
| IR-I2 | Proposal template and negotiation boundaries | Proposal stage blocked | HD-04 | — |
| IR-I3 | The DOSM's role in the buying process | Undefined in the offer | — | Draft 41 §9 #17 |
| IR-I4 | Is Day 0/2/5/9/14/21/30 the right follow-up cadence for hotels? | Cadence designed for B2B SaaS | — | `PROSPECTING_CYCLE.md` step 7 |

## J. Revenue

| ID | Question | Why it matters | Blocks | Already in repo |
|---|---|---|---|---|
| IR-J1 | Reconcile $35K/day with $1M/month (a 23–24 % gap) | Daily command reports the gap every run | — | `OPERATIONS_OS.md` §7 |
| ★ IR-J2 | Invoicing readiness: Zoho Books plan status, business bank account, USD→KES rate source | No paid pilot can be invoiced | HD-04 | GO_LIVE Phase 11 item 50; `CRM_SCHEMA.md` |
| IR-J3 | Client revenue measures: rooms only, or total revenue including F&B, spa, MICE? | Measurement scope | HD-08 | plugin P14 |
| IR-J4 | Which attribution method may be offered to clients (baseline comparison only; never causal claims)? | Draft 41 §9 #8 open | — | QG6; claims policy §8 |

## K. Creative

| ID | Question | Why it matters | Blocks | Already in repo |
|---|---|---|---|---|
| IR-K1 | How will a client's brand rules be received and stored (Canva tier, Brand Kit, client folder)? | Design checks only Arika's brand today | HD-15 | `DESIGN_OS.md` §10 |
| ★ IR-K2 | Adopt depiction rules V1–V9 (file 12 §5)? | No rule governs AI imagery of a real property | HD-16 | — |
| IR-K3 | Confirm "faceless" as a standing rule, not a style | Likeness risk | HD-16 | — |
| IR-K4 | Music and sound sources and their licences | IP in client advertising | HD-16 | — |

## L. Production

| ID | Question | Why it matters | Blocks | Already in repo |
|---|---|---|---|---|
| IR-L1 | Current KIE/OpenArt credit balances, and willingness to fund generation for a prototype | Last recorded: 62 KIE credits (2026-07-07), OpenArt exhausted | HD-10 | `DESIGN_OS.md:79` |
| IR-L2 | For real clients: AI-only imagery, hybrid with real footage, or real shoots? | Depiction truth and cost | HD-16 | — |
| IR-L3 | Who approves each generated asset before Canva assembly? | Reuse and AI-artifact gates exist; approval record does not | HD-06 | Design pipeline |

## M. AI

| ID | Question | Why it matters | Blocks | Already in repo |
|---|---|---|---|---|
| IR-M1 | Consumer-facing AI disclosure stance (pending counsel) | Origin-market audiences may require it | HD-16 | AI tooling terms §1 (client-facing only) |
| ★ IR-M2 | Which AI vendors may touch client data (sub-processor list)? | s.48 and DPA Annex B | HD-05 | `API_AND_AI_TOOLING_TERMS.md` §4 |
| IR-M3 | Spend limits and alert thresholds for generation and model use | Runway | — | `techstack-cost-guardian` |
| IR-M4 | Will any automation run during the pilot (scheduler approval, item 58)? | 30 declared triggers, 2 matrix rows | — | `AUTOMATION_APPROVAL_MATRIX.md` |

## N. Data

| ID | Question | Why it matters | Blocks | Already in repo |
|---|---|---|---|---|
| ★ IR-N1 | One location for real identity maps (consolidating the three) | Source of truth for prospects and the pilot | HV-44 | RD1/RD2 |
| ★ IR-N2 | Backup, retention and deletion rules for client data (RD2's storage half) | Required before private client data | HD-05 | readiness packet RD2 |
| ★ IR-N3 | The s.48 cross-border posture (item 61) | Data already leaves Kenya daily via SaaS tools | HD-05 | item 61 |
| IR-N4 | Will Arika ever receive guest-level personal data (MD5 samples may contain it)? | Consent, DPA scope | HD-05 | worksheet §1.4 |

## O. Technology

| ID | Question | Why it matters | Blocks | Already in repo |
|---|---|---|---|---|
| IR-O1 | When will the website be redeployed with apex DNS resolving? | Proof surface for outreach | HD-03 | `PROSPECTING_CYCLE.md` |
| IR-O2 | Re-authorise Canva, OpenArt and Relume connectors? | Unauthenticated at last checks (and in this session) | HD-10 | `TECHSTACK_OS.md` §9 |
| IR-O3 | Authorise provisioning of `Company` + `Pilot Engagement` in ClickUp (RM-06) | Pilot record cannot exist without it | HD-11 | `crm_provisioning/` |
| IR-O4 | A scheduling/calendar tool for discovery calls | No calendar tool registered for bookings | — | `AEIT_04` D2 |

## P. Hospitality

| ID | Question | Why it matters | Blocks | Already in repo |
|---|---|---|---|---|
| IR-P1 | What is a `Destination Property`? (a live option, never defined) | Cannot be ruled until defined | — | plugin P2 "Declared unruled" |
| IR-P2 | Should the safari circuit's seasonality be verified against the coast's before any client calendar (file 06 §4)? | A country-level peak may misdate a lodge calendar | HQ-05 | Draft 41 D3; plugin P2/P5 |
| IR-P3 | Commission a Mombasa destination profile? | Destination Fit blocks Mombasa | — | item 31h |
| IR-P4 | The owner's own ranking of hotel revenue centres by importance in Kenya (recorded as `owner_reasoning`, falsifiable) | Seeds P3 without inventing evidence | HD-08 | — |

## Q. Pilot client

| ID | Question | Why it matters | Blocks | Already in repo |
|---|---|---|---|---|
| ★ IR-Q1 | What will the group pilot deliver, at which level (group, one property, one outlet), and over what period? | Nothing can be agreed without it | HD-01 | GLOBAL_OS header 2026-10-02 |
| IR-Q2 | Current relationship with the group (cold, warm, known contact) — recorded outside the repository | Route and message | HD-03 | — |
| IR-Q3 | Which central functions the group has (reservations, revenue, marketing) — from public evidence | Group-level buyer route | HD-01 | prospecting route `hospitality_group_discovery` |
| IR-Q4 | What data could the group share, under what agreement? | S3 audit data set | HD-05 | MD1–MD8 |
| IR-Q5 | What would make the pilot "validated" (`pilot_state = validated`; `proof_required`)? | Exit criterion | HD-01 | `CRM_SCHEMA.md` Pilot Engagement |

## R. Calendars

| ID | Question | Why it matters | Blocks | Already in repo |
|---|---|---|---|---|
| IR-R1 | Planning horizon for the pilot's client calendar (e.g. 365 days)? | Resolution window | — | `SECTOR_OS_ARCHITECTURE.md` §4.4 |
| IR-R2 | Does the pilot property publish its own events or experiences calendar? | Step-5 client input | — | — |
| IR-R3 | Which origin markets matter for the pilot property? | DB 15 route scope | — | intake H-C02 |
| IR-R4 | Will the 7 Cognitive Calendars be run manually during the pilot? | The agent has never fired | — | `OPERATIONS_OS.md` §12 |

## S. KPIs

| ID | Question | Why it matters | Blocks | Already in repo |
|---|---|---|---|---|
| IR-S1 | Confirm KPI thresholds stay unset until real data (item 4)? | Deliberate decision | — | `AGENCY_KPI_DICTIONARY.md` |
| IR-S2 | Per-client target definition and seasonally comparable baseline for the pilot | Draft 41 §9 #8 | HD-04 | M6 |
| IR-S3 | Agency-side pilot KPIs (replies, discovery calls, audits started) | Measuring the pilot itself | — | daily targets table |
| IR-S4 | Which client results may ever be published, with what consent? | Class C unban path | — | claims policy §8–§9 |

## T. Future scale

| ID | Question | Why it matters | Blocks | Already in repo |
|---|---|---|---|---|
| IR-T1 | Next expansion: a second hospitality sub-sector (F&B) or a second vertical (Gate I)? | Generalization is untested | HD-18 | item 31b |
| IR-T2 | The hiring trigger for hospitality delivery | Solo capacity | — | `PEOPLE_DOCTRINE.md` §3 |
| IR-T3 | Timeline for a group/portfolio offer | Groups are the intended market | HD-01 | A001 AG-7 |
| IR-T4 | Priority of the expansion rungs (guest acquisition, guest CRM/retention, revenue intelligence) | Unengineered | — | plugin P11 |
