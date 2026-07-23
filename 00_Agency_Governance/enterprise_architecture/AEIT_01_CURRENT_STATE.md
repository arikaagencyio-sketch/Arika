# AEIT_01 — Enterprise Current-State Map (Discovery)

**Version:** v0.1
**Last updated:** 2026-07-22
**Owner:** Mary Thuo (Agency Governance, 00)
**Status:** Discovery consolidation. Sources: `GLOBAL_OS.md`, `REGISTRY_TAXONOMY_REFERENCE.md`,
`00_Agency_Governance/*`, all 20 `{DEPT}_OS.md`, `.claude/agents/*`, `arika-runtime/`, and the
AEIT three-agent audit (2026-07-22).

> Purpose: one honest picture of where the agency actually is, so Analysis (Stage 2) and the IntOS
> blueprint (Stage 4) start from reality, not from the aspirational directive.

---

## 1. The one-paragraph truth

Arika Agency is a **20-department, 106-agent, 4-code-plugin, heavily-governed enterprise
architecture** expressed almost entirely in markdown, sitting on top of a **solo-operator,
0-client, $0-revenue, not-yet-legally-incorporated** business. The documentation discipline is
genuinely high (self-auditing changelogs, honest 🔴 flags, supersession chains). The **built
*process* is far heavier than the operational *reality* warrants** — and the automation layer that
would make the architecture "run" **has never run on a schedule and cannot run at all today**
(no `ANTHROPIC_API_KEY` is set). This gap is the central fact Phase Zero must design around.

---

## 2. Department map (21 slots, 20 active OS files)

| # | Department | OS file | Maturity |
|---|---|---|---|
| 00 | Agency Governance | — *(governance layer, no OS file)* | Backbone — see §3 |
| 01 | Sector | `01_Sector/SECTOR_OS.md` | Developed (owns market "truth", ICP, 90-pt scorecard) |
| 02 | Offer | `02_Offer/OFFER_OS.md` | Developed (Offer Engineering Registry = index of record) |
| 03 | Marketing | `03_Marketing/MARKETING_OS.md` | Largest by file count (~140), OS thin |
| 04 | Content | `04_Content/CONTENT_OS.md` | Developed |
| 05 | Sales | `05_Sales/SALES_OS.md` | Reference-maturity pattern (has `06_AI_OPERATIONS/`) |
| 06 | ClientPartner Acquisition | `06_ClientPartner_Acquisition/CLIENTPARTNER_OS.md` | Developed |
| 07 | Client Success | `07_Client_Success/CLIENTSUCCESS_OS.md` | Developed (lifecycle states) |
| 08 | Operations | `08_Operations/OPERATIONS_OS.md` | Thin (confirmed no raw source) |
| 09 | Finance | `09_Finance/FINANCE_OS.md` | Thin OS + `finos-plugin` (code) |
| 10 | Legal | `10_Legal/LEGAL_OS.md` | Drafts only — 🔴 nothing lawyer-reviewed |
| 11 | HR / People Ops | `11_HR_People_Ops/HR_OS.md` | Doctrine (solo+AI), not staffing |
| 12 | Branding | `12_Branding/BRANDING_OS.md` | Developed + `bois` (Python RAG scaffold) |
| 13 | Tech Stack | `13_Tech_Stack/TECHSTACK_OS.md` | Developed inventory; several §7/§10/§11 placeholders |
| 14 | Audits & Diagnostics | `14_Audits_Diagnostics/AUDITS_DIAGNOSTICS_OS.md` | Agents wired, never delivered |
| 15 | Consulting & Advisory | `15_Consulting_Advisory/CONSULTING_ADVISORY_OS.md` | Agents deliberately don't do core work (owner is advisor) |
| 16 | Automation | `16_Automation/AUTOMATION_OS.md` | Developed; owns automation governance/monitoring |
| 17 | AI Enablement | `17_AI_Enablement/AI_ENABLEMENT_OS.md` | Class-3 gate blocked by design (Legal absent) |
| 18 | Cross-Domain Synthesis | — *(reference archive)* | Inactive; likely origin doc for restructuring |
| 19 | Design | `19_Design/DESIGN_OS.md` | Live agent roster + `design-plugin` (code) |
| 20 | Experience Engineering | `20_Experience_Engineering/EXPERIENCE_ENGINEERING_OS.md` | Developed; codified Spec System + 4 skills |

