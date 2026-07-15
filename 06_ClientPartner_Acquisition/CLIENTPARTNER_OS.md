# ClientPartner Acquisition — Department OS

**Department:** ClientPartner Acquisition (06)
**Position in flow:** **Dual-scope.** *Client-facing (primary):* a delivery discipline — Arika designs and installs acquisition systems **for clients**, sold via Offer (02)/Sales (05) and delivered as an Operations (08) Project. *Agency-facing (secondary):* Arika's own Partner pipeline, feeding sourced Opportunities into Sales (05).
**Mandate:** Own **the acquisition discipline** — the engineering of how revenue relationships (clients) and leverage relationships (partners) are found, qualified, earned, and compounded — **for clients primarily, and for the agency secondarily (partner-only)**.
**Owner:** Mary Thuo

> See [`GLOBAL_OS.md`](../GLOBAL_OS.md) for how this file fits into the whole system. Read that first if you haven't.
> **Read [`CLIENTPARTNER_CONSTITUTION.md`](CLIENTPARTNER_CONSTITUTION.md) before doing any work in this department** — it carries the Trust Doctrine, the separation law, and the dual scope.

---

## 1. Identity

ClientPartner Acquisition is **the acquisition discipline**. The source names it **CPAROS** — the *Client & Partner Acquisition Revenue Operating System* (`Draft 2`) — and at its runtime layer **ClientPartnerOS** (`Draft 8`). Its founding claim:

> **"Acquisition is not a process — it is a revenue-producing system architecture composed of interconnected subsystems."** The system exists to transform **random outreach → institutional acquisition infrastructure.**

**Dual scope, weighted to clients (owner-confirmed, 2026-07-15 — see §8 and `CLIENTPARTNER_CONSTITUTION.md` §2):**

- **Client-facing — primary.** Arika designs, installs, and operates acquisition systems **for its clients**: their client-acquisition engine, partner ecosystem, CRM/pipeline, and psychographic/trust architecture. This is a **service line**. `Draft 2`'s own brief states the goal outright: *"Sell high-ticket acquisition systems. Structure agency service tiers. Monetize partnerships at scale."*
- **Agency-facing — secondary, and partner-only.** The same discipline pointed at Arika: sourcing, qualifying, enabling, and expanding Arika's **own** partners. **Arika's own client acquisition belongs to Sales (05) and Marketing (03)/Content (04), not here.**

The owner's own words in the source settle it (`Draft 13`, line 1): the CRM is *"what you get maybe from **a client's audit**… the deliverables that **you are actually giving the client**"*, required for *"client/partner acquisition **for self and any scope of sectors**."* **"For self and any scope of sectors"** is the dual scope, stated in the source.

**The core distinction — the department's supreme law**, repeated across the corpus: **"Client = Revenue Extraction Engine"** (you sell to them) vs. **"Partner = Distribution/Leverage Engine"** (you don't sell to them — you align incentives so they bring opportunities/access/scale). Hence: *"The system MUST NEVER confuse [client vs. partner] logic"* — the architecture requires **dual-runtime cognition**. *Clients = Fuel · Partners = Engines · Your system = Vehicle.*

## 2. Status

**Live on the runtime (2026-07-15) — 7 agents + a departmental constitution, advisory-first.**
See §5 (roster), §12 (trigger chain), and [`CLIENTPARTNER_CONSTITUTION.md`](CLIENTPARTNER_CONSTITUTION.md).
**The mandate was corrected on 2026-07-15** — this department is dual-scope (client-facing
primary, agency-partner secondary), not partner-only. See §8 for the full reversal and its
evidence. **Deepest raw archive in the repo: 10,809 lines across 13 drafts** — all read.

**Still true: nothing here is real yet.** Zero partners, zero engagements, zero
performance data. Every threshold in §7 and §12 is an illustrative draft example, never
validated. The `Partner` object is live in ClickUp with **zero rows**.

