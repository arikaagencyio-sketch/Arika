# Registry Taxonomy Reference (Full 41-Registry Ontology)

**Status: Reference only — not the active operating structure.** This document preserves the complete enterprise registry ontology developed during this repo's architectural planning (two brainstorming sessions, summarized in `14_Cross_Domain_Synthesis/`). It is the *future-state* map of everything a fully mature AI-native agency operating system could track.

For v0.1, only a curated subset (~12) of these registries is active, embedded as standard sections inside each department's `{DEPT}_OS.md` — see `GLOBAL_OS.md` §6 for the active pattern. This file exists so the full ambition isn't lost, and so future expansion has a ready-made target instead of being reinvented from scratch.

**Do not build out the remaining registries below until the curated subset is actually populated with real content and proves insufficient.** Premature build-out of registries with no content is structure for its own sake.

---

## Currently active (embedded in department OS files)

1. **Capability Registry** — what each department can produce/do
2. **Workflow Registry** — repeatable processes per department
3. **Agent Registry** — agents/sub-agents per department
4. **Skill Registry** — atomic capabilities per department
5. **KPI / Metrics Registry** — department-local metrics, formulas, owners, thresholds
6. **Decision Registry** — append-only log of significant decisions
7. **Risk / Incident Registry** — append-only log of risks and incidents
8. **Standards Registry** — SOPs and quality standards per department
9. **Governance / RACI Registry** — ownership and decision rights per department
10. **Trigger / Automation Registry** — events that should fire automation
11. **Knowledge Registry** — pointer to each department's raw source archive

## Future-state — not yet built

**Foundation:** Domain, Service, Offer (note: Offer already has a dedicated department, 02), Identity, Context, Dependency, Semantic/Ontology

**Entities:** Client, Project, Task, Lead, Invoice, Asset, Contract

**Governance:** Permission, Audit, Compliance, Policy, Constraint

**Intelligence:** Learning, Feedback, Intelligence (external/competitive), Opportunity, Experiment

**Operations:** State (system state machine), Priority/Attention, Energy/Cost, CircuitBreaker/Safety, Signal/Noise

**Communication:** Protocol (plugin/department-to-department contracts), Message/Event

**Lifecycle:** PluginDNA (department anatomy/health metrics), Evolution/Change

**Meta:** Consciousness (self-awareness/reflection cycles), Narrative (agency story/culture), MetaRegistry (registry of registries)

**Safety & Quality:** Security, Ethics, Testing/QA, Boundary (inside vs. outside the system)

**Visibility:** Instrumentation/Telemetry, Forecasting, MasterDashboard

**Cross-cutting:** Objective, Strategy, Production (deployment/environments), Resource, Ecosystem (partners/vendors), Relationship (entity graph), Execution (work actually performed), Financial (economics beyond Finance department's own ledger), Change

---

## When to promote a future-state registry to active

A registry should move from this reference list into the active curated set (§6 of `GLOBAL_OS.md`) when at least one of these is true:

- A department's content-migration pass surfaces real, recurring content that doesn't fit any of the 11 currently-active registry sections.
- The agency starts operating multiple clients/projects simultaneously and needs a genuine cross-department Client or Project registry (not just department-local mentions of clients).
- Real automation gets built and needs a Protocol Registry to define how departments' agents actually communicate (today's Triggers/Automation Hooks sections are placeholders, not live integrations).
- A security or compliance review surfaces a concrete need for the Security/Ethics/Boundary registries beyond what Legal (09) already covers.

Promoting a registry means: add it as a new standard section to the `{DEPT}_OS.md` template (update `GLOBAL_OS.md` §6's table), not necessarily creating a new top-level folder — most of these registries are still better as department-local sections than agency-wide folders, per the same reasoning that kept the curated set small in the first place.
