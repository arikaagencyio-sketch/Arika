# Hospitality Revenue Content OS — Delivery Capacity and Cost Model Worksheet

> ⚠️ **INTERNAL WORKSHEET · NOT QUOTABLE · NO PRICES.**
> This file names **what must be known** before any test price or price floor can exist. It contains **no price, no currency, no amount, no rate, no margin and no capacity figure** — every quantity below is a **variable to be supplied**, not a value. §10 adds **relative effort bands (XS–XL), owner-approved for internal MVP planning only** — not hours, not money. §12 sets **internal planning hours** from an owner-approved band-to-hours scale — hours only, **no money**.

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

### 1.3 MVP revision policy — owner decision (2026-09-13)

✅ **Approved for the MVP only — internal delivery-scope policy, not public contract language.**

> **Policy:** **one included revision round per client-facing output.** Additional rounds are **not approved** for the MVP test model. **Any exception requires owner approval before delivery.**

**Applies to:** M1 Audit Findings Snapshot · M2 Leakage Root-Cause Classification · M3 Direct Booking Message Strategy · M4 Booking Journey Copy/Content Blueprint · M5 Basic Direct-Booking Content Plan · M6 Measurement Plan · M7 Redirect Recommendation.

| A revision corrects | A revision does not include |
|---|---|
| Accuracy · clarity · fit · client-specific context | New scope or new deliverables · implementation · full content production · nurture execution · website, CMS or booking-tool work · retainer activity |