All owners are the placeholder **Mary Thuo**. Numbering encodes the operating flow (§5 of `GLOBAL_OS.md`).

---

## 3. The four "foundational platforms" — reality mapping

The directive proposes four foundational platforms: EGOS (governance), IntOS (intelligence),
OrchOS (orchestration), RevOS (revenue). **Three already exist in substantial form under other
names; only IntOS is genuinely absent.** None are branded as "the four platforms."

| Proposed platform | Reality | Where it lives |
|---|---|---|
| **EGOS** (Enterprise Governance) | **Exists, unbranded** | `00_Agency_Governance/`: `AGENCY_OPERATING_CONSTITUTION.md`, `AGENCY_RACI.md`, `AGENCY_KPI_DICTIONARY.md`, `CRM_SCHEMA.md`, `AUTOMATION_APPROVAL_MATRIX.md`, `AGENCY_VISION.md`, `AGENCY_REVENUE_TARGETS.md`, `GO_LIVE_CHECKLIST.md`, `OWNER_INPUT_NEEDED.md` + `arika-runtime/src/governance.ts` (risk-class engine). No `{DEPT}_OS.md`. |
| **OrchOS** (Orchestration) | **Exists, unbranded** | `arika-runtime/`: `executor.ts`, `agent-registry.ts`, `triggers/`, `governance.ts`, `memory-writer.ts`, `spec-schema.ts`, `wrappers/` — the actual execution layer for all 106 agents across manual/cron/event/webhook triggers. |
| **RevOS** (Revenue) | **Exists, diffuse** | `05_Sales/Master_Revenue_Commercial_Operating_System_Blueprint.md`, `02_Offer/`, `09_Finance/`, `00_Agency_Governance/AGENCY_REVENUE_TARGETS.md`. No single consolidating platform/department. |
| **IntOS** (Intelligence) | **ABSENT** | No Intelligence department, no Intelligence OS. "Intelligence" exists only as a cross-cutting theme (Sector/Sales/Marketing/Brand) and a layer in the 10-layer vision. Closest analogues: `01_Sector` (upstream market intelligence), `12_Branding/bois/` (a local RAG/knowledge-graph scaffold). |

**Implication:** Phase Zero should *name and map* the target four-platform framing (in `AEIT_10`)
but must not rename or re-fold the existing governance/runtime work — that would be churn without
value. The real build is IntOS.

**Addendum (2026-07-23) — the outbound counterpart.** The four-platform directive has no platform
for the agency's *outward* market presence (`agency → world`). That gap was filled after Phase Zero
by the **Presence department (21)** (`21_Presence/PRESENCE_OS.md`), framed as the **outbound mirror
of IntOS** and governed by `00_Agency_Governance/AGENCY_COMMERCIAL_DOCTRINE.md`. It is a department,
**not** a fifth *branded* platform — formal platform-spec formalization stays deferred to Phase E
per `AEIT_00` §6. Recorded here so the reality mapping acknowledges the outbound direction.

---

## 4. What exists vs. what is genuinely missing

Authoritative sources for this split: `REGISTRY_TAXONOMY_REFERENCE.md` (active vs future-state) and
`GLOBAL_OS.md` §11 (Open Gaps).

### Already built — do NOT propose rebuilding
| Artifact | Location |
|---|---|
| Operating Constitution, RACI, KPI Dictionary | `00_Agency_Governance/AGENCY_*` |
| **Canonical CRM schema** (Lead/Opportunity/Client/Project/Invoice/Partner) — live in ClickUp | `00_Agency_Governance/CRM_SCHEMA.md` |
| Automation Approval Matrix (structure) | `00_Agency_Governance/AUTOMATION_APPROVAL_MATRIX.md` |
| **7 Cognitive Calendars** (Revenue, Pipeline, Operational, Cash Flow, Capacity, Opportunity, Strategic) | `AGENCY_REVENUE_TARGETS.md` + `operations-calendar-orchestrator` |
| **41-registry taxonomy** (11 active, embedded per-department) | `REGISTRY_TAXONOMY_REFERENCE.md` |
| Rigid **16-section department template** | every `{DEPT}_OS.md` |
| **106 agents + 4 skills + 4 code plugins** | `.claude/agents/*`, `.claude/skills/*`, `finos-plugin`, `bois`, `design-plugin`, `arika-runtime` |
| Agent-level I/O contracts (`inputs`, `output_schema`, `emits`, `handoff_to`) | agent frontmatter |
| Department-local capability registries | each `{DEPT}_OS.md` §3 |
| Client/Partner lifecycle **enums** | `CRM_SCHEMA.md` |

