# Legal — Department OS

**Department:** Legal (10)
**Position in flow:** Horizontal support layer — governs contracts, compliance, and risk across all other departments, reporting into Agency Governance (00).
**Mandate:** Own contracts (MSAs, SOWs), compliance, IP/copyright protection, and legal risk management for the agency and its client engagements.
**Owner:** Mary Thuo

> See [`GLOBAL_OS.md`](../GLOBAL_OS.md) for how this file fits into the whole system. Read that first if you haven't.

---

## 1. Identity

Legal is a **newly created department** — confirmed as a real gap during workspace exploration. Notably, the pre-existing `agency_workspace_completion_engine.py` script's hardcoded `WORKSPACES` dictionary already referenced a "Legal Drafts" workspace that **did not exist anywhere on disk** — independent confirmation, from the agency's own prior automation, that this gap was already known but never closed.

**It is the most-deferred-to department in the agency and the last one built** (2026-07-15). That ordering was deliberate: it has **zero inherited source material**, so there was nothing to diagnose — only demand to serve.

## 2. Status

**Built 2026-07-15: 7 template drafts, a research brief, and 2 agents. 🔴 NOTHING HERE HAS BEEN REVIEWED BY A LAWYER.**

*(This section previously read: "**Empty skeleton.** No raw draft archive exists for this department… no MSA, SOW, DPA/privacy policy, IP terms, or claims-substantiation policy exists anywhere in the repo as of v0.1." That was accurate until 2026-07-15 and is preserved here because it is the baseline this department was built from.)*

### What exists now

| Artifact | What it is |
|---|---|
| [`LEGAL_RESEARCH.md`](LEGAL_RESEARCH.md) | Kenya (DPA 2019, ODPC registration, s.48 transfers) + global (GDPR Art. 28, SCCs) desk research, **and the 8-item counsel brief** |
| [`templates/`](templates/) | **7 drafts**: MSA, SOW, DPA (+ sub-processor register), NDA (mutual + one-way), IP/Copyright/Trademark, Claims Substantiation, API & AI Tooling |
| §5 Agent Roster | `legal-exposure-register`, `legal-counsel-router` |

### 🔴 The standing caveat that governs this entire department

**Every document here was written by a language model, not an advocate.** They are **starting points for counsel review** — drafted to be genuinely usable, which is exactly what makes them dangerous. **A document that reads like a contract invites signature.**

**Nothing in `templates/` may be signed, sent, or relied on until a Kenyan-qualified advocate has reviewed it.** Each carries a banner; **the banner present means the review has not happened.** It is removed only when replaced by *"Reviewed by [NAME], [FIRM], [DATE]"* — and that fact is recorded in §8.

### ⚠️ A standing rule was consciously overridden

`CLAUDE.md` instructs: *"Do not invent agency-specific facts (numbers, client names, pricing, **legal terms**) when source material is missing — flag the gap instead."*

**Drafting these templates overrides that rule**, on the owner's explicit instruction of 2026-07-15 (§8). Recorded here, in §8, and in `GLOBAL_OS.md` §10 rather than left silent — **because the rule exists for good reasons, and a reader six months from now must know it was consciously set aside, not forgotten.**

## 3. Capability Registry — the Demand Register

**This department's only real source material is what other departments wrote about it.** Six live agents defer to Legal for decisions they cannot make. Those deferrals predate this department's existence and are the specification it was built against.

| Requester | What it needs from Legal | Served by |
|---|---|---|
| `ai-enablement-governance-gate` (17) | **AI governance framework legal/compliance review** — `Draft 40` Phase 10 makes it a **gate before any production AI deployment** | 🔴 **Nothing. No reviewer exists.** Blocks offer #11 entirely |
| `content-publishing-gate` (04) | Advertising-law exposure; *"not just off-brand"* | [`CLAIMS_SUBSTANTIATION_POLICY.md`](templates/CLAIMS_SUBSTANTIATION_POLICY.md) (unreviewed) |
| `clientpartner-trust-governor` (06) | Revenue-share terms → Legal + Finance; *"an unevidenced performance claim… is legal exposure"* | [`MSA.md`](templates/MSA.md), Claims policy (unreviewed) |
| `clientpartner-partner-enablement` (06) | Payouts, commissions, rev-share, agreements — **Class 3+** | [`MSA.md`](templates/MSA.md) (unreviewed); partner agreement **not drafted** |
| `client-success-offboarding` (07) | Involuntary offboarding — non-payment/breach — **Class 3/4** | [`MSA.md`](templates/MSA.md) Clauses 4.3–4.4 (unreviewed) |
| `sales-risk-trust-governance` (05) | Trust, compliance, ethics, legal exposure across sales | Claims policy, MSA (unreviewed) |

