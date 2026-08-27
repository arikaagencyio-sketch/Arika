# Sector — Write Contract

**Department:** Sector (01) · **Version:** v0.1 (2026-08-24) · **Status:** Gate 1 — contract only. No skill authored, nothing written to Notion.
**Machine-readable companions:** [`contracts/intelligence-object.schema.json`](contracts/intelligence-object.schema.json) · [`contracts/sector-databases.json`](contracts/sector-databases.json) · [`contracts/skill-execution-record.schema.json`](contracts/skill-execution-record.schema.json)

> **Every Sector skill opens by reading this file.** It is the single contract S01–S12 implement. It is **assembled, not invented** — roughly 70% of what follows already existed, scattered across five files. Each rule below cites its origin. Where this file and its origin disagree, **the origin wins** and the divergence is a defect here.

**Precedence** (`SECTOR_ACTIVATION_CONTRACT.md` §2, unchanged): `AGENCY_OPERATING_CONSTITUTION.md` → `GLOBAL_OS.md` → `SECTOR_ACTIVATION_CONTRACT.md` → `AEIT_06` + `CRM_SCHEMA.md` → `SECTOR_OS.md` → `SECTOR_NOTION_SCHEMA.md` → **this file** → the current task. This contract is subordinate to all of them and authoritative for *how a Sector write is performed*.

---

## 0. Two things stated plainly, because they are currently only implied

### 0.1 The apply step is a human-invoked Claude Code session

Not a daemon. Not a cron. Not an agent.

`arika-runtime` has **no Notion client of any kind** — `grep -rniE "notion|fetch\(|axios|https?://" arika-runtime/src/` returns two comment lines. It cannot write to Notion, and it cannot invoke a skill: `.claude/skills/` is invisible to `loadAgents()`. The only path to a Notion write is the MCP connector inside an interactive session, driven by a person.

This is not a limitation to route around. It is what makes the layer legal without new governance: `04_Content/CONTENT_INTELLIGENCE_SCHEMA.md:562` establishes that **manual-apply requires no `AUTOMATION_APPROVAL_MATRIX.md` row** — *"the same doctrine Sector operates under."* A human-invoked skill is manual-apply by construction.

**That exemption ends the instant anything auto-writes.** At that moment a matrix row is required *first*, with rollback, fallback and — the question the 11-day outage turned on — **detection**.

### 0.2 This contract is not enforced by a validator

A skill has no `risk_class`, no `emits`, no `department`, and no runtime binding. `arika-runtime/src/spec-schema.ts` validates **agent** frontmatter only. No zod schema, no CI, no linter reads this file or the JSON schemas beside it.

**Conformance is the skill following the contract.** Said plainly so no reader mistakes a schema for a gate. The JSON files are a shared vocabulary and a future runtime's on-ramp — not a check that runs.

---

## 1. The Intelligence-Object Contract — the eight questions

**Origin:** `SECTOR_ACTIVATION_CONTRACT.md` §13.3, where these exist as **one prose sentence**, never enumerated and never encoded. Machine-readable form: [`contracts/intelligence-object.schema.json`](contracts/intelligence-object.schema.json).

Every Sector intelligence record MUST answer all eight. A record missing any one is not a finding; it is a note.

| # | Question | Means | Notion field (DB3 / DB7) |
|---|---|---|---|
| 1 | **what** | the claim itself — one finding, not a paragraph | `Finding` / `Signal` |
| 2 | **source** | the publishing body + tier. The tier test is about the **publisher**, not the page. | `Evidence` + `Source` / `Authoritative Source` + `Source URL` + `Source Tier` |
| 3 | **when-observed** | when it was true, and when last checked | `Freshness` / `Last Verified` + `Next Verification` |
| 4 | **reliability** | how much weight it carries | `Confidence` |
| 5 | **which sector** | resolved through the Sub-Sector hub, never asserted from free text | `Sub-Sector` (+ `Geography` when place-bound) |
| 6 | **which decision it supports** | the decision-purpose gate | `Strategic Implication` |
| 7 | **which system consumes it** | must be non-empty; values come from the canonical department vocabulary (§1.1) | `Routed To` / `Departments Affected` |
| 8 | **what action can result** | an observation with no available action is not intelligence | `Recommended Action` |

This **is** `AEIT_06`'s `Knowledge Object` (`claim, entity_ref, confidence, trust, freshness, source_id, state`) expressed through fields that already exist. It does not add a store, a field or an entity.

