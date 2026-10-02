# DB6 — OD1 / OD2 Resolution Proposal

> 🔴 **PROPOSAL · NOT IMPLEMENTED · NO LIVE VALUE CHANGED · OD1 OPEN · OD2 OPEN**
>
> Nothing in this document has been enacted. No live Notion value was written, cleared or
> changed. No repository contract, gate, test or skill was edited to enact it. `Confidence`
> remains `required: true` on DB 6, its four `Medium` values are untouched, and both open
> decisions remain **OPEN** in `contracts/sector-databases.json`.
>
> **Prepared:** 2026-10-02 · **Author:** Claude Code (Opus 5) · **Live calls made:** 2, both
> read-only, both against DB 3 · **Writes performed:** 0

**Version:** 1.0

---

## 0. The decision in one page

**OD1 cannot be resolved the way the approval hoped.** The Step 2 report said the choice was
"binary and clean" once `Evidence` existed. Investigation shows it is not: **three of DB 6's four
rows can be fully supported, and the fourth cannot be supported at all without inventing
evidence.**

| | Can `Source` be populated? | Can `Evidence` be populated? | V3 after migration |
|---|---|---|---|
| **R2 Operator** | ✅ four titled sources | ✅ substance + read-depth caveats | ✅ **PASS** |
| **R3 Amplifier** | ✅ four titled sources | ✅ substance + read-depth caveats | ✅ **PASS** |
| **R4 Enabler** | ✅ four titled sources | ✅ substance + stated weakness | ✅ **PASS** |
| **R1 Buyer** | ❌ four **bare vendor names**, no titles, no locators | ❌ **nothing in the body isolates evidence** | ❌ **FAIL** |

So the owner's stated preference — *"prefer no exception if all four rows can be supported
honestly"* — **is not satisfiable**. It was the right preference; the facts do not allow it.

**Recommended:** keep `Confidence.required: true`, write **13 truthful cells** across the four
rows, and record **one named, expiring exception for R1 only** — not a standing exception for
"historical DB 6 rows", which would be a permanent loophole covering three rows that can be fixed
properly.

**Recommended OD2 convention:** **Option A, amended** — `Source` carries all contributing
authorities with their per-source tier in the text; `Evidence` carries the substance and the
read-depth caveats; **`Source Tier` and `Source URL` stay NULL**, because the row is genuinely
multi-valued and those fields are single-valued. A null there is the honest answer, not a gap.
**Local to DB 6 only.**

---

## 1. Preconditions verified

| Check | Result |
|---|---|
Step 2 committed in git HEAD | ✅ 7 files, the Step 2 authorised set |
Working tree clean before this task | ✅ |
DB 6 records 19 fields | ✅ `field_count_verified: 19` |
`Evidence` exists, nullable text | ✅ recorded NULL on every row |
Four DB 6 `Confidence` values are `Medium` | ✅ 4 of 28 cells populated |
`Source` and `Evidence` null | ✅ |
`Confidence` remains `required: true` | ✅ and carries no V3-style validation |
OD1 and OD2 remain OPEN | ✅ |

Read before analysis: `DB6-DB10-PROV-AUDIT-1`; `DB9-PROV-AUDIT-1`; the single S02 skill-run record
and its seven `evidence_refs`; the DB 6 page-body findings the audit captured; DB 9's validation
rules V3–V6 and DB 6's own recorded field validations; S10 Step 4's provenance aggregation;
`intelligence-object.schema.json`.

---

## 2. Four-row provenance matrix

**Live now** (7 provenance fields × 4 rows = 28 cells; 4 populated):

| Row | Lens | Created | `Confidence` | `Source` | `Evidence` | `Source Tier` | `Source URL` | `Last Verified` | `Next Review` |
|---|---|---|---|---|---|---|---|---|---|
| **R1** | Buyer | 2026-08-19 | `Medium` | null | null | null | null | null | null |
| **R2** | Operator | 2026-08-24 | `Medium` | null | null | null | null | null | null |
| **R3** | Amplifier | 2026-08-24 | `Medium` | null | null | null | null | null | null |
| **R4** | Enabler | 2026-08-24 | `Medium` | null | null | null | null | null | null |

