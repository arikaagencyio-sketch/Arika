# PK2 P4 / P5 — the synthetic S10 dry run

**Prepared:** 2026-10-03 · `PK2-P4-PREP`
**Owner:** Sector (01) · decision home `01_Sector/SECTOR_OS.md` §8
**Objective:** make the complete synthetic S10 dry-run path *eligible* for ONE bounded test, without `PILOT-H-001` and without any real property.

> ## 🔴 PROPOSAL · NOT ENACTED · S10 NOT RUN · NO AUTHORISATION APPROVED
>
> `SECTOR-SF3` is shipped **`draft`**. A draft admits nothing: the registry's own rule and
> `skill_run_gate.py` check 7 both refuse any record written under it. **No connector, agent,
> skill, runtime, model, Notion, ClickUp, CRM or external call was made in preparing this**, and
> none is authorised by it. **No PG gate moves. No readiness figure moves.** Preparation is not
> permission.

---

## 0. Headline

| | |
|---|---|
**P4 (authorisation)** | 🔴 **OPEN.** Closure is mechanical and fully specified — see §2. One owner decision flipping `SECTOR-SF3` from `draft` to `approved` closes it. |
**P5 (trigger)** | ✅ **SATISFIED, on both paths, and it is not a separate blocker for a fixture run** — see §3. |
**Technically ready?** | ✅ **Yes.** Every precondition except the owner's approval is met and verified offline today. |
**Which PG gate could move?** | 🔴 **None.** PG0–PG5 are defined over a *real* property. A synthetic run moves **no** PG gate — see §9. |
**Full Push readiness after a success** | **20.0 % → 20.0 %.** Unchanged, by the assessment's own cap: a `TEST_FIXTURE` run earns mechanism and simulation credit only. What moves is **Full Push *simulation*, 89.2 % → 90.6 %**. |

🔴 **One premise in the task does not hold, and it matters.** The instruction was to *"prefer SYNCO-02 if it remains the fit-passing fixture."* **SYNCO-02 is not a fit-passing fixture and never was.** It is the P10 **delivery** control: `fixture_id: SYNCO-02`, `delivery_id: SYNCO-02-D1`, an **empty payload**, living in a private sandbox outside this repository, and its authorisation is **`spent`**. It contains no sector record, no attributes and no fit verdict, so it cannot drive S10 packet assembly. The fit-passing synthetic fixture is **`SYN-S10-01`** — §4.

---

## 1. What the repository actually says about PK2, and what it does not

**Task 1 asked for the exact current meanings of P4 and P5 from live repository files. Here is the honest finding first:**

🔴 **The `SECTOR-PK2` packet is not in this repository, and never has been.** `git log -S "SECTOR-PK2"` places its first appearance on **2026-10-01**, and in every case it is a *reference by name*, never a definition. There is no file that lists P1–P10. Searched: every `*.md` and `*.json` in the tree, and the full git history for an added path matching `*PK2*` — nothing.

**Every in-repo gloss of P4 and P5, exhaustively:**

| Where | Text |
|---|---|
`01_Sector/DB9_PROVENANCE_REMEDIATION_PROPOSAL.md` §15.5 | "PK2's other blockers — **P4 (authorisation), P5 (trigger)**, P7/P8 (real pilot), P10 (delivering routes) — are untouched, and **packet assembly remains blocked**." |
`01_Sector/SECTOR_DELIVERY_P10_PROPOSAL.md` §0.1 | "**S10 packet assembly** — **BLOCKED by P4, P5, P7 and P8.**" |
`01_Sector/SECTOR_DELIVERY_P10_PROPOSAL.md` §14 | "every further step needs either **a real packet (blocked by P4/P5)** or a real destination (blocked by P7/P8, which no fixture can close)." |
`READINESS_ASSESSMENT_2026-10-02.md` §2.1 | "S10 packet assembly is BLOCKED by PK2 **P4 (authorisation)**, **P5 (trigger)** and P7/P8 (real pilot)." |
`00_Agency_Governance/offline_guard/OFFLINE_FIXTURE_GUARD.md` | the guard "does not approve … `SECTOR-PK2` … Each of those still needs its own owner decision." |

