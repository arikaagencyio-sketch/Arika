# A001 — Bounded agency-systems test plan

**Department:** Sector (01) — owns this record.
**Status:** 🟡 **Planning only.** This plan approves, schedules and runs nothing. Every test needs its own owner decision.
**Version:** v0.1
**Date:** 2026-09-21
**Scope bound:** **D20 — mechanism findings only.** Nothing here may produce a market, demand, buyer, pricing, capacity or proof claim.

---

## 1. What this is, and what it is not

This is a **simulation / mechanism test plan** built on the existing **A001** group and its units **A001-P01…A001-P09**.

- ❌ **Not the real-property push.** The Full Push Readiness Packet's readiness and PG gates are **untouched** by this plan.
- ❌ **No A001 unit is relabelled `PILOT-H-001`.** `PILOT-H-001` stays reserved for the first real, owner-supplied property (RD1).
- ❌ **No property is requested or manufactured.**
- ✅ **A001 stays `TEST_FIXTURE`**, isolated from real-pilot records.
- ✅ **Group flags and stop rules are preserved exactly.** A unit passing every unit-level check is **still not Offer-eligible** while a group flag stands.

> 🔴 **P07's unit-level passes are not Offer eligibility.** They record that a *mechanism* ran, nothing more.

---

## 2. Verified runtime behaviour — checked before any runtime test was proposed

Read from source on 2026-09-21. These facts constrain the whole matrix.

| Fact | Evidence | Consequence |
|---|---|---|
| **Every agent run writes a memory line** | `arika-runtime/src/executor.ts` — `finalizeRun()` calls `writeMemory()` unconditionally | **There is no dry-run and no `--no-memory` flag** |
| **The line carries the full input** | `memory-writer.ts` — the payload includes `input` and `recommendation` verbatim | Anything in `--input` becomes permanent repository history |
| **Only a spec with no `memory_stream` escapes it** | `writeMemory()` returns `null` when `spec.memory_stream` is absent | **Every** Sector / Offer / Content / Marketing / Sales agent checked declares one — so **no runtime test avoids a write** |
| **The write happens after the model call** | `finalizeRun()` runs post-response | A failed key still costs an API call before anything is logged |
| **Three department logs do not exist yet** | `01_Sector`, `03_Marketing`, `04_Content` memory logs are absent | A first run there **creates a new git-tracked file**, not just a line |
| **Skill runs are Claude-Code-written, not runtime-written** | All 15 lines in `01_Sector/_memory/skill_runs.jsonl` carry `source: claude-code` | A skill test needs **no API key and no runtime** — but still writes a **git-tracked** line |
| **Memory logs are tracked, not ignored** | `git check-ignore` returns nothing; `git ls-files` matches | Every line is committed by the auto-sync hook |

---

## 3. The blocking finding — isolation does not exist yet

The owner's requirement is that A001 runtime output stay **marked `TEST_FIXTURE` and isolated from real-pilot records**. Today that is **not possible**:

| Item | What it would provide | Status |
|---|---|---|
| **R2 · AG-12 / T1-5** | A sandbox memory stream, or shared-stream markers | ⛔ **Deferred under D6** |
| **R3 · AG-13 / T1-4** | A sandbox marker field in skill execution records | ⛔ **Deferred under D6** |
| **R5 · AG-11 / T1-3** | A test-fixture trust value on knowledge objects | ⛔ **Deferred under D6** |

> **So a runtime-backed A001 run today would write an unmarked line into the *shared department stream*, indistinguishable from a real-pilot record.** That is exactly what the isolation requirement forbids.
>
> This is the real blocker — **not** the API key. The credential condition (D16 · AG-19) is owner-attested closed as of 2026-09-21, and closing it authorised no A001 runtime work.

**Precedent, and why it is a caution rather than a licence:** `02_Offer/_memory/runtime.jsonl` already holds 5 unmarked control-test lines. That is the defect R2 exists to fix, not a pattern to repeat.

---

## 4. Test matrix

**Writes** column: `none` · `tracked log` (git-committed) · `new tracked file`.
**Result** is the *expected* outcome — a stop or unresolved is a **pass of the mechanism**, not a failure.

### 4.1 Sector (01)

