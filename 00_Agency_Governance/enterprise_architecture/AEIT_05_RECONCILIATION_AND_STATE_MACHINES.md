# AEIT_05 — Reconciliation Decisions & State Machines (Validation)

**Version:** v0.1
**Last updated:** 2026-07-22
**Owner:** Mary Thuo (Agency Governance, 00)
**Fills:** `REGISTRY_TAXONOMY_REFERENCE.md` future-state registry **State (system state machine)**;
resolves the coherence findings in `AEIT_04`.
**Status:** ✅ **R1–R5 ratified by the Owner 2026-07-22.** The decisions are now canonical for AEIT
purposes; **enactment** (e.g. editing `CRM_SCHEMA.md:23`, renaming Sector priority bands, deleting
the dead ClickUp template) is spec-only in Phase Zero and is **queued as roadmap items in
`AEIT_10`**, not applied here — keeping "decide" and "apply" separate with an audit trail.

> This is the reconcile-first output. Part 1 resolves ownership/terminology conflicts; Part 2
> formalizes the agency's lifecycle state machines (two already exist as CRM enums; one — Knowledge
> — is new and feeds IntOS).

---

## Part 1 — Reconciliation decisions (proposed canonical)

### R1 — ICP / prospect scoring ownership *(resolves AEIT_04 §A1)*
- **Conflict:** Sector (01) produces ICP classification (`SECTOR_OS.md:90,162`) but the CRM field
  `ICP_fit_score` is owned by Sales (`CRM_SCHEMA.md:23`); Marketing and ClientPartner also score.
- **Proposed canonical:**
  - **Sector (01) owns ICP classification and prospect signal scoring.** It *sets* `ICP_fit_score`
    and emits `ICP_CLASSIFIED` / `PROSPECT_SCORED`.
  - **Sales (05) owns qualification decisioning** — it *consumes* the Sector score to decide pursue/
    advance, and owns `qualification_status`, not the raw fit score.
  - **Marketing (03) and ClientPartner (06)** *reference* the Sector scorecard; they do not maintain
    parallel scoring models. (ClientPartner's *partner* `fit_score`/`trust_score` are a distinct
    partner-relationship measure and stay — they are not ICP.)
  - **Change required:** amend `CRM_SCHEMA.md:23` field-owner from "Sales (05)" to
    "set by Sector (01), consumed by Sales (05)".
- **Ratification needed:** confirm Sector, not Sales, owns the fit score. **Owner decision.**

### R2 — Canonical entity term *(resolves AEIT_04 §B1)*
- **Proposed canonical:** the served entity is **"Client"** everywhere. **"Account"** is reserved
  for the billing/finance sense only. **"Customer"** is deprecated (the 13 occurrences across 7 OS
  files are corrected opportunistically, not urgently). Enshrined in the `AEIT_06` glossary.
- **Ratification needed:** none of substance — this is a naming standard; Owner may simply approve.

### R3 — Risk vs priority vocabulary *(resolves AEIT_04 §B2)*
- **Proposed canonical:** **Risk** uses the Constitution's **5-class numeric** system, everywhere,
  with no synonyms. **Prospect priority** (Sector's 90-pt bands) is renamed to **P1–P4** (or
  "priority: low/medium/high/urgent") so the word **"Critical" never denotes two things**.
- **Change required:** rename the Sector priority band labels (`SECTOR_OS.md:68,89`); keep the
  numeric mapping table in Sales for backward reference.
- **Ratification needed:** approve the renamed band labels. **Owner decision (light).**

### R4 — "Pipeline" disambiguation *(resolves AEIT_04 §B3)*
- **Proposed canonical:** always qualify the noun — **"Pipeline Calendar"** (the cognitive
  calendar), **"Sales pipeline"** (deal stages), **"Acquisition/Partner/Delivery pipeline"**
  (ClientPartner). Glossary entry; no structural change.

### R5 — "CRM" disambiguation *(resolves AEIT_04 §A2)*
- **Proposed canonical:** three named, separated things — **Agency CRM** (canonical, Governance-owned,
  `CRM_SCHEMA.md`, live in ClickUp); **Client-CRM deliverable** (a ClientPartner *product*); and the
  empty ClickUp "Sales CRM" template `901511301824`, which is **deleted** (roadmap cleanup, `AEIT_10`).

