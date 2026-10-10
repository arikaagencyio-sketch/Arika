# Content — Skill Matrix

**Department:** Content (04) · **Version:** v0.3.1 (2026-10-10, follow-up unit) · **Status:** Seven skills authored. **None has run.** Contract: [`CONTENT_WRITE_CONTRACT.md`](CONTENT_WRITE_CONTRACT.md). Field ownership: [`contracts/content-databases.json`](contracts/content-databases.json). Gate: `python 04_Content/contracts/content_write_gate.py`.

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
| C03 | [`content-surface-translation`](../.claude/skills/content-surface-translation/SKILL.md) | Opportunity + Position IDs | DB6 (+ Surface, Audience Role, Editorial DRAGON), DB3, DB1 behaviour | R03 R05 R06 R07 R08 R09 R10 R23 | family + platform + **audience role** + surface + format · `Overlay ID` | C04 |
| C04 | [`content-brief-writer`](../.claude/skills/content-brief-writer/SKILL.md) | Translation ID | DB7 authored fields, `Version` | R01 R03 R04 R06 R09 R10 R15 R16 R17 R18 R20 R21 | `Translation` (one live brief; revise = VERSION, exactly +1) | C05; text-only → C06; design → human G1 |
| C05 | [`content-claim-review`](../.claude/skills/content-claim-review/SKILL.md) | Brief ID + Version | nothing (verdict names brief ID + revision) | R04 R05 R16 | n/a (read-only) | human G1, then C06; or back to C04 |
| C06 | [`content-approval-prep`](../.claude/skills/content-approval-prep/SKILL.md) | Brief ID (= write target = read-back ID, exactly) + Version + G1 + C05 verdict + finished asset set (design) or final copy (text-only), each bound to that brief and Version | DB7 `G2 Decision` (Not submitted / Submitted for review) | R01 R09 R12 R18 R20 R22 R24 R25 | Brief ID + Version | **human reviewer** |
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
   C04 brief-writer ──(Version N)──► DB7
        │
   C05 claim-review (read-only verdict on brief + N)
        │
   HUMAN: G1 concept review on brief + N, recording the path (both paths)
        │
        ├── path text_only ─────────────────────────────────────────┐
        │                                                           │
   path design: readiness (gate: readiness)                         │
        │                                                           │
   HUMAN: Ready for Design ──► Design (19) routine: storyboard for N │
        │                                                           │
   HUMAN: spend approval for brief + N ──► Design generates the artifact (provenance: brief + N)
        │                                                           │
   C06 approval-prep ──(Submitted for review: N + G1 + asset set)──► DB7 ◄┘ (text-only: N + G1 + final copy)
        │                                    (gate: submission; the packet must describe the page written)
   HUMAN: G2 on the exact finished artifact ──► HUMAN: manual publication + link-back record (Presence 21)

C07 source-retrieval is called by any step.
```

*Hardening unit (2026-10-09):* the v0.2 graph sent text-only content from C05 straight to C06 with no G1. That was the assistant's reading, never an owner decision. The owner's hardening brief requires G1 and G2 for every public item.

The order is the two-pass DRAGON order: nothing at C03 or below may proceed while C01's Strategic pass is `Not yet run`. **Corrected 2026-10-09:** v0.1 drew G2 *before* Ready for Design, so an approval would have bound a brief whose artifact did not yet exist. Rules: `CONTENT_WRITE_CONTRACT.md` §8.

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

`python -m unittest discover -s 04_Content/contracts -p "test_*.py"` covers:
- **Contract integrity.**
- **The owner's ten scenarios:** founder content from a verified source, Page framework content, a Hospitality brief, missing evidence, partial / not-applicable DRAGON, a G2 failure, a missing-approval refusal, duplicate handling, Postiz unavailable, and manual publication link-back.
- **One regression class per correction finding** (2026-10-09):
  - `SurfaceVocabulary`
  - `RevisionIntegrity`
  - `WorkflowOrder`
  - `DuplicateLookupState`
  - `ProductionMemoryUntouched`
- **Hardening unit regression classes** (2026-10-09). Each covers missing, wrong-brief, stale, invalid and valid evidence:
  - `EvidenceBinding`
  - `AssetValidity`
  - `SubmissionTarget`
  - `G1OnBothPaths`

All fixture data is synthetic (`fx-`). The tests touch no Notion record. A module-level check fails the run if `04_Content/_memory` changes.

The proposed routine's decision table has its own suite: `python -m unittest discover -s 16_Automation/routines/creative-pipeline -p "test_*.py"`.

## 6. Changelog

- **v0.3.1 (2026-10-10, follow-up unit)** — C06's input names the exact ID triple. The `SubmissionIdentityTriple` test class is added. No skill or ownership change. — Claude Code (Opus 5.5)
- **v0.3 (2026-10-09, hardening unit)** — Changes:
  - G1 is drawn on both paths.
  - C05 and C06 inputs are bound to brief ID + Version.
  - C06 gains R24 and R25.
  - Hardening test classes are listed.
  - No skill was added; no ownership changed. — Claude Code (Opus 5.5)
- **v0.2 (2026-10-09, correction unit)** — Changes:
  - C03's idempotency key regains `Audience Role`.
  - Refusal codes R09, R12 and R20–R23 are added to the skills that can trigger them.
  - The dependency graph is corrected: G1 and spend approval come before Design work, and G2 comes on the finished artifact. There is also a text-only path.
  - Test inventory updated. — Claude Code (Opus 5.5)
- **v0.1 (2026-10-09)** — Created with the seven skills and the gate. — Claude Code (Opus 5.5)
