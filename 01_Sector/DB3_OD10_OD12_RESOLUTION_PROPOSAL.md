# DB3 — OD10 / OD12 Resolution Proposal

> 🔴 **PROPOSAL · NOT IMPLEMENTED · NO LIVE VALUE CHANGED · OD10 OPEN · OD12 OPEN**
>
> Nothing here is enacted. No live Notion value was written, cleared or changed; no schema was
> mutated; no `Confidence` was assigned or altered. `Freshness` remains `Fresh` on all 217 rows,
> DB 3 still has 15 fields, and both decisions remain **OPEN** in `contracts/sector-databases.json`.
>
> **Prepared:** 2026-10-02 · **Author:** Claude Code (Opus 5) · **Live calls:** 4, all read-only,
> all against DB 3 · **Writes performed:** 0

**Version:** 1.0

---

## 0. The two findings that decide this

**OD10 is not the question it looks like.** It reads as *"pick a number for Fresh/Aging/Stale."* It
cannot be answered that way, because **there is nothing to measure a threshold from.** DB 3 has no
`Last Verified` and no `Next Review` field. A rule of the form *"Aging after N days"* needs a date,
and DB 3 has none. **Option A is not weak — it is unimplementable as written.**

**And DB 3 is already non-compliant with two governed contracts, independently of S10:**

| Contract | What it requires | DB 3 |
|---|---|---|
| `contracts/intelligence-object.schema.json` → `when_observed` | `required: ["last_verified", "freshness"]` — **both** | maps `Freshness` **alone**. Cannot supply `last_verified` |
| `SECTOR_ACTIVATION_CONTRACT.md` §6 Freshness rule | *"every intelligence/score record carries `source`, `confidence`, `freshness`, **`last update`**, **`next review`**"* | has the first three, **lacks both date fields** |

**That matters for the motive.** This proposal does **not** recommend adding date fields to make
S10 computable — the task rightly forbids that reasoning. It recommends them because **two
governed contracts already require them and DB 3 cannot satisfy either.** S10 computability is a
*consequence* of compliance, not the argument for it.

**The second finding is sharper still.** The repository governs what `Stale` *means* — *"Stale
intelligence MUST NOT drive downstream execution without revalidation"* (`SECTOR_WRITE_CONTRACT.md`,
restated in S01's own skill) — but **nothing governs when a row becomes `Stale`.** So DB 3 carries
**a consequence with no trigger**: a rule with real teeth that can never bite, because all 217 rows
are `Fresh` and nothing can ever change one.

**Recommended:** **Option D.** Keep `Freshness`, mark it **explicitly non-governing**, and add
`Last Verified` + `Next Review` as the fields that govern. This **dissolves OD10 rather than
answering it** — under D **no threshold is needed at all**, because the thing a threshold was
supposed to produce (a decay signal) comes from `Next Review` instead, which is how all ten other
dated databases already work.

**OD12: one of the three High rows requires correction; two cannot be settled from the record.**
All three page bodies are **blank**.

---

## 1. Preconditions verified

Step A committed in git HEAD (8 files); working tree clean. DB 3 records 15 fields and 217 rows;
`Evidence` required and populated 217/217; `Source` recorded as process-kind vocabulary;
`Last Verified` and `Next Review` recorded structurally absent; `Freshness` populated 217/217 and
recorded ungoverned; OD10 and OD12 both OPEN. `DB3-PROV-AUDIT-1` byte-identical to its pinned hash.

The three High rows' page identifiers were **not** available from the prior audit — its privacy
policy deliberately excluded them — so the one authorised scoped query was used to find them.

---

## 2. Repository Freshness usage map

### 2.1 Every database carrying a freshness-like field

| DB | Field(s) | Mechanism |
|---|---|---|
| **DB 1** Sectors Master | `Next Review` | **date** |
| **DB 2** Sub-Sectors | `Next Review` | **date** |
| **DB 3** Sector Intelligence | **`Freshness`** | 🔴 **categorical state — the only one in the estate** |
| **DB 6** Sector Linguistics | `Last Verified` · `Next Review` | **date** |
| **DB 7** Sector Signals | `Last Verified` · `Next Verification` · `Review Date`, plus `Refresh Status` and `Change Status` | **dates + two categoricals** |
| **DB 9** Audience Roles | `Last Verified` · `Next Review` | **date** |
| **DB 10** Decision-Maker Registry | `Last Verified` · `Next Review` | **date** |
| **DB 13** Sector Forecast | `Review Date` | **date** |
| **DB 14** Signal Sources | `Last Verified` · `Next Verification` | **date** |
| **DB 15** Market Routes | `Last Verified` | **date** |
| **DB 16** Destination Profile | `Last Verified` · `Next Review` | **date** |

