---
name: sector-source-registrar
description: Skill S03 of Sector (01). Registers an external publisher in DB 14 Signal Sources so a signal can be re-followed rather than re-Googled, and holds the registration gate — a source reaches `active` only after a live call proves it answers. Use when plugin slot P8 is authored, when a signal cites an unregistered source, at a verification cadence, or at activation Gate D.
---

# S03 · Sector Source Registrar

You are performing the **apply** step of Sector's write layer. An agent proposes what is true; this skill decides whether that truth may become a database state.

**Read [`01_Sector/SECTOR_WRITE_CONTRACT.md`](../../../01_Sector/SECTOR_WRITE_CONTRACT.md) before doing anything else.** Field-level truth is in [`01_Sector/contracts/sector-databases.json`](../../../01_Sector/contracts/sector-databases.json) — DB14. Your contract row is `SECTOR_SKILL_MATRIX.md` §2.

> **What this skill is actually for.** A signal with a source is re-followable; a signal with a remembered claim is not. **"A table that can hold sources is not a registry of sources."** Every other Sector skill inherits its authority from what you register here — so a careless `active` corrupts the tier of every record downstream of it.

---

## Step 0 · Establish the write path

| | Data source |
|---|---|
| DB14 Signal Sources | `collection://13741534-e31d-4ff8-bebf-dd50133e20af` |
| DB2 Sub-Sectors | `collection://dbe10a8b-5c67-4602-9108-12feb540995c` |
| DB11 Geography | `collection://e095c661-86cd-4f45-9149-eca1c7195e71` |

Agency-wide registry (this DB is its Sector-scoped mirror, not a rival): `00_Agency_Governance/enterprise_architecture/AEIT_08_SOURCE_REGISTRY_AND_INTELLIGENCE_CALENDAR.md` §3.2.

## Step 1 · Resolve context and read the candidate pack

Resolve the Sector Execution Context per write contract §2. Then read plugin slot **P8** — the sector's candidate source pack. **P8 supplies which publishers matter and why; this database holds the rows.** That split is deliberate: a second sector adds a pack, it does not edit the registry's reasoning.

If P8 is unauthored, record it in `plugin_slots_unavailable`. You may still register a source a live signal already cites — that is an independent trigger.

## Step 2 · The registration gate — the whole point of the skill

**`AEIT_08` §5: a source enters `State = active` ONLY after a live verification call proves it answers.** No source is registered on faith, including one the owner named, including one you are confident about.

Run the call **now**, in this session, and record what actually happened:

| Result | Write |
|---|---|
| The publisher's page/feed resolves and carries the content claimed | `active` · `Last Verified` = today |
| It resolves but does not carry what was expected | `candidate` · say so in `Notes` |
| It does not resolve, or you could not reach it | `candidate` · **never** `active` |
| It has moved | register the new one, `SUPERSEDE` the old — **both rows survive** |

**`Feed URL (ICS/API)` is filled ONLY if a feed genuinely exists.** Blank is the honest default and the common case. Most publishers have a calendar page and no ICS. Writing a plausible `/calendar.ics` is the exact fabrication this registry exists to prevent.

Note the distinction the field contract draws: **subscribing to an ICS URL is a follow; downloading the file is a snapshot.** Only the first survives a change at the publisher.

## Step 3 · Authority Level — the tier test is about the publisher, not the page

Whatever you set here, **every downstream record inherits and may never out-rank it.**

| | Means |
|---|---|
| **T1 Primary** | The body that owns the fact publishes it. The organiser's own site; the government gazette; the ministry's own circular. |
| **T2 Institutional** | An institution with standing but not ownership of this fact — an industry association, a national body reporting someone else's event. |
| **T3 Commercial-intel** | A commercial publisher: vendor blog, consultancy, trade press, aggregator. |
| **T4 Secondary** | Encyclopaedic or user-maintained. **May discover, may not confirm.** |

Three rules that decide most cases:

- **The organiser outranks every aggregator**, always, on their own event.
- **A government fact is T1 only from the government.** A newspaper reporting a gazette is T3 reporting a T1 fact — register the gazette, not the newspaper.
- **Reading a T1 publisher's page in this session makes the record T1**, because the tier describes the publisher. It does not become T3 because a browser was involved.

## Step 4 · Legal Posture — required, and a real gate

> **`HTML` means a human reads a published page. It is not a scrape — until you automate it.**
> Record `Legal Posture Note` saying so explicitly. The moment anyone configures automated extraction against an
> `HTML` source, its `Feed Type` becomes `scrape` and it goes to **Legal (10)** before it may stay `active`.
> The distinction is the whole reason `HTML` and `scrape` are separate options rather than one.

`Legal Posture` is **required on every row**: `Not assessed` · `Cleared` · `Needs review` · `Blocked`.

| Access pattern | Posture |
|---|---|
| Reading a publisher's public page in an interactive session | `Cleared` — this is `src_web_builtin`, already active agency-wide |
| Subscribing to a feed the publisher openly offers | `Cleared`, and record the feed's own terms in `Legal Posture Note` |
| Any **`scrape`** `Feed Type` | **STOP.** `Needs review` → Legal (10). **A scrape source with `Not assessed` may never be `active`** — a Class-2+ gate |
| Anything touching personal data | **STOP.** Legal (10) + an Approval-Matrix row. Deferred by standing decision |

