# Content — Write Contract

**Department:** Content (04) · **Version:** v0.4 (2026-10-10, storage unit) · **Status:** In force for manual apply. Seven skills implement it (C01–C07). **No skill has run yet**, and `04_Content/_memory/` holds no execution record. The first apply under this contract will be the first one.

**Machine-readable companion:** [`contracts/content-databases.json`](contracts/content-databases.json) (one writer per field, DB1–DB8, from the live schemas of 2026-10-09). **Runnable gate:** [`contracts/content_write_gate.py`](contracts/content_write_gate.py) with tests in [`contracts/test_content_write_gate.py`](contracts/test_content_write_gate.py).

> **Every Content skill opens by reading this file.** It is modelled on [`01_Sector/SECTOR_WRITE_CONTRACT.md`](../01_Sector/SECTOR_WRITE_CONTRACT.md) and reuses its vocabulary (field classes, mutation modes, the change-history rule) rather than inventing a second one. Where this file and an origin it cites disagree, the origin wins and the divergence is a defect here.

**Precedence:** `AGENCY_OPERATING_CONSTITUTION.md` → `GLOBAL_OS.md` → [`CONTENT_OS.md`](CONTENT_OS.md) → [`CONTENT_INTELLIGENCE_SCHEMA.md`](CONTENT_INTELLIGENCE_SCHEMA.md) (why a field exists) → **this file** (who may write it, and how) → the current task.

---

## 0. Two things stated plainly

### 0.1 The apply step is a human-invoked Claude Code session

`arika-runtime` has no Notion client. Agents in `.claude/agents/content-*.md` reason and recommend; a person invokes a skill in an interactive session, and the skill performs the write through the Notion connector. Manual apply needs no `AUTOMATION_APPROVAL_MATRIX.md` row ([`CONTENT_INTELLIGENCE_SCHEMA.md`](CONTENT_INTELLIGENCE_SCHEMA.md) §7). **That exemption ends the moment anything writes unattended.**

### 0.2 What the gate enforces, and what it does not

[`content_write_gate.py`](contracts/content_write_gate.py) enforces two things by exit code: the contract's own integrity (one writer per field, trigger properties intact, skills present on disk), and the refusal rules in §5 against a **write proposal**. It does **not** read Notion. Read-after-write verification (§6.3) is a step the skill performs and records. Said plainly so no reader mistakes the gate for a check on the live database.

**What it cannot protect (stated 2026-10-09, correction unit).** The gate sees only what a skill hands it. Three gaps follow, and none is closed:
- **A person editing a brief directly in Notion bypasses it.** That covers changing a caption without bumping `Version`, typing a new select option, or setting `G2 Approved Revision` to the wrong number.
- **Approval Integrity cannot catch every stale approval.** The formula compares `G2 Approved Revision` with `Version`. It cannot see a copy change that happened without a bump.
- **There is no change-detection evidence.** Nothing in this repository proves that any brief's copy matches the revision a human approved. Notion page history is the only trail, and nothing reads it automatically.

So: the gate makes a skill-driven write safe. It does not make the database safe. A content hash recorded at G2 would close part of the gap. That would be a new property or a page-body convention, and it is **proposed, not built**. The minimal storage and fingerprint proposal, with exactly what it would and would not catch, is [`APPROVAL_EVIDENCE_STORAGE_PROPOSAL.md`](APPROVAL_EVIDENCE_STORAGE_PROPOSAL.md) (prepared 2026-10-09, not applied).

**Stored evidence narrows, and does not close, the gap (storage unit, 2026-10-10).** DB7 now stores:
- G1 (`G1 Decision`, `G1 Reviewer`, `G1 Decided At`, `G1 Revision`);
- the G2 packet (`G2 Packet Manifest`, `G2 Submitted Fingerprint`).

What this catches, the next time a check runs:
- a direct Notion edit to publishable copy, assets or resolved context after submission (R26 at publication, R21 at re-submission);
- an unreadable or stale read, which is refused instead of trusted (R27).

