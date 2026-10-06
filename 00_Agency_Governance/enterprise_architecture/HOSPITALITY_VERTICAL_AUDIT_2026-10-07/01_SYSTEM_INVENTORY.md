# 01 — System Inventory

**Protocol §2:** *"Before evaluating Hospitality, map the existing Agency OS… Do not judge the architecture yet. First reconstruct it."*
This file reconstructs. Judgement starts in file 02.

---

## 1. The repository at a glance

| Measure | Value | Test used |
|---|---|---|
| Non-dependency files | **1,013** | `find` excluding `node_modules`, `.git`, `dist`, `__pycache__`, `.next` |
| Commits | **263** · HEAD `48cdb74` (2026-10-06 23:32 +0300) | `git log` |
| Top-level areas | Root entry points · `00_Agency_Governance` · **21 department folders (01–21)** · `arika-runtime/` · `.claude/` · `_archive/` · `Other Source Reference/` | `ls` |
| Agent specs | **115** in `.claude/agents/` across 20 departments | `ls .claude/agents/*.md` |
| Skills | **14** in `.claude/skills/` (10 Sector, 4 Experience Engineering) | `ls .claude/skills/` |
| Runnable gates | 5 (`sector_truth_gate.py`, `skill_run_gate.py`, `p2_coverage_gate.py`, `estate_event_gate.py`, `intake_gate.py`) | file listing |
| Test suites | 10 files across Sector, Governance, Sales, runtime, Finance, Design | file listing |
| Raw draft archive | ~350 `Draft N.md` files, mostly AI-chat brainstorm exports | `GLOBAL_OS.md` §2.3, §9 |
| Operating reality | Incorporated 2026-10-06 (Arika Growth Limited, PVT-PQ1EWEKM); solo owner; **0 clients, 0 delivered engagements, 0 revenue** | `ARIKA_GROWTH_COMPANY_PROFILE.md` §14 |
| Auto-sync | A Claude Code `Stop` hook **commits and pushes every change to GitHub** at the end of every turn | `.claude/hooks/README.md`, `.claude/settings.local.json` |

## 2. Root and governance layer

