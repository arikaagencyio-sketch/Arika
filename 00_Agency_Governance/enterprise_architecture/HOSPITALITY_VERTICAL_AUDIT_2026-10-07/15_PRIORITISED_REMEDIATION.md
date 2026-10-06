# 15 — Prioritised Remediation (P0–P4)

**Protocol §24–§25:** rank every gap; *"do not allow cosmetic improvements to outrank structural requirements"*; identify what not to build; aim for **minimum sufficient system complexity**.

**Nothing in this file has been applied.** Each action needs the owner's decision (file 18) before it is carried out — the repository's *decide ≠ apply* discipline (`AEIT_05`; memory `right-sized-architecture-preference`) and the owner's one-department-at-a-time cadence both apply.

**Rules for every action below:**
1. Every `NEW` or `EXTEND` passes the `AEIT_00` §5 Architecture Review Checklist (canonical fit · one owner · contract · dependencies · governance · reality · logged).
2. **A runnable check beats a described one** (memory `no-weak-deliverables`): where a done-test can be code, it is written as code.
3. **Effort** is relative — `S` (one sitting), `M` (a few sittings), `L` (a programme). No hours or money are implied.

---

## P0 — integrity and blocking

| RM | Action | Fixes | Class | Owner | Effort | Needs | Done-test |
|---|---|---|---|---|---|---|---|
| **RM-01** | Renumber the 2026-10-02 changelog entry in `01_Sector/SECTOR_OS_ARCHITECTURE.md` to `v0.5` and bump the header to `v0.5` | HV-01 | REFACTOR | Sector (01) | S | — (Class 1 doc edit; log it) | `python 01_Sector/contracts/sector_truth_gate.py` → exit 0 |
| **RM-02** | Make the commit path run the five gates: the `Stop` hook runs them before `git add -A` and **warns** (or **refuses to push**) on failure | HV-01 (class of defect) | GOVERNANCE (runnable) | Governance (00) / Automation (16) | S–M | **HD-14** (warn vs block; it changes hook configuration) | Deliberately break a changelog version on a scratch branch → hook reports the gate failure |
| **RM-03** | Decide the sector truth statement, then apply it to `GLOBAL_OS.md` §1, `SECTOR_OS.md` §1, the website (`industry-solutions`, `layout.tsx` meta, home), the claims policy's open item 1, and the LinkedIn plan | HV-02 | GOVERNANCE + REFACTOR | Governance (00) → Sector, EE, Presence, Legal | M | **HD-02**, **HD-03** | A runnable check added to an existing gate: public-surface files contain no "B2B SaaS only"/"ICP is B2B SaaS only" string while Hospitality is `Target` |
| **RM-04** | Decide what the Hospitality pilot *is* (level, scope, deliverables, commercial basis, capacity) and record it as one decision that supersedes items 72/74's pre-2026-10-02 framing | HV-03, HV-26 | WORKFLOW + decision | Offer (02) with Sales (05) | S (decision) | **HD-01**, **HD-04** | Tracker item exists with the decision; Draft 41 §12.5 and the worksheet §1.1 point to it |
| **RM-05** | Advance the legal chain: obtain counsel's reply on the narrowed scope; decide the s.48 posture; close RD2 storage (backup, hosting, retention); add file 12 §6's five depiction questions to the counsel brief | HV-04, HV-13 | GOVERNANCE (external) | Legal (10) / owner | external | **HD-05** | Banner on each reviewed template replaced by *"Reviewed by [name], [firm], [date]"* (`templates/README.md` rule) |

## P1 — required for the Hospitality pilot

