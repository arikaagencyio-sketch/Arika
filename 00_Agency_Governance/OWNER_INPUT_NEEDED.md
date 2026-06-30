# Owner Input Needed — Consolidated Tracker

**Status:** Living document — updated as each department's content migration surfaces new items. Review in one sitting once migration is further along, or pick off items anytime.
**Last updated:** 2026-06-30

> Referenced from [`GLOBAL_OS.md`](../GLOBAL_OS.md) §11. This file exists because individual departments correctly flag what's missing inside their own `{DEPT}_OS.md`, but those flags get buried across 12+ files as migration proceeds. This is the single place they roll up.

---

## How to use this

Every row below needs a real fact from the agency owner — a name, a number, a confirmed decision — that **cannot be filled in by reading the raw drafts**, because the raw drafts don't contain it (they're brainstorm theory, not operating history) and inventing it would violate the no-silent-invention rule (`AGENCY_OPERATING_CONSTITUTION.md` §3). Distinguish this from gaps that will close on their own once the system runs (Decision Logs, Memory Logs — those need no owner action, just time and real usage).

Work through this in any order — except item 0 below, which should come first if you only have time for one.

When an item is resolved, move it to "Resolved" at the bottom with the date and a pointer to where the real value now lives — don't delete the row, so there's a record of when/how it was closed.

---

## 🔴 Highest priority

| # | Item | Why it matters | Currently | Source file |
|---|---|---|---|---|
| 0 | **Which real sector(s)/industry vertical(s) does the agency actually target?** | Sector (01) is the upstream-most layer in the agency's own stated operating flow — its own doctrine states "if your sector layer is weak, everything downstream underperforms" (Offer, Marketing, Sales, Branding all package/distribute/sell "sector truth"). All 14 raw drafts in this department use only hypothetical example industries (fintech, SaaS, e-commerce, etc.) and repeatedly end with an unanswered invitation to supply a real sector. This is arguably the single highest-leverage open item in the whole repo — most other departments' content (Offer's pricing tiers, Marketing's client segments, etc.) would sharpen considerably once this is answered. | No real sector ever named | `01_Sector/SECTOR_OS.md` §1 |

---

## Agency-Wide (00_Agency_Governance)

| # | Item | Why it matters | Currently | Source file |
|---|---|---|---|---|
| 1 | Real mission statement, annual objectives, quarterly goals | Everything else (department mandates, KPI thresholds, RACI priorities) should trace back to this; currently the only "mission" is a generic working description | Placeholder | `AGENCY_OPERATING_CONSTITUTION.md` §2 |
| 2 | Agency owner's name (referenced throughout as "agency owner" for Risk Class 3+/4 sign-off) | Constitution and automation matrix both require a specific accountable human for high-risk approvals | Generic "agency owner" | `AGENCY_OPERATING_CONSTITUTION.md` §4-5 |
| 3 | All 12 department owners | RACI, KPI dictionary, and automation matrix are all structurally complete but operationally inert until real names replace "Responsible/Accountable: Department Name" | All `(unassigned)` | `GLOBAL_OS.md` §4 Department Index; every `{DEPT}_OS.md` header |
| 4 | KPI owner/cadence/threshold for every metric in the dictionary | Formulas are defined; without an owner and threshold, nothing actually gets tracked or acted on | All `(unassigned)` / `(unset)` | `AGENCY_KPI_DICTIONARY.md` |
| 5 | CRM platform selection (HubSpot/Pipedrive/Salesforce/other) | `CRM_SCHEMA.md` defines the object model but deliberately doesn't pick a tool — that's a real decision, not a research task | Not decided | `CRM_SCHEMA.md` "What this schema deliberately does not specify"; relevant to Tech Stack (13) |

## Department: Offer (02)

| # | Item | Why it matters | Currently | Source file |
|---|---|---|---|---|
| 6 | Confirm or correct positioning: "Revenue Infrastructure Partner" | This phrase recurs across 6+ independently-generated drafts (strong internal signal) but was never confirmed as actually adopted/used with a real client | Leading candidate, unconfirmed | `02_Offer/OFFER_OS.md` §1 |
| 7 | Real pricing — which (if any) of the 5 conflicting draft pricing tables is closest to reality, or none of them | 5 source files propose 5 different number ranges for the same tier concept; none are validated against actual invoices or deals | All marked draft/unvalidated | `02_Offer/OFFER_OS.md` §7 |
| 8 | Real historical conversion/margin/LTV figures | KPI table currently has only template targets pulled from AI-generated pitches, no actuals | All marked draft/unvalidated | `02_Offer/OFFER_OS.md` §7 |

