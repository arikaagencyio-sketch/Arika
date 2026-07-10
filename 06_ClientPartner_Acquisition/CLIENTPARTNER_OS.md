# ClientPartner Acquisition — Department OS

**Department:** ClientPartner Acquisition (06)
**Position in flow:** Parallel acquisition channel alongside Marketing (03)/Content (04); feeds qualified opportunities into Sales (05), same as Marketing does.
**Mandate:** Own referral/partner-channel client acquisition — distinct from direct Marketing-driven demand generation — including its own CRM architecture and partner psychographics.
**Owner:** Mary Thuo

> See [`GLOBAL_OS.md`](../GLOBAL_OS.md) for how this file fits into the whole system. Read that first if you haven't.

---

## 1. Identity

ClientPartner Acquisition's **resolved mandate (reconciliation pass, 2026-06-30): the Partner pipeline only** — sourcing, qualifying, onboarding, managing, and expanding referral/distribution/affiliate partner relationships. It does not run a parallel client-acquisition or demand-generation system; that's Sales (05) and Marketing (03)/Content (04)'s mandate (see §10 for the full reconciliation). The department's own core distinction, stated repeatedly across its source material and the basis for this boundary: **"Client = Revenue Extraction Engine"** (you sell to them) vs. **"Partner = Distribution/Leverage Engine"** (you don't sell to them — you align incentives so they bring opportunities/access/scale). The single most-repeated principle in the corpus: *"The system MUST NEVER confuse [client vs. partner] logic."*

## 2. Status

**Content migration: first pass complete (2026-06-30).** All 12 remaining drafts read (4 had already been read during the earlier duplicate-resolution pass). No independently-built OS sub-layer. Like every other department, contains no real partner names, deals, or performance data — entirely generic/hypothetical. **One real structural finding worth acting on**: this department's CRM thinking (a full Partner Pipeline with 11 stages) has no analog anywhere in `00_Agency_Governance/CRM_SCHEMA.md`, which only tracks client-side objects — see §2 of that file for the fix made alongside this migration. **Also found**: this department's source material does not draw an operational boundary with Sales/Marketing the way the department's own OS framing assumes — see §10.

## 3. Capability Registry

**Primary to this department (Partner-track, no analog elsewhere):**

| Capability | Description | Status |
|---|---|---|
| Partner acquisition funnel engineering | 7-stage funnel (Identification → Attraction → Qualification → Alignment → Conversion → Enablement → Expansion) — explicitly "not a normal sales funnel" | Draft/aspirational (Draft 6) |
| Hybrid flywheel orchestration | 6-engine compounding system (Demand, Conversion, Delivery, Authority, Partner, Ecosystem) converting client outcomes into 5 reusable assets | Draft/aspirational (Draft 6) |
| Partner CRM architecture | Multi-pipeline model (Acquisition/Partner/Delivery), 6 CRM domains, 5-dimension lead scoring — basis for the Partner object added to `CRM_SCHEMA.md` | Draft/aspirational, most elaborate file in the department (Draft 13) |
| Client-vs-partner pathway segmentation | 3-layer Attraction → Capture/Segmentation → Warm-Up system splitting audience into Client (Demand Side) vs. Partner (Supply/Leverage Side) pathways before any pitch — the *partner-routing* logic specifically is this department's own | Draft/aspirational (Draft 7) |

**Superseded by neighboring departments (reconciled 2026-06-30 — see §10):** the raw material also contains a full parallel client-acquisition system that duplicates other departments' actual mandates. Kept here only as a cross-reference, not an active capability of this department:

| Capability | Description | Now owned by |
|---|---|---|
| Client acquisition system engineering | 5-layer Demand Generation → Capture → Qualification → Conversion → Feedback machine | Sales (05) — matches its citation-backed "Demand Generation," "Lead Qualification and Discovery," and "Sales Execution and Closing" agents |
| Client-offer-type mapping | Maps 7 client awareness/maturity types to offer structures | Offer (02) |
| Social-media-as-acquisition-infrastructure | 4-layer model (Attention/Authority/Relationship/Conversion) with parallel client-content track | Marketing (03) / Content (04) |

## 4. Workflow Index

| Workflow | Trigger | Steps | Output | Owner | Source |
|---|---|---|---|---|---|
| Partner sourcing | New partner category targeted | Classify into 6 partner categories (Distribution/Capability/Credibility/Strategic/Capital/Ecosystem), score against 7 fit criteria | Prioritized partner target list | Mary Thuo | Draft 6 |
| Partner attraction & qualification | Sourced partner identified | Build proof/authority assets first ("high-value partners are not acquired through begging") → score on Audience Fit/Revenue Potential/Operational Fit/Brand Alignment/Ecosystem Value (/10 each) | Qualified partner | Mary Thuo | Drafts 6, 9 |
| Partner onboarding/enablement | Partner qualified | Partner Toolkit (messaging, offers, case studies, scripts) + Partner Portal/CRM + training/reviews/support | Active, enabled partner | Mary Thuo | Draft 6 |
| Partner management/expansion | Active partnership | Co-branded campaigns, shared audiences, ecosystem integration; 4-tier partner ecosystem (Strategic core → Active distribution → Referral → Experimental) | Expanded partner network | Mary Thuo | Draft 6 |
| Client acquisition pipeline | New demand cycle | Demand Generation → Demand Capture → Qualification → Conversion → Feedback/Optimization | Converted client | Mary Thuo | Draft 5 |
| CP-AOS state machine | Any acquisition task | 12-state client lifecycle and 11-state partner lifecycle, run as separate runtimes that "MUST NEVER" be confused | Correctly-routed acquisition action | Mary Thuo | Drafts 8, 11 |

## 5. Agent Roster

*(placeholder — none yet)*

## 6. Skill Library Index

*(placeholder — none yet)*

## 7. KPI Dictionary (department-local)

**All values below are illustrative/draft, not validated against real performance** — same caveat as every other department.

| Metric | Formula | Draft value(s) found | Source | Owner | Cadence | Threshold |
|---|---|---|---|---|---|---|
| Client/Partner scoring threshold | Sum of /10 factors | 45+ priority, 30-44 nurture, <30 reject | Draft 6 | Mary Thuo | *(unset)* | *(unset)* |
| Partner revenue split (example) | % of deal value by partner role | Distribution Partner 20-40%, Fulfillment Operator 40-70%, Strategic Connector 10-20% | Draft 6, explicitly labeled "Example Split" | Mary Thuo | *(unset)* | *(unset)* |
| Trust degradation escalation | Probability threshold | Escalate if >40% | Draft 8 | Mary Thuo | *(unset)* | *(unset)* |
| Acquisition confidence escalation | Confidence threshold | Escalate if <85% | Draft 8 | Mary Thuo | *(unset)* | *(unset)* |
| Funnel/conversion metric categories | CPA, CPL, conversion rate, close rate, CAC, LTV:CAC | Named only, no benchmark values | Draft 5 | Mary Thuo | *(unset)* | *(unset)* |

## 8. Decision Log

- **2026-06-30 — Department mandate narrowed to Partner pipeline only.** Resolved the boundary with Sales (05) and Marketing (03)/Content (04): this department owns sourcing/qualifying/onboarding/managing partner relationships; it does not run a parallel client-acquisition system. See §1, §3, §10 for full reasoning. — Claude Code (Sonnet 4.6)

## 9. Risk / Incident Log

*(placeholder — empty)*

## 10. Standards & SOPs Index

**Recurring principles** (treat as working doctrine):
- "The system MUST NEVER confuse [client vs. partner] logic" — the single most-repeated rule in this department's source material (Draft 8).
- Partner funnels are "trust funnels," not sales funnels — partners risk their own reputation/audience by association, so credibility gates entry before pitching (Draft 6).
- CRM logs "MUST append, NEVER overwrite" (Drafts 8, 13).
- Trust Doctrine: "Trust MUST be earned before extraction... MUST NOT manipulate psychological vulnerabilities... every acquisition interaction MUST increase long-term trust position" (Draft 8).
- Client psychology is problem-driven (pain relief, speed, certainty, ROI clarity); Partner psychology is opportunity-driven (leverage, alignment, control retention, strategic upside) — pitching one as the other is named as a stated failure mode: *"pitch partners like clients → they disengage; treat clients like partners → they don't convert"* (Draft 4).

**Boundary reconciliation — resolved (2026-06-30), now that Sales, Marketing, and Content are all fully migrated.** The source material draws a strong *internal* boundary (client-track vs. partner-track within this department) but did **not** itself draw an operational boundary with Sales (05) or Marketing/Content (03/04) — Draft 5's "Client Acquisition System" includes a full "Conversion (Sales Engine)" layer naming sales call systems, close rates, and CRM tools; Draft 7 (audience-building) and Draft 9 (social media) substantially duplicate Marketing/Content territory.

**Resolution:** this department's active mandate is the **Partner pipeline only** (§1, §3). The client-acquisition-system content in Drafts 5/7/9 is read as an artifact of when this material was drafted before the repo split client-acquisition mechanics across dedicated departments (Sales for conversion, Marketing/Content for demand-gen) — not as a second, competing client-acquisition system this department should run. This is supported by Sales (05)'s own citation-backed Capability Registry, which already cross-references "Demand Generation... referral/partnership channels" to Marketing (03)/ClientPartner Acquisition (06) — i.e. Sales already expects partner-sourced opportunities to land in *its* conversion pipeline, consistent with `CRM_SCHEMA.md`'s Partner → sourced-Opportunity handoff (Partner sources the lead; Sales closes it). No content was deleted — the superseded capabilities remain visible in §3's cross-reference table for provenance.

## 11. RACI / Ownership

| Function | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| *(placeholder — `00_Workspace_Intelligence_Inventory/`'s own intent statement describes broader scope than this OS file currently reflects: "Convert partner, relationship, referral, and acquisition channel intelligence into governed pipeline leverage and CRM-backed relationship systems," with downstream deps listed as Sales, Partnerships, Distribution, Revenue channels, Client acquisition memory — wider than just "feeds Sales")* | | | | |

## 12. Triggers / Automation Hooks

Escalation triggers named in source material (Draft 8): trust degradation probability >40%, acquisition confidence <85%, reputation exposure detected, contractual ambiguity. All illustrative example thresholds within a meta-architecture template, not derived from real operating data — treat as a starting point for `00_Agency_Governance/AUTOMATION_APPROVAL_MATRIX.md` rows once real automation is built, not as live thresholds today.

## 13. Existing OS Sub-Layer

None yet.

## 14. Raw Archive Pointer

~12 root-level "Draft N.md" files. Existing gap backlog: `06_ClientPartner_Acquisition/00_Workspace_Intelligence_Inventory/`.

**Resolved (2026-06-30):** the 5-file near-duplicate cluster flagged during exploration was content-diffed:
- `Client Partner Acquisition System. Draft 10.md` was a byte-exact duplicate of `ClientPartner Acquisition System. Draft 2.md` (same system prompt, same CPAROS revenue-architecture output) — **deleted**, `Draft 2.md` retained as canonical.
- `Client Partner Acquisition. Draft 11.md` is genuinely distinct — a different framework (CP-AOS: a dual-agent Codex/Claude Code acquisition orchestration system), not a duplicate.
- `ClientPartner Acquisition. Draft 3.md` is genuinely distinct — a Q&A-style breakdown of client-vs-partner acquisition scope.
- `ClientPartner Aquisition. Draft 1.md` is genuinely distinct — a Q&A-style definitional/architecture walkthrough plus a partner-deal-vs-client-offer design framework.

No further dedup action needed on this cluster.

**Content migration completed (2026-06-30):** the remaining 8 unread files (`Building Pre- Acquisition Audience. Draft 7.md`, `Client Acquisition System Dynamics. Draft 5.md`, `ClientPartner Os Architure. Draft 8.md`, `ClientPartner Types.Draft 6.md`, `CRM System Architure. raft 13.md` [note filename typo, missing 'D' in "Draft"], `Psychographics in Client Acquisition. Draft 4.md`, `Social Media in Acquisition. Draft 9.md`, `Strategic Operational System. Draft 12.md`) were read in full and synthesized with the 4 previously-read files into the registries above. Drafts 8 and 12 are largely meta-architecture/system-prompt-design documents (how to prompt Claude Code/Coworker) rather than acquisition-specific content.

## 15. Changelog

- 2026-06-30 — File created as part of v0.1 skeleton restructuring (folder renamed from "The ClientPartner Draft").
- 2026-06-30 — Content migration: remaining 8 files read and synthesized. Capability Registry, Workflow Index, KPI Dictionary, Standards & SOPs Index, RACI, and Triggers/Automation Hooks populated. Found that this department's CRM thinking (a full Partner Pipeline) has no analog in `00_Agency_Governance/CRM_SCHEMA.md` — extended that file with a Partner entity/pipeline alongside this migration (see that file's own changelog). Documented, not resolved, an operational-boundary gap with Sales (05) and Marketing/Content (03/04) that the source material itself never draws.
- 2026-06-30 — Reconciliation pass: resolved the operational boundary with Sales (05) and Marketing/Content (03/04) flagged above, now that all three departments are migrated. Mandate narrowed to Partner pipeline only; client-acquisition-system content reclassified as cross-referenced/superseded rather than active capability. See §1, §3, §8, §10. — Claude Code (Sonnet 4.6)
- 2026-07-01 — Added §16 Memory/Feedback Loop/Cadence (structure-only placeholder, per the go-live plan in 00_Agency_Governance/GO_LIVE_CHECKLIST.md). — Claude Code (Sonnet 5)

## 16. Memory / Feedback Loop / Cadence

*(placeholder — structure only, no agent roster exists yet to generate real memory/feedback entries; see §5, which reads "placeholder — none yet.")* Once this department has a real or code-based agent roster (per the Tier 1 pattern in `05_Sales/SALES_OS.md` §16), this section should define: **Memory** (where Decision/Learning/Prompt-Evolution logs live), **Feedback Loop** (what happens when a §7 KPI misses threshold), and **Cadence** (which of the 7 Cognitive Calendars — `00_Agency_Governance/AGENCY_REVENUE_TARGETS.md` §4 — this department's workflows run against, and how often).
