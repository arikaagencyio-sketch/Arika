# Content — Write Contract

**Department:** Content (04) · **Version:** v0.1 (2026-10-09) · **Status:** In force for manual apply. Seven skills implement it (C01–C07). **No skill has run yet**, and `04_Content/_memory/` holds no execution record. The first apply under this contract will be the first one.

**Machine-readable companion:** [`contracts/content-databases.json`](contracts/content-databases.json) (one writer per field, DB1–DB8, from the live schemas of 2026-10-09). **Runnable gate:** [`contracts/content_write_gate.py`](contracts/content_write_gate.py) with tests in [`contracts/test_content_write_gate.py`](contracts/test_content_write_gate.py).

> **Every Content skill opens by reading this file.** It is modelled on [`01_Sector/SECTOR_WRITE_CONTRACT.md`](../01_Sector/SECTOR_WRITE_CONTRACT.md) and reuses its vocabulary (field classes, mutation modes, the change-history rule) rather than inventing a second one. Where this file and an origin it cites disagree, the origin wins and the divergence is a defect here.

**Precedence:** `AGENCY_OPERATING_CONSTITUTION.md` → `GLOBAL_OS.md` → [`CONTENT_OS.md`](CONTENT_OS.md) → [`CONTENT_INTELLIGENCE_SCHEMA.md`](CONTENT_INTELLIGENCE_SCHEMA.md) (why a field exists) → **this file** (who may write it, and how) → the current task.

---

## 0. Two things stated plainly

### 0.1 The apply step is a human-invoked Claude Code session

`arika-runtime` has no Notion client. Agents in `.claude/agents/content-*.md` reason and recommend; a person invokes a skill in an interactive session, and the skill performs the write through the Notion connector. Manual apply needs no `AUTOMATION_APPROVAL_MATRIX.md` row ([`CONTENT_INTELLIGENCE_SCHEMA.md`](CONTENT_INTELLIGENCE_SCHEMA.md) §7). **That exemption ends the moment anything writes unattended.**

### 0.2 What the gate enforces, and what it does not

[`content_write_gate.py`](contracts/content_write_gate.py) enforces two things by exit code: the contract's own integrity (one writer per field, trigger properties intact, skills present on disk), and the refusal rules in §5 against a **write proposal**. It does **not** read Notion. Read-after-write verification (§6.3) is a step the skill performs and records. Said plainly so no reader mistakes the gate for a check on the live database.

---

## 1. What Content owns, and what it never owns

| Store | Owner | Content's relationship |
|---|---|---|
| DB1 Platform Registry: platform behaviour fields | Content (04) | Writes via C03 |
| DB1 `Account Status` | Presence (21) | Reads. Account truth is `21_Presence/PLATFORM_ONBOARDING_TRACKER.md` |
| DB2–DB7 | Content (04) | Writes via C01–C06, one writer per field |
| DB8 Offer Registry (thin) | **Offer (02)** | Reads only. Content never creates, edits or prices an offer |
| Sector DBs (findings, signals, audience roles, decision-makers, linguistics) | **Sector (01)** | Links by relation; never retypes Sector truth |
| CRM people and companies | **Sales (05) / ClientPartner (06)** in ClickUp | Never stored here. No named individual in any Content store |
| Assets, storyboards, generation prompts, Canva folders | **Design (19)** | Referenced by ID (§9). Content never stores the master file |
| `Packet State`, `packet_id`, `variant_id` | **Presence (21)** L3 Reservoir | Reserved. Content does not write them |

**Hospitality is the first pilot sector, not the default.** A record with no `Sub-Sector` is agency-wide and legal. A skill that falls back to Hospitality when no sector is given has made Content a hospitality tool. That is a defect.

---

## 2. Writer kinds

Every field in [`content-databases.json`](contracts/content-databases.json) names exactly one writer:

| Writer | Meaning |
|---|---|
| `C01`…`C07` | The one skill that may write the field (§3) |
| `computed:formula` · `computed:rollup` | Never written. Change the upstream record |
| `reverse:<DB>.<field>` | The back-side of a two-way relation. Written only by writing the named forward side |
| `human_only` | Set by a named human in Notion. No agent or skill writes it, ever |
| `external:<dept>` | Owned elsewhere. Content reads |
| `reserved:<dept>` | Frozen for another department's machinery |

