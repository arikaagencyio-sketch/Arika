# Automation — Department OS

**Department:** Automation (16)
**Position in flow:** Horizontal support layer — closely tied to Operations (08) and Tech Stack (13), and the execution-layer counterpart to AI Enablement (17)'s strategic layer. Reports into Agency Governance (00).
**Mandate:** Own the agency's process-and-AI-workflow offers — AI Workflow Infrastructure and Business Operating Systems — both as sellable client offers and as the agency's own internal automation capability.
**Owner:** Mary Thuo

> See [`GLOBAL_OS.md`](../GLOBAL_OS.md) for how this file fits into the whole system. Read that first if you haven't.

---

## 1. Identity

**Newly created department (2026-06-30)**, promoted from a category inside the Offer (02) catalog after the owner decided Draft 28's "Automation" division deserved its own department. It houses two deliberately distinct offers: **AI Workflow Infrastructure** (the AI/agent execution layer — CRM automation, AI agents, workflow orchestration) and **Business Operating Systems** (the human/process layer — SOPs, dashboards, KPI ownership). These are a real two-offer split within one division, not duplicates — a client with a working team but no documented process needs Business Operating Systems before they need AI agents.

**Dual mandate, not just an offer line.** Because this department's offers are about automating execution, it is also the natural home for the agency's *own* internal automation — once any client-facing automation work matures, the same systems are the candidate first deployment for the agency's internal operations (cross-reference `00_Agency_Governance/AGENCY_VISION.md`'s Automation Vision layer).

## 2. Status

**Content seeded from Offer's catalog, not yet operationally run.** Full offer engineering exists for both founding offers:
- `02_Offer/OEOS - Automation Division - AI Workflow Infrastructure (Claude-Synthesized). Draft 35.md` — Phase 1 and Phase 2 positioning real (Draft 28); Phases 3-12 Claude-synthesized, owner-approved as-is 2026-06-30.
- `02_Offer/OEOS - Automation Division - Business Operating Systems (Claude-Synthesized). Draft 36.md` — Phase 1 real; Phases 2-12 Claude-synthesized, owner-approved as-is 2026-06-30.

No real automation engagements (client or internal) have run yet.

## 3. Capability Registry

| Capability | Description | Status |
|---|---|---|
| AI Workflow Infrastructure | AI/agent execution layer — CRM automation, AI agents, workflow orchestration, internal copilots | Offer engineered (`Draft 35`), not yet delivered |
| Business Operating Systems | Process/documentation layer — SOPs, dashboards, KPI ownership, org-design clarity | Offer engineered (`Draft 36`), not yet delivered |
| Internal automation (agency's own operations) | Same systems as above, applied to Arika Agency itself once mature enough to deploy internally | Not started — flagged as a future opportunity, not yet scoped |

## 4. Workflow Index

| Workflow | Trigger | Steps | Output | Owner | Source |
|---|---|---|---|---|---|
| AI Workflow Infrastructure delivery | Signed engagement | Discovery → Architecture Design → Build → Integration & Testing → Deployment & Training → Monitoring/Optimization | Deployed, monitored AI automations | Mary Thuo | `Draft 35` (synthesized) |
| Business Operating Systems delivery | Signed engagement | Discovery → Process Mapping → Redesign → Dashboard/KPI Build → Rollout & Training → Optimization | SOP library + dashboard system | Mary Thuo | `Draft 36` (synthesized) |

## 5. Agent Roster

*(placeholder — the offer-engineering files use functional role labels — Automation Engineer, Integration Specialist, Process Analyst, Dashboard/BI Engineer — describing AI-assisted execution functions the owner currently performs solo, not real hires. See `11_HR_People_Ops/HR_OS.md` for when real staffing becomes relevant.)*

## 6. Skill Library Index

*(placeholder — none yet)*

## 7. KPI Dictionary (department-local)

| Metric | Formula | Source | Owner | Cadence | Threshold |
|---|---|---|---|---|---|
| Automation failure rate | Failed automation runs ÷ total runs | `Draft 35` (QA gate: target <2%) | Mary Thuo | Continuous, post-deployment | *(unset — no real data yet)* |
| SOP adherence rate | Measured adoption ÷ documented process | `Draft 36` | Mary Thuo | Weekly | *(unset)* |

## 8. Decision Log

*(placeholder — empty)*

## 9. Risk / Incident Log

*(placeholder — empty. Note: `Draft 35` flags a hard immutable constraint — human-in-the-loop required for any client-facing AI output, no fully autonomous deployment without a review gate. Carries forward into any real incident logging once delivery begins.)*

## 10. Standards & SOPs Index

Full offer-engineering detail lives in `Draft 35` and `Draft 36` — cited here rather than duplicated.

## 11. RACI / Ownership

| Function | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| AI workflow delivery | Automation (16) | Automation (16) | Offer (02), AI Enablement (17) | Operations (08) |
| Business Operating Systems delivery | Automation (16) | Automation (16) | Offer (02) | Operations (08) |
| Internal automation deployment (agency's own ops) | Automation (16) | Mary Thuo | Operations (08), Tech Stack (13) | All departments |

## 12. Triggers / Automation Hooks

*(placeholder — structure only)*

## 13. Existing OS Sub-Layer

None yet — code-based automation not built. The offer-engineering content (`Draft 35`, `Draft 36`) is the canonical design reference.

## 14. Raw Archive Pointer

No department-local raw drafts. Source content lives in `02_Offer/` — see `02_Offer/OFFER_OS.md` §3 (Offer Engineering Registry, offers #6-7) and `Agency Pricing Architure. Draft 28.md` for the original seed material.

## 15. Changelog

- 2026-06-30 — Department created, promoted from Offer (02)'s "Automation" division category per owner decision. Seeded from `Draft 35` (offer #6, AI Workflow Infrastructure) and `Draft 36` (offer #7, Business Operating Systems), both owner-approved as-is the same day. — Claude Code (Sonnet 4.6)