**Plus `00_Agency_Governance/AGENCY_RACI.md`**, which consults Legal on contracts and compliance agency-wide.

### Capabilities

| Capability | Status |
|---|---|
| Contract framework (MSA + SOW) | **Drafted, unreviewed.** Blocks the first client |
| Data protection (DPA + sub-processor register) | **Drafted, unreviewed.** Highest regulatory risk here |
| Confidentiality (NDA, mutual + one-way) | **Drafted, unreviewed** |
| IP / copyright / trademark | **Drafted, unreviewed.** Carries the unresolved **AI-copyright** question |
| Claims substantiation | **Drafted, unreviewed.** Class C performance claims **banned** — no engagements exist to substantiate one |
| AI/API tooling terms | **Drafted, unreviewed** |
| **AI-governance legal review** | 🔴 **Not possible.** No reviewer. Blocks 17 |
| **Entity structure** | 🔴 **Unresolved and deliberately un-researched** — `[ARIKA LEGAL ENTITY]` is a placeholder in every template |
| Partner agreement | **Not drafted.** 06 needs one |
| Privacy policy (public-facing) | **Not drafted.** Needed if the site collects anything |

## 4. Workflow Index

| Workflow | Trigger | Steps | Output | Owner |
|---|---|---|---|---|
| Weekly exposure check | Cron `53 7 * * 1` (`legal-exposure-register`) | Read template review state, transfer state, claims state → report what's blocked | `LEGAL_POSTURE_REPORTED` / `LEGAL_EXPOSURE_BLOCKING` | Mary Thuo |
| Counsel routing | `LEGAL_REVIEW_REQUESTED` (`legal-counsel-router`) | Classify the matter → does it need a lawyer? → is one named? → what's safe to proceed with meanwhile | `ROUTED_TO_COUNSEL` / `LEGAL_BLOCKED_NO_REVIEWER` / `NO_COUNSEL_NEEDED` | Mary Thuo |
| **Counsel engagement** | **Owner action** | `LEGAL_RESEARCH.md` §6's 8-item brief | Reviewed documents; a named reviewer | **Mary Thuo — nobody else can do this** |

## 5. Agent Roster

**2 agents, built 2026-07-15 — and neither does legal work.**

This department, like Consulting & Advisory (15), is one where the agents deliberately **do not perform the department's core function**. The reason is starker here: **Arika has no lawyer, and Claude is not one.** A confident wrong answer about a statute is worse than no answer, because a confident answer stops the referral.

| Agent | Class | Trigger → emits | Role |
|---|---|---|---|
| `legal-exposure-register` | 1 | weekly cron → `LEGAL_POSTURE_REPORTED` / `LEGAL_EXPOSURE_BLOCKING` | **Reports state, never interprets.** What's drafted vs. reviewed, what transfers happen with no basis, what's blocked |
| `legal-counsel-router` | 2 | `LEGAL_REVIEW_REQUESTED` → `ROUTED_TO_COUNSEL` / `LEGAL_BLOCKED_NO_REVIEWER` / `NO_COUNSEL_NEEDED` | Decides **whether** something needs a lawyer — never **what the lawyer would say** |

**The distinction both enforce, absolutely:**
- ✅ *"The DPA is drafted and unreviewed. It blocks the first client."* — **state**
- ❌ *"The DPA is adequate for GDPR."* — **an opinion neither agent may hold**

`legal-counsel-router`'s most useful field is **`can_arika_proceed_meanwhile`**, which separates **preparation from commitment**. Preparation is nearly always safe — there are no clients. Commitment nearly always needs the lawyer. Its honest default today is `blocked_no_reviewer`, because **no counsel is named**.