**Content migration: first pass complete (2026-06-30).** All 12 remaining drafts read (4 had already been read during the earlier duplicate-resolution pass). No independently-built OS sub-layer. Like every other department, contains no real partner names, deals, or performance data — entirely generic/hypothetical. **One real structural finding worth acting on**: this department's CRM thinking (a full Partner Pipeline with 11 stages) has no analog anywhere in `00_Agency_Governance/CRM_SCHEMA.md`, which only tracks client-side objects — see §2 of that file for the fix made alongside this migration. **Also found**: this department's source material does not draw an operational boundary with Sales/Marketing the way the department's own OS framing assumes — see §10.

## 3. Capability Registry

**Primary to this department (Partner-track, no analog elsewhere):**

| Capability | Description | Status |
|---|---|---|
| Partner acquisition funnel engineering | 7-stage funnel (Identification → Attraction → Qualification → Alignment → Conversion → Enablement → Expansion) — explicitly "not a normal sales funnel" | Draft/aspirational (Draft 6) |
| Hybrid flywheel orchestration | 6-engine compounding system (Demand, Conversion, Delivery, Authority, Partner, Ecosystem) converting client outcomes into 5 reusable assets | Draft/aspirational (Draft 6) |
| Partner CRM architecture | Multi-pipeline model (Acquisition/Partner/Delivery), 6 CRM domains, 5-dimension lead scoring — basis for the Partner object added to `CRM_SCHEMA.md` | Draft/aspirational, most elaborate file in the department (Draft 13) |
| Client-vs-partner pathway segmentation | 3-layer Attraction → Capture/Segmentation → Warm-Up system splitting audience into Client (Demand Side) vs. Partner (Supply/Leverage Side) pathways before any pitch — the *partner-routing* logic specifically is this department's own | Draft/aspirational (Draft 7) |

**🟢 UN-SUPERSEDED 2026-07-15 — reclassified as client-facing delivery doctrine.** The 2026-06-30 pass marked the capabilities below "superseded duplicates" of Sales/Marketing/Content. **That was a category error** (§8, §10): it read them as acquisition *for Arika*. They are acquisition **for a client** — the thing Arika sells. Marketing (03) markets Arika; this department builds acquisition systems for clients. Different customer, no overlap. These are now **primary, active capabilities**:

| Capability | Description | Status |
|---|---|---|
| Client acquisition system engineering | 5-layer Demand Generation → Capture → Qualification → Conversion → Feedback machine, with 5 control points and a client-sized execution stack | **Active — client-facing** (`Draft 5`, `Draft 1`); `clientpartner-acquisition-architect` |
| Client-offer-type mapping (COAA) | Maps 7 client awareness/maturity types to offer structures; "offers are risk structures"; offer ascension model | **Active — client-facing** (`Draft 6`); `clientpartner-acquisition-architect`. *Arika's own* offer engineering stays with Offer (02) |
| Acquisition diagnostic & intake | The 12-input client intake + friction diagnosis + readiness verdict | **Active — client-facing** (`Drafts 3`, `11`, `5`); `clientpartner-acquisition-diagnostic` |
| Client CRM architecture (as deliverable) | 22 entities, 6 domains, 3 pipelines, 5-domain lead scoring, append-only governance | **Active — client-facing** (`Draft 13`); `clientpartner-crm-architect`. *Arika's own* CRM is `00_Agency_Governance/CRM_SCHEMA.md` — Governance (00) owns it |
| CPAROS tiered acquisition offer system | 3-tier ladder (AFS / AGE / ADN) by client segment | **Structure active, pricing NOT adopted** (`Draft 2`) — registered in `02_Offer/OFFER_OS.md`; numbers are Claude-generated and illustrative (§7, Constitution §9.2) |
| Social-media-as-acquisition-infrastructure | 4-layer model (Attention/Authority/Relationship/Conversion), client vs partner split | **Folded into `clientpartner-acquisition-architect`'s demand-generation layer** for client-facing work (`Draft 9`). *Arika's own* social/platform work remains Marketing (03)/Content (04) |

