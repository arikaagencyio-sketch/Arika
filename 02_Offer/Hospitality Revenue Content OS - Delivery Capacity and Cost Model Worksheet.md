# Hospitality Revenue Content OS — Delivery Capacity and Cost Model Worksheet

> ⚠️ **INTERNAL WORKSHEET · NOT QUOTABLE · NO PRICES.**
> This file names **what must be known** before any test price or price floor can exist. It contains **no price, no currency, no amount, no rate, no margin and no capacity figure** — every quantity below is a **variable to be supplied**, not a value. §10 adds **relative effort bands (XS–XL) for owner review** — not hours, not money.

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

### 1.1 MVP delivery scope — owner decision (2026-09-13)

✅ **Approved for INTERNAL DESIGN ONLY** — a minimum viable delivery scope, so effort and capacity can be estimated against something concrete. It is **not** a public offer and carries **no price**.

| In MVP scope | Deferred — out of the MVP |
|---|---|
| **P1 Gateway** — OTA Leakage & Direct-Booking Audit | **P2 beyond Phase 1** — content production and implementation |
| **P2 Entry Build — Phase 1 only:** Direct Booking Message/Journey Blueprint | **Email / WhatsApp nurture implementation** (D6) |
| **P4 redirect recommendation**, delivered inside the audit | **P3 Governance retainer**, including monthly reporting (D7) |
| **H1 and H2 properties only** | **H3** — out of scope until group / property-profile handling is solved |

**MVP outputs:**