Two value-level restrictions sit on top of the writer:

- **`human_only_values`**: values only a human may set. `Publishing Status` = `Ready for Design` or `Done`. `G2 Decision` = `Approved`, `Rejected`, `Changes requested`.
- **`owner_decision_values`**: values a skill may write **only when transcribing a recorded owner decision**, with the quote and date in the proposal and in the page-body change line. DB2 `Status = Active`, DB2 `Authority Level = Agency doctrine`, DB5 `Decision = Promoted to Brief`, a new DB1 platform, a new DB4 campaign.

Field classes reuse Sector's seven (`direct`, `derived`, `state`, `relation`, `strategic`, `meta`, `vocab`) verbatim. An empty `derived` field means the computation has not run. An empty `strategic` field means the owner has not decided. Neither is a research task.

---

## 3. The skills and their write boundaries

Full matrix: [`CONTENT_SKILL_MATRIX.md`](CONTENT_SKILL_MATRIX.md). Grouped by real write boundary, not one skill per database.

| ID | Skill | Writes | Reads |
|---|---|---|---|
| C01 | [`content-opportunity-intake`](../.claude/skills/content-opportunity-intake/SKILL.md) | DB5 (opportunity + **Strategic DRAGON**), DB4 (campaign) | Sector findings, signals, audience roles; DB2; DB1 |
| C02 | [`content-narrative-review`](../.claude/skills/content-narrative-review/SKILL.md) | DB2 only | DB5, DB6, DB7 (to review both DRAGON passes in order) |
| C03 | [`content-surface-translation`](../.claude/skills/content-surface-translation/SKILL.md) | DB1 (behaviour), DB3, DB6 (incl. **Editorial DRAGON**, `Surface`) | DB2, DB5, Sector |
| C04 | [`content-brief-writer`](../.claude/skills/content-brief-writer/SKILL.md) | DB7 authored fields (copy, script, carousel, long-form) | DB5, DB6, DB2, DB3, DB4, DB8 |
| C05 | [`content-claim-review`](../.claude/skills/content-claim-review/SKILL.md) | **nothing** (returns a verdict) | Everything the claim cites |
| C06 | [`content-approval-prep`](../.claude/skills/content-approval-prep/SKILL.md) | DB7 `G2 Decision` = `Not submitted` / `Submitted for review` only | DB7 + C05 verdict |
| C07 | [`content-source-retrieval`](../.claude/skills/content-source-retrieval/SKILL.md) | **nothing** | Any source or asset by canonical ID |

**Agents decide; skills validate and apply.** The six `content-*` agents produce recommendations shaped to these fields. They never write.

---

## 4. Two-pass DRAGON (owner-ratified 2026-10-09)

DRAGON is one strategy run in two passes. Strategic DRAGON decides what is true and worth saying; Editorial DRAGON decides how to say it so it lands.

| Pass | Letters | Recorded on | Writer |
|---|---|---|---|
| **Strategic** | Diagnosis · Revenue Logic · Architecture · Growth Systems · Operational Intelligence · Navigation | DB5 `Strategic DRAGON` + `Strategic DRAGON Notes` | C01 |
| **Editorial** | Dialogue · Relatability · Authenticity · Growth · Opinion · Niche-orientation | DB6 `Editorial DRAGON` + `Editorial DRAGON Notes` | C03 |

**One canonical representation.** In agent output it is a single nested object, `dragon.strategic` and `dragon.editorial`, each `{status, reason, letters: {D,R,A,G,O,N}}`. No flat aliases are stored beside it.

**Rules (enforced: R07, R08):**
1. Order is fixed: Strategic → Editorial → G2 quality review → human approval. An Editorial pass may not be recorded while the Opportunity's Strategic pass is `Not yet run`.
2. Every new record declares its pass status: `Complete`, `Partial`, `Not applicable`, or `Not yet run`. A blank is refused.
3. `Partial` and `Not applicable` require a reason in the Notes field.
4. **History is preserved.** The v1 record `nar-terminology-dragon` keeps `Conflict — unresolved` and is `Superseded`; its successor is `nar-terminology-dragon-v2`. Records carrying `LinkedIn — content construction` or `Realignment — operating philosophy` keep those values. The 10 belief rows created 2026-08-19 with a blank `DRAGON Reading` are left as they are and recorded as a known gap ([`CONTENT_RECONCILIATION_LEDGER.md`](CONTENT_RECONCILIATION_LEDGER.md) §4).