## Department: Sales (05)

| # | Item | Why it matters | Currently | Source file |
|---|---|---|---|---|
| 9 | Real KPI Dictionary values (CAC, conversion rate, sales cycle length, etc.) | RevOps Agent's mandate covers this, but no real figures exist anywhere in the raw material — confirmed genuine absence, not unmigrated content | Empty | `05_Sales/SALES_OS.md` §7 |
| 10 | Locate or confirm-absent: 11 "companion" source `.docx` files referenced in `Master_Source_Registry.csv` but not present anywhere in this folder (e.g. `HE SALES OS_2024.docx`, `Sales Mechanism 102.docx`) | Citation system is otherwise verified-trustworthy; these specific citations can't currently be checked | Unlocated | `05_Sales/SALES_OS.md` §14 |
| 11 | Reconcile this department's 4-tier risk classification with the agency-wide one in the Constitution | Both exist and map closely but were never formally merged into one system | Two parallel frameworks | `05_Sales/SALES_OS.md` §10; `AGENCY_OPERATING_CONSTITUTION.md` §5 |

## Department: Marketing (03)

| # | Item | Why it matters | Currently | Source file |
|---|---|---|---|---|
| 12 | Confirm or correct: does the agency actually operate in/serve Kenya? | "Kenya Data Protection Act" appears alongside GDPR/CCPA in one raw draft — the only concrete jurisdictional signal found anywhere in this department, possibly real, possibly just an AI-generated example | Unconfirmed signal | `03_Marketing/MARKETING_OS.md` §14 |
| 13 | Real KPI values (LTV:CAC, CAC payback, funnel conversion, etc.) — currently only industry-standard benchmark ranges, no agency actuals | KPI Dictionary structurally complete but substantively template-only | All marked template/aspirational | `03_Marketing/MARKETING_OS.md` §7 |
| 14 | Confirm which (if any) MCP/connector blueprint items are actually configured/in use | Blueprint lists 7 connector-class layers as a wishlist — none confirmed real | All aspirational | `03_Marketing/MARKETING_OS.md` §12 |

## Department: Content (04)

