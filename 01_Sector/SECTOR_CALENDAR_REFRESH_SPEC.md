# Sector Signal — Real-Time Refresh Engine (Spec)

> **Evolved 2026-08-15 (SCIC Phase D):** this spec now governs the full **Sector Signal Refresh** — all 16 signal types + commercial-impact + lead-time + downstream routing, of which calendar-date re-verification is one facet. The agent was renamed `sector-calendar-refresher` → **`sector-signal-refresher`**. (Filename kept for link stability; content generalized.)

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

**Selection policy (real-time without waste):** near-term entries (next 90 days) re-verified weekly; 90–365 days monthly; regulatory deadlines monthly (they move rarely but matter enormously); `Needs verification` entries every run until resolved.

## 3. Propagation — why "the update determines the whole intelligence"

A material calendar change is itself sector intelligence. On `REGULATORY_CHANGE` / `CALENDAR_UPDATED`, the engine writes a **Sector Intelligence** finding (Category = `Risk/Fragility` or `Strategic Node`) and flags the affected sub-sector's **readiness** for re-scoring. Worked example already in the data: **FSMA 204 slipped Jan 2026 → Jul 2028** and **CSRD Wave 2 slipped to 2028** — both reduce the near-term AgriTech/FoodTech/EnergyTech urgency that Sheet 11 readiness leaned on. That is the calendar → intelligence → leverage loop, live.

Emits (reuse the runtime event bus): `CALENDAR_UPDATED` → `sector-intelligence-mapper` (01) + `content-intelligence-hub` (04, timing for campaigns); `REGULATORY_CHANGE` → `sector-readiness-analyst` (01) + `sales-lead-qualification` (05, timing triggers).

## 4. Agent spec (to build)

> **Built** — the live spec is `.claude/agents/sector-signal-refresher.md`. Summary frontmatter:

```yaml
name: sector-signal-refresher
department: "01"
description: Monitors the Sector Signals DB — re-verifies all 16 signal types, flags stale/moved/delayed/new, proposes commercial-impact + lead-time + downstream routing. Advisory.
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
