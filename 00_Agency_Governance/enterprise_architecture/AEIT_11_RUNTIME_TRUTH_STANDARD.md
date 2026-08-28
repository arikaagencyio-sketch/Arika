# AEIT_11 — Runtime Truth Standard

**Version:** v0.2
**Last updated:** 2026-08-29
**Owner:** Agency Governance (00)
**Status:** Standard — **owner-ratified 2026-08-28**, arising from decision 31d.
**Measured against the whole estate:** [`AEIT_11_ESTATE_AUDIT.md`](AEIT_11_ESTATE_AUDIT.md) — enforced by [`estate_event_gate.py`](estate_event_gate.py).
**Depends on:** `AEIT_06` (canonical entities — the rule that departments consume rather than reinvent), `AEIT_09` (interface contracts).

> **The system must always tell you what exists, what is designed, what is connected, and what is merely intended.**
> — owner, 2026-08-28

---

## 1. The defect this exists to prevent

Every serious error found during the Sector (01) build programme was **one defect wearing different clothes: a claim about the system's state that nothing had verified.**

| The claim | The reality | How it was found |
|---|---|---|
| `emits` chains agents together — declared **199 times** (193 distinct names) | `executor.ts` returns `emitted` and **never publishes**. The only `publish()` call site is an inbound external webhook | reading the runtime |
| Two event edges are "wired", asserted in **four files** | Neither receiving agent has the trigger | grepping `on:` across all 115 agents |
| Agents log to `runtime.jsonl` "on every run" | **The directory did not exist** — proof no agent had ever run | looking for the file |
| 24 signals are `T1 Primary` | Not one was linked to a registered publisher | measuring the relation |
| The property-type rule matrix is complete | It was **sparse**, and the sector's own dominant signal type was ruled by no archetype | building a coverage gate |
| A plugin sidecar records 1 forecast row | Zero, and always zero | counting |
| Database row counts (Gate 0) | Taken from changelogs; **3 of 6 measured were wrong** | querying |

None of these was a lie. Each was **a true statement about intent, filed where a statement about operation belonged.**

**This standard does not add caution. It adds a place to put the intent** — so that recording what a thing *is* costs nothing and never requires overstating it.

---

## 2. The five reality states

One axis, and one question: **does this capability actually operate?**

| State | Means | **The test that proves it** |
|---|---|---|
| `INTENDED` | Someone decided it should exist. No artifact yet. | A decision record names it |
| `DESIGNED` | Specified in enough detail to build. The artifact is a **specification**; nothing executes. | The spec resolves to a named file or section |
| `BUILT` | The executable artifact exists. | It is at a named path |
| `CONNECTED` | It is wired to its counterpart, **and both ends were checked**. | Both ends named **and the edge itself tested** |
| `LIVE` | It has actually produced a result. | **A dated execution record** |

## 3. The seven rules

**R1 · A state may only be claimed with its named test. Without the test, the claim is the state below.**
This is the entire standard. Everything else follows.

**R2 · A state is never inherited.** An agent being `BUILT` does not make its `emits` `CONNECTED`. A publisher being authoritative does not make it reachable. A database existing does not make it populated. A specification being excellent does not make it run. **Each edge and each capability carries its own state and its own test.**

**R3 · `CONNECTED` and `LIVE` decay. Both carry a `last_verified` date and a re-check cadence.**
Reachability is a property of the moment; authority is not. Three government hosts were unreachable on one date and answered four days later — because the block had been recorded as a *state* rather than as a downgrade of the publisher, promoting them cost one call instead of a re-argument.

**R4 · Downgrade is ordinary reporting, not failure.** A capability moving `LIVE → BUILT` because its verification lapsed is the standard working. **Treat a downgrade as information; never as something to avoid producing.**

**R5 · Retire to `DESIGNED`. Never delete the intent.**
Removing something from the runtime contract **archives the design and strikes the operational claim** — it does not erase the architecture. *Deleting the intent loses the reasoning; keeping the claim loses the truth.* Do both correctly: keep one, strike the other, and date the change.

**R6 · Three axes exist and must not be merged.** A thing can be `LIVE` and badly sourced.

| Axis | Question | Vocabulary |
|---|---|---|
| **Reality** | Does it operate? | **this standard** |
| **Evidence** | How well-sourced is the content? | plugin honesty states 🟢🟡🔴⚫⬜◐ |
| **Reachability** | Can we still follow the publisher? | source `State`: candidate / active / superseded / archived |