### Genuinely missing / partial — the real Phase Zero build targets
| Gap | Status | Named where | AEIT artifact |
|---|---|---|---|
| Intelligence Operating System | **Absent** | — (10-layer vision only) | `AEIT_07` |
| Canonical entity model / ontology beyond CRM's 6 objects | **Partial** | Future-state: Semantic/Ontology | `AEIT_06` |
| Knowledge graph / entity relationship graph | **Missing** | Future-state: Relationship (entity graph) | `AEIT_06` |
| Agency Global Source Registry | **Open** | `GLOBAL_OS.md` §11 item 1 | `AEIT_08` |
| Dependency graph / matrix | **Missing (formal)** | Future-state: Dependency | `AEIT_02` |
| Agency-wide capability-map rollup | **Partial** | `GLOBAL_OS.md` §6 ("none yet") | `AEIT_03` |
| Unified state machine | **Partial** | Future-state: State | `AEIT_05` |
| Cross-department handoff/interface contracts | **Partially open** | `GLOBAL_OS.md` §11 item 6 | `AEIT_09` |
| Unified memory protocol | **Partially open** | `GLOBAL_OS.md` §11 item 8 | `AEIT_07` |
| Dashboard spine | **Open** | `GLOBAL_OS.md` §11 item 9 | sequenced in `AEIT_10` |

---

## 5. The architecture-vs-reality gap (headline)

The single most important current-state fact, quantified:

- **Business reality:** headcount 1 (solo, AI-assisted); 0 employees / 0 contractors / 0 payroll;
  0 clients; $0 revenue; target $1M/month ($35K/day). The agency **does not legally exist yet**
  (`[ARIKA LEGAL ENTITY]` is a placeholder in every contract template; counsel instructed
  2026-07-19, reply awaited).
- **Automation reality:** the entire agent layer is **unrunnable today** — `ANTHROPIC_API_KEY` is
  not set, and 93 of 106 agents are `prompt` agents that depend on Claude. **28 scheduled cron
  triggers have never fired** (no daemon; crons only register while `npm start` holds a foreground
  terminal, which has never been left running). The one automation that ever fired (2026-07-04)
  auto-disabled 3h41m later and went **unnoticed for 11 days**.
- **Infrastructure reality:** the one piece of real, verified infrastructure is the **ClickUp CRM**
  (free tier, built). Email/invoicing = **Zoho** (Books Premium trial expired; M365 rejected on
  cost). No calendar or transcription tool registered despite an offer selling a weekly advisory
  cadence.

**Consequence for the plan:** IntOS cannot be *activated* on top of an automation layer that has
never run. Therefore Phase Zero designs IntOS but the roadmap (`AEIT_10`) gates its build behind
activation (API key + a proven scheduled run) and behind legal existence — the reconcile-first
posture the Owner selected.

---

## 6. What is strong and should be preserved

The audit is not a teardown. These are genuine strengths to build on, not replace:

1. **Template governance is excellent** — all 20 OS files hold the identical 16-section spine;
   someone enforces it. Divergence is in depth, not structure.
2. **The registry pattern is sound** — embedding registries as department sections (not 41 top-level
   folders) is the right call for this scale, and `REGISTRY_TAXONOMY_REFERENCE.md` already documents
   the promotion rule.
3. **Honesty is built in** — changelogs self-report failures (dead crons, false inventory rows,
   the 11-day outage), which is exactly what makes reconciliation tractable.
4. **The CRM schema already solved the duplication problem once** — it exists precisely because
   "each department's raw drafts independently reinvented a slightly different model." AEIT extends
   that same discipline to the rest of the enterprise.

---

## 7. Decision Log

- **2026-07-22 — Current-state consolidated.** Confirmed EGOS/OrchOS/RevOS exist unbranded, IntOS
  absent; confirmed the architecture-vs-reality gap as the governing constraint for sequencing.
  — Claude Code (Opus 4.8)

## 8. Changelog

- **v0.1 (2026-07-22):** Current-state map created. — Claude Code (Opus 4.8)
