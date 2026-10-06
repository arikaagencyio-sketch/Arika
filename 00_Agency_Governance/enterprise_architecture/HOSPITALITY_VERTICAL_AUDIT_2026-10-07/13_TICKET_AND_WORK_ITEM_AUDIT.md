# 13 — Ticket and Work-Item Audit (and the "Ready" Audit)

**Protocol §4:** how do tickets, notes, tasks and work items work — and does the system distinguish **information, decision, task, deliverable, approval, outcome and learning**? **§5:** what exactly does "ready" mean?

---

## 1. What constitutes a "ticket" here

**There is no ticket, task or work-item entity** — not in `CRM_SCHEMA.md`, not in `AEIT_06`, not in any Notion schema (`CONFIRMED` by reading all three). Work is held as **numbered rows in markdown registers**, plus three machine-readable authorisation registers, plus (for future client delivery) the ClickUp `Engagement / Project` list.

### 1.1 The registers that function as ticket systems

| Register | Holds | ID scheme | Status vocabulary | Fresh? |
|---|---|---|---|---|
| `00_Agency_Governance/OWNER_INPUT_NEEDED.md` | Owner decisions and facts needed | `0`–`75`, plus `31a`–`31m`, `32a`–`32g` | free text + emoji (`✅ DECIDED`, `🟡 PARTIALLY DECIDED`, `🔴`) + a Resolved table | **No** — header 2026-09-21; rows 60/72/74 stale (`HV-07`) |
| `OWNER_DECISION_WORKSHEET.md` | Former action surface | item numbers | `[DECISION]` / `[WAITING ON DATA]` | **Frozen 2026-06-30** (marked) |
| `GO_LIVE_CHECKLIST.md` | Setup work, 11 phases | `1`–`58` | `Done (date)` · `Fully done` · `Not started` · prose | Phase 11 added 2026-10-06 |
| Department §8 Decision Logs (×20) | Decisions with reasoning | dated bullets; named decisions `SECTOR-SF1`, `SECTOR-CRM1`, `OFFER-F2`, `DB9-PROV-1`, … | `ENACTED and SPENT`, `APPROVED · IMPLEMENTED and VERIFIED`, … | per department |
| A001 records (6 files) | Sandbox decisions, gaps, queue | `D1`–`D21` · `AG-1`–`AG-19` · `T1-1`–`T1-5` · `F1`–`F4`, `V1`–`V4`, `W1`–`W5`, `O1`–`O3`, `R1`–`R6` · `SR-1`–`SR-3` | `Now / Later / Never` · `safe now / needs owner decision / later only / blocked by D16 / never from A001` | closed 2026-09-16 |
| Full Push Readiness Packet | Owner inputs, pre-run decisions, gates, run steps | `OI1`–`OI9` · `RD1`–`RD7`, `RD1a` · `PG0`–`PG5` · `R1`–`R7` | ❌ / ◐ / ✅ / ⛔ | partly stale (2026-10-03 note) |
| Draft 41 | Open decisions, gates, deliverables | `#1`–`#19` · `QG1`–`QG8` · `G1`–`G6` · `D1`–`D7` | `OPEN` · `BLOCKED` · `✅ Decided` | 2026-09-14 |
| Delivery worksheet | MVP decisions, readiness gate | `#1`–`#27` · `G1`–`G7` · `M1`–`M7` · `MD1`–`MD8` · `P1`–`P4` | owner-decision blocks | 2026-09-14 |
| Intake profile + overlay | Questions and decisions | `U-A01`… · `H-A01`… · `ID1`–`ID6` · `LQ1`–`LQ3` · `G-1`… | answer states (`ANSWERED`, `UNKNOWN`, `NOT_ASKED`, `BLOCKED`, …) | `v0.1-draft` |
| AEIT package | Gaps, decisions, gates, risks | `A1`–`D3` · `R1`–`R5` · `SM1`–`SM4` · `G0`–`G5` · `RK-1`–`RK-8` · `HP-1`–`HP-4` | ratified / queued | 2026-07-22 → 2026-09-14 |
| Sector DB proposals | Open data decisions | `OD1`–`OD13` | open / closed / closed-with-exception | 2026-10-02 |
| **Authorisation registers** (`crm_provisioning/…`, `01_Sector/delivery/…`, `01_Sector/contracts/skill-fixture-…`) | One-shot permissions for state-changing runs | `CRM-PROV-1`, `SECTOR-SF1`–`SF3`, `SECTOR-DELIVERY-P10` | **`draft → approved → spent`**, never deleted | machine-checked |
| ClickUp `Engagement / Project` list | Future client delivery | ClickUp IDs | `scoped → in-delivery → review → complete` | `LIVE` list, **empty** |

### 1.2 Identifier collisions — `CONFIRMED`

Fifteen-plus namespaces would be manageable if they were disjoint. They are not:

| Identifier | Means (at least) |
|---|---|
| **`R1`** | `AEIT_05` reconciliation decision (Sector owns ICP fit) · A001 runtime blocker · Full Push run step |
| **`G1`** | `AEIT_10` reality gate (legal existence) · worksheet readiness gate · Draft 41 gate rule ("audit first") |
| **`D1`** | A001 decision (sandbox root) · Draft 41 deliverable (the audit) · `AEIT_04` finding (Zoho off the DPA register) |
| **`P1`** | plugin slot (ontology) · Sector priority band ("Pursue now") · worksheet package (Gateway) · and this audit's own priority scale |
| **`S1`** | intake stage (public desk profile) · A001 queue item |

A sentence such as *"G1 is partial"* is ambiguous without its file. → `HV-10`.

## 2. The protocol's questions about tickets

| Question | Answer | Evidence |
|---|---|---|
| What constitutes a ticket? | A numbered row in one of ≥10 registers; for system actions, an authorisation entry | §1.1 |
| Who creates it? | Almost always a Claude Code (or Codex) session, on the owner's instruction; the owner decides | changelog signatures |
| What does it contain? | Varies by register — typically *what is needed · why it cannot be inferred · what it blocks*; authorisations add *target, permits, forbids, risk class, spent* | tracker headers; JSON `_meta` |
| Status states | Free text per register; machine-checked only in authorisation registers and ClickUp statuses | §1.1 |
| Priority states | A "🔴 Highest priority" tracker section (currently empty); emoji; no priority field anywhere else | `OWNER_INPUT_NEEDED.md` |
| Ownership | Department names; "Owner action" vs "Buildable" in the go-live checklist; every row resolves to one person | Constitution §4 |
| Dependencies | Free-text "Blocks" column | tracker |
| Approvals | Quoted owner approvals inside decision entries; authorisation registers (system actions); nothing for client work | §3 |
| Evidence attached | **Strong** — paths, dates, run IDs, hashes, live-check notes | throughout |
| Completion | Per register: Resolved table with date + pointer; authorisation `spent`; Project `complete` | — |
| "Ready" / "blocked" / "in progress" / "needs review" | Defined locally and inconsistently (§5) | — |
| Strategic decisions recorded? | **Yes, rigorously** — with reasoning, overrides and "was:" history | department §8 logs |
| Decisions → operational work? | **By hand.** No enactment tracking: ratified `AEIT_05` R1 and R3 (2026-07-22) are still unapplied (`CRM_SCHEMA.md:45` still says Sales sets `ICP_fit_score`; `sector-signal-scorer.md:41` still emits `Critical`) | `HV-21` |
| Completed work → institutional knowledge? | **Yes, as prose** — changelog lessons, memory files, standards distilled from incidents (`AEIT_11` came from seven verified defects) | — |
| Historical decisions recoverable? | **Yes** — append-only logs, superseded text kept as "Was:", git history; but scattered across registers | — |
| Linked to clients · campaigns · revenue · calendar · sector · audience · channels? | Clients: only via ClickUp Project (empty). Sector: Sector-owned items, yes. **Campaigns, revenue, calendar events, audiences, channels: no** | `CRM_SCHEMA.md`; Content DB 4 |

## 3. The seven kinds of record (protocol §4) — kept distinct?

| Kind | Where it lives | Distinct from the others? | Quality | Gap |
|---|---|---|---|---|
| **Information** | Sector DBs with provenance (DB 3 findings, DB 7 signals, DB 14 sources, DB 16 profiles); intake answers (client folder) | ✅ — a finding is never a decision | **High** (tiered sources, honesty states, verification dates) | DB 9/DB 10 row-level provenance empty |
| **Decision** | Department §8 logs; tracker; A001 D-series; packet RD-series; `AEIT_05` | ✅ — and *decide ≠ apply* is explicit doctrine | **High** content, fragmented location | Enactment tracking (`HV-21`); namespace collisions (`HV-10`) |
| **Task** | Go-live items; A001 queue; agent `recommendedActions`; ClickUp tasks | ◐ — tasks and decisions share registers (the tracker mixes "decide X" with "supply Y" and "do Z") | Medium | No owner/priority/due/dependency standard |
| **Deliverable** | Draft 41 D1–D7, MVP M1–M7; ClickUp `Project.scope_summary` | ✅ in design | Designed only | No per-engagement deliverable register |
| **Approval** | Authorisation registers (system actions); `finos.approvals` (money); runtime `awaiting_review`; content-gate layers; quoted approvals in decision entries | ◐ — four mechanisms, none for client work | High for system actions | **No client/creative approval record** (`HV-09`) |
| **Outcome** | `_memory/*.jsonl` execution records; spent authorisations; prospecting queue (`sent: 0`) | ✅ — outcomes are never claimed without a record | High honesty, little volume | No client outcome store (`HV-18`) |
| **Learning** | Changelog lessons; memory files; standards from incidents; `Learning_Loop_Log.md` (empty) | ◐ — learning is embedded in changelog prose | Rich but not queryable | No learning register (`HV-33`) |

