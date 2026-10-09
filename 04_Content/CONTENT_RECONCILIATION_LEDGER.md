# Content Reconciliation Ledger — LinkedIn launch drafts and V2 briefs

**Department:** Content (04) · **Created:** 2026-10-09 · **Status:** **Every item is pending review. Nothing here is approved.** This implementation unit authorised reconciliation, not publication. No G2 decision has been made on any item.

**What this ledger is.** One linked record of all 17 drafts in [`21_Presence/LINKEDIN_LAUNCH_CONTENT.md`](../21_Presence/LINKEDIN_LAUNCH_CONTENT.md) (drafted 2026-08-09) and both briefs in Notion DB 7 Content Briefs v2. Original labels and source text are preserved where they are. This file proposes; it does not edit them. Rules: [`CONTENT_WRITE_CONTRACT.md`](CONTENT_WRITE_CONTRACT.md).

**Where the drafts live today.** The 17 repository drafts are **not** in Notion (live search 2026-10-08). They enter the V2 chain only through C01 → C03 → C04, after the owner selects them, with each claim passing C05.

---

## 1. The ledger

`Legacy pillar` is the label in the launch file, kept as metadata. `Canonical` is the proposed mapping to the 7 pillars (`CONTENT_OS.md` §10). `Position (proposed)` is the DB2 narrative family the piece would belong to; C02 confirms it. Confidence: H/M/L.

