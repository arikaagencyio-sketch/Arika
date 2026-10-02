# Sector Delivery — `SECTOR-DELIVERY-P10` Assessment and Proposal

> ## ✅ IMPLEMENTED AND VERIFIED 2026-10-02 — see §0 before reading further
>
> | | |
> |---|---|
> | **P10 internal acknowledgement mechanism** | **CLOSED / VERIFIED** |
> | **P10 real-packet delivery to a real destination** | **OPEN** |
> | **Event-route delivery for Sales (05), Marketing (03), Operations (08)** | **UNCHANGED** |
> | **S10 packet assembly** | **BLOCKED by P4, P5, P7 and P8** |
>
> **"P10 closed" on its own is wrong.** Only the internal acknowledgement mechanism is closed.

> ## 📜 HISTORICAL STATUS — NOT LIVE
>
> *The banner below was accurate when this document was written, on 2026-10-02 before
> implementation. It is retained as history and no longer describes the current state: the mechanism
> was subsequently implemented, amended and exercised once. Read §0 for what is true now.*
>
> > 🔴 PROPOSAL · NOT IMPLEMENTED · NO EVENT PUBLISHED · NO RECEIVER INVOKED · NO EXTERNAL WRITE ·
> > NO ROUTE APPROVED
> >
> > Read-only architecture assessment. No runtime code, event catalog, agent, skill, gate,
> > subscriber, fixture or authorization registry was modified. No bus was instantiated, no event
> > published, no receiver invoked and no delivery attempted or tested.

**Raised by:** `SECTOR-PK2` prerequisite **P10** — no Sector destination has been observed actually
receiving a governed handoff.

---

## 0. Completion record — what was implemented, amended and verified

### 0.1 Status, stated with its qualification

| Claim | Status |
|---|---|
| **P10 internal acknowledgement mechanism** | **CLOSED / VERIFIED** |
| **P10 real-packet delivery to a real destination** | **OPEN** |
| **Event-route delivery for Sales (05), Marketing (03), Operations (08)** | **UNCHANGED** |
| **S10 packet assembly** | **BLOCKED by P4, P5, P7 and P8** |

### 0.2 Implemented — the mechanism

The internal **Sector (01) → Offer (02) packet-reference** mechanism was implemented as §4
recommended: a packet reference handed **directly** to an offline receiver, with **no event, no event
bus and no runtime boot**. Three new files under `01_Sector/delivery/` — the receiver, a
one-attempt delivery-authorisation registry, and its focused tests. **No file under
`arika-runtime/src/` was touched**, so `executor.ts` still contains neither `publish(` nor
`event-bus` and the estate event gate's check 4 passes unaltered.

### 0.3 Amended — read root separated from write root

A first attempt was **not** made, because a read-only dry run of the receiver's pure path predicates
showed the approved row could not succeed: the receiver required the packet to sit inside
`sandbox_root`, which bounded both the read and the write, while the approved row named **sibling**
directories. That was an over-restriction in the implementation, not a gap in the authorisation —
the receiver contract required only that the *acknowledgement destination* be inside the authorised
sandbox.

The owner approved an additive amendment: an optional **`packet_root`** separates the authorised
read root from the authorised write root. Absent, behaviour is unchanged. Present, both roots pass
every safe-root check independently, and the two must be the named sibling directories
(`04_fixture_inputs`, `05_outputs`) of one authorised fixture root whose directory **name** is the
authorisation's fixture id — the normalization rule established there, which is what refuses a
cross-fixture read or write even when both paths are independently safe.

### 0.4 Verified — the one delivery

| Fact | Value |
|---|---|
| Authorization id | `SECTOR-DELIVERY-P10-D1` |
| Authorization status | **`spent`** (was `approved`), transitioned by the receiver's success path |
| Delivery id | `SYNCO-02-D1` |
| Packet sha256 | `09bfd65f7c00c1798bf47b3494be7c0f8b5588550ff0cf2550530a9e3ded6ee7` |
| Acknowledgement sha256 | `a41eab8da1691e58aa570cb2c1c166ed9c5668e3c746a0d0f82c1b11900b310f` |
| Receiver invocations | **exactly 1** |
| Durable acknowledgements | **exactly 1** |
| Outcome | `ACKNOWLEDGED` |

