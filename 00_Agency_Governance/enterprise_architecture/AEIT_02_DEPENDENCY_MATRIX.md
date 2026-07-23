# AEIT_02 — Enterprise Dependency Matrix (Analysis)

**Version:** v0.1
**Last updated:** 2026-07-22
**Owner:** Mary Thuo (Agency Governance, 00)
**Fills:** `REGISTRY_TAXONOMY_REFERENCE.md` future-state registry **Dependency** (not previously built).
**Sources:** `GLOBAL_OS.md` §5 (operating flow), agent frontmatter (`emits`/`handoff_to`),
`CRM_SCHEMA.md` (Handoff Points), department `{DEPT}_OS.md` §12.

> Purpose: make dependencies explicit so we can see circular, hidden, and broken ones. Every node
> has a named owning department (verification gate #2). Nothing here is invented — each edge traces
> to an `emits`/`handoff_to` declaration, a CRM handoff row, or the §5 flow.

---

## 1. Primary revenue flow (the spine)

```
Sector(01) → Offer(02) → Marketing(03)/Content(04) → Sales(05) → Client Success(07)
          → Operations(08) → Finance(09) → Governance(00)
```

| System | Depends on (upstream) | Consumes | Produces | Consumed by (downstream) | Owner |
|---|---|---|---|---|---|
| Sector (01) | Tech Stack tools, source data | market/xlsx data | `PROSPECT_SCORED`, `ICP_CLASSIFIED`, `SECTOR_MAPPED`, `SECTOR_READINESS_SET` | Sales (05), Marketing (03), Offer (02) | Mary Thuo |
| Offer (02) | Sector maps | `SECTOR_MAPPED` | engineered offers, Offer Engineering Registry | Marketing (03), Sales (05) | Mary Thuo |
| Marketing (03) | Sector, Offer | `SECTOR_*`, offers | demand, qualified opportunities (Lead→Opportunity) | Sales (05) | Mary Thuo |
| Content (04) | Marketing, Branding, Design | briefs, narrative | content assets, Lead touch history | Marketing (03), Sales (05) | Mary Thuo |
| Sales (05) | Sector scores, Marketing/CP opportunities | `ICP_CLASSIFIED`, `PROSPECT_SCORED`, Lead | closed deals (Opportunity→Client) | Client Success (07), Finance (09) | Mary Thuo |
| Client Success (07) | Sales | closed Client | onboarding scope, `lifecycle_stage`, `relationship_status` | Operations (08), Sales (05, expansion) | Mary Thuo |
| Operations (08) | Client Success | scoped engagement | delivered work, billable events | Finance (09) | Mary Thuo |
| Finance (09) | Operations | billable events | invoices, revenue, forecasts | Governance (00) | Mary Thuo |
| Governance (00) | all | reports, KPIs | Constitution, RACI, Approval Matrix, CRM schema | all (governs) | Mary Thuo |

## 2. Horizontal / support layers

| System | Depends on | Produces | Consumed by | Owner |
|---|---|---|---|---|
| Branding (12) | Sector truth | brand identity, voice, Brand Genome | Content (04), Design (19), Experience Eng (20), Marketing (03) | Mary Thuo |
| Design (19) | Branding, Content briefs, **OpenArt/KIE credits** | creative assets | Content (04), Marketing (03), Experience Eng (20) | Mary Thuo |
| Experience Eng (20) | Design assets, Spec System, tech stack | interactive experiences | Marketing (03), Offer (02, future) | Mary Thuo |
| ClientPartner Acq (06) | Sector, partner ecosystem | partner-sourced opportunities | Sales (05) | Mary Thuo |
| Audits & Diagnostics (14) | Sector, owning-dept standards | audit reports (Gateway Offer) | Sales (05), delivery offers | Mary Thuo |
| Consulting & Advisory (15) | every offer's output; **the Owner** | advisory decisions | client; routes execution to owning dept | Mary Thuo |
| Automation (16) | arika-runtime, Approval Matrix | client automations; **agency automation governance/monitoring** | all departments | Mary Thuo |
| AI Enablement (17) | **Legal (10) review** (blocked), readiness data | roadmap, governance framework | Automation (16), client | Mary Thuo |
| Finance (09) plugin | Zoho Books, exchange-rate API | ledger, cashflow | Governance (00) | Mary Thuo |
| Legal (10) | **external counsel (not engaged/awaited)** | contracts, compliance | all client-facing depts | Mary Thuo |
| HR (11) | revenue signal | people doctrine, hiring trigger | Owner | Mary Thuo |
| Tech Stack (13) | vendors, `ANTHROPIC_API_KEY` | tool inventory + verification | all departments | Mary Thuo |

## 3. Infrastructure substrate (everything depends on these)

| Substrate | What depends on it | State |
|---|---|---|
| **`arika-runtime` (OrchOS)** | all 106 agents, all triggers | Built; **never run persistently** |
| **`ANTHROPIC_API_KEY`** | all 93 `prompt` agents | **Unset** — the whole agent layer is inert (`TECHSTACK_OS.md:173`) |
| **ClickUp CRM** | Sales, Client Success, Operations, Finance | Live (free tier) — the one verified piece of infra |
| **Zoho** (email + Books) | Finance, all outbound comms | Load-bearing; **Books trial expired**; missing from DPA register |
| **Governance (Constitution + Approval Matrix)** | every automation, every Class 3+ action | Structure closed; owner-data pending |

---

## 4. Critical / hidden / broken dependencies (the point of this document)

- **🔴 The whole graph is inert on one unset key.** Every downstream capability that relies on an
  agent depends transitively on `ANTHROPIC_API_KEY`, which is set nowhere (`TECHSTACK_OS.md:173`).
  This is the single largest hidden dependency: the architecture *looks* connected but cannot
  execute. → `AEIT_10` sequences activation first.
- **🔴 Broken dependency — AI Enablement (17) → Legal (10).** AI Enablement's Class-3 governance
  gate requires a legal-reviewed framework, but Legal has no engaged counsel and the agency does not
  legally exist. The dependency is *declared and unsatisfiable* — blocked by design
  (`GLOBAL_OS.md` §4, dept 17).
- **🔴 Disconnected "hybrid automation" halves.** The runtime's 21 schedule triggers live in a
  process that never runs; the one cloud routine that *does* run is a bespoke prompt not generated
  from any spec (`AUTOMATION_OS.md:178`). The two halves of the intended hybrid model are not
  wired to each other.
- **🟠 Governance-coverage gap.** ~21+ armed automations depend on the Approval Matrix for a
  trigger/action/risk-class/rollback/human-gate row; the matrix has **1 real row**
  (`AUTOMATION_OS.md:164`). Activation without closing this is a governance breach waiting on a
  single command.
- **🟠 Resource-exhaustion dependency.** Design (19) production depends on OpenArt/KIE credits with
  **~2 images of runway** agency-wide; Experience Engineering (20) depends transitively on Design.
- **🟡 Ownership-contradiction dependency.** Sales (05) qualification depends on an `ICP_fit_score`
  the CRM schema says Sales owns (`CRM_SCHEMA.md:23`), while Sector (01) actually produces the ICP
  classification (`SECTOR_OS.md:90,162`). The edge exists but its ownership is contested → resolved
  in `AEIT_05`.

**No true circular dependencies were found** in the revenue spine — the flow is acyclic. The
pathologies are *broken* and *hidden* dependencies, not cycles. That is a good structural sign.

---

## 5. Decision Log
- **2026-07-22 — Dependency matrix built.** Confirmed acyclic revenue spine; surfaced 3 broken/
  hidden infra dependencies (API key, Legal gate, hybrid disconnect). — Claude Code (Opus 4.8)

## 6. Changelog
- **v0.1 (2026-07-22):** Created. — Claude Code (Opus 4.8)
