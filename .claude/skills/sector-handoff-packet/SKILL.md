---
name: sector-handoff-packet
description: Skill S10 of Sector (01). The only sanctioned exit from the department. Assembles the handoff packet — findings, language, audience, offer match, timing, CRM tags — and routes it by the correct mechanism per destination, which differs. Reports a handoff into a destination it cannot reach as HANDOFF_FAILURE rather than performing it silently. Use when a sector reaches Offer-Ready, at activation Gate G, or when a resolver run produces opportunities. Runs LAST, after every write skill for that sector.
---

# S10 · Sector Handoff Packet

You are performing the **apply** step of Sector's write layer, at its boundary.

**Read [`01_Sector/SECTOR_WRITE_CONTRACT.md`](../../../01_Sector/SECTOR_WRITE_CONTRACT.md) first.** The packet shape: [`AEIT_09 Interface Contract Standard`](../../../00_Agency_Governance/enterprise_architecture/AEIT_09_INTERFACE_CONTRACT_STANDARD.md) §1. Reality states: [`AEIT_11 Runtime Truth Standard`](../../../00_Agency_Governance/enterprise_architecture/AEIT_11_RUNTIME_TRUTH_STANDARD.md). Field truth: [`contracts/sector-databases.json`](../../../01_Sector/contracts/sector-databases.json). Live routing truth: [`contracts/event-catalog.json`](../../../01_Sector/contracts/event-catalog.json).

> **This is the only sanctioned exit from the department.** Everything Sector produces — findings, signals, language, audience, routes, destination profiles, resolutions — stays inside until it leaves through here. That is why this skill's job is **not** to move as much as possible. It is to move what it can, **by a mechanism that actually delivers**, and to say plainly what it could not move.

---

## Step 0 · Check the route before you build the packet

**The mechanism differs per destination, and three of them do not work today.** Verify against the live catalog every run — do not trust this table, which is dated.

| Destination | Mechanism | Reality state | Works? |
|---|---|---|---|
| **Content (04)** | native relation — 9 available | `CONNECTED` | ✅ |
| **Offer (02)** | relation + text reference | `CONNECTED` | ✅ |
| **ClickUp CRM** | free-text ID tags on `Lead`: `sector`, `sub_sector`, `icp_tier`, `offer_id` | **`CONNECTED`** — the four tag fields exist; a direct connector write round-tripped (SECTOR-CW2), and on 2026-09-29 **S10 itself wrote, read back and deleted** one disposable fixture task (SECTOR-SF2). **No real `Lead` has ever been tagged and no hand-off has been observed arriving** *(was `DESIGNED`, no target, 2026-09-22)* | ⚠️ |
| **Sales (05)** | **event only** | `CONNECTED` subscriber, **no observed delivery** | ❌ |
| **Marketing (03)** · **Operations (08)** | **event only**, and that event is `DEMAND_SHIFT` | **`DESIGNED`** — archived 2026-08-28 (31d) | ❌ |

> 🔴 **An event route does not deliver, however well subscribed.** `executor.ts` returns `emitted` and **never publishes**; the bus's only `publish()` call site is an inbound external webhook. So a `CONNECTED` event has a verified listener and **no observed delivery** — `AEIT_11` R2: *a state is never inherited.*
>
> **Consequence: Marketing (03) and Operations (08) have no working route from Sector at all**, because their only route was an event now archived. **Sales (05) is reachable in principle and not in fact.** Say this in the run report; do not let a packet look delivered because it was assembled.
>
> **Updated 2026-09-29:** the four `Lead` tag fields exist; SECTOR-CW2 proved a written value survives a read-back, and **SECTOR-SF2 then had this skill do it** — one disposable fixture task, tagged, read back, deleted. So the mechanism is available **and exercised by S10**. It is still **not** a delivery: no real `Lead` has been tagged, and nothing has been observed arriving at a real record. On an ordinary run, **read the tags back from the task before recording anything other than `HANDOFF_FAILURE`** — assembled is not delivered, and neither is written-without-reading. *(Before 2026-09-29 the route had no target at all.)* `ICP Fit Score` does exist on that list, but it is a score, not a tier, and is **not** a substitute for `icp_tier` *(corrected 2026-09-22: an earlier note called it Sales-set; `AEIT_05` R1, ratified 2026-07-22, makes Sector the setter and Sales the consumer)*.

