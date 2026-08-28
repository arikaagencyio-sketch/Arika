---
name: sector-signal-writer
description: Skill S04 of Sector (01). Writes one market signal in DB 7 with its full commercial interpretation — type, geography, lead-time activation dates, per-function impact, routing — and owns the change-history discipline. Tiers are INHERITED from a source S03 registered, never assigned by hand. Use on a refresher proposal, a verification cadence, a newly registered source, or a signal that changed.
---

# S04 · Sector Signal Writer

You are performing the **apply** step of Sector's write layer. An agent proposes what is true; this skill decides whether that truth may become a database state, and in what mutation mode.

**Read [`01_Sector/SECTOR_WRITE_CONTRACT.md`](../../../01_Sector/SECTOR_WRITE_CONTRACT.md) first.** Field truth: [`01_Sector/contracts/sector-databases.json`](../../../01_Sector/contracts/sector-databases.json) — DB7. Contract row: `SECTOR_SKILL_MATRIX.md` §2.

> **DB 7 is the single signal store.** All five calendar layers are **views** over it — never a calendar per layer, never a second table. And the calendar itself is *computed* by S09, never stored: a 365-day calendar is an output, not 365 rows.

---

## Step 0 · The write path

| | Data source |
|---|---|
| DB7 Sector Signals | `collection://c14fedb3-6048-4bc5-8a40-6558cc985f57` |
| DB14 Signal Sources | `collection://13741534-e31d-4ff8-bebf-dd50133e20af` |
| DB11 Geography | `collection://e095c661-86cd-4f45-9149-eca1c7195e71` |
| DB2 Sub-Sectors | `collection://dbe10a8b-5c67-4602-9108-12feb540995c` |

## Step 1 · Resolve context, then resolve the source

Standard Execution Context resolution (write contract §2), then the thing that makes this skill different:

**Find the registered DB 14 row for this signal's publisher, and link it.** `Signal Source` is a relation for a reason — a `Source Tier` with no relation behind it is an assertion, not an inheritance.

| Source state in DB 14 | What you may write |
|---|---|
| `active` | Inherit its `Authority Level` into `Source Tier`. Set the `Signal Source` relation. |
| `candidate` | **You may not inherit.** Record the signal as unbacked (Step 3) and say which source it is waiting on. |
| Not registered at all | **STOP the tier claim.** Either run S03 first, or write the row unbacked. Never invent the tier. |

**A signal may never out-rank its publisher.** T4 may *discover* but may not *confirm*, and a T4, unverified or stale row **must not drive a downstream event or department action**. Where an aggregator and the organiser disagree, **the organiser wins**.

## Step 2 · Duplicate detection and mutation mode

Match on **title + sub-sector** before creating. Then choose the mode explicitly — `CREATE` · `UPDATE` · `VERSION` · `SUPERSEDE` · `NO_OP` · `REJECT` · `ESCALATE`.

**`NO_OP` is a real outcome here more than anywhere else.** Most refresh runs find nothing changed — and *checked and unchanged* is a result worth recording. Bump `Last Verified` and move on.

## Step 3 · The tier honesty rule — this skill's central discipline

A tier that no registered publisher stands behind is worse than a blank one, because it passes the tier gate silently.

When you cannot inherit:

- Leave the existing `Source Tier` **as it is** — do not "correct" it to something else you also cannot back.
- Say so in `Change Reason`: which source it needs, and that the tier is currently unbacked.
- Set `Refresh Status = Needs verification`, which **blocks the row from resolution** at Resolution Engine step 1. That is the correct consequence, not a punishment.
- Never upgrade a tier because a claim *looks* authoritative. Authority comes from the registry.

> **An unexamined `T1` is more dangerous than an admitted `T3`.** Rows that declare their own weakness in `Authoritative Source` are doing the right thing; rows that assert T1 with nothing behind them are the actual risk.

## Step 4 · The change-history rule — five steps, and step 4 is the one that matters

**This rule's home is here** (`SECTOR_CALENDAR_REFRESH_SPEC.md` §2b), generalised by the write contract to every Sector database. On any `VERSION` or `SUPERSEDE`:

1. **Preserve the prior value** — `Previous Signal Date`, and `Change Reason` saying what changed, when, which source, what tier.
2. **Append a dated line to the page body.**
3. **Set the status fields** — `Change Status` (`New` · `Changed` · `Cancelled` · `Unchanged`) and `Refresh Status`.
4. **Name what it invalidates** — Market Routes, Content Opportunities, campaign windows, derived activation dates, downstream briefs.
5. **Emit the matching event — only after checking it has a subscriber** (Step 7).

**Step 4 is the difference between a database row edit and operating-system behaviour.** A moved date silently orphans every derived date computed from it. List them.

## Step 5 · Dates — three kinds, never confused

| Kind | Fields | Rule |
|---|---|---|
| **Observed** | `Signal Date`, `Announcement / Source Date` | **Web-cited or blank. Never invented.** |
| **Derived** | `Strategic Planning Date` · `Marketing Activation Date` · `Sales Activation Date` · `Offer Activation Date` · `Revenue Watch Date` · `Action Deadline` · `Execution Deadline` | Computed from plugin **P7** via [`plugin.config.json`](../../../01_Sector/sector_plugins/hospitality/plugin.config.json). **Label as a planning offset — never as an external fact.** |
| **Governance** | `Last Verified` · `Next Verification` · `Review Date` | `Last Verified` means last *successful* verification. |