| # | Component · input source | Mechanism tested | Expected | Mode | Writes | Approval | Now? |
|---|---|---|---|---|---|---|---|
| **S-1** | **Group-flag inheritance** (queue O1) · sandbox §6 group flags + P07 unit verdicts | Group flags inherit to every unit and are never suppressed | **PASS** — unit passes do not confer eligibility | Doc-only | none | Owner nod to record one sentence | ✅ **Yes** |
| **S-2** | `sector_truth_gate.py` · repo files | Prose agrees with disk, contracts, AEIT_11 | **PASS** | Non-runtime | none | None — already routine | ✅ **Yes** |
| **S-3** | **S10 hand-off packet schema** · `.claude/skills/sector-handoff-packet` + A001's recorded packet | Packet conforms to its own schema; confidence carries the weakest item | **PASS** | Doc-only (read) | none | None | ✅ **Yes** |
| **S-4** | `sector-offer-router` skill · A001-P07 fixture | Routing decision + hand-off emission | **STOP** — group flag stands | Skill (Claude Code) | **tracked log** | Owner + **R3 marker** | ⛔ **Blocked — R3** |
| **S-5** | `sector-icp-fit` agent · A001-P07 fixture | Company-fit classification | **UNRESOLVED** — AG-17: no Sector agent fits a hotel | Runtime | **new tracked file** | Owner + **R2** | ⛔ **Blocked — R2, AG-17** |
| **S-6** | `sector-place-profiler` · destination profile (queue S1) | Profile authoring | — | Doc-only | none | Owner decision | ⛔ **Blocked** — content must come from real sources; A001 cannot supply (D20) |

### 4.2 Offer (02)

| # | Component · input source | Mechanism tested | Expected | Mode | Writes | Approval | Now? |
|---|---|---|---|---|---|---|---|
| **O-1** | **Registry-action semantics** · `offer-orchestrator` spec + packet RD7 | `add_new_offer` / `update_existing_offer` authorise **no** registry change | **PASS** | Doc-only (read) | none | None | ✅ **Yes** |
| **O-2** | **Approval-flag propagation** · `governance.ts` + `finalizeRun()` | An agent's own `requiresHumanApproval: true` reaches the top level | **PASS** — the control test's dropped-flag defect was fixed | Doc-only (code read) | none | None | ✅ **Yes** |
| **O-3** | `offer-orchestrator` · A001-P07 structural seed | Seed sufficiency routing | **`needs_more_seed_data`** or `reject` | Runtime | **tracked log** | Owner + **R2** | ⛔ **Blocked — R2** |
| **O-4** | `offer-oeos-engineer` · orchestrator output | Structural continuation under RD7 | Structural only; Phase 11 **BLOCKED** | Runtime | **tracked log** | Owner + **R2** + PG3 | ⛔ **Blocked — R2** |
| **O-5** | `offer-pricing-floor-analyst` | — | — | — | — | — | ⛔ **Excluded** — RD5 skips pricing; **D20 bars pricing from A001** |

### 4.3 Content (04) · Marketing (03) · Sales (05)

| # | Component · input source | Mechanism tested | Expected | Mode | Writes | Approval | Now? |
|---|---|---|---|---|---|---|---|
| **C-1** | **Hand-off note format** · RD6 rules | Notes carry an *angle*, never an artifact or performance claim (S10 boundary law) | **PASS** | Doc-only | none | None | ✅ **Yes** |
| **C-2** | `content-intelligence-hub` · A001 fixture | 5-source intelligence assembly | **UNRESOLVED** — insufficient real sources | Runtime | **new tracked file** | Owner + **R2** | ⛔ **Blocked — RD6 bars downstream agent runs** |
| **M-1** | **Sector → Marketing route gap** (item 31k) · dept OS files | The documented gap is real and unclosed | **PASS** (gap confirmed) | Doc-only | none | None | ✅ **Yes** |
| **M-2** | `marketing-market-intelligence` · A001 fixture | Market-signal intake | **UNRESOLVED** | Runtime | **new tracked file** | Owner + **R2** | ⛔ **Blocked — RD6** |
| **SA-1** | **Sales route shape** · dept OS files | Sales is event-only with no delivery path | **PASS** (gap confirmed) | Doc-only | none | None | ✅ **Yes** |
| **SA-2** | `sales-lead-qualification` · A001 fixture | Lead qualification | **STOP** — A001 is not a prospect (D17) | Runtime | **tracked log** | Owner + **R2** | ⛔ **Blocked — RD6; would imply a lead** |

### 4.4 Gates and hand-offs

| # | Component | Mechanism tested | Expected | Mode | Writes | Now? |
|---|---|---|---|---|---|---|
| **G-1** | `estate_event_gate.py` | Orphaned waits classified; runtime does not publish | **PASS** | Non-runtime | none | ✅ **Yes** |
| **G-2** | **PG0–PG5 stop-rule trace** · packet §6 vs A001 fixtures | Each gate's stop condition fires where it should | **PASS** | Doc-only | none | ✅ **Yes** |
| **G-3** | **D20 boundary test** · queue §8 | Every proposed finding is checked against the six barred classes | **PASS** | Doc-only | none | ✅ **Yes** |

---

## 5. Safe now vs blocked