**Eleven of sixteen databases carry a freshness-like field. Ten of the eleven use dates. DB 3 is
the sole holdout, and the sole owner of the `Fresh`/`Aging`/`Stale` vocabulary.**

### 2.2 Exact vocabularies

| Vocabulary | Where | What it measures |
|---|---|---|
| `Fresh` · `Aging` · `Stale` | **DB 3 only** | intended: record age. Actual: nothing — see §2.3 |
| `Confirmed` · `Annual-recurring` · `Needs verification` · `Superseded/Delayed` | DB 7 `Refresh Status` | a **signal's verification status**, not a record's age |
| `new` · `changed` · `cancelled` · `unchanged` | DB 7 `Change Status` | **what changed since last check** |

**No vocabulary is shared between DB 3 and DB 7.** They are three unrelated three-and-four-value
enums measuring three different things. There is no latent common standard to converge on.

### 2.3 Is any threshold governed? **No.**

Searched every markdown, JSON contract and Python gate in `01_Sector/`, `.claude/` and
`00_Agency_Governance/`. **No document anywhere defines when a DB 3 row becomes `Aging` or
`Stale`.** What does exist:

- **A governed consequence.** `SECTOR_WRITE_CONTRACT.md`: *"Stale rule: 'Stale intelligence MUST
  NOT drive downstream execution without revalidation.'"* Restated in the **T4 rule**: *"a T4,
  unverified or **stale** record MUST NOT drive a downstream event, a department action, or an
  execution."*
- **A skill-level assertion that it matters.** S01 `sector-finding-writer`: *"`Freshness` is
  `Fresh` · `Aging` · `Stale` — and it is **operational, not decorative**. A `Stale` finding is
  barred from driving execution until revalidated."*
- **An operational staleness sweep that does not cover DB 3.** `SECTOR_CADENCE.md` M4:
  *"Stale-signal sweep — anything past `Next Verification`"*, owned by S04, state `DESIGNED`. It
  keys on **DB 7's `Next Verification` date** — a field DB 3 does not have. So the one mechanism
  that operationalises staleness **cannot reach DB 3**, and it has never run.

🔴 **A consequence with no trigger.** The estate says clearly what `Stale` *does*. Nothing says
how a row *becomes* `Stale`. The field is load-bearing in prose and inert in fact.

### 2.4 Manual, derived, or mixed? **Manual.**

`Freshness`'s recorded `writer_skill` is **S01**, and S01's Step 5 lists it under *"Yours"* — an
authored value, same as `Confidence`. It is **not** computed from anything, and could not be: there
is no date to compute from. **Mixed is not the answer either — it is purely authorial.**

### 2.5 Does any agent or skill write it? **One skill: S01.**

`Freshness` appears in exactly two skills: **S01** (`sector-finding-writer`), which writes it, and
**S10** (`sector-handoff-packet`), which only states that it **may not** substitute for a date.
No agent writes it. DB 3's `writer_skills` is `["S01"]`.

### 2.6 Does any gate validate it? **No row value is validated.**

Truth-gate `check 7c` (added by Step A) asserts only that the **repository records** `Freshness` as
a declaration with no threshold. It validates no row's value — and could not, being offline. **No
gate anywhere checks a DB 3 `Freshness` value, and none could while no threshold exists.**

### 2.7 Does S10 read it? **No — and it is explicitly forbidden from using it.**

S10 Step 4 computes `freshness_requirement` from `Last Verified` and `Next Review`. DB 3 has
neither, so its contribution is `UNRESOLVED`. Step 4 states outright: *"No assembly date, current
date, or `Freshness` label may substitute for a missing verification date."* **So `Freshness` is
currently read by nothing that computes anything.** Its only consumer is a human reading the row.

---

## 3. The 30-day and 90-day horizons — analysis

**Both exist. Neither measures what DB 3's `Freshness` would need to measure.**

### 3.1 The 30-day horizon — two distinct uses, neither about record age