**Exactly one receiver invocation occurred and exactly one durable acknowledgement was created.**
**One `TEST_FIXTURE` control reference carrying an EMPTY payload** was delivered to the **offline
fake Offer-side receiver**. The packet and the acknowledgement live in the **private SYNCO-02
sandbox**, outside this repository; no absolute path to it is recorded here.

**Acknowledgement and authorization state agree:** the row and the acknowledgement carry the same
packet hash, the row's `spent_by_delivery_id` is the acknowledged delivery id, and its `spent_at`
equals the acknowledgement's `received_at`. The hash the receiver returned equals the file on disk,
so the write completed rather than merely starting.

**Idempotency and concurrency are covered by the offline tests, not by a second invocation.** No
second invocation was made — including one to demonstrate duplicate refusal. The suite proves a
repeat attempt is refused `ACKNOWLEDGEMENT_EXISTS` leaving the first acknowledgement byte-identical,
and that eight concurrent invocations at one delivery id produce exactly one acknowledgement with
exactly one winner, in both the single-root and separated-root configurations.

### 0.5 What did NOT happen

**No event was published. No event bus was used. No runtime, scheduler or webhook server was
started. No S10 or AEIT_09 packet was assembled. No external destination changed. No production
handoff occurred. No Lead, prospect, opportunity or pipeline entry was created. PG1, PG2 and PG5 did
not move.**

### 0.6 What this proves, and what it does not

**Proves — A, B and C of §4's ladder, with D false.** Transport implemented; a receiver invoked; and
**a durable, idempotent acknowledgement recorded — the first time anything in this estate has been
observably *received*.**

**Does not prove** anything about content: the acknowledged packet carried an **empty payload**, so
this is evidence about the transport mechanism only. No external destination received anything and
none is reachable by that receiver. The event routes are untouched — nothing still publishes, and
`DEMAND_SHIFT` remains `DESIGNED` with zero subscribers, so **Sales (05), Marketing (03) and
Operations (08) are exactly as `SECTOR-PK2` found them.** PK2's **P4, P5, P7 and P8** are untouched.

**The delivery line is stopped here.** Every remaining step needs either a real packet (blocked by
P4/P5) or a real destination (blocked by P7/P8, which no fixture can close).

### 0.7 Standing of the sections below

§1–§3's assessment and call graph remain accurate. §4's recommendation was adopted. §7's minimal
diff was followed, **with one correction**: it proposed writing a durable `DELIVERY_FAILED` record,
and the implementing decision instead required a failure to be reported **only** in the returned
result, so a refusal writes nothing at all. §6's durable-failure gap therefore stays open. §7's
"changes required to the estate event gate: NONE" held — no gate changed. §10's owner decisions D1–D6
were adopted as recommended; **D4, the estate-wide approval-bypass gap, remains open** and this
mechanism closes it only for itself, by enforcing its own approval before any side effect rather
than inheriting the runtime flag.

**Precondition satisfied.** Working tree clean; `DB9-PROV-1`'s nine files are in Git HEAD at
`a191ab2`, whose contents are exactly the nine reported, so attribution is unambiguous. Nothing was
committed by this task.

---

## 1. Does a delivery route exist in fact?

**Two different answers, and conflating them is the trap.**

**For an event route: NO.** Nothing in the runtime ever publishes an agent's returned emits. The
*only* `publish()` call site in all of `arika-runtime/src/` is `webhook-server.ts:20`, and that is
the **inbound** path — external HTTP turned into an internal event. `executor.ts:153` computes
`emitted` and returns it; **no call site anywhere consumes that array.**

