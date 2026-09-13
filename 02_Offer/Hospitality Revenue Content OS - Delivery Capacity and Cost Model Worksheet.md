# Hospitality Revenue Content OS — Delivery Capacity and Cost Model Worksheet

> ⚠️ **INTERNAL WORKSHEET · NOT QUOTABLE · NO PRICES.**
> This file names **what must be known** before any test price or price floor can exist. It contains **no price, no currency, no amount, no rate, no margin and no capacity figure** — every quantity below is a **variable to be supplied**, not a value.

## 1. Status

| Field | Value |
|---|---|
| **Type** | Internal worksheet — Offer (02) |
| **Offer** | Hospitality Revenue Content OS · "Direct Booking Engine" (gateway: OTA Leakage & Direct-Booking Audit) |
| **Offer status** | Working Hypothesis / **Not Quotable** · not in the Offer Engineering Registry |
| **Prices** | **None.** No test price is approved (Owner Decision 71). No hotel floor exists. |
| **Why it exists** | To unblock two decisions that gate all pricing work: **cost-to-deliver** and **delivery capacity** (`Draft 41` §5.1 inputs 1–2; Owner Decision 71). |
| **Parent document** | `02_Offer/OEOS - Hospitality Division - Hospitality Revenue Content OS (Structural, Non-Pricing). Draft 41.md` — deliverables §6, roles §7, QC gates §8, open decisions §9, Commercial Test Model §11 |
| **Date** | 2026-09-13 |

**Grounding for the capacity questions.** Operations (08) already records that **no capacity model exists** and that `operations-capacity-planner` must *"flag rather than invent"* one (`08_Operations/OPERATIONS_OS.md` §3, Decision Log 2026-07-14). The Offer department records that the roles below are **AI-assisted functional labels, not headcount**, and that the owner currently orchestrates delivery **solo with AI** (`OFFER_OS.md` §3). This worksheet keeps both positions: it asks for the model; it does not supply one.

**Legend used below.** ● core to the package · ◐ light or conditional · — not in the package. These are structural judgements from `Draft 41`, not measurements.

---

## 2. Delivery packages to estimate