| Use | Source | What it measures |
|---|---|---|
| **Prospect-score decay** | `SECTOR_ACTIVATION_CONTRACT.md` §6; `sector-signal-scorer`; `SECTOR_OS.md` §§ on the scorecard; DB 5's `Re-score Date` field | *"Medium-band prospect scores are **re-scored every 30 days** ('signals decay')"* — the age of a **score**, on **DB 5** |
| **Signal proximity** | `SECTOR_CADENCE.md` D1; `SECTOR_CALENDAR_REFRESH_SPEC.md` §2a | a signal whose **date is inside 30 days** is re-verified every run — **distance to a future event**, on DB 7 |

`AEIT_09` §2 HP-1 restates the first as *"score freshness ≤ 30 days (Sector's re-score decay
rule)"* — again a **score**, not a finding.

### 3.2 The 90-day horizon — two distinct uses, neither about DB 3 rows

| Use | Source | What it measures |
|---|---|---|
| **Truth-gate metadata warning** | `sector_truth_gate.py` check 5: *"no `verified_date` in the future; warn on any older than 90 days"* | the age of a **row-count verification claim recorded in a repository contract file** — not any Notion row's content |
| **Signal proximity bands** | `SECTOR_CALENDAR_REFRESH_SPEC.md` §2a: 180–90 days Elevated/Fortnightly, 90–30 High/Weekly | again **distance to a future event** |

### 3.3 Can either be reused legitimately? **No.**

- The **30-day** rule governs a *score's* decay and a *signal's proximity*. A DB 3 finding is
  neither. Borrowing it would assert that a structural market finding decays at the same rate as a
  prospect's buying-signal score — a claim no document makes and this audit cannot support.
- The **90-day** gate check is the closest in *shape* — it genuinely measures age-since-verification
  and warns. But it governs **repository metadata, not row content**, and it produces a **warning**,
  not a state transition. Lifting its number into DB 3 would be choosing a threshold because a
  number was available, which is precisely what this task forbids.

🟢 **Under the recommended Option D the question becomes moot.** No threshold is needed, so neither
horizon has to be reused, reconciled or chosen between. **The unreconciled 30/90 split flagged in
`DB9_PROVENANCE_REMEDIATION_PROPOSAL.md` §12 stays open — but it stops blocking DB 3.**

### 3.4 One thing that *is* reusable

**The `Next Review` field name and convention.** DB 1, DB 2, DB 6, DB 9, DB 10 and DB 16 all use
`Next Review`; DB 7 and DB 14 use `Next Verification`. **DB 3 should adopt `Next Review`**, joining
the six-database majority rather than inventing a third name. That is reuse of a *convention*,
which is legitimate, as against reuse of a *number*, which is not.

---

## 4. OD12 — the three High-confidence rows

**All three page bodies are BLANK.** No sources section, no tier, no verification date, no
caveat — nothing. This is a sharp contrast with the six Target-sector rows, every one of which
carried either a structured `## Provenance` block or at least a one-line source note.

| | **H1** predictive-hire signal | **H2** CSRD delay | **H3** FSMA 204 delay |
|---|---|---|---|
| Category | Decision Dynamics | Risk/Fragility | Risk/Fragility |
| `Confidence` | **High** | **High** | **High** |
| `Source` | 🔴 **`chat`** | `research` | `research` |
| `Freshness` | `Fresh` | `Fresh` | `Fresh` |
| `Impact` | High | Medium | Medium |
| `Evidence` present | yes | yes | yes |
| Sources named | 🔴 **an internal Arika draft only** | **EU Commission** (named primary body) | **US FDA** (named primary body) |
| Locator quality | 🔴 **none — self-referential** | assertion of verification, no document reference | names the rule and both dates; no document reference |
| Caveats / limitations | **none** | none | none |
| Page body | 🔴 **blank** | 🔴 **blank** | 🔴 **blank** |
| `Sub-Sector` | present (non-Target) | 🔴 **NULL** | 🔴 **NULL** |
| In a current Target S10 path | **No** | **No** | **No** |
| **Classification** | 🔴 **HIGH_OVERSTATED** | ⚠️ **HIGH_UNRESOLVED** | ⚠️ **HIGH_UNRESOLVED** |

### 4.1 H1 — `HIGH_OVERSTATED`, and correction is required