**R7 · Absence has three states, and they need three different remedies.**
A thing that is missing is not one condition. **Nobody owns it** needs a *decision*. **Someone owns it and has not built it** needs a *build*. **Nothing internal should own it — it arrives from outside, or from a person** needs *nothing but a label*.

| Absence | Remedy | The mistake it prevents |
|---|---|---|
| Producer / owner **unassigned** | An ownership decision | Building the wrong thing, fast |
| Producer / owner **named but unbuilt** | A build | Re-litigating ownership that was already settled |
| Producer is **external or human, by design** | A label, and nothing else | Reading a working design as a break, and “fixing” it |

*This rule exists because the three were collapsed.* On 2026-08-28 a database field was reported as having **no owner**; an audit of all 311 fields found **311 of 311 owned**. The field had an owner and **the owner was unbuilt** — a different state, with a different remedy, and the report sent the reader to the wrong one. **Never write “missing” without saying which of the three it is.**

## 4. This is not a fourth vocabulary — it is the one three places already improvised

Per `AEIT_06`, *departments consume canonical entities; they do not reinvent them.* Three local vocabularies were invented independently for the same idea. They map onto §2 rather than being replaced piecemeal:

| Where | Local value | Reality state |
|---|---|---|
| `01_Sector/contracts/event-catalog.json` | `LIVE` | `CONNECTED` — subscriber verified; **not `LIVE`, because nothing publishes** |
| " | `LIVE_BUT_INTRA_DEPARTMENT_ONLY` | `CONNECTED`, with the boundary named |
| " | `DEAD` | `DESIGNED` — the event is specified and has no subscriber |
| Source registry (DB 14) | `candidate` / `active` | reachability axis (R6) — **not** a reality state |
| `AEIT_06` | `[CANDIDATE]` entity | `DESIGNED` |
| Plugin slots | ⬜ unauthored / ◐ partial | evidence axis (R6) |

**`DEAD` is retired as a value.** It conflates *"specified and unsubscribed"* with *"broken"*, and it reads as a defect when it is usually an honest design state.

## 5. How to apply it

**On any claim that a thing works:** name the test, run it, record the state and the date. If you cannot run the test, claim the state below and say which test you could not run.

**In prose:** a capability's first mention in any OS file carries its state. *"The Resolution Engine (`DESIGNED`)"* costs four words and prevents a reader from planning against something that does not run.

**In JSON contracts:** `reality_state` + `reality_test` + `last_verified`.

**On any absence:** say which of R7's three it is. “No producer” is not a finding; *“no producer has been assigned”*, *“the assigned producer is unbuilt”* and *“the producer is the accounting system”* are three findings with three different owners.

**Make the test runnable wherever it can be.** A described gate decays; a gate with an exit code does not. `estate_event_gate.py` re-derives the estate's reality states on demand and fails on an unclassified absence — including the parser bug that would have made the whole estate look clean.

**The cheapest possible version, and the one that matters most:** when you write a sentence claiming something operates, **ask what you would run to prove it.** If the answer is *"nothing — it's in the spec"*, that is `DESIGNED`.

---

## 6. Changelog

- **v0.2 (2026-08-29) — R7 added; first estate-wide measurement.** Run across all 115 agents and the 20 departments that carry them — see [`AEIT_11_ESTATE_AUDIT.md`](AEIT_11_ESTATE_AUDIT.md). **R7 (absence has three states)** generalised from a correction: a field reported as unowned was owned-and-unbuilt. Of the estate's **74 orphaned waits**, 4 are external entry points, 59 are manual, and **11 are genuinely unassigned** — 6 of them in Presence (21) alone. Corrects §1's `emits` count from 196 to **199** (193 distinct names); the earlier figure matched neither quantity. Ships [`estate_event_gate.py`](estate_event_gate.py), falsified the same day. — Claude Code (Opus 5)

- **v0.1 (2026-08-28) — created; owner-ratified.** Arising from owner decision **31d**: *retire the dead events from the active runtime contract, but archive the intent — "the system should always tell you what exists, what is designed, what is connected, and what is merely intended."* Generalised from seven verified instances of one defect found across the Sector (01) build programme, all of which were **true statements about intent filed where statements about operation belonged**. Retires `DEAD` as a catalog value. Establishes the three orthogonal axes so the Reality axis does not absorb the Evidence and Reachability vocabularies that already exist. — Claude Code (Opus 5)