**Safe now — 10 tests, all document-only or non-runtime, none writes anything:**
S-1 · S-2 · S-3 · O-1 · O-2 · C-1 · M-1 · SA-1 · G-1 · G-2 · G-3

**Blocked — every runtime-backed test, and one skill test:**

| Blocker | Blocks |
|---|---|
| **R2 (AG-12 / T1-5)** — no sandbox memory stream or marker | S-5, O-3, O-4, C-2, M-2, SA-2 |
| **R3 (AG-13 / T1-4)** — no sandbox marker in skill records | S-4 |
| **RD6** — no downstream agent runs | C-2, M-2, SA-2 |
| **D20** — barred content classes | S-6, O-5 |
| **Replacement API key unverified by use** | every runtime test |

---

## 6. Recommended FIRST test — S-1

**The smallest useful test, and the one that guards the stated risk directly.**

- **Component:** group-flag inheritance rule (mechanism queue **O1**, triaged *"safe now"*).
- **Mode:** document-only. **No agent, skill, API, connector or runtime. No log line. No Drive file.**
- **Exact input:** read-only — the **A001 group flags** recorded in the sandbox record §6, and **A001-P07's** recorded unit-level verdicts in the same section. Nothing else is opened, and nothing is re-derived.
- **What it tests:** that group flags are **inherited by every unit and never suppressed**, so a unit passing every unit-level check is still **not Offer-eligible** while a group flag stands.
- **Expected output:** a **PASS/FAIL on whether the existing records already express the rule**, plus — if PASS — **one sentence** recorded in Sector-owned documentation. No Offer rule, band, gate or ICP definition changes.
- **Expected result:** **PASS.** A001 showed the routing behaving as designed; this records that it holds.
- **Why this one first:** it is the only proposed test that is simultaneously zero-write, zero-runtime, already triaged safe, and directly protective of *"P07's unit passes are not Offer eligibility."*

> ⚠️ **The only real D20 risk here is in the drafting.** The permitted sentence describes **routing logic**. It must not drift into any statement about a real hotel, group, destination, band or ICP.

**Not run.** This is a recommendation awaiting owner approval.

---

## 7. Safeguards that remain in force

1. **A001 stays `TEST_FIXTURE`** and is never a prospect, CRM record or Offer evidence (D17).
2. **D20 bars** demand, seasonality, guest mix, pricing, competitors, capacity, performance figures, and any *"a property like this would…"* claim.
3. **Group flags and stop rules are preserved** — no unit-level pass is promoted to eligibility.
4. **`PILOT-H-001` stays reserved**; no A001 unit is relabelled.
5. **No runtime test proceeds until R2/R3 give A001 a marked, isolated stream.**
6. **The Full Push Readiness Packet's readiness and PG gates are untouched** by this plan.
7. **The replacement API key stays unverified by use** — verifying it is a runtime call and its own decision.

---

## 8. Cross-references

- `01_Sector/A001_HOSPITALITY_SECTOR_SANDBOX.md` — group, units, flags, phase plan
- `01_Sector/A001_DOCUMENT_ONLY_PILOT_CLOSEOUT.md` — what the pilot proved, and §8's hard stop
- `01_Sector/A001_MECHANISM_IMPROVEMENT_QUEUE.md` — §7 runtime blockers, §8 D20 exclusions
- `01_Sector/A001_MECHANISM_QUEUE_TRIAGE.md` — O1 and F1 examined closely
- `02_Offer/Hospitality Revenue Content OS - Full Push Readiness Packet.md` — §3 allowed data, §6 gates (**not modified**)
- `arika-runtime/src/executor.ts`, `memory-writer.ts` — the verified write behaviour in §2

---

## 9. Changelog

- 2026-09-21 — **v0.1 created.** A bounded agency-systems test plan over the existing A001 group and units — **planning only, nothing approved or run**. Built after reading the runtime's actual write behaviour rather than assuming it: `finalizeRun()` writes memory **unconditionally**, the line carries the **full input**, every relevant agent declares a `memory_stream`, and three department logs would be **created** by a first run. **Central finding: the isolation the owner requires does not exist yet** — R2/R3/R5 (sandbox stream, skill marker, test-fixture trust) are all deferred under D6, so a runtime A001 run would write an **unmarked** line into a shared department stream. That, not the API key, is what blocks every runtime test. **11 document-only or non-runtime tests are safe now; every runtime-backed test is blocked.** First test recommended: **S-1**, the group-flag inheritance rule (queue O1) — zero-write, zero-runtime, and directly protective of the rule that P07's unit passes are **not** Offer eligibility. No agent, skill, API or connector was called; no memory-log entry, Drive file or CRM record was created; no `.env` or key value was read; the Full Push Readiness Packet's readiness and PG gates were not changed. — Claude Code (Opus 5)
