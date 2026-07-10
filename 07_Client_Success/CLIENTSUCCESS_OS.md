# Client Success — Department OS

**Department:** Client Success (07)
**Position in flow:** Receives closed deals from Sales (05); owns the client relationship; hands off scoped delivery to Operations (08).
**Mandate:** Own the post-sale client lifecycle — onboarding, journey, segmentation, fit/qualification, retention, health, and offboarding.
**Owner:** Mary Thuo

> See [`GLOBAL_OS.md`](../GLOBAL_OS.md) for how this file fits into the whole system. Read that first if you haven't.

---

## 1. Identity

Client Success owns everything that happens to a client *after* the sale: onboarding, journey design, segmentation, retention, and offboarding. Confirmed during exploration to be distinct from ClientPartner Acquisition (which is a pre-sale acquisition channel) despite the similar original folder name ("The Agency Client. Drafts"). Recurring stated rule across the source material: *"A strong system rejects more clients than it accepts."*

## 2. Status

**Content migration: first pass complete (2026-06-30).** All 22 raw drafts read. Like every other department, **100% generic/hypothetical — no real client names, case studies, retention data, or onboarding transcripts found anywhere.** Onboarding is the most concrete, usable content in the folder (a real 5-layer model plus two scored diagnostics). Two confirmed scope-blur issues found, consistent with the pattern seen in ClientPartner Acquisition (06): (1) segmentation content conflates pre-sale qualification (Sales' territory) with post-sale segmentation (this department's actual mandate), and (2) the source material does not cleanly hand off delivery to Operations (08) the way this file's header assumes — several drafts describe Client Success as owning delivery execution directly. Two files (Drafts 21-22) are largely generic AI-agent-architecture content relabeled "ClientOS," contributing little client-success-specific value — flagged in §14, not used to populate the registries below.

## 3. Capability Registry

| Capability | Description | Status |
|---|---|---|
| Client onboarding | 5-layer model (Confirmation → Clarity → Data Capture → Control → Activation); sequence: deal closed → welcome → onboarding form → internal review → kickoff call → define success metrics → start execution | Draft/aspirational, most concrete content in this department (Draft 16) |
| Onboarding diagnostic | 6-item pass/fail checklist (Confirmation, Outcome Clarity, Scope Control, Input Readiness, Control Structure, Momentum Trigger), 5-10 min, scored 0-2/3-4/5-6 | Draft/aspirational (Draft 16) |
| Client Clarity diagnostic | Outcome/Problem/Context/Expectation/Process/Commitment/Success/Risk scan, 5-10 min | Draft/aspirational (Draft 12) |
| Post-sale segmentation | 5 types: Value-based, Needs-based, Behavioral, Lifecycle, Strategic | Draft/aspirational, genuinely post-sale (Draft 3) — this department's actual segmentation mandate, confirmed in §10's reconciliation |
| Client journey/lifecycle design | 3+ unreconciled stage models (see §4) | Draft/aspirational |
| Legal identity intake | "Client Legal Identity Framework" (Legal Person, Authority, Obligation, Risk Profile, Jurisdiction) as a pre-onboarding checkpoint | Draft/aspirational; confirmed generic business-entity-type explainer, NOT the agency's own legal infrastructure (that's Legal, 10) (Draft 11) |
| Retention cadence | Monthly/quarterly health-score review + proactive value-recap, risk escalation on score drop | **Claude-synthesized (2026-06-30)** — see §10 |
| Expansion/upsell triggering | Identifies ascension-ready clients, hands qualified expansion opportunities to Sales | **Claude-synthesized (2026-06-30)** — see §10 |
| Advocacy & referral capture | Identifies advocacy-ready clients, requests testimonials/case studies/referrals, feeds Marketing and ClientPartner Acquisition | **Claude-synthesized (2026-06-30)** — see §10 |
| Offboarding & churn process | 3-path process (planned/unplanned/involuntary), retention-attempt gate, structured exit interview, asset handover, churn-reason capture | **Claude-synthesized (2026-06-30)**, resolves tracker item 24 — see §10 |
| Re-entry / win-back loop | Periodic review of dormant/churned accounts tagged win-back-candidate, re-qualification, re-engagement | **Claude-synthesized (2026-06-30)** — see §10 |