**Body provenance available** (what the page bodies actually assert):

| Row | Written by a logged run | Sources named | Titled? | Tiers labelled | Tier spread | Verification date | Next-review date | Read-depth caveat |
|---|---|---|---|---|---|---|---|---|
| **R1** | ❌ none | 4 | ❌ **bare names only** | ❌ | — | ✅ 2026-08-19 | ❌ absent | scope caveat only |
| **R2** | ✅ S02 `CREATE` | 4 | ✅ | ✅ | T3 + T4×3 | ✅ 2026-08-24 | ✅ 2026-11-24 | ✅ explicit |
| **R3** | ✅ S02 `CREATE` | 4 | ✅ | ✅ | T2×3 + T3 | ✅ 2026-08-24 | ✅ 2026-11-24 | ✅ explicit |
| **R4** | ✅ S02 `CREATE` | 4 | ✅ | ✅ | T3 + T2×2 + T4 | ✅ 2026-08-24 | ✅ 2026-11-24 | ✅ explicit |

**R1 is structurally different from the other three, and that difference is the whole of OD1.**
R1 predates the skill-run log and no logged run names it. R2–R4 were written by one S02 run whose
own `confidence_matches_evidence` gate recorded why `Medium` was the ceiling. R1 has no such
record anywhere.

---

## 3. Exact proposed values

### 3.1 R1 — Buyer · **1 cell**

| Field | Proposed | Why |
|---|---|---|
| `Source` | **NULL — leave unwritten** | The body names four vendor/publication names with **no document titles and no locators**. DB 6's own `Source` validation requires *"the authority the claim comes from — re-followable"*. Four bare names are not re-followable. Transcribing them would put a non-conforming value into a governed field and make the row *look* sourced. The names stay where they already are: in the page body. |
| `Evidence` | **NULL** | **No body statement isolates substance within any source.** The one candidate sentence is a *scope caveat* — that the patterns come from industry sources rather than a specific property — which limits the claim rather than evidencing it. |
| `Last Verified` | **`2026-08-19`** | Explicitly stated in the body as a verification date. The only truthful cell on this row. |
| `Next Review` | **NULL** | No review date is asserted anywhere for this row. Deriving one from R2–R4's `2026-11-24` would be inventing a date for a row verified five days earlier by a different, unlogged process. |
| `Source Tier` | **NULL** | No tier is labelled. Assigning one from a vendor name is prohibited inference. |
| `Source URL` | **NULL** | No URL asserted. |
| `Confidence` | **unchanged `Medium`** | Not cleared. See §7. |

### 3.2 R2 — Operator · **4 cells**

`Source` (proposed, verbatim):

> Hospitality Net — "Mastering hotel Revenue Management: the essential role of pickup and pace"
> (T3 trade press); Lighthouse — "Hotel revenue management: the complete guide" (T4 vendor
> content, discovery only); Otelier — "Hotel Revenue Manager: Daily Checklist" (T4 vendor
> content, partially gated — public summary only); roommaster — "Hotel Performance Metrics: the
> 2026 KPI Guide" (T4 vendor content)

`Evidence` (proposed, verbatim):

> Pickup and pace as the leading indicators with ADR and RevPAR as the lagging ones, the
> displacement test applied to group business, and index performance (RGI / MPI / ARI) read
> against the comp set — the substance drawn from the four sources above. TIER AND READ-DEPTH
> CAVEAT, carried from the page body: three of the four sources are vendor-published, and under
> write contract 4.4 a T4 source may discover but may NOT confirm — this row is usable for
> language and framing and must not be cited as authority for market fact. One source was read
> only as its public summary. Re-source to a T1/T2 publisher at the next review.

`Last Verified` **`2026-08-24`** · `Next Review` **`2026-11-24`** — both explicit in the body.

### 3.3 R3 — Amplifier · **4 cells**

`Source` (proposed, verbatim):