**Genuinely owned elsewhere (unchanged):** Arika's **own** client acquisition → Sales (05) + Marketing (03)/Content (04). Arika's **own** offers/pricing → Offer (02). Delivery of a client acquisition project → Operations (08). Meta-architecture/prompt design (`Drafts 8`, `12`) → superseded by the real `arika-runtime` + `AGENCY_OPERATING_CONSTITUTION.md` + `GLOBAL_OS.md` (Constitution §9.6).

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

**7 runtime agents, live in `arika-runtime` (2026-07-15).** Specs at
`.claude/agents/clientpartner-*.md`. **Advisory-first** — they recommend and log; humans
act. All are governed by [`CLIENTPARTNER_CONSTITUTION.md`](CLIENTPARTNER_CONSTITUTION.md).

**Client-facing (primary scope) — the acquisition system Arika builds *for clients*:**

| Agent | Does | Class | Triggers | Emits |
|---|---|---|---|---|
| `clientpartner-acquisition-diagnostic` | The 12-input intake, friction diagnosis, readiness verdict, client-vs-partner confusion check | 2 | manual · `ACQUISITION_AUDIT_REQUESTED` · `PROJECT_IN_DELIVERY` | `ACQUISITION_DIAGNOSED`, `ACQUISITION_NOT_READY` |
| `clientpartner-acquisition-architect` | Designs the client's 5-layer acquisition engine, COAA offer mapping, control points, *their* stack | 2 | manual · `ACQUISITION_DIAGNOSED` | `ACQUISITION_SYSTEM_DESIGNED` |
| `clientpartner-crm-architect` | Designs the client's CRM — entities, 3 pipelines, 5-domain lead scoring, risk-classed automation hooks | 2 | manual · `ACQUISITION_SYSTEM_DESIGNED` · `CRM_DESIGN_REQUESTED` | `CRM_ARCHITECTURE_DESIGNED` |
| `clientpartner-partner-ecosystem-architect` | The 7-stage trust funnel, 6 categories, incentive shape, 4-tier ecosystem, flywheel diagnosis *(works both scopes)* | 2 | manual · `ACQUISITION_SYSTEM_DESIGNED` · `PARTNER_ECOSYSTEM_REQUESTED` | `PARTNER_ECOSYSTEM_DESIGNED` |

**Agency-facing (secondary scope) — Arika's own partner pipeline, partner-only:**

| Agent | Does | Class | Triggers | Emits |
|---|---|---|---|---|
| `clientpartner-partner-sourcing` | Scores candidates (5×/10 → 45+/30–44/<30) against the **live** CRM Partner pipeline; runs the Client→Partner bridge | 1 | manual · **`ADVOCACY_CAPTURED`** · `ICP_CLASSIFIED` · `PARTNER_ECOSYSTEM_DESIGNED` · Tue 09:00 | `PARTNER_QUALIFIED`, `PARTNER_REJECTED` |
| `clientpartner-partner-enablement` | Partner Toolkit, portal spec, success cadence, tiered expansion | 2 | manual · `PARTNER_QUALIFIED` · `PARTNER_ENABLEMENT_REQUESTED` | `PARTNER_ENABLED`, `PARTNER_ENABLEMENT_BLOCKED` |

**Cross-cutting governance:**

| Agent | Does | Class | Triggers | Emits |
|---|---|---|---|---|
| `clientpartner-trust-governor` | Enforces the 4-part Trust Doctrine + the separation law; gates every contractual/economic obligation | **3** — `requires_human_approval: true` | manual · `PARTNER_QUALIFIED` · `PARTNER_ECOSYSTEM_DESIGNED` · `ACQUISITION_SYSTEM_DESIGNED` · `TRUST_REVIEW_REQUESTED` | `TRUST_CLEARED`, `TRUST_VIOLATION`, `ACQUISITION_ESCALATED` |