**For the in-process transport mechanism: YES, and it is already tested.** `EventBus.publish()`
emits, `index.ts:22` registers subscribers from spec triggers at boot, and `JoinGate` delivers to a
handler with once-only semantics. **`arika-runtime/tests/executor.test.mjs` already instantiates a
bus, publishes, and observes a receiver acknowledgement** (`fired.push(joined)`) — including a test
that a stray late arrival cannot re-fire a completed barrier.

**So what is missing is not the mechanism. It is a governed Sector handoff that uses a mechanism with
a durable acknowledgement.** That reframing is the main finding of this assessment, and it makes the
first step far smaller than P10's wording suggests.

### Against the A–D ladder

| | Claim | State today |
|---|---|---|
| **A** | transport implemented | ✅ **Yes** — `EventBus.publish()` works, and a non-event reference transport works by hand |
| **B** | receiver invoked | ✅ **Yes, in tests** — `JoinGate.onComplete` and `eventBus.on` handlers fire |
| **C** | acknowledgement recorded | ⚠️ **In test memory only.** `fired.push()` is an in-process array. **Nothing durable records that a delivery was received** |
| **D** | external destination changed | ❌ **No** — and for the CRM route only, it has happened before under fixture authorisation (CW2, SF2) |

**C is the real gap.** A, B and D are each already settled; the estate has never produced a durable
receiver acknowledgement for a Sector handoff.

---

## 2. Current-state call graph

```
INBOUND — implemented and working
───────────────────────────────────────────────────────────────────────────────
  external HTTP  POST /webhook/:source
        │
        └─▶ webhook-server.ts:20   await bus.publish({ type, payload, source })
                  │                 ◀── THE ONLY publish() IN THE RUNTIME
                  │
                  └─▶ index.ts:22  eventBus.on(t.on, handler)      [wired at boot]
                        │
                        └─▶ executor.runAgent(spec, { trigger:"event", … })
                              │
                              └─▶ finalizeRun()
                                    ├─▶ requiresHumanApproval(...)  → humanGate
                                    │     ◀── RECORDED, NOT ENFORCED (see §5)
                                    ├─▶ writeMemory()  → _memory/*.jsonl   [DURABLE]
                                    │     └─ assertStreamMatchesMode() fails closed
                                    │        BEFORE any file is touched
                                    └─▶ returns { …, emitted: [ … ] }
                                              │
                                              ╳  NOTHING CONSUMES THIS
                                              ╳  no dispatcher exists
                                              ╳  estate gate check 4 FAILS the build
                                                 if executor.ts ever contains
                                                 "publish(" or "event-bus"

OUTBOUND — does not exist
───────────────────────────────────────────────────────────────────────────────
  finalizeRun().emitted ──╳──▶ (no dispatcher) ──╳──▶ bus.publish ──╳──▶ subscriber

CLI — the only path in use today; never touches the bus
───────────────────────────────────────────────────────────────────────────────
  arika run <name> --input  ─▶ runAgent ─▶ finalizeRun ─▶ writeMemory ─▶ stdout

JOIN BARRIER — in-process, once-only, already tested
───────────────────────────────────────────────────────────────────────────────
  bus.publish(A) ─┐
  bus.publish(B) ─┼─▶ JoinGate.accept() ─▶ buffers per correlation key
  bus.publish(C) ─┘        │
                           └─▶ onComplete(joined)      ◀── RECEIVER INVOKED
                                 byKey.delete(key)     ◀── once-only; a stray
                                                           late arrival cannot
                                                           re-fire the barrier
```

### Code trace — the ten questions, answered precisely

