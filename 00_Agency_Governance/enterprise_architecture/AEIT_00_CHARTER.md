# AEIT_00 — Charter & Index

**Initiative:** Agency Enterprise Intelligence Transformation (AEIT) — Phase Zero
**Version:** v0.1
**Last updated:** 2026-07-22
**Owner:** Mary Thuo (Agency Governance, 00)
**Author of this pass:** Claude Code (Opus 4.8)
**Status:** Complete — all 11 artifacts written; R1–R5 ratified 2026-07-22 (R1: Sector sets
`ICP_fit_score`); enactment queued in `AEIT_10` Phase 0 (Implementation Protocol, deferred).

---

## 1. Mandate

Before any **Intelligence Operating System (IntOS)** is built, verify that the agency is
**internally coherent as an enterprise**, and produce an implementation-ready architecture package
that a future implementation session (and every future feature) can trace back to.

This is an **enterprise architecture review**, not a code review, prompt review, or repository
review. It exists to *understand, reconcile, and blueprint* — not to implement.

### What this initiative IS
- A right-sized reconciliation of what the agency has already built, plus a design for the
  genuinely-missing pieces (chiefly IntOS).
- A set of governance-owned, versioned specifications and maps.
- A prioritized, reality-gated roadmap.

### What this initiative is NOT
- Not implementation. **No code is written, no live system is touched** (CRM, agents,
  `arika-runtime`, crons) during Phase Zero.
- Not a green-field redesign. The repo already contains a strong governance backbone, a live CRM
  schema, 7 cognitive calendars, a 41-registry taxonomy, a rigid 16-section department template,
  and 106 agents. Phase Zero **consolidates and corrects**, it does not restart.
- Not a licence to invent agency facts. Missing owner facts are flagged to
  `../OWNER_INPUT_NEEDED.md`, never fabricated (`CLAUDE.md` / Constitution rule).

---

## 2. Method — four protocols across five stages

The user's requested protocol sequence (Discovery → Analysis → Validation → Blueprint →
[Implementation, deferred]) maps onto five delivery stages:

| Stage | Protocol | Artifacts | Reviewable output |
|---|---|---|---|
| 0 | — | `AEIT_00` (this file) | Charter, index, review gate |
| 1 | Discovery | `AEIT_01` | Current-state map |
| 2 | Analysis | `AEIT_02`, `AEIT_03`, `AEIT_04` | Dependency matrix, capability map, gap report |
| 3 | Validation | `AEIT_05` | Reconciliation decisions + state machines |
| 4 | Blueprint | `AEIT_06`–`AEIT_09` | Canonical model/graph, IntOS, source registry, contracts |
| 5 | Blueprint (roadmap) | `AEIT_10` | Prioritized roadmap + risk register |

**Reconcile-first gate:** Stages 1–3 are delivered and reviewed by the Owner *before* Stage 4 is
written, so the IntOS blueprint is designed on a reconciled foundation rather than inheriting
today's coherence bugs.

---

## 3. Package index

| # | File | Purpose | Status |
|---|---|---|---|
| 00 | `AEIT_00_CHARTER.md` | Mandate, method, index, review gate | ✅ written |
| 01 | `AEIT_01_CURRENT_STATE.md` | Where the agency actually is; four-platform reality; exists/missing | ✅ |
| 02 | `AEIT_02_DEPENDENCY_MATRIX.md` | System → depends-on/consumes/produces/owner/risk | ✅ |
| 03 | `AEIT_03_CAPABILITY_MAP.md` | Agency-wide capabilities × owning/consuming departments | ✅ |
| 04 | `AEIT_04_GAP_AND_DUPLICATION_REPORT.md` | Cited coherence findings + resolutions | ✅ |
| 05 | `AEIT_05_RECONCILIATION_AND_STATE_MACHINES.md` | Proposed canonical decisions + lifecycle state machines | ✅ |
| — | **OWNER REVIEW GATE** | Stages 1–3 ratified before Stage 4 | ✅ |
| 06 | `AEIT_06_CANONICAL_MODEL_AND_KNOWLEDGE_GRAPH.md` | Canonical entity model/ontology + knowledge-graph edges | ✅ |
| 07 | `AEIT_07_INTOS_BLUEPRINT.md` | The Intelligence Operating System design | ✅ |
| 08 | `AEIT_08_SOURCE_REGISTRY_AND_INTELLIGENCE_CALENDAR.md` | Global source registry spec + refresh/decay calendar | ✅ |
| 09 | `AEIT_09_INTERFACE_CONTRACT_STANDARD.md` | Cross-department handoff-packet standard | ✅ |
| 10 | `AEIT_10_ROADMAP_AND_RISK.md` | Prioritized, reality-gated roadmap + risk register | ✅ |