Its `Evidence` is *"Draft 15 6-category signal framework — Predictive category (leading
indicator)"* — **Arika's own internal draft**. Its `Source` is **`chat`**. Its body is blank. There
is **no external evidence of any kind** that the market behaves as the finding claims.

This is the breach S01's own skill names in its own words: *"Weak evidence plus `High` confidence is
a **constitutional breach**, not a rounding error. Downgrading to `Low` is always available and
always preferable to inflating."*

**It is self-referential provenance:** the agency's own framework cited as evidence for a claim
about buyer behaviour. The framework may be a perfectly good *hypothesis generator*; it is not
evidence that the hypothesis is true.

It is **routed to Sales and Marketing**, and its `Recommended Action` is *"Trigger
sector-signal-scorer on the account; route to Sales qualification"* — so it is written to drive
execution. It is not in a Target S10 path, but **it is not inert either.**

**Recommended treatment: downgrade.** The value is the owner's call; the evidence supports `Low`
and at most `Medium`. **This proposal does not change it.**

### 4.2 H2 and H3 — `HIGH_UNRESOLVED`, no correction proposed

Both are **regulatory facts attributed to a named primary authority** — the EU Commission and the
US FDA. That is the one category where `High` is genuinely defensible: a published rule either says
this or it does not, and H3 in particular names the rule, the exact delta (30 months) and both
dates.

**But neither can be confirmed from the record.** *"Verified regulatory fact (EU Commission)"* is an
**assertion that verification happened, not a record of it** — no document, no locator, no date,
and a blank body. By this programme's standing rule, **an assertion is not evidence**, so neither
may be marked `HIGH_SUPPORTED`.

⚠️ **And H2 has independently gone out of date while reading `Fresh`.** Its `Evidence` says *"revised
ESRS set due H1 2026"* and its `Recommended Action` says *"re-time outreach to the revised ESRS
H1-2026 milestone"*. **Today is 2026-10-02 — that milestone has passed.** The row instructs a
reader to aim at a date that is already behind them, and its `Freshness` still says `Fresh`.

**This is OD10 observed rather than argued.** Not a hypothetical about decay: a row whose own
content has expired while its freshness label remains unchanged, because nothing can change it.

**Recommended treatment: no confidence change. Re-source both**, recording a document reference and
a verification date — which requires the §5 date fields to exist first. Until then they are
honestly `UNRESOLVED`.

### 4.3 An incidental finding — `Sub-Sector` is null on two of three

DB 3's contract makes `Sub-Sector` **REQUIRED**, with the validation *"REQUIRED. A finding that
resolves to no sub-sector is noise."* **H2 and H3 both have none.**

**The estate-wide count is unmeasured.** `DB3-PROV-AUDIT-1` measured the four provenance fields and
did not check `Sub-Sector`, and this task's read authorisation does not extend to another aggregate.
So: **two confirmed breaches, unknown total.** Recorded as a new open item, not acted on.

---

## 5. OD10 — the four options assessed

Common to all: `Freshness` is **authored by S01**, read by **no computation**, validated by **no
gate**, and governs **nothing** today.

### Option A — keep `Freshness`, define DB 3-local deterministic thresholds

| | |
|---|---|
**Semantic clarity** | Would be good *if achievable* |
**🔴 Achievability** | **IMPOSSIBLE AS WRITTEN.** A deterministic threshold needs a date to measure from. DB 3 has none. There is no `Last Verified` to compare against, and `createdTime` is prohibited as a provenance basis |
**Migration across 217 rows** | Cannot start |
**Truthfulness** | n/a |
**Maintenance** | n/a |
**S10 compatibility** | Still fails — `last_verified` remains unsatisfiable |
**Skill compatibility** | S01 could not compute it either |
**Historical `Fresh` values** | n/a |
**Live schema write** | None — which is exactly why it cannot work |
**30/90 reuse** | Would *require* choosing one, with no legitimate basis |

**Rejected: not weak, unimplementable.** This is the finding that reframes OD10 — the option the
question implies cannot be built.

### Option B — keep `Freshness` as a manual declaration, add date fields, dates authoritative

| | |
|---|---|
**Semantic clarity** | Good. Two signals, one authoritative |
**Migration** | **None required.** 217 `Fresh` values stand; new fields start null |
**Truthfulness** | High — stops `Freshness` implying a measurement |
**Maintenance** | Two fields to keep, as all ten other dated databases already do |
**S10 compatibility** | ✅ Resolves it. `last_verified` becomes satisfiable |
**Skill compatibility** | S01 gains two fields; its `Freshness` guidance survives unchanged |
**Historical values** | **Merely non-governing**, not false |
**Live schema write** | **Yes — 2 additive date properties** |
**30/90 reuse** | **Not needed** |