What it does not do:
- **No check runs on its own.** Nothing is scheduled.
- **Human-only fields are not enforced.** The rule is this contract's convention, not a Notion permission.
- **Reviewer names are not authenticated.** A typed reviewer name is compared with the owner-only approver list (R28); neither the gate nor Notion verifies who typed it.
- **The Approval Integrity formula prevents nothing.** It shows a red cell; it stops no edit and authenticates no reviewer.

**A linked page can change beneath an approval (recorded 2026-10-10).** *(Closed for the resolved Surface, Audience Role, Format, Platform IDs and Offer Status by the storage unit, the same day: they are in the fingerprint. Other linked-page attributes are still not covered.)* The surface, audience role and format live on the DB6 translation, not on the brief. If that page's `Surface` changes after G2 while the brief's `Translation` relation keeps the same page ID, nothing in DB7 moves. Today's publication check then compares the published surface with the surface read **at publication**, not the one approved, so the approval silently carries over. Closing this needs stored approval evidence. The capture and comparison rules are specified in [`APPROVAL_EVIDENCE_STORAGE_PROPOSAL.md`](APPROVAL_EVIDENCE_STORAGE_PROPOSAL.md) §3.1. **Proposed, not built.**

**Evidence is only as good as its identity (hardening unit, 2026-10-09).** Every gate binds stage evidence to one brief ID and one Version: G1, storyboard, spend approval, claim review, asset provenance and the G2 packet. The gate cannot check that the evidence is *true*. A G1 line a person typed is taken at its word. What it refuses is evidence that is **unidentified, about another brief, or about another revision**. Before this unit, a G1 from brief B at revision 2 satisfied brief A at revision 2.

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
1. Order is fixed: Strategic → Editorial → the rest of the workflow in §8 (G1, then Design and spend approval for visual work, then G2 on the finished artifact). An Editorial pass may not be recorded while the Opportunity's Strategic pass is `Not yet run`. *(v0.1 wrote "Strategic → Editorial → G2 quality review → human approval", which skipped G1 and Design. Corrected 2026-10-09.)*
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
| R09 | A surface that does not fit the platform (a LinkedIn surface on a non-LinkedIn row, or `Single-identity channel` on LinkedIn); a brief recommended ready, or submitted to G2, while `Surface = Not yet assigned`. **R09_SURFACE_UNKNOWN:** a surface that is neither a live Notion option nor a mapped agent enum (§7.1). A Notion write must carry the exact Notion name | §7 |
| R10 | A CREATE without its natural key, or one that duplicates an existing natural key. Retries never duplicate. **R10_LOOKUP_UNVERIFIED:** a CREATE whose duplicate lookup is missing, failed, partial or of unknown status. Only a lookup with `status: complete`, a timestamp and a records list counts | Sector contract §5 |
| R11 | Publication without a human G2 `Approved` decision, reviewer and date; any agent as publisher; design work approved without a finished artifact | Constitution §5, Class 3 |
| R12 | A stale binding: an approval, G1 pass, spend approval, storyboard, submission or artifact for a different revision than the current one; published artifacts that differ from the approved set | §8 |
| R13 | Publishing through Postiz before warm-up has cleared, the channel is connected, and a matrix row exists | Presence tracker §3 |
| R14 | A publication record that cannot link back: missing brief, surface, URL or date; a surface outside the vocabulary or unassigned; a URL that is not https, or not on the surface's host (`linkedin.com` for both LinkedIn surfaces) | §8 |
| R15 | First-person singular in copy for a surface whose voice is `institutional` (`LinkedIn - Company Page`). The Page speaks institutionally | `21_Presence/LINKEDIN_PRESENCE_OS.md` §4.6 |
| R16 | Any pricing or offer-term claim without an `Active` Offer (02) row. The Offer relation is optional; its absence forbids commercial claims | §1 |
| R17 | Renaming, retyping, dropping or reordering a trigger-read property | §7 |
| R18 | Writing a field reserved for or owned by another department | §1 |
| R19 | An owner-decision value without a recorded quote and date | §2 |
| R20 | A revision that is missing or is not a whole number of 1 or more, anywhere it binds something (brief `Version`, approved revision, published revision, G1, spend approval, submission) | §6.4 |
| R21 | A publication-affecting change without exactly one `Version` increment; a bump with no such change; a copy change sent as UPDATE instead of VERSION; a new brief not at 1; a change checked without the prior brief | §6.4 |
| R22 | A workflow stage out of order: Ready for Design without a human G1 for this revision; **a G2 submission without a human G1 for this revision, on either path**; a G1 that records no path, or a path the brief no longer matches; text-only content sent to Design; text-only content listing assets; generation without a human spend approval for this revision; G2 submission before the finished artifact (design) or the final copy (text-only); C06 submitting without context | §8 |
| R23 | A select value outside its recorded vocabulary (`Audience Role`, `Format`); an unknown format, which leaves the design or text-only path undecidable | §7.1 |
| R24 | Stage evidence without identity: a brief with no ID; a G1, storyboard, spend approval, claim review or asset provenance that names no brief or **another brief**; a G2 submission whose packet describes a page other than the write target, or whose target was not read back | §8.1 |
| R26 | Stored approval evidence that does not match a fresh computation: a G2 Submitted Fingerprint or Packet Manifest that differs from the gate's recomputation (copy, assets or resolved context changed); a manifest not in canonical form; evidence typed instead of computed; a packet whose copy or translation context differs from the page | §8.2 |
| R27 | Context that cannot be trusted as fresh: no read-back; a part not read completely; read in another session, with no time zone, or outside the 30-minute window; a partial read; a non-canonical page ID; not exactly one linked translation; a linked offer not read. **Stored evidence is never reused in its place** | §8.2 |
| R28 | A G1 or G2 decision recorded by anyone not on the approver list (owner only, initially). A typed-name comparison, not authentication | §8.2 |
| R25 | An invalid asset: an ID that is blank, too short, contains whitespace or is a URL (a temporary vendor link is never an asset reference, §9.3); a version that is missing or not a whole number of 1 or more; the same asset listed twice | §8.1 |

