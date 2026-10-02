# DB9 Provenance Remediation Proposal — `DB9-PROV-1`

> ## 🔴 PROPOSAL · NOT IMPLEMENTED · NO DB9 VALUE CHANGED · NO S10 AUTHORIZATION · NO PACKET ASSEMBLY
>
> Nothing here is in force. No DB9 field was added, no DB9 value was written or read, and
> `sector-databases.json`, the S10 skill, its schemas, `AEIT_09`, every validator, every gate and the
> fixture-authorisation registry are **byte-identical** to their state before this task.

**Raised by:** `SECTOR-PK2` prerequisite **P9**, which found that DB9 carries no governed provenance
while S10 requires `confidence_threshold` and `freshness_requirement` to inherit from the weakest
packet item and to state real verification provenance.

**Scope:** DB9 only. §12 flags the wider standardisation decision **without legislating it**.

---

## 1. Assessment — answers from repository evidence

### Q1. Is there an existing canonical provenance pattern to reuse? **Yes — and DB9 is the only Sector database with none of it.**

Surveyed all sixteen databases in `contracts/sector-databases.json`:

| Element | Established type and values | Databases carrying it |
|---|---|---|
| `Confidence` | `select` — **`Low` · `Medium` · `High`** | **10 of 16:** DB1, DB2, DB3, DB6, DB8, DB12, DB13, DB14, DB15, DB16 |
| `Last Verified` | `date` | DB7, DB14, DB15, DB16 |
| `Next Verification` | `date`, **required** | DB7, DB14 |
| `Next Review` | `date` | DB1, DB2, DB16 |
| `Source` | `text` | DB16 |
| `Source URL` | `url` | DB7, DB16 |
| `Source Tier` | `select` — **`T1 Primary` · `T2 Institutional` · `T3 Commercial-intel` · `T4 Secondary`** | DB7, DB16 |
| `Authoritative Source` | `text` | DB7 |
| `Evidence` | `text` | DB3 |
| `Freshness` | `select` — `Fresh` · `Aging` · `Stale`, **required** | DB3 |
| `Refresh Status` | `select` — `Confirmed` · `Annual-recurring` · **`Needs verification`** · `Superseded/Delayed` | DB7 |

**The closest exemplar is DB16 Destination Profile** — a profile-style record, like an audience role:
`Source` (text, required) · `Source URL` (url) · `Source Tier` (select, required) · `Confidence`
(select) · `Last Verified` (date, required) · `Next Review` (date). **DB7 is the fullest** and adds
`Next Verification` and `Refresh Status`. **`Evidence` comes from DB3.**

**Independent corroboration that DB9 cannot answer the contract today.**
`contracts/intelligence-object.schema.json` encodes the eight questions every Sector intelligence
record must answer, and maps each to real Notion fields — **for DB3 and DB7 only**:

| Question | DB3 field | DB7 field | DB9 |
|---|---|---|---|
| Q2 `source` | `Evidence + Source` | `Authoritative Source + Source URL + Source Tier + Signal Source` | **none** |
| Q3 `when_observed` | `Freshness` | `Last Verified + Next Verification` | **none** |
| Q4 `reliability` | `Confidence` | `Confidence` | **none** |

That mapping is the same finding `sector-databases.json` records as DB9's `MISSING_FIELD`:
*"DB9 carries NO Confidence, Source, Evidence or Last Verified field at all — weaker than DB6, which
at least has Confidence. It cannot satisfy Intelligence-Object questions 2, 3 or 4 in-schema."*

**Nothing needs inventing. Every field below already exists somewhere in Sector.**

### Q2. Exact fields DB9 should add

Six fields, all **additive**, all **nullable**, every name and type copied from an existing database.