**Where a P7 offset is unauthored, report it unavailable.** For Sector #001 that is `Sports`, `Mega-Event`, `Cruise/Port` and `Aviation/Connectivity` — `null` in the sidecar. **Never substitute a neighbouring row's offset**; a plausible date is the failure mode this whole layer exists to prevent.

`Recurrence = Annual` is **never auto-rolled forward.** *A recurring event is a prediction until its next edition is published.* Verify at T-180 each cycle.

### `Next Verification` comes from the ladder, not from habit

| Time to `Signal Date` | Re-verify |
|---|---|
| > 180 days | Monthly |
| 180–90 | Fortnightly |
| 90–30 | Weekly |
| < 30 | **Every run** |
| < 7 | **Every run**, and a change escalates immediately |

Overrides that beat the ladder: `Needs verification` → every run · `Superseded/Delayed` → every run until resolved · **Regulatory and Economic → at least monthly regardless of distance.**

## Step 6 · Fields — yours, and the two traps

**Yours (41):** `Signal` · `Sub-Sector` · `Sector` · `Signal Type` · `Signal Role` · `Geography` · all seven date fields above plus `Previous Signal Date` and `Announcement / Source Date` · the eight impact selects (`Demand Impact` · `Revenue Impact` · `Sales Impact` · `Marketing Impact` · `Offer Impact` · `Distribution Impact` · `Competitive Impact` · `Regulatory / Risk Impact`) · `Commercial Priority` · `Departments Affected` · `Recommended Action` · `Audience / Market Segment` · `Recurrence` · `Status` · `Change Status` · `Change Reason` · `Refresh Status` · `Source Tier` · `Authoritative Source` · `Source URL` · `Signal Source` · `Confidence` · `Last Verified` · `Next Verification` · `Review Date`.

**Not yours:** `Sector Intelligence` (S01) · `Market Routes` (S05) · `Platform Overlays` and `Content Opportunities` (S10).

**Trap 1 — `Sub-Sector` is the scope axis, not `Sector`.** The select is now literally named **`Sector (deprecated — use Sub-Sector)`** in Notion (renamed 2026-08-28, owner item 31e) — a **column** rename, so all 21 options kept their IDs and no row lost a value. It is a **deprecated overloaded axis** (F1): it mixes SaaS categories with verticals and has **no Hospitality option at all**. Populate it only for continuity with existing rows; **never filter or resolve on it**, and do not extend it one name at a time. *A deprecation that lives only in a markdown file is not a deprecation — someone will populate the field. The name now says so in the UI.*

**Trap 2 — `Departments Affected` carries two deprecated options.** `Revenue (Ops)` (canonical: **Operations**) and `ClientPartner` (canonical: **ClientPartner Acquisition**) are still live only because removing an option strips it from every row using it. **Never write either on a new row.** Validate against the live option set at write time.

The eight impact fields are **derived** — your reading of what the signal does to each function, not a market fact. `Low`/`Medium`/`High` each, feeding `Commercial Priority` and the P13 compression threshold. Leave them empty rather than guessing.

## Step 7 · Verify, log, and the event check

Read the write back. Append to `01_Sector/_memory/skill_runs.jsonl` per [`contracts/skill-execution-record.schema.json`](../../../01_Sector/contracts/skill-execution-record.schema.json) with `skill_id: "S04"`, every gate result, and `writes[].invalidates` on any version.

**Check subscribers before recording any event** ([`contracts/event-catalog.json`](../../../01_Sector/contracts/event-catalog.json)):

| Event | State |
|---|---|
| `CALENDAR_UPDATED` · `REGULATORY_CHANGE` | ⚠️ **intra-Sector only** — three files claim otherwise; neither subscriber has the trigger |
| `DEMAND_SHIFT` · `COMPRESSION_EVENT` · `COMPETITOR_MOVE` | 🔴 **zero subscribers** — recording one is a `HANDOFF_FAILURE`, not a handoff |

Record the event you *would* emit and its subscriber state. **Never claim a publish happened** — nothing in this repo calls `eventBus.publish()`.

Loops: `signal_change`, `refresh`, `calendar_recomputation`.

---

## Refuse

- **A `Source Tier` with no registered `active` source behind it.** The core refusal.
- An invented `Signal Date`, or a derived activation date presented as external fact.
- A property's live booking or revenue figures — ⚫ never fill.
- A signal out-ranking its publisher.
- Auto-rolling an annual recurrence to next year.
- Writing a deprecated `Departments Affected` value on a new row.
- Any field whose `writer_skill` is not S04.

## Appendix · A dated snapshot — re-measure it, do not trust it

> **Observation with an expiry date.** Step 1 governs.

**Measured 2026-08-28.** DB 7 held **34 rows, none with a null tier**: 25 `T1 Primary`, 7 `T3`, 2 `T4` — and **zero linked to a registered source**. Every tier was a hand-assignment. Only 1 of the 25 T1 rows was Hospitality; **24 were the SaaS branch**, outside the Kenya-inbound P8 pack and unexamined, while the 9 flagged Hospitality rows honestly declared themselves T3/T4 in their own source fields.

DB 14 held 2 `active` sources, so exactly **3 signals could legitimately inherit** a tier. The rest were unbacked and had to be recorded as such.