| Artefact | What it is | State |
|---|---|---|
| `CLAUDE.md`, `AGENTS.md` | Thin pointers into `GLOBAL_OS.md` (Claude / platform-neutral) | `BUILT` |
| `GLOBAL_OS.md` (v0.29.3, 308 lines / 165 KB) | The single root: identity, department map, flow, registry pattern, changelog, open gaps | `BUILT`; changelog entries average ~3 KB each |
| `REGISTRY_TAXONOMY_REFERENCE.md` | The 41-registry future-state ontology; 11 active as department sections | `DESIGNED` (reference only) |
| `agency_intelligence_extractor.py`, `agency_workspace_completion_engine.py` | Pre-restructure extraction scripts with hard-coded paths and a phantom "Legal Drafts" workspace | **Orphaned** — `GLOBAL_OS.md` §11 says "need a rewrite before being re-run"; `AEIT_04` C6 calls them dead |
| `00_Agency_Governance/AGENCY_OPERATING_CONSTITUTION.md` | Non-negotiables, decision rights, **Risk Class 0–4**, amendment process | `BUILT` — still headed `v0.1-draft`, last updated 2026-06-30 |
| `AGENCY_RACI.md` | Cross-department RACI | `BUILT` 2026-06-30; **no rows for Sector intelligence, Design (19), Experience Engineering (20) or Presence (21)** |
| `AGENCY_KPI_DICTIONARY.md` | 17 agency-wide metrics with formulas | `BUILT`; every threshold `(unset)` by owner decision |
| `CRM_SCHEMA.md` (v0.2.1) | Company/Org-level, Lead, Opportunity, Client, Engagement/Project, **Pilot Engagement**, Invoice, Partner | Core five `LIVE` in ClickUp since 2026-07-01; Company + Pilot Engagement `DESIGNED` (*"not yet confirmed live"*, line 159) |
| `AUTOMATION_APPROVAL_MATRIX.md` (v0.4) | Trigger → action → risk class → rollback → fallback → human gate | 2 real rows (Creative Pipeline routine; CRM provisioner) against **30 declared schedule triggers** |
| `AGENCY_VISION.md`, `AGENCY_REVENUE_TARGETS.md` | 10-layer vision, 15-step closed loop, $1M/month target, the **7 Cognitive Calendars** | `BUILT` (doctrine) |
| `AGENCY_COMMERCIAL_DOCTRINE.md` | Worldview, five commercial movements, voice, Presence Economics | `BUILT` (doctrine) |
| `ARIKA_GROWTH_COMPANY_PROFILE.md` (2026-10-06) | Master brief for Design/Marketing/Sales; Part B internal guardrails incl. a can/cannot-claim table | `BUILT` — **the most current outward-facing source of truth** |
| `CLIENT_INTAKE_PROFILE.md` + `intake/intake_gate.py` | Universal stage-gated question bank S1–S5 + runnable lint/template/answers/scan gate | Profile `v0.1-draft`, **unratified (item 73)**; gate `BUILT` |
| `OWNER_INPUT_NEEDED.md` (171 KB) | The live decision/owner-action queue | Header "Last updated **2026-09-21**"; one 2026-10-03 note added; rows 60/72/74 not reconciled (see `HV-07`) |
| `OWNER_DECISION_WORKSHEET.md` | Former action surface | **Frozen at 2026-06-30**, honestly marked so (2026-09-13 banner) |
| `GO_LIVE_CHECKLIST.md` | 58 numbered setup items in 11 phases | `BUILT`; a working task list |
| `crm_provisioning/` | Governed ClickUp field provisioner + spec + **authorisation register** + audit record | `LIVE` once (CRM-PROV-1, 2026-09-29) |
| `offline_guard/` | Python + Node guard that blocks network in fixture runs; 46 tests | `BUILT`, tests pass (2026-10-03 record) |
| `enterprise_architecture/` | `AEIT_00`–`AEIT_11`, estate audit + register + gate, PIL integration report, **readiness assessment** | `BUILT` (blueprints + measurements) |

## 3. Department inventory

Agents = count in `.claude/agents/`. Mechanism % = `READINESS_ASSESSMENT_2026-10-02.md` §3 (refreshed 2026-10-03), quoted, not re-measured.