**The Client→Partner bridge is wired to a real event.** `client-success-advocacy` (07)
emits `ADVOCACY_CAPTURED` on an advocacy-ready client (testimonials, case studies,
**referrals**). Two agents now listen: `clientpartner-partner-sourcing` (Partner
Leverage) and `content-intelligence-hub` (04) (Case Study → authority). That is `Draft 6`'s
*"every client must create 5 assets"* — **Revenue · Case Study · Referral Potential ·
Data/Insights · Partner Leverage** — running as real infrastructure, and it is the
department's own flywheel hinge: *"If a 'client' brings you more clients → they are
becoming a partner layer."*

**🔴 Deliberately NOT built — 4, with reasons:**
- **Agency client-acquisition agent** → Sales (05) + Marketing (03)/Content (04) own it. This is the **correct, surviving half** of the 2026-06-30 reconciliation (§8), now correctly scoped to the agency dimension only.
- **Offer/pricing agent for the CPAROS tiers** → Offer (02) owns offer engineering and pricing authority (`offer-orchestrator`, `offer-oeos-engineer`, `offer-pricing-floor-analyst`). Tiers registered there, not re-engineered here.
- **Delivery/PM agent for a client acquisition build** → Operations (08) owns delivery (`operations-delivery-scheduler`, `-risk`, `-qa`). 06 supplies the **methodology**; Operations runs the **Project**.
- **Meta-architecture / prompt-design agent** (`Drafts 8`, `12`) → **already built and running.** Draft 8 specified a 12-layer `/constitution /governance /agents /memory /runtime` architecture; that is now `arika-runtime/` + `AGENCY_OPERATING_CONSTITUTION.md` + `GLOBAL_OS.md` + the JSONL streams. It predicted this repo — don't rebuild it (Constitution §9.6).

**Psychographics (`Draft 4`) folded, not built as its own agent.** Client internal states
(Desperate/Aware/Strategic) live in `clientpartner-acquisition-diagnostic`; partner
drivers in `clientpartner-partner-ecosystem-architect`; and the **vulnerability models**
are policed by `clientpartner-trust-governor` under *"MUST NOT manipulate psychological
vulnerabilities"* (Constitution §4). Buyer psychology for **Arika's own** deals stays
with `sales-customer-psychology` (05).

## 6. Skill Library Index

*(placeholder — none yet; the 7 agents in §5 carry their doctrine inline, matching every
other migrated department. The shared law lives in `CLIENTPARTNER_CONSTITUTION.md`
rather than in a skill.)*

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

- **2026-07-15 — ⚠️ MANDATE CORRECTED: dual scope, weighted to clients.** Owner-confirmed. **Partially reverses the 2026-06-30 decision below.** This department is **not** partner-only; it is the **acquisition discipline**, delivered *for clients* (primary) and applied *to Arika's own partners* (secondary). Drafts 5/7/9 **un-superseded** and reclassified as client-facing delivery doctrine (§3).
  **Why the 2026-06-30 pass erred:** it searched for a boundary between 06 and Marketing/Sales, concluded *"the source material does not draw an operational boundary with Sales/Marketing"* (§10), and narrowed the department accordingly. It never found that boundary **because the boundary in the source is a different one — agency-self vs. client-delivery.** Reading every draft as acquisition *for Arika* made a client deliverable look like a duplicate of Arika's own marketing.
  **The evidence it missed, all owner-authored:**
  1. `Draft 13` line 1 — *"the CRM is what you get maybe from **a client's audit**… the deliverables that **you are actually giving the client**… client/partner acquisition **for self and any scope of sectors**."*
  2. `Draft 2` line 1 — *"…for a 360° growth agency operating across any industry"*; **FINAL GOAL: "Sell high-ticket acquisition systems. Structure agency service tiers."**
  3. `Draft 3` — a **12-question intake** asking a business to identify its own model (*"Agency / Consultancy / SaaS / Media / Holding…"*) and desired clients (*"NGOs / Governments / Creators / E-commerce"*). Arika knows what Arika is; its ICP is confirmed 3-tier B2B SaaS (Sector 01). **A client discovery instrument.**
  4. `Draft 5` — deploy stack **ClickFunnels / HubSpot / GoHighLevel / ActiveCampaign**; human layer *"content operator, media buyer, sales rep/closer, systems manager."* Arika runs ClickUp+Zoho+Notion and is **solo + AI**. `Draft 7`'s examples: *"NGO leaders building donor pipelines," "E-commerce brands stuck at fulfillment bottlenecks."* **Someone else's business.**
  **What survives unchanged:** the 2026-06-30 conclusion was **correct about the agency dimension** — Arika's own client acquisition *is* Sales (05) + Marketing (03)/Content (04)'s mandate. That rule is preserved verbatim as the agency-side scope (§1, Constitution §2.2). The error was applying an agency-scoped conclusion to the whole department. — Claude Code (Opus 4.8)