## Step 1 · `HANDOFF_FAILURE` is a result, not an error

When the route does not deliver, **report `HANDOFF_FAILURE`, keep the packet, and name the destination.**

**Do not** perform the handoff silently. **Do not** discard the packet. **Do not** substitute a working route for a broken one — routing a Marketing packet into Content because Content happens to work is how a department's intelligence ends up in the wrong store with nobody's name on it.

A `HANDOFF_FAILURE` is the most useful thing this skill produces on a broken route: it converts an invisible gap into a named, dated one.

## Step 2 · The packet shape

Per `AEIT_09` §1, every packet carries: `handoff_id` · `producer`/`consumer` · `trigger` · `payload` · `validation_rules` · `confidence_threshold` · `freshness_requirement` · `owner` · `SLA / cadence` · `failure_modes`.

**The payload may carry only canonical entities** (`AEIT_06`). A handoff needing a non-canonical shape is a signal to extend the model, **not** to invent a local one.

**What Sector puts in the payload:** the finding (pain), the signal (timing), the language (DB 6), the audience and title (DB 9/DB 10), the offer match or `GAP — needs OEOS` (DB 8), the destination profile and route where place-bound (DB 16/DB 15).

## Step 3 · The boundary law — angle, never artifact

`SECTOR_ACTIVATION_CONTRACT.md` §14.3. Sector emits **timing · pain · language · who · offer-match · outreach *angle***.

It does **not** write the final email, the proposal, or the script. That is **Sales (05)** enablement and **Content (04)**. *An angle is what to say and why now; an artifact is the saying of it* — and the moment this skill writes the artifact, two departments own the same object.

## Step 4 · Freshness and confidence travel with the packet

A packet inherits the **weakest** thing in it. A finding at `Confidence = Low`, or a signal at `Needs verification`, caps the packet — say so in `confidence_threshold` rather than letting the consumer assume.

**Never hand off a `Needs verification` or `Superseded/Delayed` signal** as if settled. `freshness_requirement` is the consumer's right to reject on age; state the real `Last Verified`, not the assembly date.

### The two floors are computed, and they fail closed

*Added by `DB9-PROV-1`, 2026-10-02. Before this, neither floor could be expressed for the audience element at all, because DB 9 carried no provenance in-schema.*

**`confidence_threshold`**

```
ORDER:  Low < Medium < High          — the only confidence scale Sector uses
if ANY contributing item has a null Confidence  ->  UNRESOLVED, naming each such element
else                                            ->  the weakest value on ORDER
```

**A null is UNASSESSED, and null is weaker than `Low`.** `Low` is a judgement someone made; null is the absence of one. Never read null as `Low` — that would let an unexamined row inherit a floor the other elements earned.

**`freshness_requirement`**

```
if ANY contributing item has a null Last Verified
   OR a null Next Review                          ->  UNRESOLVED, naming each such element
else  ->  the EARLIEST Next Review is the consumer's rejection date,
          stated alongside the OLDEST Last Verified
```

*The `Next Review` half of that condition was added 2026-10-02 by `DB6-OD1-OD2-1`. Before it, the
rule failed closed on a missing `Last Verified` but said nothing about a missing `Next Review` —
so a row with no review date of its own would have silently taken the **earliest non-null** one
from its siblings. That is the exact substitution this rule exists to prevent, and it became
reachable the moment DB 6's dates were partly populated.*

**Both dates are required from every contributing record before either floor may be computed.**
`UNRESOLVED` is not a failure state to be worked around — it is the answer, and it must **name the
record or audience element** that is unresolved so the consumer knows which one to chase.