| ID | Original label (launch file) | Surface | Legacy pillar → Canonical | House · Format | Source · source date | Position (proposed) | Review flags | Proposed action |
|---|---|---|---|---|---|---|---|---|
| LC-P01 | Post 1, wk 1 Mon | Founder profile | Revenue Reality → Revenue Reality | Founder Thinking · Opinion Stand | Repo state, 2026-08-09 | `nar-core-revenue-growth-system` (M) | 🔴 **premise false** (§3.1); "I watch companies… every week" is an experience claim | **Replace** with §3.1 |
| LC-P02 | Post 2, wk 1 Wed | Founder profile | Revenue Intelligence (canonical) | Frameworks · Framework Drop | Sector node, owner-curated xlsx | `nar-misconception-tactics` (L) | none material | Keep; enter chain when selected |
| LC-P03 | Post 3, wk 1 Fri | Founder profile | Revenue Architecture (canonical) | Insights · Hook-and-Pivot | Sector cross-sector pattern "tool adoption without process design" | **Family A** (§2) | "used at about 20% and blamed at 100%" reads as a statistic with no source | Revise the figure into plain argument |
| LC-P04 | Post 4, wk 2 Mon | Founder profile | Revenue Operations (canonical) | Founder Thinking · Narrative Lesson | 11-day outage, 2026-07-04→07-15 (`16_Automation/AUTOMATION_OS.md` incident) | none fits (L) | 🔴 "Mine now has all three" unsupported (§3.3); "most common gap I find" is an experience claim | **Revise** with §3.3 |
| LC-P05 | Post 5, wk 2 Wed | Founder profile | Revenue Reality → Revenue Reality | Insights · Opinion Stand | Draft 13 argument, biography removed | `nar-misconception-sales-solution` (H) | none material | Keep |
| LC-P06 | Post 6, wk 2 Fri | Founder profile | Revenue Signals (canonical) | Frameworks · Framework Drop | Sector 6-category signal framework | `nar-belief-bi-is-growth-advantage` (M) | "Most teams work only category 4" is a generalisation; frame as opinion | Minor revise |
| LC-P07 | Post 7, wk 3 Mon | Founder profile | **Revenue Decisions (legacy)** → Revenue Leadership (M) | Insights · Hook-and-Pivot | Sector Anti-ICP (`01_Sector/SECTOR_OS.md` §1) | none fits; positioning piece (L) | ⚠ legacy pillar mapping needs owner review (§4) | Keep text; confirm pillar |
| LC-P08 | Post 8, wk 3 Tue | Founder profile | Revenue Operations (canonical) | Founder Thinking · Narrative Lesson | TechStack re-check 2026-07-15 (4 of 30 rows false) | `nar-belief-data-drives-decisions` (L) | 🔴 "last month" stale (§3.2) | **Revise** with §3.2 |
| LC-P09 | Post 9, wk 3 Wed | Founder profile | **Unpopular Opinions (legacy)** → format, not pillar; subject → Revenue Architecture (M) | Founder Thinking · Opinion Stand | Draft 13 argument | `nar-enemy-fragmentation` (L) | ⚠ legacy label (§4) | Keep text; confirm pillar |
| LC-P10 | Post 10, wk 3 Thu | Founder profile | **Revenue Beyond Money (legacy)** → Revenue Intelligence (M) | Frameworks · Framework Drop | Draft 13 "5 Forms of Revenue" | `nar-belief-revenue-is-a-system` (M) | ⚠ legacy label (§4) | Keep text; confirm pillar |
| LC-P11 | Post 11, wk 4 Mon | Founder profile | Revenue Signals (canonical) | Insights · Hook-and-Pivot | Sector cross-sector pattern | `nar-belief-bi-is-growth-advantage` (M) | "the window is roughly the first two quarters" needs a source or an opinion frame | Revise or source |
| LC-P12 | Post 12, wk 4 Tue | Founder profile | Revenue Reality → Revenue Reality | Founder Thinking · Narrative Lesson | Host migration (`21_Presence/CONTENT_DISTRIBUTION_ENGINE.md` §10: Railway rejected card, OOM kill, Hostinger live 2026-08-07) | none fits (L) | "Three days" not confirmed by the record: verify or remove | Verify, then keep |
| LC-P13 | Post 13, wk 4 Wed | Founder profile | **Unpopular Opinions (legacy)** → format; subject → Revenue Architecture (M) | Insights · Opinion Stand | Draft 13 argument | `nar-misconception-tactics` (H) | 🔴 "I've watched companies hit a number they'd chased for two years…" asserts observed client history the record does not hold | **Revise**: remove or reframe as argument |
| LC-P14 | Post 14, wk 4 Thu | Founder profile | Revenue Intelligence (canonical) | Frameworks · Framework Drop | Draft 13 revenue-anatomy structure | `nar-belief-data-drives-decisions` (M) | "Revenue was up 12%" is a hypothetical; label it as one | Minor revise |
| LC-C1 | Page launch post | Company Page | (none) → Revenue Architecture (M) | Founder Thinking (institutional) | Repo positioning | `nar-core-revenue-growth-system` (H) | Positioning string still open (L10); copy is cross-sector-safe | Keep; recheck after L10 |
| LC-C3 | Institutional observation | Company Page | (none) → Revenue Architecture (M) | Insights | Sector cross-sector pattern | **Family A** (§2) | "repeats across almost every sector we map" overstates; soften | Minor revise |
| LC-B1 | Revenue Architecture Brief #001 | Company Page | (none) → Revenue Architecture (M) | Frameworks · Article | Sector cross-sector pattern | **Family A** (§2) | Two unsourced figures: "repeats more than any other", "below a third of capability" | Revise both |
| LC-H1 | Notion DB7 `3c121e15eb9381f48574dfe6e1f43828` · "The OTA Tax — LinkedIn carousel (Awareness)" | **Not yet assigned** | Revenue Intelligence (inherited, DB5) | Insights · Carousel | StayNTouch / Pixel & Polish 2026, T3, researched 2026-08-19 | `nar-misconception-more-leads` (**linked**) | Surface unassigned (blocks readiness); both DRAGON passes `Not yet run`; Engagement Follow-up names an audit offer not in DB8 (no price stated) | Owner: choose surface; C01/C03 run passes |
| LC-H2 | Notion DB7 `3c121e15eb9381b9aa93cad6e6ac7d9c` · "The real cost of an OTA booking — Newsletter #1" | Single-identity channel | Revenue Intelligence (inherited) | Insights · Newsletter issue | Same sources + Sector direct-share benchmark | `nar-misconception-more-leads` + `nar-belief-trust-accelerates-sales` | No email list exists; copy names the OTA-Leakage Audit, which is not in DB8; DRAGON passes `Not yet run` | Hold until a list exists; Offer (02) to confirm the audit |

**Status of every row:** `pending review`. **G2:** none. **Notion:** LC-H1 and LC-H2 carry `G2 Decision = Not submitted` (set 2026-10-09).

---

## 2. Family membership

- **Family A, "tool adoption without process design":** LC-P03 (founder argues it) + LC-C3 (Page observes it) + LC-B1 (Page documents it). Three surfaces, one argument: a real family, not duplicates. **No DB2 position exists for it yet.** C02 decides whether it is a new position (proposed ID `nar-misconception-tools-before-process`) or maps to `nar-misconception-automation-solution` (L). Until then, no translation is created for it.
- **OTA family (`nar-misconception-more-leads`):** LC-H1 (LinkedIn) + LC-H2 (Newsletter). Distinct platforms, `Narrative Preserved = Yes` on both. Verified intact 2026-10-09. **Do not create a third member until the surface decision on LC-H1.**
- Every other row is a single-member family candidate. Its `Position (proposed)` is a starting point for C02, not a decision.

---

## 3. Proposed revisions

Originals are preserved in the launch file. These proposals replace them only after the owner selects them and G2 approves the exact revision.

### 3.1 LC-P01: replacement for the obsolete premise

The original says "I built 106 AI agents… Not one of them can run. The API key isn't set." That is false today, and the run records show it was already inaccurate on 2026-08-09: Branding and Design agents had run in July.

