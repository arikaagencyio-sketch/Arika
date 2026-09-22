# A001 — Bounded agency-systems test plan

**Department:** Sector (01) — owns this record.
**Status:** 🟡 **Planning only.** This plan approves, schedules and runs nothing. Every test needs its own owner decision.
**Version:** v1.5 *(SECTOR-SF1's one S10 fixture run made and spent, 2026-09-22 — see §6.9; v1.4 corrected OFFER-F3's overclaim)*
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
| **0** | **D17 — A001 ratification** | *"It may not enter the **Offer runtime**, the Sector store, the CRM or any shared store"* — and `offer-orchestrator` **is** the Offer runtime | ❌ **No.** R2/T1-5, and any change to D6 or D15, **cannot override D17** — only an explicit, narrow amendment to D17 itself |
| **1** | **D15 (B1) — Phase 3 run mode** | *"No-runtime, document-only first … **No `arika run`, agent, skill, scheduler or event activity, and no runtime memory write**."* | ❌ **No.** Only a new owner decision superseding D15 |
| **2** | **D6 — Tier-1 deferred** | T1-1…T1-5 are deferred, and **R2 *is* T1-5** | ❌ **No.** Building R2 requires amending D6 first |
| **3** | **R2 (AG-12 / T1-5)** | No sandbox memory stream or marker exists | Necessary, **not sufficient** |
| **4** | **R3 (AG-13 / T1-4)** | No sandbox marker in skill execution records | Necessary for **skill** runs, not sufficient |
| **5** | **Replacement API key unverified by use** | Rotation is owner-attested; validity is not proven | Necessary, **not sufficient** |

> 🔴 **R2 alone could never authorise an A001 agent or skill run** — and neither could D6
> and D15 together. **D17 is the binding one**: it bars A001 from **the Offer runtime** by name,
> and a run through `offer-orchestrator` is exactly that. A build cannot lift a ratification.
>
> ⚠️ **v0.2 omitted D17 entirely.** Corrected here.

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
| **S-7** | **S10 `sector-handoff-packet` as a fixture** · a synthetic unit | Sector's only exit: packet assembly and per-destination outcomes | — | Skill (Claude Code) | **one marked record** in `01_Sector/_memory/skill_runs-sandbox.jsonl` and **one marked packet** in `01_Sector/fixtures/` — never `skill_runs.jsonl` | Sector decision **SECTOR-SF1** (enacted and **spent** 2026-09-22, `SECTOR_OS.md` §8) | ✅ **Run once 2026-09-22 — mechanism evidence only.** Offer, Content and CRM `not_attempted_fixture`; Sales, Marketing and Operations `HANDOFF_FAILURE`; nothing `delivered`; no write, no event. Isolation held: one marked record, one marked packet, `skill_runs.jsonl` byte-unchanged. No fit verdict; no retry. *(Was prepared and disabled; before that, blocked.)* **S-4 stays blocked**: the fixture mode is S10-only |

### 4.2 Offer (02)

| # | Component · input source | Mechanism tested | Expected | Mode | Writes | Approval | Now? |
|---|---|---|---|---|---|---|---|
| **O-1** | **Registry-action semantics** · `offer-orchestrator` spec + packet RD7 | `add_new_offer` / `update_existing_offer` authorise **no** registry change | **PASS** | Doc-only (read) | none | None | ✅ **Yes** |
| **O-2** | **Approval-flag propagation** · `governance.ts` + `finalizeRun()` | An agent's own `requiresHumanApproval: true` reaches the top level | **PASS** — the control test's dropped-flag defect was fixed | Doc-only (code read) | none | None | ✅ **Yes** |
| **O-3** | `offer-orchestrator` · A001-P07 `seed_brief` (§6.4) | Seed-sufficiency routing, and whether SR-1–SR-3 reach the orchestrator | **Returned `reject`** — observed, not predicted | Runtime — `TEST_FIXTURE` lane | **one line** in `02_Offer/_memory/sandbox.jsonl` | D21 | ✅ **RAN ONCE 2026-09-21 under D21 — complete; the authorisation is spent.** A successful stop-rule test (§6.8), not an eligibility result. **Not re-runnable** without a fresh decision |
| **O-4** | `offer-oeos-engineer` · orchestrator output | Structural continuation under RD7 — **only on `needs_more_seed_data`** | — | Runtime | **tracked log** | — | ⛔ **STOPPED for the A001-P07 sequence (2026-09-22).** The only orchestrator output that exists is D21's, and it returned **`reject`**. **`reject` stops the sequence** — packet PG3 (stop if `registry_action: reject`), R5 (stop on `reject`) and RD7 (*“a `reject` result stops the sequence”*). RD7's structural-only continuation exists **only for `needs_more_seed_data`**. **O-4 may not be fed by that output as a continuation**, whatever isolation or decision exists |
| **O-5** | `offer-pricing-floor-analyst` | — | — | — | — | — | ⛔ **Excluded** — RD5 skips pricing; **D20 bars pricing from A001** |
| **O-6** | `offer-oeos-engineer` · the OFFER-F2 synthetic RD7-shaped brief *(Offer-owned, independent of A001; `OFFER_OS.md` §8)* | Whether RD7's constraints hold against OEOS's standing instructions: questions stay unresolved, output stays structural and non-pricing, Phase 11 BLOCKED | **Observed, not predicted:** Q1–Q5 unresolved · Phase 11 blocked · **zero generated figures** · no outcome claim · the agent's own approval flag reached the top level · `emitted: []` | Runtime — `TEST_FIXTURE` lane | **one line** in `02_Offer/_memory/sandbox-offer-f2.jsonl` | OFFER-F2 | ✅ **COMPLETED 2026-09-22 — one attempt, SPENT.** **One sample:** it shows only that this brief held on this run; *“unresolved”* was judged from free text, because the schema has no field for it; the orchestrator→OEOS handover was not tested. **Not source evidence:** its model-generated phases, components and tiers must **never** be cited as the offer's structure, which stays `OFFER_OS.md` §3/§8 and `Draft 41` |
| **O-7** | `offer-orchestrator` · the OFFER-F3 synthetic, flag-free, R4-shaped brief (§6.9) | An **Offer intake test of an asserted synthetic brief** — **not** a demonstrated positive hand-off. Its in-scope result is *asserted inside the Offer seed*, not produced by an independent Sector record or an S10 packet. It tests only whether the intake routes that brief without a spurious stop, with every constraint intact *(corrected 2026-09-22)* | **Not predicted** — any of the four `registry_action` values | Runtime — `TEST_FIXTURE` lane | **one line** in `02_Offer/_memory/sandbox-offer-f3.jsonl` | A new Offer decision, OFFER-F3 | 🟡 **PROPOSED for owner review — not approved, not registered in code** |

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
| **D15** — no agent/skill/runtime activity for A001 Phase 3 | **all of** S-4, S-5, O-3, O-4, C-2, M-2, SA-2 | A new owner decision superseding D15 — **except O-4 on the A001-P07 sequence, which no decision reopens: D21 returned `reject`, and `reject` stops the sequence** |
| **D6** — T1-1…T1-5 deferred | the R2/R3 builds themselves | An owner amendment to D6 |
| **R2 / R3** — no sandbox stream or skill marker | the same tests, *after* D15/D6 | The build in §6.1 |
| **RD6** — no downstream agent runs | C-2, M-2, SA-2 | A separate RD6 decision |
| **D20** — barred content classes | S-6, O-5 | ⛔ Never, from A001 |
| **The skill-run record cannot carry a fixture** — *mechanism prepared 2026-09-22 and exercised once under SECTOR-SF1* | S-7 (and S-4) | **S-7:** ✅ resolved: SECTOR-SF1 run once and spent 2026-09-22 · **S-4:** still needs a fixture mode of its own |
| **Key unverified by use** | every runtime test | An approved verification run |

