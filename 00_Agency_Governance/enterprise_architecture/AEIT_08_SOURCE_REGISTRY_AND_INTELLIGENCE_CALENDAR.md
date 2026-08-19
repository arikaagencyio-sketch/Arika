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

## 3.1 Registered intelligence sources — Sector Commercial Activation MCP stack *(added 2026-08-19)*

First **real** (non-illustrative) registration, driven by Sector (01)'s commercial-activation phase
(plan ADDENDUM 4). Split by PII/Legal exposure — the honest line between what runs now and what is
gated. Every row names its **`consumers`** (destination DB) per the decision-purpose gate
(`SECTOR_ACTIVATION_CONTRACT.md` §13.3): **no source without a downstream home.**

**Tier 1 — Market / web intelligence (non-PII; lower Legal risk).** *For the single-sector pilot the
"web researcher" is the interactive Claude Code session itself — `WebSearch`/`WebFetch` are already
available and sufficient. The scraping MCPs below are registered for when we generalize across many
sub-sectors/companies, not for the pilot.*

| source_id | name | category | access | trust | cost | consumers | state |
|---|---|---|---|---|---|---|---|
| `src_web_builtin` | Interactive WebSearch/WebFetch | Search/Browser | MCP/AI-assisted | 3 | free | Sector Signals · Intelligence · Linguistics · DM-titles · Tool-Stack | **active** (verified in session) |
| `src_firecrawl` | Firecrawl (scrape-first; keyless tier) | Scraping platform | MCP | 3 | free tier / metered | Sector Intelligence · company-website reads · DM-title pages | registered — stand up at generalization |
| `src_tavily` | Tavily (ranked web search) | Search platform | MCP | 3 | free tier / metered | Sector Signals · Intelligence | registered — stand up at generalization |
| `src_exa` | Exa (semantic search) | Search platform | MCP | 3 | metered | Sector Signals · Intelligence | registered (alt to Tavily) |
| `src_perplexity` | Perplexity (cited synthesis) | Research platform | MCP | 3 | metered | Sector State / Forecast summaries | registered — optional |
| `src_fetch` | Fetch (URL fallback) | Browser automation | MCP | 2 | free | any | registered — fallback |

**Tier 2 — People / contact data (PII; paid; Legal-gated; DEFERRED).** Provides real decision-maker
names/emails/dials → CRM. **Not connected.** Enters `active` only after a Legal (10) posture note
(ToS/robots/PII/GDPR) + a live verification call + cost governance + an Approval-Matrix row
(`AEIT_07`/`AEIT_10`; §5 below).

| source_id | name | category | access | trust | cost | consumers | state |
|---|---|---|---|---|---|---|---|
| `src_apollo` | Apollo.io (contact DB + enrichment + sequences) | Directory/API | MCP | 4 | paid | CRM `Lead` · Decision-Maker Registry (named people) | **registered — GATED (Legal + cost)** |
| `src_clay` | Clay (waterfall enrichment, 150+ providers) | Data platform | MCP | 4 | paid | CRM `Lead` enrichment | **registered — GATED (Legal + cost)** |
| `src_cognism` | Cognism (EU verified dials/emails) | Directory/API | MCP | 4 | paid | CRM `Lead` (EU/GDPR region) | **registered — GATED (Legal/GDPR)** |

**Honesty (carried from `SECTOR_ACTIVATION_CONTRACT.md` §14.5):** cloud routines have **no web** —
collection is interactive/human or a gated runtime; **no unattended scraper daemon**. Tier-1 sources
read public, non-PII pages; Tier-2 sources touch personal data and stay gated until Legal signs the
posture. The paid people-data MCP is authorized by the owner **after** the Hospitality pilot proves
the loop.

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
- **2026-08-19 — First real sources registered (§3.1), driven by Sector commercial activation
  (ADDENDUM 4).** The registry moves from spec-only to holding a live Tier-1 source (`src_web_builtin`,
  verified active) + a registered-but-not-connected web-research MCP stack (Firecrawl/Tavily/Exa/
  Perplexity/Fetch) + a **gated** Tier-2 people-data set (Apollo/Clay/Cognism, Legal+cost gate). Every
  source names its `consumers` DB (decision-purpose gate). Population is still narrow (Sector's stack);
  other departments' sources remain deferred. — Claude Code (Opus 4.8)

## 8. Changelog
- **v0.1 (2026-07-22):** Created. — Claude Code (Opus 4.8)
- **v0.2 (2026-08-19):** Added §3.1 — the Sector Commercial Activation MCP stack (Tier-1 market/web
  now; Tier-2 people-data gated). First non-illustrative rows. — Claude Code (Opus 4.8)
