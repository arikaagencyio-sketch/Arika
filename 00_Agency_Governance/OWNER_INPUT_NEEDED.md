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

*(empty — item 0, the real-sector decision, was resolved 2026-06-30. See Resolved table at the bottom.)*

---

## Agency-Wide (00_Agency_Governance)

| # | Item | Why it matters | Currently | Source file |
|---|---|---|---|---|
| 1 | Real mission statement, annual objectives, quarterly goals | Everything else (department mandates, KPI thresholds, RACI priorities) should trace back to this; the agency's name is now confirmed (Arika Agency, item 0 resolution) but mission/objectives are still a generic working description | Placeholder | `AGENCY_OPERATING_CONSTITUTION.md` §2 |
| 2 | Agency owner's name (referenced throughout as "agency owner" for Risk Class 3+/4 sign-off) | Constitution and automation matrix both require a specific accountable human for high-risk approvals | Generic "agency owner" | `AGENCY_OPERATING_CONSTITUTION.md` §4-5 |
| 3 | All 12 department owners | RACI, KPI dictionary, and automation matrix are all structurally complete but operationally inert until real names replace "Responsible/Accountable: Department Name" | All `(unassigned)` | `GLOBAL_OS.md` §4 Department Index; every `{DEPT}_OS.md` header |
| 4 | KPI owner/cadence/threshold for every metric in the dictionary | Formulas are defined; without an owner and threshold, nothing actually gets tracked or acted on | All `(unassigned)` / `(unset)` | `AGENCY_KPI_DICTIONARY.md` |
| 5 | CRM platform selection (HubSpot/Pipedrive/Salesforce/other) | `CRM_SCHEMA.md` defines the object model but deliberately doesn't pick a tool — that's a real decision, not a research task | Not decided | `CRM_SCHEMA.md` "What this schema deliberately does not specify"; relevant to Tech Stack (13) |

## Department: Sector (01)

| # | Item | Why it matters | Currently | Source file |
|---|---|---|---|---|
| 31 | Export and provide the full "Sider Fusion" chat conversation that produced the Tier 2/3 ICP material | The version captured in this repo (`01_Sector/Draft 16-17`) was pasted in chunks and hit a paste-size limit 3 times — Tier 2 and the Healthcare deep-dive are real but partial; Real Estate Brokerages and Franchise Systems (Tier 3) never received their full deep-dive | Partial — flagged explicitly in source files, not silently treated as complete | `01_Sector/Tier 2 ICP...Draft 16.md`; `01_Sector/Tier 3 ICP...Draft 17.md` |
| 32 | Pick one of the 3 unreconciled "intelligence layer" models (4-layer Data/Process/Human/AI vs. 7-layer vs. a different 4-layer Data/Diagnostic/Operational/Strategic) as the agency's actual operating framework | These describe the agency's own core capability stack — used to organize how Arika Agency itself delivers work, not just a client-facing diagnostic, so worth a deliberate owner call rather than a default pick | 3 versions documented, none chosen | `01_Sector/SECTOR_OS.md` §10 |

## Department: Offer (02)

| # | Item | Why it matters | Currently | Source file |
|---|---|---|---|---|
| 6 | Confirm or correct positioning: "Revenue Infrastructure Partner" | This phrase recurs across 6+ independently-generated drafts (strong internal signal) but was never confirmed as actually adopted/used with a real client | Leading candidate, unconfirmed | `02_Offer/OFFER_OS.md` §1 |
| 7 | Real pricing — which (if any) of the now 6 conflicting draft pricing sources is closest to reality, or none of them | 5 source files in Offer propose 5 different number ranges for the same tier concept; Sector (01)'s new real ICP database (`01_Sector/SECTOR_OS.md` §1, §3) adds a 6th, more granular pricing hypothesis (per-subsector entry-audit + retainer ranges) — none validated against actual invoices or deals | All marked draft/unvalidated | `02_Offer/OFFER_OS.md` §7; `01_Sector/SECTOR_OS.md` §3 |
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
| 20 | Confirm real partner names, deals, or revenue-share terms (currently all illustrative — e.g. "Distribution Partner 20-40%" is explicitly labeled "Example Split" in its source file) | KPI Dictionary and Partner CRM object are structurally ready but have zero real data | All draft/illustrative | `06_ClientPartner_Acquisition/CLIENTPARTNER_OS.md` §7 |