---

## 6. The smallest path to live mechanism testing

**A separate `TEST_FIXTURE` runtime lane is feasible.** It is a small, contained change —
the obstacle is decision-order, not engineering.

### 6.1 Fixture isolation — PREPARED, NOT ENABLED

Written and tested 2026-09-21. **`FIXTURE_LANE_ENABLED = false`**, so `--fixture` is refused and
the lane cannot run until the owner enacts a decision.

| File | Change |
|---|---|
| `arika-runtime/src/fixture.ts` | **New.** The master switch, `SANDBOX_BASENAME`, the `TEST_FIXTURE` marker, the fail-closed guard, and the CLI mapping |
| `arika-runtime/src/memory-writer.ts` | Optional `FixtureOptions`; guard runs **before** any `mkdir` or write; stamps `classification` only in fixture mode |
| `arika-runtime/src/executor.ts` | `RunContext` gains `fixture?` / `memoryStreamOverride?`, passed through `finalizeRun()` |
| `arika-runtime/src/triggers/cli.ts` | `--fixture` and `--memory-stream`, mapped through `buildFixtureOptions()` |
| `arika-runtime/tests/executor.test.mjs` | **17 new tests** — 9 lane mechanics, 8 pre-approval hardening |

**Fail-closed in both directions** — this is the property that matters:

- a **fixture** run may write **only** to a `sandbox.jsonl` stream; anything else **throws before
  writing**;
- an **ordinary** run may **never** write to a `sandbox.jsonl` stream; it throws too.

So a real run cannot pollute the fixture lane, and a fixture cannot leak into a real one.
Isolation is carried by the **filename**, not a flag inside the line, so it survives a plain
`cat`, a `grep`, or a reader who has never heard of the marker.

**Proof ordinary runs are unchanged:** a test asserts an ordinary line still has **no
`classification` key** and the **exact previous key order**
(`timestamp, agent, department, stream, event_type, source, payload`). The fixture key is spread
in conditionally, so with no options the serialized line is byte-identical to its pre-lane shape.

**Tested on both entry paths**, as required: `finalizeRun()` **directly** (including that a direct
call cannot smuggle a fixture into a real stream) and the **CLI mapping** via `buildFixtureOptions`
— tested as a separate module because `cli.ts` parses argv on import.

**Result: 36 tests, 36 pass, 0 fail** (19 pre-existing, unchanged, plus 17 new). **The gate also runs at the `runAgent` entry point, before any model call**, so a disabled lane, a wrong agent, a wrong destination, a bad brief or a spent lane all fail **without costing an API call**. `npm run build`
compiles clean. **No agent ran, no API was called, no memory log was written.**

**Skill runs (R3 / T1-4) are deliberately out of scope**, which keeps the first decision smaller.

### 6.2 Minimum record changes

- **Sandbox record §5.1** — a new decision superseding **D15** *for the bounded fixture
  lane only*, leaving document-only as the default everywhere else; and an amendment to **D6**
  un-deferring **T1-5** only.
- **§7** — AG-12 row updated; AG-13 left open.
- **Queue §7** — R2 status; R3 explicitly still deferred.
- **`TECHSTACK_OS.md` §3** — register the lane once verified live.
- **This plan** — re-audit the matrix against the new decisions.

### 6.3 Proposed decision — **D21, DRAFT. NOT APPROVED.**

> 🔴 **A draft for the owner to accept, amend or reject. Deliberately *not* written into
> the sandbox record's §5.1 decision table, because that would read as enacted.**

**D21 — A001 `TEST_FIXTURE` mechanism lane: one invocation attempt.**

**1. What is authorised.** **ONE manual invocation attempt** of `offer-orchestrator`, carrying the
exact approved `seed_brief` in §6.4, through the `TEST_FIXTURE` lane, writing **at most one
line** to `02_Offer/_memory/sandbox.jsonl`.

- **No automatic retry.** If the API call fails **before a log line is written**, the
  authorisation is **spent**. A retry needs a **fresh owner decision**.
- **No concurrent invocation.** One attempt, by hand, at a time.
- The attempt is authorised whether it **succeeds or fails**. Expiry is by attempt, not by outcome.

**2. Narrow D17 amendment — storage, stated accurately.**

> ⚠️ **Corrected in v0.5.** v0.3/v0.4 claimed A001 *"enters no shared store"*. **That was
> false.** `02_Offer/_memory/sandbox.jsonl` is a **separate, marked fixture stream**, but it sits
> **inside the git-tracked, auto-synced repository** — it is not gitignored, no `.gitignore`
> pattern excludes `_memory` or `.jsonl`, and a `post-commit` auto-sync hook has committed that
> directory before. **The line will be committed to `master` and synced.**

This amendment therefore **explicitly permits exactly ONE shared fixture log entry**: one marked
line, in one named file, created and committed. It makes **no claim** that A001 stays out of
shared storage — it does not.

**Still barred, unchanged:**

- the **real runtime stream** — `02_Offer/_memory/runtime.jsonl` and every other department's;
- the **Sector store**;
- the **CRM**;
- **any registry change**, whatever `registry_action` returns;
- **use as Offer evidence**, or as evidence about any market, property or buyer.

**3.** Supersedes **D15** for this one attempt only. Document-only remains the default for all
other A001 work.

**4.** Amends **D6** to un-defer **T1-5 only** (the sandbox stream). **T1-4 stays deferred**, so
**no skill run** is permitted.

**5.** **D18 and D20 are unchanged and still bind:** the slice stays `A001-P07` only, and the
output may improve **mechanisms only** — never market, demand, buyer, pricing, capacity or
proof.

**6. Confers nothing else.** No Offer eligibility, no registry change, no group ID, no change to
`PILOT-H-001` or any PG gate.

**7. Expires on that single attempt**, completed or failed.

> ⚠️ **On the one-run safeguard, stated honestly.** The code refuses to run when
> `02_Offer/_memory/sandbox.jsonl` already exists. That is a safeguard against a **second
> completed write**. It is **not proof that only one API attempt occurred** — an attempt that
> fails before the write leaves no file behind, so the check would pass again. **Counting
> attempts is the owner's discipline, not the code's.**

**Also required, separately:** approval to **verify the replacement API key by use** — which
this same single attempt would do.

### 6.4 First runtime test — input verified against the actual contract

> ⚠️ **Corrected across v0.3 and v0.4.** v0.2 proposed *"pilot ID, archetype,
> destination and H-band"* as structured fields and predicted the outcome. The spec declares
> **`inputs: seed_brief: { type: string }`** — a **single string**, so flags and provenance
> must live **inside it**. **Nothing in the contract constrains `registry_action`**, so no
> outcome is predicted. v0.3 then carried only a loose flag list and the wrong command; v0.4
> carries **SR-1, SR-2 and SR-3 by name**, keeps the **group verdict separate from them**, and
> fixes the command.

