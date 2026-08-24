# Sector Signal — Real-Time Refresh Engine (Spec)

> **Evolved 2026-08-15 (SCIC Phase D):** this spec now governs the full **Sector Signal Refresh** — all signal types + commercial-impact + lead-time + downstream routing, of which calendar-date re-verification is one facet. *(The enum was 16 types when this was written; it has been **21 since 2026-08-20**.)* The agent was renamed `sector-calendar-refresher` → **`sector-signal-refresher`**. (Filename kept for link stability; content generalized.)

**Department:** Sector (01) · **Status:** Agent spec **built** 2026-08-11, **broadened 2026-08-15** (`.claude/agents/sector-signal-refresher.md`, advisory, registered in the runtime; loop wired to `sector-intelligence-mapper` via `CALENDAR_UPDATED` + `sector-readiness-analyst` via `REGULATORY_CHANGE`; `DEMAND_SHIFT`/`COMPRESSION_EVENT`/`COMPETITOR_MOVE` emitted-but-not-yet-subscribed, Contract §8). **Not yet armed as a live routine.** Key finding (§5a): a claude.ai cloud routine has **no web access**, so the honest unattended form is a **comment-posting staleness watchdog** (flags what's due + where to check it), **never** an unattended date/number-writer — that would fabricate. Runs manual/advisory today; ready to arm as the comment-watchdog form pending the owner's go + an `AUTOMATION_APPROVAL_MATRIX.md` row.
**Purpose:** Keep the **Sector Signals (Commercial Intelligence Calendar)** Notion DB accurate and commercially interpreted in *real time* (= a freshness cadence, not a live stream) — re-verify signal dates against authoritative sources, surface newly-announced signals and regulatory deadlines, flag delays/cancellations, **propose the commercial interpretation** (impact + lead-time + routing), and **propagate material changes into Sector Intelligence + readiness**. The signal layer is a living intelligence surface, not a static table (Draft 8 + SCIC doctrine + owner's real-time directive).

> Governing rule: **no invented dates.** Every dated entry must trace to an authoritative source (the body that runs it) and carry `Last Verified` + `Refresh Status`. Unverifiable dates are marked `Needs verification`, never guessed.

---

## 1. What already exists (this feeds the engine)

- **DB:** `Sector Calendar (Market Events)` — `collection://c14fedb3-6048-4bc5-8a40-6558cc985f57` (under the SectorOS parent page). Enhanced 2026-08-11 with: **Sector** (color-coded select, for multi-sector overlay), **Calendar Type** (the 7 Draft-8 layers), **Authoritative Source**, **Source URL**, **Last Verified**, **Refresh Status** (`Confirmed / Annual-recurring / Needs verification / Superseded/Delayed`).
- **The 7 layers (Draft 8), with their authoritative drivers:**
  1. **Regulatory** ⭐ — the date-certain, budget-moving deadlines: CSRD/ESRS (EU Commission/EFRAG), FSMA 204 (US FDA), HIPAA (HHS/OCR), SOC 2 (AICPA), PCI DSS (PCI SSC), SEC climate. *Highest leverage.*
  2. **Event** — where decision-makers gather (Sheet 10's real conferences: HIMSS, RSA, Money20/20, GDC, CSCMP EDGE, ITC, BIO, HLTH…).
  3. **Demand** — buying-season windows (Q4 budget, fiscal year-end).
  4. **Financial** — fiscal years, funding cycles, procurement windows.
  5. **Operational** — internal product/inventory/hiring cycles.
  6. **Content/Media** — campaign + publishing rhythms.
  7. **Innovation/Trend** — tech-release cadences.
- **Real source of WHO/WHERE:** xlsx Sheet 10 (`10 EVENTS & COMMUNITIES`) — owner-curated events + communities + entry strategy per sub-sector. This is the seed list the engine keeps dated + fresh.
- **Loaded so far (2026-08-11, web-verified): 24 entries** — 10 flagship events + 2 date-certain regulatory drivers (CSRD Omnibus delay, FSMA 204 delay) + **12 sector-anchor events** giving every one of the 20 sectors ≥1 real future-dated anchor (all `Confirmed`; anchors chosen future-of-Aug-2026). See the DB. Remaining: the secondary Sheet-10 events per sub-sector + the 5 non-Event layers (add as dates verify).

## 2. The refresh loop (per run)

```
TRIGGER → SELECT entries due for re-verification → for each:
  retrieve Authoritative Source (web) → compare to stored Date/Window →
    if changed materially (date moved, delayed, cancelled, new edition):
        update Date + Last Verified + Refresh Status
        EMIT event (CALENDAR_UPDATED; REGULATORY_CHANGE for the Regulatory layer)
    else: bump Last Verified, keep Confirmed
  ALSO: discover newly-announced events/deadlines for active sub-sectors →
        insert with Authoritative Source + Refresh Status
→ REPORT changes → route to Sector Intelligence + Readiness
```

### 2a. Selection policy — the proximity escalation ladder *(upgraded 2026-08-19, LSEI)*

The original two-band policy (near-term weekly / mid-term monthly) under-watches the window where a date change does the most damage: the last 30 days, when campaigns are already live and money is already committed. Replaced by a **proximity ladder** — monitoring intensity rises as the signal approaches, so effort is spent where a change is both most likely to appear and most expensive to miss.

| Time to `Signal Date` | Monitoring level | Re-verify |
|---|---|---|
| > 180 days | Normal | Monthly |
| 180 – 90 days | Elevated | Fortnightly |
| 90 – 30 days | High | Weekly |
| < 30 days | **Critical** | Every run |
| < 7 days | **Critical** | Every run — *and a change escalates immediately* |

**Overrides (these win over the ladder):**
- `Needs verification` → every run, until resolved.
- `Superseded/Delayed` → every run, until a new date is confirmed or the signal is closed.
- **Regulatory** and **Economic** → at least monthly regardless of distance; they move rarely, and when they move they move budgets (FSMA 204, CSRD Wave 2).
- **`Source Tier` drives a floor, not just the ladder:** `T3`/`T4`-sourced signals are re-verified at **one level higher** than their distance implies, and cannot reach `Confirmed` without a T1/T2 source (`CALENDAR_INTELLIGENCE.md` §2). *This is the rule that would have caught the Hospitality seasonality rows sourced to vendor blogs.*
- **`Annual-recurring`** → verified once per cycle at the T-180 boundary, when next year's edition is normally published. Never auto-rolled forward — a recurring event is a **prediction** until its next edition is published.

**Source-side cadence (DB 14, new).** The ladder above governs *signals*; each **`Signal Sources`** row separately carries its own `Cadence` + `Next Verification`, because a publisher can go stale independently of any single event. `Last Synced ≠ Last Verified` — a feed can keep delivering while the body behind it has moved, renamed, or stopped maintaining the calendar.

### 2b. Change-history write rule *(added 2026-08-19, LSEI)*

A moved date **must not silently overwrite** the old one. On any material change (moved · cancelled · postponed · venue changed · new edition):

1. `Previous Signal Date` ← the prior value; `Change Reason` ← what changed + the confirming source.
2. Append a dated line to the signal's page body: *what changed · when · which source · what tier.*
3. Set `Change Status` + `Refresh Status`.
4. **Name what it invalidates** — affected Market Routes, Content Opportunities, campaign windows, derived activation dates, agency-calendar entries (Contract §15). This is the step that makes the calendar an operating system rather than a table.
5. Emit the matching event (§3).

## 3. Propagation — why "the update determines the whole intelligence"

A material calendar change is itself sector intelligence. On `REGULATORY_CHANGE` / `CALENDAR_UPDATED`, the engine writes a **Sector Intelligence** finding (Category = `Risk/Fragility` or `Strategic Node`) and flags the affected sub-sector's **readiness** for re-scoring. Worked example already in the data: **FSMA 204 slipped Jan 2026 → Jul 2028** and **CSRD Wave 2 slipped to 2028** — both reduce the near-term AgriTech/FoodTech/EnergyTech urgency that Sheet 11 readiness leaned on. That is the calendar → intelligence → leverage loop, live.

Emits (reuse the runtime event bus): `CALENDAR_UPDATED` → `sector-intelligence-mapper` (01); `REGULATORY_CHANGE` → `sector-readiness-analyst` (01).

> 🔴 **Corrected 2026-08-24.** This line previously also listed `content-intelligence-hub` (04) and `sales-lead-qualification` (05) as subscribers. **Neither agent subscribes to these events** — verified by grepping every `on:` trigger across all 115 agent files. Both events reach only Sector's own agents and **never leave the department**, so the "calendar → intelligence → leverage loop" described above closes *within* Sector and does not currently reach Content or Sales. Ground truth: [`SECTOR_EVENT_CATALOG.md`](SECTOR_EVENT_CATALOG.md) §3.

## 4. Agent spec (to build)

> **Built** — the live spec is `.claude/agents/sector-signal-refresher.md`. Summary frontmatter:

```yaml
name: sector-signal-refresher
department: "01"
description: Monitors the Sector Signals DB — re-verifies all 21 signal types, flags stale/moved/delayed/new, proposes commercial-impact + lead-time + downstream routing. Advisory.
model: claude-opus-4-8
execution: prompt
risk_class: 2            # WRITES to an external system (Notion) → needs approval-matrix row before unattended
requires_human_approval: true    # advisory until the write path is approved
triggers:
  - type: manual
  - type: schedule
    cron: "0 7 * * 1"    # weekly near-term sweep (illustrative)
  - type: schedule
    cron: "0 7 1 * *"    # monthly full + regulatory/economic sweep
inputs: { scope: { type: string } }   # e.g. "next-90-days" | "regulatory" | a Signal Type | sub-sector id
emits: [CALENDAR_UPDATED, REGULATORY_CHANGE, DEMAND_SHIFT, COMPRESSION_EVENT, COMPETITOR_MOVE]
memory_stream: 01_Sector/_memory/runtime.jsonl
```

## 5. Governance (Draft 13 doctrine)

- **This agent writes to Notion → external state change.** Before it runs unattended it REQUIRES a row in `00_Agency_Governance/AUTOMATION_APPROVAL_MATRIX.md` (Trigger · Action · Risk Class 2 · Rollback = revert to prior Date/Refresh Status · Fallback = mark `Needs verification` · Log destination = `runtime.jsonl` · Human gate · Last verified · Detection = "how do we know it stopped?"). Until then it runs **advisory** (proposes updates for human apply).
- **No fabrication gate:** an update only writes a date it retrieved from the Authoritative Source this run; otherwise it sets `Needs verification` and reports the gap. VALIDATE source before write.
- **Escalation:** a Regulatory change that flips a sub-sector's readiness tier escalates to the owner (it changes GTM sequencing).

## 5a. 🔴 What "the live form" can honestly be — the web-access finding (2026-08-11)

Verified against the one live, healthy cloud routine on the account (`trig_01WyyrXEkFZck1D49tm6BfKv`, Design Creative Pipeline — `enabled`, last fired 2026-08-11): **a claude.ai cloud routine's session has `allowed_tools: [Bash, Read, Write, Edit, Glob, Grep]` and a Notion connector — and NO web access** (no WebSearch, no WebFetch, no browser). That single fact governs what an unattended calendar refresher can be, because this agent's whole job depends on *verifying dates against authoritative web sources*:

- ❌ **Cannot** be an unattended "verify-the-web-and-write-the-date" routine. In an environment with no web, "verify" would collapse into "guess" — which violates the calendar's one sacred rule (**no invented dates**; "we are not making up any calendars").
- ✅ **Can** be an unattended **staleness watchdog + re-verification prompter** — structurally identical to the proven Creative Pipeline pattern (draft + recommend + comment; a human applies). Each run it: reads the Notion calendar, finds entries whose `Last Verified` is stale (per the §2 selection policy) or marked `Needs verification`, and **posts a Notion comment** listing exactly which entries are due and *where to check each* (`Authoritative Source` + `Source URL`). It writes **comments, never dates.** A human — or Claude Code in an interactive session *with* web tools — then does the actual verify + write + event-emit.

So the honest "live" promotion is a self-running *surveillance* of calendar freshness, not a self-writing calendar. It is genuinely unattended and genuinely incapable of fabricating a committed date. The date-write step stays a **manual apply** (matches `SECTOR_NOTION_SCHEMA.md` §7). If a future cloud environment grants web access to the routine, this can be revisited — but only with the no-fabrication gate proven, and a new matrix row.

**Status of promotion (decided 2026-08-11): stays MANUAL — not armed.** The owner chose to keep the refresher manual rather than put a second always-on routine on the account. So: no `RemoteTrigger` is created, and **no `AUTOMATION_APPROVAL_MATRIX.md` row is added** (correct per matrix doctrine — no live row for an automation that isn't running). Freshness sweeps are run on demand: `arika run sector-signal-refresher` for the advisory proposal, or Claude Code in an interactive session (which *has* web tools) to verify + apply. The honest comment-watchdog form above remains **ready to arm** if the owner later wants it — at which point its matrix row is written on arm.

## 6. File-design fields (per Draft 13)
Purpose §Purpose · Authority: subordinate to `SECTOR_ACTIVATION_CONTRACT.md` + the Constitution · Inputs §4 · Outputs: updated calendar rows + emitted events + intelligence findings · Rules §1/§5 · Failure: stale/unreachable source → `Needs verification`, never invent · Escalation §5 · Examples §3 (FSMA 204 / CSRD).