---

## 6. Mutation modes, change history, verification

### 6.1 Modes

Reused verbatim from Sector: `CREATE` · `UPDATE` · `VERSION` · `SUPERSEDE` · `NO_OP` · `REJECT` · `ESCALATE`. Select exactly one, explicitly. Match on the natural key before any CREATE. A retried skill never creates a second record.

**The lookup must be verified (R10).** Before a CREATE, the skill queries or fetches the database for the natural key. It hands the gate the outcome as `{status, checked_at, records}`. Only `status: complete` with a records list counts. A failed, partial, quota-exhausted or unknown lookup refuses the CREATE. **It never means the database is empty.**

| DB | Natural key |
|---|---|
| DB1 | `Platform` |
| DB2 | `Position ID` (a new version gets a new ID, e.g. `-v2`) |
| DB3 | `Overlay ID` |
| DB4 | `Campaign Code` |
| DB5 | `Opportunity ID` |
| DB6 | `Translation Family ID` + `Platform` + **`Audience Role`** + `Surface` + `Format` |
| DB7 | `Translation` (one live brief per translation; a new revision is a VERSION, which bumps `Version`) |

**DB6 identity carries the audience (restored 2026-10-09).** The schema's primary entity is one *(Narrative × Platform × Audience)* expression (`CONTENT_INTELLIGENCE_SCHEMA.md` DB 6). v0.1 dropped the audience from the key, so a General Manager variant and a Revenue Manager variant of one family collided as duplicates. The key uses the **existing** DB6 `Audience Role` field. Its options mirror Sector DB9 Audience Roles verbatim; DB5 `Audience` is the relation to DB9 itself. No second audience store exists or is created.

### 6.2 The change-history rule