**Verified from the spec:** `execution: prompt` · `risk_class: 1` ·
`requires_human_approval: false` · `memory_stream: 02_Offer/_memory/runtime.jsonl` (the lane
overrides this) · `emits: [OFFER_BRIEF_RECEIVED]`. **The manual CLI path never publishes** —
`cli.ts` calls `runAgent` directly with no event bus. Verified in source.

**The three inherited stop rules, as the sandbox record states them:**

| Flag | Meaning |
|---|---|
| **SR-1** | The group archetype is **unresolvable** — the `Hospitality Group` union operator is not built (AG-4) |
| **SR-2** | The group has a **central brand, reservations and direct-booking team**, which Owner Decision 71 treats as **anti-ICP** |
| **SR-3** | The group **sits above every H-band** — no band in the current model describes it |

**The group verdict is not a fourth flag.** `SIMULATED_VERDICT` — outside the current offer
ICP, by design — is the sandbox's recorded *outcome*, and the brief keeps it in its own
labelled block so it cannot be read as another inherited rule.

**Exact approved input** — valid JSON, single line, no secrets, no real property name, no
price, no private data:

```json
{"seed_brief": "TEST_FIXTURE - SIMULATED SANDBOX UNIT. Not a prospect, not a client, not a CRM record, not market evidence (A001 D17, D20).\nUnit: A001-P07. Group: A001 (internal simulation group).\nPROVENANCE: every value below is SIMULATED and was authored to exercise mechanisms. None is sourced from a market, a real property or a buyer. No volume of it becomes evidence.\n\nINHERITED GROUP STOP RULES - carried from A001, never suppressed at unit level:\n  SR-1: the group archetype is UNRESOLVABLE - the Hospitality Group union operator is not built (AG-4).\n  SR-2: the group has a central brand, reservations and direct-booking team, which Owner Decision 71 treats as ANTI-ICP.\n  SR-3: the group sits ABOVE EVERY H-BAND - no band in the current model describes it.\nAll three fired by design at S1. SR-4, SR-5 and SR-6 did not fire.\n\nGROUP VERDICT (recorded separately from the stop rules above): SIMULATED_VERDICT - outside the current offer ICP, by design. It is the sandbox's recorded outcome, not a fourth flag and not evidence about any market.\n\nEVALUATION-ORDER RULE: inherited group stop rules are not suppressed at unit level, so unit-level passes do not imply eligibility.\n\nUNIT-LEVEL SIMULATED DESCRIPTORS: archetype Tented Camp, inheriting Safari Lodge; destination Maasai Mara (DB 16, profiled); size band H2; no unit-level stop rule fired. These unit-level passes do NOT override SR-1, SR-2 or SR-3.\n\nSCOPE: structural and mechanism test only. NON-PRICING - no price, rate, floor, band, commission or cost figure is supplied, implied or requested.\nREGISTRY: this run authorises no registry change, whatever registry_action is returned."}
```

**Command — corrected.** `cli.ts` runs `JSON.parse(opts.input)` on the raw argument: it has
**no `@file` support**, so v0.3's `--input @brief.json` would have failed with *"--input must be
valid JSON."* The JSON above is passed literally:

```bash
# bash / Git Bash - single quotes keep the JSON intact
arika run offer-orchestrator --fixture \
  --memory-stream 02_Offer/_memory/sandbox.jsonl \
  --input '<the JSON above, on one line>'
```

```powershell
# PowerShell - read the file yourself and pass the string
arika run offer-orchestrator --fixture `
  --memory-stream 02_Offer/_memory/sandbox.jsonl `
  --input (Get-Content brief.json -Raw)
```

**Parsing verified without invoking the agent:** the JSON was round-tripped through Python's
`json`, then through **Node's own `JSON.parse`** — the exact call `cli.ts` makes — and
then passed to the **compiled** `assertApprovedFixtureInput`. All three accepted it. No agent, no
API call.

| | |
|---|---|
| **Mechanism tested** | Whether **SR-1, SR-2 and SR-3 survive into the orchestrator's reasoning**, and whether seed-sufficiency routing reflects them |
| **Expected output** | **Not predicted.** `registry_action` may return **any** of `add_new_offer`, `update_existing_offer`, `needs_more_seed_data`, `reject`. The test records which, and compares `misaligned_assumptions` and `control_questions` against the three flags |
| **A finding** | The output **ignoring or suppressing** a stop rule, or treating the unit-level passes as eligibility |
| **NOT a finding** | Anything it says about demand, guests, prices, competitors, capacity or a real property — **barred by D20 however phrased** |
| **Registry** | `add_new_offer` / `update_existing_offer` **authorise nothing** (D21 §6) |
| **Writes** | One line to `02_Offer/_memory/sandbox.jsonl` with `classification: TEST_FIXTURE`; **nothing** in `runtime.jsonl` |

**Not approved, not enabled, not run.**

### 6.5 Non-runtime checks available immediately

No decision needed beyond a nod; none writes anything:

- **S-1a** — confirm O1's rule is present and still bounded to evaluation order
- **O-2** — confirm an agent's own `requiresHumanApproval: true` reaches the top level
- **O-1** — confirm registry actions authorise no registry change
- **G-2** — trace PG0–PG5 stop rules against A001 fixtures
- **G-3** — D20 boundary check over every proposed finding
- **S-2 / G-1** — the two existing gates

### 6.6 What is enforced by code, and what is only procedure

> Stated plainly, because a control that exists only in a sentence is not a control.

| Claim | Enforced by | Strength |
|---|---|---|
| **Lane is off** | ✅ **Code** — `FIXTURE_LANE_ENABLED = false`, checked at the `runAgent` gate **before any model call** | Strong. A closed lane costs no API call to discover |
| **Only `02_Offer/_memory/sandbox.jsonl`** | ✅ **Code** — exact-path match; absolute paths, traversals and other departments' `sandbox.jsonl` all refused | Strong |
| **Ordinary runs never touch the lane** | ✅ **Code** — an ordinary run writing to any `sandbox.jsonl` throws | Strong |
| **`offer-orchestrator` only** | ✅ **Code** — agent-name pin at the gate *(was procedure-only before v0.4)* | Strong |
| **Exactly one completed write** | ✅ **Code** — the lane refuses if the destination already exists | Good. **Deleting the file re-arms it** — deliberate, and visible in git history |
| **Exactly one API attempt** | ❌ **Not enforced** — a call that fails before the write leaves **no file**, so the existence check passes again | **Owner discipline.** File-existence proves at most one *completed write*, **never how many attempts were made** |
| **No concurrent invocation** | ❌ **Not enforced** — `existsSync` and `appendFileSync` are separate steps, so two parallel invocations could both pass the check (a TOCTOU race) | **Owner discipline.** Run it by hand, once |
| **A001 enters no shared store** | ❌ **Claim withdrawn (v0.5)** — the sandbox stream is inside the **git-tracked, auto-synced** repo | D21 §2 permits **exactly one** such entry and says so plainly |
| **`A001-P07` only** | ⚠️ **Code, but a text check** — requires the `TEST_FIXTURE` marker and the unit ID; rejects any other `A001-Pnn` and any real `PILOT-H-` ID | **Weaker.** `seed_brief` is free text, so this catches mistakes, **not** a determined rewrite, and cannot verify the descriptors are truthful |
| **Output is not evidence (D20)** | ❌ **Procedure only** | No code can stop a human citing a line as market evidence. This stays a reading discipline |
| **Master switch on direct `finalizeRun` calls** | ⚠️ **Partial** | The switch sits at `runAgent`. A caller reaching `finalizeRun` directly bypasses it — but makes **no API call** and still cannot escape the sandbox guard |