🔴 **A row's null `Next Review` may NEVER be filled from another row's.** Not from the earliest,
not from the latest, not from a sibling in the same database, not from a department default.
**No assembly date, no current date and no global decay threshold may substitute for either
date.** **Absent dates stay UNRESOLVED** — they are not filled, defaulted or inferred, because the
repository defines no decay threshold and a borrowed date is a fabricated one.

**DB 6 after the `DB6-OD1-OD2-1` backfill, as a worked example:** the Operator, Amplifier and
Enabler rows each carry an explicit `Last Verified` (2026-08-24) and `Next Review` (2026-11-24).
The **Buyer** row carries an explicit `Last Verified` (2026-08-19) but **its `Next Review` is
null**, and no body asserts one. **So the DB 6 freshness contribution is `UNRESOLVED`, naming the
Buyer row** — even though three of its four rows are now fully dated, and even though a
`2026-11-24` sits one row away. That is the rule working, not the rule failing.

> **The live field name is `Next Review`**, not `Next Verification`. DB 7 and DB 14 use the latter; DB 1, DB 2, DB 9 and DB 16 use the former. Read the name the store actually carries.

**What this means in practice today:** an Accommodation packet's **both floors resolve to `UNRESOLVED`**. *Corrected twice, both times for the same reason — under-counting the contributing elements. Step 1 (2026-10-02) replaced wording that named DB 9 as the only cause and listed **three**. `DB3-PROV-1` Step A (2026-10-02) then found the table itself omitted DB 3. There are **four** contributing elements, and naming fewer lets a reader think fixing one clears the floor.*

| Element | `Confidence` | `Last Verified` | `Next Review` | What it contributes |
|---|---|---|---|---|
| **DB 3** findings | **`Medium` on all 6 Target rows** | **FIELD DOES NOT EXIST** | **FIELD DOES NOT EXIST** | **confidence floor `Medium`; freshness floor `UNRESOLVED` — structurally, not emptily** |
| **DB 9** audience | null on all 4 rows | null on all 4 | null on all 4 | `UNRESOLVED` on **both** floors |
| **DB 6** linguistics | **`Medium` on all 4** | **all 4 populated** | **3 of 4 — Buyer null** | **confidence floor `Medium`; freshness floor `UNRESOLVED`, naming the Buyer row** |
| **DB 10** decision-makers | null on all 57 | null on all 57 | null on all 57 | `UNRESOLVED` on **both** floors |

*DB 3 added as the fourth element 2026-10-02 by `DB3-PROV-1` Step A, from `DB3-PROV-AUDIT-1`. It was **missing from this table while Step 4's own prose named findings as a confidence contributor** — "A finding at `Confidence = Low` … caps the packet". The table named three of four contributing elements, which is the same class of omission Step 1 corrected when the table named DB 9 alone.*

**DB 3's behaviour, because it differs from the other three in kind:**

- **Confidence contributes normally.** All 217 rows carry a governed `Confidence`, and all six Accommodation rows are `Medium`. DB 3 never triggers a null-driven `UNRESOLVED` on the confidence floor.
- **`Evidence` is REQUIRED and populated on 217 of 217 rows.** Five of the six Target rows name re-followable sources inline; one does not.
- 🔴 **`Source` is a process-kind dimension, not an authority.** Its four values — `xlsx` · `chat` · `agent run` · `research` — record **how** a finding was obtained, never **who** published it. **Never read `Source` as the authority and never report a row as unsourced because `Source` looks generic** — the locator lives in `Evidence`.
- 🔴 **Freshness contributes `UNRESOLVED`, and no backfill can change that.** DB 3 has **no `Last Verified` and no `Next Review` field at all**. **An absent field is a different fact from a present-but-null cell. Both fail closed, but only the second could ever be filled.** Say which one you are reporting.
- 🔴 **No assembly date, current date, or `Freshness` label may substitute for a missing verification date.** DB 3's `Freshness` is `Fresh` on all 217 rows with **no threshold defined anywhere**, so it cannot age and carries no temporal information. It is a declaration, not a measurement.
- ⚠️ **Restrictions recorded only in page bodies can be lost.** Two Target rows state limits on how the finding may be used — one that it may not drive a downstream execution without stronger confirmation, one that a particular reading would be overclaiming. **No field carries either.** A packet assembled from properties alone silently drops both, so **read the body before relying on a DB 3 finding**, and do not treat property-completeness as permission.
- ⚪ **Three DB 3 rows carry `Confidence = High`, none of them Target rows. Their bodies were outside the authorised audit, so make no claim about them** — neither that they are sound nor that they are not.

