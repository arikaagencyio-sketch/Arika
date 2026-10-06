# Hospitality Vertical — Forensic Audit & Alignment (2026-10-07)

**Owner of record:** Agency Governance (00) — filed beside the AEIT series, the estate audit and the readiness assessment, which is this repository's existing home for enterprise-architecture reviews.
**Type:** Audit only. **Read-only with respect to the existing system** — no existing file was modified, renamed, moved or deleted to produce this package.
**Measured:** 2026-10-06 (gates and suites run) · **written:** 2026-10-07 · repository HEAD `48cdb74` (2026-10-06 23:32 +0300), working tree clean before and after.
**Produced by:** Claude Code (Opus 5.5), against the owner's pasted *Hospitality Vertical Forensic Audit & Alignment Protocol*.

> **Read [`20_EXECUTIVE_SUMMARY.md`](20_EXECUTIVE_SUMMARY.md) first.** It answers the protocol's 24 final questions in four pages. Every other file is the evidence behind it.

---

## 1. What was done — and what was deliberately not done

| Done | Not done (by design) |
|---|---|
| Read `GLOBAL_OS.md`, every governance file in `00_Agency_Governance/`, the AEIT package, every department `{DEPT}_OS.md` the vertical touches, all Hospitality artefacts (plugin, sidecar, Draft 41, worksheet, readiness packet, intake overlay, A001 records, prospecting cycle), the runtime source, the CRM/intake/provisioning code, the relevant agent and skill specs | **No Notion, ClickUp, Zoho, Canva, Google, Postiz or website call.** This repository records even read-only CRM schema checks as *owner-authorised* events (`CRM_SCHEMA.md` live-check note, 2026-09-22). None was authorised for this audit, so every live-store state below is quoted from its last recorded verification, with its date, and marked accordingly |
| Ran, read-only: `p2_coverage_gate.py`, `skill_run_gate.py`, `sector_truth_gate.py`, `estate_event_gate.py`, the prospecting test suite (8), the `arika-runtime` suite (71) | No `.env` file was opened. No agent, skill or model call was made. No memory stream was written — five memory logs were hashed before and after the runtime suite and are byte-identical |
| Grepped the whole repository for every concept the protocol names (pre-experience, tennis, B2B2C, revenue centre, occasion, MICE, …) | No raw `Draft N.md` file was treated as fact. Raw drafts were consulted only through their department OS files, as `CLAUDE.md` requires |
| Reconciled every finding against prior audits (`AEIT_04`, `AEIT_11_ESTATE_AUDIT.md`, `READINESS_ASSESSMENT_2026-10-02.md`, `A001_*`) so a known item is cited, not re-reported as new | No department Decision Log or changelog was updated — the protocol forbids modifying existing files. The proposed log entries are in §5 below, for the owner to apply |

## 2. Evidence and status vocabularies — reused, not invented

This package uses the repository's own vocabularies wherever one exists, per `AEIT_06` (*"departments consume canonical entities; they do not reinvent them"*).