**Smallest reliable one-run control — recommended, and now implemented:** refuse when the
approved destination already exists. It needs no counter, no state file and cannot drift. **Pair
it with committing that file immediately after the run**, so the auto-sync hook puts re-arming on
the record rather than leaving it silent.

### 6.7 The exact approval statement required

Nothing runs until the owner gives this, in writing. **It is reproduced here as the wording
needed — it has not been given.**

> I approve A001 decision **D21** as drafted in `A001_AGENCY_SYSTEMS_TEST_PLAN.md` §6.3:
> enact D21, enable the `TEST_FIXTURE` lane, and authorise **ONE manual invocation attempt** of
> `offer-orchestrator` with the exact approved `A001-P07` `seed_brief` in §6.4, writing at
> most one marked line to `02_Offer/_memory/sandbox.jsonl` — **which I accept will be
> committed to the repository**. I also approve **verifying the replacement API key by use** as
> part of that same single attempt. **No retry without a fresh decision.**

Until then: lane **disabled**, D21 **DRAFT**, no agent run, no API call.

### 6.8 Attempt record — the one authorised invocation, MADE

**Status: ✅ the single attempt was made, and the authorisation is now SPENT.** No retry is
authorised; a further run needs a fresh owner decision.

| | |
|---|---|
| **Decision** | **D21 — ENACTED 2026-09-21** (owner approval in writing), recorded in the sandbox record §5.1 |
| **Attempt** | ONE manual invocation, started **2026-09-21T16:38:26Z**, log line written **16:38:54Z** |
| **Command** | `arika run offer-orchestrator --fixture --memory-stream 02_Offer/_memory/sandbox.jsonl --input <the §6.4 JSON>` |
| **Input** | The exact §6.4 JSON, extracted **from this document** and verified byte-identical to the reviewed brief before the call |
| **Result** | Exit code **0**, empty stderr |

**✅ Replacement API key — VERIFIED BY USE.** The call reached the model and returned a
valid structured response, which is the first live proof the rotated key works. It closes the last
open item from the RD3 rotation, which until now was owner-attested only.

**Mechanism outcome — TEST_FIXTURE evidence under D20, nothing more:**

| Field | Value |
|---|---|
| `registry_action` | **`reject`** |
| `riskLevel` | `low` |
| Top-level `requiresHumanApproval` | `false` |
| Agent's own `requiresHumanApproval` | `false`, with 1 `approvalReason` explaining why none is needed |
| `misaligned_assumptions` | 4 |
| `control_questions` | 5 |

**✅ SR-1, SR-2 and SR-3 all survived — named verbatim in the output.** The orchestrator
reproduced each rule with its own reasoning (unresolvable archetype / AG-4 · central
brand-reservations-direct-booking as anti-ICP per Decision 71 · above every H-band), and
**applied the evaluation-order rule correctly**: it recorded that the unit-level descriptors passed
and that this does **not** override the inherited group stop rules. **No eligibility was asserted.**

**✅ D20 boundary held.** A scan for barred content found **no** demand, seasonality, guest-mix,
competitor, capacity, staffing or performance claim, and **no claim about a real hotel**. The words
*price*, *rate* and *commission* appear only where the output **restates the non-pricing
constraint**; the only digits present are list and decision references (Decision 71, OEOS phases).
**No figure of any kind was produced.**

**✅ Isolation held — verified, not assumed:**

| Check | Result |
|---|---|
| `02_Offer/_memory/runtime.jsonl` | **Byte-unchanged.** sha256 `0295b173…` before and after; **5 lines** before and after |
| `02_Offer/_memory/sandbox.jsonl` | Created, **exactly 1 line** |
| Envelope marker | `classification: TEST_FIXTURE`, `stream: sandbox`, `source: arika-runtime` |
| Any other memory log created | **None** |
| Events | `emitted` declares `OFFER_BRIEF_RECEIVED`, but **the manual CLI path has no event bus and published nothing** |

**What this is evidence of, and what it is not.** It is evidence that **the mechanism carries
inherited group stop rules into Offer routing and refuses on them**. It is **not** an ICP finding,
**not** a market, demand, pricing or capacity statement, and **not** a claim about any real
property. `reject` here is **the gate working on a simulated unit**, not a verdict about anything
real. **No registry change is authorised or implied** — D21 §6.

**🔴 A successful stop-rule test, not permission to advance.** **`reject` stops the sequence** — packet PG3 (stop if `registry_action: reject`), R5 (stop on `reject`) and RD7 (*“a `reject` result stops the sequence”*). RD7's structural-only continuation exists **only for `needs_more_seed_data`**. The A001-P07 sequence therefore **ends here**: `reject` is the designed stop firing, and **no `offer-oeos-engineer` continuation of this output is proposed or permitted**. *(A continuation was suggested in session on 2026-09-21 as a possible “D22”; it was never written into this plan and is **withdrawn**, because it would have tested the one path PG3 and RD7 forbid.)*

**Why nothing chained — and why that is incidental, not designed.** No runtime code reads `registry_action`, and `handoff_to` is a **schema field only**. The orchestrator's static `emits: [OFFER_BRIEF_RECEIVED]` was reported **on this `reject`**, and `offer-oeos-engineer` **subscribes to that exact event**. OEOS did not run only because **no path publishes an agent's `emits`**: the CLI has no event bus, and the booted runtime's event handler calls `runAgent` and discards `result.emitted`. **So the `reject` stop is enforced by procedure (PG3 · R5 · RD7 and owner review), not by code.** *Mechanism finding (D20-permitted, routing logic):* if agent emits are ever published, a `reject` must suppress `OFFER_BRIEF_RECEIVED`, or OEOS would run on a stopped sequence — the same static-emit hazard already handled for `offer-pricing-floor-analyst`, which declares no emits for that reason. ✅ **Corrected 2026-09-22:** `finalizeRun()` now withholds `OFFER_BRIEF_RECEIVED` from the advertised `emitted` list when `registry_action` is `reject`; the recommendation and memory line are unchanged (`OFFER_OS.md` §12, `arika-runtime/DECISIONS.md`). The line already in `sandbox.jsonl` is left as written — `emitted` was never part of the memory payload.

**Not done, deliberately:** no retry, no second invocation, no scheduler, no event publication, no
other agent, skill or connector, no registry action, no CRM write, and no `.env` or key value
opened or printed. **`PILOT-H-001` and every real-push PG gate are unchanged.**

### 6.9 A positive Sector-to-Offer hand-off — route audit, the prepared S10 fixture path, and OFFER-F3

> Recorded here because this is the agency-systems matrix. OFFER-F2 and OFFER-F3 are **Offer-owned
> and independent of A001**: they carry no A001 unit, and their decisions belong in `OFFER_OS.md`
> §8, not A001's D-series.

**What the route actually is.** It was read from the readiness packet (§8, R2–R5), the S10
contract (`.claude/skills/sector-handoff-packet/SKILL.md`), the skill-run schema
(`01_Sector/contracts/skill-execution-record.schema.json`), the Hospitality plugin and the
orchestrator contract. It is **not** an automated channel:

| Step | What it is | Can a fixture test it truthfully today? | Record and isolation |
|---|---|---|---|
| **R2** Sector fit | **Manual, no agent** (RD4): a cited basis for archetype, destination, size band, website, booking path and anti-ICP | ✅ **Document-only.** A001 already exercised it; a synthetic unit's record is labelled `SIMULATED_VERDICT` | None — a document |
| **R3** S10 packet | A **skill** run by Claude Code; in the push, Offer is *"delivered by text reference"* | ✅ **Exercised once** under SECTOR-SF1 (spent 2026-09-22): mechanism evidence only | The run wrote one marked record to `01_Sector/_memory/skill_runs-sandbox.jsonl` and one marked packet, and **nothing** to `skill_runs.jsonl` |
| **R4** Seed brief | **Human-drafted and owner-approved** text (PG2) | ✅ **Document-only.** The fixture input *is* an R4-shaped brief | None |
| **R5** Orchestrator | A **runtime** call | ✅ Through the runtime fixture lane, under a new authorisation | One line in `02_Offer/_memory/sandbox-offer-f3.jsonl`: `classification: TEST_FIXTURE`, `emitted: []` |

The orchestrator does subscribe to `SECTOR_MAPPED`, but **that subscription never fires**, because
nothing sends agent emits. The only real bridge is the R4 text.

**Why S10 could not run as a fixture — three independent blockers.** ✅ *All three are addressed by a mechanism prepared on 2026-09-22 and exercised once under SECTOR-SF1, now spent. The analysis is kept because it is why that mechanism looks as it does.*

1. **The skill record cannot be marked.** `skill-execution-record.schema.json` is
   `additionalProperties: false` at the top level **and** in `payload`. Every field that could
   distinguish a record is a **constant**: `stream: "skill"`, `source: "claude-code"`,
   `event_type: "skill_run"`, `department: "01"`. A fixture record would be byte-for-byte
   indistinguishable from a real one, and S10 names **one fixed, shared** file.
2. **S10 has no fixture mode.** Its routes either **deliver** or report `HANDOFF_FAILURE`, and
   delivery means live-store writes: the only real S10 run recorded `writes: [DB1]` in Notion.
   A fixture that skipped a *working* route would have to misreport it as a failure, which S10's
   own refuse list forbids.
3. **There is nowhere to record "not attempted".** S10 says to record *"each destination, its
   mechanism, and whether it delivered"*, but the schema has **no structured field** for
   per-destination outcomes. This is a contract gap for real runs too.

**Smallest mechanism change for the S10 half** — ✅ **prepared 2026-09-22 and exercised once under SECTOR-SF1**, as specified below. See the 2026-09-22 changelog entry and `SECTOR_OS.md` §8, SECTOR-SF1:

- **Schema:** an optional top-level `classification` restricted to `TEST_FIXTURE`, and an
  optional `payload.destinations[]` of `{destination, mechanism, outcome}`, whose `outcome` enum
  includes `not_attempted_fixture` beside `delivered` / `HANDOFF_FAILURE` / `held`. The
  destinations field would also close gap 3 for real runs.
- **A distinct file,** `01_Sector/_memory/skill_runs-sandbox.jsonl`, mirroring the runtime lane's
  filename isolation.
- **An S10 fixture mode:** assemble the packet, make **no** cross-boundary write (no Notion
  relation, no CRM tag), record every destination as `not_attempted_fixture`, and write only to
  the sandbox file.
- **A gate check:** it fails if a marked record appears in `skill_runs.jsonl`, or an unmarked one
  in the sandbox file. Skills are executed by Claude Code following instructions, so without a
  check this isolation would be **procedure only**.
- **Owner decision:** a **Sector (01)** decision in `SECTOR_OS.md`, because skills are
  Sector-owned. ⚠️ This is the same change A001 lists as **T1-4** (R3), which D6 defers
  **for A001**. The decision must say whether it is Sector-general for non-A001 fixtures only, or
  also amends D6.

#### The S10 fixture run under SECTOR-SF1 · ✅ run once and SPENT 2026-09-22 — mechanism evidence only

The full decision, with its input pin, permitted writes, expected outcomes, stop conditions, limits and approval wording, is in `SECTOR_OS.md` §8, **SECTOR-SF1**, with its attempt record. In short:

- **One** S10 run in fixture mode on `01_Sector/fixtures/SYN-S10-01.sector-record.json` (sha256 `8247eefd…`).
- It reads **no live store** and makes **no** cross-boundary write.
- It writes **one** marked record to `skill_runs-sandbox.jsonl` and **one** marked packet.
- **Expected, and derivable from the contracts:** Offer, Content and CRM `not_attempted_fixture`; Sales, Marketing and Operations `HANDOFF_FAILURE`; nothing `delivered`.
- **Verified from rules:** the five rule results, recomputed by `test_skill_fixture.py`. **Synthetic:** the unit and every attribute value.
- **Observed 2026-09-22:** exactly the expected outcomes; nothing `delivered`; isolation held; five mechanism findings, recorded in the attempt record. **No retry.**

#### OFFER-F3 — an Offer intake test of an **asserted** synthetic brief · 🟡 proposed; not approved, not registered

> ⚠️ **Corrected 2026-09-22.** v1.3 called this *"the Offer half of a positive hand-off."* **It is not.** Without an S10 fixture packet and an independent Sector fit record, F3 is **only an Offer intake test of an asserted synthetic brief**. Its in-scope result is written *into the Offer seed itself*; no Sector step produced it, and no test recomputes it. **Its declared fit must not be called a demonstrated positive hand-off.**

**Purpose.** Test the Offer **intake**, R5, on a brief that **asserts** a flag-free, in-scope simulated unit: does the orchestrator route it **without a spurious stop**, with every constraint intact? It is D21's complement only at the intake: D21 showed the orchestrator refusing on inherited group flags.

**It does not exercise S10** and **it produces no fit verdict.** SECTOR-SF1's one run has since produced a synthetic S10 packet, as mechanism evidence only. A stronger F3 could take its brief from that packet, replacing assertion with a Sector-produced input. SF1 does not authorise that; it would be a new decision, not this one.

**Why this is not a manufactured pass — and how far that goes.** The brief *asserts* that every documented rule passes, because the synthetic attributes were **chosen** to be in scope. Unlike `SYN-S10-01`'s record, those assertions are **not recomputed** by any test. No rule is skipped, suppressed
or overridden: an independent unit with no group flags is simply a unit on which the anti-ICP
rule does not fire. A manufactured pass would be something like taking a group unit and deleting
its flags — which this is not. **The consequence is stated as a limit:** a good result shows
that the intake does not stop *constructed* inputs spuriously. It says **nothing** about whether
any real property fits.

**Identity.** The test ID is `OFFER-F3` and the unit is `SYN-F3` — visibly synthetic, **not**
A001 and **not** `PILOT-H-001`. It carries no real property identity, no URL, no private data, no
market finding and no price. The destination slot names **Nairobi**, a real place, so the rule
*"destination is profiled"* is checked against a real DB 16 profile. That is a place, not a
property; no property is named.

**Exact input.** Single-line JSON, ASCII only. `seed_brief` sha256 `633b2a72bc3994fe794bbe370ebba331552e10c416e28c2e3557e8afa8f054f4`:

