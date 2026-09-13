# Sector — Operating Cadence

**Department:** Sector (01) · **Version:** v0.1 (2026-09-13) · **Status:** `DESIGNED`, executed **manual-apply**.
**Reads:** [`SECTOR_WRITE_CONTRACT.md`](SECTOR_WRITE_CONTRACT.md) §4.4 (the proximity ladder — the daily tier *is* that ladder) · [`SECTOR_OS.md`](SECTOR_OS.md) §4 · [`SECTOR_SKILL_MATRIX.md`](SECTOR_SKILL_MATRIX.md) §2 · [`AEIT_11`](../00_Agency_Governance/enterprise_architecture/AEIT_11_RUNTIME_TRUTH_STANDARD.md) §2.

---

## 0. Read this before the tables

> 🔴 **Every tier below is `DESIGNED`. Not one has ever run on a schedule.**

The agent specs declare a Monday cron (`0 8 * * 1`) and a monthly cron (`0 8 1 * *`). **Neither has ever fired.** `01_Sector/_memory/runtime.jsonl` does not exist, and `memory-writer.ts` creates it on first write — so its absence is the proof, not an assumption. Every one of the department's 15 executions to date was a **human opening a session and invoking a skill**.

**A cadence with a cron and no run is a schedule, not a habit.** This file is written so the distinction stays visible: it describes what *should* recur and names, per row, what would prove it did.

**This introduces no new loop.** It sequences the six loops already in `SECTOR_WRITE_CONTRACT.md` §6 (activation · refresh · signal-change · calendar recomputation · feedback · failure-recovery) onto a clock.

**Promotion rule.** A row moves `DESIGNED → LIVE` when — and only when — a dated execution record exists for it in `_memory/skill_runs.jsonl`. Per `AEIT_11` R3 that state then **decays**: it carries a `last_verified` date and reverts on lapse. Per R4, **a downgrade is ordinary reporting.**

---

## 1. Daily — *what is about to happen, and what has gone stale*

**This tier is not a new invention: it is the proximity ladder's short bands made operational.** The ladder already says a signal inside 30 days is re-verified every run and one inside 7 days escalates immediately. The daily tier is the *run*.

| # | Check | Owner | Input | Output | Reality |
|---|---|---|---|---|---|
| D1 | Signals with `Signal Date` or an activation date **inside 30 days** | S04 | DB 7 + the `⚡ Next Up` view | Re-verified dates, or a `VERSION` | `DESIGNED` |
| D2 | Signals **inside 7 days** — a change escalates same-day | S04 | DB 7 + `🚨 Gate Watch — Act Now` | Escalation, not a queue entry | `DESIGNED` |
| D3 | Anything at `Needs verification` or `Superseded/Delayed` | S04 | DB 7 status filter | Resolved, or explicitly carried with its caveat | `DESIGNED` |
| D4 | **Derived activation dates that have passed** | S09 | the Timeliness gate | A finding — *a failed Timeliness gate is a finding, not a filter* | `DESIGNED` |
| D5 | Open opportunity windows for the active sector | S09 | resolution output | What is actionable today | `DESIGNED` |

> **D4 is the one that earns this tier.** Gate F's first run caught a derived Action Deadline that had passed **ten days earlier**, silently. Nothing was watching. That is precisely the failure a daily pass exists to catch, and it is the reason this tier is daily rather than weekly.

**Skip conditions are legitimate.** If no signal sits inside 30 days and nothing is flagged, the daily pass is a **NO_OP** — and a NO_OP still bumps `Last Verified`, because *checked and unchanged* is a real result.

---

## 2. Weekly — *the operating cadence the department already had*

The five steps from `SECTOR_OS.md` §4, unchanged. **Declared on `sector-intelligence-mapper` as a Monday cron that has never fired.**

| # | Step | Owner | Output | Reality |
|---|---|---|---|---|
| W1 | **Intelligence Update** — what changed in the market | S01 (+ `sector-intelligence-mapper`) | New/updated DB 3 findings, each answering all eight questions | `DESIGNED` |
| W2 | **Opportunity Review** — what the changes open | S09 → Content (04) | Scored content opportunities | `DESIGNED` |
| W3 | **Offer Refinement** — what we can now sell into | S08 | DB 8 routing, or `GAP — needs OEOS` | `DESIGNED` |
| W4 | **Pipeline Push** — what leaves the department | S10 | A packet, **plus a `HANDOFF_FAILURE` per unreachable destination** | `DESIGNED` |
| W5 | **Execution Audit** — did last week's intent become rows | — | The drift register | `DESIGNED` |

> **W4 currently reports three failures of six destinations every time it runs**, and will keep doing so until owner item **31k** is decided. That is the gate working, not the gate broken.
>
> **W5 is the step this department has historically skipped**, and skipping it is how sixteen documentation-drift items accumulated. It is now partly mechanical: `python 01_Sector/contracts/sector_truth_gate.py`.

---

## 3. Monthly — *is the picture still true*

