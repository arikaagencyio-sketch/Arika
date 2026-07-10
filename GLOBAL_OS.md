# Global Operating System — Arika Agency

**Version:** v0.7.2
**Last updated:** 2026-07-09
**Status:** Structural skeleton + core governance closed (constitution, RACI, KPI dictionary, CRM schema, automation approval matrix). Content migration complete for all 9 departments with real raw material; 4 departments confirmed to have none. Cross-department reconciliation pass underway. Real sector confirmed (B2B SaaS) — see §9 and `01_Sector/SECTOR_OS.md`. **New department added 2026-07-01: Design (19)** — the agency's creative production studio, seeded from an owner planning session on brand kit/creative infrastructure (see §4, §10). **New department added 2026-07-03: Experience Engineering (20)** — the agency's interactive/experiential production discipline (scrollytelling, motion- and 3D-native digital experiences), downstream of Design, seeded from an owner-relayed external AI session (see §4, §5, §10). **2026-07-04: Design and Experience Engineering both got real, invokable agent rosters** (6 and 11 Claude Code subagents respectively, see §7, §10) — the first departments in this repo with a live agent layer rather than a proposed-only roster. **2026-07-09: Experience Engineering (20) gained a codified, runnable spec discipline** — the six-station Experience Spec System (`20_Experience_Engineering/EXPERIENCE_SPEC_SYSTEM.md`) + four reference docs (`build-system/`) + four real Claude Code skills (`.claude/skills/`), aligned from the owner's "Design Department" plugin and homed in Experience Engineering (not Design 19) because it governs interactive *web builds*, not asset production. Remaining work is owner-input (`00_Agency_Governance/OWNER_INPUT_NEEDED.md`), not more reading.

---

## 1. Identity

This repository is **Arika Agency's** own command center — the operating system the agency runs itself on, and the pattern it can extend to run client businesses. It is not a deliverable; it is the agency's internal nervous system: strategy, governance, knowledge, and (progressively) the agents/workflows that execute daily operations.

**Vision (confirmed real, 2026-06-30):** *"Arika Agency is a 360° Cognitive Revenue Operating System that transforms businesses into self-orchestrating revenue engines by integrating sales, marketing, branding, acquisition, automation, operations, and financial intelligence into a unified system that manages revenue probability under time, capital, and opportunity constraints to produce predictable, scalable, and compounding growth."*

More plainly: the agency exists to become a fully integrated Revenue Intelligence and Execution System that designs, builds, and operates the entire growth infrastructure of B2B and complex B2C companies — where revenue is engineered through systems, not generated through services. Businesses don't "hire the agency"; they plug into a revenue operating system that behaves like an extension of their own business brain. **Full 10-layer architecture (Strategic, Revenue, Acquisition, Sales, Marketing, Branding, Operations, Automation, Intelligence, Financial Orchestration), the closed-loop system logic, and the 5 foundational realities of business/project management: `00_Agency_Governance/AGENCY_VISION.md`.**

**Real operating target (confirmed, 2026-06-30):** $1,000,000/month, $35,000/day — non-negotiable. Full deal-count logic and the 7-calendar cognitive operating system: `00_Agency_Governance/AGENCY_REVENUE_TARGETS.md`.

Real sector confirmed 2026-06-30 (B2B SaaS, see `01_Sector/SECTOR_OS.md` §1).

**What this repo is NOT:** a client deliverable, a finished strategy document, or a fully built automation platform. As of v0.1 it is the *structure* the agency's real source-of-truth content gets poured into — deliberately built before that content, per the agency's own stated principle of "preparing the room before adding the source of truth."

---

## 2. How to Use This Repo

This section is the anti-hallucination contract. Any reader — human or AI agent, on any platform — should follow this order:

1. **Read this file (`GLOBAL_OS.md`) first.** It is the single global root. `CLAUDE.md` and `AGENTS.md` are thin pointers into this file — they carry no independent authority.
2. **Read the relevant department's `{DEPT}_OS.md`** for the department your task touches (see Department Index, §4). Each department file is the local source of truth for that department's capabilities, workflows, agents, KPIs, decisions, and risks.
3. **Only then consult the raw archive** (the loose `Draft N.md` files still living in each department folder) — and only via the specific pointers the department's `{DEPT}_OS.md` gives you. Do not free-associate across the 350+ raw drafts directly; they are unedited, unstructured brainstorm exports and have not been verified, deduplicated, or fact-checked against real agency data.
4. **When you complete meaningful work**, log it in the relevant department's Decision Log or Changelog (§15 of the department template) rather than only stating it in conversation — this is how the system avoids re-deriving or contradicting itself across sessions.
5. **If something is missing or contradictory**, flag it rather than guessing. Open Gaps are tracked explicitly in §11 below and per-department.

This applies identically whether you are a human, Claude Code, Claude Chat/Projects, a Claude Code worker, or another agent platform (e.g. Codex via `AGENTS.md`).

---

## 3. Operating Constitution (Summary)

Full version: `00_Agency_Governance/AGENCY_OPERATING_CONSTITUTION.md` (written 2026-06-30 — process/structure sections are load-bearing; mission/objectives content remains placeholder pending owner input).

The load-bearing rules, compressed from the full constitution:

- **No silent invention.** When source material is missing, say so — don't fabricate agency-specific facts (numbers, client names, pricing, legal terms).
- **Department ownership is local; the constitution is supreme.** Each department's `{DEPT}_OS.md` is authoritative for that department, but cannot override the constitution.
- **Structure before content.** Registries may exist as empty/placeholder structure without being a failure — but may not be filled with guessed values to look complete.
- **Every significant decision is logged**, not just stated in conversation.
- **Human sign-off required** for Risk Class 3+ actions (anything touching real client commitments, contracts, money movement, or public-facing claims) — see the full 5-tier risk classification in the constitution §5, and the expanded `00_Agency_Governance/AUTOMATION_APPROVAL_MATRIX.md` for how this applies to automations specifically.

---

## 4. Department Index / Map

| # | Department | Path | Mandate | Owner | OS File |
|---|---|---|---|---|---|
| 00 | Agency Governance | `00_Agency_Governance/` | Cross-cutting governance, prior gap-analysis archive | Mary Thuo | — *(governance layer, no department OS file; see §11)* |
| 01 | Sector | `01_Sector/` | Upstream market/industry intelligence — determines "truth" the rest of the agency packages and sells | Mary Thuo | [`01_Sector/SECTOR_OS.md`](01_Sector/SECTOR_OS.md) |
| 02 | Offer | `02_Offer/` | Offer design, packaging, pricing architecture | Mary Thuo | [`02_Offer/OFFER_OS.md`](02_Offer/OFFER_OS.md) |
| 03 | Marketing | `03_Marketing/` | Positioning, campaign strategy, channel strategy, demand generation | Mary Thuo | [`03_Marketing/MARKETING_OS.md`](03_Marketing/MARKETING_OS.md) |
| 04 | Content | `04_Content/` | Content strategy, creation, narrative/messaging architecture, channel-specific execution | Mary Thuo | [`04_Content/CONTENT_OS.md`](04_Content/CONTENT_OS.md) |
| 05 | Sales | `05_Sales/` | Pipeline, conversion, deal execution | Mary Thuo | [`05_Sales/SALES_OS.md`](05_Sales/SALES_OS.md) |
| 06 | ClientPartner Acquisition | `06_ClientPartner_Acquisition/` | Referral/partner-channel client acquisition (distinct from direct Sales) | Mary Thuo | [`06_ClientPartner_Acquisition/CLIENTPARTNER_OS.md`](06_ClientPartner_Acquisition/CLIENTPARTNER_OS.md) |
| 07 | Client Success | `07_Client_Success/` | Post-sale client lifecycle: onboarding, journey, retention, health | Mary Thuo | [`07_Client_Success/CLIENTSUCCESS_OS.md`](07_Client_Success/CLIENTSUCCESS_OS.md) |
| 08 | Operations | `08_Operations/` | Delivery execution, SOPs, capacity, quality control *(new department — confirmed gap)* | Mary Thuo | [`08_Operations/OPERATIONS_OS.md`](08_Operations/OPERATIONS_OS.md) |
| 09 | Finance | `09_Finance/` | Accounting, cash flow, treasury, forecasting | Mary Thuo | [`09_Finance/FINANCE_OS.md`](09_Finance/FINANCE_OS.md) |
| 10 | Legal | `10_Legal/` | Contracts, compliance, IP, risk *(new department — confirmed gap, was a phantom workspace in the old completion engine)* | Mary Thuo | [`10_Legal/LEGAL_OS.md`](10_Legal/LEGAL_OS.md) |
| 11 | HR / People Ops | `11_HR_People_Ops/` | Hiring, onboarding (internal), capacity/utilization *(new department — confirmed gap)* | Mary Thuo | [`11_HR_People_Ops/HR_OS.md`](11_HR_People_Ops/HR_OS.md) |
| 12 | Branding | `12_Branding/` | Brand architecture, narrative, identity systems | Mary Thuo | [`12_Branding/BRANDING_OS.md`](12_Branding/BRANDING_OS.md) |
| 13 | Tech Stack | `13_Tech_Stack/` | Tooling/software inventory used across the agency *(new department — confirmed gap)* | Mary Thuo | [`13_Tech_Stack/TECHSTACK_OS.md`](13_Tech_Stack/TECHSTACK_OS.md) |
| 14 | Audits & Diagnostics | `14_Audits_Diagnostics/` | The agency's Gateway Offer (Revenue Infrastructure Audit) and future diagnostic products *(new department, 2026-06-30 — promoted from an Offer-catalog division)* | Mary Thuo | [`14_Audits_Diagnostics/AUDITS_DIAGNOSTICS_OS.md`](14_Audits_Diagnostics/AUDITS_DIAGNOSTICS_OS.md) |
| 15 | Consulting & Advisory | `15_Consulting_Advisory/` | Executive advisory offer (Revenue Growth Advisory) — the agency's Embedded-Partnership-stage layer *(new department, 2026-06-30 — promoted from an Offer-catalog division)* | Mary Thuo | [`15_Consulting_Advisory/CONSULTING_ADVISORY_OS.md`](15_Consulting_Advisory/CONSULTING_ADVISORY_OS.md) |
| 16 | Automation | `16_Automation/` | AI workflow and business-operating-system offers, plus the agency's own internal automation *(new department, 2026-06-30 — promoted from an Offer-catalog division)* | Mary Thuo | [`16_Automation/AUTOMATION_OS.md`](16_Automation/AUTOMATION_OS.md) |
| 17 | AI Enablement | `17_AI_Enablement/` | Organization-wide AI transformation, readiness, and governance offer *(new department, 2026-06-30 — promoted from an Offer-catalog division)* | Mary Thuo | [`17_AI_Enablement/AI_ENABLEMENT_OS.md`](17_AI_Enablement/AI_ENABLEMENT_OS.md) |
| 18 | Cross-Domain Synthesis | `18_Cross_Domain_Synthesis/` | NOT an active department — early whole-agency synthesis draft, kept as historical/reference material (likely origin document for this restructuring; see `AgencyOs Cognitive Framework. Draft 1.md`) | — | — *(reference archive, no OS file)* |
| 19 | Design | `19_Design/` | Creative asset production — asset library, AI production engine, and Canva as the creative-assembly layer — for the agency's own content/campaigns first, and as a future client/sector design service *(new department, 2026-07-01 — confirmed gap, not a promotion from an Offer-catalog division)* | Mary Thuo | [`19_Design/DESIGN_OS.md`](19_Design/DESIGN_OS.md) |
| 20 | Experience Engineering | `20_Experience_Engineering/` | Interactive/experiential production — scrollytelling, motion- and 3D-native digital experiences (websites, presentations, product launches, interactive reports) — downstream of Design (19), for Arika's own flagship builds first, and as a future client offer *(new department, 2026-07-03 — seeded from an owner-relayed external AI session, not a promotion from an Offer-catalog division)* | Mary Thuo | [`20_Experience_Engineering/EXPERIENCE_ENGINEERING_OS.md`](20_Experience_Engineering/EXPERIENCE_ENGINEERING_OS.md) |