```json
{"seed_brief": "TEST_FIXTURE - OFFER-F3 - POSITIVE-PATH OFFER INTAKE TEST. Unit SYN-F3 is SYNTHETIC: not a real property, not a client, not a prospect, not a CRM record and not market evidence. Its fit result is a SIMULATED_VERDICT and is never a real fit verdict. This output is not Offer evidence.\nPROVENANCE: no S10 hand-off packet exists for this fixture - S10 cannot yet run as a fixture, because no marked, isolated skill-run record exists. This brief is shaped like a readiness packet R4 seed brief. Every unit attribute below is SYNTHETIC, chosen to satisfy the documented rules; none was observed. It carries no real property identity, no URL, no private data, no market finding and no price. It cannot satisfy or bypass readiness gates PG1, PG2 or PG3 for any real run.\n\nUNIT: SYN-F3 (synthetic).\nSIMULATED SECTOR FIT - each basis SYNTHETIC, checked against the documented rule:\n- Archetype: City / Conference Hotel [SYNTHETIC] - an archetype ruled in live geography (Hospitality plugin P2).\n- Destination: Nairobi [SYNTHETIC assignment to a real destination] - one of the three places with a Destination Profile (plugin P4, DB 16).\n- Size band: H2 [SYNTHETIC] - inside the H1/H2 MVP scope (Owner Decision 71). No room count is given.\n- Website: present [SYNTHETIC].\n- Direct booking path: present [SYNTHETIC].\n- Group or chain: none, independent [SYNTHETIC] - no central brand.com or direct-booking team, so the anti-ICP rule does not fire.\n- Stop rules: none fired, because the synthetic attributes were chosen to be in scope. No rule was skipped, suppressed or overridden.\nSIMULATED_VERDICT: in scope. A mechanism fixture result, not a fit verdict.\n\nOFFER MATCH: the Accommodation entry offer, Hospitality Revenue Content OS - \"Direct Booking Engine\". Status: Working Hypothesis - Not Quotable - not registered.\n\nCONSTRAINTS (readiness packet R4): synthetic data only; a pre-audit hypothesis, never a finding; H1/H2 MVP scope; diagnostic-first, two-stage, audit-gated; NON-PRICING; PHASE 11: BLOCKED; Not Quotable. State no figure and make no outcome, result or performance claim. Make no statement about any market, demand, guests, competitors or destination performance. This run authorises no registry change, whatever registry_action is returned, and no downstream step."}
```

**Verified without a model call.** `offer-orchestrator` declares exactly one input,
`seed_brief: { type: string }`, and this object has exactly that key. It parses through Node's
`JSON.parse`, the call `cli.ts` makes. It carries the six markers, and none of: A001, a pilot ID,
currency, a percentage, a URL or a room count. Its only digits are references (S10, Phase 11,
DB 16, H2, P2/P4, PG1–PG3, R4, Decision 71). **It was built from documented rules only, not
from OFFER-F2's model output.**

**Expected mechanism behaviour — observed, never predicted.** `registry_action` may be **any**
of its four values. Each has a correct reading:

| If it returns | The mechanism reading |
|---|---|
| `add_new_offer` / `update_existing_offer` | The intake did not stop a flag-free unit. **It authorises nothing** — in the real push, reading either as permission is itself a PG3 stop condition |
| `needs_more_seed_data` | A valid response to synthetic, unobserved data. It would produce the **first real orchestrator output** a later, separately authorised fixture could carry into OEOS under RD7, testing the handover OFFER-F2 could not — **though that output would still rest on an asserted brief**, not on a Sector-produced packet |
| `reject` | **Not automatically a defect.** A reject is a legitimate outcome for an asserted synthetic brief. It is a defect **only** if the cited reason is **not** traceable to the input or the contract (a spurious stop); it is valid if it cites a documented constraint such as Working Hypothesis or Not Quotable, or the brief's unobserved data |

**A defect is any of:** a figure of any kind · an outcome, result or performance claim · any
statement about a market, demand, guests, competitors or destination performance · treating
`SYN-F3` as a real property or the `SIMULATED_VERDICT` as a real fit verdict · a stop rule cited
that the input does not carry · `add_new_offer` / `update_existing_offer` treated as permission
· truncation.

**Also recorded:** whether `misaligned_assumptions` and `control_questions` flag that the data is
synthetic and unobserved, which is the behaviour a real R5 needs. Also the agent's own and the
top-level `requiresHumanApproval`.

**Log destination.** Exactly one line, in `02_Offer/_memory/sandbox-offer-f3.jsonl`, marked
`classification: TEST_FIXTURE`, with `emitted: []` by the fixture rule. The file is **git-tracked
and auto-synced**. The decision would permit that one shared fixture entry and nothing else: not
`runtime.jsonl`, not either existing fixture file, not any other department's stream.

**Stop conditions — before the call:**

| Stop | Enforced by |
|---|---|
| Lane off; `OFFER-F3` not `approved`; destination not exactly `02_Offer/_memory/sandbox-offer-f3.jsonl`; agent not `offer-orchestrator`; the input differs from the recorded one by one byte; a marker missing; A001, a pilot ID, currency, a percentage, a URL or a room count present; destination already exists | **Code**, once registered, by the same gate that ran OFFER-F2 |
| Offline tests and gates not green; baselines for all three existing logs not captured; another arika process running | **Procedure** |

**What it cannot prove:** one attempt is one sample · constructed in-scope inputs say nothing
about real fit · S10 is not exercised · the R4 human-transcription step is represented by this
constructed brief, not by an owner-approved R4 drawn from a real S10 packet · it cannot count API
attempts (only completed writes).

**On acceptance of this design, and not before:** register `OFFER-F3` in
`arika-runtime/src/fixture.ts` as `draft`, with the pin above, stream
`02_Offer/_memory/sandbox-offer-f3.jsonl`, agent `offer-orchestrator` and forbidden patterns;
add offline tests; and draft decision OFFER-F3 in `OFFER_OS.md` §8 with its approval wording,
as OFFER-F2 was. **The procedure lesson from OFFER-F2 carries over:** the full suite pins the
closed state, so it runs before enabling and after closing, with a targeted compiled-gate check
in between.

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