| # | Question | Finding |
|---|---|---|
| 1 | Does `executor.ts` publish? | **No.** Line 153 returns `emitted`; the file contains no `publish(` and no `event-bus` import — which the estate gate enforces |
| 2 | Does any boot path publish returned emits? | **No.** `index.ts` wires subscribers, the JoinGate, the scheduler and the webhook server. It never reads `result.emitted` — it logs only `result.requiresHumanApproval` |
| 3 | Does an event bus exist, and where? | **Yes.** `triggers/event-bus.ts`, a bare `node:events` `EventEmitter`. A **shared singleton** `eventBus` is exported at line 34 and instantiated at module load |
| 4 | Are subscribers registered for Sector-relevant events? | **Yes, at boot only** — `index.ts:22` binds every spec trigger of `type: "event"`. With the runtime unbooted (the only sanctioned mode), **zero are live** |
| 5 | Do subscribers perform external writes? | **Indirectly, by design.** A subscriber runs `runAgent`, which can call the model and append to a memory log. No subscriber writes to a connector itself |
| 6 | Is approval checked before dispatch and before side effects? | **No — and this is the sharpest finding.** `humanGate` is computed *after* the agent answers and is only *reported*. **No code branches on it.** Today that is harmless because no dispatch exists; **the moment dispatch is added without an explicit check, approval is silently bypassed** |
| 7 | Can delivery occur twice? | **Yes, trivially.** The bus is a bare `EventEmitter`: no dedupe, no delivery-once, no cycle detection, no depth limit — the estate gate's own check-6 docstring states this. The **only** idempotency anywhere is `JoinGate`'s per-correlation-key `byKey.delete(key)` |
| 8 | Is failed delivery durably recorded? | **No.** `index.ts:26` catches a handler error and `console.error`s it. **A failed delivery is lost when the process exits.** `writeMemory` records the *run*, never the *delivery* |
| 9 | Does an offline fake receiver exist? | **Yes, as a test pattern** — `executor.test.mjs` builds `new EventBus()`, registers a handler, publishes, and asserts on an in-memory `fired[]`. There is **no reusable receiver module**, and no durable acknowledgement |
| 10 | Are fixture runs terminal under the no-emits safeguard? | **Yes.** `emitted: ctx.fixture ? [] : advertisedEmits(...)` — a fixture advertises no event whatever its spec declares |

**No outbox, queue or handoff store exists.** A repository-wide search for `outbox`, `queue` and
`handoff_store` returns nothing. The nearest thing is the append-only `_memory/*.jsonl` logs written
by `memory-writer.ts`, which record runs rather than deliveries.

---

## 3. Route comparison matrix

| | **Offer (02)** | **Content (04)** | **Marketing (03)** | **Sales (05)** | **Operations (08)** | **ClickUp CRM** | **Internal store** |
|---|---|---|---|---|---|---|---|
| Producer | Sector S10 | Sector S10 | Sector S10 | Sector S10 | Sector S10 | Sector S10 | `memory-writer.ts` |
| Event / packet | **AEIT_09 §1 packet** (no event) | packet by relation | `DEMAND_SHIFT` | event only | `DEMAND_SHIFT` | four governed tags | JSONL run line |
| Transport | **relation + text reference** | native relation (9 available) | event bus | event bus | event bus | connector REST | `appendFileSync` |
| Subscriber / receiver | Offer, by reference | Content, by relation | **none** | a registered subscriber | **none** | `Lead` list | the log file |
| Implementation state | `CONNECTED` ✅ | `CONNECTED` ✅ | **`DESIGNED`**, zero subscribers | `CONNECTED`, **no observed delivery** | **`DESIGNED`**, zero subscribers | `CONNECTED`, round-trip proven | **working** |
| Human-approval gate | **PG2 — char-for-char owner approval** | **PG5** | — | — | — | fixture authorisation | none |
| Idempotency | **none** (manual) | none | n/a | **none** — bare `EventEmitter` | n/a | task id, by hand | append-only, no key |
| Retry | none | none | n/a | **none** | n/a | **never retry** (S10 F3a) | none |
| Delivery acknowledgement | **none** | none | n/a | **none** | n/a | **read-back** (CW2/SF2) | the line itself |
| Failure recording | by hand | by hand | n/a | **stdout only, lost** | n/a | `HANDOFF_FAILURE` | n/a |
| Cleanup / reversal | n/a (internal) | n/a | n/a | n/a | n/a | **delete once, confirm absence** | append-only, no reversal |
| Internal or external | **internal** | internal | internal | internal | internal | **EXTERNAL** | internal |
| Fixture-safe? | **✅ yes** | ⚠️ PG5 holds it | n/a | ⚠️ needs the bus to publish | n/a | ⚠️ only under authorisation | ✅ yes |
| Real pilot required? | **No, for the mechanism** | no | no | no | no | no | no |
| Current blocker | **no acknowledgement mechanism exists** | PG5 | **no route at all** (31d) | **nothing publishes** | **no route at all** (31d) | no authorisation; D would be true | records runs, not deliveries |