**Viable.** Differs from D only in how explicitly `Freshness`'s demotion is recorded.

### Option C — retire `Freshness`, replace with `Last Verified` + `Next Review`

| | |
|---|---|
**🔴 Contract compatibility** | **EXCLUDED.** `intelligence-object.schema.json` sets `when_observed.required = ["last_verified", "freshness"]`. **`freshness` is a REQUIRED property of the canonical Intelligence-Object.** Retiring it breaches the contract in the opposite direction |
**Migration** | A destructive 217-row field deletion |
**Truthfulness** | Would discard S01's authored judgement on every row |
**Live schema write** | Yes — **a deletion**, the most dangerous class available |

**Rejected on the contract, not on preference.** Also note: Notion cannot "retire" a select
cleanly — the DB 7 lesson on record is that renaming an option drops it and strips it from every
row. A deletion here would discard 217 authored values.

### Option D — preserve `Freshness` for display, mark it **non-governing**, add date fields for computation ✅

| | |
|---|---|
**Semantic clarity** | **Best.** It names which signal governs and which does not — the ambiguity *is* OD10 |
**Migration** | **None.** No row value changes |
**Truthfulness** | **Highest.** `Freshness` stops claiming to be a measurement and becomes what it has always been: an author's declaration |
**Maintenance** | Same as B |
**S10 compatibility** | ✅ Resolves `last_verified`; **and S10 already behaves this way** — Step 4 already forbids substituting a `Freshness` label, so D formalises existing behaviour rather than changing it |
**Skill compatibility** | S01 keeps authoring `Freshness`; the **`Stale` rule finally gets a trigger** — `Next Review` in the past |
**Historical `Fresh` values** | **Merely non-governing.** Nothing that was true becomes false: a label that governed nothing continues to govern nothing, but now says so |
**Live schema write** | **Yes — 2 additive date properties, `Last Verified` and `Next Review`** |
**30/90 reuse** | **Not needed — no threshold is required** |

### 5.1 Why D, decisively

1. **It dissolves OD10 instead of answering it.** The honest resolution is not *"pick 30 or 90
   days"* — it is **stop asking `Freshness` to carry a meaning nobody ever gave it**, and put the
   meaning where ten other databases already keep it.
2. **It gives the `Stale` rule a trigger for the first time.** *"Stale intelligence MUST NOT drive
   downstream execution"* becomes enforceable: a row past its `Next Review` is stale. Today that
   rule is unenforceable.
3. **It is the only option that satisfies both governed contracts** without breaching the other.
4. **It formalises what S10 already does**, so no S10 behaviour changes — only its inputs improve.
5. **It costs no row-value migration.** Two additive writes; 217 rows untouched.

### 5.2 Why **not** make `Freshness` derived

Tempting: compute `Fresh`/`Aging`/`Stale` from the dates. **Rejected on recorded precedent.** A
derived value needs a Notion **formula** property — and the estate already learned, when DB 5's
`Total Score` became a formula on 2026-09-13, that **a formula property is
`notAvailableInQuerySql`**. A derived `Freshness` would become unreadable by the exact query path
every audit in this programme has used. **Keep it a manual select; let dates govern.**

### 5.3 What D does **not** do

- It does **not** define a threshold. **OD10 closes by removing the need for one**, not by choosing.
- It does **not** backfill a single date. The fields would start **null on all 217 rows**, so
  **S10's freshness floor stays `UNRESOLVED`** until a separate, separately-authorised backfill.
  **Adding fields creates capacity, not provenance** — the same caution recorded at DB 6 Step 2.
- It does **not** ratify anything Sector-wide. **OD4 stays OPEN**; DB 3 remains a counterexample to
  one latent standard, because `Freshness` survives and no other database has it.
- It does **not** touch `Source`, whose process-kind semantics are correct and recorded.

---

## 6. Exact schema and migration implications

**Two additive live writes, DB 3 only:**

| # | Property | Type | Nullable | Notes |
|---|---|---|---|---|
1 | `Last Verified` | date | yes | satisfies the Intelligence-Object `last_verified` requirement |
2 | `Next Review` | date | yes | adopts the DB 1/2/6/9/10/16 convention, **not** DB 7's `Next Verification` |

