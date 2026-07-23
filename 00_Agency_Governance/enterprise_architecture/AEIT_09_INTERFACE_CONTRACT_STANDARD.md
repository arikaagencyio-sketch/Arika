# AEIT_09 — Cross-Department Interface Contract Standard (Blueprint)

**Version:** v0.1
**Last updated:** 2026-07-22
**Owner:** Mary Thuo (Agency Governance, 00)
**Fills:** `GLOBAL_OS.md` §11 item 6 (*Handoff packet standards between departments* — Partially
open); `REGISTRY_TAXONOMY_REFERENCE.md` future-state **Protocol** registry.
**Depends on:** `AEIT_06` (canonical entities exchanged), `AEIT_05` SM3 (commercial states).
**Status:** Standard + worked examples. Agent-level I/O contracts already exist in frontmatter; this
raises them to the **department-pair** level.

> Today the flow is described narratively (`GLOBAL_OS.md` §5) and seeded by the CRM Handoff Points
> table (`CRM_SCHEMA.md:102`). This document gives every department handoff **one packet shape** so
> nothing is dropped, and each side knows exactly what it owes the other.

---

## 1. The Handoff Packet template

Every department-to-department handoff publishes a packet with these fields:

| Field | Meaning |
|---|---|
| `handoff_id` | producer→consumer + entity (e.g. `sector→sales:ICP`) |
| `producer` / `consumer` | the two departments |
| `trigger` | the event/state that emits the packet (a `Signal` or state transition) |
| `payload` | canonical entities + fields transferred (must reference `AEIT_06`, not ad-hoc shapes) |
| `validation_rules` | what the consumer checks before accepting |
| `confidence_threshold` | minimum confidence to act on (ties to IntOS scoring) |
| `freshness_requirement` | max age of the payload's last-verified date |
| `owner` | who owns the *contract* (usually the producer) |
| `SLA / cadence` | how quickly / how often the handoff happens |
| `failure_modes` | what happens if payload is missing/stale/rejected + the fallback |

**Rule:** a handoff packet may only carry **canonical entities** (`AEIT_06`). If a handoff needs a
shape that isn't canonical, that's a signal to extend the model — not to invent a local one
(the Architecture Review Checklist, `AEIT_00 §5`).

---

## 2. Worked examples (highest-traffic handoffs)

### HP-1 — Sector (01) → Sales (05): ICP & prospect score
| Field | Value |
|---|---|
| trigger | `ICP_CLASSIFIED` / `PROSPECT_SCORED` emitted (`SECTOR_OS.md:162`) |
| payload | `Company`, `ICP Classification {tier, ICP_fit_score}` **set by Sector (R1)**, `Prospect Signal Score {P1–P4}` |
| validation | Sales checks tier ≠ Anti-ICP; score freshness ≤ 30 days (Sector's re-score decay rule) |
| confidence_threshold | act on Tier 1/2 with High/urgent priority |
| owner | Sector (01) |
| failure_modes | stale score → Sales requests re-score; Anti-ICP → `educate_dont_sell`, no pursuit |

### HP-2 — Marketing (03)/Content (04)/ClientPartner (06) → Sales (05): Lead→Opportunity
| Field | Value |
|---|---|
| trigger | qualified lead ready (`CRM_SCHEMA.md:102`) |
| payload | `Lead {source, ICP_fit_score (from Sector), touch_history}` → `Opportunity` |
| validation | Sales verifies `ICP_fit_score` present and set-by-Sector; source attributed |
| confidence_threshold | qualification firewall (`sales-lead-qualification`) |
| owner | producing department; contract co-owned with Sales |
| failure_modes | missing ICP score → route back to Sector (HP-1) before qualifying |

### HP-3 — Sales (05) → Client Success (07): Won → Onboarding
| Field | Value |
|---|---|
| trigger | Opportunity → **won** (SM3), Client created (SM1 `onboarding`) |
| payload | `Client {company_id, offer_id, scope, commercials}` |
| validation | CS confirms scope + success metrics defined before accepting |
| owner | Sales (05) |
| failure_modes | scope undefined → onboarding blocked; escalate to Owner |

### HP-4 — Client Success (07) → Operations (08) → Finance (09): Deliver → Bill
| Field | Value |
|---|---|
| trigger | scoped engagement (CS) → delivery (Ops) → billable event (Fin) |
| payload | `Project {scope}` → delivered work → `Invoice {amount USD-priced/KES-invoiced}` |
| validation | Ops confirms capacity (`operations-capacity-planner`); Finance confirms conversion rate |
| owner | each producing department for its leg |
| failure_modes | **USD→KES conversion calculator not built** (`AEIT_04`/`AEIT_10`) → Finance leg blocked until it is |

---

## 3. Relationship to existing agent contracts

Agent frontmatter already declares `inputs`, `output_schema`, `emits`, `handoff_to` — those are the
**implementation** of these packets at the agent level. This standard is the **department-pair
contract** they must conform to. Where an agent's `emits` has no matching consumer contract, that's
a gap to close (an orphaned emit).

## 4. What is deferred
- Contracts for **every** department pair. Phase Zero specifies the template + the 4 spine handoffs;
  the rest are authored as each pair goes live (`AEIT_10`), not pre-written for pairs that never
  exchange anything yet.

## 5. Decision Log
- **2026-07-22 — Interface contract standard set.** One handoff-packet template + 4 worked spine
  examples; canonical-entities-only rule adopted; agent frontmatter positioned as the packet's
  implementation layer. — Claude Code (Opus 4.8)

## 6. Changelog
- **v0.1 (2026-07-22):** Created. — Claude Code (Opus 4.8)