---

## 4. Recommended first route

### **Sector (01) → Offer (02), packet-by-reference, in-process, to an offline receiver that writes a durable acknowledgement.**

**The decisive property: the Sector→Offer route is not an event route at all.** S10's own table calls
it *"relation + text reference"*. So the first delivery test needs **no `publish()`, no event bus, no
runtime boot, no scheduler, and no change to `executor.ts`** — which means it **cannot trip estate
gate check 4** and does not touch the runtime publication prohibition in any way.

**Why this one, against the stated priorities:**

| Priority | How this route satisfies it |
|---|---|
| No external side effect | **D stays false by construction.** Nothing outside the repository and the fixture sandbox is touched; Offer's registry and `runtime.jsonl` are not written |
| No runtime boot or scheduler | Neither is involved. The receiver is a plain offline module run through `run_offline.py` |
| Explicit human approval | A one-attempt authorisation row, checked **before** the receiver is invoked — closing finding #6 for this route by construction |
| Deterministic single delivery | One attempt, synchronous, in-process. No bus, so no fan-out and no re-entry |
| Idempotency | A content-addressed key; a repeat is **refused, not re-delivered** |
| Durable acknowledgement | One append-only line in the fixture sandbox — **this is the C the estate has never had** |
| Fail-closed | Refuses on a missing authorisation, a key collision, a shape failure or an ambiguous result. Never retries |
| Fixture isolation | `TEST_FIXTURE` classified; sandbox-only destination; no production connector reachable |
| Useful to the real pilot | **This is the route the readiness packet's R3 designates** (*"Offer — delivered by text reference"*). Proving acknowledgement here is reusable at PG2 |

**What the first test would prove, exactly:** **A, B and C true; D false.** Transport implemented; a
receiver invoked and observed; an acknowledgement recorded durably and idempotently — with no
external destination changed, no event published, and the runtime's publication prohibition intact.

**What it would NOT prove, and must not be read as proving:** that the *event* routes deliver; that
Sales, Marketing or Operations are reachable; that a real `Lead`, Offer registry entry or Notion row
received anything; or that PG1, PG2 or PG5 moved. **It establishes the acknowledgement mechanism, and
nothing else.**

---

## 5. Rejected alternatives