| RM | Action | Fixes | Class | Owner | Effort | Needs | Done-test |
|---|---|---|---|---|---|---|---|
| **RM-06** | Decide where a property lives (Company, Geography place, or both), then provision `Company` and `Pilot Engagement` in ClickUp through the governed provisioner (spec + authorisation + audit) | HV-05 | EXTEND | Governance (00) | M | **HD-11** | Provisioner audit record + read-back, like `CRM-PROV-1` |
| **RM-07** | One `entity_level` enum in `CRM_SCHEMA.md`; `prospecting_cycle.py` and the intake overlay read it; Kenya scope read from plugin P4 instead of a literal; one test that fails on vocabulary drift | HV-06 | REFACTOR | Sales (05) + Governance (00) | S | — | New unit test in `test_prospecting_cycle.py` comparing `LEVELS` to the schema enum |
| **RM-08** | Re-sync `OWNER_INPUT_NEEDED.md`: close item 60 (incorporated 2026-10-06), rewrite 72/74 to the current state, add the file-18 decisions as numbered items; give the tracker an age warning like `estate_event_gate.py`'s | HV-07 | GOVERNANCE | Governance (00) | S | — | Header date ≥ newest department changelog date; age warning prints |
| **RM-09** | Confirm (or reverse) the apply-approval for the 2026-10-03 group/outlet reconciliation and record it as a dated decision | HV-46 | GOVERNANCE | owner | S | **HD-17** | Decision entry quoting the owner's instruction |
| **RM-10** | Adopt a Definition-of-Ready table in the `AEIT_06` glossary; add a `Status` select to Content DB 4 | HV-08 | GOVERNANCE + EXTEND | Governance (00) + Content (04) | S | **HD-07** | Glossary row per "ready" term with owner + exit test; DB 4 schema shows `Status` |
| **RM-11** | Client-delivery approval record: four fields on ClickUp `Project` tasks (`approved_by`, `approved_at`, `version`, `evidence_ref`) via the provisioner; a client-approver layer added to the publishing path for client work | HV-09 | EXTEND | Operations (08) + Governance (00) | S–M | **HD-06** | Provisioner read-back; one fixture task approved and read back, then deleted |
| **RM-12** | Client separation: `Client Company ID` (text) on Content DB 4 and DB 7; a `Clients/{ORG-ID}/` tier in Canva; BOIS client workspaces moved outside the repository | HV-11 | EXTEND + DATA | Content (04), Design (19), Branding (12) | M | **HD-15** | DB 4/7 schema read-back; `git ls-files 12_Branding/bois/clients 12_Branding/bois/memory/client-memory` lists no real-client workspace (only `arika-agency` and the existing sample) |
| **RM-13** | Adopt depictive-claims rules V1–V9 (file 12 §5) as a class in the claims policy; add V1/V2/V6/V7 to `design-brand-environment-consistency-checker`'s checklist | HV-13 | GOVERNANCE | Legal (10) + Design (19) | M | **HD-16**, counsel | Checker spec lists the V-rules; claims policy has the class; banner rule still applies |
| **RM-14** | Supply Phase 11 inputs (or decide the first engagement is unpaid/discovery-only); fix the pricing-floor agent spec so a non-SaaS sector **must** return `insufficient_data` unless a sector floor exists | HV-27 | DATA (human) + EXTEND | Offer (02) | M | **HD-04** | A fixture run with a hotel input returns `insufficient_data` *without* the input having to say so (Draft 41 §11.4 test) |
| **RM-15** | Consolidate real-identity maps into one location outside every Git tree and outside OneDrive; retire the Codex scratch-folder copy | HV-44 | DATA | Governance (00) | S | **HD-05** (storage half) | `prospecting_cycle.py` identity root points at the consolidated path; old path empty |
| **RM-16** | Decide gateway-audit ownership for Hospitality (by hand under Draft 41 for the MVP; extend `audits-scoping` enums later) | HV-30 | INTEGRATION (ownership) | Offer (02) / Audits (14) | S | **HD-19** | Decision entry; for the later build, `audits-scoping` accepts a hotel-audit input |
| **RM-17** | Minimum self-marketing for the pilot: reconciled website copy (after RM-03), a short LinkedIn authority series built from the three Accommodation content opportunities, and a release decision for the three drafts | HV-29 | WORKFLOW | Presence (21) · Content (04) · EE (20) · Sales (05) | M | **HD-02**, **HD-03** | Website redeployed with apex DNS resolving (`PROSPECTING_CYCLE.md` release table); Class 3 sign-off recorded per post |
| **RM-18** | Re-measure the readiness assessment's stale entries: gate count (now 4/5), D4 (largely addressed by `7d341f5`), integration ages | HV-01, HV-38 | GOVERNANCE | Governance (00) | S | — | Refreshed §2.2 / §11 rows with 2026-10 dates |
| **RM-19** | **Only if HD-10 says "proceed":** prototype prerequisites — a `SIM-H-001` decision record (field shape from SYNCO-01-P01, values invented fresh), depiction rules in force, a Plane B narrative variant, a generation-budget check | HV-15, HV-28 | GOVERNANCE + NEW | Offer (02) · Content (04) · Design (19) | M | **HD-10**, **HD-16** | Decision entry; budget check recorded with date (`techstack-cost-guardian`) |