| # | Check | Owner | Trigger detail | Reality |
|---|---|---|---|---|
| M1 | **Readiness reassessment** across the vertical universe | `sector-readiness-analyst` | declared monthly cron; never fired | `DESIGNED` |
| M2 | **Source health** — DB 14 `Next Verification` falling due | S03 | **Authority ≠ reachability.** A failed call leaves `Last Verified` **blank**; it never downgrades the publisher's tier | `DESIGNED` |
| M3 | **Sector State re-distil** | S06 | May introduce **no new fact**; empty stays empty with its reason | `DESIGNED` |
| M4 | **Stale-signal sweep** — anything past `Next Verification` | S04 | Stale intelligence must not drive downstream execution | `DESIGNED` |
| M5 | **Regulatory + Economic signals** — monthly floor regardless of distance | S04 | The ladder's standing override | `DESIGNED` |
| M6 | **Prospect re-score**, Medium band — *"signals decay"* | S12 | 🔲 **BLOCKED — S12 does not exist.** Its two schema blockers (F4, F5) were closed 2026-09-13; the **scraping gate** remains: API key + cost governance + Legal posture + an Approval-Matrix row | `INTENDED` |

> **M6 is the only row here whose blocker is not time.** It is listed so the 30-day decay rule stays visible as an unhonoured commitment rather than quietly disappearing — the scorecard remains *"ready to use, not validated by use."*

---

## 4. Quarterly — *is the model still right*

| # | Review | Owner | What it decides | Reality |
|---|---|---|---|---|
| Q1 | **P2 rule matrix** — re-run `p2_coverage_gate.py`; re-examine cells at `basis: owner_reasoning` | owner + S11 | Whether any cell has earned evidence and can leave `owner_reasoning`. **Ratified for internal use only (31i)** — a cell may filter a calendar and may not be quoted to a client | `DESIGNED` |
| Q2 | **P14 semantics** — what the DB 12 state selects mean for this sector | owner | Includes the two still undefined, `Tech Disruption` and `Regulatory Risk` (31f) | `DESIGNED` |
| Q3 | **Source-cost review** | owner + Tech Stack (13) | Whether the free T1 path still suffices (31g). **Rate/benchmark data is a Legal (10) engagement-clause question, not a purchase** | `DESIGNED` |
| Q4 | **Sector priority re-score** — the 8-dimension score across the universe | `sector-readiness-analyst` | Which vertical is next. **No black-box number** — the rationale travels with the score | `DESIGNED` |
| Q5 | **Gate I / generalization work** | S11 | Progress toward Sector #002, per §3c's five pre-written falsifiers | `DESIGNED` |

---

## 5. Yearly — *is the foundation still standing*

| # | Review | Owner | Why annual | Reality |
|---|---|---|---|---|
| Y1 | **Plugin recertification** — every slot in every `sector_plugins/*/` re-verified or demoted to ⬜ | S11 | A plugin is a set of claims about a market. Claims expire. **A slot nobody can re-source goes back to unauthored** | `DESIGNED` |
| Y2 | **Taxonomy review** — DB 1 / DB 2 | S07 | Markets merge, split and die. **Promotion stays evidence-gated; no self-promotion** | `DESIGNED` |
| Y3 | **Legal / data-posture review** | Legal (10) | Scrape postures, source T&Cs, and the open **Kenya DPA s.48 cross-border finding** (item 61) — *s.48 safeguards are pre-transfer and cannot be applied retroactively* | `DESIGNED` |
| Y4 | **Stale-signal archiving** | S04 | **Archive, never delete.** A recurring event is a **prediction until its next edition is published** and is never auto-rolled forward | `DESIGNED` |
| Y5 | **Strategic sector-priority reset** | owner | Which sectors Arika is actually in next year | `DESIGNED` |

---

## 6. What no cadence can currently do

Stated so no tier above is read as more than it is.

1. **Nothing fires unattended.** Every row needs a person to open a session. The crons are declarations.
2. **No event delivers.** `executor.ts` never publishes; a cadence step may *record* an intended event, never assert one was delivered.
3. 🔴 **The feedback loop cannot close.** There is **no performance store anywhere in the agency** — Marketing (03) owns the concept and has none. No cadence can measure whether last quarter's intelligence was *right*; only whether it was *refreshed*. **Never infer performance from activity.**
4. **Two of six handoff destinations have no route at all** (31k).

---

## 7. Cross-references

[`SECTOR_WRITE_CONTRACT.md`](SECTOR_WRITE_CONTRACT.md) §4.4 §6 · [`SECTOR_SKILL_MATRIX.md`](SECTOR_SKILL_MATRIX.md) · [`SECTOR_OS.md`](SECTOR_OS.md) §4 §16 · [`SECTOR_ACTIVATION_PROTOCOL.md`](SECTOR_ACTIVATION_PROTOCOL.md) §3b §3c · [`SECTOR_CALENDAR_REFRESH_SPEC.md`](SECTOR_CALENDAR_REFRESH_SPEC.md) §2a · `00_Agency_Governance/OWNER_INPUT_NEEDED.md` 31f/31g/31i/31k · `08_Operations/OPERATIONS_OS.md` §12a (**this is an input to the 7 Cognitive Calendars, never an 8th**).

## 8. Changelog

- **v0.1 (2026-09-13):** Created. The department had a **weekly and monthly** cadence in `SECTOR_OS.md` §16 and nothing else; the **daily, quarterly and yearly** tiers are new here. The daily tier is not an invention — it is the existing proximity ladder's `<30d` and `<7d` bands finally given a run, and its justification is empirical: Gate F's first run found a derived Action Deadline that had **passed ten days earlier with nothing watching**. Every row carries a reality state, and **all of them are `DESIGNED`** — the Monday and monthly crons have never fired, because `runtime.jsonl` does not exist. A promotion rule to `LIVE` is stated so the file cannot drift into describing itself as operational. **§6 names the four things no cadence here can do**, the sharpest being that the feedback loop cannot close for want of any performance store in the agency. — Claude Code (Opus 5)
