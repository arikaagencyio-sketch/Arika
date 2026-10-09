---
name: content-claim-review
description: Skill C05 of Content (04). Read-only claim and provenance review of one brief revision — classifies every claim (fact, statistic, outcome, pricing, opinion, hypothesis, framework, question), traces each fact to a dated, tiered source, and refuses invented clients, outcomes, proof, sector facts or performance. Use before content-approval-prep and before any G2 decision. Writes nothing; returns a verdict.
---

# C05 · Content Claim Review

**Read [`04_Content/CONTENT_WRITE_CONTRACT.md`](../../../04_Content/CONTENT_WRITE_CONTRACT.md) §5 first** (R04, R05, R16).

> **The one rule that defines this skill: a claim with no source is not softened. It is removed or reclassified.** "We've seen", "most companies", "I watch every week" are claims too.

## Inputs

One DB7 brief ID and its current `Version`. Read the brief, its translation, its opportunity (`Proof`, `Proof Status`, `Source Tier`) and every source it cites.

## Classification

| Kind | Needs |
|---|---|
| `fact` · `statistic` | A source with ID and `verified_at`, tier T1–T3. T4 alone is refused (R05) |
| `outcome` | `Proof Status = Proof exists` **and** a source. The agency has no client outcomes on record today |
| `pricing` · `offer_term` | An `Active` Offer (02) row. None is priced today |
| `opinion` · `hypothesis` · `framework` · `question` | Labelled as such in the copy, not dressed as fact |

**First-person experience claims** ("I watched", "the most common gap I find") are facts about the founder. They need a source in the agency's own record (a dated repo entry, a real event). Otherwise reclassify them as opinion or rewrite them.

**Time-relative words** ("last month", "this week") are checked against the source date and the earliest possible publish date. Prefer absolute dates.

## Output (writes nothing)

`{brief_id, version, verdict: pass | revise | reject, claims: [{text, kind, sources, issue}], unsupported: [...], stale_terms: [...]}`. Run `validate_write` with the claims list; a refusal code means `revise` or `reject`.

## Handoff

The verdict goes to C06. A `revise` returns to C04, which will bump `Version`.