It also carries `owner_decision` as a verdict, for the class of open items **a lawyer cannot resolve**: whether the liability cap is commercially survivable, whether to accept uncapped data-protection liability, whether to register with the ODPC voluntarily, the FX basis. *A lawyer advises on consequences; the owner decides.*

## 6. Skill Library Index

*(none — the templates are the artifacts)*

## 7. KPI Dictionary (department-local)

**No KPIs are proposed, deliberately.** The obvious candidate — *"% of templates counsel-reviewed"* — would read **0%** and stay there until the owner engages a lawyer, which is not a metric, it is a single decision. Setting a threshold to measure one binary owner action would be theatre.

The real measures once counsel is engaged: **templates reviewed / total**, and **time from `LEGAL_REVIEW_REQUESTED` to counsel response**. Neither is meaningful before then.

## 8. Decision Log

- 2026-07-15 — **🔴 The owner explicitly overrode `CLAUDE.md`'s ban on inventing legal terms**, directing that full MSA, SOW, DPA, NDA, IP/copyright/trademark, claims, and API/AI-tooling language be drafted — *"full-on full language… for the agency itself as well as for real paying clients."* **Recorded rather than silent**, because the rule exists for good reasons. **Mitigation, applied to every document:** an unmissable unreviewed-draft banner; a `README.md` stating the review requirement; every open question surfaced as a counsel item rather than drafted around; **no document represented as sufficient.** — Claude Code (Opus 4.8)
- 2026-07-15 — **Agents report and route; they never advise** (owner-confirmed). Arika has no lawyer and Claude is not one. `legal-exposure-register` reports state; `legal-counsel-router` decides *whether* counsel is needed, never *what counsel would say*. **A confident wrong answer here is worse than none, because it stops the referral.** — Claude Code (Opus 4.8)
- 2026-07-15 — **Entity structure and tax deliberately NOT researched** (`LEGAL_RESEARCH.md` §7). Consequential, jurisdiction-specific, and desk research would be actively misleading. **`[ARIKA LEGAL ENTITY]` remains a placeholder in every template** — and it is load-bearing: a **sole proprietorship has no liability shield**, so `MSA.md`'s liability cap is contractual only, with personal assets behind it. **Resolve the entity before signing anything with a cap.** — Claude Code (Opus 4.8)
- 2026-07-15 — **Class C performance claims banned outright** (`CLAIMS_SUBSTANTIATION_POLICY.md` §3), not restricted. Arika has **zero delivered engagements**; there is nothing to substantiate a performance claim with. No case studies, testimonials, client logos, "typical results", or borrowed credibility. `ARIKA_WEBSITE_PROJECT.md`'s **intentionally empty Testimonials section** was this policy in practice before the policy existed — it stays. — Claude Code (Opus 4.8)
- 2026-06-30 — Department created as part of v0.1 skeleton restructuring, addressing a confirmed gap independently flagged by the agency's own prior automation. — Claude Code (Sonnet 4.6)

## 9. Risk / Incident Log

*(No incidents — no clients, no contracts, no engagements.)*

**This department's primary registry. The exposure list, ranked by what it blocks:**

| # | Exposure | Blocks | Severity today |
|---|---|---|---|
| 1 | **No counsel-reviewed contract set.** All 7 templates are Claude drafts | **The first client engagement.** §10's *"highest-priority gap"* | **Latent** — no clients yet |
| 2 | **🔴 No named AI-governance legal reviewer** | **`ai-enablement-governance-gate` (17)** → **offer #11 entirely**: highest setup ceiling in the catalog ($250,000+) and the **only path to Draft 28's $500K–$5M whale tier** | **Active** — 17 is wired and cannot deliver |
| 3 | **🔴 Personal data leaves Kenya daily with no documented s.48 basis** | Any client data entering any Arika tool | **Active but low-consequence** — no client data exists *yet* |
| 4 | **Sub-processor register incomplete** — every entry in `DPA.md` Annex B reads `[TO VERIFY]` | Any GDPR-covered client; **Arika is fully liable for all of them** | Latent |
| 5 | **`[ARIKA LEGAL ENTITY]` unresolved** | Every MSA with a liability cap | Latent |
| 6 | **AI-copyright position unresolved** | What Arika can honestly tell a client it owns | Latent — **but Arika already ships AI-generated assets** |
| 7 | **OpenArt Free-plan commercial terms unchecked** — imagery generated under it is **live on the Arika website** | Possibly already in breach | **Checkable today, free** |
| 8 | No partner agreement; no public privacy policy | 06's partner ecosystem; the website | Latent |

