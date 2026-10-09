# Content — Skill Matrix

**Department:** Content (04) · **Version:** v0.1 (2026-10-09) · **Status:** Seven skills authored. **None has run.** Contract: [`CONTENT_WRITE_CONTRACT.md`](CONTENT_WRITE_CONTRACT.md). Field ownership: [`contracts/content-databases.json`](contracts/content-databases.json). Gate: `python 04_Content/contracts/content_write_gate.py`.

Modelled on [`01_Sector/SECTOR_SKILL_MATRIX.md`](../01_Sector/SECTOR_SKILL_MATRIX.md). **Agents decide; skills validate and apply.** Skills are grouped by write boundary, so seven skills cover eight capabilities: copywriting, long-form, scripts and carousels are one boundary (DB7 authored fields).

---

## 1. Ownership: skill → database → fields

| Skill | DB1 | DB2 | DB3 | DB4 | DB5 | DB6 | DB7 | DB8 |
|---|---|---|---|---|---|---|---|---|
| C01 opportunity-intake | | | | **writes** | **writes** | | | |
| C02 narrative-review | | **writes** | | | | | | |
| C03 surface-translation | **behaviour fields** | | **writes** | | | **writes** | | |
| C04 brief-writer | | | | | | | **authored fields** | read |
| C05 claim-review | read | read | read | read | read | read | read | read |
| C06 approval-prep | | | | | | | **G2 Decision (2 values)** | |
| C07 source-retrieval | read | read | read | read | read | read | read | read |

The JSON twin holds the field-level assignment: **361 fields across 8 databases, each with exactly one writer** (a skill, a computation, the reverse side of a relation, a named human, or another department). The gate fails on any field with zero or two writers.

### 1.1 Where ownership crosses a boundary

| Field(s) | Owner | Why it is not Content's |
|---|---|---|
| DB1 `Account Status` | Presence (21) | Account truth is the onboarding tracker |
| DB1 `Launch Priority`, DB4 `Revenue Target`, DB7 `Target Publish Date` | Owner (human only) | Owner decisions and money |
| DB4 `Design Folder` | Design (19) | Design creates and records its own folders |
| DB6 `Approved By`, DB7 `G2 Reviewer` / `G2 Decided At` / `G2 Approved Revision` | Human only | Approval is never delegated |
| DB7 `Packet State`, `packet_id`, `variant_id` | Presence (21) | L3 Reservoir packet machine |
| DB8 (all fields) | Offer (02) | Content never owns an offer or a price |

---

## 2. The seven skills

| ID | Skill | Inputs | Writes | Key refusals | Idempotency key | Hands off to |
|---|---|---|---|---|---|---|
| C01 | [`content-opportunity-intake`](../.claude/skills/content-opportunity-intake/SKILL.md) | Mapper recommendation, Sector finding ID | DB5 (+ Strategic DRAGON), DB4 | R03 R04 R05 R07 R10 R16 R19 | `Opportunity ID` · `Campaign Code` | C02 → C03 |
| C02 | [`content-narrative-review`](../.claude/skills/content-narrative-review/SKILL.md) | Opportunity / translation / brief ID | DB2 only | R08 R10 R19 | `Position ID` (new version = new ID) | C03 / C04 |
| C03 | [`content-surface-translation`](../.claude/skills/content-surface-translation/SKILL.md) | Opportunity + Position IDs | DB6 (+ Surface, Editorial DRAGON), DB3, DB1 behaviour | R03 R05 R06 R07 R08 R09 R10 | family + platform + surface + format · `Overlay ID` | C04 |
| C04 | [`content-brief-writer`](../.claude/skills/content-brief-writer/SKILL.md) | Translation ID | DB7 authored fields, `Version` | R01 R03 R04 R06 R10 R15 R16 R17 R18 | `Translation` (one live brief; revise = VERSION) | C05 → C06; human → Design |
| C05 | [`content-claim-review`](../.claude/skills/content-claim-review/SKILL.md) | Brief ID + Version | nothing | R04 R05 R16 | n/a (read-only) | C06 or back to C04 |
| C06 | [`content-approval-prep`](../.claude/skills/content-approval-prep/SKILL.md) | Brief ID + Version + C05 verdict | DB7 `G2 Decision` (Not submitted / Submitted for review) | R01 R18 | Brief ID + Version | **human reviewer** |
| C07 | [`content-source-retrieval`](../.claude/skills/content-source-retrieval/SKILL.md) | Any canonical ID | nothing | temp URLs, `rights: unknown`, private pilot data | n/a | caller |

---

## 3. Dependency graph

```
Sector finding / narrative position
        │
   C01 opportunity-intake ──(Strategic DRAGON)──► DB5
        │
   C02 narrative-review (verdict; DB2 only when a position changes)
        │
   C03 surface-translation ──(Editorial DRAGON, Surface)──► DB6 (+DB3, DB1)
        │
   C04 brief-writer ──(Version)──► DB7
        │
   C05 claim-review (read-only verdict)
        │
   C06 approval-prep ──(Submitted for review)──► DB7
        │
   HUMAN: G2 decision on this Version ──► HUMAN: Ready for Design ──► Design (19) routine
                                     └──► HUMAN: manual publication + link-back record (Presence 21)

C07 source-retrieval is called by any step.
```

The order is the two-pass DRAGON order: nothing at C03 or below may proceed while C01's Strategic pass is `Not yet run`.

---

## 4. Agent → skill mapping (agents decide, skills apply)

| Agent (`.claude/agents/`) | Produces | Applied by |
|---|---|---|
| `content-intelligence-hub` | Insights with source references | C01 (when one becomes an opportunity) |
| `content-opportunity-mapper` | Scored opportunity + `dragon.strategic` | C01 |
| `content-narrative-architect` | Verdict + `position_id` + two-pass order check | C02 |
| `content-multiplication-engine` | Translation plan per surface (+ `dragon.editorial` proposals) | C03, once per surface |
| `content-brief-builder` | V2 brief payload + readiness recommendation | C04 |
| `content-publishing-gate` | G2 advisory verdict on one Version | C06 packet → human |

No new agent was built. No event bus, scheduler or Notion runtime client was added (owner instruction, 2026-10-09).

---

## 5. Tests

`python -m unittest discover -s 04_Content/contracts -p "test_*.py"` covers contract integrity and the owner's ten scenarios: founder content from a verified source, Page framework content, a Hospitality brief, missing evidence, partial / not-applicable DRAGON, a G2 failure, a missing-approval refusal, duplicate handling, Postiz unavailable, and manual publication link-back. All fixture data is synthetic (`fx-`). The tests touch no Notion record and no `_memory` stream.

## 6. Changelog

- **v0.1 (2026-10-09)** — Created with the seven skills and the gate. — Claude Code (Opus 5.5)