| # | Field | Notion type | `field_class` | Required | Allowed values | Pattern taken from |
|---|---|---|---|---|---|---|
| 1 | `Confidence` | `select` | `meta` | **no** | `Low` · `Medium` · `High` | 10 of 16 DBs |
| 2 | `Source` | `text` | `meta` | **no** | — | DB16 |
| 3 | `Source Tier` | `select` | `meta` | **no** | `T1 Primary` · `T2 Institutional` · `T3 Commercial-intel` · `T4 Secondary` | DB7, DB16 |
| 4 | `Evidence` | `text` | `direct` | **no** | — | DB3 |
| 5 | `Last Verified` | `date` | `meta` | **no** | — | DB7, DB14, DB15, DB16 |
| 6 | `Next Verification` | `date` | `meta` | **no** | — | DB7, DB14 |

**Why nullable rather than required**, where DB16 makes `Source` and `Last Verified` required: DB9
already holds four rows for which **no provenance exists anywhere in the repository** (Q8). Making a
field required would force either a fabricated value or a broken record. Nullable-plus-fail-closed
keeps the absence honest and visible. §5 proposes a conditional requirement instead, which is
stricter where it can be.

**Three fields deliberately NOT proposed:**

- **`Source URL`** (DB7, DB16) — omitted because no URL is known for any DB9 row and adding an
  always-empty url field would imply one exists. Add it later if a source is ever established.
- **`Freshness`** (`Fresh`/`Aging`/`Stale`, DB3) — omitted because **the repository nowhere records
  the thresholds** that turn a date into those three states. Deriving it would mean inventing a
  decay rule. DB9 stores the raw dates instead, which is DB7's and DB14's convention.
- **`Refresh Status`** (DB7) — omitted as signal-lifecycle vocabulary; `Confirmed` and
  `Annual-recurring` are meaningless for an audience role. Its one useful token, **`Needs
  verification`**, is reused in §4 as a *reporting* value rather than as a new stored enum.

### Q3. Is Confidence numeric, an enum, an object, or something else? **An enum.**

A Notion `select` with exactly `Low` · `Medium` · `High`, `field_class: meta`. Identical in all ten
databases that carry it — there is no numeric or structured variant anywhere in Sector.

**Do not confuse it with a score.** DB5 Prospect Signal Scores holds a 90-point scorecard and the CRM
holds a numeric `ICP Fit Score`; both are *measurements of a prospect*, not *confidence in a claim*.
Conflating them is the error already corrected once in `CRM_SCHEMA.md` (`ICP Fit Score` is not
`icp_tier`).

### Q4. What qualifies as `Source` versus `Evidence`?

The two are not synonyms, and the Intelligence-Object schema maps **both together** to Q2:

- **`Source` — the authority the claim comes from.** *Who or what said it.* DB16 uses free text
  naming the publisher; DB7 pairs `Authoritative Source` with `Source Tier` and a relation to DB14
  Signal Sources. A source is re-followable: it answers *"where would I go to check this again?"*