---

## 5. Refusal rules

Every rule has a code in the gate. A refusal is a record: which rule, and what would make the write valid.

| Code | Refuses | Origin |
|---|---|---|
| R00 | Unknown database, field or mode. A mode is always explicit | Sector contract §5 |
| R01 | A field written by the wrong skill; a human-only field or value written by a skill | §2 |
| R02 | Writing a formula, rollup, or the reverse side of a relation | §2 |
| R03 | A brief without Opportunity, Translation and Narrative Position; a translation without Opportunity, Platform and a source; an opportunity with no Source or no upstream finding/position | Schema doc §8 ("the brief is never the starting point") |
| R04 | A fact or statistic with no dated source; a client outcome without proof on record; an unclassified claim | "Never publish: Authority Without Evidence" |
| R05 | A fact resting only on T4 sources | Sector activation contract §12 |
| R06 | Translation Family ID ≠ Source Truth Position ID; a brief whose narrative positions exclude its translation's family | Schema doc DB6 |
| R07 | A blank, invalid, or unreasoned DRAGON pass status | §4 |
| R08 | Editorial before Strategic; a Ready-for-Design recommendation without both passes | §4 |
| R09 | A LinkedIn translation with a non-LinkedIn surface; a LinkedIn brief recommended ready while `Surface = Not yet assigned` | §7 |
| R10 | A CREATE without its natural key, or one that duplicates an existing natural key. Retries never duplicate | Sector contract §5 |
| R11 | Publication without a human G2 `Approved` decision, reviewer and date; any agent as publisher | Constitution §5, Class 3 |
| R12 | Approval bound to a different revision than the one published | §8 |
| R13 | Publishing through Postiz before warm-up has cleared, the channel is connected, and a matrix row exists | Presence tracker §3 |
| R14 | A publication record that cannot link back: missing brief, surface, URL or date; a non-LinkedIn URL for a LinkedIn surface | §8 |
| R15 | First-person singular in Company Page copy. The Page speaks institutionally | `21_Presence/LINKEDIN_PRESENCE_OS.md` §4.6 |
| R16 | Any pricing or offer-term claim without an `Active` Offer (02) row. The Offer relation is optional; its absence forbids commercial claims | §1 |
| R17 | Renaming, retyping, dropping or reordering a trigger-read property | §7 |
| R18 | Writing a field reserved for or owned by another department | §1 |
| R19 | An owner-decision value without a recorded quote and date | §2 |

---

## 6. Mutation modes, change history, verification

### 6.1 Modes

Reused verbatim from Sector: `CREATE` · `UPDATE` · `VERSION` · `SUPERSEDE` · `NO_OP` · `REJECT` · `ESCALATE`. Select exactly one, explicitly. Match on the natural key before any CREATE. A retried skill never creates a second record.

| DB | Natural key |
|---|---|
| DB1 | `Platform` |
| DB2 | `Position ID` (a new version gets a new ID, e.g. `-v2`) |
| DB3 | `Overlay ID` |
| DB4 | `Campaign Code` |
| DB5 | `Opportunity ID` |
| DB6 | `Translation Family ID` + `Platform` + `Surface` + `Format` |
| DB7 | `Translation` (one live brief per translation; a new revision is a VERSION, which bumps `Version`) |

### 6.2 The change-history rule

On any UPDATE that replaces a value, and on every VERSION and SUPERSEDE, append a dated line to the page body: what changed, the prior value, why, the source, and what it invalidates. Never silently overwrite. Example (applied 2026-10-09): *"`Audience Role` `CEO` → `General Manager / Owner`. Reason… Source: Sector DB 9 role page… Prior value preserved here."*

### 6.3 Read-after-write

After every apply, read the record back (fetch the page, or query the field) and compare it with the proposal. A write the connector reports as successful but that does not read back is a **partial failure**. Record it as one; do not retry blind.

**A failed query is never zero results.** When the Notion query quota is exhausted or the connector errors, the operation is `incomplete`, and the record says so. Fall back to fetching pages by ID where possible.