- **2026-07-15 — Departmental constitution created.** [`CLIENTPARTNER_CONSTITUTION.md`](CLIENTPARTNER_CONSTITUTION.md) — closes the `Constitution | Missing | **Critical**` gap the workspace inventory has carried since **2026-06-03**, which specified this exact artifact (`/constitution/trust_doctrine.md`). Codifies the Trust Doctrine, the separation law, dual-runtime cognition, the 12/11 state machines, authority/risk mapping, and 6 flagged gaps. Subordinate to the agency constitution. — Claude Code (Opus 4.8)
- **2026-07-15 — CPAROS tier pricing NOT adopted.** Owner-confirmed among 3 options. The AFS/AGE/ADN **structure** is registered in Offer (02); its numbers ($2K–$250K+ setup, $1K–$100K+ retainer, 2–10% rev share) and outcome projections (+100–2000% pipeline, 10–80% CAC reduction) are **Claude-generated and unvalidated** — same status as `Draft 6`'s explicitly labelled *"Example Split."* Pricing authority remains `offer-pricing-floor-analyst` (02). Per `CLAUDE.md`: do not invent pricing. — Claude Code (Opus 4.8)
- **2026-06-30 — Department mandate narrowed to Partner pipeline only.** Resolved the boundary with Sales (05) and Marketing (03)/Content (04): this department owns sourcing/qualifying/onboarding/managing partner relationships; it does not run a parallel client-acquisition system. See §1, §3, §10 for full reasoning. — Claude Code (Sonnet 4.6) — **⚠️ SUPERSEDED IN PART 2026-07-15 (above): correct for the agency scope, wrong as the whole-department mandate.**

## 9. Risk / Incident Log

*(placeholder — empty)*

## 10. Standards & SOPs Index

**Recurring principles** (treat as working doctrine):
- "The system MUST NEVER confuse [client vs. partner] logic" — the single most-repeated rule in this department's source material (Draft 8).
- Partner funnels are "trust funnels," not sales funnels — partners risk their own reputation/audience by association, so credibility gates entry before pitching (Draft 6).
- CRM logs "MUST append, NEVER overwrite" (Drafts 8, 13).
- Trust Doctrine: "Trust MUST be earned before extraction... MUST NOT manipulate psychological vulnerabilities... every acquisition interaction MUST increase long-term trust position" (Draft 8).
- Client psychology is problem-driven (pain relief, speed, certainty, ROI clarity); Partner psychology is opportunity-driven (leverage, alignment, control retention, strategic upside) — pitching one as the other is named as a stated failure mode: *"pitch partners like clients → they disengage; treat clients like partners → they don't convert"* (Draft 4).

**Boundary reconciliation — ⚠️ CORRECTED 2026-07-15. The passage below is retained for provenance; its resolution is superseded in part.**