Numbering encodes the agency's own previously-documented operating flow (see §5) directly into the filesystem.

**Correction (2026-06-30):** Content was initially merged into Marketing as a subfolder (`360_Agency_Content/`) during the first restructuring pass. Per explicit owner feedback, it was always meant to be a full standalone department, not a Marketing sub-area — it has now been restored as department 04, and every department from Sales onward was renumbered up by one to make room (Sales 04→05, ClientPartner Acquisition 05→06, Client Success 06→07, Operations 07→08, Finance 08→09, Legal 09→10, HR/People Ops 10→11, Branding 11→12, Tech Stack 12→13, Cross-Domain Synthesis 13→14).

**Expansion (2026-06-30):** 4 new departments (Audits & Diagnostics, Consulting & Advisory, Automation, AI Enablement) were added at 14-17, promoted from divisions inside the Offer (02) catalog's master pricing document (`Agency Pricing Architure. Draft 28.md`) once their founding offers existed in enough depth to justify dedicated ownership. Per owner direction, this was a selective promotion, not automatic — Draft 28 named 7 divisions total; only these 4 lacked any existing departmental home (Sales, Marketing, and Partner & Client Acquisition already had one). Cross-Domain Synthesis moved from 14→18 to make room. The Offer (02) department's Offer Engineering Registry (`02_Offer/OFFER_OS.md` §3) remains the index of record for every offer's pricing/engineering detail — these new departments own *delivery*, not the registry itself.

---

## 5. Cross-Department Operating Flow