---

## 7. Four state axes, never merged

| Axis | Field | Who moves it |
|---|---|---|
| Knowledge maturity | `Status` (Draft → Validating → Active → Superseded → Archived) on DB1–DB6, DB8 | The DB's writer skill; `Active` on DB2 needs an owner decision |
| Production trigger | DB7 `Publishing Status` (Not started → In progress → **Ready for Design** → Done) | C04 for the first two; **a human** for Ready for Design and Done |
| G2 decision | DB7 `G2 Decision` + `G2 Reviewer` + `G2 Decided At` + `G2 Approved Revision` | C06 may set Not submitted / Submitted for review; **a human** sets the decision, reviewer, date and revision |
| Packet lifecycle | DB7 `Packet State` | Reserved for Presence (21) |

A value on one axis never implies a value on another. DB7 `Approval Integrity` (formula) shows a red cell when the packet lifecycle runs ahead of G2, or when an approval names a revision other than the current `Version`.

**Trigger-read properties are frozen** (R17): `Title`, `Script`, `Caption`, `Visual Direction`, `Canva Instructions` (text/title) and `Publishing Status` (select: `Not started`, `In progress`, `Ready for Design`, `Done`, in that order). Routine `trig_01WyyrXEkFZck1D49tm6BfKv` reads them by name.

---

## 8. G1 and G2 are different decisions

| | G1 Concept review | G2 Pre-publish approval |
|---|---|---|
| Question | Should this exist at all? | Is this exact artifact safe and right to publish? |
| Object | An opportunity or translation (an idea) | One brief at one `Version` (the final artifact) |
| Who | Presence economics gate + Content (advisory) → human | `content-publishing-gate` (advisory) → **a named human**, Class 3 |
| Recorded | DB5 `Decision` (`Promoted to Brief` = owner decision) | DB7 `G2 Decision` = Approved + Reviewer + Decided At + Approved Revision |
| Expires | No | **Yes.** Any copy change bumps `Version`, and the approval no longer covers it |

Passing G1 never implies G2. A G2 approval never covers a later revision. **No agent and no skill can approve** (R01, R11).

---

## 9. Source and asset retrieval contract

Content references sources and assets **by canonical ID**. It never becomes a second store of them.

### 9.1 What a reference carries