> *Original (2026-06-30):* "The source material draws a strong *internal* boundary (client-track vs. partner-track within this department) but did **not** itself draw an operational boundary with Sales (05) or Marketing/Content (03/04) — Draft 5's 'Client Acquisition System' includes a full 'Conversion (Sales Engine)' layer naming sales call systems, close rates, and CRM tools; Draft 7 (audience-building) and Draft 9 (social media) substantially duplicate Marketing/Content territory. **Resolution:** this department's active mandate is the **Partner pipeline only**… the client-acquisition-system content in Drafts 5/7/9 is read as an artifact of when this material was drafted before the repo split client-acquisition mechanics across dedicated departments…"

**The observation was accurate. The inference was not.** The source genuinely never draws a 06-vs-Marketing boundary — **because that isn't the boundary it draws.** The boundary in the source is **agency-self vs. client-delivery** (`Draft 13`: *"for self and any scope of sectors"*). Drafts 5/7/9 aren't a competing client-acquisition system and aren't a dated artifact; they are **the deliverable** — the acquisition system Arika designs *for a client*. Marketing (03) markets **Arika**. This department builds acquisition systems **for clients**. Different customer, no overlap, no duplication. Full evidence in §8.

**What holds from the original resolution:** Sales (05)'s Capability Registry cross-referencing *"Demand Generation… referral/partnership channels"* to Marketing (03)/ClientPartner Acquisition (06), and `CRM_SCHEMA.md`'s **Partner → sourced-Opportunity** handoff (Partner sources the lead; Sales closes it). That remains exactly right — **for the agency-facing scope** (§1, Constitution §2.2). It was never the whole department.

**Current boundary set:**