## P2 — required for scale

| RM | Action | Fixes | Class | Owner | Effort | Needs |
|---|---|---|---|---|---|---|
| **RM-20** | Author plugin **P3** (demand-pattern layer) with four controlled vocabularies — `guest_segment`, `occasion`, `pathway`, `revenue_centre` — values only, each cited or declared `unruled`; add a coverage gate in the style of `p2_coverage_gate.py` | HV-12, HV-16 | EXTEND (Tier 2) | Sector (01) | M | **HD-08** |
| **RM-21** | Fix the audience-plane conflation: a `Plane` select on DB 9, or retarget DB 16 audiences to P3 segments | HV-17 | REFACTOR (Tier 1) | Sector (01) | S | **HD-09** |
| **RM-22** | A ratified Plane B narrative variant beside Story Architecture, and a plane-aware path through `content-publishing-gate` for client and demonstration content | HV-14 | EXTEND | Content (04) | M | **HD-10** |
| **RM-23** | Write the Pre-Experience methodology (Content) and production recipe (Design) — one document each, no new agent | HV-15 | NEW over EXTEND | Content (04) + Design (19) | M | **HD-10** |
| **RM-24** | One role vocabulary (`buyer · decision_maker · influencer · user · booker · intermediary · advocate`) for `AEIT_06` `Person` and P3 patterns | HV-16 | EXTEND | Governance (00) | S | **HD-08** |
| **RM-25** | Constrain `Lead.source_campaign` to a DB 4 `Campaign Code`; an M6 baseline template for the client folder; **defer the performance store until a client exists** | HV-18 | EXTEND | Marketing (03) + Governance (00) | S | — |
| **RM-26** | PIL profiles for WhatsApp, Google Business Profile, review platforms, OTAs, metasearch — when the first client needs them | HV-19 | EXTEND | Content (04) | M | first client |
| **RM-27** | Decide the owner of the Sector → Marketing/Operations route (item 31k); manual notes remain sufficient until then | HV-20 | INTEGRATION | Marketing (03) / Operations (08) | S | — |
| **RM-28** | Enact `AEIT_05` R1, R3, R5 and add an enactment column to ratified decisions | HV-21 | GOVERNANCE | Governance (00) | S | — |
| **RM-29** | Publish the lifecycle crosswalk (file 10 §3) beside the Client Success canonical model | HV-22 | REFACTOR | Client Success (07) | S | **HD-13** |
| **RM-30** | Calendar research: verify country- vs destination-level seasonality against T1 sources; author P7 rows for Sports, Mega-Event, Aviation; research route lead times; run Gate H on a real `< 30 days` signal | HV-24, HV-42 | DATA | Sector (01) | M | — |
| **RM-31** | P2 Tier 2 cells (incl. `Demand`); define `Destination Property`; a mixed-archetype rule | HV-25, HV-40 | DATA | Sector (01) | M | owner sector reasoning |
| **RM-32** | Register-prefixed identifiers in prose (`A001-D1`, `D41-G1`); one row schema for registers as each is next touched | HV-10 | REFACTOR | Governance (00) | S | — |
| **RM-33** | Refresh the RACI (Sector, Design, EE, Presence, client creative approval) | HV-31 | GOVERNANCE | Governance (00) | S | — |
| **RM-34** | Make Content DB 6 `Audience Role` sector-supplied (plugin P9 titles) rather than a fixed SaaS set | HV-43 | REFACTOR | Content (04) | S | — |
| **RM-35** | Carry archetype, destination, trigger, timing window and temperature in the prospecting batch/queue | HV-36 | EXTEND | Sales (05) | S | RM-07 |
| **RM-36** | Decide how outlets carry other sub-sectors (F&B, Wellness) under a hospitality parent | HV-41 | decision | Sector (01) | S | **HD-18** |
| **RM-37** | A learning register — **after** the first real client outcome exists (reality gate) | HV-33 | OWNED-UNBUILT | IntOS / Governance | M | first outcome |
| **RM-38** | Glossary: `Experience` = EE build; the guest product gets another name | HV-39 | DUPLICATE (risk) | Governance (00) | S | **HD-08** |