> HSMAI Commercial Strategy Conference (T2 — the industry body itself, primary for how this
> population frames its own agenda); HSMAI Global — "Perspective: Building and Optimizing a
> Commercial-Focused Team and Strategy" (T2 industry body); HSMAI Americas — "Commercial Strategy
> Accelerates" (T2 industry body); PhocusWire — "Breaking Out of the Silo" and "Does Your Hotel
> Need a Commercial Strategist?" (T3 trade press)

`Evidence` (proposed, verbatim):

> The convergence thesis — marketing, revenue optimization, sales and distribution collapsing
> into one commercial function inside hotel companies — stated directly by the three T2
> industry-body sources, which are primary for how this population frames its own agenda. READ
> DEPTH CAVEAT, carried from the page body: the two PhocusWire items were seen only as
> search-result summaries and were NOT read directly. They are recorded because they corroborate
> the thesis the T2 sources state outright, NOT as independent evidence. Read them or drop the
> reference at the next review.

`Last Verified` **`2026-08-24`** · `Next Review` **`2026-11-24`**.

### 3.4 R4 — Enabler · **4 cells**

`Source` (proposed, verbatim):

> Hospitality Net — "Hotel Tech Partner vs. Vendor: Knowing the Difference and Why It Matters"
> (T3 trade press, read in full); Oracle Hospitality — Partner Integration programme (T2 for its
> own programme); IDeaS — Certified Integration Partners (T2 for its own programme);
> HotelTechConsultant (T4)

`Evidence` (proposed, verbatim):

> The partner-not-vendor identity, the rejection of a "sell and release" quota model, and
> referral-rather-than-force-fit behaviour — evidenced directly by the T3 source, which was read
> in full. "Repeatable integrations", ISV framing and marketplace placement from the two T2
> programme sources, each primary for its own programme. "Vetting and technical evaluation"
> language only from the T4 source. STATED WEAKNESS, carried from the page body: the Incentive
> layer (attach rate, installed-base retention) is INFERRED from how those partner programmes are
> structured rather than quoted from them — treat it as a working hypothesis and confirm against
> a partner-programme agreement or a direct conversation before building outreach on it.

`Last Verified` **`2026-08-24`** · `Next Review` **`2026-11-24`**.

### 3.5 Backfill total

| | Cells |
|---|---|
`Source` (R2, R3, R4) | 3 |
`Evidence` (R2, R3, R4) | 3 |
`Last Verified` (all four rows) | 4 |
`Next Review` (R2, R3, R4) | 3 |
| **Truthful proposed backfill** | **13** |
`Confidence` already populated, not rewritten | 4 |
Remaining NULL by design | 11 |
| **Total cells** | **28** |

---

## 4. `Source Tier` and `Source URL` treatment

**Both stay NULL on all four rows. This is the proposal's most important negative
recommendation.**

**Q5 — can `Source Tier` be assigned without a new convention?** **No, on any row.** R2, R3 and R4
each cite four sources at **two or more different tiers**; `Source Tier` is a single-select. R1
labels no tier at all. There is no row where a single tier is simply correct.

**Q6 — can `Source URL` be assigned when multiple sources exist?** **No.** R2–R4 each carry four
locators against one `url` property; R1 carries none.

Three ways to force a value into a single-valued field, and why each is rejected:

| Forced value | What it would say | Why rejected |
|---|---|---|
| **Weakest tier** (T4 on R2 and R4, T3 on R3) | "this row is T4" | **Understates** — it buries the T2 industry-body sources that carry R3 and half of R4. Fail-closed in spirit, but it makes a well-sourced row look poorly sourced, and a reader cannot tell understatement from fact. |
| **Strongest tier** (T2 on R3 and R4, T3 on R2) | "this row is T2" | **Overstates** — exactly the breach the Intelligence-Object contract names: *weak evidence plus high confidence*. It would hide that R3's T3 items were never read. |
| **Primary source only** | "this row has one source" | **Loses three of four sources per row** and erases every read-depth caveat. |

**A NULL here is not an absence of work — it is the accurate statement that the row's tier is not
representable in a single-select.** The per-source tiers are preserved in the `Source` text, where
they remain legible to a human. The cost, stated plainly: **tier and locator stop being
queryable** for DB 6. That cost is real and is the price of not asserting something false.