**DB 3 would go 15 → 17 properties.** Nothing renamed, retyped, reordered or deleted. **No row
value written. All 217 `Freshness` values untouched. No `Confidence` touched.**

**Repository records required** (no live write): `field_count_verified: 17`; the two fields with
their validations; `Freshness` re-recorded as **non-governing by decision** rather than merely
*ungoverned by omission*; OD10 recorded **closed by dissolution** with the reasoning; the `Stale`
rule's new trigger recorded in `SECTOR_WRITE_CONTRACT.md`; S01's skill updated so it authors the two
dates; and truth-gate `check 7c` extended.

**Not included and explicitly out of scope:** `Source Tier` (OD8 — and DB 6's multi-source problem
would apply immediately), `Source URL` (OD9), any row backfill, any `Confidence` change.

---

## 7. S10 implications

| | Before | After D (schema only) | After D + a future backfill |
|---|---|---|---|
`confidence_threshold` | `Medium` from DB 3 | **unchanged** | unchanged |
`freshness_requirement` | `UNRESOLVED` — **fields absent** | `UNRESOLVED` — **fields present, values null** | computable for DB 3 |
Nature of the failure | **structural, unfixable by backfill** | **ordinary null — fixable** | resolved |

🟢 **The valuable change is in the *kind* of failure, not the verdict.** Today DB 3's freshness
contribution is **permanently** unresolved; after D it is **merely empty**. That converts a dead end
into ordinary outstanding work — exactly the `absent field` versus `present-but-null cell`
distinction Step A wrote into Step 4.

**The packet floor stays `UNRESOLVED` either way**, because DB 9 and DB 10 contribute nulls on both
floors. **Nobody should read this proposal as unblocking S10.**

One S10 text change would follow: DB 3's row in the Step 4 table moves from
**`FIELD DOES NOT EXIST`** to **`null on all 217`**, and the note that DB 3 is *"the binding
constraint … unfixable by any backfill"* must be corrected, since after D it becomes fixable.

---

## 8. Tests and rollback plan

**Rollback is clean, and the reason is structural:** both new properties start **null on every
row**, so the inverse of each write is dropping an empty column. **No row value exists to restore.**
`Freshness` and `Confidence` are never touched, so the only populated fields on these rows are never
at risk.

**Pre-write assertions** (abort on mismatch; repair nothing): DB 3 live field count is **15**;
`Freshness` populated 217/217 and all `Fresh`; `Confidence` populated 217/217 with 3 High / 214
Medium / 0 Low; `Evidence` populated 217/217; `Last Verified` and `Next Review` **absent**; row
count exactly 217.

**Post-write verification:** **17** properties; the two new fields present exactly once each, typed
date, nullable; **both null on all 217 rows**; every pre-existing property unchanged **by
select-option ID**, not merely by name; `Freshness` still `Fresh` ×217; `Confidence` unchanged;
row count still 217.

**Failure handling:** one attempt per property, no retry. If the first succeeds and the second
fails, **stop and report the partial state** — do not roll back, do not repair.

**Offline tests to add:**

1. DB 3 records 17 fields with `field_count_verified: 17`.
2. `Last Verified` and `Next Review` recorded date, nullable, **null on all 217 rows**.
3. `Next Review` is the recorded name — **not** `Next Verification`.
4. `Freshness` recorded **non-governing by decision**, still `Fresh` ×217, still written by S01.
5. **No threshold is defined anywhere** — and OD10 is recorded closed **by dissolution**, not by
   choosing a number.
6. The `Stale` rule's trigger is recorded as `Next Review` in the past.
7. `Confidence` untouched: 3 High / 214 Medium / 0 Low.
8. S10 Step 4 shows DB 3 as `null on all 217`, and the *unfixable-by-backfill* claim is corrected.
9. OD12's three classifications recorded, with **H1 flagged for correction and H2/H3 not**.
10. The `Sub-Sector` finding recorded as a new open item with its total **unmeasured**.
11. OD4, OD5, OD7, OD8, OD9, OD11 and the new `Sub-Sector` item all still OPEN.
12. No claim that any High row is `HIGH_SUPPORTED`.

Extend `check 7c` to assert the 17-field count, the two date fields' nullability, the
non-governing record, and that no threshold exists. **Mutation-test each.**