| Axis | Values | Source |
|---|---|---|
| **Confidence in a finding** (the protocol's own) | `CONFIRMED` — read in a file, read in code, or reproduced by a run · `LIKELY` — strongly implied by several files, not directly stated · `INFERRED` — reasoned from structure, no direct statement · `UNKNOWN — HUMAN INPUT REQUIRED` | Protocol §29 |
| **Reality state** of a capability | `INTENDED` · `DESIGNED` · `BUILT` · `CONNECTED` · `LIVE` — *a state is claimed only with its named test* | `AEIT_11_RUNTIME_TRUTH_STANDARD.md` §2–§3 |
| **Kind of absence** | `UNASSIGNED` (needs a decision) · `OWNED-UNBUILT` (needs a build) · `EXTERNAL-BY-DESIGN` (needs only a label) | `AEIT_11` R7 |
| **Gap class** | `EXISTING` · `EXTEND` · `NEW` · `DUPLICATE` · `REFACTOR` · `REMOVE` · `GOVERNANCE GAP` · `DATA GAP` · `INTEGRATION GAP` · `WORKFLOW GAP` · `METRIC GAP` · `UNKNOWN` | Protocol §23 |
| **Priority** | `P0` integrity/blocking · `P1` required for the Hospitality pilot · `P2` required for scale · `P3` optimisation · `P4` future | Protocol §24 |
| **Evidence chain** | `FILE → COMPONENT → FUNCTION → BEHAVIOUR → CONCLUSION`, written compactly as `E:` lines | Protocol §29 |

**Audit-local identifiers.** Findings are `HV-nn` (file 14), remediation actions `RM-nn` (file 15), decisions `HD-nn` (file 18), open questions `HQ-nn` (file 19), information requests `IR-<group><n>` (file 17). File 13 shows that this repository already runs more than fifteen identifier namespaces; these five are **temporary**. On adoption, each surviving item should be re-issued as an `OWNER_INPUT_NEEDED.md` item number or a department Decision Log entry, and the audit-local ID retired.

## 3. File index

| # | File | Answers protocol § |
|---|---|---|
| 01 | [`01_SYSTEM_INVENTORY.md`](01_SYSTEM_INVENTORY.md) | §2 — everything that exists |
| 02 | [`02_CURRENT_ARCHITECTURE.md`](02_CURRENT_ARCHITECTURE.md) | §3 — the evidence-based layer map |
| 03 | [`03_HOSPITALITY_ALIGNMENT.md`](03_HOSPITALITY_ALIGNMENT.md) | §1, §6, §7 — where Hospitality belongs; property types; revenue centres; experience model |
| 04 | [`04_ENTITY_AND_DATA_MODEL.md`](04_ENTITY_AND_DATA_MODEL.md) | §20, §21 — entities, relationships, sources of truth |
| 05 | [`05_WORKFLOW_MAP.md`](05_WORKFLOW_MAP.md) | §4 (flow side), §22 (handoffs) — workflows and handoffs |
| 06 | [`06_CALENDAR_ARCHITECTURE.md`](06_CALENDAR_ARCHITECTURE.md) | §11, §12 — calendars, seasonality, destination intelligence |
| 07 | [`07_REVENUE_AND_DEMAND_MODEL.md`](07_REVENUE_AND_DEMAND_MODEL.md) | §14 — content → demand → revenue, attribution |
| 08 | [`08_B2B_B2C_NETWORK_MODEL.md`](08_B2B_B2C_NETWORK_MODEL.md) | §10, §13 — relationship pathways and buyer roles |
| 09 | [`09_PROSPECTING_ALIGNMENT.md`](09_PROSPECTING_ALIGNMENT.md) | §16, §17 — prospecting and agency self-marketing |
| 10 | [`10_CLIENT_LIFECYCLE_ALIGNMENT.md`](10_CLIENT_LIFECYCLE_ALIGNMENT.md) | §15 — prospect → client → retention |
| 11 | [`11_PRE_EXPERIENCE_ALIGNMENT.md`](11_PRE_EXPERIENCE_ALIGNMENT.md) | §8, §18 — Pre-Experience and the corporate-tennis prototype |
| 12 | [`12_AI_GOVERNANCE_AND_PRODUCTION.md`](12_AI_GOVERNANCE_AND_PRODUCTION.md) | §9 — AI's role and safeguards |
| 13 | [`13_TICKET_AND_WORK_ITEM_AUDIT.md`](13_TICKET_AND_WORK_ITEM_AUDIT.md) | §4, §5 — work items, approvals, "ready" |
| 14 | [`14_GAPS_AND_DISCONNECTIONS.md`](14_GAPS_AND_DISCONNECTIONS.md) | §19, §22, §23, §25 — every finding, classified |
| 15 | [`15_PRIORITISED_REMEDIATION.md`](15_PRIORITISED_REMEDIATION.md) | §24, §25 — P0–P4 actions, and what not to build |
| 16 | [`16_PILOT_READINESS.md`](16_PILOT_READINESS.md) | §26 — 0–5 scores with evidence |
| 17 | [`17_INFORMATION_REQUIRED_FROM_AGENCY.md`](17_INFORMATION_REQUIRED_FROM_AGENCY.md) | §28 — the questionnaire, groups A–T |
| 18 | [`18_DECISION_REGISTER.md`](18_DECISION_REGISTER.md) | decisions that must precede implementation |
| 19 | [`19_OPEN_QUESTIONS.md`](19_OPEN_QUESTIONS.md) | unknowns |
| 20 | [`20_EXECUTIVE_SUMMARY.md`](20_EXECUTIVE_SUMMARY.md) | §31 — the 24 final answers |

## 4. Three things this audit found that a reader should not miss

1. 🔴 **A runnable integrity gate is red on `master`.** `01_Sector/contracts/sector_truth_gate.py` fails 2 checks (a duplicated `v0.3` changelog entry and a header/changelog mismatch in `SECTOR_OS_ARCHITECTURE.md`), introduced by commit `7d341f5` (2026-10-03) and pushed by auto-sync without the gate being run. `READINESS_ASSESSMENT_2026-10-02.md` §2.2 records the same gate passing earlier that day. → `HV-01`.
2. 🔴 **The agency's root documents and its public website still say the real sector is B2B SaaS — "only", on the website — while every live artefact is Hospitality.** The pivot was recorded on 2026-08-19 (`01_Sector/FIELD_POPULATION_PLAN.md:28`, `:196`) and the 2026-10-06 company profile states it correctly, but `GLOBAL_OS.md:24`, `01_Sector/SECTOR_OS.md` §1 and `arika-website/src/app/industry-solutions/page.tsx:24` were never reconciled. → `HV-02`.
3. 🟠 **Hospitality as the protocol describes it — a multi-revenue-centre commercial ecosystem with B2C, B2B and intermediary pathways and a Pre-Experience methodology — is mostly absent.** "Pre-experience", "tennis", "B2B2C", "B2C2B", "B2C2C" and "revenue centre" each return **zero** matches in the repository. What exists is excellent but narrow: an *Accommodation* sector plugin and a *rooms-revenue* direct-booking offer, both modelling the agency's own sale to hotels far better than the hotel's sale to its guests. → file 03 §2, file 08 §1.

## 5. Proposed log entries — for the owner to apply (not applied here)

The protocol forbids modifying existing files during the audit, which overrides `CLAUDE.md`'s instruction to log meaningful work. These are drafted for the owner to apply, edit or reject:

- **`GLOBAL_OS.md` §10** — *"2026-10-07 — Hospitality vertical forensic audit filed at `00_Agency_Governance/enterprise_architecture/HOSPITALITY_VERTICAL_AUDIT_2026-10-07/` (20 files, audit-only, nothing modified). Headline findings: Sector truth gate red on master since `7d341f5` (HV-01); root/website still declare B2B SaaS as the sole real sector (HV-02); the Hospitality plugin and offer model the agency's sale to hotels well and the hotel's sale to guests weakly (two market planes, file 08). Pilot readiness 1.9 / 5. Decisions HD-01–HD-19 await the owner; the next phase proposed is H0 — integrity and definition (file 20, answer 24)."*
- **`01_Sector/SECTOR_OS.md` §8** — the gate failure (HV-01) and the DB 16 audience-relation finding (HV-17), each pointing to file 14.
- **`00_Agency_Governance/OWNER_INPUT_NEEDED.md`** — re-issue the decisions in file 18 as tracker items; correct rows 60 (entity — incorporated 2026-10-06), 72 and 74 (superseded by the 2026-10-02 / 2026-10-03 group reconciliation and the prospecting run). See `HV-07`.