| # | Item | Why it matters | Currently | Source file |
|---|---|---|---|---|
| 15 | Confirm the Content/Marketing department boundary (Content = assets/narrative, Marketing = positioning/campaign/channel) | The raw source material never anticipates a Content/Marketing split at all — it describes one unified system and one file explicitly argues content should NOT be a marketing sub-function. The current boundary is an architectural decision made during this restructuring, not one drawn from the source. | Imposed split, unconfirmed by owner | `04_Content/CONTENT_OS.md` §1 |
| 16 | Confirm/adopt or reject the Project Realignment's repositioning (LinkedIn-centric "Revenue Reality" → broader "Revenue Intelligence/Architecture/Engineering" with LinkedIn as one node among several) | This is the most decision-like document found in any department so far, but it's unconfirmed reasoning, not a logged decision — no date, no approver, no outcome | Unconfirmed | `04_Content/CONTENT_OS.md` §10 |
| 17 | Resolve the 3-way content-pillar naming conflict (generic Growth/Revenue/Acquisition set vs. LinkedIn-specific "Revenue Reality" set vs. the Realignment file's 7-pillar set) | Downstream content planning can't proceed consistently with 3 unreconciled pillar sets | Documented, not resolved | `04_Content/CONTENT_OS.md` §10 |
| 18 | Confirm real LinkedIn/Instagram launch timing, so the 90-day numeric targets (comments, DMs, profile views, newsletter subscribers, discovery calls) become a real plan instead of a draft template | These targets are unusually concrete (more so than any other department's KPIs) but have no anchor start date | Targets exist, no launch date | `04_Content/CONTENT_OS.md` §7 |

## Department: ClientPartner Acquisition (06)

| # | Item | Why it matters | Currently | Source file |
|---|---|---|---|---|
| 19 | Reconcile the operational boundary between ClientPartner Acquisition (06), Sales (05), and Marketing/Content (03/04) | The source material for this department sprawls into Sales territory (full "Conversion/Sales Engine" layer with close rates, CRM tools) and Marketing/Content territory (audience-building, social media) — the current narrow boundary ("feeds Sales, same as Marketing") is this restructuring's own framing, not something the source material draws itself. Best done once Sales, Marketing, and Content are all fully migrated so the comparison is apples-to-apples. | Documented, not resolved | `06_ClientPartner_Acquisition/CLIENTPARTNER_OS.md` §10 |
| 20 | Confirm real partner names, deals, or revenue-share terms (currently all illustrative — e.g. "Distribution Partner 20-40%" is explicitly labeled "Example Split" in its source file) | KPI Dictionary and Partner CRM object are structurally ready but have zero real data | All draft/illustrative | `06_ClientPartner_Acquisition/CLIENTPARTNER_OS.md` §7 |

## Department: Client Success (07)

| # | Item | Why it matters | Currently | Source file |
|---|---|---|---|---|
| 21 | Pick a single client journey/lifecycle stage model — 3 unreconciled versions exist (7-stage, 9-stage, 7-phase) | Downstream onboarding/retention workflows can't be built consistently against 3 different stage namings for the same idea | Documented, not resolved | `07_Client_Success/CLIENTSUCCESS_OS.md` §4 |
| 22 | Reconcile the Client-Success/Operations delivery handoff | Source material inconsistently shows Client Success owning delivery execution directly vs. handing off cleanly to Operations (08) — only one of several drafts draws a clean line | Documented, not resolved | `07_Client_Success/CLIENTSUCCESS_OS.md` §14 |
| 23 | Reconcile pre-sale qualification (Sales' territory) vs. post-sale segmentation (this department's actual mandate) — same class of issue as item 19 for ClientPartner Acquisition | Source material conflates the two; affects where qualification scoring logic should actually live | Documented, not resolved | `07_Client_Success/CLIENTSUCCESS_OS.md` §14 |
| 24 | Build a real offboarding/churn process | Confirmed near-total absence — appears only as an empty filename placeholder in the source material | Effectively nonexistent | `07_Client_Success/CLIENTSUCCESS_OS.md` §10 |

## Department: Finance (09)

| # | Item | Why it matters | Currently | Source file |
|---|---|---|---|---|
| 25 | Connect at least one real financial integration (Stripe/QuickBooks/banking API/etc.) | `integrations/index.ts` is the one confirmed genuine stub in an otherwise more-real-than-expected codebase — no real connector exists, so none of the working risk/cashflow logic can run against actual data | Interface only, zero real connectors | `09_Finance/FINANCE_OS.md` §13 |
| 26 | Confirm or set real thresholds for runway, DSCR, client concentration, reserve tiers, expense approval tiers | These are generic doctrine numbers currently hardcoded as if real (e.g. runway alert <60 days, concentration critical >35%, expense approval at $500/$5K/$25K) — they're implemented in working risk-engine code, so they'll actually fire once real data flows through, using assumed-not-confirmed values | Doctrine defaults, unconfirmed by owner | `09_Finance/FINANCE_OS.md` §7 |
| 27 | Decide whether to wire the 7 documented AI agents (CFO, Cashflow, Risk, Profitability, Treasury, Compliance, Leakage Detection) to an actual LLM, or keep them as structured prompts/event-routing metadata only | Currently real spec data but no code calls an LLM to execute them | Spec exists, not executable | `09_Finance/FINANCE_OS.md` §5 |

## Department: Branding (12)

| # | Item | Why it matters | Currently | Source file |
|---|---|---|---|---|
| 28 | Decide whether to wire the 20 documented brand agents to an actual LLM, or keep them as structured prompts/routing metadata only | Same open question as Finance's 7 agents (#27) — `agent_prompt()` generates a prompt string per agent but nothing in the codebase calls an LLM to execute them | Spec + routing exists, not executable | `12_Branding/BRANDING_OS.md` §5 |
| 29 | Confirm or set real `BrandScoringEngine` dimension thresholds (currently generic 70-78 defaults) | These are implemented in working code and will actually gate/flag deliverables once real data flows through — but the cut-lines are designed defaults, not calibrated against real outcomes | Doctrine defaults, unconfirmed by owner | `12_Branding/BRANDING_OS.md` §7 |
| 30 | Define the agency's own real brand (positioning, voice, identity) so BOIS has a non-hypothetical client to run against | Every BOIS run to date (including the one confirmed smoke test) has used a hypothetical example client ("Sample Nairobi Laundry") — the system has never been pointed at the agency's own brand, which is the most immediate real use case available | No real brand object exists yet, even for the agency itself | `12_Branding/BRANDING_OS.md` §2, §4 |

---

## Resolved

*(none yet)*

## Changelog

- 2026-06-30 — Tracker created, seeded with items surfaced during Offer and Sales content migration plus 5 agency-wide items from the governance-closure pass. — Claude Code (Sonnet 4.6)
- 2026-06-30 — Added items 25-27 (Finance) and 28-30 (Branding) as those departments' content migrations completed. — Claude Code (Sonnet 4.6)