| Alternative | Why it loses |
|---|---|
| **Sales (05) via the event bus** | It is the route PK2 named, which is precisely why it should not be first. It requires something to **publish** — the one behaviour the estate gate guards and AEIT_11 R2 says invalidates every `CONNECTED` state. It would also inherit a bare `EventEmitter` with **no dedupe, no cycle detection and no depth limit**, so delivery-once would have to be built before the first test rather than after |
| **Marketing (03) / Operations (08)** | **No route exists at all.** Their only one was `DEMAND_SHIFT`, retired to `DESIGNED` under owner decision 31d. Building a route *and* proving acknowledgement in one step confounds two findings |
| **ClickUp CRM** | The only route with a **proven** round-trip (CW2, SF2) — and the only one where **D becomes true**. An external write is the wrong place to establish a mechanism that does not yet exist internally |
| **Content (04)** | A genuine second choice: internal, `CONNECTED`, relation-based. Rejected only because **PG5 holds it** and Offer is the route R3 designates first. If Offer is declined, this is the fallback |
| **Making `executor.ts` publish `emitted`** | Fails estate gate check 4 by design, converts every `CONNECTED` edge into a LIVE candidate requiring re-derivation (AEIT_11 R2), and would dispatch **without an approval check** (finding #6). The largest possible first step |
| **A general outbox / queue abstraction** | Correct eventually, wrong now. It is new infrastructure justified by one unproven delivery; build it after one acknowledgement exists, not before |

---

## 6. Security and failure analysis

**The approval bypass (finding #6) is the most serious latent risk in the estate.** `humanGate` is
computed and reported but **no code branches on it**. That is currently harmless only because
nothing dispatches. Any dispatcher added without an explicit pre-side-effect check would make every
Class 3+ agent capable of acting unreviewed. **The recommended route closes this for itself by
checking authorisation before invoking the receiver — and the gap remains open for every future
route, which is owner decision D4.**

| Risk | Severity | Mitigation in this design |
|---|---|---|
| Double delivery | high (bare `EventEmitter`) | No bus used. Content-addressed idempotency key; a repeat is refused |
| Approval bypass | **high, estate-wide** | Authorisation checked **before** the receiver runs. Does not fix the general gap — see D4 |
| Silent delivery failure | high | Failure is written to the durable acknowledgement store as `DELIVERY_FAILED` with a reason, never only to stdout |
| Re-entry / loop | high if the bus is used | No bus, no fan-out, no re-entry possible |
| Fixture leaking to production | **critical** | Sandbox-only destination; `TEST_FIXTURE` classification; no connector imported; the offline guard active on every command |
| A fixture mistaken for a real handoff | high | The acknowledgement carries `classification: TEST_FIXTURE` and an explicit `is_not` list; it may never be recorded as `delivered` |
| Unresolved floors passed off as complete | medium | The receiver **accepts and records** an unresolved floor but marks the acknowledgement `acknowledged_with_unresolved_floor`, never a complete hand-off |
| Timeout / hang | low | Synchronous and in-process; **no network, no timer, no timeout semantics exist** — stated rather than invented |

---

## 7. Minimal implementation diff

**New files only. Nothing existing is modified.**

| File | Purpose |
|---|---|
| `01_Sector/delivery/offer_inbox_receiver.py` *(new)* | The offline receiver. Reads one packet, validates it against AEIT_09 §1, checks the authorisation, enforces the idempotency key, writes one acknowledgement. Imports no connector and no runtime module |
| `01_Sector/delivery/delivery-authorisations.json` *(new)* | One-attempt authorisation rows, mirroring `skill-fixture-authorisations.json`'s `approved`/`spent` discipline |
| `01_Sector/delivery/test_offer_inbox_receiver.py` *(new)* | Focused offline tests (§8) |
| `01_Sector/SECTOR_DELIVERY_P10_PROPOSAL.md` | this document |

**Explicitly NOT changed:**

- `arika-runtime/src/**` — **no file.** No `publish(`, no `event-bus` import, no dispatcher. `npm test` and the build are untouched
- `executor.ts` — untouched, so **estate gate check 4 needs no change and keeps passing**
- `event-catalog.json`, `estate-event-register.json` — untouched; **no new edge is declared**, because no event is involved
- Any agent spec, any `emits`, any skill, `skill-fixture-authorisations.json`, the four gates, the fixture logs

**Changes required to the estate event gate: NONE.** That is the point of choosing a non-event route.
*(If a later route uses the bus, check 4 must be deliberately re-baselined and every `CONNECTED` edge
re-derived per AEIT_11 R2 — a separate decision, not this one.)*

**Production behaviour explicitly unchanged until separately enabled.** The receiver is not wired into
`index.ts`, has no trigger, is not an agent, has no spec, and is invoked only by an explicit
owner-authorised command. **Booting the runtime behaves exactly as it does today.**

### Design specification

| Element | Specification |
|---|---|
| Exact packet | one S10 AEIT_09 §1 packet. **Not an event** — no event type is published or declared |
| Producer | Sector (01) S10, manual apply per RD4 |
| Receiver | `offer_inbox_receiver.py`, an **offline Offer-side receiver**. It is a fake receiver and says so; Offer's real registry and `runtime.jsonl` are not touched |
| Trigger | explicit owner-authorised single command. No schedule, no event, no webhook, no boot |
| Approval check | the authorisation row must read `approved` **before** the receiver is invoked. Refuse on `draft`, `spent` or absent |
| Fixture classification | `TEST_FIXTURE`, stamped on the acknowledgement and on every refusal record |
| One-attempt authorisation | the row is marked `spent` on the single attempt, whatever the outcome. **No second attempt under the same row** |
| Idempotency key | `sha256(packet_bytes + authorisation_id)`. A key already present in the store is **refused as `DUPLICATE_REFUSED`**, never re-delivered |
| Durable acknowledgement | one append-only JSONL line in the SYNCO-02 sandbox. **Not** the repository skill-run log, so no schema or gate changes — see D3 |
| Retry policy | **none.** One attempt. An ambiguous result is recorded as ambiguous and stops |
| Failure outcome | `DELIVERY_FAILED` with a category, durably written. Never stdout-only |
| Timeout behaviour | **not applicable** — synchronous, in-process, no network. Stated explicitly so no reader assumes a timeout exists |
| Cleanup | nothing external to clean. The acknowledgement store is history and is retained; a cleanup record goes to `07_cleanup` if any artifact is ever created |
| Logging | the acknowledgement store is the log. No stdout-only path for any outcome |

---

## 8. Focused test plan — all offline, no bus, no network

| # | Test | Asserts |
|---|---|---|
| T1 | a missing authorisation refuses before the receiver runs | fail-closed on approval |
| T2 | `draft` and `spent` rows both refuse | one-attempt discipline |
| T3 | a valid authorisation invokes the receiver exactly once | **B** |
| T4 | the acknowledgement line is written and re-readable | **C**, durable |
| T5 | a second delivery with the same key is `DUPLICATE_REFUSED` | idempotency |
| T6 | a packet missing an AEIT_09 §1 field is refused, with the field named | shape validation |
| T7 | a packet with an `UNRESOLVED` floor is accepted but marked `acknowledged_with_unresolved_floor` | never a complete hand-off |
| T8 | a receiver exception is written as `DELIVERY_FAILED`, not stdout-only | durable failure |
| T9 | no outcome path writes outside the sandbox | **D stays false** |
| T10 | the receiver imports no connector and no `arika-runtime` module | isolation, by source inspection |
| T11 | the acknowledgement is never recorded as `delivered` | fixture labelling |
| T12 | `executor.ts` still contains no `publish(` and no `event-bus` | the estate-gate invariant holds |
| T13 | `event-catalog.json` and `estate-event-register.json` are byte-identical | no new edge declared |
| T14 | Sector 56, DB9 33, guard 31+15, runtime 68 and all four gates still pass | no regression |

---

## 9. Rollout and rollback

**Rollout** — one step, then stop: approve §11 → add the three new files → run the §8 tests → **stop
before any delivery attempt**. The delivery attempt itself is a *separate* authorisation, because
`SECTOR-DELIVERY-P10` is the mechanism and the attempt is the test.

**Rollback** — clean, because nothing existing is touched: delete the three new files. No runtime
code, contract, gate, catalog or log reverts, and **no production behaviour was ever altered**. An
acknowledgement already written is retained as dated history, never rewritten.

---

## 10. Owner decisions required

| # | Decision | Recommendation |
|---|---|---|
| **D1** | Offer (02) as the first route, or Content (04)? | **Offer** — the route R3 designates; Content is the fallback if PG5 is preferred as the gate |
| **D2** | Is a *fake* Offer-side receiver acceptable for the first test? | **Yes.** A real Offer receiver means writing Offer's store, which makes D true and needs PG2 |
| **D3** | Acknowledgement store: the fixture sandbox, or the repository skill-run log? | **The sandbox.** The log would need a new outcome token and a gate change — note `delivered_fixture_verified` **cannot** be reused: `skill_run_gate` check 7 requires it to carry `external_writes`, and an internal delivery has none |
| **D4** | Fix the **estate-wide** approval-bypass gap (finding #6) now or later? | **Separately and soon.** This route closes it for itself; the gap stays open for every future dispatcher. It is the single most consequential latent risk found |
| **D5** | Build a general outbox abstraction? | **Not yet.** After one acknowledgement exists |
| **D6** | Does the event-bus route stay deferred? | **Yes.** It needs delivery-once, cycle protection and a deliberate check-4 re-baseline with every `CONNECTED` edge re-derived (AEIT_11 R2) |

---

## 11. Exact implementation approval wording

> **OWNER APPROVAL — `SECTOR-DELIVERY-P10` MECHANISM (implementation only, no delivery)**
>
> I approve implementing the smallest Sector delivery mechanism exactly as proposed in
> `01_Sector/SECTOR_DELIVERY_P10_PROPOSAL.md`, with decisions D1–D6 as recommended there: route
> **Sector (01) → Offer (02) packet-by-reference**, an **offline fake Offer-side receiver**, and the
> acknowledgement store in the **SYNCO-02 fixture sandbox**.
>
> Add only the three new files in §7 — `01_Sector/delivery/offer_inbox_receiver.py`,
> `01_Sector/delivery/delivery-authorisations.json` and
> `01_Sector/delivery/test_offer_inbox_receiver.py` — and run the §8 test plan through
> `00_Agency_Governance/offline_guard/run_offline.py`.
>
> **Modify nothing else.** No file under `arika-runtime/src/`, and specifically **no change to
> `executor.ts`**, so estate gate check 4 keeps passing unaltered. No event catalog, estate event
> register, agent spec, `emits` declaration, skill, gate, subscriber, fixture log or authorization
> registry. **Production behaviour stays byte-for-byte unchanged:** the receiver is not wired into
> `index.ts`, has no trigger and no spec, and booting the runtime behaves exactly as it does today.
>
> **This authorizes the MECHANISM ONLY. It does not authorize a delivery attempt** — no packet may be
> dispatched, no receiver invoked with real input and no acknowledgement written until a separate
> one-attempt authorization is approved. It does not authorize publishing any event, instantiating or
> using the event bus, booting the runtime, starting the scheduler or webhook server, running S10,
> adding a fixture authorization, assembling a packet, or any CRM, Notion, registry, connector or
> pricing write.
>
> **Nothing is weakened:** fixture emits suppression, the runtime publication prohibition, PG1, PG2,
> PG5, RD6's downstream restrictions, S10's fixture authorization and the D20 evidence boundaries all
> stand exactly as written. A fixture may never be dispatched to a production connector or a real
> destination. **PK2's blockers P4, P5, P7 and P8 are untouched and packet assembly remains blocked.**

---

## 12. Limitations

1. **Nothing was implemented, published, invoked or delivered.** No bus was instantiated.
2. The A–D assessment is **code-trace evidence**, not runtime observation: the runtime was not booted,
   so the claim that zero subscribers are live is a statement about the unbooted mode this repository
   operates in.
3. **This closes no PK2 blocker.** P10 stays open until a delivery attempt is separately authorised
   and succeeds. P4, P5, P7 and P8 are untouched.
4. The recommended route proves an **internal** acknowledgement. It says nothing about whether any
   external destination would receive anything.
5. **A fake receiver proves the mechanism, not the integration.** Offer's real store is not written,
   and a later real-receiver step needs PG2 and its own decision.
6. Mechanism evidence only — nothing here is evidence about a market, demand, pricing, buyers,
   capacity, performance or any real property.
