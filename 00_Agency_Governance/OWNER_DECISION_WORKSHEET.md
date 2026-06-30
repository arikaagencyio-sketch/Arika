# Owner Decision Worksheet

**Purpose:** This is the working companion to [`OWNER_INPUT_NEEDED.md`](OWNER_INPUT_NEEDED.md) — that file is the technical tracker (what's open, why, where it lives); this file is the action surface. Every still-open tracker item is below, sorted into two kinds:

- **[DECISION]** — there's nothing more to wait for. You have a real choice to make, and I've given you my actual recommendation, reasoned from what's already confirmed in this repo (`AGENCY_VISION.md`, `AGENCY_REVENUE_TARGETS.md`, the confirmed positioning/sector/offer catalog) — not a generic best-practice guess.
- **[WAITING ON DATA]** — there's genuinely nothing to decide yet. These resolve themselves once the agency has operated for a real period and produces real numbers. No recommendation is possible without inventing figures, which violates this repo's no-silent-invention rule. Listed here so you can see the gap, not so you can act on it today.

**How to use this:** for each [DECISION] item, write your call in the **Your decision** line — either agree with my recommendation, modify it, or override it entirely. You can write directly in this file, or just tell me in conversation and I'll fill it in. Once you've gone through it, tell me which ones to action and I'll update the real source files and close out `OWNER_INPUT_NEEDED.md` to match.

**Tally:** 18 open tracker items. 13 are [DECISION] (you can close these today). 5 are [WAITING ON DATA] (genuinely nothing to do yet, will resolve once the agency has real operating history).

---

## Quick wins (5 minutes, low-stakes)

### Item 31 — Sector's partial chat export
**The question:** Should we still try to get the full "Sider Fusion" chat export that produced the Tier 2/3 ICP material, or leave it as-is?
**My recommendation:** Leave it. You already made this call once (2026-06-30) — proceed with what's captured. Tier 1 (your primary, most-detailed ICP) is fully real and unaffected; only the Tier 2/3 deep-dives are partial. Not worth revisiting unless the export becomes trivially available.
**Your decision:** _______________________________________________

### Item 14 — Marketing's MCP/connector blueprint
**The question:** Is any of the 7 documented connector-class layers (the marketing automation/integration blueprint) actually wired up and in use, or is all of it still aspirational?
**My recommendation:** Given Finance's integrations turned out to be zero real connectors and you confirmed no payment platform is in use yet, I'd bet this is the same — entirely aspirational. But this is a 10-second factual answer only you can give (yes/no, or "X of the 7").
**Your decision:** _______________________________________________

### Item 10 — Sales' missing companion `.docx` files
**The question:** 11 files referenced in Sales' source registry (e.g. `HE SALES OS_2024.docx`) aren't anywhere in this repo. Do you have them somewhere else, or should we mark them confirmed-lost and move on?
**My recommendation:** Mark confirmed-absent and move on. Sales' citation system is otherwise solid (verified against what *is* present); these 11 are a minor completeness gap, not a trust problem. Only worth digging up if you happen to know exactly where they are.
**Your decision:** _______________________________________________

---

## Threshold/defaults decisions (pattern already set by Finance)

These four follow the exact precedent you already set for Finance (item 26/27): generic doctrine defaults stay in place until real operating data exists to calibrate against, rather than guessing real numbers prematurely. Flagging them so you can either rubber-stamp the same logic or override it department-by-department.

### Item 4 — Agency-wide KPI thresholds
**The question:** Every metric in `AGENCY_KPI_DICTIONARY.md` has an owner and cadence now, but no threshold (e.g., "alert if CAC > $X"). Set real thresholds now, or wait?
**My recommendation:** Same logic as Finance — keep `(unset)` for now. Setting real alert thresholds before the agency has run a single real month against the $1M target would be guessing, and a wrong threshold (false alarms or missed real problems) is worse than an honest "not yet measured." Revisit after the first full operating month.
**Your decision:** _______________________________________________

### Item 28 — Branding's 20 AI agents: wire to a real LLM?
**The question:** Same question as Finance's 7 agents, but for Branding's 20-agent roster — keep as structured prompts/routing metadata, or wire to a live LLM now?
**My recommendation:** Keep spec-only, matching the Finance decision exactly — and for the same reason: BOIS has never run against the agency's own real brand (see item 30 below), so there's no real data yet for live agents to reason over. Resolve item 30 first; revisit this once there's something real to point the agents at.
**Your decision:** _______________________________________________

### Item 29 — Branding's `BrandScoringEngine` thresholds
**The question:** Generic 70-78 default scoring thresholds — keep or calibrate?
**My recommendation:** Keep, same logic as item 4/26. No real BOIS run against a real client (including the agency itself) has happened yet — nothing to calibrate against.
**Your decision:** _______________________________________________

### Item 8 / Item 13 — Offer's and Marketing's historical conversion/margin/LTV/CAC figures
**The question:** Both KPI tables only have industry-benchmark template numbers, no agency actuals.
**My recommendation:** Same logic — these are **[WAITING ON DATA]**, not a decision, listed here only because they're the same pattern. Nothing to do until real deals close.
**Your decision:** *(no action needed yet)*

---

## Offer department — the bigger decisions

### Item 39 — Standardize the internal team-role roster?
**The question:** All 4 real offers (and the 7 synthesized ones, deliberately kept consistent with each other) use different team-role names. Pick one canonical roster, per-division rosters, or leave it per-offer?
**My recommendation:** **One canonical core roster, with division-specific specialist titles layered on top** — not full per-division or per-offer rosters. Concretely: every offer needs a Client Partner (relationship), Strategy Lead (audit/strategy), Implementation Lead (delivery coordination), QA Specialist, and Account Manager (retainer phase) — these 5 roles repeat in some form across every offer captured so far, real or synthesized. What varies legitimately is the *specialist* role doing the actual deliverable work (e.g. Automation Engineer for offer #6, Copywriter for offer #5, Partnership Manager for offer #8) — that's real variation, not inconsistency, and shouldn't be forced into one name. This is also the structure I already used by default across offers #5-11 (`OFFER_OS.md` §3), so adopting it formally doesn't require new work, just a decision to retrofit offers #1-4's rosters to match the same core-5 pattern when convenient.
**Your decision:** _______________________________________________

### Item 38 — Pricing segmentation variable: rep-count vs. ARR-band?
**The question:** Offer #1 segments pricing by rep count; offer #3 by ARR band. Which should the pricing-floor methodology standardize on?
**My recommendation:** **ARR-band as the primary, universal segmentation variable, with rep-count as a secondary modifier only for sales-team-delivery offers** (offers #1, #2, and similar). Reasoning: ARR-band applies cleanly to *every* offer in the catalog — Brand Positioning, AI Transformation, and Revenue Growth Advisory have no "rep count" to speak of, but every client has a revenue size. Rep-count is a real, useful secondary signal specifically where the offer's value scales with the client's sales-team size (offers #1/#2), but it can't be the agency-wide standard since 9 of 11 offers in the catalog have no natural rep-count axis at all. This also matches Sector's own real ICP, which is already ARR-banded (Tier 1/2/3).
**Your decision:** _______________________________________________

### Item 7 — Compute the first pricing-floor mean
**The question:** The segmented pricing-floor methodology is adopted but said to be "blocked on more real OEOS offers." With all 11 offers now captured (4 real, 7 synthesized), is it time to compute a first-draft floor, or keep waiting for purely real data?
**My recommendation:** **Compute a first-draft floor now, explicitly labeled as a mix of real and synthesized inputs**, rather than waiting indefinitely for more real offers that may not arrive soon. A clearly-flagged provisional floor (e.g., "Tier 1 SaaS, $1-10M ARR: floor ≈ $X, computed from N real + M synthesized data points") is more useful than no floor at all, as long as it's never mistaken for a fully-real number. Refine it each time a new real offer arrives. This only works if you're comfortable with that explicit real/synthesized blending — if not, it should stay genuinely blocked.
**Your decision:** _______________________________________________

### Item 37 — Approve the offer #2 synthesized completion (Phases 6-12)?
**The question:** Does the Claude-synthesized completion of Sales Enablement Systems hold up, or does it need revision?
**My recommendation:** Approve as-is, with one specific thing worth your eyes: the synthesized **Client Constraint System** (Phase 9 — the Ghost/Unrealistic/Micromanager/Doubter/Know-It-All/Quitter/Result Ghoster archetypes) was the first time any offer actually fulfilled that part of the OEOS prompt, real or synthesized — worth a read since it may be worth retrofitting into offers #1 and #3 too, which skipped it entirely in their real chat output.
**Your decision:** _______________________________________________

### Item 40 — Approve the offers #5-11 synthesized batch + the division-mapping question
**The question A:** Does the 7-offer synthesized batch (Brand Positioning through AI Transformation Systems) hold up?
**My recommendation A:** Approve as-is, but specifically sanity-check offer #5 (Brand Positioning Systems) — it's the only offer with no retainer in the source material at all, which I flagged rather than inventing one; worth confirming that's actually intentional and not a gap in the original master pricing document.

**The question B:** Draft 28's 7 "Divisions" (Sales, Marketing, Automation, Partner & Client Acquisition, Consulting & Advisory, Audits & Diagnostics, AI Enablement) don't map onto this repo's 13 real departments — should any of these become real departments?
**My recommendation B:** No — keep them as Offer-internal categories, not real departments, until team size actually requires a dedicated owner for any of them. Right now you're the sole owner across everything; a new department only earns its existence once there's a real reason to delegate ownership of that specific function. Automation, Consulting/Advisory, Audits/Diagnostics, and AI Enablement are coherent *offer groupings* today, not yet coherent *operating units*.
**Your decision (A):** _______________________________________________
**Your decision (B):** _______________________________________________

### Item 41 — Reconcile offer #8 (Strategic Partnership Infrastructure) against the ClientPartner Acquisition department
**The question:** Offer #8 and the ClientPartner Acquisition (06) department both cover partner/referral systems — do they conflict, and if so, who owns what?
**My recommendation:** Same split pattern already used elsewhere in this repo (Offer defines the *priced, packaged offering* sold to clients who want a partnership program built for them; ClientPartner Acquisition owns the agency's *own* partner pipeline for acquiring clients through referral). These are two different audiences for similar mechanics — offer #8 is something Arika Agency sells; ClientPartner Acquisition is how Arika Agency itself grows. Worth a direct skim of both files to confirm they don't actually contradict each other on the mechanics (e.g. commission ranges), but I don't expect a real conflict, just two legitimately separate uses of similar systems.
**Your decision:** _______________________________________________

---

## Build-now items (not blocked on data — these are real work I can do once you say go)

### Item 24 — Client Success offboarding/churn process
**The question:** This is confirmed to barely exist (an empty filename placeholder). Should I draft a real offboarding SOP now?
**My recommendation:** Yes — this is the same category of work as the offer completions: a real process design exercise, not a fact that needs to come from your operating history. I can draft a Claude-synthesized offboarding/churn SOP (exit triggers, asset handover, knowledge transfer, win-back logic) calibrated against Client Success's already-real 9-stage client journey model and the Constitution's risk-class framework, clearly labeled as synthesized for your review — same discipline as everything in the Offer catalog.
**Your decision:** _______________________________________________

### Item 30 — Define Arika Agency's own real brand for BOIS
**The question:** BOIS (the branding system) has only ever run against a hypothetical example client. Should I build it a real brand object for Arika Agency itself?
**My recommendation:** Yes, and unlike most remaining gaps, **this one is mostly buildable right now from facts already confirmed elsewhere in this repo** — not from scratch. We already have: the real name (Arika Agency), the confirmed positioning ("Revenue Infrastructure Partner"), the full vision/mission (`AGENCY_VISION.md`), the confirmed target client (B2B SaaS, Tier 1/2/3), and the operating philosophy (ROCBO, the "do-or-die" revenue framing). What's still missing and would need to come from you: visual identity preferences (if any exist yet) and voice/tone specifics beyond what's implicit in the existing positioning. I can assemble a first real brand object from what's confirmed and flag the visual/voice gaps explicitly, rather than waiting until every field is real before starting.
**Your decision:** _______________________________________________

---

## Genuinely waiting on data (nothing to decide — listed for visibility only)

| Item | What it's waiting on |
|---|---|
| 8 | Real historical conversion/margin/LTV figures (Offer) — needs closed deals |
| 9 | Real historical Sales KPI actuals — needs operating history against the now-real daily targets |
| 13 | Real Marketing KPI values — needs campaign history |
| 20 | Real ClientPartner Acquisition partner names/deals/revenue-share — needs actual partners (none yet, consistent with solo operation) |
| 31 | *(see Quick Wins above — already addressed)* |

These will close on their own as the agency operates. No action needed now; they're listed so the full picture is visible in one place.

---

## Changelog

- 2026-06-30 — Created at owner's request, as a working action-companion to `OWNER_INPUT_NEEDED.md`. Sorted all 18 open tracker items into [DECISION] (13 items, with reasoned recommendations) vs. [WAITING ON DATA] (5 items, no action possible). — Claude Code (Sonnet 4.6)