**Verified facts (2026-10-09):** 115 agent specifications register in `arika-runtime` (`npx arika list`). Non-fixture run records exist for **7 distinct agents, 15 runs in total**, across Branding (2026-07-14, 2026-07-19), Design (2026-07-19), Tech Stack (2026-08-23 → 08-30) and Offer (2026-09-13), counted from `*/_memory/runtime.jsonl`. **Re-count at G2: the numbers will move.**

> I've written 115 AI agent specifications for my agency.
>
> Seven of them have ever run. Fifteen runs, in total.
>
> The other 108 are documents. Careful, connected, well-argued documents that have never done a thing.
>
> I did the fun part first.
>
> I want to be precise about why that matters, because it isn't a story about AI. It's the pattern I think sits under most revenue problems:
>
> — The CRM before the process it's supposed to hold
> — The sales hire before the offer they're supposed to sell
> — The campaign before the thing it's supposed to point at
> — The automation before the workflow it's supposed to remove
>
> Architecture feels like progress because it looks like progress. Execution is small, repetitive and unglamorous, and it's the only thing that produces revenue.
>
> I'm fixing it in public, one department at a time.
>
> What have you architected beautifully and never turned on?

Changes: the false premise is replaced by counted facts; "I watch companies make with revenue every week" (an experience claim) becomes "the pattern I think sits under most revenue problems" (an opinion).

### 3.2 LC-P08: relative timing

The audit ran on **2026-07-15**. "Last month" was true on 2026-08-09 and is wrong on any later publish date. Proposed first line: *"In July I audited my own tool inventory."* Everything else is unchanged. The figures (4 of 30) match `13_Tech_Stack/TECHSTACK_OS.md`.

### 3.3 LC-P04: the unsupported claim

"Every automation you own needs three things: a heartbeat, an owner, and an alert… **Mine now has all three.**" The record does not support the last sentence. `automation-reliability-monitor` exists as an agent specification (built 2026-07-15), but no approved schedule runs it, and nothing shows a heartbeat or alert live on the Creative Pipeline routine. Substantiate it or remove it. Proposed replacement for the last two lines:

> Mine has an owner. The monitor that would raise the alarm is written, and isn't switched on yet. I'm saying that out loud because it's the honest version of this lesson.
>
> What's running in your business right now that nobody would notice had stopped?

If the monitor is switched on and verified before publication, the original line may return, with the evidence recorded in `Evidence`.

---

## 4. Legacy pillar labels: flagged for the owner

The launch file uses four LinkedIn-only labels (`21_Presence/LINKEDIN_PRESENCE_OS.md` §7.2). The Notion `Pillar` field accepts only the canonical seven. Proposals, all **pending owner review**; legacy labels are kept as metadata and never silently re-tagged:

| Item | Legacy label | Proposal | Why |
|---|---|---|---|
| LC-P07 | Revenue Decisions | Revenue Leadership | "Leadership decisions that determine growth": deciding whom not to serve |
| LC-P09 | Unpopular Opinions | Format, not pillar. Subject: Revenue Architecture | The argument is about how agency contracts are structured |
| LC-P10 | Revenue Beyond Money | Revenue Intelligence | "Why revenue behaves the way it does": five forms of revenue |
| LC-P13 | Unpopular Opinions | Format, not pillar. Subject: Revenue Architecture | Growth amplifies structure |

---

## 5. Known gaps carried forward (not fixed in this unit)

| Gap | Where | Why it was not fixed |
|---|---|---|
| 10 DB2 belief rows (created 2026-08-19) have a blank `DRAGON Reading` | Notion DB2 | Filling them is a judgement (`Not applicable` is likely). Proposed for C02's first run; not done silently |
| DB1 LinkedIn `Account Status = Not created`, but the profile and Company Page exist | Notion DB1 | Presence (21) owns `Account Status`; listed for the Presence unit |
| Opportunities `opp-accom-direct-benchmark-002` and `opp-accom-low-season-003` have no Narrative Position | Notion DB5 | No translation or brief carries evidence of the right position; the link is not guessed |
| No hospitality offer exists in DB8; LC-H1 and LC-H2 name the OTA-Leakage Audit | Notion DB7 | Offer (02) owns offers. Absence recorded; no price or term may be stated |
| LC-H1 `Surface = Not yet assigned` | Notion DB6 | Founder profile or Company Page is an owner editorial decision |
| `Approval Integrity` formula output is not readable through the API | Notion DB7 | Verify once in the Notion UI |

## 6. Changelog

- **2026-10-09** — Created. 19 items reconciled (17 repository drafts, 2 Notion briefs). Notion repairs applied the same day are recorded in `CONTENT_OS.md` §8. — Claude Code (Opus 5.5)
