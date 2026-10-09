---
name: content-source-retrieval
description: Skill C07 of Content (04). Read-only, ID-based retrieval of the sources and assets a piece of content depends on — Sector findings, narrative positions, offers, and Design-owned assets — returning a reference with owner, URI or folder ID, version, provenance, rights, licence, permitted use, media type and approval state. Use whenever a skill or agent needs a source or asset. Never stores a master file, never treats a temporary vendor URL as storage.
---

# C07 · Content Source Retrieval

**Read [`04_Content/CONTENT_WRITE_CONTRACT.md`](../../../04_Content/CONTENT_WRITE_CONTRACT.md) §9 first.**

> **The one rule that defines this skill: retrieve by canonical ID from the owner's store, or report that it cannot be found.** No search-by-title guess becomes a citation.

## What it returns

For each requested ID: `{id, owner, uri, scope, version, provenance, rights, licence, permitted_use, media_type, approval_state, retrieved_at}`. Any field the owner's store does not hold is returned as `unknown`, never filled.

## Where it looks

| ID kind | Owner store |
|---|---|
| Sector finding / signal / audience role | Sector (01) Notion data sources |
| Narrative position, opportunity, translation, brief | Content (04) DB2, DB5, DB6, DB7 |
| Offer | DB8 (mirror of Offer 02) |
| Asset, storyboard, generation prompt | **Design (19) Asset Registry — not built yet.** Return `asset_registry: not built` |
| Canva design or folder | Canva (Design 19). Connector currently unauthorised: return `blocked` |
| Pilot file | Google My Drive, limited public-only test mode. Never private or client data |

## Refusals

A temporary or signed vendor URL offered as an asset's location · an asset with `rights: unknown` requested for public output · a pilot private-data request · a lookup by title when no ID is given.

## Failure handling

A connector error or an exhausted query quota returns `incomplete` with the error. It never returns an empty result as if the source did not exist.