- **`Evidence` — the specific substance within that source.** *What exactly it said.* DB3 uses text,
  and the S05 run that wrote DB16 recorded refs at this grain (a named report, *"Table 3, section
  2.17, and the nationality × port-of-entry matrix"*).

So `Source` is the locator and `Evidence` is the citation inside it. **A `Source` with no `Evidence`
is an unchecked pointer; `Evidence` with no `Source` is an unattributable quote.** §5 rule V3 requires
them together whenever either is present.

### Q5. What format does `Last Verified` use?

Notion `date` — an ISO calendar date, as in DB7, DB14, DB15 and DB16. In DB7 and DB14 it is
**required** and always paired with `Next Verification`, also required. DB16 pairs it with
`Next Review`.

### Q6. How is freshness computed from `Last Verified`? **The repository does not define one rule, and this proposal does not invent one.**

Four different treatments exist today:

| Where | Rule | Horizon |
|---|---|---|
| `sector_truth_gate.py` check 5 | *"no `verified_date` in the future; warn on any older than 90 days"* | **90 days** — and this governs row-count verification dates, not record provenance |
| `AEIT_09` §2 HP-1 `validation` | *"score freshness ≤ 30 days (Sector's re-score decay rule)"* | **30 days**, for a prospect score |
| DB3 `Freshness` | `Fresh`/`Aging`/`Stale` | **no thresholds recorded anywhere** |
| DB7, DB14 | an explicit per-record `Next Verification` date | **declared, not computed** |

**Proposal: reuse DB7's and DB14's approach — freshness is declared per record, not computed from a
global threshold.** `Next Verification` carries the date the row stops being trustworthy, and a
consumer compares today against it. This invents nothing, and it is the only one of the four that is
unambiguous. Choosing between the 30-day and 90-day horizons, or defining DB3's thresholds, is a
separate decision flagged in §12.

### Q7. What happens when `Last Verified` is absent? **It fails closed.**

The Intelligence-Object schema makes Q3 `when_observed` **required**, with the reason stated in the
schema itself: *"Freshness is not optional metadata; it is what stops truth decaying into fiction."*
S10 Step 4 then forbids the obvious shortcut: *"state the real Last Verified, not the assembly date."*

So an absent `Last Verified` means the row **cannot** answer Q3, **cannot** contribute a freshness
floor, and **must not** have one substituted. S10's `freshness_requirement` becomes `UNRESOLVED` and
names the element responsible (§8).

### Q8. Can the four existing DB9 rows be populated truthfully from current sources? **No — not from anything the repository holds.**

This was checked rather than assumed:

1. **No skill-run record ever wrote DB9.** All **15** records in `_memory/skill_runs.jsonl` were
   enumerated and their `writes` blocks read. They touched DB1, DB3, DB6, DB7, DB8, DB11, DB12,
   DB14, DB15, DB16 — **never DB9**.
2. **The one S02 run wrote DB6, not DB9**, and its own trigger says so: *"Target: the three DB6 role
   lenses missing against a sub-sector whose DB9 role set is already complete."* **The DB9 rows
   already existed before 2026-08-24**, which is where the run log begins.
3. **Its seven `evidence_refs` therefore belong to DB6.** Attaching them to DB9 rows they did not
   produce would be exactly the fabrication the non-invention rules forbid.
4. **The plugin is a pointer, not a source.** `HOSPITALITY_PLUGIN.md` §P9 reads *"Live — read them in
   their stores, not here."* It confirms the rows exist; it is not evidence for their content.

**One honest unknown.** DB6's own `MISSING_FIELD` note records the current workaround: *"Provenance
must live in the page body until a schema change is ratified."* The DB9 **page bodies may therefore
contain provenance** — and **this task could not look**, because the rows live in Notion and no
connector is authorized. The correct status is **unverifiable from the repository**, not *known
absent*. §11 names the one read-only call that would settle it.

### Q9. Verifiable, derivable, or must stay unknown

| Directly verifiable from the repository | Derivable | Must remain `UNKNOWN` / `Needs verification` |
|---|---|---|
| Row count = 4 (`row_count_verified`, 2026-08-24) | — | `Confidence` |
| All four `Role` values exist: `Operator` · `Buyer` · `Amplifier` · `Enabler` | — | `Source` |
| Each relates to the Accommodation sub-sector | — | `Source Tier` |
| Each carries Content Persona, Access Paths, Primary Signal Type | — | `Evidence` |
| | — | `Last Verified` |
| | — | `Next Verification` |

**Nothing provenance-related is derivable.** A row existing is not evidence for what it says. The
derivable column is deliberately empty.

### Q10. How should S10 compute `confidence_threshold` from the weakest item?

See §8. In short: take the minimum on the ordered scale `Low < Medium < High`, and treat a **null
Confidence as `UNRESOLVED`, which dominates the whole aggregate** rather than being read as `Low`.

Null is weaker than `Low`, because `Low` is an *assessed* value while null is *unassessed*. Reading
null as `Low` would let an unexamined record set a floor, which the Intelligence-Object schema calls
out directly: *"Confidence MUST match the evidence; weak evidence plus High confidence is a
constitutional breach, not a rounding error."*

### Q11. How should S10 state `freshness_requirement`?

See §8. The **earliest** `Next Verification` among contributing items, with the **oldest**
`Last Verified` stated alongside it. If any contributing item lacks `Last Verified`, the result is
`UNRESOLVED` naming that element — never the assembly date.

### Q12. Which tests and gates would need updating?

**Checked, not assumed.** The current state is better than expected:

| Artifact | Needs a change? | Detail |
|---|---|---|
| `contracts/test_skill_fixture.py` (56 tests) | **No** | DB9 appears only inside `not_read_fixture` lists at lines 75 and 385 — declarations that a fixture did *not* read it. **No test pins DB9's field set or the `sector-databases.json` hash**, so the suite does not re-baseline. |
| `contracts/sector_truth_gate.py` | **Optional, recommended** | None of its six checks reads DB9 fields, so nothing breaks. §10 proposes **new check 7** to enforce the §5 rules in a runnable gate rather than in prose. |
| `contracts/skill_run_gate.py` | **No** | Validates skill-execution records; DB9's schema is outside its scope. |
| `contracts/p2_coverage_gate.py` | **No** | Covers P2 archetype cells only. |
| `contracts/sector-databases.json` | **Yes** | The six fields are added to DB9's `fields`, and its `MISSING_FIELD` is **rewritten, not deleted** — it becomes a record of what the schema change closed, with the row-level gap (Q8) still flagged. |
| `contracts/intelligence-object.schema.json` | **Yes** | Q2/Q3/Q4 `notion_field` maps gain DB9 entries. This is the change that makes DB9 contract-answerable. |
| `.claude/skills/sector-handoff-packet/SKILL.md` | **Yes** | Step 4 gains the §8 aggregation and fail-closed rules. **Not touched by this proposal.** |
| `AEIT_09` | **No** | Its §1 field list and §2 examples are unchanged; DB9 simply becomes able to answer them. |
| `01_Sector/SECTOR_NOTION_SCHEMA.md` | **Yes** | The human-readable schema doc must match the JSON. |
| Live Notion DB9 | **Yes** | Six properties added. **The only step that touches live data.** |

### Q13. Would the migration change ordinary Sector behaviour? **No — it makes missing provenance explicit, and makes S10 stricter rather than looser.**

- **Additive only.** Six new fields. No existing field is renamed, retyped, reordered or removed; no
  existing value is written; no existing row is modified. The four DB9 rows keep every value they
  have today and gain six nulls.
- **No new required field**, so no existing row becomes invalid.
- **Ordinary reads are unaffected.** Every skill that reads DB9 today reads the same fields.
- **The one behavioural change is in S10, and it tightens.** Before: `confidence_threshold` and
  `freshness_requirement` could not be expressed at all for the audience element. After: they are
  computed, and because every DB9 row's provenance is null (Q8), **S10 will report `UNRESOLVED` where
  it previously said nothing.** A packet that looked complete will now visibly carry an unresolved
  floor.

**That is the point.** The migration does not make S10 pass; it makes S10 able to *fail honestly*.

---

## 2. Proposed DB9 schema addition

To be appended to DB9's `fields` array in `contracts/sector-databases.json`:

```json
{ "name": "Confidence", "notion_type": "select", "field_class": "meta",
  "purpose_tag": "GOV", "required": false, "writer_skill": "S02",
  "allowed_values": ["Low", "Medium", "High"],
  "validation": "Set ONLY from recorded evidence. Null means UNASSESSED, never Low. A non-null value requires Source and Evidence (rule V3).",
  "pattern_source": "identical to the Confidence field in DB1, DB2, DB3, DB6, DB8, DB12, DB13, DB14, DB15, DB16" },

{ "name": "Source", "notion_type": "text", "field_class": "meta",
  "purpose_tag": "GOV", "required": false, "writer_skill": "S02",
  "validation": "The authority the claim comes from - re-followable. Cited or blank; never a guess.",
  "pattern_source": "DB16.Source" },

{ "name": "Source Tier", "notion_type": "select", "field_class": "meta",
  "purpose_tag": "GOV", "required": false, "writer_skill": "S02",
  "allowed_values": ["T1 Primary", "T2 Institutional", "T3 Commercial-intel", "T4 Secondary"],
  "validation": "Required whenever Source is set (rule V4).",
  "pattern_source": "DB7.Source Tier and DB16.Source Tier, same four values" },

{ "name": "Evidence", "notion_type": "text", "field_class": "direct",
  "purpose_tag": "GOV", "required": false, "writer_skill": "S02",
  "validation": "The specific substance within the Source that supports the row. Cited or blank.",
  "pattern_source": "DB3.Evidence" },

{ "name": "Last Verified", "notion_type": "date", "field_class": "meta",
  "purpose_tag": "GOV", "required": false, "writer_skill": "S02",
  "validation": "The date a qualifying verification actually occurred. NEVER the write date, NEVER a file modification time, NEVER today's date absent a real verification (rule V5).",
  "pattern_source": "DB7, DB14, DB15, DB16" },

{ "name": "Next Verification", "notion_type": "date", "field_class": "meta",
  "purpose_tag": "GOV", "required": false, "writer_skill": "S02",
  "validation": "Required whenever Last Verified is set (rule V6). Freshness is DECLARED per record, not computed from a global threshold the repository does not define.",
  "pattern_source": "DB7.Next Verification and DB14.Next Verification, both required there" }
```

The existing `MISSING_FIELD` entry is **rewritten rather than removed**, so the dated finding
survives:

```json
"MISSING_FIELD": {
  "name": "provenance",
  "note": "SCHEMA GAP CLOSED by DB9-PROV-1: Confidence, Source, Source Tier, Evidence, Last Verified and Next Verification now exist, so DB9 can answer Intelligence-Object questions 2, 3 and 4 in-schema. The ROW-LEVEL gap remains: all four existing rows carry null provenance because no skill-run record ever wrote DB9 and no source is recorded anywhere in the repository. They are UNKNOWN pending verification, not verified-as-absent.",
  "severity": "schema fixed; row-level provenance outstanding"
}
```

---

## 3. Migration behaviour for existing records

1. **Add the six properties to the live DB9. Write no values.** All four rows receive six nulls.
2. **Touch nothing else.** No existing field or value on any row is read for writing, altered or
   reordered.
3. **Do not backfill.** Backfilling would require inventing provenance (Q8).
4. **Record the row-level gap** in `sector-databases.json` per §2, so the absence is documented in
   the repository rather than only in a proposal.
5. **Four rows, six fields, 24 cells — every one null.** That is the truthful outcome.

---

## 4. Truthful proposed values for each current DB9 record

**Source basis for all four: none exists in the repository.** Evidence in Q8.

| Row (`Role`) | `Confidence` | `Source` | `Source Tier` | `Evidence` | `Last Verified` | `Next Verification` |
|---|---|---|---|---|---|---|
| `Operator` | null | null | null | null | null | null |
| `Buyer` | null | null | null | null | null | null |
| `Amplifier` | null | null | null | null | null | null |
| `Enabler` | null | null | null | null | null | null |

**Reported state for every row: `Needs verification`** — reusing DB7's established
`Refresh Status` token rather than coining one. It is a *reporting* value here, not a stored field.

**Citations for leaving them null:**

- `_memory/skill_runs.jsonl` — 15 records, none writes DB9.
- the same log, `s02-2026-08-24-accommodation-language` — wrote DB6 and states DB9 was already
  complete, so its `evidence_refs` are not DB9's.
- `HOSPITALITY_PLUGIN.md` §P9 — *"Live — read them in their stores, not here."* A pointer.
- `contracts/sector-databases.json` DB9 `MISSING_FIELD` — the gap, recorded by the repository itself.
- `contracts/intelligence-object.schema.json` — Q2/Q3/Q4 map to DB3 and DB7 only.

**What was deliberately NOT used as provenance**, per the non-invention rules: the S02 run's
`evidence_refs` · any file modification time · the 2026-08-24 `verified_date` (that verified a *row
count*, not row content) · today's date · the plugin pointer · any SYNCO-01 or SYNCO-02 fixture
result.

### Records that must remain unresolved

**All four, on all six fields, until a qualifying verification occurs.** No row may receive a
`Confidence` value before a `Source` and `Evidence` exist, and none may receive a `Last Verified`
before a verification actually happens.

---

## 5. Validation rules

| ID | Rule | Rationale |
|---|---|---|
| **V1** | `Confidence` ∈ {`Low`,`Medium`,`High`} or null. Null means **UNASSESSED**, never `Low`. | Q10 |
| **V2** | `Source Tier` ∈ the four established values, or null. | DB7/DB16 vocabulary |
| **V3** | **A non-null `Confidence` requires a non-null `Source` AND `Evidence`.** | *"weak evidence plus High confidence is a constitutional breach"* |
| **V4** | A non-null `Source` requires a non-null `Source Tier`. | DB16 makes both required together |
| **V5** | `Last Verified` may be set **only** when a qualifying verification occurred, and must not be in the future. Never the write date, a file mtime, or today's date absent a real verification. | non-invention rules; truth-gate check 5 already forbids future dates |
| **V6** | A non-null `Last Verified` requires a non-null `Next Verification`, strictly later. | DB7/DB14 make both required |
| **V7** | A non-null `Next Verification` requires a non-null `Last Verified`. | a decay date with no baseline is meaningless |
| **V8** | No fixture result — SYNCO-01, SYNCO-02 or any other — may ever be cited as DB9 `Source` or `Evidence`. | fixture boundaries: mechanism evidence only |
| **V9** | Adding these fields must not alter any existing DB9 field or value. | §3, backward compatibility |

---

## 6. Weakest-item aggregation for S10 `confidence_threshold`

Implements S10 Step 4 — *"A packet inherits the weakest thing in it"* — for the first time
computably.

```
ORDER:  Low < Medium < High          (the only scale Sector uses)
UNRESOLVED is not on this scale and DOMINATES it.

confidence_threshold(items):
    if any item's Confidence is null       -> "UNRESOLVED", naming each such element
    else                                   -> min(Confidence) on ORDER

A null is UNASSESSED, not Low. Low is a judgement; null is the absence of one.
```

**Applied to an Accommodation packet today:** the audience element (DB9) has null `Confidence` on all
four rows, so `confidence_threshold` = **`UNRESOLVED`**, naming the audience element. Finding, signal,
language, offer-match and destination elements all carry a real `Confidence` and would otherwise have
set a `Medium` floor — the packet's readiness-packet PG2 row already states *"Sector findings are
Medium"*.

**The packet must state the unresolved floor rather than fall back to `Medium`.** Falling back would
let four unexamined rows inherit a floor set by other elements.

---

## 7. Freshness calculation for S10 `freshness_requirement`

```
freshness_requirement(items):
    if any item lacks Last Verified  -> "UNRESOLVED", naming each such element
    else:
        oldest_last_verified = min(Last Verified)
        earliest_next_verification = min(Next Verification)
        state both; the earliest Next Verification is the consumer's rejection date

NEVER substitute the assembly date.                       (S10 Step 4, verbatim)
NEVER apply a global decay threshold.                      (none is defined - Q6)
```

**Applied today:** `UNRESOLVED`, naming the audience element.

---

## 8. Fail-closed behaviour

| Situation | Required behaviour |
|---|---|
| Any contributing item has null `Confidence` | `confidence_threshold: UNRESOLVED`, offending elements named |
| Any contributing item has null `Last Verified` | `freshness_requirement: UNRESOLVED`, offending elements named |
| Either is `UNRESOLVED` | The packet **may be assembled and must declare it**. It may **not** be reported as a complete hand-off, and no consumer may act on an unresolved floor. |
| A row has `Confidence` but no `Source`/`Evidence` | **V3 violation — reject the row, do not downgrade the confidence.** |
| Provenance is missing | It stays missing. **No optimistic default, and S10 is never weakened to accommodate the absence.** |

**S10 is not relaxed anywhere by this proposal.** Every rule above is a new way for it to decline to
claim something, which is the opposite of making it pass.

---

## 9. Backward compatibility and rollback

**Compatibility.** Six additive nullable fields; no rename, retype, reorder or removal; no value
written; no new required field; every current reader unaffected; the 56-test Sector suite needs no
re-baseline (Q12).

**Rollback.** Clean, because nothing is populated:

1. Remove the six properties from the live DB9 — **no data is lost, since all 24 cells are null**.
2. Revert DB9's `fields` and `MISSING_FIELD` in `sector-databases.json`.
3. Revert the DB9 entries in `intelligence-object.schema.json`.
4. Revert S10 Step 4 and `SECTOR_NOTION_SCHEMA.md`.
5. Re-run the suites and the four gates.
6. **Leave the decision-log entry in place, marked reverted** — dated history is never rewritten.

**Rollback stops being clean the moment a real provenance value is written.** From then on, removing
the fields destroys evidence, and rollback becomes a schema decision with data loss.

---

## 10. Test matrix for implementation

| # | Test | Asserts |
|---|---|---|
| T1 | DB9 carries all six fields with the exact names, types and `allowed_values` of §2 | schema applied |
| T2 | Every `allowed_values` list is byte-identical to its pattern source (DB16 `Source Tier`, DB3 `Confidence`, …) | reuse, not a variant |
| T3 | None of the six is `required: true` | no existing row invalidated |
| T4 | DB9's pre-existing 14 fields are unchanged in name, type, order and `required` | V9 |
| T5 | V3: a `Confidence` with null `Source` or null `Evidence` is rejected | — |
| T6 | V4, V6, V7: the paired-field rules hold in both directions | — |
| T7 | V5: a future `Last Verified` is rejected | aligns with truth-gate check 5 |
| T8 | All four existing rows report null on all six fields | §4, no silent backfill |
| T9 | `confidence_threshold` returns `UNRESOLVED` — not `Low`, not `Medium` — when any item's Confidence is null | §6 |
| T10 | `confidence_threshold` returns the minimum when every item is assessed | §6 |
| T11 | `freshness_requirement` returns `UNRESOLVED` when any `Last Verified` is null, and never the assembly date | §7 |
| T12 | An unresolved floor names the offending element | §8 |
| T13 | V8: a fixture result is rejected as `Source` or `Evidence` | fixture boundary |
| T14 | `intelligence-object.schema.json` maps DB9 for Q2, Q3 and Q4 | the contract is answerable |
| T15 | The 56 existing Sector tests, the runtime suite and all four gates still pass | no regression |

**Proposed new gate check — `sector_truth_gate.py` check 7:** assert DB9's six fields exist with their
established vocabularies, and that V3/V4/V6/V7 hold for every row the contract records. *"A described
gate decays; a gate with an exit code does not."*

---

## 11. The one call that could change §4

A **single read-only** Notion read of the four DB9 rows would establish whether their **page bodies**
hold the provenance DB6's note says lives there. If they do, §4's nulls become real values with real
citations, and the migration becomes a genuine backfill rather than six columns of nulls.

**It is not authorized here and was not performed.** It needs its own decision: one read-only call,
four rows, no write, no other database, and nothing beyond the fields named in §2.

---

## 12. Flagged separately — the cross-database decision this proposal does NOT make

**Three databases share this gap, all written by S02:**

| DB | Gap recorded in `sector-databases.json` |
|---|---|
| **DB6** Sector Linguistics | *"carries Confidence but NO Source, Evidence, Last Verified or Next Review field … Provenance must live in the page body until a schema change is ratified."* |
| **DB9** Audience Roles | *"NO Confidence, Source, Evidence or Last Verified field at all."* ← **this proposal** |
| **DB10** Decision-Maker Registry | *"No Confidence, Source or Last Verified field."* |

**This proposal covers DB9 only, by instruction.** It does not amend DB6 or DB10, and it does not
establish a repository-wide provenance standard.

**But it would be the third local fix to the same defect, and that is worth saying plainly.** The
separate decision available to the owner is whether to ratify **one Sector provenance standard** —
the six fields in §2, applied uniformly to DB6, DB9 and DB10, and named as the pattern for any future
database. Deciding that *after* DB9 ships risks DB9 becoming a fourth variant rather than the
template. **Recommendation: take the DB9 fix now and the standardisation decision next, not
silently.**

Two further open questions this proposal deliberately leaves alone: DB3's `Freshness`
`Fresh`/`Aging`/`Stale` thresholds are undefined, and the **30-day** (prospect-score decay) and
**90-day** (truth-gate warning) horizons have never been reconciled.

---

## 13. Decision-log and changelog updates implementation would require

| File | Entry |
|---|---|
| `01_Sector/SECTOR_OS.md` §8 | Decision **DB9-PROV-1**: the six fields, that all four rows stay null and why, the S10 Step 4 change, and that it closes PK2's **P9** at schema level while the row-level gap stays open. |
| `01_Sector/SECTOR_OS.md` §15 | Dated changelog line, newest first. |
| `01_Sector/SECTOR_NOTION_SCHEMA.md` | The six fields, matching the JSON exactly. |
| `01_Sector/SECTOR_WRITE_CONTRACT.md` | S02's write surface gains six fields; note that writing `Confidence` requires `Source` and `Evidence` (V3). |
| `.claude/skills/sector-handoff-packet/SKILL.md` Step 4 | The §6–§8 aggregation and fail-closed rules. |
| `contracts/sector-databases.json` | §2's fields and rewritten `MISSING_FIELD`. |
| `contracts/intelligence-object.schema.json` | DB9 entries under Q2, Q3, Q4. |

**Honest note for the §8 decision entry:** this change makes S10 report `UNRESOLVED` on Accommodation
packets where it previously reported nothing. **That is a visible regression in apparent packet
completeness and a real improvement in honesty.** The entry should say so, so nobody later reads the
new `UNRESOLVED` as a bug.

---

## 14. Owner approval

```
DB9-PROV-1 PROVENANCE REMEDIATION
[ ] APPROVED as proposed
[ ] APPROVED WITH AMENDMENTS (list below)
[ ] REJECTED
[ ] DEFERRED

Amendments / notes:
_______________________________________________

Owner: ______________________  Date: __________
```

See the task report for the exact approval wording.

---

## 15. Limitations

1. **Nothing here is implemented.** No field exists, no value changed, no schema or gate was edited.
2. **The four DB9 rows were not read.** They live in Notion and no connector is authorized. §4's
   nulls reflect *the repository's* silence, not a verified absence — §11 names the call that would
   settle it.
3. **Confidence and freshness values are not proposed for any row**, because none can be sourced
   truthfully today. Six columns of nulls is the honest first state.
4. **No freshness threshold is proposed.** The repository defines none, and §12 flags the two
   unreconciled horizons.
5. **This closes P9 at schema level only.** PK2's other blockers — P4 (authorisation), P5 (trigger),
   P7/P8 (real pilot), P10 (delivering routes) — are untouched, and **packet assembly remains
   blocked**.
6. **Mechanism evidence only.** Nothing here is evidence about a market, demand, pricing, buyers,
   capacity, performance or any real property.