| # | Output | Maps to `Draft 41` | Package |
|---|---|---|---|
| M1 | Audit Findings Snapshot | D1 — report | P1 |
| M2 | Leakage Root-Cause Classification | D1 — the (a)–(d) verdict; §3 diagnostic gate | P1 |
| M3 | Direct Booking Message Strategy | D2 — scoped to messaging | P2 Phase 1 |
| M4 | Booking Journey Copy/Content Blueprint | D5 — **blueprint with sample copy**, not D5's full copy package (§1.2) | P2 Phase 1 |
| M5 | Basic Direct-Booking Content Plan | D3 — basic version | P2 Phase 1 |
| M6 | Measurement Plan | Baseline and measurement design (§7's seasonally comparable baseline) — **not** D7's monthly reporting | P2 Phase 1 |
| M7 | Redirect Recommendation — only if the root cause is pricing/rate strategy or tech-stack/integration | P4 hand-off | P1 |

**The diagnostic gate still governs the build.** M3–M6 are produced only when M2 finds an (a) content/messaging or (b) journey-messaging root cause. A (c), (d) or technical-(b) finding ends the MVP at M1, M2 and M7.

**Still not approved:** prices · a public offer · the retainer · test price figures · legal claims · performance guarantees. The full offer remains **Working Hypothesis / Not Quotable.**

**The two scope edges this decision left open are now settled** by Owner Decision #17 (§1.2): M4's depth, and the exclusion of D4 content production (§8 #17–#18).

### 1.2 M4 depth — Owner Decision #17 (2026-09-13)

✅ **Decided for INTERNAL DESIGN ONLY.** M4 is a **strategic blueprint, not a production build.**

| M4 includes | M4 excludes |
|---|---|
| Blueprint and structure of the booking journey | Full finished copy for every page or message |
| Page / message hierarchy | Full content production (D4) |
| Key messaging blocks | Implementation inside booking tools or the website CMS |
| Sample copy examples for **critical sections only** | |

**What follows from it:**
- **D4 content production is outside the MVP.** The decision excludes full content production and keeps the MVP "a strategic blueprint, not a full production build" — the confirmation §8 #18 asked for. *If D4 was meant to stay open as a separate question, #18 reopens and G1 returns to partial.*
- **No implementation work.** Nothing is built inside a booking engine or CMS — consistent with `Draft 41` §3, where technical journey work is a redirect, not this offer.
- **Sample copy is client-facing text, so the content gates apply to it:** QG2 (no outcome claims — the proof method is blocked, so samples carry none), QG3 (benchmarks labelled), QG5 (no price) and QG7 (positioning). Legal claims and performance guarantees remain unapproved.
- **"Critical sections" has no fixed count.** Which sections receive sample copy is an estimation assumption, to be stated when V1 and V3 are estimated (G2).

---

## 2. Delivery packages to estimate

| # | Package | What is delivered (from `Draft 41`) | MVP (§1.1) | Estimable today? |
|---|---|---|---|---|
| P1 | **Gateway — OTA Leakage & Direct-Booking Audit** | D1: client-data diagnosis, (a)–(d) leakage verdict, one-page roadmap (§6) | ✅ **In** — M1, M2, M7 | **Structure yes; effort banded for the MVP** (§10, owner review required) — no hours; audit duration still open (`Draft 41` §9 #13) |
| P2 | **Entry Build — Direct Booking Engine setup** | D2 strategy · D3 revenue-year content calendar · D4 content production · D5 booking-journey messaging · D6 email/WhatsApp nurture · baseline for D7 | ◐ **Phase 1 only** — M3–M6, the message/journey blueprint with sample copy (§1.2). D4 production, D6 nurture and implementation deferred | **Structure yes; effort banded for the MVP** (§10, owner review required) — no hours |
| P3 | **Governance Retainer — monthly optimization/governance** | D7 monthly reporting · optimization of D4–D6 · QBR · governance QA | ⏸ **Deferred** | Not needed for the MVP |
| P4 | **Redirect paths** | The hand-off when the audit finds a non-content root cause (§3) | ◐ **Hand-off only** — M7, inside P1; the redirected work is out of scope | **No** — none of the destinations is engineered |

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

**Cross-cutting dependency surfaced while mapping:** the nurture workstream has **no registered delivery tool**. `13_Tech_Stack/TECHSTACK_OS.md` §3 lists no email-marketing or WhatsApp Business platform — ManyChat is *proposed, account not created*, and the Zoho entry is mailbox hosting. Until one is chosen and verified, P2's and P3's nurture workstream cannot be sized or costed. *(The MVP defers nurture, so this does not block MVP estimation — §3.1.)*

### 3.1 MVP overlay (§1.1)

| Workstream | MVP status | MVP outputs | Note |
|---|---|---|---|
| **Sector / client diagnosis** | ✅ In | M1, M2 | H1/H2 only — no multi-property profiling |
| **Data collection + channel-mix analysis** | ✅ In | M1, M2, M6 | Audit data only; no monthly pulls |
| **Direct-booking message strategy** | ✅ In | M3 | Only after an (a) or (b)-messaging verdict |
| **Booking-journey copy / content** | ◐ In, as a blueprint | M4, M5 | Structure, page/message hierarchy, key messaging blocks, sample copy for critical sections (§1.2) · no full copy, no D4 production, no booking-tool/CMS implementation |
| **Email or WhatsApp nurture** | ⏸ Deferred | — | Removes the nurture-platform and consent-send dependencies from the MVP |
| **Reporting** | ◐ Reduced | M1, M6 | Audit report and measurement plan; monthly reporting deferred with the retainer |
| **Client communication** | ✅ In | All | Audit readout and blueprint approvals; no QBR |
| **QA / approval gates** | ✅ In, reduced set | All | QG1, QG2, QG3, QG5, QG6, QG7 apply; QG4 (consent) and QG8 (automation go-live) are not triggered while nurture is deferred |
| **Compliance review** | ◐ Reduced | M1, M2 | Audit-data handling terms still needed; no consent sends |
| **Hand-off / offboarding** | ✅ In | M7 | Redirect hand-off or close; no transition to a retainer |

---

## 4. Role / capacity model

Role-based. The only named person is the owner of record already confirmed in the repo. Mapping to `Draft 41` §7.1 is shown so the two documents stay aligned.

| Role | `Draft 41` §7.1 equivalent | P1 | P2 | P3 | Required? | **MVP (§1.1)** | Internal owner assigned? | Capacity unknowns |
|---|---|---|---|---|---|---|---|---|
| **Owner / strategist** | Senior Diagnostic Reviewer · Account Lead (default) | ● | ● | ● | **Required** | ✅ **In** — M2 verdict, M7 redirect, approvals | **Yes, by default** — the agency owner (Offer (02) owner of record, `OFFER_OS.md`: Mary Thuo); **not** a confirmed delivery assignment | Weekly time available for delivery after running the agency; how many senior-only tasks (verdict, redirect, approvals) one engagement consumes |
| **Offer engineer** | — (Offer 02 function) | ◐ | ◐ | — | **Conditional** — package design and scope changes, not routine delivery | ◐ Conditional — scope changes only | **Yes** — owner + advisory `offer-oeos-engineer`; no separate person | How often a client needs scope customization beyond the standard package |
| **Content strategist** | Revenue-Content Strategist | ◐ | ● | ◐ | **Required** for P2 | ✅ **In** — M3; M4 structure, hierarchy and messaging blocks; M5 | **No** | Effort per strategy + calendar; how much AI drafting reduces it |
| **Copy / content producer** | Content Producer · Conversion Copywriter | — | ● | ● | **Required** for P2, P3 | ◐ **Light** — sample copy for critical sections only (§1.2); no full copy, no production. Could sit with the content strategist rather than a separate role | **No** | Output per cycle; revision load · *MVP:* how many critical sections are sampled; review rounds on samples |
| **Design support** | — (Design 19) | — | ◐ | ◐ | **Conditional** — when content or landing pages need visuals | ⏸ **Deferred** — no production in the MVP | **No** | Image-generation runway was near-exhausted when last verified (`TECHSTACK_OS.md` §3, 2026-07-15); Canva authentication lapsed (same date) |
| **Automation or booking-journey advisor** | Lifecycle Engineer · journey-messaging side of Conversion Copywriter | — | ◐ | ◐ | **Conditional** — nurture needs consent + a platform; technical engine work is a redirect, not this role | ⏸ **Deferred** — nurture excluded; no booking-tool or CMS implementation (§1.2); journey-messaging direction sits with the content strategist in M4 | **No** | No nurture platform registered; every automation needs an approval-matrix row (`AUTOMATION_APPROVAL_MATRIX.md`) |
| **Analytics / reporting** | Audit Analyst · Reporting Analyst | ● | ◐ | ● | **Required** | ✅ **In** — M1, M2, M6; no monthly reporting | **No** | Data-access effort per client; whether pulls can be automated given integration-type stack chaos |
| **Legal / compliance review** | — (Legal 10) | ◐ | ● | ◐ | **Required** once client data or client-facing sends exist | ◐ **Reduced** — audit-data handling terms; no consent review while nurture is deferred; sample copy carries no claims (QG2), so no claims review | **Blocked** — no counsel engaged (`OWNER_INPUT_NEEDED.md` item 59); `legal-counsel-router` routes, it does not review | Review turnaround; whether review is per template or per engagement |
| **Delivery QA** | QA gates (`Draft 41` §8) · Operations (08) delivery QA | ● | ● | ● | **Required** | ✅ **In** — reduced gate set (§3.1); sample copy adds QG2, QG3, QG5 and QG7 checks (§1.2) | **Blocked** — advisory `operations-delivery-qa` exists; no named human reviewer | Whether QA can be the owner (self-review) or needs a second person |

**Two structural constraints that bound every row:**
- **The delegability ceiling.** Senior-expert-only work — the audit verdict, redirect decisions, Class 3 approvals — stays with one person however many agents exist (`11_HR_People_Ops/PEOPLE_DOCTRINE.md`; `Draft 41` §12 Phase 12). More agents raise the volume arriving at that ceiling, not the ceiling.
- **Delegation is itself an open decision.** Any human help beyond solo + AI is an HR (11) engagement question, including the misclassification test for creative contractors (`hr-engagement-classifier`).

---

## 5. Cost-to-deliver inputs needed

**Variables only.** Every "value" is to be supplied by the named source; none is estimated here.

| # | Variable | Unit | Applies to | Who supplies | Known now? |
|---|---|---|---|---|---|
| V1 | **Effort by role** | Hours or effort units per role, per package | P1, P2, P3, P4 hand-off | Owner, with Operations (08) | ◐ **MVP bands drafted (§10)** — owner review required; legal not estimated; no hours |
| V2 | **Number of audit data sources** | Count per client (booking engine, PMS/CRS exports, channel manager, OTA extranets, web analytics, email/CRM) | P1, P3 | Per client, at Qualification · minimum MVP data set open (§8 #20) | ❌ varies by stack — the MVP estimate assumes basic channel-mix data (§10.2 A5) |
| V3 | **Number of pages / assets / messages** | Count per build; count per retainer cycle | P2, P3 | Owner — from minimum viable scope (§6 Q5) | ❌ |
| V4 | **Number of review rounds** | Rounds per deliverable | P1–P3 | Owner — revision policy is open (`Draft 41` §9 #14) | ❌ |
| V5 | **Tool / API cost categories** | Categories only (below) | P1–P3 | Tech Stack (13) | ◐ categories listed; no costs |
| V6 | **Design / content production load** | Assets per build; assets per retainer cycle | P2, P3 | Owner + Design (19) | ❌ |
| V7 | **Reporting cadence** | Reports per period | P3 | `Draft 41` — **monthly** [RUN]; effort per report unknown | ◐ cadence only |
| V8 | **Compliance / legal review requirement** | Reviews per engagement; reviews per new template | P1–P3 | Legal (10) | ❌ blocked on counsel |
| V9 | **Owner time requirement** | Senior-only effort per engagement (verdict, redirect, approvals, client relationship) | P1–P3 | Owner | ❌ |
| V10 | **H-band and severity scaling** | How V1–V9 change from H1 → H3 and L1 → L3 (qualitative first) | P1–P3 | Owner (axes approved by Decision 71) | ❌ |

**MVP effect on these variables — values still blank.** V3 counts blueprint items (journey structure, page/message hierarchy, key messaging blocks) plus the sections given sample copy — not finished pages, messages or produced assets (§1.2) · V4 applies to the blueprint and the samples only · V6 design load is deferred with production · V7 does not apply until the retainer returns · V8 narrows to audit-data handling terms · V10 narrows to H1 → H2, since H3 is out of the MVP. **No hours or cost value has been entered** — relative effort bands only, in §10.

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
| Q5 | ~~What is the minimum viable delivery scope?~~ ✅ **Answered for the MVP, internal design only (§1.1–§1.2, 2026-09-13):** audit + Entry Build Phase 1 blueprint with sample copy, H1/H2 only; nurture, retainer, H3, D4 production and booking-tool/CMS implementation deferred. *Full-offer scope (P2 beyond Phase 1, P3) not chosen* | Scope is the largest single driver of V1, V3 and V6 | Owner (Offer 02) |
| Q6 | **Does an H3 engagement count as more than one unit of capacity?** (2–5 properties, multiple stakeholders) — ⏸ *deferred: H3 is out of the MVP (§1.1)* | If H3 consumes several slots, its cost cannot be one band's cost | Owner |
| Q7 | **How much owner time per week is actually available for client delivery?** | V9 has no ceiling without it | Owner |
| Q8 | **Does demand cluster by season?** Low season is the buying window (Plugin P13), and client approvals slow in peak season (`Draft 41` §8) | Sales and delivery load may peak together | Owner + Sector (01) |

---

## 7. Pricing-test readiness gate

**Rule:** no `TEST_FIXTURE` price figure may be written anywhere until **every** item below is ✅. Passing this gate permits **internal test figures only** — it does not create a floor, does not unblock Phase 11 by itself, and does not make the offer quotable.

| # | Gate item | Status (2026-09-13) | Evidence required to pass | Owning department |
|---|---|---|---|---|
| G1 | **Delivery scope chosen** (minimum viable P1/P2/P3 scope) | ✅ **Passed — MVP only** (§1.1–§1.2, 2026-09-13) · **not passed for the full offer** — P2 beyond Phase 1 and P3 scope not chosen | Q5 answered in writing — done for the MVP, including M4 depth (#17) and the D4 exclusion (#18) | Offer (02) |
| G2 | **Role effort estimated** (V1 for every required role, per package) | ◐ **PARTIAL — not passed** (MVP only, §10, 2026-09-13): bands drafted for every active MVP role; legal BLOCKED, not estimated; revision policy and data-source range unresolved; owner review pending | V1 filled, labelled estimate — owner-confirmed bands satisfy V1's effort units; legal effort estimated once a review path exists (G5); §10.7 lists the four decisions needed | Offer (02) + Operations (08) |
| G3 | **Capacity owner assigned** | ❌ | A named owner for delivery capacity; Q1 answered | Operations (08) |
| G4 | **Tool cost categories identified** | ◐ categories listed (§5 V5); **for the MVP the nurture platform is no longer required** (nurture deferred) | Every MVP category confirmed; the nurture platform returns with nurture | Tech Stack (13) |
| G5 | **Legal / compliance review path identified** | ❌ no counsel (item 59) — **scope reduced for the MVP** (no consent sends) | A named review path for contract and audit-data terms; consent review returns with nurture | Legal (10) |
| G6 | **Audit / build / retainer commercial shape selected** | ❌ (`Draft 41` §11.5 #2, #3) — **reframed for the MVP:** the retainer is deferred, so the MVP question is how the audit and the Phase 1 blueprint are packaged | Owner choice recorded | Offer (02) |
| G7 | **Owner approves use of `TEST_FIXTURE` figures** | ⏸ deferred by Owner Decision 71 until cost-to-deliver and capacity exist | Owner decision recorded | Owner |

**Also required before a *positive* pricing-floor test — beyond this gate:**
- **A method for deriving a hotel floor.** §10's method averages comparable offers; no comparable hotel offer exists.
- **A pricing-agent spec that can express an H-band.** `offer-pricing-floor-analyst`'s `arr_band` field accepts only `A`–`D` or `unknown`.

---

## 8. Open decisions

| # | Decision | Owning department | Decider | Blocks |
|---|---|---|---|---|
| 1 | ~~Minimum viable delivery scope (Q5)~~ ✅ **Decided for the MVP, internal design only (§1.1–§1.2)** | Offer (02) | Owner | ~~G1~~ — passed for the MVP |
| 2 | Effort estimates by role (V1) — ◐ *MVP bands drafted (§10); owner review required* | Offer (02) + Operations (08) | Owner | G2 |
| 3 | Delivery capacity model and its owner (Q1, Q6, Q7) | Operations (08) | Owner | G3 |
| 4 | What is delegated, and under what engagement type (Q3) | HR (11) | Owner | Q2–Q3 |
| 5 | Email / WhatsApp nurture platform — ⏸ *not needed for the MVP* | Tech Stack (13) | Owner | Nurture, when it returns |
| 6 | Legal review path — counsel engagement (item 59) | Legal (10) | Owner | G2 (legal effort), G5, QG4, contract, consent |
| 7 | Audit commercial shape — paid standalone vs credited into build | Offer (02) | Owner | G6 |
| 8 | Entry commercial shape — build + retainer vs audit + monthly retainer · *for the MVP (retainer deferred): how the audit and the Phase 1 blueprint are packaged* | Offer (02) | Owner | G6 |
| 9 | Approval to use `TEST_FIXTURE` figures | Offer (02) | Owner | G7 |
| 10 | Hotel floor derivation method | Offer (02) + Finance (09) | Owner | Any floor |
| 11 | Pricing-agent spec support for H-bands | Offer (02) + runtime | Owner | Positive agent test |
| 12 | L2 / L3 severity thresholds | Offer (02) + Audits & Diagnostics (14) | Owner | V10, audit verdict consistency |
| 13 | Revision policy, SLAs, approval windows (V4) | Offer (02) + Client Success (07) | Owner | V4, G2 (§10 assumes one round) |
| 14 | Image-generation runway and Canva re-authentication | Design (19) + Tech Stack (13) | Owner | Design support role |
| 15 | Redirect destinations for (c), (d) and technical (b) | Offer (02) | Owner | P4 |
| 16 | Launch ICP — *narrowed: the MVP is H1/H2 only* | Offer (02) + Sector (01) | Owner | Qualification |
| 17 | ~~Does M4 include finished copy, or only the blueprint?~~ ✅ **Decided 2026-09-13 (Owner Decision #17):** blueprint and structure, page/message hierarchy, key messaging blocks, sample copy for critical sections — no full finished copy, no full content production, no booking-tool/CMS implementation (§1.2) | Offer (02) + Content (04) | Owner | ~~V3, V4, copy/content producer role~~ — unblocked |
| 18 | ~~Confirm D4 content production is outside the MVP~~ ✅ **Confirmed by Decision #17's wording** — "not a full production build" (§1.2) | Offer (02) | Owner | ~~V3, V6~~ — unblocked |
| 19 | H3 group / property-profile handling — needed before H3 returns (the Hospitality plugin's P2 group-union operator is unimplemented) | Sector (01) + Offer (02) | Owner | H3 |
| 20 | Minimum audit data set for an MVP audit — what counts as basic channel-mix data, and the data-source range accepted (V2) | Offer (02) + Audits & Diagnostics (14) | Owner | G2 (analytics band), V2 |

---

## 9. Changelog

- **2026-09-13 — Created.** Internal worksheet to unblock the two decisions that gate all pricing work on the Hospitality Revenue Content OS: cost-to-deliver and delivery capacity. Maps four packages (audit, build, retainer, redirect hand-off) against ten workstreams and nine roles, lists ten cost variables and nine tool-cost categories, poses eight capacity questions, and defines a seven-item readiness gate that must fully pass before any `TEST_FIXTURE` price figure is written. **Contains no price, currency, amount, rate, margin or capacity figure.** Surfaced while building it: **no email or WhatsApp nurture platform is registered** in Tech Stack (13), so the nurture workstream cannot be sized. Status of the offer unchanged: **Working Hypothesis / Not Quotable**, not registered. — Claude Code (Opus 5)
- **2026-09-13 — MVP delivery scope recorded (owner decision, internal design only).** Added §1.1: Gateway audit + Entry Build Phase 1 (Direct Booking Message/Journey Blueprint), H1/H2 only; nurture implementation, governance retainer and H3 deferred; seven MVP outputs (M1–M7) mapped to `Draft 41` deliverables. §2 and §4 gained an MVP column, §3 an MVP overlay, §5 a note on which variables the MVP narrows. G1 marked **partially passed (MVP only)**; G4, G5 and G6 annotated for the reduced scope; Q5 answered for the MVP, Q6 deferred; three new open decisions (#17–#19). **Cost and effort left blank.** Still not approved: prices, public offer, retainer, test price figures, legal claims, performance guarantees. — Claude Code (Opus 5)
- **2026-09-13 — Owner Decision #17 recorded: M4 is a blueprint, not a production build (internal design only).** Added §1.2: M4 includes blueprint and structure, page/message hierarchy, key messaging blocks and sample copy for critical sections; excludes full finished copy, full content production and booking-tool/CMS implementation. #17 decided; #18 closed by the same decision's wording (D4 production outside the MVP). **G1 now passed for the MVP only** — not for the full offer. G2 marked ready to start for the MVP. §2, §3.1, §4, §5 and Q5 updated for the effort implications: the copy/content producer drops to light sample copy, and sample copy triggers QG2, QG3, QG5 and QG7 checks. **Cost and effort still blank; no prices.** — Claude Code (Opus 5)
- **2026-09-13 — Added §10 MVP Role-Effort Estimate (owner review required).** Relative bands (XS–XL) only, for one H1/H2 MVP engagement: owner/strategist **L** · offer engineer **XS** · content strategist **M** · sample-copy producer **S** · analytics/reporting **M** · delivery QA **S** · legal/compliance **BLOCKED, not estimated** · design support and automation/booking-journey advisor **deferred** (the advisor is XS if a booking-journey root cause triggers it). Includes effort assumptions A1–A8, a redirect-path comparison, the capacity implication (one MVP client at a time appears plausible for a solo owner with AI — **not a capacity claim**, owner to confirm), and the four decisions that move G2 to passed. **G2 marked PARTIAL, not passed.** V1, V2, §2 P1/P2, §5's MVP note, §8 #2, #6 and #13 updated; new §8 #20 (minimum audit data set). Placed after §9 Changelog under the requested section number §10. **No hours, no money, no prices.** — Claude Code (Opus 5)

---

## 10. MVP Role-Effort Estimate — Owner Review Required

> ⚠️ **DRAFT ESTIMATE · OWNER REVIEW REQUIRED · NOT HOURS · NOT MONEY.** Relative effort bands for **one MVP engagement**, reasoned from §1.1–§1.2 of this worksheet and `Draft 41` §6–§8. Nothing here is measured, and no agent was run. The bands are **not** converted to hours or money, and they are **not** a capacity figure or a pricing input until the owner confirms them. The offer remains **Working Hypothesis / Not Quotable.**

**Scope estimated:** the approved MVP only — Gateway audit + Entry Build Phase 1 blueprint, outputs M1–M7, M4 as blueprint + sample copy, H1/H2 only. **Excluded:** H3 groups, the retainer, email/WhatsApp nurture implementation, and booking-tool or website implementation.

### 10.1 Band scale

Bands are **ordinal and relative within one MVP engagement**: they rank how much of that engagement's total effort a role consumes. They are not durations.

| Band | Meaning |
|---|---|
| **XS** | An occasional touchpoint — only when something departs from the standard MVP |
| **S** | A bounded set of tasks; a small share of the engagement |
| **M** | A substantial workstream within one phase, or light work across both phases |
| **L** | A major workstream; among the largest effort consumers in the engagement |
| **XL** | Dominates the engagement — *no MVP role is assigned XL* |

### 10.2 Effort assumptions

| # | Assumption | Basis | If it changes |
|---|---|---|---|
| A1 | **One H1 or H2 property** per engagement | §1.1 | H3 is out of the MVP; a second property is a second engagement |
| A2 | **Sample copy for a limited number of critical sections** only | Owner Decision #17 (§1.2) | More sections move the sample-copy producer from S toward M |
| A3 | **No implementation** — nothing built in booking tools, a website CMS or a messaging platform | §1.1–§1.2 | Implementation is out of scope, not a larger band |
| A4 | **One revision round** per client-approved output, unless the owner sets a different revision policy | Revision policy open (§8 #13; `Draft 41` §9 #14) | Each extra round raises the content strategist, sample-copy and owner bands |
| A5 | **The client supplies basic channel-mix data** from its own systems | Data sources vary by client (V2) | Extra sources or access friction move analytics/reporting from M toward L |
| A6 | *Additional:* AI assistance drafts analysis, strategy, blueprint and sample copy; **every client-facing output still gets owner review** | §6 Q2; delegability ceiling (§4) | Delegated review would lower the owner band — no delegate exists today |
| A7 | *Additional:* bands are for the **full path** — M2 finds an (a) or (b)-messaging root cause, so M3–M6 are produced. The redirect path is in §10.4 | Diagnostic gate (§1.1; `Draft 41` QG1) | — |
| A8 | *Additional:* the **standard MVP package**, with no client-specific scope customization | §4, offer engineer row | Customization moves the offer engineer from XS to S |

### 10.3 Role estimates

| Role | MVP responsibilities | Required for | Effort band | Assumptions | Blockers |
|---|---|---|---|---|---|
| **Owner / strategist** | M2 root-cause verdict (senior-only, QG1) · M7 redirect decision · audit readout and blueprint approvals with the client · Class 3 approvals · review of every AI-assisted client-facing output · client relationship | **Both** | **L** | A4, A6. Senior-only work does not delegate (§4). *This band covers the owner role only — today the owner also performs the roles below (§10.6)* | Weekly delivery time unknown (Q7) · "dominant" and the mixed-finding rule undefined (`Draft 41` §9 #9), so a contested verdict takes longer · no second reviewer |
| **Offer engineer** | Scope changes only — adjusting the package when a client needs something outside the standard MVP | Both, *conditional* | **XS** | A8 | None for a standard engagement. Commercial shape (G6) is design work, not delivery effort |
| **Content strategist** | M3 Direct Booking Message Strategy · M4 journey structure, page/message hierarchy and key messaging blocks · M5 Basic Direct-Booking Content Plan · QG7 positioning check | **Blueprint** | **M** | A2, A3, A4, A6. Blueprint only — no calendar production, no D4 content | Runs only after an (a) or (b)-messaging verdict · per-client target definition undefined (`Draft 41` §9 #8) · launch archetype scope open (`Draft 41` §9 #18) |
| **Light copy / sample-copy producer** | Sample copy for a limited set of critical sections inside M4 · one revision round · self-check against QG2 (no outcome claims), QG3 (benchmark labels) and QG5 (no price) | **Blueprint** | **S** | A2, A4, A6. May be performed by the content strategist rather than a separate role | Which sections are "critical" is an assumption (A2), not a decision · proof method BLOCKED, so samples carry no outcome claims |
| **Analytics / reporting** | Data ingestion and channel-mix analysis · M1 Audit Findings Snapshot · evidence for the M2 classification · M7 evidence pack when redirecting · M6 Measurement Plan (baseline and measurement design) · QG6 data integrity | **Both** | **M** | A5, A6. No monthly reporting (retainer deferred); client-system data only | **Data-source range unresolved (V2, §8 #20) — this band could become L** · audit scope and duration open (`Draft 41` §9 #13) · per-client target undefined for M6 (`Draft 41` §9 #8) |
| **Delivery QA** | Reduced gate set across M1–M7 — QG1, QG2, QG3, QG5, QG6, QG7 · completeness check before the audit readout and before blueprint handover | **Both** | **S** | A4. Checks, not rework; QG4 and QG8 are not triggered while nurture is deferred | No named reviewer (§4) — if the owner self-reviews, this effort lands on the owner |
| **Legal / compliance review path** | Audit-data handling terms (§3.1) · client contract terms | **Both** | **BLOCKED — not estimated** | — | No counsel engaged (`OWNER_INPUT_NEEDED.md` item 59; §8 #6) · `legal-counsel-router` routes, it does not review · contract template with data terms missing (`Draft 41` §9 #15) |
| **Design support** | None in the MVP — no produced assets | Neither | **Deferred — not estimated** | A3 | Returns with content production · image-generation runway and Canva authentication (§8 #14) |
| **Automation / booking-journey advisor** | None by default. **Trigger: the audit finds a booking-journey root cause.** A messaging-side (b) finding keeps journey direction inside M4 (content strategist), with at most a light advisor review. A technical (b) finding is a redirect (M7), and the redirected work is out of scope | Blueprint, *only if triggered* | **Deferred — not estimated** · *XS if triggered and the owner wants a separate review* | A3 — no booking-tool or CMS work in any case | No nurture platform registered (§3) · no engineered destination for a technical (b) redirect (§2, P4b) |

### 10.4 Effort by delivery path

| Role | Full path — (a) or (b)-messaging verdict: M1–M6 | Redirect path — (c), (d) or technical (b): ends at M1, M2, M7 |
|---|---|---|
| Owner / strategist | **L** | **M** — verdict, redirect decision and readout; no blueprint approvals |
| Offer engineer | XS | XS |
| Content strategist | **M** | — |
| Sample-copy producer | S | — |
| Analytics / reporting | **M** | **M** — audit analysis and evidence pack are most of the band; M6 drops out |
| Delivery QA | S | XS — QG1, QG3 and QG6 only |
| Legal / compliance | BLOCKED | BLOCKED |
| Design support | Deferred | Deferred |
| Automation / booking-journey advisor | Deferred · XS if triggered | — (a technical finding is a redirect) |

### 10.5 G2 readiness result

**◐ G2 — PARTIAL, not passed** (§7).

- **Done:** a labelled band now exists for every active MVP role except legal. V1's unit is "hours *or effort units*", so owner-confirmed bands can satisfy it.
- **Why it is not passed:**
  1. **Legal review path unresolved** — the one required role with no estimate (G5; §8 #6).
  2. **Revision policy unresolved** — every client-approved output's band assumes one round (A4; §8 #13).
  3. **Data-source range unresolved** — the analytics band could move from M to L (A5; V2; §8 #20).
  4. **Bands not yet owner-reviewed** — V1 needs an estimate the owner stands behind.
- **Not this step:** converting bands to hours or money. That comes later, for cost-to-deliver, and before any `TEST_FIXTURE` figure (G7).

### 10.6 Capacity implication — not a capacity claim

- **Every active role falls on one person today.** §4 assigns no one but the owner, so the owner's real load for one engagement is the stack of active bands: **L** (owner) + **M** (content strategist) + **M** (analytics) + **S** (sample copy) + **S** (QA) + **XS** (offer engineer), with AI assistance drafting.
- **One MVP client at a time appears plausible for a solo owner with AI assistance — on these assumptions only.** No role reaches XL. The execution-heavy work (analysis, strategy, blueprint, sample copy) is the kind AI can draft. And the MVP excludes the workstreams most likely to add sustained load: content production, implementation, nurture, the retainer and H3.
- **What would make it implausible:** too little weekly owner time (Q7 unanswered) · more than one revision round (A4) · data-access friction beyond basic channel-mix data (A5) · review load — AI drafting does not remove owner review (A6).
- **Concurrency is not assessed.** There is no basis for two or more MVP clients at once. The owner band is L per engagement, and its senior-only part does not delegate, so concurrency is the first thing to test once Q7 is answered.
- **Capacity is not a start condition on its own.** No engagement can begin while the offer is Not Quotable and the audit-data terms have no review path (G5).
- **Not a capacity figure.** G3 stays ❌ and Q1 is unanswered. **The owner must confirm before any capacity is recorded.**

### 10.7 Open decisions — what moves G2 from partial to passed

**Required for G2 to pass:**

| # | Decision | Why G2 needs it | Decider | Reference |
|---|---|---|---|---|
| 1 | **Name a review path for the audit-data handling terms** — and whether review is once per template or per engagement | Legal is the only required role with no estimate | Owner + Legal (10) | §8 #6; item 59 |
| 2 | **Revision policy** — confirm one round per client-approved output, or set another | Changes the content strategist, sample-copy and owner bands | Owner + Client Success (07) | §8 #13; `Draft 41` §9 #14 |
| 3 | **Minimum audit data set** — what counts as basic channel-mix data, and the data-source range an MVP audit accepts (below it, QG1 already returns "insufficient data") | Decides whether analytics stays M | Owner + Audits & Diagnostics (14) | V2; §8 #20 |
| 4 | **Owner review of the §10.3 bands** — confirm, adjust or reject each | V1 must be an estimate the owner stands behind | Owner | §10.3 |

**Worth settling alongside, but not required for G2:** a working limit for "critical sections" (A2 — keeps sample copy at S) · whether the owner may self-review delivery QA (lands on G3) · weekly owner delivery time (Q7 → G3) · audit scope and duration (`Draft 41` §9 #13 → timeline) · the "dominant" definition (`Draft 41` §9 #9 → verdict effort).