### The honest framing

**Arika has zero clients, so nearly all of this is latent, not on fire.** A register that cries `critical` when nothing is at risk gets ignored when something is.

**But the transition is fast.** The gap between *"they said yes"* and *"we need a signed MSA"* is days, and `legal-exposure-register`'s `pre_client_blocked` posture is the one that matters. **This window — zero clients, everything drafted, nothing signed — is the cheapest moment this department will ever have.** Exposure #2 is the exception: it is active now, and it is holding the agency's largest offer.

## 10. Standards & SOPs Index

*(Was: "no MSA, SOW, DPA, IP policy, or compliance procedure exists yet anywhere in the repo; highest-priority gap to close before onboarding any real client.")*

**Now drafted — all unreviewed.** See [`templates/README.md`](templates/README.md) first.

| Document | Covers | Highest risk if wrong |
|---|---|---|
| [`MSA.md`](templates/MSA.md) | The frame every engagement hangs on | Liability, IP, payment |
| [`SOW_TEMPLATE.md`](templates/SOW_TEMPLATE.md) | Scope, deliverables, price, timeline | Scope disputes |
| [`DPA.md`](templates/DPA.md) | Data processing + **sub-processor register** | **Regulatory** |
| [`NDA.md`](templates/NDA.md) | Mutual + one-way (ideas, campaigns, content) | Concepts taken to a cheaper executor |
| [`IP_COPYRIGHT_TRADEMARK_TERMS.md`](templates/IP_COPYRIGHT_TRADEMARK_TERMS.md) | Ownership; **AI-generated work**; marks | Client believes it owns what it may not |
| [`CLAIMS_SUBSTANTIATION_POLICY.md`](templates/CLAIMS_SUBSTANTIATION_POLICY.md) | What Arika may claim, on what evidence | Advertising-law exposure |
| [`API_AND_AI_TOOLING_TERMS.md`](templates/API_AND_AI_TOOLING_TERMS.md) | AI in delivery; disclosure; vendor terms | Vendor ToS breach |

**The gap §10 named is now half-closed: the documents exist; the review does not.**

## 11. RACI / Ownership

| Function | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| Contract framework (MSA/SOW) | Legal (10) | **Mary Thuo** | External counsel *(not engaged)*, Sales (05), Finance (09) | All departments |
| Data protection / DPA / transfers | Legal (10) | **Mary Thuo** | External counsel *(not engaged)*, Tech Stack (13) | All departments |
| **AI-governance legal review** | **🔴 Nobody** | **Mary Thuo** | External counsel *(not engaged)* | AI Enablement (17) |
| IP / copyright / trademark | Legal (10) | **Mary Thuo** | External counsel *(not engaged)*, Design (19), Branding (12) | All |
| Claims substantiation | Legal (10) | **Mary Thuo** | Sales (05), Content (04), Marketing (03) | All |
| Entity / tax | **🔴 Nobody** | **Mary Thuo** | External counsel + accountant *(neither engaged)* | Finance (09) |
| Counsel engagement | **Mary Thuo** | **Mary Thuo** | — | All |

**Every "Consulted" cell names counsel that does not exist.** That is the department's defining fact, stated in its own RACI rather than hidden.

## 12. Triggers / Automation Hooks

2 agents on `arika-runtime` (`GLOBAL_OS.md` §5): one weekly cron (`legal-exposure-register`, `53 7 * * 1`), one event-driven router.

**Known gaps:**

