# A001 — Bounded agency-systems test plan

**Department:** Sector (01) — owns this record.
**Status:** 🟡 **Planning only.** This plan approves, schedules and runs nothing. Every test needs its own owner decision.
**Version:** v0.2 *(v0.1 corrected 2026-09-21 — see §9)*
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

## 3. What actually blocks a runtime test

> ⚠️ **Corrected 2026-09-21 (v0.2).** v0.1 said the blocker was the missing sandbox
> stream (R2/R3) rather than the API key. **That was wrong in its causation.** The governing bar
> is a **decision**, not a missing mechanism.

**The bar, in order of precedence:**

| # | Bar | What it says | Can a build lift it? |
|---|---|---|---|
| **1** | **D15 (B1) — Phase 3 run mode** | *"No-runtime, document-only first … **No `arika run`, agent, skill, scheduler or event activity, and no runtime memory write**."* | ❌ **No.** Only a new owner decision superseding D15 |
| **2** | **D6 — Tier-1 deferred** | T1-1…T1-5 are deferred, and **R2 *is* T1-5** | ❌ **No.** Building R2 requires amending D6 first |
| **3** | **R2 (AG-12 / T1-5)** | No sandbox memory stream or marker exists | Necessary, **not sufficient** |
| **4** | **R3 (AG-13 / T1-4)** | No sandbox marker in skill execution records | Necessary for **skill** runs, not sufficient |
| **5** | **Replacement API key unverified by use** | Rotation is owner-attested; validity is not proven | Necessary, **not sufficient** |

> 🔴 **R2 alone could never authorise an A001 agent or skill run.** D15 bars run-mode
> activity outright and says so in those exact terms; D6 keeps the build itself deferred. R2 and
> R3 are **preconditions that become relevant only after** D15 and D6 are changed by the owner.

**Why isolation still matters.** Once D15 and D6 are lifted, the write behaviour in §2 takes
over: a run would put an **unmarked** line into the **shared** department stream,
indistinguishable from a real-pilot record. `02_Offer/_memory/runtime.jsonl` already holds 5 such
unmarked control-test lines — the defect R2 exists to fix, not a pattern to extend.

---

## 4. Test matrix

**Writes** column: `none` · `tracked log` (git-committed) · `new tracked file`.
**Result** is the *expected* outcome — a stop or unresolved is a **pass of the mechanism**, not a failure.

### 4.1 Sector (01)

| # | Component · input source | Mechanism tested | Expected | Mode | Writes | Approval | Now? |
|---|---|---|---|---|---|---|---|
| ~~**S-1**~~ | ⛔ **WITHDRAWN 2026-09-21 — duplicates work already done.** Queue item **O1 was implemented 2026-09-16**: the evaluation-order rule is recorded in `A001_DOCUMENT_ONLY_PILOT_CLOSEOUT.md` §2, with the `OFFER_OS.md` §15 pointer. v0.1 proposed re-recording it | — | — | — | — | — | ⛔ **No — already done** |
| **S-1a** | **Verification read** of the implemented O1 rule · closeout §2 + `OFFER_OS.md` §15 | The rule is present, worded as **evaluation order**, and not extended into ICP/demand/pricing (D20) | **PASS** | Doc-only (**read only, genuinely zero-write**) | none | None | ✅ **Yes** |
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

> ⚠️ **Corrected 2026-09-21 (v0.2).** v0.1 listed **S-1** as safe-now with
> *"writes: none"* while its stated output was *"one sentence recorded in Sector-owned
> documentation"* — **a git-tracked repository write**. The row contradicted its own
> column. S-1 is withdrawn as a duplicate; **S-1a** replaces it and is genuinely read-only.

**Safe now — 11 checks, all document-only or non-runtime. None writes anything:**
S-1a · S-2 · S-3 · O-1 · O-2 · C-1 · M-1 · SA-1 · G-1
· G-2 · G-3

> **"Zero writes" means zero writes.** Any test whose output is a recorded sentence is a
> **write**, needs its own owner approval, and is counted as such — not filed under
> document-only.

**Blocked — every runtime-backed test, and one skill test:**