**So P4 and P5 are named by a one-word gloss and nothing else.** Rather than guess at an absent packet, this proposal derives both from the **operative conditions in the live governing contracts** — which are fully determinate — and names the exact lines. ⚠️ **If the owner holds a PK2 packet outside this repository whose P4 or P5 differ from §2 and §3, this proposal is wrong and should be rejected on that ground.** That is a real risk and it is not resolvable from inside the tree.

**A namespace warning, because it is easy to get wrong.** `P4` and `P5` carry three unrelated meanings here: PK2 prerequisites (this document); **Hospitality plugin slots** (`P4` = Destination Profiles, `P5` = place profiling — both cited *inside* `SYN-S10-01`'s own rule checks); and **Sector ADDENDUM phases**. Nothing below refers to the plugin slots or the phases.

---

## 2. P4 — the exact closure condition

**P4 is the authorisation precondition of S10's fixture mode.** Live source, `.claude/skills/sector-handoff-packet/SKILL.md`, fixture-mode block, *"Refuse unless every one of these holds"*:

> 1. **The authorisation named is `approved`, for `sector-handoff-packet` / `S10`.**

Enforced by `01_Sector/contracts/skill_run_gate.py` check 7 (`check_fixture_log`), which fails any record naming a `draft` authorisation, and check 8 (`check_registry`), which validates every row's synthetic record, pinned hash, markings and packet location.

### 2.1 Live state — audited, not assumed

`01_Sector/contracts/skill-fixture-authorisations.json` holds **three** rows:

| id | status | spent | synthetic record | packet |
|---|---|---|---|---|
`SECTOR-SF1` | **`spent`** | 2026-09-22, one attempt (`s10-2026-09-22-sector-sf1-syn-s10-01-fixture-1`) | `SYN-S10-01.sector-record.json` | `SYN-S10-01.s10-packet.json` |
`SECTOR-SF2` | **`spent`** | 2026-09-29T072952Z, one attempt (`s10-2026-09-29-sector-sf2-syn-s10-01-crm-tag-1`) | same | `SYN-S10-01.s10-packet-sf2.json` |
`SECTOR-SF3` | **`draft`** ← prepared here, **NOT enacted** | — | same | `SYN-S10-01.s10-packet-sf3.json` |

**`approved` rows: 0.** Verified by assertion, not by reading: `test_no_authorisation_is_currently_approved` (new, §7).

**Neither spent row may be reused or reopened.** The registry's own rule: *"Entries are never deleted: a spent one stays so its records remain explained."* Each has `max_records: 1` and each already holds exactly its one record in `skill_runs-sandbox.jsonl` — now asserted by `test_each_spent_authorisation_has_exactly_its_one_record`.

### 2.2 How P4 closes

| Route | Sufficient? |
|---|---|
**Owner decision only** | ❌ No. The gate reads the registry file, not a decision log. |
**A prepared fixture authorisation** | ✅ **This is the route.** The row exists as `draft`; the owner's decision flips one field. |
**An offline trigger record** | ❌ Not applicable — see §3; the trigger is the authorisation. |
**Code or contract work** | ❌ Not needed. No code change is required to close P4. |
**An actual S10 invocation** | ❌ That is what P4 *gates*, not what closes it. |

🔴 **P4's closure condition, exactly:** `SECTOR-SF3.status` becomes `"approved"` in `01_Sector/contracts/skill-fixture-authorisations.json`, by owner decision recorded in `SECTOR_OS.md` §8. **Nothing else.** Every other field is already pinned and verified.

---

## 3. P5 — the exact trigger, and why it is satisfied

**S10's trigger contract**, live, from its own frontmatter:

> *"Use when a sector reaches **Offer-Ready**, at **activation Gate G**, or when a **resolver run produces opportunities**. **Runs LAST, after every write skill for that sector.**"*

and its Refuse list, line 173: *"Running before the sector's write skills have completed for that sector."*

### 3.1 On the fixture path — the authorisation *is* the trigger

Both spent runs recorded an identical trigger shape in `skill_runs-sandbox.jsonl`:

```json
"trigger": {"kind": "manual",
            "detail": "SECTOR-SF1 owner-approved TEST_FIXTURE execution (one attempt, no retry)",
            "gate": null}
```

✅ **So for a `TEST_FIXTURE` run, P4 and P5 collapse into one instrument.** A fixture unit has no sector state machine, no Offer-Ready promotion and no Gate G — `gate` is explicitly `null`. The trigger is the owner's authorisation, recorded as `kind: manual`. **This is established precedent, twice, in a gate-validated log**, not an interpretation.

🔴 **The readiness assessment therefore overstates the obstacle.** It lists *"PK2 P4 (authorisation) and P5 (trigger)"* as two blockers on the synthetic path. On that path **P5 is not a separate blocker at all.** §12 records the correction.

### 3.2 On the real path — already satisfied for Hospitality / Accommodation

Not needed for this run, recorded so the distinction is not lost:

- **Offer-Ready reached 2026-08-28.** S10's own appendix: *"Hospitality reached `Offer-Ready` the same day, so this skill's primary trigger is live for the first time."*
- **Write skills completed.** `skill_runs.jsonl` holds 15 records covering **S01–S10**; S10's own exit-building run is `s10-2026-08-28-offer-ready-promotion-and-exit-built`.
- ⚠️ **That run's timestamp is unverifiable.** It is one of the 8 ids in `skill_run_gate.py`'s `UNVERIFIABLE_TIMESTAMPS` — *"Composed, not read"* — grandfathered because the log is append-only. **The run happened; its date is unproven.**

✅ **P5 status: SATISFIED.** On the fixture path by the authorisation; on the real path by the 2026-08-28 Offer-Ready promotion, with the date caveat above.

---

## 4. The selected synthetic fixture

✅ **`SYN-S10-01`** — `01_Sector/fixtures/SYN-S10-01.sector-record.json`, sha256 **`8247eefd3b84d1f4a64f385637eabb2dc617b1b76a43c2466a1b99ae7e62d94f`**.

| Property | Value |
|---|---|
`classification` | `TEST_FIXTURE` |
`synthetic` | `true` |
Sector / sub-sector | Hospitality / Accommodation |
Rule checks | **5, all computed from live sources**: `R-ARCHETYPE` pass · `R-DESTINATION` pass · `R-SIZE-BAND` pass · `R-ANTI-ICP-WEB` not_fired · `R-ANTI-ICP-GROUP` not_fired |
`stop_rules_fired` | `[]` |
`simulated_verdict` | **`in_scope`** — this is the **fit-passing** fixture |
`verdict_label` | *"SIMULATED_VERDICT: a mechanism fixture result, not a fit verdict."* |
Names a pilot or sandbox group? | **No.** `provenance`: *"names no sandbox group, no pilot identifier and no real property."* |

Its rule results are **recomputed from the repository's own sources** by `test_skill_fixture.py`'s `SyntheticRecord` class, which fails on any mismatch — so the fixture is not merely asserted to pass, it is checked to pass.

### 4.1 Why not the others

| Candidate | Verdict |
|---|---|
**SYNCO-02** | ❌ **Not a fit-passing fixture, and not a sector record.** The P10 delivery control: empty payload, private sandbox outside the repo, authorisation `SECTOR-DELIVERY-P10-D1` **`spent`**. Its own mechanism record lists *"packet assembly"*, *"S10 execution"* and *"a Sector skill fixture authorisation"* under **`does_not_authorise`**. |
**SYNCO-01** | ❌ Excluded by the task. A synthetic *company* fixture, normalization-only, with reference-identifying figures withheld. |
**A001** | ❌ **Forbidden by code.** `skill_run_gate.py` `FORBIDDEN` refuses any record or packet matching `\bA001\b`; its records stay deferred under A001 D6 (T1-4). |
**PILOT-H-001** | ❌ **Forbidden by code.** `FORBIDDEN` refuses `PILOT-H-\d`. It is a real property identifier and has **no runs of any kind**. |

**No contract requires any of the four**, so none is used.

---

## 5. Exact inputs, outputs and writes

### 5.1 Pinned source artifacts

| Path | sha256 | bytes |
|---|---|---|
| `01_Sector/fixtures/SYN-S10-01.sector-record.json` | `8247eefd3b84d1f4a64f385637eabb2dc617b1b76a43c2466a1b99ae7e62d94f` | 3368 |
| `01_Sector/contracts/skill-fixture-authorisations.json` | `62a0e8bf0af10c939c6351369245f05ca604488cc20c945410c539bb60bdfeac` | 5209 |
| `01_Sector/contracts/skill_run_gate.py` | `b547f61b6217ceae5c85d4e734116cb44bc588c9229670f22c7b4aeb637d6df7` | 15396 |
| `01_Sector/contracts/sector-databases.json` | `51004a2e2d42d0c87e9417cae9efb1007ba68252f13b319594afd3559d5dacb6` | 183333 |
| `01_Sector/contracts/event-catalog.json` | `2e1e174af4edcae2325b58c00c6ae84b0de1dd783e8f9b0149c777adef3f2f71` | 13824 |
| `.claude/skills/sector-handoff-packet/SKILL.md` | `05d4fec9f623a6d073f804815a79e7e57d751833094d9a1af0b10ac4ac3d6c46` | 27806 |
| `01_Sector/SECTOR_WRITE_CONTRACT.md` | `c493a9679b8586a5abb82cd4774f4cfe067b3b041b3e5c5d6a900e3b2dca60d3` | 29309 |
| `00_Agency_Governance/CRM_SCHEMA.md` | `44d226541eb46c1655d0556e83434f0ad201dc63571c9475343ca3f05869185e` | 22949 |
| `arika-runtime/src/executor.ts` | `a07ced0d4e04c968bf68fb0ff8d738c30028c0363467c0ffc211eff6de62ea09` | 8574 |
| `01_Sector/delivery/delivery-authorisations.json` | `cc73b5a3658082bc83fba071f65a7d17789be04fcf0613bcd8118fcc63b8a387` | 9009 |
| *prior packets, must stay byte-unchanged* | | |
| `01_Sector/fixtures/SYN-S10-01.s10-packet.json` (SF1) | `7554729f114d737dc4f365847dd336c0606e9fbc776d5e339a94671acb2f1798` | 6582 |
| `01_Sector/fixtures/SYN-S10-01.s10-packet-sf2.json` (SF2) | `a4e0ff7ce334dcf4fc4c834821ce1e4322be484e313628aa741e2f179c6bb673` | 5660 |

### 5.2 Exactly what one authorised attempt may write

**Three repository files. Nothing else, anywhere.**

| # | Path | Write |
|---|---|---|
1 | `01_Sector/fixtures/SYN-S10-01.s10-packet-sf3.json` | **CREATE** one new file: the assembled packet, `classification: TEST_FIXTURE`, carrying all 11 AEIT_09 §1 fields |
2 | `01_Sector/_memory/skill_runs-sandbox.jsonl` | **APPEND** exactly one line. Never `skill_runs.jsonl`; never touching an existing line |
3 | `01_Sector/contracts/skill-fixture-authorisations.json` | **UPDATE** `SECTOR-SF3.status` → `"spent"` at F6, after the gate passes |

🔴 **Forbidden, explicitly, and none is required by the S10 contract for this run:**
no Notion read or write · no ClickUp or CRM read or write · no Offer or Content write · no event published · no event bus · no runtime, scheduler or webhook boot · no model call · no connector of any kind · **no delivery to `offer_inbox_receiver.py`** · no second packet · no retry · no change to `skill_runs.jsonl` · no change to SF1's or SF2's rows, records or packets.

`payload.writes` and `payload.events` stay **`[]`**. `payload.fixture.external_writes` is **absent**. `decision` stays **`NO_OP`**.

### 5.3 External destination

✅ **None.** `SECTOR-SF3` carries `permits_external_write: "NONE"`, so F3's default applies in full. SF2 is the only authorisation that ever permitted an external write, and it is spent.

**This is a deliberate narrowing versus SF2.** The task's boundary *"no Notion or ClickUp write unless strictly required by the existing S10 contract"* is satisfied by requiring **none at all**: Step 4's floors are computed from `sector-databases.json`, a repository file, which F0 permits — *"Read only the synthetic record and repository files."*

### 5.4 Cleanup

**No cleanup is required, because nothing external is created.** SF2 needed F3a (create → tag → read back → delete → confirm absence) because it touched ClickUp. SF3 touches nothing outside the repository.

**If the run fails part-way**, the rule is **stop, do not retry, report what exists by name**:
- packet written but no log line → **leave both as they are**, report; the authorisation stays `approved` and is **not** re-used.
- log line written but gate fails at F6 → **leave the line**, report; the log is append-only and a record is never edited or deleted.
- 🔴 **Never delete or rewrite a line in either log.** A failed attempt stays failed and a further attempt needs a **new owner decision and a new row**.

---

## 6. What the run would exercise that nothing ever has

**This is the whole justification, and it is specific.**

S10 Step 4 computes two fail-closed floors:

```
confidence_threshold:  Low < Medium < High; null is UNASSESSED and weaker than Low
                       if ANY contributing item has a null Confidence -> UNRESOLVED, naming each

freshness_requirement: if ANY contributing item has a null Last Verified
                          OR a null Next Review     -> UNRESOLVED, naming each such element
                       else -> the EARLIEST Next Review, stated with the OLDEST Last Verified
```

over **four** contributing elements (DB 3 findings, DB 9 audience, DB 6 linguistics, DB 10 decision-makers).

🔴 **No S10 run — fixture or real — has ever executed that rule in its current form.**

| Run | Date | Why it does not count |
|---|---|---|
Real S10 exit-building run | 2026-08-29 | Predates every provenance change; its timestamp is also unverifiable |
`SECTOR-SF1` | 2026-09-22 | Its packet states both floors as **prose about the synthetic record** — `freshness_requirement` reads *"this packet carries no observed data to age"* — not a computation over four elements |
`SECTOR-SF2` | 2026-09-29 | Same prose shape, plus the CRM write. Also predates everything below |

**Everything the rule depends on landed on 2026-10-02, after both fixture runs:** `DB9-PROV-1` (DB 9 `Evidence`), `DB6-DB10-PROV-1` Steps 1–2 (DB 6/DB 10 `Evidence`), `DB6-OD1-OD2-1` (13 DB 6 cells **and the `Next Review` half of the freshness rule itself**), `DB3-PROV-1` Step A (DB 3 as the **fourth** element), `DB3-OD10-OD12-1` (DB 3's two date fields, `Freshness` non-governing, **the absent-vs-null-vs-populated three-state report**).

**So the dry run is the first execution of the four-element computed floors, and of the three-state date reporting.** That is exactly why the readiness assessment holds Sector's simulation `G` at `P`.

---

## 7. Repository work done in preparation

Two **stale self-describing claims** were found in governance artifacts this proposal must rely on. Both are the same defect class: **a count-or-absence claim written beside the data it describes, which drifted when the data changed, and which nothing checked.**

| # | Artifact | Claim | Status |
|---|---|---|---|
1 | `01_Sector/delivery/delivery-authorisations.json` `_no_approved_delivery` | *"there is no `approved` delivery row in this file, **and no SYNCO-02 row of any status**"* | 🔴 **False.** `SECTOR-DELIVERY-P10-D1` (`fixture_id: SYNCO-02`, `spent`) sits two keys above it |
2 | `.claude/skills/sector-handoff-packet/SKILL.md` fixture notice | *"**The only one**, SECTOR-SF1, was spent on 2026-09-22"* | 🔴 **False.** Two rows exist; SF2 was approved and spent 2026-09-29 |

**In both cases the operative clause stayed correct** — no approved delivery row; none is `approved` — **so nothing was ever wrongly admitted.** Only the counts drifted. Defect 1 is the sharper one: the governing **test** had already been re-baselined on 2026-10-02 *for exactly this reason*, and its docstring says so, but the data file's own prose was never updated to match its test.

**Both corrected, preserving the superseded wording verbatim.** The S10 notice sits inside the `FIXTURE-MODE` block, which `S10_ORDINARY_SHA` excludes, so **no hash re-baseline was needed**.

### 7.1 The class fix — six new tests

Correcting two sentences fixes two instances. These make the **class** detectable:

| Test | Suite | Checks |
|---|---|---|
`test_self_describing_claims_match_the_rows` | delivery | the note's claims against the actual rows, and that no spent fixture's existence is denied |
`test_the_spent_p10_row_is_retained_and_still_admits_nothing` | delivery | the spent row stays **and** stays inert |
`test_s10_fixture_notice_matches_the_registry` | skill fixture | every spent id is named; *"The only one"* is refused when several exist; the operative refusal matches the registry |
`test_no_authorisation_is_currently_approved` | skill fixture | **P4's live state, asserted** — if a row is ever approved deliberately, this test must be changed, which cannot happen quietly |
`test_each_spent_authorisation_has_exactly_its_one_record` | skill fixture | record count equals the authorised limit; a draft holds none |
`test_a_draft_row_holds_no_record_and_pins_its_inputs` | skill fixture | a draft is inert **and** fully specified, so approving it adds no new decision |

**One pre-existing test was rewritten, not loosened.** `test_both_authorisations_are_spent_and_nothing_is_approved` pinned the exact roster `[SF1 spent, SF2 spent]` and correctly failed when SF3 was added. Pinning the whole roster could not distinguish *"a third authorisation was approved behind our backs"* from *"a third was prepared for the owner to decline"*. The replacement is **stricter**: SF1 and SF2 unchanged and first, **nothing approved**, and **every row beyond the two must be a `draft` carrying `_not_enacted`**.

**One false positive was found and fixed in my own new test.** `test_s10_fixture_notice_matches_the_registry` initially failed because *"The only one"* still appeared — inside the correction note's **quotation of the sentence it retracts**. The scan now covers the operative notice only, stopping at the `*Corrected` marker. **Preserved history must not be scanned as a live assertion** — the same false-positive class as truth-gate check 7c's `xlsx sheet` ban tripping on the sentence explaining the correction.

**Mutation-tested: 11 mutations, all caught, all 4 touched files restored byte-identically.** Reinstating the SYNCO-02 denial, dropping the no-approved claim, deleting or recasting the superseded record, deleting or re-approving the spent P10 row, reverting the notice to *"The only one"*, dropping the operative refusal, approving an authorisation, and removing or duplicating a spent authorisation's record — each fails the suite.

---

## 8. PASS, FAIL, STOP — pinned before any result

**Pinned in `SECTOR-SF3.expected_outcome_pinned_before_the_run`, so a different result is a finding rather than a rationalisation.**

### ✅ PASS — every one of these

1. `skill_run_gate.py` **exits 0** both before and after.
2. Exactly **one** new line in `skill_runs-sandbox.jsonl`; `classification: TEST_FIXTURE`; `payload.fixture.authorisation_id == "SECTOR-SF3"`.
3. The packet exists at the authorised path, is valid JSON, `classification: TEST_FIXTURE`, and carries **all 11** AEIT_09 §1 fields.
4. `payload.writes == []` · `payload.events == []` · `payload.decision == "NO_OP"` · `payload.fixture.external_writes` **absent**.
5. **`freshness_requirement` resolves to `UNRESOLVED` and names EVERY unresolved element:** DB 3 (both dates present, null on all 217), DB 9 (null on all 4), DB 6 (**Buyer** row's `Next Review` null), DB 10 (null on all 57).
6. **`confidence_threshold` resolves to `Medium`**, as the weakest governed `Confidence`, with the synthetic cap stated.
7. DB 3 reported with the **three-state** distinction — *present but null*, not *absent*.
8. **No** destination reads `delivered` or `delivered_fixture_verified`. Routes that would deliver read `not_attempted_fixture`; routes that do not read `HANDOFF_FAILURE`.
9. `skill_runs.jsonl`, SF1's and SF2's rows, records and packets all **byte-unchanged**.
10. `git status` shows **only** the three files in §5.2.
11. All offline suites and all five gates still pass.

### ❌ FAIL — the run completed and the result is wrong

Any PASS item unmet. Specifically: a floor resolving to anything other than `UNRESOLVED` / `Medium`; a floor computed but **not naming** each unresolved element; DB 3 reported as *absent*; a missing AEIT_09 field; a non-empty `writes` or `events`.

**On FAIL: record it, do not retry.** A failed attempt is evidence. A second attempt needs a new decision and a new row.

### 🛑 STOP — halt at once, do not continue, tell the owner

- Any output contains a **price, amount, fee, floor or quote**, an outcome guarantee, or a claim the offer is quotable.
- Any **personal, client, contact or guest datum**, or a secret, appears anywhere. *The memory line cannot be edited, so this is an owner-level incident, not a clean-up task.*
- The input or output names **A001** or matches **`PILOT-H-\d`**.
- Anything would require a **Notion, ClickUp, CRM or connector call**, an event, or a runtime boot.
- The working tree shows changes beyond §5.2, or any gate fails.
- The packet path already exists before the run.
- Any claim is made about a **market, demand, guests, competitors or destination performance**.

---

## 9. What it would prove, what it cannot, and which gate moves

### ✅ Would prove

- S10's **four-element computed floors execute** and fail closed on the current recorded state.
- The floors **name** each unresolved element rather than returning a bare verdict.
- DB 3's **three-state** date reporting works end to end, post-`DB3-OD10-OD12-1`.
- Fixture isolation holds with **zero** external surface — stricter than SF1 or SF2.
- The packet shape, route check, boundary law and confidence cap still hold after five provenance changes landed on 2026-10-02.

### ❌ Cannot prove

- **Anything about a real property.** The unit does not exist; every attribute is synthetic.
- **Any fit verdict.** `simulated_verdict` is a mechanism result by its own label.
- **Any market, demand, pricing, buyer, capacity or performance fact.**
- **Any delivery.** Nothing is handed off; no external destination is touched.
- **That the floors would resolve for a real property** — they resolve to `UNRESOLVED` precisely because the data is absent, and a real run would be `UNRESOLVED` too, for the same reason.
- **That `PILOT-H-001` is ready.** It has no runs of any kind, and none is proposed.

### 🔴 Which Full Push gate could move: **NONE**

| Gate | Why it cannot move |
|---|---|
**PG0** | Satisfied for public-only *preparation* only. **Still fails on RD2's open storage half.** A synthetic run does not touch RD2 |
**PG1** | Requires **OI1–OI8 answered** and public observation notes for a real property. A synthetic unit supplies neither |
**PG2** | Requires *"Sector fit record says **in scope**"* for a real property **and** a seed brief using the **pilot ID (RD1)**, owner-approved character for character. `SYN-S10-01`'s verdict is a `SIMULATED_VERDICT`, and the fixture names no pilot ID — **by design, and `FORBIDDEN` would refuse one** |
**PG3** | Downstream of PG2 |
**PG4** | **Skipped, not passed** (RD5) |
**PG5** | Downstream of PG3, and RD6 permits notes only |

🔴 **The PG ladder is defined over the real Full Push throughout. A synthetic dry run moves none of it, and no PG gate may be marked passed because this run succeeded.**

### What *does* move

| Measure | Before | Max justified after |
|---|---|---|
**Full Push readiness** (real-pilot) | **20.0 %** | **20.0 %** — unchanged. `TEST_FIXTURE` earns mechanism and simulation credit only |
Full Push **gates passed** | **0 of 5** | **0 of 5** — unchanged |
**Full Push simulation** | 89.2 % | **90.6 %** (Sector and S10 simulation `G`: `P → V`, `PVVVVV` 92.5 % → `VVVVVV` 100 %) |
Sector (01) simulation | 92.5 % | **100.0 %** |
S10 simulation | 92.5 % | **100.0 %** |
Agency-wide simulation | 53.4 % | **53.9 %** |
Mechanism · real-prospect · client-facing | 53.0 % · 15.0 % · 2.3 % | **all unchanged** |

---

## 10. Every blocker that would remain afterward

**Full Push, real path:** OI1–OI8 (one real property) · PK2 **P7/P8** — *no fixture can close these* · RD2's storage half, so **PG0 still fails** · PG1, PG2, PG3, PG5 all unmet · PG4 skipped not passed · the seed brief needs character-for-character owner approval · all P8 sources still `candidate`.

**Sector:** 5 agents never run · S11/S12 contracts only · `sector-icp-fit` is B2B-SaaS-only and **cannot fit a hotel** (RD4 accepted, not closed) · **DB 3 OD12 H1's overstated High confidence** · **OD13** Sub-Sector null count unmeasured · the tier half of OD6 — `Source Tier` and `Source URL` structurally inexpressible on DB 3 · **the DB 3 date backfill is not authorised**, so the freshness floor stays `UNRESOLVED` for every element.

**Delivery:** **P10 real-packet delivery to a real destination — OPEN.** No `approved` delivery row exists and this proposal adds none. Marketing (03) has **no route** from Sector (31k); Sales (05) is event-only with no observed delivery.

**Estate:** **D4** — `humanGate` computed after the agent answers and nothing refuses dispatch · Finance's 3 pure non-terminating loops · **59** counsel, **60** entity, **61** s.48 — so **client-facing stays 0 %** · **58** scheduler ungoverned · item **66**, unchecked image rights on a live public surface.

**And P4 itself returns to OPEN**, because `SECTOR-SF3` becomes `spent`. A fourth run would need a fourth decision.

---

## 11. Boundaries this proposal preserves

✅ `TEST_FIXTURE` / `SIMULATED` only · ✅ no real property, no `PILOT-H-001`, no A001, no SYNCO-01 · ✅ no client, contact, guest or private data · ✅ no pricing or performance claim · ✅ **no Notion or ClickUp write of any kind** · ✅ no connector, agent, runtime, model or external call in preparation · ✅ no downstream hand-off · ✅ **no readiness figure or PG gate marked passed because preparation is complete** · ✅ no spent authorisation reused or reopened · ✅ dated history preserved and superseded, never rewritten.

---

## 12. Corrections to the governing baseline

| Claim | Correction |
|---|---|
`READINESS_ASSESSMENT` §3.1: *"**PK2 P4 (authorisation) and P5 (trigger)** block S10 packet assembly"* as the Sector simulation blocker | **P5 is not a separate blocker on the synthetic path.** The authorisation *is* the trigger for a fixture run — precedent in both spent records, `kind: manual`, `gate: null`. The synthetic path is blocked by **P4 alone** |
Task premise: *"prefer SYNCO-02 if it remains the fit-passing fixture"* | **SYNCO-02 was never a fit-passing fixture.** It is the P10 delivery control: empty payload, private sandbox, `spent`, and its own record forbids S10 execution and packet assembly. The fit-passing fixture is **`SYN-S10-01`** |
`SECTOR-PK2` as a readable source | **Not in the repository, and never has been.** P4 and P5 are derived here from the live S10 contract and the registry, with every line cited. ⚠️ If an out-of-repo PK2 packet defines them differently, reject this proposal |

---

## 13. Decision record — DRAFT, NOT ENACTED

**Draft Sector decision `SECTOR-SF3`.** Prepared 2026-10-03 under `PK2-P4-PREP`. Status in `01_Sector/contracts/skill-fixture-authorisations.json`: **`draft`**, carrying `_not_enacted`.

**Preparing this closed no blocker, moved no gate and changed no readiness figure.** P4 remains **OPEN** until the owner approves the row; S10 has not run; no packet exists at the SF3 path.

The exact approval wording is in the covering report, not here, so that this document cannot be mistaken for the approval itself.