On any UPDATE that replaces a value, and on every VERSION and SUPERSEDE, append a dated line to the page body: what changed, the prior value, why, the source, and what it invalidates. Never silently overwrite. Example (applied 2026-10-09): *"`Audience Role` `CEO` → `General Manager / Owner`. Reason… Source: Sector DB 9 role page… Prior value preserved here."*

### 6.3 Read-after-write

After every apply, read the record back (fetch the page, or query the field) and compare it with the proposal. A write the connector reports as successful but that does not read back is a **partial failure**. Record it as one; do not retry blind.

**A failed query is never zero results.** When the Notion query quota is exhausted or the connector errors, the operation is `incomplete`, and the record says so. Fall back to fetching pages by ID where possible.

### 6.4 Revisions

`Version` on DB7 is the revision, and every gate binds to it.
- **Valid values.** A whole number of 1 or more. Notion returns it as a float (`2.0`), and the gate accepts integral values only. Empty, 0, negative, fractional, boolean or text is not a revision (R20).
- **A new brief starts at 1.**
- **What counts as a change.** The **publication-affecting** fields are marked in `content-databases.json`: `Script`, `Caption`, `Visual Direction`, `Canva Instructions`, `Platform`, `Engagement Follow-up`, `Evidence`, `Translation` and `Offer`. `Title` is an internal name and is not one.
- **How a change is applied.** A change to any of those fields is a **VERSION** that sets `Version` to exactly prior + 1. The skill must hand the gate the prior brief so it can compare (R21).
- **No change, no bump.** A bump with no such change is refused, because it would silently stale an approval.
- **What binds to a revision.** A G1 pass, a spend approval, a storyboard, a G2 submission, a finished artifact and a G2 approval each name one revision. A different current `Version` makes them stale (R12).
- **What this does not cover.** These rules hold only for writes that pass through a skill. §0.2 says what they cannot see.

---

## 7. Four state axes, never merged

| Axis | Field | Who moves it |
|---|---|---|
| Knowledge maturity | `Status` (Draft → Validating → Active → Superseded → Archived) on DB1–DB6, DB8 | The DB's writer skill; `Active` on DB2 needs an owner decision |
| Production trigger | DB7 `Publishing Status` (Not started → In progress → **Ready for Design** → Done) | C04 for the first two; **a human** for Ready for Design and Done |
| G2 decision | DB7 `G2 Decision` + `G2 Reviewer` + `G2 Decided At` + `G2 Approved Revision` | C06 may set Not submitted / Submitted for review; **a human** sets the decision, reviewer, date and revision |
| Packet lifecycle | DB7 `Packet State` | Reserved for Presence (21) |

A value on one axis never implies a value on another. DB7 `Approval Integrity` (formula) shows a red cell when the packet lifecycle runs ahead of G2, or when an approval names a revision other than the current `Version`.

**Trigger-read properties are frozen** (R17): `Title`, `Script`, `Caption`, `Visual Direction`, `Canva Instructions` (text/title) and `Publishing Status` (select: `Not started`, `In progress`, `Ready for Design`, `Done`, in that order). Routine `trig_01WyyrXEkFZck1D49tm6BfKv` reads them by name. Their option IDs are recorded in `content-databases.json` (`trigger_contract.publishing_status_option_ids`).

### 7.1 One vocabulary, Notion names authoritative

`content-databases.json` → `vocabularies` holds the live option names and option IDs for DB6 `Surface`, `Audience Role` and `Format`, and the DRAGON statuses. They were read by a read-only fetch on 2026-10-09, in the correction unit. Agents emit snake_case enums; the vocabulary maps each one to its Notion name. **That mapping lives there and nowhere else.**

| Notion option (exact) | Option ID | Agent enum | Platform | Voice | Post URL host |
|---|---|---|---|---|---|
| `LinkedIn - Founder profile` | `016f7eea-b42e-4485-8b26-120eebbd5e24` | `linkedin_founder_profile` | LinkedIn only | First person allowed, substantiated | `linkedin.com` |
| `LinkedIn - Company Page` | `18754c3f-6008-4447-a13e-022a11119d2e` | `linkedin_company_page` | LinkedIn only | **Institutional: no first person singular** (R15) | `linkedin.com` |
| `Single-identity channel` | `e06665b3-559b-497c-8c52-918b9ccf7443` | `single_identity_channel` | Not LinkedIn | The channel's one identity | (none recorded) |
| `Not yet assigned` | `7ceba672-abc1-44eb-b4ec-8db1eda6b23d` | `not_yet_assigned` | Any | Drafting only; never Ready for Design, G2 or publication | — |