## P3 — optimisation

| RM | Action | Fixes |
|---|---|---|
| RM-39 | Reword `AEIT_08` §4 "8th rhythm" → "a refresh rhythm that feeds the seven" | HV-23 |
| RM-40 | Give `finos.clients` a CRM `client_id` reference before finos holds real data | HV-32 |
| RM-41 | `AEIT_10` Phase 0 hygiene: archive the root scripts, delete the superseded brief DB after the routine is re-pointed, break the three non-terminating loops | HV-34 |
| RM-42 | Constitution header/contact line; claims-policy ICP line; positioning string L10 | HV-35 |
| RM-43 | Add the Content DB 5 → DB 16 `Destination` relation (31l) | HV-37 |
| RM-44 | Owner-authorised re-verification of decayed live claims (Postiz, KIE/OpenArt credits, Zoho plan, connector auth) with the Tech Stack agents | HV-38 |
| RM-45 | Run Gate I (a second, non-travel sector) when one is activated | HV-42 |
| RM-46 | First real runs of the agents a delivery needs — only when the pilot needs them | HV-45 |

## P4 — future enhancement (deliberately deferred)

IntOS proper (`AEIT_07`) · a dashboard spine · a knowledge-graph store · unattended ingestion and ICS subscriptions · the demand-surge rule · an EE interactive prototype microsite · a client portal · a group/portfolio offer (OEOS) · expansion rungs (guest acquisition, guest CRM/retention, revenue intelligence) · a performance store at scale.

## 6. Do not overbuild (protocol §25)

| Temptation | Why not | What to do instead |
|---|---|---|
| A **Hospitality department** or "Hospitality OS" | Fails the plugin-removal test; *"a hospitality system wearing a sector-OS label"* | Plugin + offer + overlay + CRM structure (file 03) |
| **Fifteen calendar stores** | `SECTOR_ACTIVATION_CONTRACT.md` §15 forbids a calendar per layer; a 17-layer proposal was already reduced to 2 DBs | Views over DB 7/15/16 + client inputs (file 06) |
| A **Property / Outlet / Venue store** | The CRM `Company` is the entity registry; a parallel store is banned (§14.4) | `Company` levels |
| An **Experience / Occasion / Season / Audience database** | Values, not entities, until a second department must reference one by ID | P3 vocabularies |
| A **B2B2C CRM** or intermediary database | Duplicates the CRM and the Partner object | Intake rows + pathway vocabulary |
| A **ticketing platform** (Jira, Linear, etc.) | Moves the problem; the registers' content is good, their shape is the issue | ClickUp Project tasks for client work; one row schema for registers |
| **New agents** for Pre-Experience, B2B2C, calendars | 115 agents exist; 106 have never run on real input | Use Content, Design and EE's existing agents |
| **Automated outreach sequences** | A public inbox is not consent; Class 3 per send | One manual, reviewed touch per account |
| **Unattended AI generation** | Credit runway; depiction risk; Class 3 publishing | Human-approved generation through the reuse gate |
| **A performance store before a client** | Empty structure; nothing to measure | M6 baseline in the client folder |
| **Exhaustive P2/P3 rule matrices** | *"A guess is worse than a declared gap"* | Tiered authoring; declared `unruled` |
| **Renumbering every identifier** | Breaks history and references | Prefix by register in prose |
| **Rewriting governance documents wholesale** | Churn without value (`AEIT_01` §3) | Targeted edits with dated "was:" notes |

**Things that can stay simple:** one owner (all RACI cells resolve to one person); manual hand-offs for one pilot (RD6); markdown registers; text IDs across platforms (Content design law 2); public-only research until the legal chain closes.