---

## 5. The Buyer / DB 3 finding

### 5.1 The pointer is **DB 9's**, not DB 6's

The task described "the Buyer row's recorded DB3 pointer" as an input to OD1. It is not DB 6's.

- **DB 9's** Buyer row (`ROLE-BUYER`, Audience Roles) carries a body cross-reference to a Sector
  Intelligence (DB 3) finding, which `DB9-PROV-AUDIT-1` classified `POINTER_ONLY` and did not
  resolve.
- **DB 6's** Buyer row (R1) names four vendor/publication names and **references no DB 3 record
  at all**.

OD1 concerns DB 6. So the pointer was never capable of supplying R1's `Source`. Reported here
because the premise mattered: had it been DB 6's, R1 might have been rescuable.

### 5.2 Resolved anyway — and the chain terminates unsourced

Two bounded read-only calls resolved it. One DB 3 record matches, `Category = Buying Psychology`,
`Confidence = Medium`, `Freshness = Fresh`.

🔴 **Its own `Source` property is the single word `research`.**

That is a bare, non-re-followable value — precisely the class this provenance programme exists to
reject. **The pointer resolves to a record that is itself unsourced**, so it could not supply a
governed `Source` to DB 9's Buyer row either. `DB9-PROV-AUDIT-1`'s `POINTER_ONLY` classification
is confirmed and now **resolved-and-still-insufficient**, which is strictly more than it knew.

### 5.3 One genuinely useful by-product

The DB 3 record's `Evidence` property does carry real substance, and it names a specific document
inline: a **ProStay 2026 revenue-manager guide**. **"ProStay" is one of R1's four bare vendor
names** — so this upgrades one of them from a vendor name to a *titled document*.

**That is a lead for re-sourcing R1. It is not evidence for R1**, for two reasons:

1. **It evidences a different claim.** The DB 3 evidence describes buyer *structure* — the GM+RM
   reporting relationship and its capacity constraint. R1 records *language patterns* (net RevPAR,
   commission leakage, comp-set index). Attaching structural evidence to a linguistic claim would
   misrepresent both.
2. **It is another database's evidence.** `DB6-DB10-PROV-AUDIT-1` lists *"another database's
   evidence"* among the things provenance may not be inferred from. Importing it would breach the
   rule this task operates under.

**Concrete remedy it does enable:** R1's re-sourcing should start from the named ProStay guide,
which is locatable, rather than from four bare names. That is the first action the §7 exception
should require.

### 5.4 A third database shows the same defect — flagged, not expanded

DB 3 holds `Confidence = Medium` against `Source = "research"`. **That is the OD1 pattern exactly:
a populated confidence with no governed, re-followable source.** So OD1's defect class is **not
DB 6-only**, and this was found incidentally in a single-record read, not a survey.

This is **flagged and deliberately not acted on.** It strengthens one existing recommendation:
**OD4 must not be ratified repository-wide** until DB 3 and the remaining databases are audited —
ratifying a standard now would ratify it over records that already breach it.

---

## 6. OD2 — the smallest honest multi-source convention

### 6.1 The three options assessed

**Option A — `Source` holds a concise multi-source summary; `Evidence` holds structured evidence
references; `Source Tier` and `Source URL` stay null.**

- *Information lost:* tier and locator become unqueryable. Real cost.
- *Overstates certainty:* **no.** Every source and every caveat survives in text.
- *Conflicts with field semantics:* **no**, for DB 6. DB 6's `Source` validation asks for a
  re-followable authority — publisher plus document title satisfies that. DB 6 carries **no V4**
  ("`Source Tier` required whenever `Source` is set"); that rule is DB 9's. **It would conflict if
  applied to DB 9**, which is exactly why this convention must stay local.

**Option B — `Source` names the research run; `Evidence` lists all contributing sources;
`Source Tier` takes the weakest tier; `Source URL` null.**