- 2026-09-22 — **v1.5. SECTOR-SF1 enacted, its one S10 fixture run made, and SPENT.** **S-7** moves from prepared-and-disabled to ✅ **run once — mechanism evidence only**: Offer, Content and CRM `not_attempted_fixture`; Sales, Marketing and Operations `HANDOFF_FAILURE`; nothing `delivered`; no write and no event. Isolation held: one marked record in `skill_runs-sandbox.jsonl`, one marked packet, `skill_runs.jsonl` and every other log byte-unchanged. Five mechanism findings are recorded in `SECTOR_OS.md` §8. **S-4 stays blocked**, and **OFFER-F3 stays proposed and unregistered**: the packet feeds no Offer run without a decision of its own. A001 D6, the Full Push Packet, `PILOT-H-001` and every PG gate are unchanged. No retry. **Dated entries below stand as written.** — Claude Code (Opus 5)
- 2026-09-22 — **v1.4. OFFER-F3's overclaim corrected; the S10 fixture path prepared and disabled.** **Correction:** v1.3 called OFFER-F3 *"the Offer half of a positive hand-off."* Without an S10 fixture packet and an independent Sector fit record, it is **only an Offer intake test of an asserted synthetic brief**. Its in-scope result is written into the Offer seed, no Sector step produced it, and no test recomputes it. O-7 and §6.9 now say so; the declared fit is no longer called a demonstrated hand-off; `reject` is restated as a legitimate outcome, a defect only when its reason is untraceable. F3 stays **proposed and unregistered**. **Prepared, disabled:** a non-A001 `TEST_FIXTURE` mode for S10. It comprises an additive schema extension (all 15 existing records still validate), `skill_run_gate.py` checks 6–8, one delimited S10 fixture block that strips back byte-for-byte, and an independently labelled synthetic Sector record `SYN-S10-01`, whose five rule results an offline test recomputes from `plugin.config.json`, the readiness packet and `OFFER_OS.md`. **S-7** moves from blocked to prepared-and-disabled, pending draft decision **SECTOR-SF1** (`SECTOR_OS.md` §8). **S-4** stays blocked. A001 D6 is unchanged. No skill, agent, API or connector call; no log written. **Dated entries below stand as written.** — Claude Code (Opus 5)
- 2026-09-22 — **v1.3. OFFER-F2 recorded as completed; the positive Sector-to-Offer route audited; OFFER-F3 proposed.** **O-6:** OFFER-F2 is complete, one attempt and spent, with its one-sample limits. **Its model-generated structure is marked as never to be cited as source evidence.** **Route audit (§6.9):** the Sector-to-Offer hand-off is R2 (a manual fit document) → R3 (the S10 skill) → R4 (a human-drafted brief) → R5 (the orchestrator). It is not an automated channel, since `SECTOR_MAPPED` never fires. **S10 cannot run as a fixture (S-7),** for three reasons: the skill-run schema is `additionalProperties: false` with every identifying field constant, so a fixture record cannot be marked, and it goes to one shared file; S10 has no fixture mode, and its only real run wrote to Notion; and the schema has no structured per-destination outcome field, a gap for real runs too. The smallest mechanism change and the Sector (01) decision it needs are specified, **not made**, including its overlap with A001's T1-4 under D6. **O-7 / OFFER-F3 proposed:** the Offer half only (R4 → R5), with a synthetic, flag-free unit `SYN-F3`, exact input pinned by sha256 `633b2a72…`, a result that is observed and never predicted, a defect list, a log destination and stop conditions. It is **not registered in code and not approved**. Every fixture lane stays off, every existing log is unchanged, and the real-push PG gates are untouched. No agent, skill, API or connector call. **Dated entries below stand as written.** — Claude Code (Opus 5)
- 2026-09-22 — **v1.2. The stale O-3 row corrected, and §6.8's reject-emit finding marked as fixed.** **O-3** still read *“Blocked — R2”* with a predicted outcome of `needs_more_seed_data` or `reject`. **It is not an unrun test:** D21 ran it once on 2026-09-21 and it **returned `reject`**. The row now records the observed result, the one fixture line it wrote, that it is a stop-rule result rather than eligibility, and that it cannot be re-run without a fresh decision. **§6.8's mechanism finding is now acted on** — a rejected brief no longer advertises `OFFER_BRIEF_RECEIVED` (details in `OFFER_OS.md` §12). **The fixture log is unchanged** and dated entries below stand as written. — Claude Code (Opus 5)
- 2026-09-22 — **v1.1. D21's `reject` recorded as a successful stop-rule test; no OEOS continuation of the A001-P07 sequence.** Audited against the readiness packet: **`reject` stops the sequence** — packet PG3 (stop if `registry_action: reject`), R5 (stop on `reject`) and RD7 (*“a `reject` result stops the sequence”*). RD7's structural-only continuation exists **only for `needs_more_seed_data`**. **Corrected live text:** §4.2's O-4 row described OEOS consuming *“orchestrator output”* under RD7 and read as blocked only by R2 — the only such output is D21's `reject`, so O-4 is now marked **stopped for this sequence**, and §5's D15 row no longer implies a decision could reopen it. **Withdrawn:** the session suggestion of a “D22” feeding D21's output into `offer-oeos-engineer`; it was never written into this plan. **Added to §6.8:** the stop-rule framing, and a D20-permitted mechanism finding — the runtime never reads `registry_action`, the orchestrator emitted `OFFER_BRIEF_RECEIVED` even on `reject`, OEOS subscribes to it, and nothing chained **only** because no path publishes agent emits. The stop is procedural. **Not changed:** the one-line fixture log, the lane (closed), D21 (spent), every PG gate, and `PILOT-H-001`. No agent, skill or API call. **Dated entries below stand as written.** — Claude Code (Opus 5)
- 2026-09-21 — **v1.0. D21 ENACTED, the lane enabled, and the ONE authorised attempt made. The authorisation is now SPENT.** Recorded in full in §6.8. **Preflight passed before the call:** both gates green · 36/36 tests · build clean · `sandbox.jsonl` absent · `runtime.jsonl` baseline captured (sha256 `0295b173…`, 5 lines) · no concurrent arika invocation · the §6.4 JSON verified byte-identical to the reviewed brief and parsed through Node's own `JSON.parse`. **Two tests were corrected first, and this mattered:** with the lane enabled, the old *“refuses a disabled lane”* test would have **passed the gate and made a real API call of its own**; it now uses a non-approved agent so it can never reach the model. **Outcome:** exit 0 · **the replacement API key is VERIFIED BY USE**, closing the last open piece of the RD3 rotation · `registry_action` **`reject`** · approval flag `false` with a reason given · **SR-1, SR-2 and SR-3 all survived verbatim** and the evaluation-order rule was applied correctly, with **no eligibility asserted** · **no D20-barred content** (pricing words appear only as negations; no figures). **Isolation held:** `runtime.jsonl` **byte-unchanged**, `sandbox.jsonl` exactly **one line** carrying `classification: TEST_FIXTURE`, no other log created, nothing published. **Treated solely as mechanism evidence under D20** — `reject` is the gate working on a simulated unit, not an ICP, market or real-property finding, and authorises **no registry change**. No retry, no second invocation, no `.env` or key value read. `PILOT-H-001` and every PG gate unchanged. **The v0.1–v0.5 entries below stand as written.** — Claude Code (Opus 5)
- 2026-09-21 — **v0.5. D21's storage claim corrected, and the authorisation redefined as ONE invocation attempt. Still DRAFT; lane still disabled.** **(1) The storage claim was false.** v0.3/v0.4's D21 said A001 *“enters no shared store”* while directing a write to `02_Offer/_memory/sandbox.jsonl` — which is **inside the git-tracked, auto-synced repository**. Verified: the path is **not gitignored**, **no `.gitignore` pattern** excludes `_memory` or `.jsonl`, a **`post-commit` auto-sync hook** exists, and history shows it committing that directory. The amendment now **explicitly permits exactly ONE shared fixture log entry**, committed and synced, and **withdraws the no-shared-store claim**. A separate, marked stream is **isolation, not absence from the repo** — the two were conflated. **Still barred:** the real runtime stream, the Sector store, the CRM, any registry change, and use as Offer evidence. **(2) The unit of authorisation is now an *attempt*, not a run** — one manual invocation attempt, authorised whether it succeeds or fails, with **no automatic retry** (a failure before the write spends the authorisation; retrying needs a fresh decision) and **no concurrent invocation**. **(3) The one-run safeguard is described honestly:** the destination-existence check guards against a **second completed write** and is **not proof that only one API attempt occurred** — a call failing before the write leaves no file, so the check would pass again. §6.6 also now records that **concurrency is not enforced** (`existsSync` and `appendFileSync` are separate steps — a TOCTOU race), making both **owner discipline** rather than code. **(4) Added §6.7:** the exact approval wording, marked as **not given**. **D20 and every PG gate are unchanged**, `PILOT-H-001` untouched, memory logs unchanged, no API call, no secret read, no agent run. **The v0.1–v0.4 entries below stand as written.** — Claude Code (Opus 5)
- 2026-09-21 — **v0.4. Five pre-approval defects fixed in the prepared lane. Still disabled; D21 still DRAFT.** **(1) The brief now carries SR-1, SR-2 and SR-3 by name** — unresolvable group archetype (AG-4), central brand/reservations/direct-booking anti-ICP (Decision 71), and above every H-band — with the **group verdict kept in its own block** so `SIMULATED_VERDICT` cannot be misread as a fourth inherited rule. **(2) The command was wrong.** `cli.ts` runs `JSON.parse` on the raw `--input` argument and has **no `@file` support**, so v0.3's `--input @brief.json` would have failed outright. §6.4 now carries valid single-line JSON, a bash and a PowerShell form, and the JSON was verified through Python, through **Node's own `JSON.parse`**, and through the **compiled** guard — **without invoking the agent**. **(3) Destination validation was basename-only**, so `01_Sector/_memory/sandbox.jsonl`, an absolute path or a traversal would all have passed. The gate now demands the **exact** `02_Offer/_memory/sandbox.jsonl` and refuses absolute paths and `..` segments. **(4) The guard sat in `writeMemory`, which runs AFTER the model call** — so a disabled lane or a misdirected write would have cost a real API call to discover. `assertFixturePreconditions` now runs at the **top of `runAgent`, before any model call**, and covers direct executor callers; a test asserts the failure is the closed lane and **never** an `ANTHROPIC_API_KEY` error. Ordinary runs return from the gate immediately and are unchanged. **(5) Enforcement honesty (§6.6):** *offer-orchestrator only* and *exactly one run* were **procedure only** and are now **code-enforced** (agent pin; single-use via destination existence). *A001-P07 only* is code-enforced but by a **text check on a free-text string** — recorded as **weaker**, since it catches mistakes rather than a determined rewrite. *Output is not evidence* remains **procedure only**, and no code can change that. **36 tests, 36 pass.** One pre-existing lane test was updated because the stricter destination rule correctly rejected its throwaway path. Lane **disabled**, D21 **DRAFT**, memory logs **unchanged**, no API call, no agent run. **The v0.1–v0.3 entries below stand as written.** — Claude Code (Opus 5)
- 2026-09-21 — **v0.3. The D17 omission corrected, D21 drafted, the first input rebuilt against the real contract, and the fixture lane implemented but left disabled.** **(1) D17 was missing from v0.2's bar list** — it forbids A001 from *“the Offer runtime … or any shared store”* by name, and `offer-orchestrator` **is** the Offer runtime. **R2/T1-5 and any change to D6 or D15 cannot override a ratification**; only a narrow amendment to D17 can. It now heads §3 as bar 0. **(2) The proposed input was wrong twice.** The spec declares `seed_brief` as a **single string**, so v0.2's *“archetype, destination and H-band”* fields would never have reached the agent — §6.4 now carries the flags and provenance **inside the string**. And v0.2 asserted the result would be `needs_more_seed_data`/`reject`; **the contract constrains no such thing**, so the expected outcome is now *not predicted* and all four enum values are treated as possible. **(3) A correction to my own v0.2 claim:** v0.2 said the queue's O1 row *“still reads as open”*. **It does not** — its final column has said **“Implemented 2026-09-16”** all along. I had truncated the row when reading it and never saw that column; the queue was accurate and needs no correction. **(4) Added §6.1:** the fail-closed fixture lane, written and tested — guard in both directions, filename-carried isolation, `FIXTURE_LANE_ENABLED = false`, tested on the **direct executor path and the CLI mapping**, with a test proving ordinary lines keep their exact key order. **28 tests, 28 pass.** **(5) Added §6.3:** **D21 drafted — NOT APPROVED**, and deliberately not written into the sandbox §5.1 decision table. Nothing enabled, nothing run; no API call, no memory log, no Drive or CRM record, no secret read; `PILOT-H-001` and every PG gate untouched. **The v0.1 and v0.2 entries below stand as written.** — Claude Code (Opus 5)
- 2026-09-21 — **v0.2. Audited against D6, D15, D17, D18 and D20; three factual errors in v0.1 corrected.** **(1) S-1 duplicated work already done** — queue item **O1 was implemented 2026-09-16**, as the evaluation-order rule in `A001_DOCUMENT_ONLY_PILOT_CLOSEOUT.md` §2 with the `OFFER_OS.md` §15 pointer. The queue row was never marked done, which is what v0.1 misread; the implementation was there all along. S-1 is **withdrawn** and replaced by **S-1a**, a read-only verification that the rule is present and still bounded to evaluation order. **(2) S-1 contradicted its own “zero writes” column** — it was filed document-only with *writes: none* while proposing to record a sentence in a git-tracked file. §5 now states plainly that a recorded sentence **is** a write and needs its own approval. **(3) The blockers were mis-attributed.** v0.1 named R2/R3 as what blocks runtime testing. The governing bar is **D15**, which forbids *“`arika run`, agent, skill, scheduler or event activity”* for A001 Phase 3 in those exact terms, and **D6**, which keeps the R2 build itself deferred. **R2 alone could never authorise an A001 agent or skill run** — it is a precondition that matters only after the owner changes D15 and D6. §3 and §5 are rewritten accordingly. **Added §6:** the smallest path to a live `TEST_FIXTURE` lane — feasible, four code touches, fail-closed, with a distinct `sandbox.jsonl` filename so isolation survives a careless read; plus the record changes, the five owner decisions, one concrete first runtime test, and the non-runtime checks available now. **The v0.1 entry below stands as written.** Nothing was implemented or run; no agent, skill, API or connector called; no memory log, Drive file or CRM record created; no secret read; the Full Push Readiness Packet and its PG gates untouched. — Claude Code (Opus 5)
- 2026-09-21 — **v0.1 created.** A bounded agency-systems test plan over the existing A001 group and units — **planning only, nothing approved or run**. Built after reading the runtime's actual write behaviour rather than assuming it: `finalizeRun()` writes memory **unconditionally**, the line carries the **full input**, every relevant agent declares a `memory_stream`, and three department logs would be **created** by a first run. **Central finding: the isolation the owner requires does not exist yet** — R2/R3/R5 (sandbox stream, skill marker, test-fixture trust) are all deferred under D6, so a runtime A001 run would write an **unmarked** line into a shared department stream. That, not the API key, is what blocks every runtime test. **11 document-only or non-runtime tests are safe now; every runtime-backed test is blocked.** First test recommended: **S-1**, the group-flag inheritance rule (queue O1) — zero-write, zero-runtime, and directly protective of the rule that P07's unit passes are **not** Offer eligibility. No agent, skill, API or connector was called; no memory-log entry, Drive file or CRM record was created; no `.env` or key value was read; the Full Push Readiness Packet's readiness and PG gates were not changed. — Claude Code (Opus 5)
