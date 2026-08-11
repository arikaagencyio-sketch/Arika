# Sector Calendar — Real-Time Refresh Engine (Spec)

**Department:** Sector (01) · **Status:** Agent spec **built** 2026-08-11 (`.claude/agents/sector-calendar-refresher.md`, advisory, registered in the runtime; loop wired to `sector-intelligence-mapper` via `CALENDAR_UPDATED` + `sector-readiness-analyst` via `REGULATORY_CHANGE`). **Not yet a live auto-writer** — the unattended cloud-routine form (writes to Notion) needs an `AUTOMATION_APPROVAL_MATRIX.md` row first. Runs manual/advisory today.
**Purpose:** Keep the **Sector Calendar (Market Events)** Notion DB accurate in *real time* — re-verify event dates against authoritative sources, surface newly-announced events and regulatory deadlines, flag delays/cancellations, and **propagate material changes into Sector Intelligence + readiness**. The calendar is a living intelligence surface, not a static table (Draft 8 + owner's real-time directive).

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
- **Seeded so far (2026-08-11, web-verified):** 10 flagship events + 2 date-certain regulatory drivers (CSRD Omnibus delay, FSMA 204 delay). See the DB.

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

```yaml
name: sector-calendar-refresher
department: "01"
description: Re-verifies Sector Calendar dates against authoritative sources and propagates material changes to Sector Intelligence + readiness. Advisory-first.
model: claude-opus-4-8
execution: prompt
risk_class: 2            # WRITES to an external system (Notion) → needs approval-matrix row
requires_human_approval: false   # advisory until the write path is approved
triggers:
  - type: manual
  - type: schedule
    cron: "0 7 * * 1"    # weekly near-term sweep (illustrative)
  - type: schedule
    cron: "0 7 1 * *"    # monthly full + regulatory sweep
inputs: { scope: { type: string } }   # e.g. "next-90-days" | "regulatory" | sub-sector id
emits: [CALENDAR_UPDATED, REGULATORY_CHANGE]
memory_stream: 01_Sector/_memory/runtime.jsonl
```

## 5. Governance (Draft 13 doctrine)

- **This agent writes to Notion → external state change.** Before it runs unattended it REQUIRES a row in `00_Agency_Governance/AUTOMATION_APPROVAL_MATRIX.md` (Trigger · Action · Risk Class 2 · Rollback = revert to prior Date/Refresh Status · Fallback = mark `Needs verification` · Log destination = `runtime.jsonl` · Human gate · Last verified · Detection = "how do we know it stopped?"). Until then it runs **advisory** (proposes updates for human apply).
- **No fabrication gate:** an update only writes a date it retrieved from the Authoritative Source this run; otherwise it sets `Needs verification` and reports the gap. VALIDATE source before write.
- **Escalation:** a Regulatory change that flips a sub-sector's readiness tier escalates to the owner (it changes GTM sequencing).

## 6. File-design fields (per Draft 13)
Purpose §Purpose · Authority: subordinate to `SECTOR_ACTIVATION_CONTRACT.md` + the Constitution · Inputs §4 · Outputs: updated calendar rows + emitted events + intelligence findings · Rules §1/§5 · Failure: stale/unreachable source → `Needs verification`, never invent · Escalation §5 · Examples §3 (FSMA 204 / CSRD).