- 🔴 **Rejected on a semantic conflict, not a preference.** The research run is an **internal
  process handle, not an authority**. Putting it in `Source` would make an internal artifact look
  like an external publisher — the exact defect class this whole programme was built to catch, and
  a close cousin of the "declared `emits`" and "Gate 0 row counts" errors already on the record.
- The weakest-tier half also fails on R1, which has no tiers to take a minimum over.
- *Does one part survive?* Yes: the run id is worth recording — but in `Evidence` as traceability,
  never in `Source`.

**Option C — select one primary source, omit the others.**

- 🔴 **Rejected: it overstates certainty and loses the most.** It discards three of four sources
  per row and every read-depth caveat. On R3 it would present an unread T3 item or a T2 source as
  "the" source. This is the only option that makes a row look *better* sourced than it is.

### 6.2 Recommended — **Option A, amended**

> **DB 6 local multi-source convention (proposed, not ratified)**
>
> 1. `Source` lists **every** contributing authority as *publisher — "document title"*, each
>    followed by **its own tier in parentheses**, semicolon-separated.
> 2. `Evidence` states the substance those sources support, and **must carry any read-depth or
>    inference caveat** the page body records (not read / summary only / inferred).
> 3. `Source Tier` and `Source URL` are **NULL whenever a row cites more than one source.** The
>    null means *not representable in a single-valued field*, not *unknown*.
> 4. A row citing exactly **one** source may populate `Source Tier` and `Source URL` normally.
> 5. The research-run id, where one exists, goes in `Evidence` as traceability — **never** in
>    `Source`.
> 6. **Local to DB 6.** It is **not** ratified for DB 9, DB 10 or any other database, and it
>    **must not** be applied to DB 9, whose V4 requires a tier whenever a source is set.

The amendment over plain Option A is **rule 1's inline per-source tier**: it keeps tier
information legible instead of letting it evaporate, without pretending the select can hold it.

**What this convention costs, stated honestly:** DB 6 can no longer be filtered or grouped by
source tier, and no row-level URL is machine-readable. Anyone needing either must read `Source`.
**What it refuses to do:** manufacture a single tier, a single URL, or a single source where the
row genuinely has four.

---

## 7. OD1 — the `Confidence.required` rule

### 7.1 The three options assessed

| | Truthful | Backward-compatible | S02 authoring | S10 fail-closed | Future enforcement | Migration risk |
|---|---|---|---|---|---|---|
| **1. Keep required, populate all four, apply V3** | ❌ **requires inventing R1's `Evidence`** | ✅ | ✅ strongest | ✅ | ✅ | low — but **unreachable honestly** |
| **2. Make `Confidence` optional, clear unsupported values** | ⚠️ honest about R1, but **destroys a real judgement** | ❌ weakens the rule for every future row | ⚠️ S02 may omit confidence entirely | ✅ null → `UNRESOLVED`, stricter for R1 | ❌ weaker | 🔴 **highest** — the only option that deletes a live value |
| **3. Keep required, explicit exception for historical DB 6 rows** | ✅ if the exception is narrow | ✅ | ✅ | ✅ | ⚠️ depends entirely on scope | low |

**Option 1 is unreachable.** It needs `Evidence` on R1, and no body statement supplies any. The
only way to make V3 pass on R1 is to write evidence that does not exist.

**Option 2 is the most destructive fix available for the narrowest problem.** It changes a schema
rule affecting every future row, and clears a judgement that — however thinly sourced — a person
actually made, in order to repair **one** row. It also discards information: `Medium` records that
someone assessed this row and did not rate it `High`.

**Option 3 as written is too broad.** "Historical DB 6 rows" covers all four. Three of them can be
supported properly, so a blanket historical exception would permanently excuse rows that need no
excuse — a standing loophole.

### 7.2 Recommended — **Option 3, narrowed to one named row, with an expiry**