| Question | Owner |
|---|---|
| How does **a client** acquire clients and partners? | **ClientPartner Acquisition (06)** — primary |
| How does **Arika** acquire partners? | **ClientPartner Acquisition (06)** — secondary |
| How does **Arika** acquire clients? | **Sales (05)** + **Marketing (03)**/**Content (04)** |
| What does Arika sell, and at what price? | **Offer (02)** |
| Who delivers a client's acquisition build? | **Operations (08)** (06 supplies the methodology) |

## 11. RACI / Ownership

Solo owner + AI. "Responsible" = the agent producing the recommendation; **Accountable is
always Mary Thuo** — advisory-first means no agent contacts a partner, quotes a price, or
writes to a client's system.

*(The inventory's intent statement — "Convert partner, relationship, referral, and
acquisition channel intelligence into governed pipeline leverage and CRM-backed
relationship systems," downstream to Sales, Partnerships, Distribution, Revenue channels,
Client acquisition memory — is now **matched** by §1's dual scope. The mismatch flagged
here on 2026-06-30 was a symptom of the narrowing corrected in §8.)*

| Function | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| Client acquisition diagnosis | `clientpartner-acquisition-diagnostic` | Mary Thuo | Sector (01) — ICP method; Operations (08) — the engagement | Client Success (07) |
| Client acquisition system design | `clientpartner-acquisition-architect` | Mary Thuo | Offer (02) — offer shapes; Marketing (03) — channel craft | Operations (08) |
| Client CRM design | `clientpartner-crm-architect` | Mary Thuo | Governance (00) — schema patterns; Tech Stack (13) | Operations (08) |
| Partner ecosystem design (both scopes) | `clientpartner-partner-ecosystem-architect` | Mary Thuo | Legal (10) + Finance (09) on any economics | Sales (05) |
| Arika's partner sourcing/scoring | `clientpartner-partner-sourcing` | Mary Thuo | Client Success (07) — the advocacy bridge; Sector (01) | Sales (05) |
| Arika's partner enablement | `clientpartner-partner-enablement` | Mary Thuo | Branding (12), Content (04), Sales (05) — toolkit assets; Operations (08) — capacity | Finance (09) |
| Trust & separation governance | `clientpartner-trust-governor` | Mary Thuo | Sales (05) risk/trust; Legal (10) | All of 06 |
| **Any contractual/economic term** | **Mary Thuo (human)** | Mary Thuo | **Legal (10) + Finance (09)** | — |
| **Pricing** | **Offer (02)** `offer-pricing-floor-analyst` | Mary Thuo | — | 06 |

## 12. Triggers / Automation Hooks

**The chain (all real, all wired):**

```
ACQUISITION_AUDIT_REQUESTED / PROJECT_IN_DELIVERY
        │
        ▼
clientpartner-acquisition-diagnostic ──→ ACQUISITION_DIAGNOSED
        │
        ▼
clientpartner-acquisition-architect ──→ ACQUISITION_SYSTEM_DESIGNED
        │                                        │
        ├────────────────┬───────────────────────┤
        ▼                ▼                       ▼
 crm-architect   partner-ecosystem-architect   trust-governor (Class 3)
                         │                       │
                         ▼                       ▼
                 PARTNER_ECOSYSTEM_DESIGNED   human sign-off

— agency-facing —
ADVOCACY_CAPTURED (07) ──┐
ICP_CLASSIFIED (01) ─────┼─→ clientpartner-partner-sourcing ─→ PARTNER_QUALIFIED
Tue 09:00 ───────────────┘                                          │
                                          ┌─────────────────────────┤
                                          ▼                         ▼
                        clientpartner-partner-enablement    trust-governor (Class 3)
                                          │
                                          └─→ Partner → sourced Opportunity → Sales (05)
```

**Scheduled:** `clientpartner-partner-sourcing` runs **Tuesdays 09:00** (`0 9 * * 2`) —
a weekly ecosystem sweep independent of upstream events, so the (currently total)
absence of partners surfaces on a cadence rather than by silence.

**Escalation triggers** (`Draft 8`, `Draft 11`), now enforced by
`clientpartner-trust-governor`: trust degradation **>40%** · acquisition confidence
**<85%** · reputation exposure detected · contractual ambiguity. **Still illustrative
example thresholds, not derived from real operating data** (Constitution §9.4) — they
fire escalations, but the numbers are not measured. They remain the starting point for
`00_Agency_Governance/AUTOMATION_APPROVAL_MATRIX.md` rows.

**No automation is live.** Every agent is advisory; the Class 3 governor requires human
sign-off by construction. No row in the approval matrix has been requested, because
nothing here takes an action.

## 13. Existing OS Sub-Layer

No department-local code. 06 runs on the shared `arika-runtime` substrate
(`arika-runtime/DESIGN.md`) plus [`CLIENTPARTNER_CONSTITUTION.md`](CLIENTPARTNER_CONSTITUTION.md)
as its departmental law, and drives one real external object: the **`Partner` entity in
ClickUp** (`00_Agency_Governance/CRM_SCHEMA.md`) — **live schema, zero rows**.

**Note (Constitution §9.6):** `Draft 8` specified a 12-layer AI-native operational
repository (`/constitution /governance /operations /agents /projects /context /memory
/playbooks /workflows /knowledge /logs /runtime`) with an instruction hierarchy,
execution state machine, and escalation doctrine. **That system now exists** —
`arika-runtime/` is the executor, `AGENCY_OPERATING_CONSTITUTION.md` the constitution,
`GLOBAL_OS.md` the hierarchy, the JSONL streams the memory. Draft 8 described the repo it
now lives in. Do not rebuild it as a sub-layer.

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
- 2026-07-15 — **Department revived on `arika-runtime`, and its mandate corrected.** Diagnosis first: all 13 drafts (**10,809 lines — the deepest archive in the repo**) + the workspace inventory + `CRM_SCHEMA.md` re-read against the owner's stated framing that 06 does client *and* partner acquisition **for clients**. Found §1's "Partner pipeline only" mandate to be a **category error** by the 2026-06-30 pass, which read every draft as acquisition *for Arika* and therefore marked a client deliverable a duplicate of Arika's own marketing — deleting a productized service line (`Draft 2`'s AFS/AGE/ADN ladder) in the process. Corrected to **dual scope, client-weighted** (§1, §8), preserving the old decision's correct half as the agency-side rule. **Un-superseded Drafts 5/7/9** as client-facing delivery doctrine (§3). Created [`CLIENTPARTNER_CONSTITUTION.md`](CLIENTPARTNER_CONSTITUTION.md), closing the inventory's `Constitution | Missing | Critical` gap open since **2026-06-03**. Built **7 agents** — client-facing `clientpartner-{acquisition-diagnostic, acquisition-architect, crm-architect, partner-ecosystem-architect}` (Class 2), agency-facing `clientpartner-{partner-sourcing (Class 1), partner-enablement (Class 2)}`, and `clientpartner-trust-governor` (**Class 3, human approval by construction**) — populating §5, §11, §12, §13, §16. **Wired the Client→Partner bridge**: `ADVOCACY_CAPTURED` from `client-success-advocacy` (07) now feeds both `clientpartner-partner-sourcing` (Partner Leverage) and `content-intelligence-hub` (04) (Case Study), making `Draft 6`'s *"every client must create 5 assets"* real infrastructure. 4 agents deliberately not built with reasons (§5); psychographics (`Draft 4`) folded rather than built; `Drafts 8`/`12`'s meta-architecture recognized as **already built** — it specified `arika-runtime` before `arika-runtime` existed (Constitution §9.6). CPAROS tier **structure** registered in Offer (02); its **pricing rejected as illustrative** (§8). 6 genuine gaps flagged, not filled (Constitution §9). Verified: `arika list` → **61 agents**, `npm test` → 8/8. — Claude Code (Opus 4.8)

## 16. Memory / Feedback Loop / Cadence

**Memory.** All 7 agents append to `06_ClientPartner_Acquisition/_memory/runtime.jsonl`
in the shared bois-compatible envelope (`arika-runtime/DESIGN.md`). **Append-only is
doctrine here, not just convention** — *"CRM logs MUST append, NEVER overwrite"*
(`Drafts 8`, `13`; Constitution §8), because institutional relationship memory is this
department's compounding asset:

> *"The CRM must remember every interaction, every objection, every stakeholder, every
> scope change, every promise… Without this, institutional intelligence collapses."*

This stream is the only evidence `operations-state-monitor` (08) can use to mark 06
`live` rather than `documented`. **It is empty until the first run.**

**Feedback loop.** §7's KPIs cannot miss a threshold — there are **no partners, no
engagements, and no performance data** (Constitution §9.5). The loops that *are* live:
- `clientpartner-partner-sourcing` reports `prerequisite_check` every agency-scope run — currently that Arika lacks the proof assets partner attraction requires, and that `Draft 3`'s **Phase 1 client-first → Phase 3 partner layering** sequencing says partner-building now would be the source's own named strategic mistake.
- `clientpartner-trust-governor` (Class 3) escalates on any doctrine breach or obligation, to a human, by construction.
- `clientpartner-partner-enablement` reports `asset_readiness: not_ready` while zero case studies exist.

**Cadence** (`00_Agency_Governance/AGENCY_REVENUE_TARGETS.md` §4 — the 7 Cognitive
Calendars):
- **Agency-facing** work runs against the **Opportunity Calendar** (the partner ecosystem is an opportunity register) and the **Strategic Calendar** — *"partner acquisition is slower but more compounding"* (Constitution §5), so it must not be judged on the Revenue Calendar's daily beat.
- **Client-facing** work runs against the engagement's own **Operational Calendar** via Operations (08)'s Project, not against an internal 06 cadence.
- The one hard beat: `clientpartner-partner-sourcing`, **Tuesdays 09:00**.

**A caution the flywheel demands.** `Draft 6`: *"Without outcomes: no referrals, no
retention, no authority, no partner attraction"* — **Delivery is the most important
engine.** This department's compounding therefore depends on Operations (08) and Client
Success (07) producing real outcomes first. 06 cannot bootstrap itself, and should not
pretend to.