Each artifact fills a gap the repo itself already names — either in `GLOBAL_OS.md` §11 (Open Gaps)
or `REGISTRY_TAXONOMY_REFERENCE.md` "Future-state — not yet built." Traceability table:

| AEIT artifact | Fills named gap |
|---|---|
| `AEIT_02` | Registry taxonomy future-state: **Dependency** |
| `AEIT_05` (state machines) | Future-state: **State (system state machine)** |
| `AEIT_06` | Future-state: **Semantic/Ontology**, **Relationship (entity graph)** |
| `AEIT_07` | Future-state: **Intelligence, Learning, Feedback**; §11 item 8 (memory protocol) |
| `AEIT_08` | §11 item 1: **Agency Global Source Registry** (Open) |
| `AEIT_09` | §11 item 6: **Handoff packet standards** (Partially open); future-state **Protocol** |
| `AEIT_10` | §11 item 9 (Dashboard spine) sequenced; overall roadmap |

---

## 4. Governing principles for this package

1. **Right-sized.** Recommend the simpler option wherever added complexity does not add strategic
   value. A solo, pre-revenue business does not get 500-person process weight.
2. **Reconcile before build.** Coherence first; new platforms second.
3. **Proposals, not enactment.** Every reconciliation decision is a *proposed canonical resolution
   pending Owner ratification*. Agency-policy calls (e.g. who owns ICP scoring) are the Owner's.
4. **No silent invention.** Missing facts → `../OWNER_INPUT_NEEDED.md`.
5. **Reality-gated.** The roadmap sequences everything behind the real blockers (legal existence,
   automation activation, first content/clients) — see `AEIT_10`.

---

## 5. Architecture Review Checklist (the proportionate gate)

The user asked that Claude become an "Enterprise Architecture Reviewer" so nothing enters
production without review. For a solo+AI agency, the proportionate form of that gate is a short
pre-merge checklist — **not** a 13-stage review board. Any new system/feature/agent/workflow
should answer:

- [ ] **Canonical fit** — does it reuse a canonical entity/registry, or does it reinvent one? (If it
      reinvents, stop — extend the canonical model instead.)
- [ ] **Ownership** — is there exactly one owning department? Any second claimant is a conflict.
- [ ] **Contract** — what does it receive, produce, and who consumes it? (Reference the
      `AEIT_09` handoff standard.)
- [ ] **Dependencies** — does it add a circular or hidden dependency? (Check against `AEIT_02`.)
- [ ] **Governance** — for automations: is there an Approval Matrix row (trigger/action/risk
      class/rollback/human gate) *before* it can fire?
- [ ] **Reality** — can it actually run today (API key, auth, activation), or is it structure ahead
      of content? Label honestly.
- [ ] **Logged** — is the decision recorded in the relevant Decision Log?

This checklist is itself a deliverable of Phase Zero; it becomes an operating habit, not a bureaucracy.

---

## 6. Explicitly deferred (with activation triggers)

Building these today would add empty structure faster than a solo pre-revenue business fills it:

- **The 15-chapter Enterprise Design Specification (EDS) "constitution"** and **formal branded
  EGOS / IntOS / OrchOS / RevOS platform specs.** *Trigger:* legal entity exists **and** the
  automation layer is proven to run on a schedule **and** first clients/revenue create real content.
  Until then, `AEIT_10` describes the four-platform target framing; the existing Governance folder +
  `arika-runtime` already serve those functions unbranded.
- **Populated source-registry data, live knowledge-graph instances, per-pair contracts for every
  department.** *Trigger:* IntOS blueprint approved and activation unblocked.

---

## 7. Decision Log

- **2026-07-22 — AEIT Phase Zero chartered.** Scope set to *right-sized* and priority to
  *reconcile-and-stabilize first* (Owner decisions via clarifying questions). Package = 11 artifacts
  under `00_Agency_Governance/enterprise_architecture/`. Full 33-artifact directive + 15-chapter EDS
  + 4 formal platform specs deferred with triggers (§6). — Claude Code (Opus 4.8)

## 8. Changelog

- **v0.1 (2026-07-22):** Charter created; package index and review checklist established. — Claude Code (Opus 4.8)