> **Proposed:** keep `Confidence.required: true` on DB 6. Write the 13 truthful cells. Record
> **one** exception, scoped to **R1 (Buyer) alone**:
>
> - **Named:** the Buyer role-lens row, identified by role lens and creation date — not a class of
>   rows.
> - **Reason recorded:** `Confidence = Medium` is asserted in the page body; its four sources are
>   bare vendor names with no titles or locators, and **no body statement isolates evidence**. So
>   `Source` and `Evidence` must stay null and V3 cannot pass.
> - **Not cleared:** the `Medium` stands. It is a real judgement with a weak but stated basis.
> - **Expires on an owner-set date**, recorded in the exception, **not** in `Next Review` — which
>   stays null because no body asserts one. The expiry is an owner judgement about how long to
>   tolerate a known breach; it is not an evidence claim, so it does not belong in a governed
>   date field.
> - **Required action before expiry:** re-source R1, starting from the ProStay guide named in
>   §5.3. On expiry with no re-sourcing, `Confidence` is cleared — which then needs
>   `required: true` revisited, or the row rewritten by S02.

### 7.3 Why keeping `required: true` is the stronger choice

`required: true` and V3 **compose into something stricter than DB 9 has**: if `Confidence` must
always be set, and any non-null `Confidence` demands `Source` and `Evidence`, then **S02 cannot
create a DB 6 row without provenance at all.** DB 9, where `Confidence` is optional, permits a row
with no confidence and no source.

So DB 6's `required: true` is not an inconvenience to be relaxed — **it is the forcing function
that makes V3 bite on creation.** Option 2 would trade that away to fix one legacy row.

### 7.4 The S10 rule gap this exposes

⚠️ **A finding, not a proposed change.** S10 Step 4's freshness floor fails closed on a null
`Last Verified` but says nothing about a null `Next Review`:

```
if ANY contributing item has a null Last Verified  ->  UNRESOLVED
else  ->  the EARLIEST non-null `Next Review` is the consumer's rejection date,
          stated alongside the OLDEST non-null `Last Verified`
```

After the proposed migration all four DB 6 rows have a non-null `Last Verified`, but **R1's
`Next Review` is still null**. As written, the rule skips the fail-closed branch and takes the
*earliest non-null* `Next Review` — `2026-11-24`, from R2–R4. **R1 would silently inherit a review
date it does not have**, which is the one behaviour this rule exists to prevent.

Not fixed here: S10 is outside this task's scope, and the gap is pre-existing rather than caused by
this proposal. **It should be settled in the same decision as OD1**, because this migration is
what makes it reachable. The minimal fix is one clause: *a null `Next Review` on any contributing
item also yields `UNRESOLVED`.*

### 7.5 What the migration does **not** unblock

**The packet floor stays `UNRESOLVED` either way.** DB 9 contributes nulls on both floors and DB 10
contributes nulls on both across all 57 rows. Improving DB 6 changes the *reason* the floor is
unresolved, not the *result*. Nobody should read this proposal as unblocking S10.

---

## 8. V3 result per row after the proposed migration

V3: *a non-null `Confidence` requires a non-null `Source` **and** a non-null `Evidence`.*

| Row | `Confidence` | `Source` | `Evidence` | **V3** |
|---|---|---|---|---|
| **R2** Operator | `Medium` | ✅ 4 titled sources | ✅ substance + caveats | ✅ **PASS** |
| **R3** Amplifier | `Medium` | ✅ 4 titled sources | ✅ substance + caveats | ✅ **PASS** |
| **R4** Enabler | `Medium` | ✅ 4 titled sources | ✅ substance + weakness | ✅ **PASS** |
| **R1** Buyer | `Medium` | ❌ null | ❌ null | ❌ **FAIL — named exception** |

**3 of 4 pass. V3 is not extended to DB 6 as an enforced rule by this proposal** — extending it is
a separate decision, and it should not be enforced while R1 is in breach unless the exception is
recorded first.

**Q7 — is `Medium` supported once `Source` and `Evidence` are populated?** For R2–R4, **yes**, and
`Medium` is specifically the *right* value rather than merely a permitted one: each body states why
`High` was unavailable (no T1/T2 primary confirmation of language patterns; no primary interview
evidence; a layer inferred rather than stated). For R1, **no** — `Medium` remains an assertion with
no governed support.

**Q9 — what remains ambiguous:**

