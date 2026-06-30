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
| 4 | KPI thresholds for every metric in the dictionary | Owner and cadence are now set for every metric; only real threshold cut-lines (e.g. "alert if CAC > $X") remain genuinely unset — needs actual measured agency data, can't be invented | All `(unset)` | `AGENCY_KPI_DICTIONARY.md` |
| 33 | Confirm exact owner email address — given as `mary.thuo@arikaagencycom`, likely missing a "." before "com" | Real contact info now lives in the constitution; a typo'd email shouldn't be silently "corrected" and treated as confirmed | Recorded as given, flagged as a likely typo | `AGENCY_OPERATING_CONSTITUTION.md` §2 |
| 35 | Confirm the derived weekly/quarterly/half-year/yearly revenue targets (item 34's resolution only directly confirmed monthly/daily) | These are simple multiplication from the real $1M/month and $35K/day figures, not invented — but real operating cadence (weekends, holiday slowdowns) could mean they're not strictly linear; quick confirmation pass worth doing | Derived, not separately owner-confirmed | `AGENCY_REVENUE_TARGETS.md` |
| 36 | Reconcile Offer #1's own stated ICP (5-200 employees, $1M-$50M ARR, multi-industry) against Sector's real B2B-SaaS-only Tier 1/2/3 ICP | The two ICPs overlap but aren't identical — Offer's is broader (more industries) and slightly differently banded; affects which real sector segmentation the pricing-floor methodology should actually use | Two unreconciled real ICPs | `02_Offer/OFFER_OS.md` §3; `01_Sector/SECTOR_OS.md` §1 |

## Department: Sector (01)

| # | Item | Why it matters | Currently | Source file |
|---|---|---|---|---|
| 31 | If/when available: export and provide the full "Sider Fusion" chat conversation that produced the Tier 2/3 ICP material | The version captured in this repo (`01_Sector/Draft 16-17`) was pasted in chunks and hit a paste-size limit 3 times — Tier 2 and the Healthcare deep-dive are real but partial; Real Estate Brokerages and Franchise Systems (Tier 3) never received their full deep-dive. **Not blocking** — owner decided (2026-06-30) to proceed with what's captured rather than wait. | Partial — flagged explicitly in source files, not silently treated as complete | `01_Sector/Tier 2 ICP...Draft 16.md`; `01_Sector/Tier 3 ICP...Draft 17.md` |

## Department: Offer (02)

| # | Item | Why it matters | Currently | Source file |
|---|---|---|---|---|
| 7 | Real pricing — compute the segmented pricing-floor mean (methodology adopted 2026-06-30, not yet computable) | 7 conflicting pricing sources now exist (5 Offer drafts, Sector's real ICP database, and the first OEOS-engineered offer — itself now a real 3-tier example of the segmentation principle). Owner's direction: don't pick one as correct — compute a real per-(offer × sector-tier × company-size) mean as an internal "do not discount below" floor. **No longer blocked on revenue targets (item 34 resolved)** — still blocked on more real OEOS-engineered offers per segment (only 1 of likely many received so far) | Methodology adopted, offer #1 complete; first real floor calculation pending more offers | `02_Offer/OFFER_OS.md` §3, §10 |
| 8 | Real historical conversion/margin/LTV figures | KPI table currently has only template targets pulled from AI-generated pitches, no actuals | All marked draft/unvalidated | `02_Offer/OFFER_OS.md` §7 |
| 37 | Review/revise the Claude-synthesized completion of offer #2 (Sales Enablement Systems Phases 6-12) | The owner didn't have the original chat's completion, so Claude filled it in using offers #1/#3 as calibration — explicitly not owner-original, should be reviewed/approved or revised rather than treated as equally authoritative | Synthesized, unreviewed | `02_Offer/OEOS - Sales Division - Sales Enablement Systems (Claude-Synthesized Completion). Draft 32.md` |
| 38 | Decide pricing-segmentation variable: rep-count (offer #1's approach) vs. ARR-band (offer #3's approach), or both depending on offer type | Affects how the pricing-floor methodology's segmentation actually works once computable — the two real offers captured so far use different variables | Two real offers, two different real approaches, undecided | `02_Offer/OFFER_OS.md` §3 |
| 39 | Decide whether the agency should standardize on one canonical internal team-role roster, per-division rosters, or per-offer rosters | All 4 OEOS offers captured so far (across 2 divisions) each invented their own team-role names with only partial overlap — no longer a "watch for it" pattern, now a confirmed real inconsistency affecting how delivery teams would actually be staffed/named | 4 real offers, 4 different rosters, undecided | `02_Offer/OFFER_OS.md` §3 |

## Department: Sales (05)

| # | Item | Why it matters | Currently | Source file |
|---|---|---|---|---|
| 9 | Real historical KPI values (CAC, conversion rate, sales cycle length, etc.) — narrowed | Real daily *targets* now exist (item 34's resolution) — revenue/quotation/call/proposal/close targets, all owner-confirmed. What's still missing is *historical actuals* measured against those targets, which can't exist until the agency has operated against them for a real period | Targets real; historical actuals pending | `05_Sales/SALES_OS.md` §7 |
| 10 | Locate or confirm-absent: 11 "companion" source `.docx` files referenced in `Master_Source_Registry.csv` but not present anywhere in this folder (e.g. `HE SALES OS_2024.docx`, `Sales Mechanism 102.docx`) | Citation system is otherwise verified-trustworthy; these specific citations can't currently be checked | Unlocated | `05_Sales/SALES_OS.md` §14 |

## Department: Marketing (03)

| # | Item | Why it matters | Currently | Source file |
|---|---|---|---|---|
| 13 | Real KPI values (LTV:CAC, CAC payback, funnel conversion, etc.) — currently only industry-standard benchmark ranges, no agency actuals | KPI Dictionary structurally complete but substantively template-only | All marked template/aspirational | `03_Marketing/MARKETING_OS.md` §7 |
| 14 | Confirm which (if any) MCP/connector blueprint items are actually configured/in use | Blueprint lists 7 connector-class layers as a wishlist — none confirmed real | All aspirational | `03_Marketing/MARKETING_OS.md` §12 |

## Department: Content (04)

*(all 4 prior items resolved 2026-06-30 — see Resolved table)*

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
| 32 | Pick one of the 3 unreconciled "intelligence layer" models as the agency's actual operating framework | Resolved by architectural reconciliation, same class as item 19/21/22/23 — didn't need a real fact, just a structural call. Adopted the xlsx's 4-layer (Data/Process/Human/AI) model as canonical; the 7-layer and alternate-4-layer chat-sourced models are kept as elaborations layered on top, not competing frameworks. | 2026-06-30 | `01_Sector/SECTOR_OS.md` §8, §10 |
| 0 | Which real sector(s)/industry vertical(s) does the agency actually target? | **Resolved by direct owner input** — the highest-priority item in this tracker. Owner provided `Other Source Reference/Arika_B2B_SaaS_Intelligence_Database.xlsx` (a 13-sheet real, curated database) plus a partial chat transcript. Real sector confirmed: B2B SaaS, 3-tier ICP (Tier 1: Series A-C $5M-$50M ARR; Tier 2: Post-Seed-Series A $1M-$10M ARR; Tier 3: multi-location niche verticals). Agency's real name also confirmed in the same exchange: **Arika Agency**. | 2026-06-30 | `01_Sector/SECTOR_OS.md` §1, §2, §3 |
| 5 | CRM platform selection | **Resolved by direct owner input.** HubSpot confirmed. | 2026-06-30 | `CRM_SCHEMA.md` "Platform selection" |
| 6 | Confirm or correct positioning: "Revenue Infrastructure Partner" | **Resolved by direct owner input.** Confirmed as the real, adopted positioning. | 2026-06-30 | `02_Offer/OFFER_OS.md` §1 |
| 11 | Reconcile Sales' 4-tier risk classification with the agency-wide 5-class system | Resolved by architectural reconciliation, not owner input — didn't need a real fact, just a direct mapping (Constitution's Class 0+1 → Sales' Low; Class 2 → Medium; Class 3 → High; Class 4 → Critical). | 2026-06-30 | `05_Sales/SALES_OS.md` §8, §10 |
| 12 | Confirm or correct: does the agency actually operate in/serve Kenya? | **Resolved by direct owner input.** Confirmed real — Arika Agency operates in/serves Kenya, plus broader confirmation it serves clients globally and must comply with each jurisdiction's real laws as engagements happen. | 2026-06-30 | `03_Marketing/MARKETING_OS.md` §14 |
| 2 | Agency owner's real name | **Resolved by direct owner input.** Mary Thuo. Applied to `AGENCY_OPERATING_CONSTITUTION.md` (header + §4 Decision Rights), `AGENCY_RACI.md`, `AGENCY_KPI_DICTIONARY.md` (every metric's Owner column), `GLOBAL_OS.md` §4, and every `{DEPT}_OS.md` header. | 2026-06-30 | `AGENCY_OPERATING_CONSTITUTION.md` §4 |
| 3 | All 12 (now 13) department owners | **Resolved by direct owner input.** Mary Thuo, sole owner across all departments. Same propagation as item 2. | 2026-06-30 | `GLOBAL_OS.md` §4 Department Index; every `{DEPT}_OS.md` header |
| 15 | Confirm the Content/Marketing department boundary | **Resolved by direct owner input.** Confirmed: keep the split. | 2026-06-30 | `04_Content/CONTENT_OS.md` §1 |
| 16 | Confirm/adopt or reject the Project Realignment's repositioning | **Resolved by direct owner input.** Adopted: broader "Revenue Intelligence/Architecture/Engineering" framing, LinkedIn as one node among several. | 2026-06-30 | `04_Content/CONTENT_OS.md` §10 |
| 17 | Resolve the 3-way content-pillar naming conflict | **Resolved by synthesis, per owner direction to map all three correctly rather than pick one.** Built a canonical 7-pillar structure (Realignment's top level) populated with the generic set's 35 sub-topics and the LinkedIn DRAGON set's fully-built post series, kept intact under its own pillar. Flagged Sector (01)'s new real signal framework as stronger fuel for the "Revenue Signals" pillar than the generic placeholder topics. | 2026-06-30 | `04_Content/CONTENT_OS.md` §10 |
| 18 | Confirm real LinkedIn/Instagram launch timing | **Resolved by direct owner input.** Not launched yet, no date set — targets remain a ready-to-use template. | 2026-06-30 | `04_Content/CONTENT_OS.md` §7 |
| 1 | Real mission statement, annual objectives, quarterly goals | **Resolved by direct owner input.** Owner produced a full vision synthesis from a deep-dive across the entire project folder — preserved in full (not flattened, per explicit owner instruction) in new file `AGENCY_VISION.md`: 10-layer architecture, closed-loop system logic, financial architecture, client/offer/automation vision, and the "5 foundational realities" of business/project management. `AGENCY_OPERATING_CONSTITUTION.md` §2 now points to it. | 2026-06-30 | `AGENCY_VISION.md` |
| 34 | Real agency revenue targets | **Resolved by direct owner input.** $1,000,000/month, $35,000/day, non-negotiable — plus the deal-count logic (7 offers ≥$5K or 5 deals ≥$7K per day) and a 7-calendar cognitive operating system. New file `AGENCY_REVENUE_TARGETS.md`. Cross-referenced into Offer's pricing-floor methodology, Finance's KPI dictionary, and Sales' KPI dictionary. | 2026-06-30 | `AGENCY_REVENUE_TARGETS.md` |

## Changelog

- 2026-06-30 — Captured offer #4 (Demand Generation Infrastructure, Marketing Division, partial — see `Draft 33`) — the first non-Sales-division offer, confirming OEOS is being run agency-wide. Confirmed the prompt's templating mechanic (only the Phase 1 "Offer Constraints" seed block varies per offer run). With 4 real offers now in, upgraded the team-role-roster inconsistency from a "watch for it" note to item 39 (real decision needed — every offer invented its own roster). — Claude Code (Sonnet 4.6)
- 2026-06-30 — Captured offer #3 (Outbound Sales Engine, real, substantially complete — see `Draft 31`). Completed offer #2's missing Phases 6-12 via Claude synthesis since the owner didn't have that part (explicitly flagged, not owner-original — see `Draft 32`). Added items 37 (review the synthesized completion) and 38 (pricing-segmentation variable: rep-count vs. ARR-band — two real offers now use two different real approaches). — Claude Code (Sonnet 4.6)
- 2026-06-30 — **Resolved items 1 (mission/vision) and 34 (revenue targets)** via direct owner input — full detail preserved in two new files, `AGENCY_VISION.md` and `AGENCY_REVENUE_TARGETS.md` (not flattened, per explicit owner instruction). Narrowed item 9 (Sales KPI) now that real targets exist — historical actuals still pending. Unblocked item 7 (pricing floor) from its revenue-target dependency — still needs more real OEOS offers. Captured the completion of OEOS offer #1 (full 44-deliverable manifest, QA, risk register, and a real 3-tier client-segmented pricing architecture). Added items 35 (confirm derived weekly/quarterly/yearly targets) and 36 (reconcile Offer #1's own ICP against Sector's real ICP). — Claude Code (Sonnet 4.6)
- 2026-06-30 — Owner introduced the Offer Engineering Operating System (OEOS) and the first OEOS-engineered offer (Revenue System Architecture, Sales Division, partial). Adopted a segmented pricing-floor methodology for item 7 (not yet computable — needs more OEOS offers + real revenue targets). Added item 34: real agency revenue targets (daily/weekly/monthly/quarterly/half-year/yearly), confirmed absent anywhere in the repo after a direct check. — Claude Code (Sonnet 4.6)
- 2026-06-30 — **Resolved items 15-18 (Content)**: department-boundary split confirmed, Project Realignment repositioning adopted, the 3-way pillar-naming conflict resolved by synthesizing all three sets into one canonical 7-pillar structure (rather than picking one), and LinkedIn/Instagram launch timing confirmed as not-yet-set. Tracker down to ~10 open items, all genuine owner-input gaps in Offer, Sales, Marketing, ClientPartner Acquisition, Client Success, Finance, and Branding. — Claude Code (Sonnet 4.6)
- 2026-06-30 — Tracker created, seeded with items surfaced during Offer and Sales content migration plus 5 agency-wide items from the governance-closure pass.
- 2026-06-30 — **Resolved item 0** (real sector, agency's #1 priority item) via direct owner input — see Resolved table. Added items 31-32 (Sector) for the now-partial chat-transcript source and the unreconciled intelligence-layer models. Updated item 7 (Offer pricing) to note the new 6th conflicting pricing source from Sector's real ICP database. — Claude Code (Sonnet 4.6)
- 2026-06-30 — Added items 25-27 (Finance) and 28-30 (Branding) as those departments' content migrations completed. — Claude Code (Sonnet 4.6)
- 2026-06-30 — Reconciliation pass: resolved items 19, 21, 22, 23 (cross-department boundary/model decisions) by direct architectural analysis now that all relevant departments are migrated — these turned out not to be owner-input items at all (no real fact was missing, just full-repo context), so moved to Resolved rather than left for the owner. Remaining open items are genuine owner-input gaps.
- 2026-06-30 — Resolved item 32 (Sector intelligence-layer model) by architectural reconciliation; deprioritized item 31 (chat export) as not blocking per owner direction.
- 2026-06-30 — Resolved items 5 (CRM=HubSpot), 6 (positioning confirmed), 12 (Kenya confirmed + global compliance scope) via direct owner input. Resolved item 11 (Sales risk-class mapping) by architectural reconciliation. Confirmed item 3's structure (solo ownership) — item 2's actual name still pending to fully close 2 and 3.
- 2026-06-30 — **Resolved items 2 and 3**: agency owner confirmed as Mary Thuo, sole owner across all 13 departments. Propagated her name to `AGENCY_OPERATING_CONSTITUTION.md`, `AGENCY_RACI.md`, `AGENCY_KPI_DICTIONARY.md` (Owner column, every metric), `GLOBAL_OS.md` §4, and every `{DEPT}_OS.md` header. Added confirmed contact info (domain `arikaagency.com`, `support@`/`growth@` addresses) to the constitution; flagged the owner's own email as a likely typo rather than silently correcting it (new item 33). Item 4 narrowed — only KPI thresholds remain unset now that owner/cadence are set. — Claude Code (Sonnet 4.6)
