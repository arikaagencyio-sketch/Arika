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
if ANY contributing item has a null Last Verified  ->  UNRESOLVED, naming each such element
else  ->  the EARLIEST non-null `Next Review` is the consumer's rejection date,
          stated alongside the OLDEST non-null `Last Verified`
```

**No assembly date may ever substitute for `Last Verified`.** **Absent dates stay UNRESOLVED** — they are not filled, defaulted or inferred, and no global decay threshold is applied, because the repository defines none.

> **The live field name is `Next Review`**, not `Next Verification`. DB 7 and DB 14 use the latter; DB 1, DB 2, DB 9 and DB 16 use the former. Read the name the store actually carries.

**What this means in practice today:** an Accommodation packet's **both floors resolve to `UNRESOLVED`**. *Corrected 2026-10-02 by `DB6-DB10-PROV-1` Step 1 — the previous wording named DB 9 as the only cause, which under-stated it. There are **three** contributing elements, and naming only one would let a reader think fixing DB 9 clears the floor.*

| Element | `Confidence` | `Last Verified` | What it contributes |
|---|---|---|---|
| **DB 9** audience | null on all 4 rows | null on all 4 | `UNRESOLVED` on **both** floors |
| **DB 6** linguistics | **`Medium` on all 4 rows** | **null on all 4** | **confidence floor `Medium`; freshness floor `UNRESOLVED`** |
| **DB 10** decision-makers | null on all 57 | null on all 57 | `UNRESOLVED` on **both** floors |

**Name every contributing element, not just the first.** Four more facts belong in the packet's own words:

1. **DB 6 carries a populated `Confidence` with an EMPTY `Source`.** The value is real and is **not** to be cleared or downgraded — it has a recorded basis in the S02 run record and in each page body. But a confidence with no governed source is **not** the same as a sourced one, and a packet must not present it as though it were. This is **open decision OD1**, and **rule V3 is deliberately NOT extended to DB 6** — do not apply it, and do not report DB 6 as non-compliant with a rule that does not govern it.
2. **`Evidence` does not exist in DB 6's or DB 10's live schema.** Only DB 9 has it. So for those two elements the *substance within the source* cannot be carried in-schema at all, whatever any row holds. Adding it is **open decision OD3**.
3. **Multi-source rows have no defined tier mapping.** `Source Tier` and `Source URL` are each **single-valued**, while DB 6's S02-written rows cite four sources at mixed tiers. There is **no convention** for collapsing them — **open decision OD2**. Do not invent one inside a packet, and do not report a single tier as if it covered every source.
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