1. **R1's four vendor names.** Whether any is re-followable is unknown without research this task
   does not authorise. Only ProStay is now identifiable, via DB 3.
2. **Tier queryability for DB 6** is given up under the recommended convention.
3. **Whether V3 should be enforced on DB 6 at all**, or stay a documented expectation.
4. **The expiry date for R1's exception** — an owner judgement, with no evidential basis to derive.
5. **DB 3's own `Source = "research"`** — out of scope, newly surfaced, unresolved.

---

## 9. Exact live writes implementation would make

**13 row-value writes across 4 rows in 1 database. No schema change. No `Confidence` write.**

| # | Row | Field | Value |
|---|---|---|---|
1 | R1 | `Last Verified` | `2026-08-19` |
2 | R2 | `Source` | §3.2 text |
3 | R2 | `Evidence` | §3.2 text |
4 | R2 | `Last Verified` | `2026-08-24` |
5 | R2 | `Next Review` | `2026-11-24` |
6 | R3 | `Source` | §3.3 text |
7 | R3 | `Evidence` | §3.3 text |
8 | R3 | `Last Verified` | `2026-08-24` |
9 | R3 | `Next Review` | `2026-11-24` |
10 | R4 | `Source` | §3.4 text |
11 | R4 | `Evidence` | §3.4 text |
12 | R4 | `Last Verified` | `2026-08-24` |
13 | R4 | `Next Review` | `2026-11-24` |

**Explicitly NOT written:** any `Confidence` value · any `Source Tier` · any `Source URL` · R1's
`Source`, `Evidence` or `Next Review` · anything in DB 9, DB 10 or DB 3 · any schema property.

Expected call count: **4 pre-write reads, 4 row updates (one per row), 4 post-write reads** — or 2
reads + 4 updates + 2 reads if batched per database. One attempt per row, no retry.

---

## 10. Validation and rollback plan

**Rollback is unusually clean, and worth stating because it is a property of this specific
migration:** every one of the 13 target cells is **currently null**. The inverse of each write is
therefore exactly "set back to null" — there is no prior value to reconstruct and nothing to
restore from memory. `Confidence` is never touched, so the only populated cells on these rows are
never at risk.

**Pre-write assertions** (abort on any mismatch, repair nothing):

1. DB 6 live field count is **19**; all seven provenance properties present with recorded types.
2. All four rows have `Confidence = Medium` and **all 13 target cells null**.
3. Row count is exactly 4, identified by role lens.
4. Substantive text byte-lengths match the Step 2 fingerprints (R1 218/145, R2 320/152,
   R3 294/152, R4 290/163 for `Surface` / `Words to use`).

**Post-write verification:**

1. Re-read field definitions: still **19** properties, no schema change, option IDs unchanged.
2. Re-read all four rows: the 13 cells hold exactly the proposed values, byte-for-byte.
3. `Confidence` still `Medium` on all four — **unchanged**.
4. `Source Tier` and `Source URL` still null on all four; R1's `Source`, `Evidence` and
   `Next Review` still null.
5. Substantive byte-lengths unchanged.
6. Row count still 4.

**Failure handling:** if any row's write fails or returns ambiguously, **stop**. Do not retry, do
not roll back the rows that succeeded, and report the partial state with the exact cells written.
A partial migration is safe here — the written cells are individually true.

---

## 11. Tests

Offline, to add to `contracts/test_db9_provenance.py`:

1. DB 6 records 13 populated provenance cells after migration (17 of 28 non-null including the
   four `Confidence`), and `backfill_authorised` reflects the authorisation.
2. `Source Tier` and `Source URL` are recorded null on **all four** rows, with the multi-source
   reason stated.
3. R1 is recorded as the **single** named V3 exception; no second exception exists, and the
   exception is **not** phrased as a class of rows.
4. R1's `Source`, `Evidence` and `Next Review` are recorded null, each with its reason.
5. Every proposed `Evidence` value carries its read-depth or inference caveat — asserted per row,
   not globally.
