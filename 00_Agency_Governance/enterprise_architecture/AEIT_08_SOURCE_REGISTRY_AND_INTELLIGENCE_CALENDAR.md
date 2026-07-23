# AEIT_08 — Agency Global Source Registry & Intelligence Calendar (Blueprint)

**Version:** v0.1
**Last updated:** 2026-07-22
**Owner:** Mary Thuo (Agency Governance, 00)
**Fills:** `GLOBAL_OS.md` §11 item 1 — *Agency Global Source Registry (source IDs, active/superseded/
archive state, owners, cadence)* — the longest-standing **Open** gap.
**Status:** **Specification only.** Defines the registry schema + the refresh discipline. Does **not**
populate sources (that arrives with IntOS activation). Illustrative rows are labelled as examples.

> The repo already has a **tool/connector inventory** (Tech Stack 13) and a **CRM object model**
> (Governance). What it lacks is a registry of *where intelligence comes from* — the inputs to IntOS.
> This is that registry's design.

---

## 1. Source entity schema

Every source is one row keyed by a stable `source_id`. Fields (extends the `Source` entity in
`AEIT_06`):

| Field | Type | Meaning |
|---|---|---|
| `source_id` | id | stable, never reused |
| `name` | text | human name |
| `category` | enum | see §2 |
| `access_method` | enum | official-API / public-API / registry / scrape / RSS / MCP / manual / AI-assisted |
| `trust` | 1–5 | how much we trust its claims (drives IntOS trust score) |
| `coverage` | text | what entities/topics it covers |
| `latency` | enum | realtime / daily / weekly / on-demand |
| `freshness` | date | **last verified** (not "added" — per `TECHSTACK_OS.md:152` discipline) |
| `legal` | enum + note | ToS/robots/PII posture → Legal (10) sign-off flag |
| `auth` | enum | none / key / oauth / account |
| `rate_limits` | text | calls/window |
| `cost` | text | free / metered / subscription (runway in units) |
| `fallback` | source_id | what to use if this fails |
| `consumers` | dept[] | who relies on it |
| `cadence` | cron-ish | how often it is collected/revalidated (→ §4) |
| `owner` | dept | single owning department |
| `state` | enum | **active / superseded / archived** (with supersession chain) |

---

## 2. Source categories (coverage of the input universe)

Official APIs · Public APIs · Public/government registries · Research platforms · Social networks ·
Search engines · Company websites · RSS · Forums · Communities · Directories · News · Technical
documentation · Public repositories · Knowledge bases · Browser automation · Scraping platforms ·
Search platforms · Manual collection · AI-assisted collection.

Each registered source declares its category; the category informs default `trust`, `legal`, and
`access_method`.

---

## 3. Illustrative rows (EXAMPLES — not a populated registry)

Drawn only from what the repo already confirms exists, to show the schema in use. Real population is
deferred.

| source_id | name | category | access | trust | state | owner |
|---|---|---|---|---|---|---|
| `src_sector_xlsx` | Owner-curated SaaS taxonomy (xlsx) | Knowledge base | manual | 5 | active | Sector (01) |
| `src_clickup_crm` | Agency CRM (ClickUp) | Official API | account | 5 | active | Governance (00) |
| `src_zoho_books` | Zoho Books (invoicing) | Official API | account | 4 | active* | Finance (09) |

\* `src_zoho_books` illustrates two live findings: it is **missing from the DPA sub-processor
register** and its **trial expired** (`AEIT_04 §D1`) — exactly the kind of drift the registry's
`legal` + `freshness` fields exist to catch.

---

## 4. The Intelligence Calendar (refresh / decay / revalidation)

Information is dynamic; **nothing is assumed permanently correct.** This is an operational rhythm
that sits alongside the existing 7 Cognitive Calendars (it is the intelligence-specific 8th rhythm,
owned jointly by IntOS and Operations' calendar-orchestrator).

| Mechanism | Rule |
|---|---|
| **Scheduled refresh** | Each source's `cadence` drives routine re-collection. |
| **Event-based refresh** | A `Signal/Event` (`AEIT_06`) about an entity forces re-collection of related knowledge. |
| **Risk-based refresh** | Higher-risk-class decisions demand fresher, higher-trust knowledge before acting. |
| **Confidence decay** | Confidence declines with age; below a threshold, the Knowledge Object returns to **Revalidate** (SM4). |
| **Staleness detection** | `freshness` older than the source's max-age flags the object stale. |
| **Change detection** | Diff against last snapshot; a change emits a `Signal`. |
| **Revalidation** | Re-run verification; update trust/confidence; log to Learning memory. |
| **Learning loop** | Sources whose claims proved wrong lose trust; the registry self-corrects. |

**Anchor discipline:** every knowledge claim carries a **last-verified date**, generalizing the
convention Tech Stack adopted after its inventory rotted undetected (`TECHSTACK_OS.md:152`) and
Automation adopted after the 11-day outage (`AUTOMATION_OS.md:152`).

---

## 5. Governance of the registry

- **Registration gate:** a source enters `active` only after a **live verification call** proves it
  answers — mirroring `techstack-inventory-registrar`'s "verify, don't assume" rule. No source is
  registered on faith.
- **Legal boundary:** any `scrape`/`browser-automation` source requires a Legal (10) posture note
  (ToS/robots/PII) before `active`. This is a Class-2+ gate.
- **Supersession, not deletion:** replaced sources move to `superseded` with a pointer to their
  successor; the chain stays auditable (the repo's existing supersession pattern).

---

## 6. What is deferred
- **Population.** No real sources are catalogued here beyond the three illustrative rows.
- **Collector code.** Connectors are built in the IntOS Collection layer post-activation (`AEIT_10`).

## 7. Decision Log
- **2026-07-22 — Source Registry + Intelligence Calendar specified.** Closes the design of
  `GLOBAL_OS.md` §11 item 1; schema includes active/superseded/archived state + last-verified
  freshness + legal boundary gate. — Claude Code (Opus 4.8)

## 8. Changelog
- **v0.1 (2026-07-22):** Created. — Claude Code (Opus 4.8)