| # | Department | OS file | Agents | Skills / code | Live stores (last verified) | Mechanism % | Hospitality role today |
|---|---|---|---|---|---|---|---|
| 00 | Governance | — (governance layer) | — | gates, provisioner, offline guard | — | 77.5 | CRM entity model, intake, approvals |
| 01 | **Sector** | `SECTOR_OS.md` (266 KB) + architecture, activation contract/protocol, Notion schema, calendar intelligence, write contract, skill matrix | 5 | **10 skills**, 3 gates, contracts, offline Offer-inbox receiver | **16 Notion DBs** — DB 3 217 findings · DB 7 34 signals · DB 9 4 · DB 10 57 · DB 11 13 · DB 14 33 · DB 15 5 · DB 16 3 (dates 2026-08-24 → 2026-10-02) | 82.5 | **Home of the vertical** — Sector Plugin #001 |
| 02 | **Offer** | `OFFER_OS.md` (140 KB) + Draft 41 + worksheet + readiness packet + intake overlay | 3 | — | Offer Registry (markdown); Content DB 8 mirror | 92.5 | **Hospitality Revenue Content OS** (registry #13 candidate, unpriced) |
| 03 | Marketing | `MARKETING_OS.md` + `Elite_Marketing_Agentic_OS/` (19 files) | 9 | — | **none** (no Notion store — item 31k) | 39.0 | None specific; owns measurement truth and holds no performance store |
| 04 | Content | `CONTENT_OS.md` + `CONTENT_INTELLIGENCE_SCHEMA.md` + `PLATFORM_INTELLIGENCE_REGISTRY.md` | 6 | — | **8 Notion DBs** (built 2026-08-16); 3 Accommodation opportunities + one campaign/brief chain recorded 2026-08-19 | 39.0 | Three OTA-tax content opportunities aimed at hotel buyers |
| 05 | Sales | `SALES_OS.md` + `06_AI_OPERATIONS/` + `PROSPECTING_CYCLE.md` | 10 | `prospecting/prospecting_cycle.py` + 8 tests | Zoho mailbox drafts (outside Git) | 60.0 | **Live prospecting run `PROSPECT-H-20261003-01`** |
| 06 | ClientPartner Acquisition | `CLIENTPARTNER_OS.md` + constitution | 7 | — | ClickUp Partner list | 39.0 | None specific (intermediaries not modelled) |
| 07 | Client Success | `CLIENTSUCCESS_OS.md` | 6 | — | ClickUp Client list | 39.0 | None specific |
| 08 | Operations | `OPERATIONS_OS.md` + constitution | 8 | — | ClickUp Project list | 39.0 | 7 Cognitive Calendars (agency); capacity flagged as unmodelled |
| 09 | Finance | `FINANCE_OS.md` + `finos-plugin/` (TypeScript, Postgres schema, Zoho connector) | 7 | 8 tests | Zoho Books org (trial **expired** at 2026-07-15 check) | 52.5 | None (hospitality unpriced) |
| 10 | Legal | `LEGAL_OS.md` + 7 unreviewed templates + counsel packets | 2 | `build_counsel_package.py` | — | 39.0 | Gates every client-data step; nothing reviewed by counsel |
| 11 | HR / People Ops | `HR_OS.md` + `PEOPLE_DOCTRINE.md` | 4 | — | — | 39.0 | Capacity doctrine (solo + AI) |
| 12 | Branding | `BRANDING_OS.md` + `bois/` (Python) | 3 | BOIS engine | BOIS memory (writes client workspaces **inside the repo**) | 77.5 | None |
| 13 | Tech Stack | `TECHSTACK_OS.md` | 3 | — | Inventory (markdown) | 57.5 | Verify-don't-assume pattern for client tools |
| 14 | Audits & Diagnostics | `AUDITS_DIAGNOSTICS_OS.md` | 6 | — | — | 39.0 | Gateway pattern; **cannot scope a hotel audit** (A001 AG-14) |
| 15 | Consulting & Advisory | `CONSULTING_ADVISORY_OS.md` | 3 | — | — | 39.0 | None |
| 16 | Automation | `AUTOMATION_OS.md` | 4 | — | 1 cloud routine (Creative Pipeline) | 50.0 | Approval gate for nurture/reporting automations |
| 17 | AI Enablement | `AI_ENABLEMENT_OS.md` | 4 | — | — | 39.0 | Governance gate blocked by design |
| 18 | Cross-Domain Synthesis | — (reference archive) | — | — | — | excluded | None |
| 19 | Design | `DESIGN_OS.md` + language system + `design-plugin/` (KIE client) | 6 | 15 tests | Canva root "Arika Agency" + 8 folders | 50.0 | Production engine a Pre-Experience build would use |
| 20 | Experience Engineering | `EXPERIENCE_ENGINEERING_OS.md` + spec system + `arika-website/` (Next.js) | 11 | **4 skills** | Vercel deployment | 39.0 | Owns the public website (still SaaS-only) |
| 21 | Presence | `PRESENCE_OS.md` + LinkedIn OS + launch content + platform tracker | 8 | — | LinkedIn profile + Company Page; Postiz (recorded `LIVE` 2026-08-07, 0 channels) | 39.0 | None; **0 hospitality mentions** in LinkedIn files |

## 4. Runtime, code and data infrastructure

| Component | What it does | State (test) |
|---|---|---|
| `arika-runtime/` (TypeScript) | One canonical agent spec + one executor; triggers `manual · schedule · event · webhook · join`; Constitution risk model in `governance.ts`; JSONL memory writer; TEST_FIXTURE lane | `BUILT`; **71/71 tests pass (run 2026-10-06)**; `LIVE` for manual Offer runs (5 records, 2026-09-13) |
| Runtime approval behaviour | A run ends `awaiting_review` or `advisory_complete` (`executor.ts:150`); non-manual triggers on gated specs are refused before any model call (`executor.ts:61`); gated runs advertise no events | `BUILT`, test-verified (`tests/approval-dispatch.test.mjs`) |
| Event bus | `emits` declared 200 times; **`executor.ts` never publishes** | `estate_event_gate.py` PASS 2026-10-06 (71 `CONNECTED` edges, 123 `DESIGNED`, 9 producer-unassigned) |
| `finos-plugin/` | Ledger, cash flow, treasury, profitability, risk engines; Postgres schema incl. `clients` and **`approvals`** tables; Zoho Books connector | `BUILT`; 8 tests pass (2026-10-03 record) |
| `bois/` | Branding retrieval/grading/governance/synthesis engine | `BUILT`; no assertion-bearing suite |
| `design-plugin/` | KIE.ai client (nano-banana-pro image, seedance video) | `BUILT`; 15 mocked tests pass |
| `arika-website/` | Next.js site (16 pages) | `BUILT`; on a `.vercel.app` subdomain; apex DNS unresolved (`PROSPECTING_CYCLE.md`, 2026-10-03) |
| `05_Sales/prospecting/prospecting_cycle.py` | Validates public evidence, the org tree and contact provenance; writes an ID-only queue outside Git | `LIVE` once (2026-10-03); **8/8 tests pass (run 2026-10-06)** |
| `01_Sector/delivery/offer_inbox_receiver.py` | Offline Sector → Offer packet receiver with its own authorisation file | `BUILT`; 72 tests (2026-10-03 record) |

**Memory / execution streams that actually exist** (the repository's only proof of what ran):

| Stream | Lines |
|---|---|
| `01_Sector/_memory/skill_runs.jsonl` · `skill_runs-sandbox.jsonl` | 15 · 2 |
| `02_Offer/_memory/runtime.jsonl` · `sandbox.jsonl` · `sandbox-offer-f2.jsonl` · `sandbox-offer-f3.jsonl` | 5 · 1 · 1 · 1 |
| `12_Branding/_memory/runtime.jsonl` | 7 |
| `13_Tech_Stack/_memory/runtime.jsonl` | 2 |
| `19_Design/_memory/runtime.jsonl` | 1 |
| `05_Sales/06_AI_OPERATIONS/06_AI_Memory_Logs/runtime.jsonl` | 3 |

No memory stream exists for Marketing (03), Content (04), Client Success (07), Operations (08) or Presence (21). **None of their agents has ever run.**

## 5. The protocol's §2 checklist, answered

| Asked for | Exists? | Where | Reality state |
|---|---|---|---|
| directories / modules | Yes | 21 department folders = "Plugin = Department" model (`GLOBAL_OS.md` §7) | `BUILT` |
| applications / services | Partly | `arika-runtime`, `finos-plugin`, `bois`, `design-plugin`, `arika-website` | `BUILT`; only the website is externally reachable |
| schemas | Yes | `CRM_SCHEMA.md`, `SECTOR_NOTION_SCHEMA.md`, `CONTENT_INTELLIGENCE_SCHEMA.md`, `contracts/*.json`, `finos` SQL, `spec-schema.ts` | `BUILT` |
| databases | Yes, external | Notion (Sector 16 + Content 8), ClickUp (5 lists), Zoho Books; finos Postgres **schema only** | Notion/ClickUp `LIVE`; Postgres **UNKNOWN** — no evidence a database instance runs |
| configuration | Yes | `.mcp.json`, `.claude/settings.local.json`, `plugin.config.json`, `.env` files (not read) | `BUILT` |
| documentation | Extensive | every `{DEPT}_OS.md`; 41 registry concepts | `BUILT` |
| workflows | Yes, mostly manual | department §4 Workflow Indexes; Sector skills | see file 05 |
| automation | Minimal | 1 cloud routine; 30 declared-not-scheduled triggers | scheduler **not approved** |
| APIs | Partial | runtime webhook server; finos HTTP/MCP layer; no client-facing API | `BUILT`, not deployed |
| dashboards | **No** | dashboard spine is `GLOBAL_OS.md` §11 item 9, "not started"; Sector Control Tower is a specified Notion view | `DESIGNED` |
| UI components | Website only | `arika-website/src/components/` | `BUILT` |
| ticketing / project management | **No ticket entity**; registers + ClickUp `Project` pipeline | file 13 | partial |
| client management / CRM | Yes | ClickUp lists + `CRM_SCHEMA.md` | `LIVE` (empty of real clients) |
| prospecting / sales | Yes | Sector DB 4/5 (empty by design), scorecard agent, prospecting cycle, Sales agents | prospecting `LIVE` once |
| marketing operations | Doctrine + 9 agents, no store | `MARKETING_OS.md` | agents never run |
| revenue operations | Doctrine + `sales-revenue-operations` agent | `05_Sales` | never run |
| strategy | Yes | Vision, Commercial Doctrine, OEOS per offer, AEIT roadmap | `BUILT` |
| campaign systems | Schema only | Content DB 4 Campaign Intelligence | `BUILT` store, one recorded row |
| calendars | Yes, layered | file 06 | DB 7 `LIVE`; 7 Cognitive Calendars agent never run |
| reporting / analytics | **No** | KPI dictionary formulas only; no BI connected (`OPERATIONS_OS.md` §12a) | `DESIGNED` |
| permissions / roles | Partial | risk classes; `.claude/settings.local.json` tool allow-list; no user-role model (solo owner) | — |
| governance | Strong | file 02 §3, file 12, file 13 | `BUILT`, partly `LIVE` |
| templates | Yes | 7 legal templates (unreviewed), intake template, agent runtime template | `BUILT` |
| prompts | Yes | agent bodies; `20_Experience_Engineering/PROMPTING_SYSTEM.md`; BOIS prompts | `BUILT` |
| AI components | Yes | 115 agents, 14 skills, generation integrations | file 12 |
| integrations | Mostly unconnected | ClickUp (live), Notion (live), Zoho (lapsed plan), Canva/OpenArt/Relume (**unauthenticated** at 2026-07-15 check; Canva and OpenArt also listed as needing authorisation in this session) | mixed |
| notification systems | **No** | — | `UNASSIGNED` |
| task systems | Markdown registers | file 13 | — |
| knowledge systems | Yes | Sector Notion DBs, BOIS knowledge graph (5.3 MB), memory files, changelogs | `LIVE` (Sector) |
| sector-specific components | **Yes — Hospitality only** | §6 below | — |

## 6. Hospitality-specific artefacts — complete list

| Artefact | Owner | Purpose | State |
|---|---|---|---|
| `01_Sector/sector_plugins/hospitality/HOSPITALITY_PLUGIN.md` (v0.3) | Sector (01) | Sector Plugin #001 — 14 slots (ontology, archetype × signal rules, demand model, geography, destination themes, signal weights, timing offsets, sources, audience/DMs, linguistics, offer ladder, content pillars, seasonality, KPI semantics) | `BUILT`; P3 demand-pattern layer and P12 pillar set ⬜ unauthored |
| `…/hospitality/plugin.config.json` | Sector (01) | Machine-readable sidecar (P2, P5, P6, P7, P13) — ratified as a compiled projection (31c) | `BUILT`; read by `p2_coverage_gate.py` |
| `01_Sector/A001_*.md` (6 files) | Sector (01) | A001 — a **fictional** 9-unit hotel group used to test intake/fit/governance mechanisms (D1–D21; D20 = mechanism evidence only) | Document-only pilot **closed** 2026-09-16; one fixture run spent 2026-09-21 |
| **SYNCO-01** (+ property `SYNCO-01-P01`, + `SYNCO-02` delivery control) | Sector (01) | A second, separate **synthetic company fixture** built from a supplied simulated hospitality fact sheet; the P01 property schema (unit categories, venues, wellness, club window) approved 2026-09-29 with invented values. Records held in a private sandbox outside Git; the repository carries the fixture ID only | **Normalisation / mechanism evidence only** (D20 extended); no external use authorised (`SECTOR_OS.md` §8, 2026-09-29) |
| `01_Sector/CALENDAR_INTELLIGENCE.md` | Sector (01) | Live calendar spec — sources, feeds, origin ⇄ destination doctrine, timing rules | `BUILT`; ICS subscriptions and demand-surge rule `DESIGNED` |
| `02_Offer/OEOS - Hospitality Division … Draft 41.md` | Offer (02) | Structural (non-pricing) OEOS for the Hospitality Revenue Content OS | Working Hypothesis / Not Quotable; Phase 11 **BLOCKED** |
| `02_Offer/Hospitality Revenue Content OS - Delivery Capacity and Cost Model Worksheet.md` | Offer (02) | MVP scope (M1–M7), audit data set (MD1–MD8), capacity (one H1/H2 client), hours bands | Owner decisions recorded 2026-09-13/14 |
| `02_Offer/… Full Push Readiness Packet.md` | Offer (02) | Manual Sector → Offer → downstream push on one real property (OI1–OI9, RD1–RD7, PG0–PG5) | **NOT READY** — 0 of 5 required gates passed |
| `02_Offer/… Pilot Intake Overlay.md` | Offer (02) | 37 `H-` intake questions on top of the universal core | `v0.1-draft`, owner review required |
| `05_Sales/PROSPECTING_CYCLE.md` + `prospecting/` | Sales (05) | Public-company research and first-touch preparation | Run 2026-10-03: 4 companies, 23 org levels, 3 drafts, **0 sent** |
| Sector Notion rows for Accommodation | Sector (01) | 4 DB 3 findings · DB 6 language map · 4 DB 9 roles · 4 DB 10 titles · DB 7 seasonal rows · 3 DB 16 destinations · 5 DB 15 routes · DB 12/13 rows | `LIVE` (last verified 2026-08-24 → 2026-10-02) |
| Content Notion rows | Content (04) | 3 Accommodation opportunities; one "Own Your Guest" campaign; first DB 3/6/7 chain | recorded 2026-08-19; not re-verified |
| CRM additions for Hospitality | Governance (00) | `Company` structure (`SGL/MBR/GRP/HLD/OUT`), parent/child levels, `Pilot Engagement`, `ORG-/PER-/PILOT-/SIM-` namespaces | `DESIGNED` (2026-10-02/03) — lists not verified live |
| Agent extensions | Sector/Sales | `sector-icp-fit`, `sector-signal-scorer`, `sales-lead-qualification` given Hospitality routes (`hospitality_group/property/outlet_discovery`) | `BUILT` 2026-10-03; **never run on a real prospect** |

## 7. Concept presence scan — what the protocol names that the repository does not

Whole-repository search (ripgrep, excluding `node_modules`, `_archive`, `__pycache__`), 2026-10-06.

| Concept from the protocol | Matches | Reading |
|---|---|---|
| pre-experience / pre experience | **0** | Absent |
| tennis (corporate tennis prototype) | **0** | Absent |
| B2B2C · B2C2B · B2C2C | **0** | Absent |
| revenue centre / revenue center | **0** | Absent |
| food and beverage (spelled out) | 0 (`F&B` appears in 7 files) | Fragmentary |
| faceless | 1 — unrelated ("faceless corporations", a Marketing raw draft) | Absent |
| wedding / honeymoon | 5 files each | P5 demand-theme vocabulary + intake H-C05 only |
| MICE | many | Real signal type (`Sales/MICE`), demand theme, CRM outlet level |
| day pass | 0 | Absent |
| diaspora | 1 | Absent in practice |
| travel agent / tour operator | 1 each | Intake question H-B05 only |
| wedding planner / event planner | 0 | Absent |
| source market / origin market | 6 / 14 files | **Present and modelled** (DB 15, `Signal Role`, P7) |
| synthetic person / people | 4 / 1 files | Fixture language (SYNCO, A001), not an AI-media policy |
| deepfake | 0 | Absent |

**Conclusion of the scan (`CONFIRMED`):** the repository's hospitality knowledge is concentrated in *accommodation economics* (OTA leakage, direct booking, seasonality, destinations, origin markets) and the agency's *sale* into that market. The experiential, multi-revenue-centre and intermediary-network dimensions the protocol describes have no footprint.