6. `Confidence.required` is still `true` and still carries no V3-style `validation`.
7. The convention is recorded **local to DB 6**; DB 9's V4 is unchanged and DB 10 is untouched.
8. OD2 is recorded resolved-locally; **OD4 and OD5 remain OPEN**, and OD1 is closed only with the
   exception recorded.
9. The research-run id appears in `Evidence` and **never** in `Source`.
10. The DB 3 finding is recorded: pointer is DB 9's, chain terminates at `Source = "research"`,
    and DB 3's own unsupported `Confidence` is flagged without being acted on.

Gate `check 7b` extension: assert the 13-cell count, the all-null tier/URL rule, the single named
exception, and that `required: true` survives. Mutation-test each.

---

## 12. Limitations

1. **Nothing is implemented.** No live value changed; both decisions remain open.
2. **No source was followed or verified.** Every source statement reports what a page body
   *asserts*. The proposed `Source` and `Evidence` text is a faithful transcription of recorded
   assertions, not confirmation that those sources say it.
3. **Only one DB 3 record was read.** DB 3's schema, its other rows and its own provenance are
   unaudited. §5.4 is one incidental observation, not a survey.
4. **R1's vendor names were not researched.** Whether StayNTouch, Mews or HotelPriceWatch published
   anything locatable is unknown.
5. **The exception's expiry date cannot be derived** from any evidence. It is an owner judgement.
6. **The S10 null-`Next Review` gap (§7.4) is reported, not fixed.**
7. **Live drift remains undetectable offline** for DB 3, DB 6, DB 9 and DB 10.
8. **DB 6 only.** DB 9's four rows and DB 10's 57 are untouched and remain as audited.

---

## 13. Exact owner approval wording

```
DB6-OD1-OD2-1 — APPROVE THE BOUNDED DB6 PROVENANCE BACKFILL AND THE LOCAL
MULTI-SOURCE CONVENTION.

[ ] APPROVED as proposed
[ ] APPROVED WITH AMENDMENTS (list below)
[ ] REJECTED
[ ] DEFERRED

Authorize exactly 13 live row-value writes in DB6 only, to the cells listed in
§9, with the values in §3 verbatim:
  - Last Verified on all four rows;
  - Source, Evidence and Next Review on the Operator, Amplifier and Enabler
    rows only.

Do NOT write, clear, alter or re-assert any Confidence value. Do NOT write any
Source Tier or Source URL. Do NOT write R1's Source, Evidence or Next Review.
Do NOT change any schema property. Do NOT touch DB3, DB9 or DB10.

Adopt the §6.2 multi-source convention as LOCAL TO DB6 ONLY. Do not apply it to
DB9 or DB10 and do not ratify it Sector-wide. Record that DB9's V4 is unchanged.

Keep Confidence.required: true on DB6. Record ONE named exception for the Buyer
row only, with its reason, and an expiry date of: ______________ .
The exception must not be phrased as a class of rows. Record that on expiry
without re-sourcing, the Confidence value is cleared and required: true is
revisited.

Do not extend validation rule V3 to DB6 as an enforced rule in this task.
Record it as a documented expectation with the Buyer-row exception named.

S10 null-Next-Review gap (§7.4): [ ] fix in this task  [ ] separate decision.

Row-level: one write attempt per row, no retry on an ambiguous result. On any
failure, stop and report the partial state; do not roll back and do not repair.

Preserve byte-identical: DB9's and DB10's live schemas and all their row values;
DB3 entirely; DB6's schema and all four Confidence values; delivery files;
fixture registries and logs; event files; Full Push Packet and PG gates; all
SYNCO artifacts.

Record that OD2 is resolved LOCALLY for DB6, that OD1 is closed only with the
exception recorded, and that OD4 and OD5 remain OPEN. Record the §5.4 DB3
finding as a new open item; do not act on it.

All offline suites and all four non-runtime gates must pass. Mutation-test the
gate extension. Stop after the backfill.

Owner: ______________________  Date: __________
```

---

**Status at close: PROPOSAL · NOT IMPLEMENTED · NO LIVE VALUE CHANGED · OD1 OPEN · OD2 OPEN.**
