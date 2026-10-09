---
name: content-brief-writer
description: Skill C04 of Content (04). Writes the authored fields of one Content Brief v2 (DB7) — copywriting, long-form, scripts and carousel frames — from a translation that already exists, and bumps Version on every copy change so a G2 approval always binds to one exact revision. Use after C03. Recommends readiness but never sets Ready for Design; preserves the six trigger-read property names exactly.
---

# C04 · Content Brief Writer

You are performing the **apply** step of Content's write layer.

**Read [`04_Content/CONTENT_WRITE_CONTRACT.md`](../../../04_Content/CONTENT_WRITE_CONTRACT.md) first** (§7 state axes and trigger properties, §8 G1/G2). Field truth: DB7 in [`content-databases.json`](../../../04_Content/contracts/content-databases.json).

> **The one rule that defines this skill: the brief is never the starting point, and `Ready for Design` is never yours to set.** Every brief hangs off an Opportunity, a Translation and a Narrative Position, and a human flips the trigger.

## Step 0 · The write path

| | Data source |
|---|---|
| DB7 Content Briefs v2 *(write)* | `collection://761b3f94-bdbf-4b3d-8234-4cda579697ca` |
| DB5 / DB6 / DB2 / DB3 / DB4 *(read)* | contract §3 |
| DB8 Offer *(read only, optional)* | `collection://850f5a23-6533-4f48-89f3-ef6bc7f360b6` |

## Copy modes (all write the same fields)

| Mode | `Caption` | `Script` | `Visual Direction` / `Canva Instructions` |
|---|---|---|---|
| Text post | The post | Optional comment-starter | Usually empty: say "text-only" |
| Carousel | Post copy | One line per frame (`S1:` …) | Frame layout, sizes, data treatment |
| Long-form / article | Standfirst | The full body | Header image only, if any |
| Video / script | Caption | Scene-by-scene script | Shot and asset needs (Design storyboards it) |
| Newsletter issue | Subject line | The issue body | Optional single graphic |

Rollups (`Problem`, `Pillar`, `Content House`, `Persona`, `Story/Hook/Narrative`, `Core Message`, `Proof`, `Funnel Stage`) are inherited. **Never type them; change the upstream record.**

## Permitted writes

DB7 fields whose writer is `C04`: the six trigger-read properties, `Objective`, `Desire`, `Objection`, `Engagement Follow-up`, `Evidence`, provenance block, `Version`, `Platform`, the forward relations, `Supersedes`. `Publishing Status` only `Not started` or `In progress`.

## Refusals

R01 `Ready for Design` or `Done` · R03 missing Opportunity, Translation or Narrative Position · R04 any fact without a dated source; any client outcome · R05 T4-only facts · R06 the translation's family not among the brief's positions · R10 a second brief for the same translation (revise with VERSION instead) · R15 first person on a Company Page brief · R16 any price, package or commercial term without an `Active` Offer row · R17 renaming or retyping a trigger-read property · R18 `Packet State` / `packet_id` / `variant_id`.

## Procedure

1. Read the translation: family, surface, both DRAGON passes, audience role.
2. Write the copy so every claim is either a sourced fact, a labelled opinion, or a framework. List claims in `Evidence` with their source and date. If the Offer relation is empty, the copy names no price and no package.
3. Match the natural key (`Translation`). Existing brief → **VERSION**: change the copy, bump `Version` by 1, append a change line. A G2 approval on the old Version no longer covers it.
4. Run `validate_write`. Recommend readiness only when it passes **with** `recommend_ready_for_design: true`, and state the recommendation in the page body for the human.

## Verification

Read back the six trigger properties byte-for-byte and the `Version`. `Brief Integrity` and `Approval Integrity` are formulas: check them in the Notion UI.

## Handoff

To C05 (claim review) then C06 (approval prep). To Design only through the human `Ready for Design` flip.

## Execution record

`04_Content/_memory/skill_runs.jsonl`, `skill: content-brief-writer`.