### 1.1 The canonical department vocabulary (Q7)

**Decided 2026-08-24.** Machine-readable: [`contracts/department-vocabulary.json`](contracts/department-vocabulary.json).

Q7 answers *which department consumes this*, so it needs one vocabulary. It previously had two, and they were disjoint: `Routed To` offered 5 values, `Departments Affected` offered 7, and neither could name Design (19), Experience Engineering (20), Audits (14), Client Success (07), Legal (10), Tech Stack (13), Finance (09), Consulting (15), AI Enablement (17) or Presence (21). A packet routed on one field could not be received by a workflow reading the other.

**The vocabulary is not a Sector-curated subset — it is `GLOBAL_OS.md` §4, the canonical department registry**, per `AEIT_06`: *"departments consume canonical entities; they do not reinvent them."* Curating a subset is exactly how the original two drifted apart, so the fix is to stop curating.

21 values, names **verbatim** from §4 — no numeric prefix, because §4's names are the plain forms:

`Agency Governance · Sector · Offer · Marketing · Content · Sales · ClientPartner Acquisition · Client Success · Operations · Finance · Legal · HR / People Ops · Branding · Tech Stack · Audits & Diagnostics · Consulting & Advisory · Automation · AI Enablement · Design · Experience Engineering · Presence`

**18 Cross-Domain Synthesis is excluded** — `GLOBAL_OS.md` §4 records it as not an active department (reference archive, no OS file, no owner), so it cannot receive or act on a handoff.

**Two values have no evidenced route today** — `HR / People Ops` and `Presence`. They are included anyway: an unused option costs nothing, a missing one costs a route, and the missing-route failure is precisely what created F2. The other 19 each have a named route recorded in the JSON.

**Applied to Notion 2026-08-24.** DB 3 `Routed To` now holds exactly these 21. DB 7 `Departments Affected` holds these 21 **plus two deprecated legacy options** — `Revenue (Ops)` (canonical: **Operations**, owner-confirmed) and `ClientPartner` (canonical: **ClientPartner Acquisition**). **Never write a deprecated value on a new row;** retire them by re-tagging the affected rows, then dropping the option.

> ⚠️ **A Notion select option cannot be renamed.** `ALTER COLUMN … SET MULTI_SELECT(...)` matches options **by name** — change the name and the old option is dropped, a new one created, and **every row holding it loses that value**. This was established empirically before the migration ran, with a throwaway probe option whose ID changed on rename while the untouched options kept theirs. The originally-planned `Sales` → `05 Sales` style migration would have silently stripped the department values from all 249 rows. **Adding an option is safe; removing an unused one is safe; renaming is a data migration, not a schema change.** Always verify by comparing option IDs before and after — never by assuming.

### 1.2 Three databases cannot carry it in-schema

| DB | Provenance present | Missing |
|---|---|---|
| DB6 Sector Linguistics | `Confidence` | Source, Evidence, Last Verified, Next Review |
| DB9 Audience Roles | **none** | all of Q2, Q3, Q4 |
| DB10 Decision-Maker Registry | **none** | all of Q2, Q3, Q4 |

**Rule until a schema change is ratified:** the skill records Q2 and Q3 **in the page body**, as a dated provenance line — `Source · Tier · Verified YYYY-MM-DD`. It does **not** silently write a row that cannot answer the eight questions and it does **not** pretend the fields exist. Adding them is Gate 2+ work (finding F14).