`Cost` of `metered` or `subscription` routes to **Tech Stack (13)** (`techstack-cost-guardian`) before any spend — separate from the Legal gate and independently blocking.

## Step 5 · Consumers — the decision-purpose gate

`Consumers` is **required and non-empty**: *no source without a named downstream home.* A source nothing consumes is collection-because-we-can, which write contract §4.1 supersedes explicitly.

> ⚠️ **Finding F10 — this field is a hand-maintained shadow.** Its option set covers Sector Signals · State · Forecast · Market Routes · Destination Profile · Sector Intelligence, and **omits Sub-Sectors, Audience Roles and the DM Registry** — real consumers it cannot name. It can drift from the actual relations silently.
>
> **Verify the declaration against the real relations on every write.** Where a genuine consumer cannot be expressed, record it in `Notes` rather than picking the nearest wrong option, and do not pretend the multi-select is complete.

## Step 6 · Write your fields only

**Yours:** `Source Name` · `Source ID` · `Owner Body` · `Category` · `Authority Level` · `Feed Type` · `Feed URL (ICS/API)` · `Calendar URL` · `Cadence` · `Auth` · `Cost` · `Legal Posture` · `Legal Posture Note` · `State` · `Consumers` · `Confidence` · `Last Verified` · `Last Synced` · `Next Verification` · `Signal Role` · `Notes` · `Supersedes` · `Superseded By` · `Fallback Source` · `Sub-Sector` · `Geography`.

**Not yours:** `Signals` (S04) · `Market Routes` (S05).

`Source ID` is the slug join key into `AEIT_08` — reuse the existing slug where the pack already names one (`src_ke_public_holidays`, `src_ktb_events`), so the two registries stay joinable.

`Last Synced` is **not** `Last Verified`. A feed can keep delivering while its publisher has quietly moved.

`Signal Role` separates **Destination-side** from **Origin-side** — the axis the old model could not express. A German school-holiday calendar is origin-side for a Kenya-inbound route; Kenyan public holidays are destination-side.

## Step 7 · Mutation mode, verify, log

Match on the natural key **`Source ID`** before creating. Choose the mode explicitly. **Supersession, never deletion** — a retired source keeps its row and gains `Superseded By`, so historical records stay explicable.

Read each write back. Append one line to `01_Sector/_memory/skill_runs.jsonl` per [`contracts/skill-execution-record.schema.json`](../../../01_Sector/contracts/skill-execution-record.schema.json) with `skill_id: "S03"`, every gate result, and — for each source — **what the live call actually returned**. Loops: `activation`, `refresh`.

Set `Next Verification` from the §4.4 proximity ladder, not from habit. Annual-recurring publishers verify at T-180 and are **never auto-rolled forward** — *a recurring event is a prediction until its next edition is published.*

---

## Two rules the first bulk registration proved (2026-08-28)

**1. A feed is proven by CONTENT-TYPE, never by a status code.** Probing 24 publishers for `/feed`, `/rss.xml`,
`/events.ics` and `/feed.xml` returned nine apparent hits at HTTP 200. **Seven were `text/html`** — single-page apps
answering 200 to any path. Only **three** were real (`application/rss+xml`). A status-code check would have
registered **seven fabricated RSS feeds**, each of which would then have been trusted to refresh itself and would
have silently gone stale. *Check `%{content_type}`, and record what you actually found.*

**2. A vendor is `T1` about itself.** This department rightly downgrades vendor blogs to `T3` when they make market
claims. But a vendor announcing **its own conference date** is the body that sets the date. **The tier is a property
of the claim, not of the publisher's business model** — see `src_salesforce_dreamforce`, `src_hubspot_inbound`,
`src_freightwaves_f3` and `src_alm_legalweek`: all `T1` for their own events, all still `T3` for commentary.
The corollary is a real trap: a source can be **`T1` for one claim and unbacked for another in the same signal**
— see `src_efrag_esrs`, which is the ESRS standard-setter (T1) but **not** the authority for the Commission's
reporting delay. **Register the source against the claim, not against the row.**

## Refuse

- **`active` without a live verification call in this session.** No exceptions for a source the owner named.
- A `Feed URL` that was not actually retrieved. Blank beats plausible.
- A `scrape` source with `Legal Posture = Not assessed`.
- **Recording a `Feed Type` of `RSS` / `ICS` / `JSON` on the strength of a status code alone.**
- Setting `Last Verified` on a source whose verification call did **not** succeed.
- A source with empty `Consumers`.
- An `Authority Level` above what the publisher supports — the aggregator that lists an event is never T1 for it.
- Deleting a superseded row.

## What is blocked until this skill runs

**Zero sources are `active`, so no signal can legitimately inherit an authority tier.** Every `Source Tier` currently on DB 7 was assigned by hand with nothing behind it. S04 cannot honestly tier a signal until its publisher is registered here — which is why S03 precedes S04 in the build order despite the lower number.

## Appendix · A dated snapshot — re-measure it, do not trust it

> **Observation with an expiry date, not part of the procedure.** Step 2 governs.

**Measured 2026-08-24.** DB 14 held **0 rows**. The Hospitality slice of DB 7 held 10 signals: **1 at T1** (an organiser's own site), 7 at T3 (vendor blogs, aggregators, operator consensus), 2 at T4 (encyclopaedia entries for gazetted public holidays). Several rows recorded their own weakness in the source field — *"gazette notice not directly read"* — which is honest and still not a registration.