Agent-only values that have **no Notion option** and never pass: `not_applicable` (multiplication engine: a derivative that is not a published translation) and `unknown` (publishing gate).

**Rules.**
- A Notion write carries the exact Notion name. Notion would silently create a new option from an agent enum.
- Matching is exact, with no case-folding and no dash normalisation. `Company Page`, `Founder profile` and `LinkedIn — Company Page` (em dash) are **unknown**, and unknown fails closed (R09_SURFACE_UNKNOWN, R23).
- Options are never renamed.
- The tests pin the IDs, so a contract edit that drifts from Notion fails.

*Correction:* the 2026-10-09 decision logs (`CONTENT_OS.md` §8, `CONTENT_INTELLIGENCE_SCHEMA.md` §10) wrote the surface options as "Founder profile · Company Page". The live names carry the `LinkedIn - ` prefix. The gate always used the live names; the agents used enums with no recorded mapping.

---

## 8. The workflow: G1, spend approval, G2 (corrected 2026-10-09)

**Design work** (any format that needs Design, or text-capable formats with visual direction):

```
Strategic DRAGON (DB5) → Editorial DRAGON (DB6) → brief copy at Version N (DB7)
  → G1: concept review + readiness on Version N            (human)        R22, R12
  → human sets Publishing Status = Ready for Design
  → Creative Pipeline routine: storyboard + plan for N      (planning only)
  → spend approval for Version N, before any generation    (human)        R22, R12
  → Design produces the finished artifact (asset IDs + versions, made for N)
  → G2: the exact finished artifact = copy at N + that asset set   (human)  R11, R12, R22
  → human publishes; the publication record reproduces revision N and the asset set   R12, R14
```

**Text-only work.** It needs all four of these:
- a text-capable format (`Text post`, `Article / Long-form`, `Poll`, `Thread`, `Newsletter issue`);
- `Visual Direction` and `Canva Instructions` that are empty or read `text-only`;
- no assets;
- a human G1 that records `path: text_only`.

**A text-capable format is not automatically asset-free.** An article with a header image or a newsletter with a chart is design work.

```
Strategic DRAGON → Editorial DRAGON → final copy at Version N
  → G1: concept review on Version N, path text_only        (human)        R22, R12, R24
  → G2: the exact final copy at Version N                  (human)        R11, R12, R22
  → human publishes
```

Text-only work skips Design and spend approval. **It never skips G1** (owner direction, hardening brief, 2026-10-09: "Require human G1 and G2 for every public content item. Genuinely text-only work skips Design and generation-spend approval, not G1."). The gate refuses:
- a text-only brief as Ready for Design (R22);
- a G2 submission without G1 on either path (R22);
- a G1 whose path no longer matches the brief (R22);
- an unknown format (R23), rather than guessing.

*Was (v0.2, earlier the same day):* the text-only path ran from final copy straight to G2, with no G1. That was **the assistant's reading** of the correction brief's line "Text-only content may reach G2 once its final copy exists". The handover flagged it for owner confirmation. **It was never an owner decision**, and it is superseded.