---

## 9. Limitations

1. **Nothing is implemented.** No live value changed; both decisions remain open.
2. **No source was followed or verified.** Every source statement reports what a property
   *asserts*. In particular, neither regulatory claim (H2, H3) was checked against its authority.
3. **Only 3 of 217 page bodies were read** this task, plus 6 in the prior audit. **208 bodies
   remain unread** and are not characterised.
4. **The estate-wide `Sub-Sector` null count is unmeasured** — two confirmed, total unknown.
5. **No relation target was read.** H1's sub-sector was observed as present and non-Target by
   reference comparison only; DB 2 was not read.
6. **`createdTime` was deliberately not used** as a provenance or freshness basis anywhere in this
   assessment, though it was visible.
7. **Whether H2's and H3's regulatory facts are still accurate was not assessed** — only whether the
   record supports `High`. H2's own stated milestone has demonstrably passed.
8. **DB 3 only.** No other database's freshness field was re-examined live; §2's map is from
   repository contracts.

---

## 10. Exact owner approval wording

```
DB3-OD10-OD12-1 — APPROVE OPTION D AND THE OD12 CLASSIFICATIONS.

[ ] APPROVED as proposed
[ ] APPROVED WITH AMENDMENTS (list below)
[ ] REJECTED
[ ] DEFERRED

OD10 — adopt Option D. Authorize exactly TWO additive live schema writes on DB3
only:
  - add `Last Verified`, type date, nullable;
  - add `Next Review`, type date, nullable (NOT `Next Verification`).
One creation attempt per property, no retry on an ambiguous result. If the
first succeeds and the second fails, stop and report the partial state; do not
roll back and do not repair.

Record OD10 as CLOSED BY DISSOLUTION: no Fresh/Aging/Stale threshold is defined
or needed, because `Freshness` becomes NON-GOVERNING by decision and the dates
govern. Record that the 30-day and 90-day horizons were examined and are NOT
reusable - the 30-day rule governs prospect-score decay and signal proximity,
the 90-day rule governs repository metadata age and signal proximity, and
neither measures a finding's age.

Record that `Freshness` remains REQUIRED by the Intelligence-Object Contract, is
still authored by S01, keeps all 217 `Fresh` values, and that those values become
NON-GOVERNING rather than false.

Record the `Stale` rule's trigger for the first time: a row past its `Next
Review` is stale, and stale intelligence must not drive downstream execution
without revalidation.

Do NOT write any row value. Do NOT backfill any date. Do NOT touch `Freshness`,
`Confidence`, `Source` or `Evidence`. Do NOT add `Source Tier` or `Source URL`
(OD8, OD9 stay open). Do NOT make `Freshness` a derived or formula property.
Do NOT touch DB1, DB2, DB6, DB7, DB9, DB10 or any other database.

OD12 — record the three classifications as assessed:
  - H1 (predictive-hire signal): HIGH_OVERSTATED. Source `chat`, Evidence cites
    an internal Arika draft only, page body blank, no external evidence.
  - H2 (CSRD delay): HIGH_UNRESOLVED.
  - H3 (FSMA 204 delay): HIGH_UNRESOLVED.
Record that H1 REQUIRES a confidence correction and that H2 and H3 do NOT.

H1's correction is a SEPARATE decision and is NOT authorized here. Choose its
disposition in a later task: ______________________________ .
Do NOT change any Confidence value in this task.

Record as a NEW OPEN ITEM that `Sub-Sector` is null on H2 and H3 against a
REQUIRED validation, and that the estate-wide count is UNMEASURED. Do not
measure it in this task.

Record that OD4, OD5, OD7, OD8, OD9 and OD11 all remain OPEN, and that nothing
Sector-wide is ratified.

Preserve byte-identical: all 217 DB3 row values; every pre-existing DB3 property
including option IDs; DB6, DB9 and DB10 contracts and live state; delivery files;
fixture logs and authorization registries; event files; Full Push Packet and PG
gates; all SYNCO artifacts.

All offline suites and all four non-runtime gates must pass. Mutation-test the
gate extension. Stop after the two schema writes and the repository records.

Owner: ______________________  Date: __________
```

---

**Status at close: PROPOSAL · NOT IMPLEMENTED · NO LIVE VALUE CHANGED · OD10 OPEN · OD12 OPEN.**