*DB 6's row updated 2026-10-02 by `DB6-OD1-OD2-1`, which populated 13 cells. Note what did and did
not change: DB 6 is the **best-provenanced** of the four elements on the fields it has, and it
**still** contributes an `UNRESOLVED` freshness floor, on the strength of **one** missing
`Next Review`. One null is enough. **DB 3 is the harder case: it cannot be fixed by any backfill,
because the fields do not exist** — so as DB 9 and DB 10 are remediated, **DB 3 becomes the binding
constraint on the freshness floor.** The packet floor was `UNRESOLVED` before the backfill and is
`UNRESOLVED` after it — the
backfill improved the data, not the verdict.*

**Name every contributing element, not just the first.** Four more facts belong in the packet's own words:

1. **Three of DB 6's four rows are now properly sourced; the Buyer row alone is not.** *(Updated 2026-10-02 by `DB6-OD1-OD2-1`. The previous wording — "DB 6 carries a populated `Confidence` with an EMPTY `Source`" — was true of all four rows and is now true of one.)* The Operator, Amplifier and Enabler rows carry a `Source`, an `Evidence` and both dates, each `Evidence` keeping its read-depth or inference caveat verbatim. The **Buyer** row still carries `Medium` against an empty `Source` and `Evidence`: its body names four bare vendor names with no titles or locators, and nothing in it isolates evidence. **OD1 is CLOSED with one named exception covering that row only, expiring 2026-11-24.** The value is **not** to be cleared or downgraded. **Rule V3 is a DOCUMENTED EXPECTATION for DB 6, not an enforced validator** — do not apply it as a hard rule, and when reporting the Buyer element say it is *excepted*, not *compliant*. **A sourced row and an excepted row must never be reported the same way.**
2. **`Evidence` exists structurally in DB 6, DB 9 and DB 10. It is populated on three DB 6 rows and null everywhere else.** *(Field added 2026-10-02 by `DB6-DB10-PROV-1` Step 2 — OD3 CLOSED. Values written to DB 6's Operator, Amplifier and Enabler rows 2026-10-02 by `DB6-OD1-OD2-1`.)* **DB 9's four rows and all 57 DB 10 rows still carry a null `Evidence`.** **A null `Evidence` continues to force an UNRESOLVED provenance floor** — closing the schema gap closed nothing about the rows that are still empty. **No confidence or freshness value may be inferred from the fact that a field exists.** A column is a place to put evidence, not evidence; treat a present-but-empty `Evidence` as the absence it is, and never report an element as sourced because the store now has somewhere to record a source.
3. **DB 6's multi-source rows deliberately carry a NULL `Source Tier` and `Source URL`.** *(Convention adopted 2026-10-02 by `DB6-OD1-OD2-1` — **OD2 closed LOCALLY FOR DB 6 ONLY**.)* Both properties are **single-valued** while each S02-written row cites four sources at mixed tiers, so the null means **not representable in a single-valued field**, not *unknown*. Per-source tiers travel **inline in the `Source` text** — read them there. 🔴 **This convention is NOT ratified for DB 9, DB 10 or Sector-wide, and must NOT be applied to DB 9**, whose rule V4 requires a tier whenever a source is set. Any Sector-wide question stays **open decision OD4**. Do not invent a tier inside a packet, do not report a single tier as if it covered every source, and **do not read DB 6's null tier as a missing value to be filled**.
4. **Null and unsupported both fail closed.** A null is `UNASSESSED` and is weaker than `Low`. A populated value whose supporting provenance is absent does **not** earn the floor its value suggests. **When in doubt, `UNRESOLVED`** — and **no assembly date may ever substitute for `Last Verified`**, for any element.

**Do not fall back to the `Medium` that DB 6 and the other elements would have set.** A packet may be assembled and must declare an unresolved floor; it may **not** be reported as a complete hand-off, and no consumer may act on one.

> **A `basis: owner_reasoning` P2 rule may filter a calendar; it may not be quoted to a client.** If the packet's reasoning rests on unratified plugin rules, mark it — the consumer is often the department that would quote it.

## Step 5 · Verify, log

Read every cross-boundary write back. Append to `01_Sector/_memory/skill_runs.jsonl` per [`contracts/skill-execution-record.schema.json`](../../../01_Sector/contracts/skill-execution-record.schema.json) with `skill_id: "S10"`, recording **each destination, its mechanism, and whether it delivered** — a run that reached two of five destinations reports five outcomes, not two.

Loops: `activation`, `feedback`.

> **The feedback loop cannot close.** No performance store exists anywhere in the agency (`SECTOR_OS_ARCHITECTURE.md` §1.3). A packet can be delivered; it **cannot** be scored. Never infer that a handoff worked from the fact that it was sent.

---

## Refuse

- **A handoff into a destination with no working route, performed silently.** Report `HANDOFF_FAILURE`.
- Substituting a reachable destination for an unreachable one.
- A fabricated contact — a name, an email, or a title not in DB 10 or the CRM.
- Writing the final email, proposal or script. Sector emits the **angle**.
- Handing off a `Needs verification` or `Superseded/Delayed` signal as settled.
- A payload carrying a non-canonical entity shape.
- Claiming delivery from assembly. **Assembled is not delivered.**
- Running before the sector's write skills have completed for that sector.

<!-- FIXTURE-MODE:BEGIN -->
## Fixture mode — `TEST_FIXTURE` · prepared, **DISABLED**

> 🔴 **Disabled.** This mode runs only under a Sector fixture authorisation whose status is
> **`approved`** in [`contracts/skill-fixture-authorisations.json`](../../../01_Sector/contracts/skill-fixture-authorisations.json).
> The only one, **SECTOR-SF1, was spent on 2026-09-22** after its one attempt; none is `approved`, **so refuse.** Ordinary use of this skill never enters
> this mode. **A001 is excluded:** its skill records stay deferred under A001 D6 (T1-4).

**What it is for.** Exercising this skill's *mechanism* on an independently labelled synthetic
Sector record, without delivering anything anywhere: the route check, the per-destination
recording, the packet shape, the boundary law and the confidence cap.

**Refuse unless every one of these holds:**

1. The authorisation named is `approved`, for `sector-handoff-packet` / `S10`.
2. The synthetic record at the authorisation's path matches its pinned sha256, and is marked
   `TEST_FIXTURE` and `synthetic: true`.
3. `01_Sector/_memory/skill_runs-sandbox.jsonl` holds no record for that authorisation, since its
   limit is one.
4. `python 01_Sector/contracts/skill_run_gate.py` passes **before** the run.
5. Nothing in the input names A001 or a pilot ID.

**Steps.** Each replaces its ordinary counterpart **only inside this mode**:

- **F0 · Inputs.** Read only the synthetic record and repository files. **Read no Notion
  database, no ClickUp and no connector.** Fields the ordinary packet would take from live
  databases (DB 3, DB 4, DB 6, DB 7, DB 8, DB 9, DB 10, DB 15, DB 16 — *corrected 2026-09-22: SECTOR-SF1's run found the first list omitted DB 4, 8, 15 and 16*) are left out and listed in
  `payload.fixture.not_read_fixture`.
- **F1 · Route check.** As in Step 0: re-measure the routes from `contracts/event-catalog.json`,
  a repository file.
- **F2 · Outcomes.** For every destination, record `{destination, mechanism, outcome}` in
  `payload.destinations`:
  - a route the authorisation **explicitly permits this fixture to exercise** → **`delivered_fixture_verified`**, and only after the written value has been **read back from the destination** and matched. It is a different token from `delivered` on purpose: a fixture never performs a hand-off;
  - any other route that **would** deliver → **`not_attempted_fixture`**;
  - a route that does **not** deliver → **`HANDOFF_FAILURE`**, exactly as in Step 1. That is true
    in any mode;
  - **never `delivered`.**
- **F3 · No cross-boundary write — unless the authorisation names one.** By default: no Notion relation, no CRM tag, no event. An authorisation may permit **one named, disposable** external write and nothing else; `SECTOR-SF2`, if approved, permits exactly one ClickUp fixture task (create → tag → read back → delete → confirm absence). **Notion, Offer, Content and every event stay forbidden in every fixture.** `payload.writes` and `payload.events` stay empty — they record Notion database writes and emitted events, neither of which a fixture may make — and the permitted write is named in `payload.fixture.external_writes` instead. `decision` stays `NO_OP`.
- **F3a · Clean up once, even after a partial failure.** If an authorised external write created anything, delete it **once** and confirm its absence, whether or not the rest of the run succeeded. **Never retry** a failed step. If cleanup fails, stop and report what remains, by name; never conceal or overwrite it.
- **F4 · Packet.** Write the assembled packet as JSON at the authorisation's `packet` path,
  marked `classification: TEST_FIXTURE`, carrying every AEIT_09 §1 field: `handoff_id`,
  `producer`, `consumer`, `trigger`, `payload`, `validation_rules`, `confidence_threshold`,
  `freshness_requirement`, `owner`, `sla_cadence`, `failure_modes`. Its `confidence_threshold`
  states that the packet is synthetic, which caps everything in it (Step 4). The boundary law
  (Step 3) is unchanged: an **angle**, never an artifact.
- **F5 · Log.** Append **one** record to `01_Sector/_memory/skill_runs-sandbox.jsonl` —
  **never** to `skill_runs.jsonl`, and never touching a record already there. It carries top-level `classification: TEST_FIXTURE` and `payload.fixture` = `{authorisation_id, synthetic_record, packet, not_read_fixture}`, plus `external_writes` and `readback_verified` whenever an authorised external write happened. **The gate refuses any `delivered_fixture_verified` outcome without both.** **Read the timestamp from the clock.**
- **F6 · Close.** Run the gate again; it must pass. Then set the authorisation to `spent`.

**What a fixture run proves, and what it does not.** It can show that the route check, the
per-destination classification, the packet shape and the isolation work. It delivers nothing,
reads no live intelligence, and its payload content is synthetic. **It never produces a fit
verdict, a finding or Sector evidence.**

**Enforcement is detective.** This mode is instructions plus a gate that fails **afterwards** on
any breach. No code prevents a run; the gate makes a violation visible. A write that never reaches
a repository file, such as a Notion call, would not be caught by the gate at all. That is why F0 and
F3 are refusals, not options.
<!-- FIXTURE-MODE:END -->

## Appendix · A dated snapshot — re-measure it, do not trust it

**Measured 2026-08-28.** Hospitality reached **`Offer-Ready`** the same day, so this skill's primary trigger is live for the first time.

**Routes: 3 of 6 destinations deliver.** Content (04), Offer (02) and the ClickUp CRM work by relation and text. **Sales (05) is `CONNECTED` but has no observed delivery. Marketing (03) and Operations (08) have no route at all** — their only one was `DEMAND_SHIFT`, retired to `DESIGNED` on 2026-08-28 under owner decision 31d.

That ratio is the thing to weigh before promising a downstream department anything: **the department can now produce a packet for six consumers and hand it to three.**

**Re-measured 2026-09-22 — owner-authorised connector schema read, one call per connector (target/schema existence only; delivery not tested).** DB 2's five Content relations and its Offer relation exist live and point at their declared targets, so those two mechanisms have real targets. **The CRM row does not:** none of `sector`, `sub_sector`, `icp_tier` or `offer_id` exists on the live `Lead` list. The 2026-08-28 snapshot above is left exactly as measured; on today's evidence the ratio is **two of six destinations with a verified target, and still none with an observed delivery.** **Updated 2026-09-29:** the CRM's four tag fields were created and verified, so **three of six now have a verified target** — still none with an observed delivery.