| Field | Meaning |
|---|---|
| `id` | The canonical ID in the owning store: Notion page ID, Sector finding ID, Design asset ID |
| `owner` | The department that owns the record (01, 02, 04, 19…) |
| `uri` | Notion URL, Drive file ID or folder ID, Canva design or folder ID. **Never a temporary vendor URL** (§9.3) |
| `scope` | `company` (Arika's own content) or `pilot:<pilot-id>` |
| `version` | The owner's version or revision |
| `provenance` | Source + tier + `verified_at` for facts; generator + job ID + prompt-record ID for generated media |
| `rights` | `owned` · `licensed` · `public-source` · `unknown` |
| `licence` | The licence or terms reference when not owned |
| `permitted_use` | e.g. `internal-only`, `organic-social`, `paid`, `client-deliverable` |
| `media_type` | MIME type or `notion-record` |
| `approval_state` | The owner's approval state (Design QA; G2 for public copy) |

Rights `unknown` blocks a Ready-for-Design recommendation for any asset that would appear in public output.

### 9.2 The Design-owned Asset Registry

The Asset Library is **Design (19)'s** (`19_Design/DESIGN_OS.md` §3, `design-asset-librarian`), and today it is **documented architecture, not built**. Content does not build a competing one. The provider-neutral registry contract (stable `asset_id`, `campaign_id`, `brief_id`, `variant_id`, `translation_family_id`, source tool and job, storage URI, rights, licence, expiry, checksum, version, supersedes, approval state) is Design's to ratify. Until it exists, C07 records `asset_registry: not built` rather than inventing IDs.

### 9.3 Temporary URLs are never storage

A generation vendor's delivery URL (OpenArt, KIE.ai, any signed link) expires. It may appear in a run log as provenance. **It may never be the only reference to an asset, and never sits in a Content field as the asset's location.** Large binaries never go into Git.

### 9.4 Folder alignment (proposal only)

Design's Canva structure is campaign-first and stays so (`Campaigns/<campaign>/Storyboards · Generated Assets · Video · Carousel · Presentation · Thumbnail · Ads · Final`). The proposed mapping for Content's stages: **draft** → no asset (copy lives in DB7) · **template** → `Templates/` · **visual** → `Generated Assets/` and `Carousel/` · **video** → `Video/` · **final** → `Final/`. No folder is created by this contract. Pilot material stays within the existing permission: Google My Drive in **limited public-only test mode**, not approved for private or client data (`13_Tech_Stack/TECHSTACK_OS.md` §3, 2026-09-21).

---

## 10. Manual handoffs

No Content event reaches another department automatically: the runtime publishes no agent events (`arika-runtime/src/executor.ts`), and six Content emits have no consumer. These handoffs are **manual by design**. Each one records operator, input IDs, output IDs, acceptance criteria and evidence.

| Handoff | Operator | Input → output | Accepted when | Evidence |
|---|---|---|---|---|
| Sector → Content | Human invoking C01 | Sector finding ID → DB5 opportunity ID | R03/R04/R05 pass; read-back matches | Page-body change line + DB5 `Source Intelligence` |
| Content → Design | **Human** sets `Ready for Design` | DB7 brief ID (+ Version) → routine storyboard comment | Both DRAGON passes set, surface assigned, Brief Integrity clean | The routine's comment on the brief page, carrying its marker |
| Content → G2 | Human invoking C06, then the reviewer | DB7 brief ID + Version + C05 verdict → `G2 Decision` | Reviewer, date and approved revision recorded by the human | DB7 G2 fields + Approval Integrity green |
| G2 → publication | **Human publisher** | Approved brief ID + Version → native post | R11–R14 pass | Publication record (brief ID, revision, surface, native URL, date, publisher) in the Presence publication log (not yet built) |
| Engagement → Sales | Human | Conversation → `LEAD_CREATED` input to `sales-lead-qualification` | Consent and CRM ownership respected | CRM record, owned by Sales |

### 10.1 Ordering mismatch, identified and not rewired

The data model puts **translation before brief**: a DB7 brief requires its DB6 translation (R03). The agent chain puts **multiplication after approval**: `content-multiplication-engine` listens for `CONTENT_APPROVED`, which `content-publishing-gate` emits only after a brief exists. Read literally, the engine that plans translations fires after the brief that needs them. Today this is harmless because no event is published and every step is manual. It is recorded here so the first event wiring does not encode it. Resolution belongs to a later, approved unit.

---

## 11. Observability

- `04_Content/_memory/` exists (placeholder only). It holds **no** `runtime.jsonl` and no skill-run log yet. No execution history is fabricated to make it look used.
- When a skill first runs, it appends one record to `04_Content/_memory/skill_runs.jsonl` in Sector's envelope ([`01_Sector/contracts/skill-execution-record.schema.json`](../01_Sector/contracts/skill-execution-record.schema.json), `source: "claude-code"`). Test runs never write there.
- The 2026-10-09 Notion changes predate the skills and are recorded in [`CONTENT_OS.md`](CONTENT_OS.md) §8 and the ledger, not back-dated into a run log.

---

## 12. Standing laws

1. **Empty is legal; plausible is not.** A blank research field is a task. A guessed value is a breach.
2. **No silent invention.** No client, outcome, proof, sector fact, price or performance figure without a source.
3. **Reference, never duplicate.** Sector, Offer, CRM and Design records are linked by ID, never retyped.
4. **Agents never publish, approve, or impersonate.** Every public artifact passes a named human's G2 on its exact revision.
5. **Historical truth is versioned, never overwritten.**
6. **Hospitality is a pilot, not a default.**
7. **A failed query is incomplete, never empty.**
8. **Every significant decision is logged** in `CONTENT_OS.md` §8.

## 13. Changelog

- **v0.1 (2026-10-09)** — Created under the owner's Content-unit authorisation. Modelled on Sector's v0.2 contract. Adds what Sector's lacks: a runnable gate that refuses write proposals. Owner direction recorded: two-pass DRAGON (§4). Notion changes applied the same day are in `CONTENT_OS.md` §8. — Claude Code (Opus 5.5)