*(§1.1's vocabulary is now decided **and applied** in Notion. This one is not: it remains **decided in contract, pending in Notion**. A skill writes what the live schema can hold and records the rest in the page body — never a value the field cannot legally take, and never silence.)*

---

## 2. Sector Execution Context

**Status:** new in this pass. Grounded in the existing Sub-Sector hub; introduces no store.

> **The law: no Sector skill may execute against an unresolved sector context.**

### 2.1 Resolution order

```
the record / request
      ↓  resolve
   Sub-Sector          (DB2 — the hub; 321 rows; every Sector query traverses it)
      ↓  Parent Sector relation
   Sector              (DB1)
      ↓  Status + plugin lookup
   Sector Plugin       (sector_plugins/{sector}/ — MAY be absent)
      ↓
   Geography scope     (DB11 subtree, when the work is place-bound)
```

Resolve **through the canonical graph**, never by string-matching a name and never by hard-coded branch. `if sector == "hospitality"` in a universal skill is an architecture breach, not a shortcut.

### 2.2 What the context carries

Full shape: [`contracts/skill-execution-record.schema.json`](contracts/skill-execution-record.schema.json) `payload.context`.

`sub_sector_id · sub_sector_name · sub_sector_status · sector_id · sector_name · geography_ids · plugin · plugin_version · plugin_slots_used · plugin_slots_unavailable`

### 2.3 Stop conditions

| Condition | Action |
|---|---|
| `sub_sector_id` cannot be resolved | **STOP.** Record `resolution_failure`. No write. |
| Two sub-sectors match ambiguously | **STOP.** Ambiguity is not a tie to break. |
| Sub-Sector has no `Parent Sector` | **STOP.** Report the broken hub row. |
| The work is place-bound and no Geography resolves | **STOP** for place-bound skills (S05, S09); proceed for others with `geography_ids: []`. |
| A required plugin slot is **unauthored** | Record it in `plugin_slots_unavailable` and **report the dependency as unmet**. Do not substitute a neighbouring value. |
| No plugin exists for this sector | **PROCEED.** A plugin-less sector must return an empty-but-valid result — this is the falsification test (§7.2). |

**Never default to Hospitality.** Hospitality is Sector #001, the currently activated sector. It is not the system default, and a context that falls back to it is a system that has silently become a hospitality tool.

### 2.4 Context is not the same as authorisation

A resolved context says *which market*. It does not say *may this skill run*. Gate eligibility (`Status = Target`, upstream skills complete, sources registered) is separate — see `SECTOR_SKILL_MATRIX.md` §3.

---

## 3. Field classes and write authorisation

Two orthogonal classifications, both already in the repo, now applied per field in [`contracts/sector-databases.json`](contracts/sector-databases.json).

### 3.1 Field class — *what kind of thing is this?*

| Class | Skill behaviour |
|---|---|
| `direct` | Research it. Cite the source. Set confidence to match. |
| `derived` | **Never research it.** Run the derivation, or leave it empty. |
| `state` | Transition logic only. Evidence-gated where the state machine says so. |
| `relation` | Resolve against the canonical record. Never re-store its content. |
| `strategic` | An Arika judgement. **Owner decision, not a research task.** |
| `meta` | Required whenever the value it governs is written. |
| `vocab` | Validate against the **live** option set before writing. |

**Why this is load-bearing.** Four empty cells, four different correct responses: empty `Definition` → research; empty `Sector Priority Score` → the derivation has not run; empty `Related Clients (CRM)` → query the CRM; empty `Portfolio Mode` → the owner has not decided. A skill that treats every blank as "find something" poisons the layer.

### 3.2 Authorisation disposition

**Origin:** `FIELD_POPULATION_PLAN.md` §0 — reused verbatim, not restated in new words.

| | Who fills it | Honesty gate |
|---|---|---|
| 🟢 **Fillable now** | Claude Code + web research, or transcription from an existing repo/owner source | Cite the source; set `Confidence` to match — research = Medium, owner-adopted = High. Web-verified, dated. |
| 🟡 **Needs owner** | A decision only the owner can make | **Not a research task. Do not infer it.** |
| 🔴 **Needs scraping** | The gated Collection layer — API key + cost governance + Legal posture + Approval-Matrix row | Writes real `Person`/`Company` to CRM. **Never invented.** |
| ⚫ **Never fill / template** | Nobody, until a real external system connects | Live booking/property numbers, performance metrics, unpublished results. |

**Governing rule, verbatim:** *"A field is only filled from its true source — an empty field is a legitimate state; a plausible-looking guess is a constitutional breach."*

### 3.3 One writer per field

Every field in the JSON twin names exactly one `writer_skill`. **A field with no `writer_skill` has no sanctioned writer and must not be written until one is assigned.** This is `AEIT_06`'s "one owner per entity" applied one level down.

---

## 4. Eligibility gates

Run **in order**. Any FAIL stops the write; record which gate failed and why.

### 4.1 Decision-purpose gate

**Origin:** Contract §13.3, verbatim: *"populate a field **only** when it has a **named downstream decision or execution purpose**. A datapoint that no decision consumes is noise — do not collect it, do not store it. This supersedes 'collect because we can.'"*

Applied to sources (§14.5): every registered source names where its data feeds. **No source without a destination DB.**

### 4.2 Evidence gate

No source → no row. Not a low-confidence row: **no row.** Q2 is not optional.

### 4.3 Confidence-matches-evidence gate

Weak evidence + `High` confidence is a **constitutional breach**, not a rounding error. If the evidence supports only "several commercial-intel sources agree", the confidence is `Medium` and the basis says so.

Never: no evidence → a confident value. If evidence is insufficient: reject, leave empty, mark unresolved, escalate, or trigger research.

### 4.4 Tier and freshness gate

**Origin:** Contract §6, §12, §15; `SECTOR_CALENDAR_REFRESH_SPEC.md` §2a.

- **Inheritance:** a record's `Source Tier` is **inherited from the registered source** (DB14 `Authority Level`). A record may never out-rank its publisher.
- **T4 rule:** *a T4 source may **discover** but may not **confirm**.* A T4/unverified/stale record **MUST NOT** drive a downstream event, a department action, or an execution.
- **Disagreement rule:** where an aggregator and the organizer disagree, **the organizer wins**.
- **Stale rule:** *"Stale intelligence MUST NOT drive downstream execution without revalidation."*
- **Tier floor:** T3/T4-sourced records are re-verified **one level higher** than their distance implies, and **cannot reach `Confirmed`** without a T1/T2 source.

**Proximity escalation ladder** (`SECTOR_CALENDAR_REFRESH_SPEC.md` §2a):

| Time to date | Monitoring | Re-verify |
|---|---|---|
| > 180 days | Normal | Monthly |
| 180–90 | Elevated | Fortnightly |
| 90–30 | High | Weekly |
| < 30 | **Critical** | Every run |
| < 7 | **Critical** | Every run — a change escalates immediately |

Overrides that beat the ladder: `Needs verification` → every run · `Superseded/Delayed` → every run until resolved · **Regulatory and Economic → at least monthly regardless of distance** · `Annual-recurring` → verified once per cycle at T-180 and **never auto-rolled forward** (*a recurring event is a prediction until its next edition is published*).

### 4.5 Registration gate (sources only)

**Origin:** `AEIT_08` §5. A source enters `State = active` **only after a live verification call proves it answers**. No source is registered on faith. Any `scrape` source requires a Legal (10) posture note before `active` — a Class-2+ gate. **Supersession, never deletion.**

**Two clarifications from the first registration pass (2026-08-24), both generalisable:**

- **Authority and reachability are different axes.** `Authority Level` describes the *publisher*; `State` describes whether we can actually follow it. A government ministry whose site fails TLS is still `T1 Primary` and still `candidate` — do not downgrade the tier to express a connection problem, and do not promote on authority alone. Two of two Kenyan ministry domains failed this way in one session.
- **`Last Verified` means last *successful* verification.** A failed attempt leaves the field **blank** and is recorded in the row's notes with the URL tried and what came back. A date in that field reads as proof the source answered; writing one for a failed call is the same class of error as a plausible `Feed URL`.

### 4.6 Vocabulary gate

Every `vocab` field validates against the **live** Notion option set, fetched at write time — not against a value remembered from a spec. Two option sets are known-divergent from their documentation (F1, F13); a remembered value can be silently wrong.

### 4.7 Relation-target gate

Before writing a relation, confirm the target record exists. A relation to nothing is worse than an empty relation: it looks resolved.

---

## 5. Mutation modes

Every write selects **exactly one mode, explicitly**. Never implied by what happened.

| Mode | When | Requirement |
|---|---|---|
| `CREATE` | No equivalent record exists | All required fields; all gates pass |
| `UPDATE` | Same record, new/better values, **no contradiction of a prior claim** | Provenance updated alongside |
| `VERSION` | The claim **changed** — a date moved, a number was corrected | The 5-step change-history rule (§5.1) |
| `SUPERSEDE` | A record is replaced by a better-sourced one | Both records survive; the chain is auditable |
| `NO_OP` | Nothing material changed | Still bump `Last Verified` — *checked and unchanged* is a real result |
| `REJECT` | A gate failed | Record which gate and why. **Not a silent skip.** |
| `ESCALATE` | The write would require an architecture change | Tier-1 questions, plugin-wants-a-field, unresolvable conflict |

**Never silently overwrite historical truth where versioning or supersession applies.** **Never create a duplicate because a skill was retried** — match on the natural key first (`Sector ID`, `Sub-Sector ID`, `Source ID`, `Route ID`, `Destination ID`, or title + sub-sector).

### 5.1 The change-history rule — now general

**Origin:** `SECTOR_CALENDAR_REFRESH_SPEC.md` §2b, written for DB7 signals. **Generalised here to every Sector database**, which is the single largest addition this contract makes.

On any `VERSION` or `SUPERSEDE`:

1. **Preserve the prior value.** DB7 has `Previous Signal Date` + `Change Reason`. **Databases without those fields record it in the page body** — a dated line, never a lost value.
2. **Append a dated change line to the page body:** *what changed · when · which source · what tier.*
3. **Set the status fields.** DB7: `Change Status` + `Refresh Status`. Elsewhere: the nearest state field, or the body line if none exists.
4. **Name what it invalidates.** Market Routes, Content Opportunities, campaign windows, derived activation dates, downstream briefs. Contract §15: *"This is the difference between a database row edit and operating-system behaviour."*
5. **Emit the matching event** — **after** checking it has a subscriber (§6.5).

Step 4 is the one most easily skipped and the one that makes this a system rather than a table.

---

## 6. The loops

Every skill declares which loops it participates in.

### 6.1 Activation
`new sector/sub-sector → taxonomy → plugin → intelligence + audience/language → sources → signals → place → state → calendar → commercial routing → handoff`
Maps to the nine activation gates A–I (`SECTOR_ACTIVATION_PROTOCOL.md`; mapping in `SECTOR_SKILL_MATRIX.md` §4).

### 6.2 Refresh
`stale knowledge → research → agent proposal → skill validation → mutation → downstream refresh`
Driven by `Next Review` / `Next Verification` and the §4.4 ladder. **These fields are operational, not decorative metadata.**

### 6.3 Signal-change
`external change → source re-verification → VERSION the signal → name what it invalidates → recalculate state → recompute calendar → emit`

### 6.4 Calendar recomputation
`signal / geography / state / client change → deterministic resolver → new calendar output → content opportunities`
**The calendar is computed, never stored.** A 365-day calendar is `resolve(sector, geography, property_type, null, 365d)` — an *output*. It is never authored as 365 rows.

### 6.5 Feedback — **cannot close today**

`downstream outcome → observed intelligence → research → finding → state update`

**Stated plainly: there is no performance store anywhere in the agency.** `SECTOR_OS_ARCHITECTURE.md` §1.3 finding 3 and §6 record this; Marketing (03) owns the concept and has none. The `PERFORMANCE → INTELLIGENCE` return edge is **doctrine only**.

Until a performance store exists, the feedback loop runs **only** where a human observes an outcome and feeds it back as a cited finding through S01. A skill must not describe this loop as automated, and must not infer performance from activity.

### 6.6 Failure / recovery
`proposal → validation failure → REJECT / incomplete / stale / ESCALATE → correction or research → re-entry`
A rejection is a **record**, not a silence. It carries which gate failed, and what would make the write valid.

---

## 7. Observability

### 7.1 The execution record

Every skill run appends one line to `01_Sector/_memory/skill_runs.jsonl`, conforming to [`contracts/skill-execution-record.schema.json`](contracts/skill-execution-record.schema.json).

The envelope **deliberately mirrors** `arika-runtime/src/memory-writer.ts` (`{timestamp, agent, department, stream, event_type, source, payload}`) so a future code runtime reads one format. Divergences: `agent`→`skill`, `event_type: "skill_run"`, `source: "claude-code"`.

**A separate file from `runtime.jsonl` on purpose.** `01_Sector/_memory/` does not exist on disk today, which is *evidence* that no Sector agent has ever run through the runtime. Mixing skill runs into `runtime.jsonl` would destroy that signal.

An operator must be able to answer, from the log alone: *What happened? Why? What evidence caused it? What changed? What did it invalidate? What happens next?*

### 7.2 The falsification tests

Two, from the department's own doctrine. A skill that cannot pass them is wrong regardless of what it produced.

- **Plugin-removal (`SECTOR_OS_ARCHITECTURE.md` §7):** remove the Sector #001 plugin. The Universal Core MUST still load and return an **empty-but-valid** resolution for a sector with no plugin. If it breaks, this is a single-sector system wearing a Sector-OS label.
- **Structural difference (Gate F):** two structurally different places in the same sector MUST resolve to structurally different outputs. Identical shapes mean the destination/property-type layers are inert. **STOP** — do not load more data on top of a model that has not been falsified.

---

## 8. The standing laws

Restated because every skill inherits them, each cited to its origin.

1. **Empty is legal; plausible is not.** *"Structure before content. Registries may exist as empty/placeholder structure without being a failure — but may not be filled with guessed values to look complete."* (Constitution §3.) A slot or field filled with a plausible unsourced value is a **constitutional breach** — revert it to empty.
2. **No silent invention.** Never fabricate sector facts, company financials, pricing, dates, contacts or property numbers. When source material is missing, **say so**.
3. **Reference, never duplicate.** CRM is live in ClickUp; Offer (02) owns offers; Marketing (03) owns `Competitor`; Content (04) owns Content Intelligence. Sector links **by ID**. *"Never retype upstream truth downstream — Content inherits Sector via rollups; Sector references CRM by ID."*
4. **Sector emits the packet; Sales and Content own the script.** (Contract §14.3.) Sector produces timing + pain + language + who + offer-match + outreach **angle**. It does **not** write the final email, proposal or script. Route the packet; do not re-own their artifact.
5. **No named individuals in Sector stores.** Titles and roles only. Real people are scraped into the CRM under Legal gating. **No fabricated contact, ever.**
6. **A plugin supplies values into core fields.** It never adds a store, a field, an agent or an event. If a sector appears to need one → **ESCALATE** as a Tier-1 architecture change requiring owner ratification and an `AEIT_06` entry. Do not edit the plugin.
7. **A universal file must not carry a sector's rule values.**
8. **Derived is never fact.** An activation date computed from a plugin timing table is a **planning offset**, and must be labelled as one. A resolution output is not an external truth.
9. **No self-promotion.** Lifecycle State advances only when the underlying rows exist.
10. **No handoff into a dead event.** Routing to an event with zero subscribers is a `HANDOFF_FAILURE`, recorded as such. **Do not silently discard the packet.** ([`contracts/event-catalog.json`](contracts/event-catalog.json) is the live list.)
11. **Human sign-off for Risk Class 3+**, *"with no exceptions carved out by convenience or urgency."* (Constitution §3.)
12. **Every significant decision is logged** in the department's Decision Log — not just stated in conversation.

---

## 9. Cross-references

[`SECTOR_DISCOVERY_INVENTORY.md`](SECTOR_DISCOVERY_INVENTORY.md) · [`SECTOR_SKILL_MATRIX.md`](SECTOR_SKILL_MATRIX.md) · [`SECTOR_EVENT_CATALOG.md`](SECTOR_EVENT_CATALOG.md) · [`SECTOR_ACTIVATION_CONTRACT.md`](SECTOR_ACTIVATION_CONTRACT.md) §6 §12 §13 §14 §15 §16 · [`SECTOR_ACTIVATION_PROTOCOL.md`](SECTOR_ACTIVATION_PROTOCOL.md) · [`SECTOR_OS_ARCHITECTURE.md`](SECTOR_OS_ARCHITECTURE.md) §4 §7 · [`FIELD_POPULATION_PLAN.md`](FIELD_POPULATION_PLAN.md) §0 §7 · [`SECTOR_CALENDAR_REFRESH_SPEC.md`](SECTOR_CALENDAR_REFRESH_SPEC.md) §2a §2b · `00_Agency_Governance/AGENCY_OPERATING_CONSTITUTION.md` §3 §5 · `00_Agency_Governance/AUTOMATION_APPROVAL_MATRIX.md` · `00_Agency_Governance/enterprise_architecture/AEIT_06`, `AEIT_08` §5, `AEIT_09` · `04_Content/CONTENT_INTELLIGENCE_SCHEMA.md` §7

## 10. Changelog

- **v0.1 (2026-08-24, Gate 1 — CONTRACT):** Created. **Assembled** from `SECTOR_ACTIVATION_CONTRACT.md` §13.3 (the eight questions, enumerated and encoded for the first time), `FIELD_POPULATION_PLAN.md` §0 (dispositions), Contract §6/§12/§15 (tier, freshness, T4), and `SECTOR_CALENDAR_REFRESH_SPEC.md` §2a/§2b (ladder + change-history). **New:** the Sector Execution Context and its stop conditions; the seven explicit mutation modes; **generalisation of the 5-step change-history rule from DB7 signals to every Sector database**; the skill execution record. **Stated plainly for the first time:** the apply step is a human-invoked session, this contract has no validator, and the feedback loop cannot close because no performance store exists anywhere in the agency. — Claude Code (Opus 5)