| # | Package | What is delivered (from `Draft 41`) | Estimable today? |
|---|---|---|---|
| P1 | **Gateway — OTA Leakage & Direct-Booking Audit** | D1: client-data diagnosis, (a)–(d) leakage verdict, one-page roadmap (§6) | **Structure yes, effort no** — scope and duration are open (§9 #13) |
| P2 | **Entry Build — Direct Booking Engine setup** | D2 strategy · D3 revenue-year content calendar · D4 content production · D5 booking-journey messaging · D6 email/WhatsApp nurture · baseline for D7 | **Structure yes, effort no** — minimum viable scope not chosen (§6 Q5 below) |
| P3 | **Governance Retainer — monthly optimization/governance** | D7 monthly reporting · optimization of D4–D6 · QBR · governance QA | **Structure yes, effort no** — cadence is monthly; effort per cycle unknown |
| P4 | **Redirect paths** | The hand-off when the audit finds a non-content root cause (§3) | **No** — none of the destinations is engineered |

**P4 in detail — why the redirect paths cannot be costed yet:**

| Redirect | Trigger (audit verdict) | Destination | State |
|---|---|---|---|
| P4a · Pricing / rate strategy | (c) dominant | No engineered offer or owning department; nearest is Plugin P11's Transformation rung | **GAP — needs OEOS** |
| P4b · Booking-engine tech | (b) technical side dominant | Plugin P11 Expansion 1 — guest acquisition + booking-engine optimization | **Not engineered** |
| P4c · Stack rationalization | (d) dominant | Plugin P11 Transformation rung; flagged "AI & Business Stack Rationalization" proposal (`OFFER_OS.md` §3) | **Not engineered** |

**Only the redirect *hand-off* is estimable** — the effort, inside P1, of writing the redirect recommendation and evidence pack. The redirected work itself has no scope to estimate.

---

## 3. Workstream map

Which workstreams each package needs, and what drives the effort. **No hours, no money** — the driver column names the variable from §5 that would size it.

| Workstream | P1 Audit | P2 Build | P3 Retainer | P4 Redirect hand-off | Effort driver (see §5) |
|---|---|---|---|---|---|
| **Sector / client diagnosis** | ● | ◐ refresh from audit | ◐ periodic re-check | ● | H-band; archetype (Plugin P2); property count for H3 groups |
| **Data collection + channel-mix analysis** | ● | ◐ baseline confirmation | ● monthly data pulls | ◐ evidence pack | Number of audit data sources; access friction; tool-stack chaos |
| **Direct-booking message strategy** | ◐ roadmap level | ● | ◐ iteration | — | Positioning complexity; stakeholder count |
| **Booking-journey copy / content** | — | ● | ◐ optimization | — | Pages / assets / messages; review rounds |
| **Email or WhatsApp nurture** | — | ● *conditional on consent (QG4) and a platform* | ● | — | Sequences / messages; platform availability |
| **Reporting** | ● audit report + verdict | ◐ baseline report | ● monthly pack | ◐ | Reporting cadence; KPI count; whether data pulls can be automated |
| **Client communication** | ● readout | ● approvals | ● reviews + QBR | ● redirect conversation | Stakeholder count (H3 higher); approval windows |
| **QA / approval gates** | ● QG1, QG6 | ● QG2–QG5, QG7, QG8 | ● QG2, QG4, QG6 | ◐ QG1 | Gates per deliverable (`Draft 41` §8); review rounds |
| **Compliance review** | ◐ data-handling terms | ● consent, claims, contract | ◐ ongoing sends | ◐ | Legal (10) review path; consent basis per list |
| **Hand-off / offboarding** | ◐ to proposal or redirect | ◐ to retainer | ● at close | ● | Data return / deletion terms; asset handover |

**Cross-cutting dependency surfaced while mapping:** the nurture workstream has **no registered delivery tool**. `13_Tech_Stack/TECHSTACK_OS.md` §3 lists no email-marketing or WhatsApp Business platform — ManyChat is *proposed, account not created*, and the Zoho entry is mailbox hosting. Until one is chosen and verified, P2's and P3's nurture workstream cannot be sized or costed.

---

## 4. Role / capacity model

Role-based. The only named person is the owner of record already confirmed in the repo. Mapping to `Draft 41` §7.1 is shown so the two documents stay aligned.

| Role | `Draft 41` §7.1 equivalent | P1 | P2 | P3 | Required? | Internal owner assigned? | Capacity unknowns |
|---|---|---|---|---|---|---|---|
| **Owner / strategist** | Senior Diagnostic Reviewer · Account Lead (default) | ● | ● | ● | **Required** | **Yes, by default** — the agency owner (Offer (02) owner of record, `OFFER_OS.md`: Mary Thuo); **not** a confirmed delivery assignment | Weekly time available for delivery after running the agency; how many senior-only tasks (verdict, redirect, approvals) one engagement consumes |
| **Offer engineer** | — (Offer 02 function) | ◐ | ◐ | — | **Conditional** — package design and scope changes, not routine delivery | **Yes** — owner + advisory `offer-oeos-engineer`; no separate person | How often a client needs scope customization beyond the standard package |
| **Content strategist** | Revenue-Content Strategist | ◐ | ● | ◐ | **Required** for P2 | **No** | Effort per strategy + calendar; how much AI drafting reduces it |
| **Copy / content producer** | Content Producer · Conversion Copywriter | — | ● | ● | **Required** for P2, P3 | **No** | Output per cycle; revision load |
| **Design support** | — (Design 19) | — | ◐ | ◐ | **Conditional** — when content or landing pages need visuals | **No** | Image-generation runway was near-exhausted when last verified (`TECHSTACK_OS.md` §3, 2026-07-15); Canva authentication lapsed (same date) |
| **Automation or booking-journey advisor** | Lifecycle Engineer · journey-messaging side of Conversion Copywriter | — | ◐ | ◐ | **Conditional** — nurture needs consent + a platform; technical engine work is a redirect, not this role | **No** | No nurture platform registered; every automation needs an approval-matrix row (`AUTOMATION_APPROVAL_MATRIX.md`) |
| **Analytics / reporting** | Audit Analyst · Reporting Analyst | ● | ◐ | ● | **Required** | **No** | Data-access effort per client; whether pulls can be automated given integration-type stack chaos |
| **Legal / compliance review** | — (Legal 10) | ◐ | ● | ◐ | **Required** once client data or client-facing sends exist | **Blocked** — no counsel engaged (`OWNER_INPUT_NEEDED.md` item 59); `legal-counsel-router` routes, it does not review | Review turnaround; whether review is per template or per engagement |
| **Delivery QA** | QA gates (`Draft 41` §8) · Operations (08) delivery QA | ● | ● | ● | **Required** | **Blocked** — advisory `operations-delivery-qa` exists; no named human reviewer | Whether QA can be the owner (self-review) or needs a second person |

**Two structural constraints that bound every row:**
- **The delegability ceiling.** Senior-expert-only work — the audit verdict, redirect decisions, Class 3 approvals — stays with one person however many agents exist (`11_HR_People_Ops/PEOPLE_DOCTRINE.md`; `Draft 41` §12 Phase 12). More agents raise the volume arriving at that ceiling, not the ceiling.
- **Delegation is itself an open decision.** Any human help beyond solo + AI is an HR (11) engagement question, including the misclassification test for creative contractors (`hr-engagement-classifier`).

---

## 5. Cost-to-deliver inputs needed

**Variables only.** Every "value" is to be supplied by the named source; none is estimated here.

| # | Variable | Unit | Applies to | Who supplies | Known now? |
|---|---|---|---|---|---|
| V1 | **Effort by role** | Hours or effort units per role, per package | P1, P2, P3, P4 hand-off | Owner, with Operations (08) | ❌ |
| V2 | **Number of audit data sources** | Count per client (booking engine, PMS/CRS exports, channel manager, OTA extranets, web analytics, email/CRM) | P1, P3 | Per client, at Qualification | ❌ varies by stack |
| V3 | **Number of pages / assets / messages** | Count per build; count per retainer cycle | P2, P3 | Owner — from minimum viable scope (§6 Q5) | ❌ |
| V4 | **Number of review rounds** | Rounds per deliverable | P1–P3 | Owner — revision policy is open (`Draft 41` §9 #14) | ❌ |
| V5 | **Tool / API cost categories** | Categories only (below) | P1–P3 | Tech Stack (13) | ◐ categories listed; no costs |
| V6 | **Design / content production load** | Assets per build; assets per retainer cycle | P2, P3 | Owner + Design (19) | ❌ |
| V7 | **Reporting cadence** | Reports per period | P3 | `Draft 41` — **monthly** [RUN]; effort per report unknown | ◐ cadence only |
| V8 | **Compliance / legal review requirement** | Reviews per engagement; reviews per new template | P1–P3 | Legal (10) | ❌ blocked on counsel |
| V9 | **Owner time requirement** | Senior-only effort per engagement (verdict, redirect, approvals, client relationship) | P1–P3 | Owner | ❌ |
| V10 | **H-band and severity scaling** | How V1–V9 change from H1 → H3 and L1 → L3 (qualitative first) | P1–P3 | Owner (axes approved by Decision 71) | ❌ |

**V5 — tool / API cost categories** (categories, not costs; each must be verified per `TECHSTACK_OS.md` discipline):
- **Model usage** — Anthropic API, for any `arika-runtime` agent used in delivery
- **Image generation** — KIE.ai / OpenArt credit pools
- **Design assembly** — Canva
- **Content / brief system** — Notion
- **CRM** — ClickUp
- **Email / WhatsApp messaging platform** — **not registered**; choice pending
- **Analytics access** — usually the client's own tools; access, not licence
- **Landing-page hosting** — usually the client's own site; confirm per engagement
- **Data processing / storage** — every tool above that touches client data is a sub-processor (`10_Legal/templates/DPA.md` Annex B)

---

## 6. Capacity questions — for the owner, before test pricing

| # | Question | Why it gates pricing | Who can answer |
|---|---|---|---|
| Q1 | **How many hotels can be handled at once** — separately for audits in flight, builds in flight, and retainers active? | A floor that ignores capacity authorizes overselling against a fiction (`operations-capacity-planner`) | Owner + Operations (08) |
| Q2 | **What is solo-owner work vs AI-assisted work?** And does AI-assisted work still consume owner review time? | AI-assisted drafting is not free if every output needs senior review | Owner |
| Q3 | **What can be delegated — and to whom?** No delegate exists today | Delegation changes cost structure and triggers HR (11) classification questions | Owner + HR (11) |
| Q4 | **What must wait for another department?** Legal (10): contract, DPA, consent · Operations (08): capacity model, scheduling · Content (04): publishing gate, brief pipeline · Design (19): image runway, Canva authentication · Tech Stack (13): nurture platform | A dependency with no date makes a delivery timeline — and so a price — unfounded | Each named department |
| Q5 | **What is the minimum viable delivery scope?** Which of D2–D7 are in the smallest sellable build — and can nurture wait until consent and a platform exist? | Scope is the largest single driver of V1, V3 and V6 | Owner (Offer 02) |
| Q6 | **Does an H3 engagement count as more than one unit of capacity?** (2–5 properties, multiple stakeholders) | If H3 consumes several slots, its cost cannot be one band's cost | Owner |
| Q7 | **How much owner time per week is actually available for client delivery?** | V9 has no ceiling without it | Owner |
| Q8 | **Does demand cluster by season?** Low season is the buying window (Plugin P13), and client approvals slow in peak season (`Draft 41` §8) | Sales and delivery load may peak together | Owner + Sector (01) |

---

## 7. Pricing-test readiness gate

**Rule:** no `TEST_FIXTURE` price figure may be written anywhere until **every** item below is ✅. Passing this gate permits **internal test figures only** — it does not create a floor, does not unblock Phase 11 by itself, and does not make the offer quotable.

| # | Gate item | Status (2026-09-13) | Evidence required to pass | Owning department |
|---|---|---|---|---|
| G1 | **Delivery scope chosen** (minimum viable P1/P2/P3 scope) | ❌ | Q5 answered in writing | Offer (02) |
| G2 | **Role effort estimated** (V1 for every required role, per package) | ❌ | V1 filled, labelled estimate | Offer (02) + Operations (08) |
| G3 | **Capacity owner assigned** | ❌ | A named owner for delivery capacity; Q1 answered | Operations (08) |
| G4 | **Tool cost categories identified** | ◐ categories listed (§5 V5); nurture platform unchosen | Every category confirmed, including a verified nurture platform | Tech Stack (13) |
| G5 | **Legal / compliance review path identified** | ❌ no counsel (item 59) | A named review path for contract, data terms and consent | Legal (10) |
| G6 | **Audit / build / retainer commercial shape selected** | ❌ (`Draft 41` §11.5 #2, #3) | Owner choice recorded | Offer (02) |
| G7 | **Owner approves use of `TEST_FIXTURE` figures** | ⏸ deferred by Owner Decision 71 until cost-to-deliver and capacity exist | Owner decision recorded | Owner |

**Also required before a *positive* pricing-floor test — beyond this gate:**
- **A method for deriving a hotel floor.** §10's method averages comparable offers; no comparable hotel offer exists.
- **A pricing-agent spec that can express an H-band.** `offer-pricing-floor-analyst`'s `arr_band` field accepts only `A`–`D` or `unknown`.

---

## 8. Open decisions

| # | Decision | Owning department | Decider | Blocks |
|---|---|---|---|---|
| 1 | Minimum viable delivery scope (Q5) | Offer (02) | Owner | G1, V3, V6 |
| 2 | Effort estimates by role (V1) | Offer (02) + Operations (08) | Owner | G2 |
| 3 | Delivery capacity model and its owner (Q1, Q6, Q7) | Operations (08) | Owner | G3 |
| 4 | What is delegated, and under what engagement type (Q3) | HR (11) | Owner | Q2–Q3 |
| 5 | Email / WhatsApp nurture platform | Tech Stack (13) | Owner | G4, nurture workstream |
| 6 | Legal review path — counsel engagement (item 59) | Legal (10) | Owner | G5, QG4, contract, consent |
| 7 | Audit commercial shape — paid standalone vs credited into build | Offer (02) | Owner | G6 |
| 8 | Entry commercial shape — build + retainer vs audit + monthly retainer | Offer (02) | Owner | G6 |
| 9 | Approval to use `TEST_FIXTURE` figures | Offer (02) | Owner | G7 |
| 10 | Hotel floor derivation method | Offer (02) + Finance (09) | Owner | Any floor |
| 11 | Pricing-agent spec support for H-bands | Offer (02) + runtime | Owner | Positive agent test |
| 12 | L2 / L3 severity thresholds | Offer (02) + Audits & Diagnostics (14) | Owner | V10, audit verdict consistency |
| 13 | Revision policy, SLAs, approval windows (V4) | Offer (02) + Client Success (07) | Owner | V4 |
| 14 | Image-generation runway and Canva re-authentication | Design (19) + Tech Stack (13) | Owner | Design support role |
| 15 | Redirect destinations for (c), (d) and technical (b) | Offer (02) | Owner | P4 |
| 16 | Launch ICP, including whether H3 is in it | Offer (02) + Sector (01) | Owner | Q6, qualification |

---

## 9. Changelog

- **2026-09-13 — Created.** Internal worksheet to unblock the two decisions that gate all pricing work on the Hospitality Revenue Content OS: cost-to-deliver and delivery capacity. Maps four packages (audit, build, retainer, redirect hand-off) against ten workstreams and nine roles, lists ten cost variables and nine tool-cost categories, poses eight capacity questions, and defines a seven-item readiness gate that must fully pass before any `TEST_FIXTURE` price figure is written. **Contains no price, currency, amount, rate, margin or capacity figure.** Surfaced while building it: **no email or WhatsApp nurture platform is registered** in Tech Stack (13), so the nurture workstream cannot be sized. Status of the offer unchanged: **Working Hypothesis / Not Quotable**, not registered. — Claude Code (Opus 5)