Primary flow (inherited from the agency's own prior self-analysis in `00_Agency_Governance/_archive_2026-06-03_completion_index/00_MASTER_ARCHITECTURAL_COMPLETION_INDEX.md`):

```
Sector → Offer → Marketing/Content → Sales → Client Success → Operations → Finance → (Management/Governance)
```

Support layers running horizontally across all of the above: **Branding** (supports Marketing, Content, Sales, Client Success, Governance), **Design** (added 2026-07-01 — the production studio that converts Branding's identity and Content's briefs into finished creative assets; supports Content, Marketing, and eventually every department needing visual production), **Experience Engineering** (added 2026-07-03 — sits downstream of Design (19), converting curated assets and motion primitives into finished interactive experiences — websites, presentations, product launches, interactive reports; feeds Marketing (03)'s distribution and, once packaged, Offer (02)'s future catalog; its "Design the Spec" front-half is codified as the Experience Spec System, added 2026-07-09), **ClientPartner Acquisition** (feeds Sales and distribution, parallel to Marketing/Content-driven demand), **Legal**, **HR/People Ops**, **Tech Stack**, and **Agency Governance** (governs all layers).

**Offer-type departments (added 2026-06-30):** **Audits & Diagnostics** sits upstream of Sales as the agency's Gateway Offer — often the actual first client touchpoint, feeding qualified, diagnosed prospects into Sales or directly into an implementation offer. **Automation** and **AI Enablement** are a sequenced pair (AI Enablement sells the organization-wide roadmap/governance; Automation builds the specific workflows that roadmap commissions) sitting alongside Operations as execution-layer capability. **Consulting & Advisory** sits at the top of the ascension path, downstream of every other offer, as the Embedded-Partnership-stage layer.

**Worked example — new client onboarding** (illustrative; workflow not yet built):
1. Marketing or ClientPartner Acquisition generates a qualified opportunity → handoff to `05_Sales/`
2. Sales closes the deal → handoff to `07_Client_Success/` for onboarding
3. Client Success defines scope/expectations → handoff to `08_Operations/` for delivery
4. Operations executes → generates billable events → handoff to `09_Finance/`
5. Finance invoices and tracks revenue → reports roll up to Agency Governance

**Worked example — new capability/offer launch**:
1. `01_Sector/` identifies a market opportunity
2. `02_Offer/` packages it into a sellable offer with pricing
3. `03_Marketing/` and `04_Content/` build demand-generation content for it
4. `05_Sales/` and `06_ClientPartner_Acquisition/` sell it

Neither workflow is implemented as an executable automation yet — both are documented here as the intended shape, to be built out in each department's Workflow Index (§4 of the department template).

---

## 6. Curated Registry Index

Rather than maintaining 41 separate top-level registries (see `REGISTRY_TAXONOMY_REFERENCE.md` for the full future-state ontology), this v0.1 skeleton embeds a curated subset of the most operationally load-bearing registries as **standard sections inside every department's `{DEPT}_OS.md`**:

| Registry | Lives as department section | Cross-department rollup |
|---|---|---|
| Capability | §3 Capability Registry | *(none yet — would live in Agency Governance)* |
| Workflow | §4 Workflow Index | *(none yet)* |
| Agent | §5 Agent Roster | *(none yet)* |
| Skill | §6 Skill Library Index | *(none yet)* |
| KPI/Metrics | §7 KPI Dictionary (department-local) | *(none yet — agency-wide KPI dictionary is an open gap, §11)* |
| Decision | §8 Decision Log | *(none yet)* |
| Risk/Incident | §9 Risk/Incident Log | *(none yet)* |
| Standards | §10 Standards & SOPs Index | *(none yet)* |
| Governance/RACI | §11 RACI/Ownership | *(none yet — agency-wide RACI is an open gap, §11 below)* |
| Trigger/Automation | §12 Triggers/Automation Hooks | *(none yet)* |
| Knowledge | §14 Raw Archive Pointer | *(none yet)* |

A department-local registry section being empty/placeholder is expected at v0.1 — it means "structure exists, content pending," not "doesn't apply." Cross-department rollups (a true agency-wide Capability Registry, KPI Dictionary, etc.) are listed as open gaps in §11 and are deliberately deferred until department-local content is real.

---

## 7. Command Center Overview

The agency operates on a **Plugin = Department** model: each department is treated as a self-contained capability module with its own identity, knowledge base, tools, workflows, memory, communication protocols, permissions, and triggers — conceptually equivalent to a traditional business department, but built to be operated by AI agents as much as by people.

Concrete agents, skills, and workflows are NOT all built today — they are built progressively, per department, as real operational need and real source content justify them. Two departments already have a head start, built independently before this restructuring:

- **Sales** (`05_Sales/06_AI_OPERATIONS/`) — the most mature example in the repo: system prompts, an Agent Registry, a Skill Library, a Task Routing Matrix, Escalation Rules, AI Memory Logs (Decision/Learning/Prompt-Evolution), and Runtime Examples, with source-paragraph citation lineage back to the raw drafts. **This is the reference pattern** other departments should normalize toward as they mature.
- **Marketing** (`03_Marketing/Elite_Marketing_Agentic_OS/`) — a markdown-only agent-card catalog: master architecture doc, an agent catalog YAML, 11 individual Agent Cards, skill/workflow rulebooks, and a 30/60/90 rollout plan.

Finance (`09_Finance/finos-plugin/`) and Branding (`12_Branding/bois/`) each built code-based scaffolds instead of markdown. **Decision (2026-06-30):** both are retained as grandfathered code-backed exceptions to the markdown-first standard rather than converted or deleted — see each department's own `{DEPT}_OS.md` §13 for the full rationale. The markdown-first standard governs new department capability going forward; it does not mandate retroactively gutting working code.

**A third pattern, added 2026-07-04: real, invokable Claude Code subagents.** Design (19) and Experience Engineering (20) are the first departments with a live agent layer built as actual `.claude/agents/*.md` subagent files (callable directly via the Agent tool) rather than markdown-only proposed contracts or a separate code scaffold — 6 subagents for Design, 11 for Experience Engineering (reconciled from that department's own two source-draft rosters, then individually refined against 11 further owner-relayed AI sessions, one per role — full audit trail in `20_Experience_Engineering/EXPERIENCE_ENGINEERING_VISION.md` §5). This is a fourth agent-layer pattern alongside Sales' markdown+citations, Marketing's markdown agent-card catalog, and Finance/Branding's grandfathered code scaffolds — not a replacement for any of them, and not yet declared the new standard other departments must adopt.

---

## 8. Platform Entry Points

- **`/CLAUDE.md`** — thin pointer for Claude Code. Points here, then to department OS files. No department logic lives in it.
- **`/AGENTS.md`** — thin pointer for other agent platforms (Codex and similar conventions). Same content as `CLAUDE.md`, platform-neutral wording.
- Either file could be deleted without breaking navigation — `GLOBAL_OS.md` is the real root, not a Claude-specific artifact. This is the concrete realization of the agency's platform-neutrality requirement: the system must work from Claude Chat, Claude Code, Claude Code workers, or any other LLM agent that can read markdown.

---

## 9. Raw Archive & Content Migration Status

**As of v0.3, content migration is complete for every department that has real raw content.** Sector (01), Offer (02), Marketing (03), Content (04), Sales (05), ClientPartner Acquisition (06), Client Success (07), Finance (09), and Branding (12) — 9 of 12 departments — have each had their raw drafts (and, for Finance/Branding, their grandfathered code layers) read in full or substantially sampled, with real findings distilled into their `{DEPT}_OS.md` registries. Operations (08), Legal (10), HR/People Ops (11), and Tech Stack (13) were confirmed to have **no raw content at all** — their skeletons are accurate as-is, not pending migration.

Raw "Draft N.md" files remain in place at each migrated department's folder root (not deleted or moved) — the OS files now summarize and cite them rather than replacing them. They're conceptually rich but largely generic (agency-relevant theory, not filled-in agency-specific numbers/clients/pricing); migration consistently found **zero real client names, pricing, or measured KPI data anywhere in the entire repo**. Two departments (Finance, Branding) also had grandfathered code scaffolds that turned out more functionally real than the original skeleton pass assumed — both corrected with explicit before/after notes in their own OS files (see `09_Finance/FINANCE_OS.md` §13, `12_Branding/BRANDING_OS.md` §13).

Each department also retains its pre-existing `00_Workspace_Intelligence_Inventory/` subfolder (auto-generated by a prior pass — see `agency_workspace_completion_engine.py` at repo root); these were read as part of each department's migration where present, not left as unused backlog.

**Cross-department reconciliation pass: complete (2026-06-30).** The scope-blur issues flagged during migration — ClientPartner Acquisition / Sales / Marketing boundary, Client Success's pre-sale-qualification/Sales boundary, Client Success/Operations delivery handoff, and Client Success's 3-way lifecycle-model conflict — were all resolved by direct comparative analysis once every relevant department was migrated. None of them turned out to need a real fact from the owner; they needed full-repo context, which now exists. See each affected department's §1/§3/§4/§8/§10 and `00_Agency_Governance/OWNER_INPUT_NEEDED.md`'s Resolved table for the reasoning behind each call.

**What's still open**: every remaining item in `00_Agency_Governance/OWNER_INPUT_NEEDED.md` is a genuine "needs a real fact from the owner" gap — no more reading or reconciling will close them.

---

## 10. Versioning / Changelog

Simple convention: bump the version header (§ top of this file) on structural changes (new departments, renamed registries, changed flow). Log entries below, newest first.

### Changelog

- **2026-07-09 — v0.7.2-experience-spec-system** — Aligned the owner's "Design Department" plugin + "Elite Web Build" reference set into the repo as **Experience Engineering (20)'s codified spec discipline**. **Placement was an owner decision** (explicit choice among 3 options): homed in Experience Engineering (20), *not* Design (19) — despite the plugin's "Design" name, its stack (Next.js/Tailwind/GSAP/ScrollTrigger/Lenis/Spline) is line-for-line identical to `EXPERIENCE_TECH_STACK.md` and its output is an interactive-website build prompt, squarely EE (20)'s mandate; Design (19) owns asset/media production, a different thing. **Scope was an owner decision**: full wiring. Built `20_Experience_Engineering/EXPERIENCE_SPEC_SYSTEM.md` (a six-station brief→build-ready-spec assembly line whose stations map onto EE's existing 11 agents — no new roles), four reference docs under `20_Experience_Engineering/build-system/` (elite-web-build-system, vision-to-build-pipeline, workflow-run-sheet, discoverability-architecture), and four real skills under `.claude/skills/` (`creative-direction`, `sitemap-and-refs`, `design-tokens`, `design-audit`) — EE's first real skill layer. Hardened the plugin's Language Systems into seven checkable **design laws** and added a previously-unowned **Discoverability & Architecture** pillar (SEO/AEO/GEO), both in `EXPERIENCE_ENGINEERING_OS.md` §10. Deliberately did **not** copy the plugin's bundled standalone `CLAUDE.md` — a second root-authority file would violate §2's one-root rule; its rules were distilled into the spec-system doc and skills instead. Registered 8 tools in `13_Tech_Stack/TECHSTACK_OS.md` §3 (Next.js/Tailwind in real use; Whimsical connection-unverified; TanStack Query/Formspree/Sanity/Plausible-GA/Search Console named-not-connected). New tracker items: `OWNER_INPUT_NEEDED.md` item 56, `GO_LIVE_CHECKLIST.md` Phase 10. Added a small cross-ref note to `19_Design/DESIGN_OS.md` §1 so the "Design" naming collision can't confuse future readers. — Claude Code (Opus 4.8)
- **2026-07-04 — v0.7.1-real-agent-rosters** — Design (19) and Experience Engineering (20) both went from proposed-only agent rosters to real, invokable Claude Code subagents (`.claude/agents/design-*.md` — 6 roles; `.claude/agents/experience-engineering-*.md` — 11 roles), per direct owner decision. Experience Engineering's roster was first reconciled from the department's own two non-identical source-draft rosters (10-role and 12-role) into one canonical 11-role roster, then each role was individually refined against a further owner-relayed "Sider Fusion" AI session — every session was checked for runtime mismatches (several proposed standalone Python apps, live 3D/game engines wired to Unity/Unreal, or robotics motion-planning systems incompatible with this repo's actual Claude-Code-subagent architecture) and department-scope collisions (a Brand Strategist session would have duplicated Branding (12)'s mandate and its existing 19-agent BOIS system; a Copywriter session partially overlapped Offer (02) and Branding (12)) before anything was adopted — full audit trail in `20_Experience_Engineering/EXPERIENCE_ENGINEERING_VISION.md` §5. Design's 6-role roster was built directly from that department's own existing documented capabilities, no external source material involved. Also fixed a repo-wide mislabeling found during this pass: the Storyboard Library's entry template is 9 fields, not 8 as previously written in 5 places. Closes `OWNER_INPUT_NEEDED.md` item 50 and `GO_LIVE_CHECKLIST.md` item 37. §7 updated to document this as a new, fourth agent-layer pattern alongside Sales/Marketing/Finance-Branding's existing three. — Claude Code (Sonnet 5)
- **2026-07-03 — v0.7-experience-engineering-department** — Added **Experience Engineering (20)** as a new standalone department — the agency's interactive/experiential production discipline (scrollytelling, scroll-driven storytelling, motion- and 3D-native digital experiences), positioned downstream of Design (19) the same way Design sits downstream of Branding (12). Seeded entirely from an owner-relayed external AI chat session pasted during this planning session (not sourced from this repo, not Claude's own analysis) — flagged per the same sourcing-honesty convention already used for Branding's "Brand Genome." Two structural decisions were made directly by the owner, not sourced from the paste: the department's creation/numbering (20) and its name ("Experience Engineering," chosen over 3 alternatives). Everything else — a 16-system architecture, an "AI Creative Orchestra" agent roster, a motion/3D tech stack, an Experience Pattern Library, and a new **Prompting System** (added after owner review of the first plan draft, giving the "AI generation" capability a real, ID'd/stateful structure — reference-image workflow, sequencing, and a concrete "hyper-realistic, hyper-efficient" quality bar built from Design's existing no-visible-AI-artifacts standard) — is captured as proposed/architecture-only across 5 new files in `20_Experience_Engineering/`. The source material was internally inconsistent with itself in several places (two non-identical Creative Pipeline drafts, two non-identical AI-role rosters, two non-identical narrative-arc drafts, a 9-system outline that doesn't match its own elaborated headers); every instance was preserved as-given rather than silently merged — full audit trail in `20_Experience_Engineering/EXPERIENCE_ENGINEERING_VISION.md`. Reconciled a resulting 4-way "narrative" naming collision across Content (04)'s Story Architecture, Branding (12)'s Narrative Engineering stack, and this department's two narrative-arc drafts — cross-reference notes added to all three department files. Partially informed (not fully resolved) Design (19)'s open Motion/VFX/SFX/3D-5D Tool Registry (tracker item 48) with real candidate tool names (GSAP, Three.js, Framer Motion, Blender, Spline, Rive, etc.) — registered as named-not-connected in both `19_Design/DESIGN_LANGUAGE_SYSTEM.md` §2a and `13_Tech_Stack/TECHSTACK_OS.md` §3. New tracker items added: `OWNER_INPUT_NEEDED.md` 49-53, `GO_LIVE_CHECKLIST.md` Phase 8 (items 34-40). — Claude Code (Sonnet 5)
- **2026-07-01 — v0.6-design-department** — Added **Design (19)** as a new standalone department — the agency's creative production studio (asset library, AI production engine, Canva as creative-assembly layer, plus a proposed Design Language MCP/API and a real production-skill catalog), seeded from an owner planning session covering brand-kit direction and a full creative-infrastructure vision. Numbered 19 rather than reusing 18 (`Cross-Domain Synthesis` stays untouched as an inactive reference archive) — owner-confirmed choice among 3 presented options. Cross-department updates in the same pass: closed part of Branding (12)'s long-open visual/typography/color gap (tracker item 30) with owner-supplied moodboard direction (exact hex/type specs still pending); added a Content Houses intent axis, Story Architecture, Campaign Architecture, and a target Notion content-brief schema to Content (04); added an Engagement Layer (DM/comment automation, proposed platform ManyChat) to Automation (16); registered Canva (confirmed real/connected), Notion, and ManyChat (both proposed) in Tech Stack (13); cross-linked Marketing (03)'s aspirational MCP connector blueprint to the new concrete homes. New governance tracker items added for brand-kit finalization, Notion workspace creation, social account creation, and AI image/video vendor selection — see `00_Agency_Governance/OWNER_INPUT_NEEDED.md` and `00_Agency_Governance/GO_LIVE_CHECKLIST.md`. — Claude Code (Sonnet 5)
- **2026-07-01 — v0.5-memory-feedback-cadence-layer** — Added a new **§16 "Memory / Feedback Loop / Cadence"** section to the department template, per the go-live plan in `00_Agency_Governance/GO_LIVE_CHECKLIST.md`. Applied in two tiers: **Tier 1** (Sales, Marketing, Finance, Branding — departments with a real or code-based agent roster) got the full treatment, grounded in what already exists in each (e.g. Sales' empty `06_AI_Memory_Logs/` templates, Finance's real code-enforced Liquidity Alert feedback loop, Branding's real `core/memory/store.py` JSONL event log). **Tier 2** (Offer, Content, ClientPartner Acquisition, Client Success, Tech Stack, Audits & Diagnostics, Consulting & Advisory, Automation, AI Enablement — no real agent roster yet) got a structure-only placeholder, explicitly not fabricated, per the no-silent-invention rule. **Tier 3** (Operations, Legal, HR/People Ops) was skipped — still genuine content gaps, not architecture gaps. Also confirmed the integration architecture question raised this session: ClickUp/QuickBooks connect via the existing `finos-plugin` pattern (API key → `IntegrationConnector` implementation → `IntegrationRegistry` → already-configured MCP server), not a new mechanism. — Claude Code (Sonnet 5)
- **2026-06-30 — v0.4-offer-department-expansion** — Owner reviewed the Offer Engineering Registry's 11-offer catalog and decided 4 of Draft 28's 7 "divisions" deserved real departments, since their founding offers now exist in enough depth to support dedicated ownership: **Audits & Diagnostics (14)**, **Consulting & Advisory (15)**, **Automation (16)**, **AI Enablement (17)** — all created with seeded `{DEPT}_OS.md` files referencing their source offer-engineering drafts. Sales, Marketing, and Partner & Client Acquisition (the other 3 divisions) already had departmental homes, so weren't duplicated. `Cross-Domain Synthesis` renumbered 14→18 to make room. Also resolved: the offer team-role-roster question (tracker item 39) — clarified that these labels are AI-assisted functional execution roles, not real hires, since the owner solo-orchestrates with AI assistance; real hiring decisions stay deferred to `11_HR_People_Ops/HR_OS.md` until headcount becomes real. — Claude Code (Sonnet 4.6)
- **2026-06-30 — v0.3.1** — Resolved the #0 highest-priority owner-input item: real sector confirmed (B2B SaaS, 3-tier ICP) via a real owner-curated database (`Other Source Reference/Arika_B2B_SaaS_Intelligence_Database.xlsx`) plus a partial chat transcript. **Confirmed the agency's real name: Arika Agency** — applied across this file, `CLAUDE.md`, `AGENTS.md`. Rewrote `01_Sector/SECTOR_OS.md` to incorporate the real sector decision alongside its existing conceptual-methodology content, flagging the chat-transcript portion as partial (truncated mid-paste) rather than complete. Began the cross-department reconciliation pass (4 scope-blur items resolved: ClientPartner Acquisition/Sales/Marketing boundary, Client Success's 2 boundary items + lifecycle model). — Claude Code (Sonnet 4.6)
- **2026-06-30 — v0.3-content-migrated** — Content migration pass complete, department by department, for all 9 departments with real raw material (Sector, Offer, Marketing, Content, Sales, ClientPartner Acquisition, Client Success, Finance, Branding); confirmed Operations/Legal/HR/Tech Stack have no raw content and need none. Each migration distilled real findings into that department's `{DEPT}_OS.md` registries, clearly distinguishing draft/illustrative content from corroborated/working-code content. Corrected two earlier under-assessments from the v0.1 skeleton pass: Finance's `finos-plugin` and Branding's `bois` are both more functionally real than originally characterized (most engines/modules have working logic, not stubs; both have real source-citation systems). Extended `CRM_SCHEMA.md` with a Partner object/pipeline (gap found during ClientPartner Acquisition migration). Documented, not silently resolved, several cross-department scope-blur findings (ClientPartner Acquisition/Sales/Marketing boundary; Client Success qualification/delivery boundaries) — deferred to a deliberate reconciliation pass. Built `00_Agency_Governance/OWNER_INPUT_NEEDED.md` as the single rollup tracker for every "needs a real fact from the owner" item surfaced (30 items as of this pass). — Claude Code (Sonnet 4.6)
- **2026-06-30 — v0.2-governance** — Governance-closure pass: wrote the full Agency Operating Constitution (non-negotiables, decision rights, 5-tier risk classification, amendment process), the cross-department RACI, the agency-wide KPI dictionary, the CRM schema (Lead → Opportunity → Client → Project → Invoice), and the automation approval matrix — all in `00_Agency_Governance/`. Resolved the ClientPartner Acquisition 5-file near-duplicate cluster (1 confirmed exact duplicate deleted, 3 confirmed distinct). Made and documented the finos-plugin/bois decision: both retained as grandfathered code-backed exceptions to the markdown-first standard. Pruned a stale scratchpad-script reference from `.claude/settings.local.json`. **Corrected a structural error from v0.1:** Content was originally merged into Marketing as a subfolder; restored as its own standalone department (04) per explicit owner correction, with Sales through Cross-Domain Synthesis renumbered up by one (05–14) to make room. — Claude Code (Sonnet 4.6)
- **2026-06-30 — v0.1-skeleton** — Initial restructuring: renamed 9 existing department folders to numbered names reflecting the agency's operating flow, created 4 new department folders for confirmed gaps (Operations, Legal, HR/People Ops, Tech Stack), merged `360 Agency Content` into Marketing *(corrected in v0.2 above — this was wrong)*, archived two redundant auto-generated extraction passes, deleted confirmed-dead folders (`branding-os`, orphaned empty `Marketing Drafts` nested in Sales, `__pycache__` dirs) and one confirmed exact-duplicate file. Wrote this global MD, all 12 department OS files, and platform-agnostic entry points. First git commit. — Claude Code (Sonnet 4.6)

---

## 11. Open Gaps / Known Incomplete Areas

Inherited from the agency's own prior self-analysis (`00_Agency_Governance/_archive_2026-06-03_completion_index/00_MASTER_ARCHITECTURAL_COMPLETION_INDEX.md`, "Required Agency-Wide Closure Systems"), marked against what this v0.1 pass closes vs. leaves open:

| # | System | Status after v0.2 |
|---|---|---|
| 1 | Agency Global Source Registry (source IDs, active/superseded/archive state, owners, cadence) | **Open** — structure for this would live in Agency Governance; not built |
| 2 | Agency Operating Constitution (amendment process, decision rights, risk classes) | **Closed (process/structure)** — `00_Agency_Governance/AGENCY_OPERATING_CONSTITUTION.md` written: non-negotiables, decision rights table, 5-tier risk classification, amendment process. Mission/objectives content remains placeholder pending owner input — that part stays open. |
| 3 | Cross-domain RACI | **Closed (structure)** — `00_Agency_Governance/AGENCY_RACI.md` written, covering all cross-department functions. Named owners still pending. |
| 4 | CRM schema connecting Marketing/Content → Sales → Client → Finance | **Closed (structure)** — `00_Agency_Governance/CRM_SCHEMA.md` written: Lead/Opportunity/Client/Project/Invoice objects, relationships, handoff points. Not yet implemented in any real CRM tool (a Tech Stack decision). |
| 5 | KPI dictionary (formula, source, owner, cadence, threshold) | **Closed (formulas)** — `00_Agency_Governance/AGENCY_KPI_DICTIONARY.md` written with standard acquisition/revenue/delivery formulas. Owners, cadence, and thresholds remain unset pending real agency data — that part stays open. |
| 6 | Handoff packet standards between departments | **Partially open** — §5 above sketches the flow narratively, and `CRM_SCHEMA.md`'s Handoff Points table is a seed; no formal handoff packet spec per department pair yet. |
| 7 | Automation approval matrix (trigger, action, risk class, rollback, human gate) | **Closed (structure)** — `00_Agency_Governance/AUTOMATION_APPROVAL_MATRIX.md` written with illustrative template rows across all 4 risk classes. No real automations exist yet to populate it with live rows. |
| 8 | Memory protocol (historical, operational, decision, execution, learning) | **Partially open** — Decision Log / Changelog patterns exist per department; no unified memory protocol doc |
| 9 | Dashboard spine | **Open** — not addressed in this pass |
| 10 | Versioning/change protocol | **Closed (lightweight)** — see §10 above; sufficient for current volume, may need to formalize later |

**Additional open items still outstanding:**
- Experience Engineering (20)'s 16-system architecture, AI Creative Orchestra, Motion Tech Stack, and Prompting System are proposed/architecture-only — real tool adoption, agent build-out, and a first real project are tracked in `OWNER_INPUT_NEEDED.md` items 49-53 and `GO_LIVE_CHECKLIST.md` Phase 8, not a new §11 gap-system entry.
- Department owners are all placeholders — needs real names assigned. This blocks the RACI, KPI dictionary, and automation approval matrix from being fully operational rather than structural.
- `agency_intelligence_extractor.py` and `agency_workspace_completion_engine.py` (repo root) need a rewrite before being re-run: hardcoded dates/paths, a phantom "Legal Drafts" workspace reference that predates this restructuring, and keyword/regex-only classification with no LLM involved.
- Dashboard spine (item 9 above) — not started.
- Handoff packet standards (item 6 above) — only a seed exists in `CRM_SCHEMA.md`.

**Every item above that needs a real fact from the agency owner (not more reading/writing) is tracked in one place: `00_Agency_Governance/OWNER_INPUT_NEEDED.md`.** As each department's content-migration pass surfaces a new "needs real data" item, it gets added there rather than left buried in that department's own OS file — review that tracker in one sitting once migration is further along, rather than hunting through every department.

**As of 2026-06-30, that tracker is at 0 open decisions** — the remaining open work is build/setup, not more deciding. That sequence (ClickUp workspace setup, accounting platform decision — re-opened 2026-07-01 after Zoho CRM was superseded by ClickUp — wiring Claude into Finance's and Branding's agent rosters, first real operating cycle) is tracked in `00_Agency_Governance/GO_LIVE_CHECKLIST.md`.

**Resolved during the v0.2 governance-closure pass (no longer open):**
- Finance's `finos-plugin` (TypeScript) and Branding's `bois` (Python) — decision made and documented: both retained as grandfathered code-backed exceptions, not converted or deleted. See each department's `{DEPT}_OS.md` §13.
- The 5-file ClientPartner Acquisition near-duplicate cluster — content-diffed; 1 confirmed exact duplicate deleted, 3 confirmed genuinely distinct. See `06_ClientPartner_Acquisition/CLIENTPARTNER_OS.md` §14.
- `.claude/settings.local.json`'s stale `docx_to_md.py` scratchpad reference — pruned.