### Reconciliation summary
| ID | Decision | Change surface | Ratification weight |
|---|---|---|---|
| R1 | Sector owns ICP fit; Sales owns qualification | `CRM_SCHEMA.md:23` | **Owner call** |
| R2 | "Client" canonical; "account"=billing; "customer" deprecated | glossary + opportunistic edits | Light |
| R3 | Risk=5-class numeric; priority=P1–P4 | `SECTOR_OS.md` labels | Light |
| R4 | Qualify every "pipeline" | glossary | None |
| R5 | Three named CRMs; delete dead template | Tech Stack cleanup | Light |

---

## Part 2 — Enterprise state machines

The agency needs explicit **states**, not just workflows, so every department knows exactly where a
Client, Partner, or piece of Knowledge is. Two lifecycles already exist as CRM enums (formalized
below); the **Knowledge lifecycle is new** and is the backbone of IntOS (`AEIT_07`).

### SM1 — Client lifecycle *(formalizes `CRM_SCHEMA.md:47`, `CLIENTSUCCESS_OS.md` §4)*
`lifecycle_stage`:
```
onboarding → delivery → retention → expansion → advocacy → offboarding → re-entry-loop
```
Overlaid `relationship_status` (`CRM_SCHEMA.md:48`):
```
active → at-risk → offboarding → churned-alumni
                              ↘ churned-do-not-recontact
        at-risk → win-back-candidate → (re-entry-loop → onboarding)
```
- **Owner:** Client Success (07). **Pre-lifecycle** (prospect→lead→opportunity→client) is owned by
  Sector→Marketing→Sales (see SM3).

### SM2 — Partner lifecycle *(formalizes `CRM_SCHEMA.md:78`)*
```
ecosystem-mapping → relationship-initiated → strategic-assessment → capability-validation
  → co-value-modeling → integration-planning → pilot-engagement → active-partnership → expansion
                                                                        ↘ dormant
                                                                        ↘ terminated
```
- **Owner:** ClientPartner Acquisition (06).

### SM3 — Commercial (prospect→client) state machine *(consolidates Sector + Sales stages)*
```
observed(prospect) → scored → ICP-classified → lead → qualified → opportunity
  → proposal → negotiation → won(Client → SM1) | lost(recovery loop)
```
- **Owners by segment:** Sector (01) observed→classified; Marketing/Content/ClientPartner
  lead-generation; Sales (05) qualified→won/lost. This makes the handoff points (`CRM_SCHEMA.md:102`)
  state-explicit.

### SM4 — Knowledge lifecycle *(NEW — the IntOS backbone)*
Every piece of information the agency holds carries an explicit state, so nothing is treated as more
trustworthy than it is:
```
Observed → Collected → Validated → Verified → Normalized → Enriched → Trusted
  → Distributed → Consumed → Learned → Archived
                                    ↘ (Confidence decay / staleness) → Revalidate → Verified
```
- **State attributes** carried on every knowledge object: `confidence`, `trust`, `freshness`
  (last-verified date), `source_id`, `owner`. Decay/staleness triggers a return to Revalidate — the
  same "last-verified, not just activation date" discipline Tech Stack invented
  (`TECHSTACK_OS.md:152`) generalized to all knowledge.
- **Owner:** the future IntOS (designed in `AEIT_07`); until it exists, no department may assert a
  knowledge object is "Trusted" without a stated basis.

---

## Part 3 — What must be ratified before Stage 4

Stage 4 (`AEIT_06`+) assumes R1–R5 and SM1–SM4. The **only decision requiring genuine Owner
judgment is R1** (does Sector or Sales own the ICP fit score?). R2–R5 are naming/standards the Owner
can approve wholesale. If R1 is decided differently, `AEIT_06`'s entity ownership is updated
accordingly. Ratification requests are logged to `../OWNER_INPUT_NEEDED.md`.

---

## Decision Log
- **2026-07-22 — Reconciliation proposed.** R1–R5 drafted as proposals; SM1–SM3 formalized from
  existing enums; SM4 (Knowledge lifecycle) introduced as the IntOS backbone. Ratification of R1
  routed to Owner. — Claude Code (Opus 4.8)
- **2026-07-22 — R1–R5 RATIFIED by Owner.** R1 confirmed **Sector (01) sets `ICP_fit_score`, Sales
  (05) consumes**. R2–R5 approved. Enactment queued in `AEIT_10` (spec-only in Phase Zero).
  `AEIT_06` entity ownership reflects the ratified R1. — Claude Code (Opus 4.8)

## Changelog
- **v0.1 (2026-07-22):** Created. — Claude Code (Opus 4.8)