1. **`LEGAL_REVIEW_REQUESTED` has no emitter.** The six deferring agents (§3) name Legal in prose; none publishes the event. Routing is manual today. **Wiring those emits is real work available now** — it would turn six prose deferrals into a live queue.
2. **⚠️ The weekly cron is declared, not scheduled.** The runtime isn't booted as a daemon, and its **26 cron triggers still have 1 approval-matrix row between them** (`16_Automation/AUTOMATION_OS.md` §12).
3. **🔴 `ROUTED_TO_COUNSEL` has no destination.** No counsel is named, so the router's success path terminates in nothing. `LEGAL_BLOCKED_NO_REVIEWER` is the honest default. **This is the only department whose primary output has no recipient.**

## 13. Existing OS Sub-Layer

No department-local code. The 2 agents (§5) run on the shared `arika-runtime`; their memory stream is `10_Legal/_memory/runtime.jsonl`. The artifacts are `templates/` and `LEGAL_RESEARCH.md`.

## 14. Raw Archive Pointer

**None.** This is a genuinely new department with **no inherited backlog and no prior source content anywhere in the repo** — the only staffed department of which that is true. Everything here was created 2026-07-15 from: the six agents' deferrals (§3), public desk research (`LEGAL_RESEARCH.md`), and the owner's explicit instruction (§8).

The few "Legal" mentions elsewhere (Branding, Client Success, Sales raw drafts) are **generic explainers of business-entity types, not the agency's own legal infrastructure**.

## 15. Changelog

- 2026-07-15 — **Department built from nothing: 7 template drafts + a research brief + 2 agents.** The most-deferred-to department in the agency, and the last built — because it had **zero source material**, so there was nothing to diagnose, only demand to serve. **🔴 Nothing has been reviewed by a lawyer**; every template carries an unreviewed-draft banner that stays until a named advocate replaces it. **The owner explicitly overrode `CLAUDE.md`'s ban on inventing legal terms** (§8) — recorded, not silent. **Research produced a real finding** (`LEGAL_RESEARCH.md` §5): **Arika transfers personal data out of Kenya every day** — ClickUp, Zoho Books, Anthropic, Notion — **with no documented s.48 basis**, and s.48's safeguards are **contractual and pre-transfer**, so they cannot be applied retroactively. Also: **Arika's tool stack IS its sub-processor list** and had never been written down as one; **Anthropic sits on the critical path of nearly every offer**. ODPC registration researched — Arika is **probably exempt today** (sub-KES-5M turnover, <10 employees) but **one Scale-tier engagement crosses the threshold**. §7 KPIs deliberately **not proposed**: *"% of templates reviewed"* would read 0% and measures a single owner decision, not a process. — Claude Code (Opus 4.8)
- 2026-06-30 — Department created as part of v0.1 skeleton restructuring, addressing a confirmed gap independently flagged by the agency's own prior automation (`agency_workspace_completion_engine.py` referenced a "Legal Drafts" workspace that never existed). — Claude Code (Sonnet 4.6)

## 16. Memory / Feedback Loop / Cadence

**Memory.** Both agents (§5) write to `10_Legal/_memory/runtime.jsonl` in the runtime's bois-compatible JSONL envelope. **Empty.** Once counsel is engaged, this stream becomes the department's real value: **a dated record of what was routed to a lawyer, what came back, and what remains unreviewed** — the audit trail that `templates/README.md` requires before any document loses its banner.

**Feedback Loop.** One loop is real and one is broken, honestly:
- ✅ `legal-exposure-register` → `LEGAL_EXPOSURE_BLOCKING` → `legal-counsel-router` + `operations-state-monitor` (08). The agency's state monitor can now see legal blockers rather than inferring them.
- 🔴 `legal-counsel-router` → `ROUTED_TO_COUNSEL` → **nothing.** No counsel is named. **The department's primary output has no recipient** (§12). That is the single fact to fix.

**Cadence.** Weekly exposure check against the **Operational Calendar** (`00_Agency_Governance/AGENCY_REVENUE_TARGETS.md` §4). Routing is event-driven. But the honest cadence is different: **this department's clock is the first client.** Everything here is latent until then and urgent the moment a prospect says yes — which is why it was built now, with zero clients, rather than later.

**⚠️ The cron is declared, not scheduled** (§12) — the runtime isn't booted, so the exposure check runs only when a human runs it.