**What follows:**
- **Effort assumption A4 becomes policy** (§10.2). The §10 bands already assumed one round, so **no band changes**. The analytics/reporting band now explicitly carries one round on M1, M2, M6 and M7.
- **Flagged, not decided:** correcting M2's accuracy is in scope, but a revision that changes the root-cause class goes back through QG1 and can switch the engagement between the blueprint path and the redirect path (§10.4).
- **Not contract language.** Client-facing terms need the contract template and a Legal (10) review path (`Draft 41` §9 #15; G5).
- **Still open:** SLAs, approval windows and timelines (`Draft 41` §9 #14), and revision policy for the full offer (build beyond Phase 1, retainer).

### 1.4 MVP minimum audit data set — owner decision (2026-09-13)

✅ **Approved for INTERNAL DESIGN ONLY.** What a client must supply before an MVP audit, and what happens when part of it is missing.

| # | Data item | Detail | If missing |
|---|---|---|---|
| MD1 | **Room-night bookings by channel — last three months** | Direct website · phone/email/WhatsApp direct · OTA · corporate/group/other if available | **Audit cannot proceed** |
| MD2 | **Booking revenue by channel — last three months**, if available | If unavailable, use room-night share only | Audit proceeds; **revenue leakage marked unquantified** |
| MD3 | **OTA commission rate**, or an effective commission estimate | If unknown, record as unknown — **never invented** | Recorded as unknown |
| MD4 | **Current direct-booking path** | Website/booking-engine URL · screenshots or notes on the booking journey · main direct-booking CTA · any active landing or offer page | **Audit cannot proceed** |
| MD5 | **Existing guest communication assets** | Booking confirmation email, pre-arrival message, WhatsApp scripts — each if available. Reviewed only; **no new nurture implementation** | *No sufficiency rule set* |
| MD6 | **Current content and campaign assets** | Website homepage or rooms page · any direct-booking promotion · recent social or email campaign examples if available | *No sufficiency rule set* |
| MD7 | **Buyer interview** | One interview with the GM, Owner/MD or Revenue Manager, confirming perceived OTA dependency, direct-booking blockers and operational constraints | **Desk review only, not a diagnosis** |
| MD8 | **Constraints** | Tool access limitations · brand/legal approval needs · whether pricing/rate strategy or booking-engine tech problems are suspected | *No sufficiency rule set* |

**Data sufficiency rule:**
- **MD1 and MD4 are required** — without them the audit cannot proceed. *Recorded from "if #1 and #4 are missing" and read as: either one missing stops the audit. Confirm.*
- **MD2 missing:** the audit proceeds on room-night share only and **cannot quantify revenue leakage**.
- **MD7 missing:** the audit proceeds **only as a desk review, not a diagnosis**.
- **Pricing/rate strategy or booking-engine tech dominant:** **redirect (M7) rather than sell the Direct Booking Engine.** This matches the §1.1 diagnostic gate, which also redirects a dominant (d) tech-stack/integration finding.

**What follows** — consequences of existing rules, not new decisions:
- **A desk review delivers M1 without a signed M2 verdict.** QG1 requires a signed verdict, so the blueprint phase (M3–M6) does not open. What else a desk review delivers, and whether it is offered at all, is open (§8 #21).
- **MD3 unknown leaves commission cost unquantified too.** No sector benchmark substitutes for it (QG3), and an effective commission estimate is recorded as a *client-supplied estimate*, not a measured figure (QG6).
- **Flagged, not decided: three months is an audit window, not a seasonal baseline.** M6 uses a seasonally comparable baseline (§1.1, M6), which three months may not supply (§8 #22).
- **Flagged, not decided: guest communication assets (MD5) may contain guest personal data.** The audit-data handling terms still have no review path (G5). *This file does not assess the law.*

### 1.5 MVP commercial shape — owner decision (2026-09-14)

✅ **Approved for INTERNAL MVP DESIGN ONLY — a diagnostic-first, two-stage, audit-gated shape.** This is an internal packaging decision: **no prices, no currency, no price band, no test figures, no fee credit, no payment terms, no quote language.** The offer remains **Working Hypothesis / Not Quotable.**

| | Stage 1 — Gateway Audit | Stage 2 — Phase 1 Direct Booking Message/Journey Blueprint |
|---|---|---|
| **When** | **Always first** | **Only if Stage 1 confirms** a content/messaging or booking-journey messaging root cause |
| **Produces** | M1 Audit Findings Snapshot · M2 Leakage Root-Cause Classification | M3–M6 · M7 only where a redirect or limitation needs documenting |
| **Governed by** | §1.4 minimum audit data set · the diagnostic gate (QG1) | Blueprint limits (§1.1–§1.2) · revision policy (§1.3) |
| **Excludes** | — | Full content production · implementation · nurture · retainer · booking-tool or website work |
| **Stops the MVP** | A pricing/rate strategy, booking-engine technology, integration or other non-content root cause — **the MVP does not proceed to Stage 2** | — |

**Commercial rule — the MVP is audit-gated:** the audit controls whether the blueprint stage is delivered.

**Two readings to confirm** (§8 #24) — both affect what gets delivered, not whether G6 passes:
- **Where M7 sits on a redirect.** The decision lists M7 under Stage 2, but a redirect finding stops the MVP before Stage 2 opens. §1.1 and the redirect path in §10.4 place the redirect recommendation at the end of the audit. *Recorded as: M7 closes Stage 1 when the MVP stops on a redirect, and appears in Stage 2 only for a limitation or a secondary redirect.*
- **Severity does not gate Stage 2.** The decision opens Stage 2 on root cause alone. `Draft 41` §11.3's proposed rule — never approved — also required L3 severity and left L2 "disposition OPEN". L2/L3 thresholds are undefined (§8 #12), so a severity gate could not operate today. *Recorded as: for the MVP, severity does not gate Stage 2.*

**Consistent with earlier decisions:**
- **A desk review cannot open Stage 2** — without the buyer interview (MD7) there is no diagnosis to confirm a root cause (§1.4).
- **Capacity** — §6.1's one client at a time already covers both stages for that client.
- **Effort** — Stage 1 alone is §10.4's redirect path; Stage 1 followed by Stage 2 is the full path.

**Still blocked — unchanged by this decision:** prices · price band · cost-to-deliver in hours and costs · hotel floors · test figures (G7) · audit-fee credit policy (`Draft 41` §9 #4) · payment terms and contract language (Legal (10); G5).

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
| **Owner / strategist** | Senior Diagnostic Reviewer · Account Lead (default) | ● | ● | ● | **Required** | ✅ **In** — M2 verdict, M7 redirect, approvals | **Yes** — the agency owner (Offer (02) owner of record, `OFFER_OS.md`: Mary Thuo). **Confirmed as the MVP delivery and capacity owner, solo with AI (§6.1, provisional)**; not a full-offer assignment | Weekly time available for delivery after running the agency; how many senior-only tasks (verdict, redirect, approvals) one engagement consumes |
| **Offer engineer** | — (Offer 02 function) | ◐ | ◐ | — | **Conditional** — package design and scope changes, not routine delivery | ◐ Conditional — scope changes only | **Yes** — owner + advisory `offer-oeos-engineer`; no separate person | How often a client needs scope customization beyond the standard package |
| **Content strategist** | Revenue-Content Strategist | ◐ | ● | ◐ | **Required** for P2 | ✅ **In** — M3; M4 structure, hierarchy and messaging blocks; M5 | **No** | Effort per strategy + calendar; how much AI drafting reduces it |
| **Copy / content producer** | Content Producer · Conversion Copywriter | — | ● | ● | **Required** for P2, P3 | ◐ **Light** — sample copy for critical sections only (§1.2); no full copy, no production. Could sit with the content strategist rather than a separate role | **No** | Output per cycle; revision load · *MVP:* how many critical sections are sampled; review rounds on samples |
| **Design support** | — (Design 19) | — | ◐ | ◐ | **Conditional** — when content or landing pages need visuals | ⏸ **Deferred** — no production in the MVP | **No** | Image-generation runway was near-exhausted when last verified (`TECHSTACK_OS.md` §3, 2026-07-15); Canva authentication lapsed (same date) |
| **Automation or booking-journey advisor** | Lifecycle Engineer · journey-messaging side of Conversion Copywriter | — | ◐ | ◐ | **Conditional** — nurture needs consent + a platform; technical engine work is a redirect, not this role | ⏸ **Deferred** — nurture excluded; no booking-tool or CMS implementation (§1.2); journey-messaging direction sits with the content strategist in M4 | **No** | No nurture platform registered; every automation needs an approval-matrix row (`AUTOMATION_APPROVAL_MATRIX.md`) |
| **Analytics / reporting** | Audit Analyst · Reporting Analyst | ● | ◐ | ● | **Required** | ✅ **In** — M1, M2, M6; no monthly reporting | **No** | Data-access effort per client; whether pulls can be automated given integration-type stack chaos |
| **Legal / compliance review** | — (Legal 10) | ◐ | ● | ◐ | **Required** once client data or client-facing sends exist | ◐ **Reduced** — audit-data handling terms; no consent review while nurture is deferred; sample copy carries no claims (QG2), so no claims review | **Blocked** — no counsel engaged (`OWNER_INPUT_NEEDED.md` item 59); `legal-counsel-router` routes, it does not review | Review turnaround; whether review is per template or per engagement |
| **Delivery QA** | QA gates (`Draft 41` §8) · Operations (08) delivery QA | ● | ● | ● | **Required** | ✅ **In** — reduced gate set (§3.1); sample copy adds QG2, QG3, QG5 and QG7 checks (§1.2) | **MVP: the owner — self-review, confirmed 2026-09-13 (§10.8)** · advisory `operations-delivery-qa` exists · full offer: no named human reviewer | MVP: owner self-review (§10.8) · full offer: whether a second person is needed |

**Two structural constraints that bound every row:**
- **The delegability ceiling.** Senior-expert-only work — the audit verdict, redirect decisions, Class 3 approvals — stays with one person however many agents exist (`11_HR_People_Ops/PEOPLE_DOCTRINE.md`; `Draft 41` §12 Phase 12). More agents raise the volume arriving at that ceiling, not the ceiling.
- **Delegation is itself an open decision.** Any human help beyond solo + AI is an HR (11) engagement question, including the misclassification test for creative contractors (`hr-engagement-classifier`).

---

## 5. Cost-to-deliver inputs needed

**Variables only.** Every "value" is to be supplied by the named source; none is estimated here.

| # | Variable | Unit | Applies to | Who supplies | Known now? |
|---|---|---|---|---|---|
| V1 | **Effort by role** | Hours or effort units per role, per package | P1, P2, P3, P4 hand-off | Owner, with Operations (08) | ◐ **MVP bands owner-approved (§10.8)** for internal planning only; legal not estimated; planning hours set from the owner-approved scale (§12), excluding legal |
| V2 | **Number of audit data sources** | Count per client (booking engine, PMS/CRS exports, channel manager, OTA extranets, web analytics, email/CRM) | P1, P3 | Per client, at Qualification · ✅ MVP minimum data set decided (§1.4) | ◐ **MVP minimum defined (§1.4):** MD1 and MD4 required; the actual source count still varies by client stack |
| V3 | **Number of pages / assets / messages** | Count per build; count per retainer cycle | P2, P3 | Owner — from minimum viable scope (§6 Q5) | ❌ |
| V4 | **Number of review rounds** | Rounds per deliverable | P1–P3 | Owner — ✅ MVP policy set (§1.3); full-offer revision policy open (`Draft 41` §9 #14) | ◐ **MVP: one included round per M1–M7 output** (§1.3); P2 beyond Phase 1 and P3 open |
| V5 | **Tool / API cost categories** | Categories only (below) | P1–P3 | Tech Stack (13) | ◐ MVP categories identified (§5.1–§5.2) — G4 passed at category level; **costs and vendors unknown** |
| V6 | **Design / content production load** | Assets per build; assets per retainer cycle | P2, P3 | Owner + Design (19) | ❌ |
| V7 | **Reporting cadence** | Reports per period | P3 | `Draft 41` — **monthly** [RUN]; effort per report unknown | ◐ cadence only |
| V8 | **Compliance / legal review requirement** | Reviews per engagement; reviews per new template | P1–P3 | Legal (10) | ❌ blocked on counsel |
| V9 | **Owner time requirement** | Senior-only effort per engagement (verdict, redirect, approvals, client relationship) | P1–P3 | Owner | ◐ **MVP: 11–18 hours (L) on the audit + blueprint path, 6–10 hours (M) on the audit-only path** (§12.3) — planning hours, not capacity |
| V10 | **H-band and severity scaling** | How V1–V9 change from H1 → H3 and L1 → L3 (qualitative first) | P1–P3 | Owner (axes approved by Decision 71) | ❌ |

**MVP effect on these variables — values still blank.** V3 counts blueprint items (journey structure, page/message hierarchy, key messaging blocks) plus the sections given sample copy — not finished pages, messages or produced assets (§1.2) · V4 is one included revision round per M1–M7 output (§1.3) · V6 design load is deferred with production · V7 does not apply until the retainer returns · V8 narrows to audit-data handling terms · V10 narrows to H1 → H2, since H3 is out of the MVP. **No hours or cost value has been entered** — relative effort bands only, in §10.

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

### 5.1 MVP tool-category check against Tech Stack (13) — 2026-09-13

**Internal design only. Categories, not costs.** Checked against `13_Tech_Stack/TECHSTACK_OS.md` §3 (Capability Registry) and §9 (standing risks) **as written — no connection was re-verified in this pass.** Actual tool costs remain **unknown**, and nothing here is converted into prices, floors or test figures. No subscription or vendor commitment is made.

**Can the MVP proceed on existing or manual tools?**

| MVP work area | Existing / manual path | Tech Stack reality | Result |
|---|---|---|---|
| **Audit data collection and review** (MD1–MD3, MD5, MD6, MD8) | Client supplies exports and assets; received by agency email; reviewed with AI assistance | Agency mailboxes on Zoho — mail works, product and plan unconfirmed (§9) · Claude (§3) · **no spreadsheet or data-analysis tool registered** · **no storage for client files registered** | ◐ **Partly** — receipt and AI-assisted review exist; the working analysis tool and file storage do not |
| **Website and booking-path review** (MD4) | Manual review of the client's public website and booking engine; screenshots and notes | No account-based tool required | ✅ **Yes — manual** |
| **Document drafting** (M1–M5, M7) | AI-assisted drafting, owner-edited | Claude available: owner's Claude Pro plan (§3, Claude Design row, 2026-07-03) and the API key verified by use for manual runtime calls only (§3, 2026-09-13) · **no client-deliverable document tool or format registered** — no word processor (Microsoft 365 rejected on cost, §9), Canva unauthenticated, Notion registered for content briefs and last verified 2026-07-03 | ◐ **Partly** — drafting exists; the tool or format clients receive is not chosen |
| **Reporting / measurement-plan drafting** (M6) | Same drafting path; M6 is a plan document, not a dashboard; client-system data only (QG6) | As above · no agency analytics tool needed — baseline data comes from client exports | ◐ **Partly** — drafting exists; baseline figures depend on the unregistered analysis tool |
| **File storage / versioning** | — | **Not registered.** This repository is not a place for client data: an auto-sync job commits every change, and the folder sits in OneDrive, which §3 does not register | ❌ **Missing** |
| **Owner QA / self-review** | Manual checklist against the reduced gate set (§3.1; `Draft 41` §8) | No tool required · advisory `operations-delivery-qa` exists and is not needed | ✅ **Yes — manual** |

**Other MVP needs surfaced by the check:**

| Need | Tech Stack reality | Result |
|---|---|---|
| **Buyer interview** (MD7) — scheduling, the call, notes | No calendar connected (Google Calendar named, not connected) · no video-call tool registered · transcription/recording gap fully open (§9). A phone or in-person interview with typed notes is possible manually | ◐ **Ambiguous** — manual path possible; channel not chosen. Any recording would touch data handling (G5) |
| **Client correspondence** — sending outputs and data requests | Agency mailboxes on Zoho — working, plan unconfirmed (§9) | ✅ **Identified** — ordinary email, **not** nurture |
| **Engagement tracking** | ClickUp CRM built; Engagement / Project list live-verified 2026-07-15 (§3) | ✅ **Identified** — optional at one client at a time |
| **Client analytics** | The MVP uses client-supplied exports (§1.4); no agency analytics tool needed | ✅ **Identified** — client exports |

**Not required for the MVP** — deferred with their workstreams:
- **Email / WhatsApp nurture platform** — ⏸ **still deferred.** Nurture implementation is out of MVP scope (§1.1); ManyChat is proposed with no account created, and no email-marketing platform is registered. Ordinary client email is not nurture.
- **Image generation** (KIE.ai / OpenArt) and **design assembly** (Canva) — design support deferred.
- **Landing-page hosting** — no implementation.
- **Content / brief system** (Notion) — optional, not required.

**For G5, not G4:** every tool that touches client data is a sub-processor. `10_Legal/templates/DPA.md` Annex B drafts nine rows — ClickUp, Zoho Books, Anthropic (Claude), Notion, Canva, OpenArt, KIE.ai, Vercel and an unnamed mailbox provider — with every location and transfer mechanism marked "to verify". Zoho mail is not named, and the MVP's storage, spreadsheet and video-call tools are not listed (§11.3). *Corrected 2026-09-14: this line said Annex B lists only ClickUp, repeating a stale sentence in `TECHSTACK_OS.md` §9.*

**Verify before first use.** Tech Stack treats every row as a claim with a shelf life: ClickUp (2026-07-15), Notion (2026-07-03) and the Zoho mail plan need a live check before the first MVP delivery. This is not a G4 blocker — G4 identifies categories; it does not verify connections.

**G4 result at the time of the check — ◐ PARTIAL.**
- **Identified (six categories):** AI-assisted drafting (Claude) · website and booking-path review (manual) · owner QA (manual) · client correspondence (Zoho-hosted email) · engagement tracking (ClickUp) · client analytics via exports. The nurture platform is confirmed not required.
- **Missing or ambiguous — exactly four** (§8 #23):
  1. **Client-data file storage and versioning** — no tool registered.
  2. **Spreadsheet / data-analysis working tool** for channel-mix analysis and M6 baseline figures — none registered.
  3. **Client-deliverable document tool or format** for M1–M7 — not chosen.
  4. **Buyer-interview channel and notes** (MD7) — manual path possible; channel not chosen; no recording tool registered.

*Superseded the same day: §5.2 closes all four gaps at category level, and G4 passes for MVP tool-category identification only.*

### 5.2 MVP tool choices — owner decision (2026-09-13)

✅ **Approved as PROVISIONAL tool choices for INTERNAL MVP DESIGN ONLY.** These are categories and handling rules — **not vendors, not costs, and not approval for real client use.** `TECHSTACK_OS.md` is unchanged: no choice here registers a tool.

| # | Gap (§5.1) | Provisional choice | Handling rules | Still open |
|---|---|---|---|---|
| 1 | **Client-data storage and versioning** | **A dedicated client folder outside this git repository** (called Agency.Repo in the decision) | **Never inside the repository:** client data, hotel exports, guest data, interview notes or deliverable drafts | **The storage platform** — subject to legal/privacy review (G5) before real client use |
| 2 | **Spreadsheet / data analysis** | **A spreadsheet workbook** for channel share · revenue by channel, if supplied (MD2) · the OTA commission rate or client-supplied estimate (MD3) · support for the M2 leakage classification · M6 measurement planning | **App not chosen.** Excel, Google Sheets or another spreadsheet tool may be approved later, but **no spreadsheet vendor is registered** in `TECHSTACK_OS.md` §3, so none is named as approved. The workbook holds client data and lives in the client folder (#1) | The app · legal/privacy review if the app is cloud-hosted |
| 3 | **Client-deliverable format** (M1–M7) | **Document-format deliverables** — one compiled client-facing document, or clearly separated sections for M1–M7 | Public template design and production formatting **not decided** | Template design · production formatting · authoring app |
| 4 | **Buyer interview** (MD7) | **Phone, video call or in person, with typed notes** | **Recording is not required and not approved by default.** If an interview is ever recorded, it needs **explicit client consent and legal/privacy review first.** Notes are client data and live in the client folder (#1) | The video-call app, if one is used · recording stays unapproved |

**What this settles:** **G4 passes for MVP tool-category identification only** (§7). Every MVP work area in §5.1 now has a category-level path, and the nurture platform remains not required.

**What stays open:**
- **Actual tool costs** — unknown; not converted into prices, floors or test figures.
- **Vendors** — none chosen or registered for storage, spreadsheets or video calls. No subscription or vendor commitment is made.
- **Legal / privacy approval** — the storage platform, any cloud-hosted spreadsheet or video-call app holding client data, the existing tools that already touch client data (Zoho mail, Claude), and any interview recording all wait on a legal review path. **G5 stays blocked**, and the draft Annex B neither lists the MVP's storage, spreadsheet or video-call tools nor names Zoho mail (§11.3).
- **Live connection checks** — ClickUp, Notion and the Zoho mail plan still need verifying before first use (§5.1).

**Flagged — "outside the repository" is necessary, not sufficient.** This repository already sits under OneDrive, which `TECHSTACK_OS.md` §3 does not register. A client folder placed elsewhere under OneDrive would still be on an unreviewed platform, so where the folder lives is part of the storage-platform review.

---

## 6. Capacity questions — for the owner, before test pricing

| # | Question | Why it gates pricing | Who can answer |
|---|---|---|---|
| Q1 | ~~**How many hotels can be handled at once** — separately for audits in flight, builds in flight, and retainers active?~~ ✅ **Answered for the MVP, provisionally (§6.1, 2026-09-13): one H1/H2 MVP client at a time**, owner solo + AI — no concurrent audits or blueprints; no retainers active. *Full offer (builds beyond Phase 1, retainers) unanswered* | A floor that ignores capacity authorizes overselling against a fiction (`operations-capacity-planner`) | Owner + Operations (08) |
| Q2 | **What is solo-owner work vs AI-assisted work?** And does AI-assisted work still consume owner review time? — ◐ *partly answered (§6.1): every client-facing output requires owner review, so AI-assisted work does consume owner review time; the split is otherwise unmeasured* | AI-assisted drafting is not free if every output needs senior review | Owner |
| Q3 | **What can be delegated — and to whom?** No delegate exists today | Delegation changes cost structure and triggers HR (11) classification questions | Owner + HR (11) |
| Q4 | **What must wait for another department?** Legal (10): contract, DPA, consent · Operations (08): capacity model, scheduling · Content (04): publishing gate, brief pipeline · Design (19): image runway, Canva authentication · Tech Stack (13): nurture platform | A dependency with no date makes a delivery timeline — and so a price — unfounded | Each named department |
| Q5 | ~~What is the minimum viable delivery scope?~~ ✅ **Answered for the MVP, internal design only (§1.1–§1.2, 2026-09-13):** audit + Entry Build Phase 1 blueprint with sample copy, H1/H2 only; nurture, retainer, H3, D4 production and booking-tool/CMS implementation deferred. *Full-offer scope (P2 beyond Phase 1, P3) not chosen* | Scope is the largest single driver of V1, V3 and V6 | Owner (Offer 02) |
| Q6 | **Does an H3 engagement count as more than one unit of capacity?** (2–5 properties, multiple stakeholders) — ⏸ *deferred: H3 is out of the MVP (§1.1); **H3 capacity not approved** (§6.1)* | If H3 consumes several slots, its cost cannot be one band's cost | Owner |
| Q7 | **How much owner time per week is actually available for client delivery?** — ⏳ *still open: §6.1's cap is a client count, not a weekly time budget* | V9 has no ceiling without it | Owner |
| Q8 | **Does demand cluster by season?** Low season is the buying window (Plugin P13), and client approvals slow in peak season (`Draft 41` §8) | Sales and delivery load may peak together | Owner + Sector (01) |

### 6.1 MVP capacity rule — owner decision (2026-09-13)

✅ **Approved as a PROVISIONAL capacity assumption — not proven operating capacity.**

> **Rule:** at most **one H1/H2 MVP client at a time**, delivered by the **owner solo, with AI assistance**. A second client's engagement does not start while the first client's MVP is in flight — its audit, and its blueprint where the verdict allows one.

| Condition | Detail |
|---|---|
| **Scope** | Approved MVP only — Gateway audit + Entry Build Phase 1 blueprint, M1–M7 (§1.1–§1.2) |
| **Properties** | H1/H2 only |
| **Delivery model** | Owner solo + AI assistance; no delegate (Q3) |
| **Review** | **Every client-facing output requires owner review** — §10.2's assumption A6 is now a rule |
| **Excluded** | H3 groups · retainer delivery · email/WhatsApp nurture implementation · website, CMS or booking-tool implementation |
| **Status** | Provisional assumption — **not proven operating capacity** |
| **Revisit** | **Required after the first real MVP delivery** — compare actual owner review load, revision rounds and data-access friction against §10.2 A4–A6 and the §10.3 bands |

**Not approved:**
- ❌ **Two or more concurrent MVP clients** — including one client's audit overlapping another client's blueprint.
- ❌ **H3 capacity** — no H3 engagement of any size; whether H3 uses more than one unit (Q6) is unanswered.
- ❌ **Capacity for anything outside the MVP** — retainer, nurture, implementation, or the full offer.

**What this does not settle:**
- **Weekly owner delivery time (Q7)** — the rule is a client count, not a time budget.
- ~~**The §10 effort bands are still unreviewed** (G2 partial). If review moves a band materially, revisit this rule before the first delivery.~~ ✅ **Bands owner-approved unchanged 2026-09-13 (§10.8)**, so this rule stands as recorded; revisit after the first real MVP delivery.
- **No timeline or SLA** follows from it (`Draft 41` §9 #13–#14).
- **No start condition.** No client can begin while the offer is Not Quotable and the audit-data terms have no review path (G5).
- **Not a price input on its own**, and not quotable.

---

## 7. Pricing-test readiness gate

**Rule:** no `TEST_FIXTURE` price figure may be written anywhere until **every** item below is ✅. Passing this gate permits **internal test figures only** — it does not create a floor, does not unblock Phase 11 by itself, and does not make the offer quotable.

| # | Gate item | Status (2026-09-13) | Evidence required to pass | Owning department |
|---|---|---|---|---|
| G1 | **Delivery scope chosen** (minimum viable P1/P2/P3 scope) | ✅ **Passed — MVP only** (§1.1–§1.2, 2026-09-13) · **not passed for the full offer** — P2 beyond Phase 1 and P3 scope not chosen | Q5 answered in writing — done for the MVP, including M4 depth (#17) and the D4 exclusion (#18) | Offer (02) |
| G2 | **Role effort estimated** (V1 for every required role, per package) | ◐ **PARTIAL — blocked only by the legal review path / legal effort estimate** (MVP only, 2026-09-13): ✅ bands owner-approved for internal MVP planning (§10.8) · ✅ revision policy (§1.3) and minimum audit data set (§1.4) decided · ❌ legal/compliance BLOCKED, not estimated | V1 filled, labelled estimate — met for every MVP role except legal; legal effort is estimated once a review path exists (G5; questions packaged in §11); one §10.7 decision remains | Offer (02) + Operations (08) |
| G3 | **Capacity owner assigned** | ✅ **Passed — MVP only, provisional** (§6.1, 2026-09-13): the owner delivers solo with AI and holds the cap; Q1 answered as one H1/H2 MVP client at a time · **not passed for the full offer** · not proven capacity — revisit after the first real MVP delivery | A named owner for delivery capacity; Q1 answered — both met within MVP scope | Operations (08) |
| G4 | **Tool cost categories identified** | ✅ **Passed — MVP tool-category identification only** (§5.1–§5.2, 2026-09-13): six categories identified by the check; the four gaps closed by provisional owner choices (§5.2); nurture platform not required. **Still open:** actual tool costs · vendors · legal/privacy approval (G5) · live connection checks. Not passed for the full offer; not converted into prices | Every MVP category confirmed — met at category level (§5.2); the nurture platform returns with nurture | Tech Stack (13) |
| G5 | **Legal / compliance review path identified** | ❌ **Blocked — no engaged counsel for these matters** (§11.1): Ndwiga Law Advocates LLP is named, both letters of engagement are unsigned, and no drafted scope covers template review or the sub-processor register (item 59) · **scope reduced for the MVP** (no consent sends) · **scope added 2026-09-13 (§5.2):** the client-data storage platform, any cloud-hosted tool holding client data, and any interview recording · **review packet prepared 2026-09-14 (§11) — not a review path** · **owner scope decision recorded 2026-09-16 (item 59): the counsel scope is to be narrowed before engagement — G5 is NARROWED, NOT PASSED**, because no engagement is active, nothing has been sent or signed and no document has been reviewed | A named review path for contract and audit-data terms; consent review returns with nurture | Legal (10) |
| G6 | **Audit / build / retainer commercial shape selected** | ✅ **Passed — H1/H2 MVP only** (§1.5, 2026-09-14): diagnostic-first, two-stage, audit-gated — Stage 1 Gateway Audit always first; Stage 2 blueprint only on a confirmed content or journey-messaging root cause. **Not passed for the full offer** (build beyond Phase 1, retainer — `Draft 41` §11.5 #2–#3). Prices, fee credit and payment terms are outside this gate and stay blocked | Owner choice recorded — done for the MVP; two readings to confirm (§1.5; §8 #24) | Offer (02) |
| G7 | **Owner approves use of `TEST_FIXTURE` figures** | ⏸ deferred by Owner Decision 71 until cost-to-deliver and capacity exist — *capacity now exists provisionally for the MVP (G3); planning hours now exist for the MVP (§12, excluding legal); cost-to-deliver in money does not* | Owner decision recorded | Owner |

**Also required before a *positive* pricing-floor test — beyond this gate:**
- **A method for deriving a hotel floor.** §10's method averages comparable offers; no comparable hotel offer exists.
- **A pricing-agent spec that can express an H-band.** `offer-pricing-floor-analyst`'s `arr_band` field accepts only `A`–`D` or `unknown`.

---

## 8. Open decisions

| # | Decision | Owning department | Decider | Blocks |
|---|---|---|---|---|
| 1 | ~~Minimum viable delivery scope (Q5)~~ ✅ **Decided for the MVP, internal design only (§1.1–§1.2)** | Offer (02) | Owner | ~~G1~~ — passed for the MVP |
| 2 | Effort estimates by role (V1) — ✅ *MVP bands owner-approved for internal planning (§10.8); legal effort not estimated (§8 #6); no hours* | Offer (02) + Operations (08) | Owner | G2 — legal effort only |
| 3 | Delivery capacity model and its owner (Q1, Q6, Q7) — ✅ *MVP decided provisionally (§6.1): one H1/H2 client at a time, owner solo + AI; Q6, Q7 and full-offer capacity still open* | Operations (08) | Owner | ~~G3~~ — passed for the MVP; revisit after the first real MVP delivery |
| 4 | What is delegated, and under what engagement type (Q3) | HR (11) | Owner | Q2–Q3 |
| 5 | Email / WhatsApp nurture platform — ⏸ *not needed for the MVP* | Tech Stack (13) | Owner | Nurture, when it returns |
| 6 | Legal review path — counsel engagement (item 59) — *counsel named, letters unsigned; no drafted scope covers template review or the sub-processor register; MVP questions packaged 2026-09-14 (§11); **owner scope decision recorded 2026-09-16 — narrow the scope before engagement; the engagement is still not active, nothing sent or signed, no review yet*** | Legal (10) | Owner | G2 (legal effort), G5, QG4, contract, consent |
| 7 | Audit commercial shape — paid standalone vs credited into build — ◐ *structure decided for the MVP 2026-09-14 (§1.5): the audit is always a standalone first stage and can end the MVP; whether its fee is credited is a pricing question, held with the audit-fee credit policy (`Draft 41` §9 #4)* | Offer (02) | Owner | ~~G6~~ — passed for the MVP; the credit question blocks pricing, not G6 |
| 8 | Entry commercial shape — build + retainer vs audit + monthly retainer · ✅ *MVP decided 2026-09-14 (§1.5): audit-gated two stages, no retainer; full-offer shape still open* | Offer (02) | Owner | ~~G6~~ — passed for the MVP |
| 9 | Approval to use `TEST_FIXTURE` figures | Offer (02) | Owner | G7 |
| 10 | Hotel floor derivation method | Offer (02) + Finance (09) | Owner | Any floor |
| 11 | Pricing-agent spec support for H-bands | Offer (02) + runtime | Owner | Positive agent test |
| 12 | L2 / L3 severity thresholds | Offer (02) + Audits & Diagnostics (14) | Owner | V10, audit verdict consistency |
| 13 | Revision policy, SLAs, approval windows (V4) — ✅ *revision policy decided for the MVP 2026-09-13 (§1.3): one included round per M1–M7 output; SLAs, approval windows and full-offer revision policy still open* | Offer (02) + Client Success (07) | Owner | ~~G2~~ — no longer blocks G2 · V4 for the full offer · SLAs and timelines |
| 14 | Image-generation runway and Canva re-authentication | Design (19) + Tech Stack (13) | Owner | Design support role |
| 15 | Redirect destinations for (c), (d) and technical (b) | Offer (02) | Owner | P4 |
| 16 | Launch ICP — *narrowed: the MVP is H1/H2 only* | Offer (02) + Sector (01) | Owner | Qualification |
| 17 | ~~Does M4 include finished copy, or only the blueprint?~~ ✅ **Decided 2026-09-13 (Owner Decision #17):** blueprint and structure, page/message hierarchy, key messaging blocks, sample copy for critical sections — no full finished copy, no full content production, no booking-tool/CMS implementation (§1.2) | Offer (02) + Content (04) | Owner | ~~V3, V4, copy/content producer role~~ — unblocked |
| 18 | ~~Confirm D4 content production is outside the MVP~~ ✅ **Confirmed by Decision #17's wording** — "not a full production build" (§1.2) | Offer (02) | Owner | ~~V3, V6~~ — unblocked |
| 19 | H3 group / property-profile handling — needed before H3 returns (the Hospitality plugin's P2 group-union operator is unimplemented) | Sector (01) + Offer (02) | Owner | H3 |
| 20 | ~~Minimum audit data set for an MVP audit — what counts as basic channel-mix data, and the data-source range accepted (V2)~~ ✅ **Decided for the MVP 2026-09-13 (§1.4):** MD1–MD8 with a data-sufficiency rule; MD1 and MD4 required | Offer (02) + Audits & Diagnostics (14) | Owner | ~~G2 (analytics band), V2~~ — analytics band now set per engagement: M or L (§10.3) |
| 21 | Desk-review handling when the buyer interview (MD7) is missing — is a desk review offered as an MVP engagement, does it count as one capacity unit (§6.1), and what does it deliver beyond M1? | Offer (02) + Audits & Diagnostics (14) | Owner | Desk-review path bands (§10.4); capacity counting |
| 22 | M6 baseline when only the three-month audit window is supplied — request a seasonally comparable period, or state the limitation in M6? | Offer (02) | Owner | M6 measurement validity |
| 23 | ~~MVP tool choices for the four §5.1 gaps~~ ✅ **Decided provisionally 2026-09-13, at category level (§5.2):** client folder outside this repository · spreadsheet workbook (app not chosen) · document-format deliverables · phone, video or in-person interview with typed notes, no recording by default. **Still open:** vendors (none registered in `TECHSTACK_OS.md` §3 for these uses), costs, legal/privacy review, live checks | Tech Stack (13) + Offer (02) | Owner | ~~G4~~ — passed at category level; storage platform and vendors must be settled before real client use |
| 24 | Confirm the two §1.5 readings: (1) M7 closes Stage 1 when the MVP stops on a redirect, and appears in Stage 2 only for a limitation or secondary redirect; (2) severity does not gate Stage 2 for the MVP, although `Draft 41` §11.3's unapproved proposal required L3 | Offer (02) | Owner | What Stage 1 and Stage 2 deliver — not G6 |
| 25 | ~~**Band-to-hours scale for the MVP** (§12.2)~~ ✅ **Decided 2026-09-14:** the scale — XS 1–2 · S 3–5 · M 6–10 · L 11–18 hours per role, per engagement — **and** the counting rules (§12.2), internal MVP planning only | Offer (02) + Operations (08) | Owner | ~~Numeric hours~~ — set · cost-to-deliver in money · G7 |
| 26 | ~~Confirm the redirect-path bands~~ ✅ **Confirmed 2026-09-14:** audit-only redirect path owner/strategist **M**, delivery QA **XS** | Offer (02) | Owner | ~~Audit-only path hours~~ — set (§12.3) |
| 27 | ~~Are client meetings other than the buyer interview counted in the hour ranges?~~ ✅ **Decided 2026-09-14:** the audit readout and blueprint approval conversations are included inside the owner / strategist band (§12.2); totals unchanged | Offer (02) | Owner | ~~How owner hours are read~~ — settled |

---

## 9. Changelog

- **2026-09-13 — Created.** Internal worksheet to unblock the two decisions that gate all pricing work on the Hospitality Revenue Content OS: cost-to-deliver and delivery capacity. Maps four packages (audit, build, retainer, redirect hand-off) against ten workstreams and nine roles, lists ten cost variables and nine tool-cost categories, poses eight capacity questions, and defines a seven-item readiness gate that must fully pass before any `TEST_FIXTURE` price figure is written. **Contains no price, currency, amount, rate, margin or capacity figure.** Surfaced while building it: **no email or WhatsApp nurture platform is registered** in Tech Stack (13), so the nurture workstream cannot be sized. Status of the offer unchanged: **Working Hypothesis / Not Quotable**, not registered. — Claude Code (Opus 5)
- **2026-09-13 — MVP delivery scope recorded (owner decision, internal design only).** Added §1.1: Gateway audit + Entry Build Phase 1 (Direct Booking Message/Journey Blueprint), H1/H2 only; nurture implementation, governance retainer and H3 deferred; seven MVP outputs (M1–M7) mapped to `Draft 41` deliverables. §2 and §4 gained an MVP column, §3 an MVP overlay, §5 a note on which variables the MVP narrows. G1 marked **partially passed (MVP only)**; G4, G5 and G6 annotated for the reduced scope; Q5 answered for the MVP, Q6 deferred; three new open decisions (#17–#19). **Cost and effort left blank.** Still not approved: prices, public offer, retainer, test price figures, legal claims, performance guarantees. — Claude Code (Opus 5)
- **2026-09-13 — Owner Decision #17 recorded: M4 is a blueprint, not a production build (internal design only).** Added §1.2: M4 includes blueprint and structure, page/message hierarchy, key messaging blocks and sample copy for critical sections; excludes full finished copy, full content production and booking-tool/CMS implementation. #17 decided; #18 closed by the same decision's wording (D4 production outside the MVP). **G1 now passed for the MVP only** — not for the full offer. G2 marked ready to start for the MVP. §2, §3.1, §4, §5 and Q5 updated for the effort implications: the copy/content producer drops to light sample copy, and sample copy triggers QG2, QG3, QG5 and QG7 checks. **Cost and effort still blank; no prices.** — Claude Code (Opus 5)
- **2026-09-13 — Added §10 MVP Role-Effort Estimate (owner review required).** Relative bands (XS–XL) only, for one H1/H2 MVP engagement: owner/strategist **L** · offer engineer **XS** · content strategist **M** · sample-copy producer **S** · analytics/reporting **M** · delivery QA **S** · legal/compliance **BLOCKED, not estimated** · design support and automation/booking-journey advisor **deferred** (the advisor is XS if a booking-journey root cause triggers it). Includes effort assumptions A1–A8, a redirect-path comparison, the capacity implication (one MVP client at a time appears plausible for a solo owner with AI — **not a capacity claim**, owner to confirm), and the four decisions that move G2 to passed. **G2 marked PARTIAL, not passed.** V1, V2, §2 P1/P2, §5's MVP note, §8 #2, #6 and #13 updated; new §8 #20 (minimum audit data set). Placed after §9 Changelog under the requested section number §10. **No hours, no money, no prices.** — Claude Code (Opus 5)
- **2026-09-13 — MVP delivery capacity decision recorded (owner decision, provisional).** Added §6.1: one H1/H2 MVP client at a time, owner solo + AI assistance; approved MVP scope only; every client-facing output owner-reviewed; excludes H3, retainer delivery, nurture implementation and website/CMS/booking-tool implementation; **not proven operating capacity — revisit after the first real MVP delivery.** Two or more concurrent clients and H3 capacity **not approved**. **G3 marked passed for the MVP only, provisional:** the gate's two evidence items (a named capacity owner; Q1 answered) are met within MVP scope. Not passed for the full offer. Q1 answered, Q2 partly answered, Q6 and Q7 annotated; §4 owner and delivery QA rows, G7, §8 #3 and §10.6–§10.7 updated. **No prices, no hours, no money.** — Claude Code (Opus 5)
- **2026-09-13 — MVP revision policy recorded (owner decision, internal delivery-scope policy only).** Added §1.3: one included revision round per client-facing output (M1–M7), limited to accuracy, clarity, fit and client-specific context; no new scope or deliverables, implementation, full content production, nurture execution, website/CMS/booking-tool work or retainer activity; additional rounds not approved; exceptions need owner approval before delivery; not public contract language. A4 converted from assumption to policy — **no band changes**. §8 #13 marked decided for the MVP; G2 narrowed (three blockers remain: legal review path, minimum audit data set, owner review of the bands); V4, §5's MVP note, the analytics row, §10.5 and §10.7 updated. Flagged, not decided: an M2 revision that changes the root-cause class re-enters QG1 and can switch path. **No prices, no hours, no money.** — Claude Code (Opus 5)
- **2026-09-13 — MVP minimum audit data set recorded (owner decision, internal design only).** Added §1.4: eight data items (MD1–MD8) and a data-sufficiency rule. MD1 channel room-nights and MD4 direct-booking path are required; without MD2 revenue by channel, revenue leakage is unquantified; without the MD7 buyer interview, the work is a desk review, not a diagnosis; MD3 commission is recorded as unknown rather than invented; a dominant pricing/rate or booking-engine tech finding redirects. §8 #20 marked decided for the MVP; **G2 narrowed — now blocked only by the legal review path and owner review of the bands**. Analytics band set to **M with complete minimum data, L when data is messy or MD2 is unavailable** (A5, §10.3, §10.4). Buyer interview added to the owner row. V2, §10.5 and §10.7 updated. New open decisions: #21 desk-review handling, #22 M6 baseline from a three-month window. Flagged for confirmation: "if #1 and #4 are missing" read as both required. **No prices, no hours, no money.** — Claude Code (Opus 5)
- **2026-09-13 — Owner review of the MVP role-effort bands recorded (internal MVP planning only).** Added §10.8: the §10.3 bands approved unchanged — owner/strategist L · offer engineer XS · content strategist M · sample-copy producer S · analytics/reporting M, or L when data is messy or revenue by channel is missing · delivery QA S as owner self-review · legal/compliance BLOCKED, not estimated · design support deferred · automation/booking-journey advisor deferred, XS only if separately triggered by a booking-journey messaging cause. H1/H2 MVP only; no H3, full offer, retainer, nurture, website/CMS/booking-tool implementation or concurrent clients. **G2 now blocked only by the legal review path / legal effort estimate; G5 unchanged, still blocked.** §4 QA row, V1, §6.1, G2, §8 #2 and §10 header, §10.3, §10.5 and §10.7 updated. **No hours, costs, prices, floors or test figures.** — Claude Code (Opus 5)
- **2026-09-13 — MVP tool categories checked against `13_Tech_Stack/TECHSTACK_OS.md` (internal design only).** Added §5.1. **Can proceed on existing or manual tools:** website/booking-path review (manual) and owner QA (manual). **Partly:** audit data collection and review, document drafting, and measurement-plan drafting — Claude and agency email exist, but no analysis tool, file storage or client-deliverable format is registered. **Missing:** file storage/versioning. **Identified:** AI-assisted drafting, website/booking-path review, owner QA, client correspondence, engagement tracking, client analytics via exports. **Nurture platform confirmed not required** (nurture out of MVP scope). **G4 kept PARTIAL** — four gaps: client-data storage/versioning, spreadsheet/analysis tool, client-deliverable document tool or format, buyer-interview channel and notes; new §8 #23. Also noted: this repository is not a place for client data (auto-sync commits, OneDrive folder); Annex B lists only ClickUp (for G5); verify ClickUp, Notion and the Zoho mail plan before first use. Documents only — no live connection calls. **Tool costs unknown; no prices, no currency, no subscriptions, no vendor commitments.** — Claude Code (Opus 5)
- **2026-09-13 — Provisional MVP tool choices recorded (owner decision, internal MVP design only).** Added §5.2: client data in a dedicated folder outside this git repository — never client data, hotel exports, guest data, interview notes or deliverable drafts inside it; a spreadsheet workbook (app not chosen, no vendor named as approved); document-format deliverables for M1–M7 (template design and production formatting not decided); buyer interview by phone, video or in person with typed notes, with recording not approved by default and, if ever used, requiring explicit client consent plus legal/privacy review first. **G4 marked passed for MVP tool-category identification only.** Still open: tool costs, vendors, legal/privacy approval, live connection checks. G5 kept blocked, with storage platform, cloud-hosted client-data tools and recording added to its scope. §5.1's G4 result marked superseded; V5 and §8 #23 updated. Flagged: a client folder outside the repository but under OneDrive would still be on an unregistered platform. `TECHSTACK_OS.md` not modified. **No prices, no currency, no vendor approvals.** — Claude Code (Opus 5)
- **2026-09-14 — MVP commercial shape recorded (owner decision, internal MVP design only).** Added §1.5: diagnostic-first, two-stage, audit-gated. Stage 1, the Gateway Audit, always comes first and produces M1–M2 under §1.4 and the diagnostic gate; a non-content root cause ends the MVP. Stage 2, the Phase 1 blueprint, opens only on a confirmed content or journey-messaging root cause and produces M3–M6, plus M7 where needed — blueprint with sample copy only. **G6 marked passed for the H1/H2 MVP only.** §8 #7 structure decided (the credit question stays with pricing), #8 decided for the MVP, new #24 to confirm two readings: M7's place on a redirect, and severity not gating Stage 2 despite `Draft 41` §11.3's unapproved L3 proposal. §10.4 stage note added. **Still blocked:** prices, price band, cost-to-deliver, hotel floors, test figures, fee credit, payment terms. **No prices, no currency, no quote language.** — Claude Code (Opus 5)
- **2026-09-14 — Legal/privacy review packet prepared for the H1/H2 MVP (not a review).** Added §11: review-path status; client data handled (MD1–MD8, owner-captured screenshots, the analysis workbook, M1–M7); the tools that would touch it; seven contract and review questions (LQ1–LQ7) mapped to the unreviewed templates and the counsel brief; gate effects. **G5 kept blocked:** counsel is named (Ndwiga Law Advocates LLP), but neither letter of engagement is signed, and `LEGAL_OS.md` §5 records that no drafted letter covers template review or the sub-processor register. **G2 still blocked only by legal.** The G5 row and §8 #6 corrected from "no counsel" to that precise state. **Correction:** §5.1–§5.2 said DPA Annex B lists only ClickUp; it drafts nine rows. Fixed there; `TECHSTACK_OS.md` §9 still carries the stale sentence and was not modified. Written from repo documents; not legal advice. **No prices, no currency, no quote language.** — Claude Code (Opus 5)
- **2026-09-14 — MVP hours-only cost-to-deliver framework added (§12; owner review required).** Hours are expressed **in bands only — no numeric hours.** The repo has no delivery-hours precedent, and `OPERATIONS_CONSTITUTION.md` §7, `PEOPLE_DOCTRINE.md` §8 and `CLAUDE.md` forbid inventing them. Added: a band-to-hours scale left `[OWNER TO SET]`, with proposed counting rules; hours bands per role for the audit-only redirect path and the audit + blueprint path; the analytics M/L rule; legal BLOCKED; an owner-load stack without totals; the one-client provisional capacity warning; and a blank first-delivery actuals table. V1, V9 and G7 updated; new §8 #25 (band-to-hours scale) and #26 (confirm redirect-path bands). **G5 and G7 remain blocked. No money, rates, currency, prices, fees, floors, test figures or quote language.** — Claude Code (Opus 5)
- **2026-09-14 — Owner-approved band-to-hours scale recorded (internal MVP planning only).** §12.2 filled: XS 1–2 · S 3–5 · M 6–10 · L 11–18 hours per role, per engagement. §8 #26 confirmed: audit-only redirect path owner/strategist M, delivery QA XS. §12.3 converted to hours; §12.4 adds planning totals **excluding legal** — audit-only redirect path 13–22 hours with complete minimum data or 18–30 hours with messy data or no revenue by channel (up to 32 if scope changes); audit + blueprint path 29–48 or 34–56 hours (up to 60 with both conditional roles). Legal/compliance stays BLOCKED and outside every total. One-client-at-a-time capacity warning kept. **Still to confirm:** the proposed counting rules (§8 #25). V1, V9, G7, §12.1 and §12.6 updated. **Not a delivery promise, quote, price or cost in money; G5 and G7 still blocked. No currency, rates, fees, floors or test figures.** — Claude Code (Opus 5)
- **2026-09-14 — Owner-approved hours counting rules recorded (internal MVP planning only).** §12.2's proposed rules replaced by the approved ones. **Included:** owner review of AI-assisted output, preparation of M1–M7, internal QA/self-review, one included revision round per output, audit-data review and analysis, buyer interview time and typed notes. **Excluded:** client waiting time, client-side delays, pre-sale/sales work, legal/compliance review (BLOCKED, not estimated), tool setup and live connection checks, work outside the H1/H2 MVP. §8 #25 marked fully decided; §12.4 confirms the totals use these rules (figures unchanged); §12.6 updated. New §8 #27 flags that the audit readout and blueprint approval conversations are not named — the totals read them as inside the owner band. **G5 and G7 still blocked. Not pricing, a money cost, a quote or a delivery SLA.** — Claude Code (Opus 5)
- **2026-09-14 — §8 #27 decided (owner decision, hours meaning only).** The audit readout and blueprint approval conversations are **included inside the owner / strategist hour band** for the H1/H2 MVP, confirming the reading §12.2 had recorded. §12.2's table gains the row, its flagged reading becomes a decision, and §12.6 is updated. **§12 totals unchanged** (audit-only redirect path 13–32 hours; audit + blueprint path 29–60 hours, excluding legal). Legal stays excluded and BLOCKED; G5 and G7 still blocked. **Not a delivery SLA, pricing, money cost, quote or public-facing statement.** — Claude Code (Opus 5)
- **2026-09-14 — §11.1 tracker row brought current (documentation only).** The row said item 59 "still reads 'reply awaited'". That stopped being true when the tracker was updated the same day. It now records item 59's current state — counsel identified, both letters unsigned, reply unsent, scope not agreed, no review — with the old sentence kept as a dated "Was" note. **G5 still blocked; no prices; Working Hypothesis / Not Quotable.** — Claude Code (Opus 5)
- **2026-09-16 — Owner scope decision for the legal review path recorded (item 59); G5 narrowed, not passed.** The counsel scope is to be **narrowed or amended before engagement**, covering the six blocking matters — template review, the cross-border transfer question, transfer clauses and safeguards, FX and payment terms, the sub-processor register, and a named AI-governance reviewer. Neither unsigned letter is accepted as-is, and the path is not deferred while a real hospitality pilot is still intended. **G5 does not move:** a scope decision is not an agreed scope — **no counsel contacted, nothing sent or signed, no engagement active, no document reviewed.** **G2 unchanged**, still blocked only by legal; legal effort still not estimated. §7 G5, §8 #6, §11.1 and §11.5 updated. Canonical record: `10_Legal/LEGAL_OS.md` §8. **No prices, hours, money or quote language; still Working Hypothesis / Not Quotable.** — Claude Code (Opus 5)

---

## 10. MVP Role-Effort Estimate — Owner Review Required

> ⚠️ **DRAFT ESTIMATE · OWNER REVIEW REQUIRED · NOT HOURS · NOT MONEY.** Relative effort bands for **one MVP engagement**, reasoned from §1.1–§1.2 of this worksheet and `Draft 41` §6–§8. Nothing here is measured, and no agent was run. The bands are **not** converted to hours or money, and they are **not** a capacity figure or a pricing input until the owner confirms them. The offer remains **Working Hypothesis / Not Quotable.**
>
> ✅ **Owner review recorded 2026-09-13 (§10.8):** the §10.3 bands are approved for **internal MVP planning only** — no hours, no cost, no prices, no quote, no public or commercial use. Approval does **not** make them a pricing input.

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
| A4 | **One included revision round per client-facing output (M1–M7)** — ✅ *now policy, not assumption (§1.3)*: additional rounds not approved; exceptions need owner approval before delivery | Owner decision 2026-09-13 (§1.3; §8 #13) | An owner-approved exception adds a round — the affected output's bands rise for that engagement |
| A5 | **The client supplies the minimum audit data set** (§1.4) — MD1 and MD4 required; MD2 revenue by channel where available | Owner decision 2026-09-13 (§1.4; §8 #20) | **Analytics stays M** when the minimum data is complete; **becomes L** when data is messy or MD2 revenue by channel is unavailable |
| A6 | *Additional:* AI assistance drafts analysis, strategy, blueprint and sample copy; **every client-facing output still gets owner review** | §6 Q2; delegability ceiling (§4) | Delegated review would lower the owner band — no delegate exists today |
| A7 | *Additional:* bands are for the **full path** — M2 finds an (a) or (b)-messaging root cause, so M3–M6 are produced. The redirect path is in §10.4 | Diagnostic gate (§1.1; `Draft 41` QG1) | — |
| A8 | *Additional:* the **standard MVP package**, with no client-specific scope customization | §4, offer engineer row | Customization moves the offer engineer from XS to S |

### 10.3 Role estimates

| Role | MVP responsibilities | Required for | Effort band | Assumptions | Blockers |
|---|---|---|---|---|---|
| **Owner / strategist** | Buyer interview (MD7, §1.4) · M2 root-cause verdict (senior-only, QG1) · M7 redirect decision · audit readout and blueprint approvals with the client · Class 3 approvals · review of every AI-assisted client-facing output · client relationship | **Both** | **L** | A4, A6. Senior-only work does not delegate (§4). *This band covers the owner role only — today the owner also performs the roles below (§10.6)* | Weekly delivery time unknown (Q7) · "dominant" and the mixed-finding rule undefined (`Draft 41` §9 #9), so a contested verdict takes longer · no second reviewer |
| **Offer engineer** | Scope changes only — adjusting the package when a client needs something outside the standard MVP | Both, *conditional* | **XS** | A8 | None for a standard engagement. Commercial shape (G6) is design work, not delivery effort |
| **Content strategist** | M3 Direct Booking Message Strategy · M4 journey structure, page/message hierarchy and key messaging blocks · M5 Basic Direct-Booking Content Plan · QG7 positioning check | **Blueprint** | **M** | A2, A3, A4, A6. Blueprint only — no calendar production, no D4 content | Runs only after an (a) or (b)-messaging verdict · per-client target definition undefined (`Draft 41` §9 #8) · launch archetype scope open (`Draft 41` §9 #18) |
| **Light copy / sample-copy producer** | Sample copy for a limited set of critical sections inside M4 · one revision round · self-check against QG2 (no outcome claims), QG3 (benchmark labels) and QG5 (no price) | **Blueprint** | **S** | A2, A4, A6. May be performed by the content strategist rather than a separate role | Which sections are "critical" is an assumption (A2), not a decision · proof method BLOCKED, so samples carry no outcome claims |
| **Analytics / reporting** | Data-sufficiency check against §1.4 · data ingestion and channel-mix analysis · M1 Audit Findings Snapshot · evidence for the M2 classification · M7 evidence pack when redirecting · M6 Measurement Plan (baseline and measurement design) · QG6 data integrity | **Both** | **M** if the minimum data set is complete · **L** if data is messy or MD2 revenue by channel is unavailable | A4, A5, A6. One revision round on M1, M2, M6 and M7 (§1.3). No monthly reporting (retainer deferred); client-system data only | Data quality is known only at intake, so M or L is set per engagement (§1.4) · audit scope and duration open (`Draft 41` §9 #13) · per-client target undefined for M6 (`Draft 41` §9 #8) |
| **Delivery QA** | Reduced gate set across M1–M7 — QG1, QG2, QG3, QG5, QG6, QG7 · completeness check before the audit readout and before blueprint handover | **Both** | **S** — owner self-review | A4. Checks, not rework; QG4 and QG8 are not triggered while nurture is deferred | Owner self-review confirmed for the MVP (§10.8) — this effort lands on the owner |
| **Legal / compliance review path** | Audit-data handling terms (§3.1) · client contract terms | **Both** | **BLOCKED — not estimated** | — | No counsel engaged (`OWNER_INPUT_NEEDED.md` item 59; §8 #6) · `legal-counsel-router` routes, it does not review · contract template with data terms missing (`Draft 41` §9 #15) |
| **Design support** | None in the MVP — no produced assets | Neither | **Deferred — not estimated** | A3 | Returns with content production · image-generation runway and Canva authentication (§8 #14) |
| **Automation / booking-journey advisor** | None by default. **Trigger: the audit finds a booking-journey root cause.** A messaging-side (b) finding keeps journey direction inside M4 (content strategist), with at most a light advisor review. A technical (b) finding is a redirect (M7), and the redirected work is out of scope | Blueprint, *only if triggered* | **Deferred — not estimated** · *XS only if separately triggered after the audit finds a booking-journey messaging cause (§10.8)* | A3 — no booking-tool or CMS work in any case | No nurture platform registered (§3) · no engineered destination for a technical (b) redirect (§2, P4b) |

### 10.4 Effort by delivery path

| Role | Full path — (a) or (b)-messaging verdict: M1–M6 | Redirect path — (c), (d) or technical (b): ends at M1, M2, M7 |
|---|---|---|
| Owner / strategist | **L** | **M** — verdict, redirect decision and readout; no blueprint approvals |
| Offer engineer | XS | XS |
| Content strategist | **M** | — |
| Sample-copy producer | S | — |
| Analytics / reporting | **M** · L if data is messy or MD2 is unavailable | **M** · L on the same condition — audit analysis and evidence pack are most of the band; M6 drops out |
| Delivery QA | S | XS — QG1, QG3 and QG6 only |
| Legal / compliance | BLOCKED | BLOCKED |
| Design support | Deferred | Deferred |
| Automation / booking-journey advisor | Deferred · XS if triggered | — (a technical finding is a redirect) |

**Desk-review path (buyer interview missing, §1.4): not banded.** It ends at M1 without a signed verdict, so it should be no larger than the redirect path. Whether it is offered, and how it counts against capacity, is open (§8 #21).

**Stages (§1.5):** the redirect path is Stage 1 alone; the full path is Stage 1 followed by Stage 2.

### 10.5 G2 readiness result

**◐ G2 — PARTIAL, not passed** (§7). *Updated 2026-09-13: blocked **only** by the legal review path / legal effort estimate.*

- **Done:** a labelled band now exists for every active MVP role except legal. V1's unit is "hours *or effort units*", so owner-confirmed bands can satisfy it.
- **Why it is not passed:**
  1. **Legal review path unresolved** — the one required role with no estimate (G5; §8 #6).
  2. ~~**Revision policy unresolved**~~ ✅ **Decided for the MVP 2026-09-13 (§1.3):** one included round per output — matches A4, so no band changes.
  3. ~~**Data-source range unresolved**~~ ✅ **Decided for the MVP 2026-09-13 (§1.4):** minimum audit data set defined; analytics is M with complete minimum data, L when data is messy or MD2 is unavailable.
  4. ~~**Bands not yet owner-reviewed**~~ ✅ **Approved by the owner 2026-09-13 (§10.8)** for internal MVP planning only.
- **Not this step:** converting bands to hours or money. That comes later, for cost-to-deliver, and before any `TEST_FIXTURE` figure (G7).

### 10.6 Capacity implication — not a capacity claim

- **Every active role falls on one person today.** §4 assigns no one but the owner, so the owner's real load for one engagement is the stack of active bands: **L** (owner) + **M** (content strategist) + **M** (analytics) + **S** (sample copy) + **S** (QA) + **XS** (offer engineer), with AI assistance drafting.
- **One MVP client at a time appears plausible for a solo owner with AI assistance — on these assumptions only.** No role reaches XL. The execution-heavy work (analysis, strategy, blueprint, sample copy) is the kind AI can draft. And the MVP excludes the workstreams most likely to add sustained load: content production, implementation, nurture, the retainer and H3.
- **What would make it implausible:** too little weekly owner time (Q7 unanswered) · more than one revision round (A4) · data-access friction beyond basic channel-mix data (A5) · review load — AI drafting does not remove owner review (A6).
- **Concurrency is not assessed.** There is no basis for two or more MVP clients at once. The owner band is L per engagement, and its senior-only part does not delegate, so concurrency is the first thing to test once Q7 is answered.
- **Capacity is not a start condition on its own.** No engagement can begin while the offer is Not Quotable and the audit-data terms have no review path (G5).
- ~~**Not a capacity figure.** G3 stays ❌ and Q1 is unanswered.~~ **Owner decision recorded 2026-09-13 (§6.1):** one H1/H2 MVP client at a time, owner solo + AI, as a **provisional** assumption. Concurrency and H3 capacity are **not approved**. G3 passed for the MVP only.

### 10.7 Open decisions — what moves G2 from partial to passed

**Required for G2 to pass — only #1 remains open:**

| # | Decision | Why G2 needs it | Decider | Reference |
|---|---|---|---|---|
| 1 | **Name a review path for the audit-data handling terms** — and whether review is once per template or per engagement | Legal is the only required role with no estimate | Owner + Legal (10) | §8 #6; item 59 |
| 2 | ~~**Revision policy** — confirm one round per client-approved output, or set another~~ ✅ **Decided for the MVP 2026-09-13 (§1.3):** one included round per M1–M7 output | ~~Changes the content strategist, sample-copy and owner bands~~ — bands unchanged | Owner | §8 #13; `Draft 41` §9 #14 |
| 3 | ~~**Minimum audit data set** — what counts as basic channel-mix data, and the data-source range an MVP audit accepts~~ ✅ **Decided for the MVP 2026-09-13 (§1.4)** | ~~Decides whether analytics stays M~~ — analytics is M or L per engagement | Owner | V2; §8 #20 |
| 4 | ~~**Owner review of the §10.3 bands** — confirm, adjust or reject each~~ ✅ **Approved 2026-09-13 (§10.8)** — internal MVP planning only | ~~V1 must be an estimate the owner stands behind~~ — done | Owner | §10.3; §10.8 |

**Worth settling alongside, but not required for G2:** a working limit for "critical sections" (A2 — keeps sample copy at S) · ~~whether the owner may self-review delivery QA~~ ✅ confirmed — owner self-review for the MVP (§10.8) · weekly owner delivery time (Q7 → §6.1 revisit) · audit scope and duration (`Draft 41` §9 #13 → timeline) · the "dominant" definition (`Draft 41` §9 #9 → verdict effort).

### 10.8 Owner review of the bands — decision (2026-09-13)

✅ **The §10.3 bands are approved for INTERNAL MVP PLANNING ONLY** — no hours, no cost, no prices, no quote, no public or commercial use.

| Role | Approved band |
|---|---|
| Owner / strategist | **L** |
| Offer engineer | **XS** |
| Content strategist | **M** |
| Light copy / sample-copy producer | **S** |
| Analytics / reporting | **M** when the §1.4 minimum audit data set is complete · **L** when data is messy or revenue by channel (MD2) is missing |
| Delivery QA | **S**, performed as **owner self-review** for the MVP |
| Legal / compliance review | **BLOCKED** — not estimated until a legal review path exists |
| Design support | **Deferred** |
| Automation / booking-journey advisor | **Deferred** — **XS only if separately triggered** after the audit finds a booking-journey messaging cause |

**Applies only to the H1/H2 MVP.** **Not approved:** H3 · full offer delivery · retainer delivery · nurture implementation · website/CMS/booking-tool implementation · two clients at once.

**Not converted:** the bands are not hours, costs, prices, price floors or test figures, and approving them creates none of those. The offer remains **Working Hypothesis / Not Quotable.**

**What follows:**
- **G2's owner-review blocker is resolved.** G2 is now blocked **only** by the legal review path / legal effort estimate (§7; §10.5). **G5 stays blocked.**
- **Delivery QA as owner self-review is confirmed**, closing §4's "to confirm" note. QA effort sits with the owner, inside §6.1's one-client cap.
- **Not covered:** the desk-review path still has no bands (§8 #21).
- **Revisit with §6.1:** after the first real MVP delivery, compare actual effort with these bands.

---

## 11. Legal / Privacy Review Packet — H1/H2 MVP (prepared, not reviewed)

> ⚠️ **PREPARED FOR COUNSEL · NOT LEGAL ADVICE · NOT A REVIEW.** Written by an AI from this repository's documents. It states **questions, not answers**, and classifies nothing as lawful or unlawful. It does **not** pass G5, and it approves no contract term, price, public claim, quote or tool for real client use. The offer remains **Working Hypothesis / Not Quotable.** Nothing here has been sent.

### 11.1 Review-path status — why G5 stays blocked

| Fact | Source |
|---|---|
| Counsel is **named**: Ndwiga Law Advocates LLP (Sarah Ndwiga, Managing Partner) | `10_Legal/LEGAL_ENTITY_SETUP.md` |
| **Two Letters of Engagement (29 July and 6 August 2026) — neither signed.** The drafted reply is marked "DRAFT FOR OWNER APPROVAL. Not sent." Nothing later is recorded | `10_Legal/_correspondence/`; `10_Legal/LEGAL_OS.md` §2 |
| **No drafted letter covers this packet's core matters.** `legal-counsel-router` stays `blocked_no_reviewer` for six matters no letter covers: template review, s.48 cross-border transfers, SCCs, FX terms, **the sub-processor register**, and the AI-governance reviewer | `LEGAL_OS.md` §5 |
| **All seven templates are unreviewed AI drafts** — "Do not sign, send, or rely on any of these until a Kenyan-qualified advocate has reviewed them" | `10_Legal/templates/README.md` |
| Tracker: **item 59** (engage counsel) — *re-stated in the tracker 2026-09-14*: counsel identified, both letters unsigned, drafted reply unsent, scope not agreed, no review yet; blocked because the engagement is not active, not because no reviewer exists. *Was, when this packet was written: "Its row still reads 'reply awaited' (2026-07-19) and predates both letters."* | `OWNER_INPUT_NEEDED.md` item 59 |
| ↪ **Owner scope decision recorded 2026-09-16** — narrow or amend the counsel scope **before** engagement, covering template review and the sub-processor register among the six blocking matters; neither unsigned letter accepted as-is. **Not an agreed scope and not an engagement** — nothing sent or signed, nothing reviewed | `10_Legal/LEGAL_OS.md` §8; `10_Legal/LEGAL_REVIEW_PATH_DECISION_PACKET.md` |

**Result: no legal review path exists for the MVP's matters — G5 stays ❌, now narrowed but not passed.** *(2026-09-16: the owner decided the counsel scope is to be narrowed or amended before engagement, and it covers this packet's core matters. A decision about what to ask for is **not** an agreed scope — no counsel has been contacted, nothing has been sent or signed, no engagement is active and no document has been reviewed, so the gate does not move.)* Opening it is an owner action: an agreed engagement whose scope covers review of the templates cited in §11.4 and the sub-processor register for this MVP. When a review happens, `templates/README.md` requires the reviewer, date, changes and jurisdictions to be recorded in `LEGAL_OS.md` §8.

### 11.2 Client data handled in the MVP

"May contain personal data?" records **what the data could contain**, for counsel to classify. It is not a legal classification.

| Data | From | May contain personal data? | Where it lives | Rule already set | Question |
|---|---|---|---|---|---|
| **MD1** room-nights by channel, last three months | Client export | Aggregated counts: unlikely. A raw booking export: guest names, contact details, stay dates | Client folder; spreadsheet workbook (§5.2) | Never inside this repository (§5.2) | LQ1 — request aggregated counts only? |
| **MD2** revenue by channel, if available | Client export | As MD1; commercially confidential either way | As MD1 | As MD1 | LQ1, LQ3 |
| **MD3** OTA commission rate or estimate | Client | Commercial rather than personal; confidential | Client folder; workbook | Recorded as unknown if not supplied — never invented (§1.4) | LQ3 |
| **MD4** direct-booking path — URL, screenshots or notes, CTA, landing pages | Public site; client | Public pages: unlikely. Booking-engine back-office or confirmation screenshots: guest records | Client folder | — | LQ1 — limit to public-facing pages and redacted screenshots? |
| **MD5** guest communication assets — confirmation email, pre-arrival message, WhatsApp scripts | Client | Templates: unlikely. Real sent messages: guest personal data, possibly of guests from origin markets such as Germany and the UK (`Draft 41` QG4) | Client folder | Reviewed only; no nurture implementation (§1.4) | LQ1 — templates only, or redacted samples? Which regime applies to guest data? |
| **MD6** content and campaign assets | Client | Usually not; subscriber lists or identifiable guest content could | Client folder | — | LQ1 — exclude lists and identifiable guest content? |
| **MD7** buyer interview notes | GM, Owner/MD or Revenue Manager | **Yes** — the interviewee's identity, role and stated views | Client folder | Typed notes; **no recording by default**; recording needs explicit client consent and legal/privacy review first (§5.2) | LQ1, LQ3 |
| **MD8** constraints | Client | Unlikely | Client folder | — | — |
| **Owner-captured website / booking-path screenshots and notes** | Public site | Unlikely for public pages | Client folder | — | As MD4 |
| **Spreadsheet analysis workbook** | Derived from MD1–MD3 | Only what its inputs contain | Client folder | App not chosen (§5.2) | LQ2 |
| **Client deliverables M1–M7** | Arika | Designed to carry aggregates, not guest-level data; confidential commercial findings | Client folder; document format (§5.2) | Revision policy (§1.3); blueprint limits (§1.2); QG2, QG3, QG5 | LQ3, LQ5, LQ6 |

**The threshold question behind every row:** SOW §10.1 requires each engagement to state whether it involves processing personal data, and its drafting note warns that "a CRM audit is almost always personal-data processing". LQ1 asks counsel to answer that for this MVP.

### 11.3 Tools that would touch MVP data

| Tool / category | MVP use | In `TECHSTACK_OS.md` §3? | In the draft DPA Annex B? | Question |
|---|---|---|---|---|
| **Dedicated client folder outside this repository** | All client files | Platform not chosen; not registered | No | LQ2 — platform, hosting location, access control, deletion at close. Under OneDrive it would sit on an unregistered platform (§5.2) |
| **Spreadsheet app** | Analysis workbook | No spreadsheet tool registered | No | LQ2 — local or cloud; a cloud app is a sub-processor |
| **Document tool / format** | M1–M7 | Authoring app not chosen | No | LQ2 — only if cloud-hosted; delivery channel for finished documents |
| **Zoho mail** (agency mailboxes) | Client correspondence; receiving exports | Email hosting on Zoho noted; product and plan unconfirmed (§9) | Only as an unnamed "[Email/domain provider]" row; Zoho Books is listed separately | LQ2 — name it; is email an acceptable channel for booking exports? |
| **Claude (Anthropic)** | AI-assisted drafting and analysis | Yes — Claude Pro plan; API key verified by use for manual runtime calls | Yes — "Yes, if a prompt contains it"; location and transfer "to verify" | LQ2, LQ4 — which terms govern client data on the plan used; retention; training use (Annex B note); limit inputs to aggregates? |
| **ClickUp** (optional engagement tracking) | Client contact record | Yes — built; live-verified 2026-07-15 | Yes | LQ2 — confirm the entry covers MVP client contacts |
| **Phone / video call / note-taking** | Buyer interview (MD7) | No calendar connected; no video-call or transcription tool registered | No | LQ2 — a video platform would be a sub-processor |
| **Recording** | Not approved | Not registered | No | LQ1 — only if recording is ever proposed |

### 11.4 Contract and review questions

Positions cited are **unreviewed template drafts**. "Brief" numbers refer to `10_Legal/COUNSEL_ENGAGEMENT_BRIEF.md` §5.

| # | Question | Current drafted position (unreviewed) | Existing counsel question |
|---|---|---|---|
| **LQ1** | **Data-processing terms.** Is the MVP audit personal-data processing (SOW §10.1)? If so, does `DPA.md` apply as drafted, and what goes in its Annex A for this MVP? Can data minimisation — aggregated exports, templates rather than sent messages, redacted screenshots — keep guest-level data out? Which regime applies to guest data from origin markets (`Draft 41` QG4)? What notice does the interviewee need, and what would recording require if it were ever proposed? | SOW §10; `DPA.md`; `LEGAL_RESEARCH.md` §4 | Brief Q3 (template review) · Q1 (s.48 transfers) |
| **LQ2** | **Sub-processor list updates.** Annex B would need the client-folder platform, any cloud spreadsheet or document tool, Zoho mail by name, and any video-call platform. Is the Anthropic entry adequate for client data? Does any of this need a documented cross-border basis before first use? | `DPA.md` §5 and Annex B | Brief Q6 (register) · Q1 (s.48) · Q7 (SCCs — only if EU/UK personal data is in scope) |
| **LQ3** | **Confidentiality and client-data handling.** Does MSA §6 cover hotel commercial data (channel mix, revenue, OTA commission) and interview content? Is an NDA needed before the data request, since the audit data can arrive before any MSA is signed? What retention and deletion applies to exports, workbooks and notes at engagement close? | MSA §6; MSA §4 with §6.5 (return or destroy); `NDA.md` | Brief Q3 |
| **LQ4** | **AI-assisted drafting disclosure.** Is the disclosure in `API_AND_AI_TOOLING_TERMS.md` §1 plus MSA §8.5 enough for this MVP? Should the SOW ask for the client's AI-use policy up front? The MVP's owner review of every client-facing output (§6.1) matches the drafted human-review clause (§2) | API & AI tooling terms §1–§4 and its open item 5; MSA §8.5 | Brief Q3. **Brief Q4 (AI-governance reviewer) is not triggered** — the MVP deploys no AI into client systems |
| **LQ5** | **Client approval of findings and revisions.** How does SOW §8 acceptance — review window, deemed acceptance, no-charge correction of deficiencies — fit the MVP's one included revision round (§1.3)? Does accepting M2 mean agreeing with the diagnosis, or only receiving it? How is a disputed verdict handled, given that Stage 2 opens only on Stage 1's verdict (§1.5)? | SOW §8; MSA §2.3 (change requests) | Brief Q3 |
| **LQ6** | **No performance guarantee.** Do MSA §8.3 and SOW §12 cover audit findings, revenue-leakage estimates (or "unquantified"), measurement-plan targets and sample copy? Sector benchmarks are always labelled and never promised (QG3), and the disclaimer must match what is said in sales conversations | MSA §8.3; SOW §12; `CLAIMS_SUBSTANTIATION_POLICY.md` §5 | Brief Q3 |
| **LQ7** | **No legal approval is sought for public pricing or claims.** This packet asks counsel to review MVP data handling and contract terms only. It seeks **no** approval of any price, public offer, marketing claim, case study or testimonial — those stay blocked (QG2 proof method, QG5 pricing gate, Not Quotable) | `CLAIMS_SUBSTANTIATION_POLICY.md` | — |

**Before any signature, outside this packet:** entity formation (Brief Q2) and ODPC registration (Brief Q8) sit within the letters' drafted scope, which is unsigned (`LEGAL_OS.md` §16).

### 11.5 Gates affected

| Gate | Status | Why |
|---|---|---|
| **G2** | ◐ **Blocked only by legal** | Legal/compliance effort cannot be estimated until a review path exists. The packet names the documents and questions that effort would cover |
| **G5** | ❌ **Blocked — now narrowed** | No signed engagement, and no drafted letter covers template review or the sub-processor register (§11.1). A prepared packet is not a review path. **2026-09-16:** an owner scope decision narrows what an engagement would cover (item 59) — but a scope decision is not an agreed scope, so **G5 is narrowed, not passed** |
| **G7** | ⏸ **Blocked** | Needs every gate passed, cost-to-deliver in hours and costs (Decision 71), and owner approval |

G1, G3, G4 and G6 are unchanged.

### 11.6 Using the packet

- **Owner action only.** Whether and when to share it with counsel is the owner's decision, as part of agreeing scope under item 59. Nothing has been sent, and no agent was run.
- **It adds to, not replaces,** `COUNSEL_ENGAGEMENT_REVIEW.md`'s 24 questions and the counsel brief.
- **When a review happens:** record it in `LEGAL_OS.md` §8, per `templates/README.md`; then reassess G5 and estimate G2's legal effort.

---

## 12. MVP Hours-Only Cost-to-Deliver Estimate — Owner Review Required

> ⚠️ **HOURS ONLY · OWNER-APPROVED PLANNING SCALE (2026-09-14) · NO MONEY.** Internal planning ranges, H1/H2 MVP only. **Not** a public delivery promise, **not** approved delivery capacity, **not** a quote or price, **not** a cost in money, and **not** a rate, fee, floor or test figure. **Not approved** for the full offer, H3 groups, the retainer, nurture, implementation, or two clients at once. **G5 and G7 stay blocked.** The offer remains **Working Hypothesis / Not Quotable.**

### 12.1 Why hours needed an owner-set scale

Numeric hour ranges were to be used **only if the repo already permits estimated hours**. It does not:

| Source | What it says |
|---|---|
| `08_Operations/OPERATIONS_CONSTITUTION.md` §7 | The capacity model **"Does not exist"**, and the capacity planner "may not invent utilization %, headcount, or throughput" |
| `11_HR_People_Ops/PEOPLE_DOCTRINE.md` §8 | HR will not "**Invent headcount, utilization, or hours**", inheriting the capacity planner's reason: *"it would authorize overselling against a fiction"* |
| `CLAUDE.md` | "Do not invent agency-specific facts (numbers, client names, pricing, legal terms) when source material is missing — flag the gap instead" |
| Repo search, 2026-09-14 | **No delivery-hours estimate exists anywhere.** The only numeric hour ranges are unrelated — a sales daily-plan draft, response windows and draft client-KPI claims |

V1's unit ("hours or effort units") allows hours to be recorded, but **no source supplies them.** Hours therefore stay in bands until the owner sets a band-to-hours scale (§12.2; §8 #25).

✅ **Resolved 2026-09-14:** the owner approved the scale (§12.2). The hours below are **owner-sourced, not invented**, which is what the rules above require.

### 12.2 Band-to-hours scale — owner to set

✅ **Owner-approved 2026-09-14 — internal MVP planning only.** Hours per role, per MVP engagement. Every row in §12.3 converts from this scale without further judgement.

| Band | Hours per role, per MVP engagement | Rule |
|---|---|---|
| **XS** | **1–2 hours** | Smallest band — an occasional touchpoint |
| **S** | **3–5 hours** | Above XS |
| **M** | **6–10 hours** | Above S |
| **L** | **11–18 hours** | Above M |
| **XL** | Not set | No MVP role is XL (§10.1) |

✅ **Counting rules — owner-approved 2026-09-14, internal planning only.** Not pricing, not a cost in money, not a quote, not a delivery SLA.

| Included in the hour ranges | Excluded from the hour ranges |
|---|---|
| Owner review of AI-assisted output (A6) | Client waiting time |
| Preparation of client-facing MVP deliverables M1–M7 | Client-side delays |
| Internal QA / self-review | Pre-sale and sales work |
| One included revision round per client-facing output (§1.3) | Legal / compliance review — **BLOCKED, not estimated** |
| Audit-data review and analysis | Tool setup and live connection checks (§5.1) |
| Buyer interview time and typed notes (MD7) | Any work outside the H1/H2 MVP scope |
| Audit readout and blueprint approval conversations — inside the owner / strategist band (§8 #27) | |

**Readings recorded with the approval:**
- **Hours are effort, not calendar duration.** Waiting time and client-side delays sit outside them; audit duration is still open (`Draft 41` §9 #13).
- **Extra revision rounds are outside the ranges.** Only the one included round is counted, so any owner-approved exception (§1.3) adds hours on top.
- ✅ **Decided 2026-09-14 — client meetings other than the buyer interview** (§8 #27): the audit readout and blueprint approval conversations are **included inside the owner / strategist hour band**, as §10.3 already assumed. The §12 totals are unchanged.

### 12.3 Hours by role and path

Owner-approved §10.3 bands (§10.8), the §10.4 path split (redirect-path bands confirmed 2026-09-14, §8 #26), converted with the §12.2 scale. Stage 1 is the Gateway Audit; Stage 2 is the Phase 1 blueprint, opened only when the diagnostic gate passes (§1.5).

| Role | Audit-only redirect path — Stage 1 only; ends at M1, M2, M7 | Audit + blueprint path — Stage 1, then Stage 2 | Stages active |
|---|---|---|---|
| **Owner / strategist** | **M — 6–10 hours** | **L — 11–18 hours** | Both — buyer interview, verdict and readout in Stage 1; blueprint approvals in Stage 2; review throughout |
| **Offer engineer** | XS — 1–2 hours, *only if scope changes* | XS — 1–2 hours, *only if scope changes* | Either |
| **Content strategist** | None | **M — 6–10 hours** | Stage 2 |
| **Light copy / sample-copy producer** | None | **S — 3–5 hours** | Stage 2 |
| **Analytics / reporting** | **M — 6–10 hours** when the §1.4 minimum audit data set is complete · **L — 11–18 hours** when data is messy or revenue by channel is missing | Same two alternatives | Stage 1 (M1, M2 and M7 evidence); Stage 2 (M6) |
| **Delivery QA** — owner self-review | **XS — 1–2 hours** | **S — 3–5 hours** | Both |
| **Legal / compliance review** | **BLOCKED — not estimated** | **BLOCKED — not estimated** | Until a legal review path exists (G5; §11) |
| **Design support** | Deferred — none | Deferred — none | — |
| **Automation / booking-journey advisor** | None — a technical finding is a redirect | Deferred — **XS — 1–2 hours, only if separately triggered** by a booking-journey messaging cause | Stage 2, if triggered |

The redirect-path owner (M) and delivery QA (XS) bands were **confirmed by the owner 2026-09-14** (§8 #26).

**No per-stage sub-bands are given.** §10 approved one band per role per engagement; splitting a band between Stage 1 and Stage 2 would be a new estimate. The first real delivery should record the split (§12.5).

### 12.4 Owner load and capacity warning

- **Every active row is the owner's time today.** No delegate exists (§4; §6.1), so the totals below are the owner's own planning hours for one engagement.

**Planning ranges per engagement — EXCLUDING LEGAL.** Legal/compliance is BLOCKED and not estimated, so every total understates the real figure by an unknown amount.

| Path and roles | Minimum data complete (analytics M) | Data messy or revenue by channel missing (analytics L) |
|---|---|---|
| **Audit-only redirect path** — owner M + analytics + QA XS | **13–22 hours** | **18–30 hours** |
| + offer engineer, if scope changes | 14–24 hours | 19–32 hours |
| **Audit + blueprint path** — owner L + content strategist M + sample copy S + analytics + QA S | **29–48 hours** | **34–56 hours** |
| + one conditional role (offer engineer or triggered advisor) | 30–50 hours | 35–58 hours |
| + both conditional roles | 31–52 hours | 36–60 hours |

**How the totals are built:** the low ends and the high ends of each active role in §12.3, added separately. They use the **owner-approved counting rules** in §12.2 (2026-09-14). They exclude legal, client waiting time and client-side delays, pre-sale and sales work, tool setup and live connection checks, extra revision rounds, and any work outside the H1/H2 MVP.
- ⚠️ **Capacity warning — unchanged.** **One H1/H2 MVP client at a time** remains the **provisional** capacity (§6.1). These hours are **planning assumptions, not approved delivery capacity.** Weekly owner delivery time (Q7) is still unanswered, so hours cannot yet become a calendar duration or justify a second concurrent client. **Revisit after the first real delivery.**

### 12.5 First real delivery — record actuals

The first real MVP delivery is the only source of real hours this repo will have. Record them against the bands, then revisit §12.2 and §6.1.

| Role | Stage 1 actual hours | Stage 2 actual hours | Band held? |
|---|---|---|---|
| Owner / strategist | `[RECORD]` | `[RECORD]` | `[Y/N]` |
| Offer engineer | `[RECORD]` | `[RECORD]` | `[Y/N]` |
| Content strategist | — | `[RECORD]` | `[Y/N]` |
| Light copy / sample-copy producer | — | `[RECORD]` | `[Y/N]` |
| Analytics / reporting — minimum data complete? `[Y/N]` | `[RECORD]` | `[RECORD]` | `[Y/N]` |
| Delivery QA (owner self-review) | `[RECORD]` | `[RECORD]` | `[Y/N]` |
| Legal / compliance | `[RECORD — once a review path exists]` | `[RECORD]` | — |

### 12.6 What this does and does not change

| Item | Result |
|---|---|
| **Hours-only cost-to-deliver** | ✅ **Planning hours set for the MVP** — owner-approved scale (2026-09-14); both paths in hours, **excluding legal** (§12.3–§12.4), under owner-approved counting rules (§12.2), with the audit readout and blueprint approval conversations counted inside the owner / strategist band (§8 #27) |
| **Cost in money** | ❌ **Not drafted** — no rate, cost or currency. Converting hours to money needs a cost basis that is not set here, and tool costs are unknown (§5.2) |
| **G2** | ◐ Unchanged — blocked only by legal |
| **G5** | ❌ Unchanged — no legal review path (§11) |
| **G7** | ⏸ **Blocked** — needs G2 and G5 passed, cost-to-deliver in money, and owner approval (Decision 71). Numeric planning hours now exist, but they are not a cost |