## 4. Workflow Index

| Workflow | Trigger | Steps | Output | Owner | Source |
|---|---|---|---|---|---|
| Client onboarding sequence | Deal closed | Welcome/confirmation → onboarding form → internal review → kickoff call → define success metrics → start execution | Activated client | Mary Thuo | Draft 16 |
| Outward-facing client diagnostic | Sales call / early engagement | 5-10 min scan to find a client's business bottleneck | Diagnostic output (sellable/usable on calls) | Mary Thuo | Drafts 2, 15 |
| Retention cadence | Time-based (monthly) + health-score alert | Monthly health-score review → risk flagging if below threshold → value-recap delivery → quarterly strategic review (ties to renewal timeline) | Updated `health_score`, retention risk flagged/cleared, touchpoint log | Mary Thuo | **Claude-synthesized** — see §10 |
| Expansion / upsell | `health_score` above threshold + tenure milestone, or strategic review surfaces a new need | Identify ascension fit (Offer's Audit→Infrastructure→Optimization→Embedded Partnership→Enterprise Transformation path) → internal proposal review → hand qualified opportunity to Sales (05) | New Opportunity (handoff to Sales), or logged "not yet" with a re-check date | Mary Thuo, cross-ref Sales (05) | **Claude-synthesized** — see §10 |
| Advocacy & referral | Sustained high `health_score` + tenure milestone + positive QBR | Identify advocacy-ready clients → request testimonial/case study → request referral/introduction → track outcome | Testimonial/case-study asset (→ Marketing 03/Content 04); referral lead (→ ClientPartner Acquisition 06 or Sales 05) | Mary Thuo, cross-ref Marketing (03), ClientPartner Acquisition (06) | **Claude-synthesized** — see §10 |
| Offboarding & churn | Contract end approaching (60-90 days out), churn signal (health-score drop, non-renewal notice), client-initiated termination, or non-payment/breach | Classify path (planned/unplanned/involuntary) → retention-attempt gate (unplanned only) → offboarding kickoff (notify Finance/Operations) → asset/access handover → structured exit interview (churn-reason taxonomy) → final invoice close-out (→ Finance 09) → relationship classification (alumni/referral/do-not-recontact/win-back) | Closed account, `churn_reason` logged, assets returned, `relationship_status` set | Mary Thuo | **Claude-synthesized**, resolves tracker item 24 — see §10 |
| Re-entry / win-back loop | Time-based review (6-12mo) of `relationship_status = win-back-candidate` accounts, or external re-engagement signal | Periodic dormant-account review → re-qualification (Sales' qualification process) → re-engagement outreach → if re-engaged, restart at Conversion/Onboarding | Re-engaged lead (→ Sales 05) or remains dormant with next review date | Mary Thuo, cross-ref Sales (05) | **Claude-synthesized** — see §10 |

**Lifecycle model — resolved (reconciliation pass, 2026-06-30).** 3 unreconciled models were found; the 9-stage Draft 2 version is now canonical, because it's the only one that maps cleanly onto this repo's own department flow (Sector→Offer→Marketing→Sales→Client→Operations→Finance) with no stage left ownerless:

- **9-stage (Draft 2) — canonical:** Awareness (Marketing/Content) → Interest/Consideration (Marketing/Content) → Conversion (Sales) → Onboarding (Client Success) → Delivery (Client Success → Operations handoff) → Retention (Client Success) → Expansion (Client Success) → Advocacy (Client Success → feeds ClientPartner Acquisition/Marketing) → Re-entry/Loop (back to Marketing/Content)
- 7-stage (Draft 1): Pre-Client → Prospect → Buyer → Active Client → Transformed Client → Retained/Expanded Client → Advocate Client — kept as a superseded alternate framing, not deleted; conceptually compatible with the 9-stage model (coarser granularity), no contradiction.
- 7-phase "Journey Orchestration" (Draft 21): Attraction → Qualification → Alignment → Activation → Transformation → Expansion → Continuity — kept as a superseded alternate framing; this is the same draft flagged in §14 as drifting into generic AI-agent-architecture content, so treat its stage names as lower-confidence than the other two.

**Lifecycle coverage — complete as of 2026-06-30.** Every owned stage of the 9-stage model now has a workflow above: Onboarding (real, Draft 16), Delivery (the Operations handoff, §10), Retention/Expansion/Advocacy/Re-entry (Claude-synthesized, §10), plus Offboarding (synthesized, not itself one of the 9 named stages — it's a real exit path that can trigger from Retention, Expansion, or anywhere a contract ends or churn occurs, so it's modeled as a cross-cutting workflow rather than forced into one stage slot).

## 5. Agent Roster

*(placeholder — none yet)*

## 6. Skill Library Index

*(placeholder — none yet)*

## 7. KPI Dictionary (department-local)

**All values illustrative/draft, inconsistent across files — never tied to real measurement.**

| Metric | Formula | Draft value(s) found | Source | Owner | Cadence | Threshold |
|---|---|---|---|---|---|---|
| Pre-sale qualification score | Sum of 5 filters /5 each = /25 | 20-25 ideal, 15-19 conditional, <15 reject (Draft 1); 20-25/15-19/10-14/<10 (Draft 15, different cut lines for the same scale) | Drafts 1, 15 | Mary Thuo | *(unset)* | *(unset)* |
| Onboarding diagnostic score | 6 pass/fail checks | 5-6 / 3-4 / 0-2 | Draft 16 | Mary Thuo | *(unset)* | *(unset)* |
| Generic metric names invoked, no values given | CAC, LTV, NPS, activation rate, engagement rate, progress rate, success rate, time-to-value | Named only | Drafts 7, 17 | Mary Thuo | *(unset)* | *(unset)* |
| Churn rate | Offboarded clients ÷ active clients, per period | **Claude-synthesized formula**, no real data yet | New, via §10's offboarding workflow | Mary Thuo | Monthly | *(unset — no real data yet)* |
| Retention rate | 1 − churn rate | **Claude-synthesized formula** | New, via §10's retention workflow | Mary Thuo | Monthly | *(unset)* |
| Expansion rate | Clients with an expanded engagement ÷ total active clients, per period | **Claude-synthesized formula** | New, via §10's expansion workflow | Mary Thuo | Quarterly | *(unset)* |
| Advocacy conversion rate | Testimonials/referrals secured ÷ advocacy-ready clients identified | **Claude-synthesized formula** | New, via §10's advocacy workflow | Mary Thuo | Quarterly | *(unset)* |

**Note:** the two qualification-scoring drafts (1 and 15) use the same /25 scale but disagree on cut-line thresholds — flag rather than silently pick one if this gets operationalized. The 4 new rows above are real formulas (standard agency-retention math), not invented agency-specific figures — but have zero real data until the agency has operated long enough to measure them, same class as every other unset threshold in this repo.

## 8. Decision Log

- **2026-06-30 — Adopted the 9-stage (Draft 2) client lifecycle model as canonical**, superseding the 7-stage and 7-phase alternates (kept for reference, not deleted). See §4.
- **2026-06-30 — Reassigned pre-sale qualification scoring to Sales (05); confirmed post-sale segmentation as this department's actual mandate.** See §3, §10.
- **2026-06-30 — Reaffirmed the Client Success → Operations (08) delivery handoff** as designed (no change) — drafts that folded delivery into Client Success predate the Operations department concept. See §10. — Claude Code (Sonnet 4.6)
- **2026-06-30 — Built out the full Client Success Process Library** (Retention, Expansion, Advocacy, Offboarding & Churn, Re-entry/Win-back), Claude-synthesized per explicit owner request, since the source material confirmed genuine absence rather than unmigrated content. Every owned stage of the 9-stage lifecycle now has a real workflow. Added 4 new `Client` object fields to `CRM_SCHEMA.md` (`lifecycle_stage`, `relationship_status`, `churn_reason`, `offboarding_type`) and 4 new KPI formulas (churn/retention/expansion/advocacy rate). Resolves tracker item 24. — Claude Code (Sonnet 4.6)

## 9. Risk / Incident Log

*(placeholder — empty, no real incidents logged yet. See §10's "system failures" content for self-identified risk areas. The new Offboarding & Churn workflow (§10) routes involuntary offboarding — non-payment/breach — through Finance (09) and Legal (10) per the Constitution's risk-class escalation model, rather than leaving it as an unstructured CSM judgment call; this is the one place in this department's process library that's explicitly risk-classified.)*

## 10. Standards & SOPs Index

**Stated principles:**
- "A strong system rejects more clients than it accepts."
- "80% fixed process / 20% adaptive layer" for journey customization (Draft 10).
- "The client should never feel the complexity of the internal system" (Draft 21).

**Self-critique content — confirmed self-referential, not a client-facing diagnostic** (important distinction, verified 2026-06-30): `Client System Failures. Draft 8.md` and `Client Project Gaps. Draft 17.md` are introspective critiques of the agency's OWN client-success system design, not a diagnostic product sold to clients. Draft 8 lists 10 internal failure modes: no goal integrity, misaligned qualification, broken expectation-setting, weak onboarding, no execution layer, no feedback loop, no visibility/dashboards, poor retention design, no ownership, no standardization. Draft 17 lists missing internal systems: Control/Governance layer, Economics model, Behavior mapping, Communication system, Data/feedback loop, Success metrics, Role ownership, Value-based segmentation, Risk management, Expansion logic. **Treat these as a real, useful starting checklist for what this department's own SOPs need to eventually cover** — they're self-aware about the gap between theory and an operating system, which is a more useful signal than the generic frameworks elsewhere in this folder.

(Distinct from this: the "5-10 Minute Client Diagnostic Framework" in Drafts 2 and 15 IS outward-facing — a tool run on a client's business, not self-critique. Both flavors exist in this folder; don't conflate them.)

**Concrete intake forms and SLA templates remain entirely theory-only** — confirmed genuine absence, not unmigrated content.

### Client Success Process Library — Claude-synthesized (2026-06-30)

**Status: NOT owner-original content**, same authorization class and labeling discipline as the Offer department's synthesized offers (`02_Offer/OFFER_OS.md` §3). Built per explicit owner request to complete the offboarding/churn process and fill out the rest of the 9-stage lifecycle's missing workflows, since the source material confirmed a genuine absence rather than unmigrated content. Calibrated against: the real 5-layer onboarding model (Draft 16) for tone/structure, the 9-stage canonical lifecycle (§4), the self-critique checklists in Drafts 8/17 (used as a coverage checklist, noted per-workflow below), and cross-references to Sales (05), Operations (08), Finance (09), Marketing (03)/Content (04), and ClientPartner Acquisition (06) wherever a handoff occurs. Should be reviewed/approved or revised by the owner rather than treated as equally authoritative to the real onboarding content.

**Offboarding & Churn Process (the primary ask):**

| Step | Detail |
|---|---|
| 1. Trigger detection | Automated: `health_score` drop below threshold, contract end date within 60-90 days. Manual: client-initiated termination notice, non-payment escalation from Finance (09). |
| 2. Path classification | **Planned** (contract end, mutual, no distress signal) → skip retention attempt, go straight to step 4. **Unplanned** (churn risk, dissatisfaction, health-score-driven) → retention attempt (step 3) required first. **Involuntary** (non-payment, contract breach) → skip retention attempt, route to Finance (09) and Legal (10) per Constitution risk-class rules before proceeding. |
| 3. Retention attempt (unplanned only) | Account owner runs a structured "save" conversation: surface the specific risk signal, offer a modified scope/terms/discount if justified, set a decision deadline. If retention succeeds, exit this workflow and return `relationship_status` to active. If it fails or client declines, proceed to step 4. |
| 4. Offboarding kickoff | Internal notification: Finance (09) for final invoice/payment terms, Operations (08) for delivery wind-down, Sales (05)/Marketing (03) flagged only if win-back-relevant. No external communication until internal handoff is acknowledged. |
| 5. Asset & access handover | Deliverable export to client, access revocation on a defined timeline (not immediate — avoid disrupting any in-flight work product the client still needs), data retention/deletion per whatever real compliance requirements apply once Legal (10) is populated. |
| 6. Structured exit interview | Not an open-ended "why are you leaving" — uses the `churn_reason` taxonomy now in `CRM_SCHEMA.md`'s Client object (price, results-not-realized, fit-mismatch, internal-change-at-client, competitor, budget-cut, scope-creep-friction, non-payment, no-reason-given). Captured even for planned/amicable exits, since "no real reason, just done" is itself a real signal. |
| 7. Final financial close-out | Handoff to Finance (09): final invoice, any outstanding balance, refund logic if contractually applicable. |
| 8. Churn-reason logging | Logged against the Client record (`churn_reason`, `offboarding_type`) — feeds back into Offer (02) and Sales (05) as real signal once enough data accumulates (e.g., "results-not-realized" clustering on one offer type would be a real finding worth surfacing). |
| 9. Relationship classification | Every offboarded client gets a final `relationship_status`: **churned-alumni** (good exit, fine to reference/recontact), **churned-do-not-recontact** (bad exit, respect the boundary), or **win-back-candidate** (planned/neutral exit, real fit just bad timing — gets a re-entry review date). |
| 10. Advocacy check (even on exit) | A good-outcome offboarding (planned, high health-score) still gets an advocacy ask (testimonial/referral) before closing — churn doesn't automatically forfeit advocacy value if the engagement itself succeeded. |

**Risk coverage, addressing Draft 8's "no risk management" gap directly:** involuntary offboarding (non-payment/breach) is explicitly routed through Finance/Legal rather than handled as a standard CSM judgment call, consistent with the Constitution's risk-class escalation model (`AGENCY_OPERATING_CONSTITUTION.md` §5).

**Retention, Expansion, Advocacy, Re-entry workflows:** full step detail lives in §4's Workflow Index table above (kept there rather than duplicated here, since they're shorter than offboarding). Each directly addresses one of Draft 8/17's named gaps: Retention's monthly cadence = the "feedback loop" and "retention design" gaps; Expansion's ascension-fit check = the "expansion logic" gap; Advocacy's referral tracking = partially addresses "economics model" (referral-sourced revenue attribution, via the CRM's Partner object); account_owner on every workflow = the "no ownership" gap.

**What's still genuinely open after this build-out:** real dashboards/visibility tooling (Draft 8's gap) — these workflows assume a `health_score` and dashboard exist to monitor, but no real BI/dashboard tool is connected yet (same class of gap as Finance's and Marketing's unconnected integrations); concrete SLA templates and intake forms remain theory-only; and all of this is unvalidated against a real client, same as every other department's synthesized content.

## 11. RACI / Ownership

| Function | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| Onboarding | Client Success (07) | Client Success (07) | Sales (05) | Operations (08) |
| Retention | Client Success (07) | Client Success (07) | — | Finance (09) |
| Expansion | Client Success (07) | Sales (05) (owns the actual close) | Offer (02) | Finance (09) |
| Advocacy & referral | Client Success (07) | Client Success (07) | Marketing (03), ClientPartner Acquisition (06) | — |
| Offboarding (planned/unplanned) | Client Success (07) | Client Success (07) | Finance (09), Operations (08) | Sales (05) (if win-back-relevant) |
| Offboarding (involuntary) | Client Success (07) | Mary Thuo (per Constitution risk-class escalation) | Finance (09), Legal (10) | Agency Governance (00) |
| Re-entry / win-back | Client Success (07) | Sales (05) (owns re-qualification and the close) | — | Marketing (03) |

## 12. Triggers / Automation Hooks

*(placeholder — structure only; no automation concepts found beyond generic AI-agent-design boilerplate in Drafts 21-22, which is not client-management-specific — see §14)*

## 13. Existing OS Sub-Layer

None yet.

## 14. Raw Archive Pointer

~22 root-level "Draft N.md" files, all read in full for the 2026-06-30 content migration: client definition, segmentation, journey design, onboarding, fit/qualification, "Client OS," generic legal-entity-type explainers (not the agency's own legal infrastructure — see `10_Legal/`), flywheel, and system failures/gaps. Existing gap backlog: `07_Client_Success/00_Workspace_Intelligence_Inventory/`.

**Drafts 21-22 flagged as low-value for this department**: both drift out of client-success territory into generic AI-agent-orchestration / "Claude Coworker system prompt" design (folder structures like `/constitution`, `/governance`, `/agents`, `/runtime`), only superficially retrofitted with "Client" labels (e.g. `/clientos/constitution`). Contributed almost nothing to the registries above. Worth checking whether other departments have similarly-numbered "OS Architecture" files containing the same generic content under a different department label — same pattern independently flagged in Sector (01) Draft 13.

**Scope-blur findings — resolved (reconciliation pass, 2026-06-30):**

1. **Pre-sale qualification vs. post-sale segmentation.** Drafts 1 and 15's /25 qualification scoring (scoring leads *before* a sales call) is **reassigned to Sales (05)** — it matches that department's own citation-backed "Lead Qualification and Discovery Agent" capability almost exactly, and scoring happens upstream of this department's actual starting point (a closed deal). Draft 3's 5-type segmentation (Value/Needs/Behavioral/Lifecycle/Strategic) is confirmed as this department's real mandate — it's genuinely post-sale. Draft 13's flywheel, which places "Qualification + Client Selection" as one continuous filter before onboarding, is read as a pre-department-split framing (same pattern as the ClientPartner Acquisition reconciliation, see `06_ClientPartner_Acquisition/CLIENTPARTNER_OS.md` §10) — not evidence the two should stay merged. **Going forward: Client Success's Capability Registry (§3) owns segmentation only; qualification scoring belongs in `05_Sales/SALES_OS.md`.**

2. **Client Success → Operations (08) delivery handoff.** Reaffirmed as cleanly split: Client Success owns the relationship/journey and scopes the engagement (`scope_summary`, `sla_target_date` in `CRM_SCHEMA.md`'s Client→Project handoff); Operations executes delivery. `Client OS Architure. Draft 21.md` and the flywheel drafts (13, 14), which fold delivery into Client Success directly, are read as predating the Operations department concept entirely — Operations (08) has **zero raw draft content anywhere in this repo** (confirmed during its own skeleton pass), meaning none of this corpus was ever written with a separate delivery department in mind. `Clarification Request. Draft 5.md`'s clean assignment of delivery to "Operations / Service Team" is the one draft that already anticipates the split this repo's structure uses, and is treated as the more forward-looking source. **The handoff in this file's header (§ position-in-flow) stands as designed — no change needed.**

## 15. Changelog

- 2026-06-30 — File created as part of v0.1 skeleton restructuring (folder renamed from "The Agency Client. Drafts").
- 2026-06-30 — Content migration: all 22 raw drafts read. Capability Registry, Workflow Index, KPI Dictionary, and Standards & SOPs Index populated. Confirmed the "System Failures"/"Gaps" files (Drafts 8, 17) are self-critique of the agency's own client-success system design, not a client-facing diagnostic product (that's a separate, also-present tool in Drafts 2/15). Documented two scope-blur issues (qualification conflation with Sales; delivery-handoff conflation with Operations) rather than silently resolving them. Flagged Drafts 21-22 as low-value generic AI-architecture content mislabeled as client-success material.
- 2026-06-30 — Reconciliation pass: resolved both scope-blur issues above (now that Sales and Operations are both confirmed/migrated) and picked the 9-stage lifecycle model as canonical. See §3, §4, §8, §10. — Claude Code (Sonnet 4.6)
- 2026-06-30 — Built the full Client Success Process Library (Retention, Expansion, Advocacy, Offboarding & Churn, Re-entry/Win-back) per explicit owner request — Claude-synthesized, clearly labeled, calibrated against the real onboarding model and the self-critique gap checklists (Drafts 8, 17). Populated §3, §4, §7 (4 new KPI formulas), §9, §10, §11 (RACI). Cross-referenced new `Client` object fields into `CRM_SCHEMA.md`. Resolves tracker item 24. — Claude Code (Sonnet 4.6)
- 2026-07-01 — Added §16 Memory/Feedback Loop/Cadence (structure-only placeholder, per the go-live plan in 00_Agency_Governance/GO_LIVE_CHECKLIST.md). — Claude Code (Sonnet 5)

## 16. Memory / Feedback Loop / Cadence

*(placeholder — structure only, no agent roster exists yet to generate real memory/feedback entries; see §5, which reads "placeholder — none yet.")* Once this department has a real or code-based agent roster (per the Tier 1 pattern in `05_Sales/SALES_OS.md` §16), this section should define: **Memory** (where Decision/Learning/Prompt-Evolution logs live), **Feedback Loop** (what happens when a §7 KPI misses threshold), and **Cadence** (which of the 7 Cognitive Calendars — `00_Agency_Governance/AGENCY_REVENUE_TARGETS.md` §4 — this department's workflows run against, and how often).