| Bar | Blocks | Lifted by |
|---|---|---|
| **D15** — no agent/skill/runtime activity for A001 Phase 3 | **all of** S-4, S-5, O-3, O-4, C-2, M-2, SA-2 | A new owner decision superseding D15 |
| **D6** — T1-1…T1-5 deferred | the R2/R3 builds themselves | An owner amendment to D6 |
| **R2 / R3** — no sandbox stream or skill marker | the same tests, *after* D15/D6 | The build in §6.1 |
| **RD6** — no downstream agent runs | C-2, M-2, SA-2 | A separate RD6 decision |
| **D20** — barred content classes | S-6, O-5 | ⛔ Never, from A001 |
| **Key unverified by use** | every runtime test | An approved verification run |

---

## 6. The smallest path to live mechanism testing

**A separate `TEST_FIXTURE` runtime lane is feasible.** It is a small, contained change —
the obstacle is decision-order, not engineering.

### 6.1 Minimum code changes

| File | Change |
|---|---|
| `arika-runtime/src/executor.ts` | Add `fixture?: boolean` and `memoryStreamOverride?: string` to `RunContext`; pass both into `finalizeRun()` |
| `arika-runtime/src/memory-writer.ts` | Honour the override; stamp `classification: "TEST_FIXTURE"` into the envelope; **fail closed** — if `fixture` is set and the resolved path is not a sandbox stream, **throw and write nothing** |
| `arika-runtime/src/triggers/cli.ts` | Add `--fixture` to `arika run` |
| `arika-runtime/tests/*.test.mjs` | Four assertions: a fixture run writes **only** to the sandbox path · the envelope carries the marker · a fixture run aimed at a real stream **throws** · a normal run is byte-identical to today |

**Stream naming:** `<dept>/_memory/sandbox.jsonl` — never `runtime.jsonl`. A distinct
filename means isolation survives a careless `cat`, a grep, or a future reader who does not know
the marker exists.

**Skill runs (R3) are a separate, later change** to the `skill_runs.jsonl` payload. Keeping skills
out of the first lane makes the first decision smaller.

### 6.2 Minimum record changes

- **Sandbox record §5.1** — a new decision superseding **D15** *for the bounded fixture
  lane only*, leaving document-only as the default everywhere else; and an amendment to **D6**
  un-deferring **T1-5** only.
- **§7** — AG-12 row updated; AG-13 left open.
- **Queue §7** — R2 status; R3 explicitly still deferred.
- **`TECHSTACK_OS.md` §3** — register the lane once verified live.
- **This plan** — re-audit the matrix against the new decisions.

### 6.3 Owner decisions required before the first run

1. **Supersede D15** for a bounded `TEST_FIXTURE` lane — A001 only.
2. **Amend D6** to un-defer **T1-5** (the memory stream). T1-4 stays deferred unless skills are in scope.
3. **Approve verifying the replacement API key by use** — itself a runtime call.
4. **Approve the fail-closed rule**: a fixture run may never write to a real-pilot stream.
5. **Approve the specific first test and its exact input** (§6.4).

**None of these is granted by D16's closure.** The credential condition being met authorised no
A001 runtime work, and still does not.

### 6.4 One concrete first runtime test — for approval **after** isolation exists

| | |
|---|---|
| **Component** | `offer-orchestrator` · `arika run offer-orchestrator --fixture` |
| **Input** | `A001-P07` **pilot ID only**, plus the archetype, destination profile and H-band already recorded in the sandbox record. **Explicitly non-pricing.** No real property name — A001-P07 *is* a simulated unit |
| **Mechanism** | Seed-sufficiency routing, and that the **group flags reach the orchestrator** |
| **Expected** | **`needs_more_seed_data`** or **`reject`** — a **stop is the pass**. Phase 11 **BLOCKED**; `add_new_offer` / `update_existing_offer` authorise **no** registry change |
| **Writes** | Exactly one line to `02_Offer/_memory/sandbox.jsonl`, carrying `classification: TEST_FIXTURE` — and **nothing** in `runtime.jsonl` |
| **Refutes** | That the lane leaks. If any byte lands in a real stream, the lane has failed and the run is void |

**Not approved and not run.**

### 6.5 Non-runtime checks available immediately

No decision needed beyond a nod; none writes anything:

- **S-1a** — confirm O1's rule is present and still bounded to evaluation order
- **O-2** — confirm an agent's own `requiresHumanApproval: true` reaches the top level
- **O-1** — confirm registry actions authorise no registry change
- **G-2** — trace PG0–PG5 stop rules against A001 fixtures
- **G-3** — D20 boundary check over every proposed finding
- **S-2 / G-1** — the two existing gates

---

## 7. Safeguards that remain in force

1. **A001 stays `TEST_FIXTURE`** and is never a prospect, CRM record or Offer evidence (D17).
2. **D20 bars** demand, seasonality, guest mix, pricing, competitors, capacity, performance figures, and any *"a property like this would…"* claim.
3. **Group flags and stop rules are preserved** — no unit-level pass is promoted to eligibility.
4. **`PILOT-H-001` stays reserved**; no A001 unit is relabelled.
5. **D15 bars all A001 agent, skill, scheduler and event activity** — no runtime test proceeds until the owner supersedes it **and** an isolated, marked stream exists.
6. **D6 keeps T1-1…T1-5 deferred** — the isolation build cannot start until D6 is amended.
7. **The Full Push Readiness Packet's readiness and PG gates are untouched** by this plan.
8. **The replacement API key stays unverified by use** — verifying it is a runtime call and its own decision.

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

- 2026-09-21 — **v0.2. Audited against D6, D15, D17, D18 and D20; three factual errors in v0.1 corrected.** **(1) S-1 duplicated work already done** — queue item **O1 was implemented 2026-09-16**, as the evaluation-order rule in `A001_DOCUMENT_ONLY_PILOT_CLOSEOUT.md` §2 with the `OFFER_OS.md` §15 pointer. The queue row was never marked done, which is what v0.1 misread; the implementation was there all along. S-1 is **withdrawn** and replaced by **S-1a**, a read-only verification that the rule is present and still bounded to evaluation order. **(2) S-1 contradicted its own “zero writes” column** — it was filed document-only with *writes: none* while proposing to record a sentence in a git-tracked file. §5 now states plainly that a recorded sentence **is** a write and needs its own approval. **(3) The blockers were mis-attributed.** v0.1 named R2/R3 as what blocks runtime testing. The governing bar is **D15**, which forbids *“`arika run`, agent, skill, scheduler or event activity”* for A001 Phase 3 in those exact terms, and **D6**, which keeps the R2 build itself deferred. **R2 alone could never authorise an A001 agent or skill run** — it is a precondition that matters only after the owner changes D15 and D6. §3 and §5 are rewritten accordingly. **Added §6:** the smallest path to a live `TEST_FIXTURE` lane — feasible, four code touches, fail-closed, with a distinct `sandbox.jsonl` filename so isolation survives a careless read; plus the record changes, the five owner decisions, one concrete first runtime test, and the non-runtime checks available now. **The v0.1 entry below stands as written.** Nothing was implemented or run; no agent, skill, API or connector called; no memory log, Drive file or CRM record created; no secret read; the Full Push Readiness Packet and its PG gates untouched. — Claude Code (Opus 5)
- 2026-09-21 — **v0.1 created.** A bounded agency-systems test plan over the existing A001 group and units — **planning only, nothing approved or run**. Built after reading the runtime's actual write behaviour rather than assuming it: `finalizeRun()` writes memory **unconditionally**, the line carries the **full input**, every relevant agent declares a `memory_stream`, and three department logs would be **created** by a first run. **Central finding: the isolation the owner requires does not exist yet** — R2/R3/R5 (sandbox stream, skill marker, test-fixture trust) are all deferred under D6, so a runtime A001 run would write an **unmarked** line into a shared department stream. That, not the API key, is what blocks every runtime test. **11 document-only or non-runtime tests are safe now; every runtime-backed test is blocked.** First test recommended: **S-1**, the group-flag inheritance rule (queue O1) — zero-write, zero-runtime, and directly protective of the rule that P07's unit passes are **not** Offer eligibility. No agent, skill, API or connector was called; no memory-log entry, Drive file or CRM record was created; no `.env` or key value was read; the Full Push Readiness Packet's readiness and PG gates were not changed. — Claude Code (Opus 5)
