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
| **ClickUp CRM** | free-text ID tags on `Lead`: `sector`, `sub_sector`, `icp_tier`, `offer_id` | `CONNECTED` | ✅ |
| **Sales (05)** | **event only** | `CONNECTED` subscriber, **no observed delivery** | ❌ |
| **Marketing (03)** · **Operations (08)** | **event only**, and that event is `DEMAND_SHIFT` | **`DESIGNED`** — archived 2026-08-28 (31d) | ❌ |

> 🔴 **An event route does not deliver, however well subscribed.** `executor.ts` returns `emitted` and **never publishes**; the bus's only `publish()` call site is an inbound external webhook. So a `CONNECTED` event has a verified listener and **no observed delivery** — `AEIT_11` R2: *a state is never inherited.*
>
> **Consequence: Marketing (03) and Operations (08) have no working route from Sector at all**, because their only route was an event now archived. **Sales (05) is reachable in principle and not in fact.** Say this in the run report; do not let a packet look delivered because it was assembled.

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

## Appendix · A dated snapshot — re-measure it, do not trust it

**Measured 2026-08-28.** Hospitality reached **`Offer-Ready`** the same day, so this skill's primary trigger is live for the first time.

**Routes: 3 of 6 destinations deliver.** Content (04), Offer (02) and the ClickUp CRM work by relation and text. **Sales (05) is `CONNECTED` but has no observed delivery. Marketing (03) and Operations (08) have no route at all** — their only one was `DEMAND_SHIFT`, retired to `DESIGNED` on 2026-08-28 under owner decision 31d.

That ratio is the thing to weigh before promising a downstream department anything: **the department can now produce a packet for six consumers and hand it to three.**
