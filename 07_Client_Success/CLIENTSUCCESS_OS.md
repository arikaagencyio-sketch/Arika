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

## 4. Workflow Index

| Workflow | Trigger | Steps | Output | Owner | Source |
|---|---|---|---|---|---|
| Client onboarding sequence | Deal closed | Welcome/confirmation → onboarding form → internal review → kickoff call → define success metrics → start execution | Activated client | *(unassigned)* | Draft 16 |
| Outward-facing client diagnostic | Sales call / early engagement | 5-10 min scan to find a client's business bottleneck | Diagnostic output (sellable/usable on calls) | *(unassigned)* | Drafts 2, 15 |

**Lifecycle model — resolved (reconciliation pass, 2026-06-30).** 3 unreconciled models were found; the 9-stage Draft 2 version is now canonical, because it's the only one that maps cleanly onto this repo's own department flow (Sector→Offer→Marketing→Sales→Client→Operations→Finance) with no stage left ownerless:

- **9-stage (Draft 2) — canonical:** Awareness (Marketing/Content) → Interest/Consideration (Marketing/Content) → Conversion (Sales) → Onboarding (Client Success) → Delivery (Client Success → Operations handoff) → Retention (Client Success) → Expansion (Client Success) → Advocacy (Client Success → feeds ClientPartner Acquisition/Marketing) → Re-entry/Loop (back to Marketing/Content)
- 7-stage (Draft 1): Pre-Client → Prospect → Buyer → Active Client → Transformed Client → Retained/Expanded Client → Advocate Client — kept as a superseded alternate framing, not deleted; conceptually compatible with the 9-stage model (coarser granularity), no contradiction.
- 7-phase "Journey Orchestration" (Draft 21): Attraction → Qualification → Alignment → Activation → Transformation → Expansion → Continuity — kept as a superseded alternate framing; this is the same draft flagged in §14 as drifting into generic AI-agent-architecture content, so treat its stage names as lower-confidence than the other two.

Build any future onboarding/retention workflows against the 9-stage model.

## 5. Agent Roster

*(placeholder — none yet)*

## 6. Skill Library Index

*(placeholder — none yet)*

## 7. KPI Dictionary (department-local)

**All values illustrative/draft, inconsistent across files — never tied to real measurement.**

| Metric | Formula | Draft value(s) found | Source | Owner | Cadence | Threshold |
|---|---|---|---|---|---|---|
| Pre-sale qualification score | Sum of 5 filters /5 each = /25 | 20-25 ideal, 15-19 conditional, <15 reject (Draft 1); 20-25/15-19/10-14/<10 (Draft 15, different cut lines for the same scale) | Drafts 1, 15 | *(unassigned)* | *(unset)* | *(unset)* |
| Onboarding diagnostic score | 6 pass/fail checks | 5-6 / 3-4 / 0-2 | Draft 16 | *(unassigned)* | *(unset)* | *(unset)* |
| Generic metric names invoked, no values given | CAC, LTV, NPS, activation rate, engagement rate, progress rate, success rate, time-to-value | Named only | Drafts 7, 17 | *(unassigned)* | *(unset)* | *(unset)* |

**Note:** the two qualification-scoring drafts (1 and 15) use the same /25 scale but disagree on cut-line thresholds — flag rather than silently pick one if this gets operationalized.

## 8. Decision Log

- **2026-06-30 — Adopted the 9-stage (Draft 2) client lifecycle model as canonical**, superseding the 7-stage and 7-phase alternates (kept for reference, not deleted). See §4.
- **2026-06-30 — Reassigned pre-sale qualification scoring to Sales (05); confirmed post-sale segmentation as this department's actual mandate.** See §3, §10.
- **2026-06-30 — Reaffirmed the Client Success → Operations (08) delivery handoff** as designed (no change) — drafts that folded delivery into Client Success predate the Operations department concept. See §10. — Claude Code (Sonnet 4.6)

## 9. Risk / Incident Log

*(placeholder — empty. See §10's "system failures" content for self-identified risk areas, none of which have been logged as actual incidents.)*

## 10. Standards & SOPs Index

**Stated principles:**
- "A strong system rejects more clients than it accepts."
- "80% fixed process / 20% adaptive layer" for journey customization (Draft 10).
- "The client should never feel the complexity of the internal system" (Draft 21).

**Self-critique content — confirmed self-referential, not a client-facing diagnostic** (important distinction, verified 2026-06-30): `Client System Failures. Draft 8.md` and `Client Project Gaps. Draft 17.md` are introspective critiques of the agency's OWN client-success system design, not a diagnostic product sold to clients. Draft 8 lists 10 internal failure modes: no goal integrity, misaligned qualification, broken expectation-setting, weak onboarding, no execution layer, no feedback loop, no visibility/dashboards, poor retention design, no ownership, no standardization. Draft 17 lists missing internal systems: Control/Governance layer, Economics model, Behavior mapping, Communication system, Data/feedback loop, Success metrics, Role ownership, Value-based segmentation, Risk management, Expansion logic. **Treat these as a real, useful starting checklist for what this department's own SOPs need to eventually cover** — they're self-aware about the gap between theory and an operating system, which is a more useful signal than the generic frameworks elsewhere in this folder.

(Distinct from this: the "5-10 Minute Client Diagnostic Framework" in Drafts 2 and 15 IS outward-facing — a tool run on a client's business, not self-critique. Both flavors exist in this folder; don't conflate them.)

**Concrete intake forms, SLA templates, and an offboarding/churn process remain entirely theory-only** — confirmed genuine absence, not unmigrated content. Offboarding in particular has almost no content: it appears only as an empty filename placeholder in Draft 21's journey list.

## 11. RACI / Ownership

| Function | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| *(placeholder)* | | | | |

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