**Verdict (`CONFIRMED`):** the OS distinguishes the seven kinds **conceptually and in practice for its own construction**, better than most systems. It has **no operational layer** for them once a client exists: no task entity, no deliverable register, no client approval record, no outcome store, no learning register.

## 4. Minimum sufficient fix (proposal — not applied)

Do **not** introduce a ticketing product or a new registry. In order:

1. **Client delivery work → ClickUp `Engagement / Project` tasks**, which already exist with a status pipeline. Add four custom fields through the governed provisioner (`crm_provisioning/`): `approved_by`, `approved_at`, `version`, `evidence_ref`. That covers *task*, *deliverable* and *approval* for client work in one place the client process already uses. (`HD-06`)
2. **One row schema for every markdown register:** `id · kind (information/decision/task/approval/outcome/learning) · owner · status (from one vocabulary) · blocks · evidence · opened · closed`. Adopt it as registers are next touched — no mass migration.
3. **Prefix every identifier with its register** in prose (`A001-D1`, `D41-G1`, `AEIT10-G1`, `WS-G1`) so collisions disappear without renumbering anything.
4. **An enactment column** on ratified decisions (`decided → queued → applied (commit)`), starting with `AEIT_05` R1–R5.
5. **Re-sync the tracker** (`HV-07`) and give it an automated freshness check in the style of `estate_event_gate.py`'s age warning.

## 5. The "Ready" audit (protocol §5)

"Ready" is used with **at least seven different meanings**, each locally precise and none defined agency-wide:

| Term in use | Meaning | Where | Defined? |
|---|---|---|---|
| `Ready for Design` | A brief may trigger production (and credit spend) | Content DB 7 `Publishing Status`; the cloud routine matches it **byte-exactly** | ✅ precise |
| `✅ ready to consider` | A brief's relations and hand-off fields are complete | DB 7 `Brief Integrity` formula | ✅ |
| `ready_for_design: false` | Agent's recommendation; never flips the field itself | `content-brief-builder` | ✅ |
| `Offer-Ready`, `Content-Ready`, `Acquisition-Ready`, `Campaign-Ready` | **Sector lifecycle states** reached by passing activation gates F, G, H | `SECTOR_ACTIVATION_PROTOCOL.md` §3 | ✅ — but *about a sector*, not a campaign |
| `outreach-ready` | A pilot engagement state | `CRM_SCHEMA.md` `pilot_state` | ◐ — no exit test stated |
| "readiness" (mechanism / simulation / real-pilot / client-facing) | Four measured dimensions with caps | `READINESS_ASSESSMENT_2026-10-02.md` | ✅ |
| "Not ready to execute" / "satisfied for public-only preparation" | Full Push gates PG0–PG5 | readiness packet | ✅ |
| "Quotable" / "Not Quotable" | Whether an offer may be priced to a client | Offer (02) | ✅ |
| Intake stages S1–S5 | What may be asked of a client, and when | `CLIENT_INTAKE_PROFILE.md` §2 | ✅ |

**The protocol's twelve readiness types, mapped:**

| Protocol type | Nearest existing state | Defined? |
|---|---|---|
| Concept ready | Content DB 5 `Decision = Promoted to Brief` | ◐ |
| Strategy ready | `NARRATIVE_APPROVED` event; Draft 41 stage 4 exit (signed target + strategy) | ◐ |
| Brief ready | `CONTENT_BRIEF_READY` + `Brief Integrity = ✅ ready to consider` | ✅ |
| Creative ready | `Ready for Design` (despite the name, means *ready to produce*) | ✅ |
| Production ready | `STORYBOARD_READY` → reuse gate → production plan | ◐ |
| Approval ready | Presence `Packet State = produced → approved` (reserved field, unused) | ◐ |
| Publishing ready | `content-publishing-gate` verdict `publish` + Class 3 sign-off | ◐ — plane-blind (`HV-14`) |
| Sales ready | `pilot_state = outreach-ready`; qualification verdict | ◐ |
| **Campaign ready** | Sector `Campaign-Ready` is a *sector* state; Content DB 4 Campaign has **no status field** | ❌ |
| Client ready | Intake S-stages; `Client.onboarding_status` | ◐ |
| **Measurement ready** | Draft 41: *"Measurement window agreed with a seasonally comparable baseline before build starts"* (offer-specific) | ❌ agency-wide |
| Commercially ready | `Quotable`; sector `Offer-Ready`; readiness *client-facing* dimension | ◐ — three different meanings |

**Governance risk (`CONFIRMED`): MEDIUM.** Each local "ready" is gated, which limits the damage — but `Campaign-Ready` (a Sector lifecycle state) and *campaign ready* (a campaign's state) will be confused the first time a real campaign exists; *creative ready* is spelled `Ready for Design`; and *commercially ready* has three referents. → `HV-08`.

**Proposed (`HD-07`, not applied):** one Definition-of-Ready table in the `AEIT_06` glossary — each state, its owner, its exit test, and the field that records it — plus a `Status` select on Content DB 4 (`planned → briefed → in production → approved → live → closed`). No other new field.