| | G1 Concept review + readiness | Spend approval | G2 Pre-publish approval |
|---|---|---|---|
| Question | Should this exist, and is it ready to produce? | May credits be spent on this revision? | Is this exact finished artifact safe and right to publish? |
| Object | One brief at one `Version`, on **both** paths: before Design (design), before G2 (text-only) | One brief at one `Version`, after the storyboard (design only) | Copy at one `Version` + the finished asset set (design), or the final copy (text-only) |
| Checked by | `validate_design_readiness` (`content_write_gate.py readiness`, design) and `validate_g2_submission` (`content_write_gate.py submission`, both paths) | `validate_generation_start` | `validate_g2_submission`, then `validate_publication` |
| Who decides | A named human | A named human (Design 19's gate; approval matrix: human gate before credit spend) | `content-publishing-gate` (advisory) → **a named human**, Class 3 |
| Recorded | **DB7 properties (since 2026-10-10):** `G1 Decision` (`Passed (design)` / `Passed (text-only)` / `Returned`), `G1 Reviewer`, `G1 Decided At`, `G1 Revision`. Human-only; owner only, initially. *(Until 2026-10-10: a dated page-body line, `G1 passed \| brief <page id> \| rev N \| path … \| <reviewer> \| <date>`.)* | Owned by Design (19). Content checks only that it exists for the same brief ID and Version | DB7 `G2 Decision` = Approved + Reviewer + Decided At + Approved Revision, with `G2 Packet Manifest` and `G2 Submitted Fingerprint` written by C06 at submission (§8.2) |
| Expires | Yes, on any publication-affecting change | Yes, likewise | **Yes.** Any copy change bumps `Version`, and the approval no longer covers it |

Passing G1 never implies G2. A G2 approval never covers a later revision or a different asset. **No agent and no skill can approve, pass G1 or approve spend** (R01, R11, R22).

*Was (v0.1, 2026-10-09):* G1 was the concept decision on the opportunity (DB5 `Decision`). The skill matrix put **G2 before Ready for Design**, so approval would have bound a brief whose artifact did not yet exist. DB5 `Decision = Promoted to Brief` remains the owner's concept decision on the opportunity. G1 is now the brief-level review before Design.

**Not built, by design of this unit:** G1 and approved-artifact properties on DB7 (a Notion schema change, outside this unit), and any automatic G1 check in the routine (it cannot read a page-body convention reliably). Until they exist, the T2a checkpoint in the Creative Pipeline proposal is the human step that holds G1. *(Hardening unit: the minimal storage is now proposed in [`APPROVAL_EVIDENCE_STORAGE_PROPOSAL.md`](APPROVAL_EVIDENCE_STORAGE_PROPOSAL.md); still not built.)*

### 8.1 Evidence identity (hardening unit, 2026-10-09)

Every record a stage relies on names **the brief and the revision it covers**. The gate compares both with the brief under check:

| Evidence | Must carry | Refused when |
|---|---|---|
| G1 | `brief_id`, `revision`, `path` (`design` / `text_only`), `by: human:…`, `at`, `decision: passed`. Since 2026-10-10 this record is built from the G1 properties by `g1_from_properties`; the page it was read from is the binding | missing; agent-made; undated; another brief (R24); another revision (R12); invalid revision (R20); no path, or a path the brief no longer matches (R22) |
| Storyboard | `brief_id`, `revision`. The routine's COMPLETED marker `[… \| brief=<id> \| rev=<N>]` is this record | missing (R22); another brief (R24); stale (R12); invalid (R20) |
| Spend approval | `brief_id`, `revision`, `by: human:…`, `at`, `scope` | as G1, and no scope (R22) |
| Claim review (C05) | `brief_id`, `revision`, `verdict: pass` | missing or not `pass` (R22); another brief (R24); stale (R12) |
| Asset | `asset_id` (registry token, never a URL), `version` (whole number ≥ 1), `rights`, `provenance: {brief_id, brief_revision}` | invalid ID or version, or listed twice (R25); provenance missing or for another brief (R24); made for another revision (R12); rights unknown (R22) |
| G2 packet (C06 write) | Three page IDs, each a valid token and **exactly equal**: `proposal.target` (the page written), `state.prior.id` (the page read back) and `g2_submission.brief.id` (the page the packet describes). The read-back must also show the packet's Version | any of the three missing, empty, whitespace-only, padded, non-string or different, including a dashed and an undashed form of one page (R24) *(tightened 2026-10-10)*; target moved on (R12); target Version invalid (R20) |
| Publication | brief ID; approved and published asset sets equal, each asset valid | as above, plus R11, R12, R14 |

### 8.2 Stored approval evidence (storage unit, 2026-10-10)

**At submission.**
- C06 hands the gate a **fresh read-back** of the exact target brief: the brief page, its one linked translation and every linked offer.
- The read must be complete, from one session, and no more than 30 minutes before the check. Page IDs must be canonical Notion IDs.
- The gate computes the **G2 Packet Manifest** (canonical JSON, `content-g2-manifest/1`) and the **G2 Submitted Fingerprint** (`sha256:` of copy, assets and resolved context). It also checks that the packet's copy and translation context equal that read.
- C06 writes **exactly those two strings** with `Submitted for review`. Typed values, values from another page, or a fresh read of another page are refused (R26, R24).

**What the resolved context holds:** `translation_id`, `surface`, `audience_role`, `format`, `platform_ids` and `offers[{offer_id, offer_status}]`. Values are exact Notion option names; `null` means read-and-empty. Anything unreadable or unknown computes nothing (R27, R09, R23).

**At publication.**
- The gate recomputes the fingerprint from a fresh read plus the assets actually published, and compares it with the stored one.
- The approved surface, format and asset set come from the stored manifest, never from the current page.
- Any difference is R26, naming the component that moved, for example `resolved.surface: 'LinkedIn - Founder profile' -> 'LinkedIn - Company Page'`.

**Changes need Version +1 and renewed G1 and G2:**

| Change | How it is recorded | What the gate refuses |
|---|---|---|
| **Copy** | A VERSION (§6.4) | — |
| **Context only** (translation surface, audience, format or platform; offer status) | A VERSION with `reason: context_change` and only `Version` written. **No copy edit is invented.** The gate verifies the change against the stored manifest; before any submission, a declared `context_before` serves instead (unverifiable, so stated as such) | No change, an unreadable context, or a bump other than +1 (R21, R27) |
| **Assets only** | A VERSION with `reason: asset_change`, checked against the stored manifest's asset set | Same as above |
| **Any of these at the same Version since the last submission** | — | Re-submission (R21) |

After any bump, the G1 and G2 records bind to the old Version and must be renewed by the owner.

**Owner only, initially.** G1 and G2 reviewers must be on `approvers` in `content-databases.json` (R28). This is a name comparison.

**Provisional asset-ID format.** Design (19)'s Asset Registry is not built (§9.2), so no canonical asset-ID format exists. Until Design ratifies one, the gate accepts a 3–128 character token of letters, digits and `. _ : -`. That rules out URLs, whitespace and blanks. It is a placeholder, not Design's decision.

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
| Content → Design | **Human** records G1, then sets `Ready for Design` | DB7 brief ID + Version → routine storyboard comment | `content_write_gate.py readiness` passes on a live snapshot: both DRAGON passes, surface assigned, valid Version, upstream links, a design (not text-only) brief, G1 for this Version | The G1 properties on the brief (a page-body line until 2026-10-10); the routine's comment carrying `[creative-pipeline v2 \| completed \| …]` |
| Design → generation | **Human** spend approval | Brief ID + Version + storyboard → generation jobs | `validate_generation_start` passes | Design (19)'s spend record |
| Content → G1 (text-only) | **Human** reviewer | Brief ID + Version + final copy → `G1 Decision = Passed (text-only)` with reviewer, date and `G1 Revision` | Both DRAGON passes, surface assigned, valid Version; the copy is final | The G1 properties on the brief (a page-body line until 2026-10-10) |
| Content → G2 | Human invoking C06, then the reviewer | Brief ID + Version + G1 + C05 verdict + finished asset set (design) or final copy (text-only) → `G2 Decision` | `validate_g2_submission` (`content_write_gate.py submission`) passes, with every record bound to this brief and Version; reviewer, date and approved revision recorded by the human | DB7 G2 fields + the G2 packet's asset list + Approval Integrity green |
| G2 → publication | **Human publisher** | Approved brief ID + Version + asset set → native post | R11–R14 pass | Publication record (brief ID, revision, asset set, surface, native URL, date, publisher) in the Presence publication log (not yet built) |
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

- **v0.4 (2026-10-10, owner-authorised storage unit)** — Changes:
  - **Notion:** six DB7 properties and the Approval Integrity extension. Recorded in `CONTENT_INTELLIGENCE_SCHEMA.md` §10.
  - **G1 storage:** G1 now lives in properties.
  - **Stored evidence and refusals:** the G2 manifest and fingerprint are computed by the gate from a fresh read (§8.2). R26, R27 and R28 added.
  - **Versioning:** context-only and asset-only VERSIONs.
  - **Approvers:** owner only.
  - **Limits:** stated in §0.2.
  - **Unchanged:** triggers, emits, risk classes, department ownership and canonical option names. — Claude Code (Opus 5.5)
- **v0.3.1 (2026-10-10, owner-authorised follow-up unit)** — Repository only.
  - **Reproduced against `9124997`.** A read-back (`state.prior`) with a Version but no page ID, an empty ID or a `None` ID let `Submitted for review` through.
  - **Fixed.** `proposal.target`, `state.prior.id` and `g2_submission.brief.id` must each be a valid page ID and exactly equal (§8.1, R24). The revision checks are unchanged. The brief-ID check at every stage uses the same page-ID rule.
  - **Recorded.** The linked-page limitation is now in §0.2, and the storage proposal specifies how the resolved Surface, Audience Role and Format would be captured and compared (not built).
  - **Unchanged.** G1 and G2 on both paths, two-pass DRAGON, option names, ownership, triggers, emits and risk classes. — Claude Code (Opus 5.5)
- **v0.3 (2026-10-09, owner-authorised hardening unit)** — Repository only. No Notion write and no activation.
  - **The remaining failures were reproduced against `ce310c6`'s gate.** G1, storyboard, spend, claim-review and asset evidence for another brief were accepted at a matching revision. A G2 packet for one brief was accepted as a write on another. Assets missing a version, or an ID, on both sides passed publication. A temporary vendor URL passed as an asset ID. Text-only G2 passed with no G1.
  - **What changed.** Evidence is bound to brief ID + Version (§8.1, R24). Asset rules added (R25). **G1 is required on both paths** (owner direction, quoted in §8; the v0.2 text-only reading is marked as the assistant's, superseded). "Text-capable is not asset-free" is made explicit. A `submission` command was added to the gate. The storage and fingerprint proposal is prepared, not applied.
  - **Unchanged.** Triggers, emits, risk classes, field ownership and Notion option names. — Claude Code (Opus 5.5)
- **v0.2 (2026-10-09, owner-authorised correction unit)** — Seven review findings on `74feb86` corrected in the repository. No Notion write; only read-only schema fetches.
  - **Vocabulary.** One explicit surface, audience and format vocabulary with the live option IDs (§7.1). Unknown values fail closed.
  - **Revisions.** Positive revisions enforced; publication-affecting changes must bump `Version` exactly once; stale and missing revisions refused (§6.4, R20, R21).
  - **Workflow.** G1 and readiness before Design, human spend approval before generation, G2 on the exact finished artifact, and the text-only path (§8, R22).
  - **Lookups.** Only a verified duplicate lookup counts (§6.1).
  - **Audience.** Audience restored to DB6 identity.
  - **Limits.** What the gate cannot see is stated in §0.2.
  - Each finding has regression tests, and each was re-run against `74feb86`'s gate to confirm the defect existed. — Claude Code (Opus 5.5)
- **v0.1 (2026-10-09)** — Created under the owner's Content-unit authorisation. Modelled on Sector's v0.2 contract. Adds what Sector's lacks: a runnable gate that refuses write proposals. Owner direction recorded: two-pass DRAGON (§4). Notion changes applied the same day are in `CONTENT_OS.md` §8. — Claude Code (Opus 5.5)