## Department: Client Success (07)

| # | Item | Why it matters | Currently | Source file |
|---|---|---|---|---|
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

| # | Item | Resolution | Date | Source file |
|---|---|---|---|---|
| 19 | Reconcile the operational boundary between ClientPartner Acquisition (06), Sales (05), and Marketing/Content (03/04) | Resolved by architectural reconciliation, not owner input — didn't need a real fact, just full-repo comparative analysis once all three departments were migrated. ClientPartner Acquisition's mandate narrowed to the Partner pipeline only; client-acquisition-system content reassigned to Sales/Marketing as cross-references. | 2026-06-30 | `06_ClientPartner_Acquisition/CLIENTPARTNER_OS.md` §1, §3, §10 |
| 21 | Pick a single client journey/lifecycle stage model | Resolved by architectural reconciliation. Adopted the 9-stage (Draft 2) model as canonical — the only one of the 3 that maps cleanly onto this repo's own department flow with no stage left ownerless. Other 2 models kept as superseded reference, not deleted. | 2026-06-30 | `07_Client_Success/CLIENTSUCCESS_OS.md` §4 |
| 22 | Reconcile the Client-Success/Operations delivery handoff | Resolved by architectural reconciliation. Reaffirmed the existing handoff (Client Success scopes, Operations delivers) — drafts that folded delivery into Client Success predate the Operations department concept (Operations has zero raw content anywhere in this repo). No change made. | 2026-06-30 | `07_Client_Success/CLIENTSUCCESS_OS.md` §10 |
| 23 | Reconcile pre-sale qualification vs. post-sale segmentation | Resolved by architectural reconciliation. Qualification scoring reassigned to Sales (05) (matches its citation-backed Lead Qualification agent); Client Success's mandate confirmed as post-sale segmentation only. | 2026-06-30 | `07_Client_Success/CLIENTSUCCESS_OS.md` §3, §10; `05_Sales/SALES_OS.md` §3 |
| 0 | Which real sector(s)/industry vertical(s) does the agency actually target? | **Resolved by direct owner input** — the highest-priority item in this tracker. Owner provided `Other Source Reference/Arika_B2B_SaaS_Intelligence_Database.xlsx` (a 13-sheet real, curated database) plus a partial chat transcript. Real sector confirmed: B2B SaaS, 3-tier ICP (Tier 1: Series A-C $5M-$50M ARR; Tier 2: Post-Seed-Series A $1M-$10M ARR; Tier 3: multi-location niche verticals). Agency's real name also confirmed in the same exchange: **Arika Agency**. | 2026-06-30 | `01_Sector/SECTOR_OS.md` §1, §2, §3 |

## Changelog

- 2026-06-30 — Tracker created, seeded with items surfaced during Offer and Sales content migration plus 5 agency-wide items from the governance-closure pass.
- 2026-06-30 — **Resolved item 0** (real sector, agency's #1 priority item) via direct owner input — see Resolved table. Added items 31-32 (Sector) for the now-partial chat-transcript source and the unreconciled intelligence-layer models. Updated item 7 (Offer pricing) to note the new 6th conflicting pricing source from Sector's real ICP database. — Claude Code (Sonnet 4.6)
- 2026-06-30 — Added items 25-27 (Finance) and 28-30 (Branding) as those departments' content migrations completed. — Claude Code (Sonnet 4.6)
- 2026-06-30 — Reconciliation pass: resolved items 19, 21, 22, 23 (cross-department boundary/model decisions) by direct architectural analysis now that all relevant departments are migrated — these turned out not to be owner-input items at all (no real fact was missing, just full-repo context), so moved to Resolved rather than left for the owner. Remaining open items are genuine owner-input gaps. — Claude Code (Sonnet 4.6)
