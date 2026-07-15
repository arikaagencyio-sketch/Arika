# HR / People Ops — Department OS

**Department:** HR / People Ops (11)
**Position in flow:** Horizontal support layer — feeds capacity/staffing into Operations (08) and reports into Agency Governance (00).
**Mandate:** Own hiring, internal onboarding/training, role definitions, compensation, and capacity/utilization planning for the agency's people (distinct from client onboarding, which is owned by Client Success).
**Owner:** Mary Thuo

> See [`GLOBAL_OS.md`](../GLOBAL_OS.md) for how this file fits into the whole system. Read that first if you haven't.

---

## 1. Identity

HR / People Ops is a **newly created department** — confirmed as a real gap during workspace exploration. The agency's own prior self-analysis referenced "Hiring → Operations" as a dependency relationship, but no folder owned any actual role scorecards, hiring plan, onboarding/training content, or capacity model.

**Built 2026-07-15 from the owner's direct brief — and reframed by it.** This is **not a staffing function**, because there is no staff. It is **a doctrine and a trigger**: *what is this agency made of, when does that stop working, and what happens then?*

## 2. Status

**Built 2026-07-15: a People Doctrine, Kenya labour + payroll research, and 4 agents.**

*(This section previously read: "**Empty skeleton.** No raw draft archive exists for this department." True until 2026-07-15, and preserved as the baseline this was built from.)*

| Artifact | What it is |
|---|---|
| [`PEOPLE_DOCTRINE.md`](PEOPLE_DOCTRINE.md) | **The department's centre.** Solo+AI doctrine, the 5 rules, the real hiring map, self-pay, contractors, remote |
| [`HR_RESEARCH.md`](HR_RESEARCH.md) | Kenya Employment Act 2007 classification tests + **real 2026 payroll mechanics**, and the briefs for the two named roles |
| §5 Agent Roster | `hr-capacity-monitor`, `hr-role-architect`, `hr-engagement-classifier`, `hr-owner-sustainability` |

### The state, in four rows

| | |
|---|---|
| Headcount | **1** — Mary Thuo, solo, AI-assisted, remote |
| Employees / contractors / payroll | **0 / 0 / 0** |
| Clients / revenue to date | **0 / 0** |
| Revenue target | **$1,000,000/month · $35,000/day** — real, confirmed |

**The distance between the last two rows is this department's entire subject.**

> 🔴 **`HR_RESEARCH.md` is desk research by a language model, not counsel and not an accountant.** The statutory rates are real and cited; the judgements about how they apply to Arika are **questions, not answers**. Re-verify before acting.

## 3. Capability Registry

| Capability | Description | Status |
|---|---|---|
| **People doctrine** | What the agency is made of; when solo+AI stops working; the 5 rules | **Real, owner-sourced** ([`PEOPLE_DOCTRINE.md`](PEOPLE_DOCTRINE.md)) |
| **The hiring trigger** | 4 named triggers, watched against real commitments — never invented hours | Built (`hr-capacity-monitor`) |
| **Role scorecards** | Built from the offers' existing functional role labels (see below) | Built (`hr-role-architect`); **no role has ever been filled** |
| **Engagement classification** | Control / Integration / Substance tests before anyone is engaged | Built (`hr-engagement-classifier`); **never tested against a real arrangement** |
| **Owner as a resource** | Self-pay doctrine, the delegability ceiling, single points of failure | Built (`hr-owner-sustainability`) |
| **Employment contract** | — | 🔴 **Does not exist.** `10_Legal/templates/` has MSA/SOW/DPA/NDA and no employment contract |
| **Contractor agreement** | — | 🔴 **Does not exist.** Blocks the freelance work the owner intends |
| **Payroll machinery** | Registration, computation, remittance by the 9th | 🔴 **Nobody.** This is what the accountant is for |
| **Capacity model** | Hours, utilization, throughput | 🔴 **Does not exist and is not invented** (§9) |

**Cross-reference (2026-06-30, now load-bearing):** every offer's delivery roster uses **functional team-role labels** (Strategy Lead, Implementation Lead, QA Specialist, Client Partner, AI Governance Lead, Automation Engineer, Audit Analyst) describing **AI-assisted execution the owner performs solo — explicitly not real hires** (`02_Offer/OFFER_OS.md` §3; `OWNER_INPUT_NEEDED.md` item 39). *"When real staffing becomes relevant, those role labels are the natural starting point for role scorecards here, rather than starting from nothing."* **`hr-role-architect` is built to do exactly that** — its `derived_from` field should almost always name one.

## 4. Workflow Index

| Workflow | Trigger | Steps | Output | Owner |
|---|---|---|---|---|
| Weekly capacity check | Cron `11 8 * * 1` (`hr-capacity-monitor`) | Count real commitments → human-gate load → undelegable load → test the 4 triggers → affordability | `CAPACITY_SOLO_SUFFICIENT` / `HIRING_TRIGGER_MET` / `PERSON_BLOCKING_REVENUE` | Mary Thuo |
| Role definition | `HIRING_TRIGGER_MET` (`hr-role-architect`) | Derive from an offer's role label → **why a human?** → scorecard → real cost of engagement | `ROLE_DEFINED` / `ROLE_BLOCKED` | Mary Thuo |
| Engagement classification | `ROLE_DEFINED` (`hr-engagement-classifier`) | Control / Integration / Substance → misclassification risk → route to counsel | `ENGAGEMENT_CLASSIFIED` / `_BLOCKED` / `MISCLASSIFICATION_RISK_FLAGGED` | Mary Thuo |
| Monthly owner check | Cron `19 8 1 * *` + `REVENUE_RECEIVED` (`hr-owner-sustainability`) | Self-pay posture → delegability ceiling → single points of failure | `OWNER_SUSTAINABLE` / `SELF_PAY_DUE` / `OWNER_CEILING_REACHED` | Mary Thuo |
| **Engage the legal consultant + accountant** | **Owner action** | Briefs already written — `10_Legal/LEGAL_RESEARCH.md` §6, `HR_RESEARCH.md` §6 | Two engagements | **Mary Thuo — nobody else can** |

## 5. Agent Roster

**4 agents, built 2026-07-15.** They implement the doctrine; **none of them hires anyone.**

| Agent | Class | Trigger → emits | Role |
|---|---|---|---|
| `hr-capacity-monitor` | 1 | weekly cron · `DEAL_CLOSED_WON` → `CAPACITY_SOLO_SUFFICIENT` / `HIRING_TRIGGER_MET` / `PERSON_BLOCKING_REVENUE` | **The trigger.** Does solo+AI still work? Counts only what's real |
| `hr-role-architect` | 2 | `HIRING_TRIGGER_MET` → `ROLE_DEFINED` / `ROLE_BLOCKED` | Scorecard from the offers' own role labels. **Gate: why a human?** Real cost, never invented pay |
| `hr-engagement-classifier` | 2 **+ human-gated** | `ROLE_DEFINED` → `ENGAGEMENT_CLASSIFIED` / `_BLOCKED` / `MISCLASSIFICATION_RISK_FLAGGED` | **The misclassification gate.** Surfaces facts; routes to Legal; never opines on law |
| `hr-owner-sustainability` | 2 | monthly cron · **`REVENUE_RECEIVED`** → `OWNER_SUSTAINABLE` / `SELF_PAY_DUE` / `OWNER_CEILING_REACHED` | **The owner as a resource.** Self-pay doctrine, delegability ceiling, single points of failure |

### The four hiring triggers (`hr-capacity-monitor`)

1. **`undelegable_work_blocking`** — 🔴 **TRUE today.** No legal reviewer blocks `ai-enablement-governance-gate` (17), which blocks **offer #11 entirely** — the catalog's highest setup ceiling ($250,000+) and the only path to Draft 28's **$500K–$5M** whale tier.
2. **`human_gate_saturation`** — not yet (zero clients). **Arrives *with* the first client, not after.**
3. **`revenue_supports_it`** — revenue is **zero**. `PEOPLE_DOCTRINE.md` rule 1: *people are a consequence of revenue, not a route to it.*
4. **`statutory_obligation`** — engaging anyone creates dated, personally-liable payroll machinery. **This trigger fires the accountant, not the hire.**

### Boundaries

| Agent | Question |
|---|---|
| `operations-capacity-planner` (08) | *"Can we deliver **this engagement** without breaking the system?"* |
| `hr-capacity-monitor` (11) | *"Do we need **another human**?"* |
| **Finance (09)** | **The money** — treasury, cash flow, the actual payment |
| `hr-owner-sustainability` (11) | **The doctrine** — *should* the owner be paid, and what happens to capacity if not |

**HR owns the doctrine; Finance owns the money** (owner-confirmed 2026-07-15). `hr-owner-sustainability` never moves money and never sets a figure; it hands Finance the cash question via `what_finance_must_do`.

## 6. Skill Library Index

*(none — the doctrine and the research are the artifacts)*

## 7. KPI Dictionary (department-local)

**No KPIs are proposed, deliberately.** The placeholder previously suggested *"utilization rate, time-to-hire"*. Both are **uncomputable and would be dangerous to fake**:

- **Utilization** requires a capacity model. **None exists** (`08_Operations/OPERATIONS_CONSTITUTION.md` §7), and `operations-capacity-planner` names inventing one as *"the single most dangerous invention in this repo — it would authorize overselling against a fiction."* **HR inherits that ban** (`PEOPLE_DOCTRINE.md` §8).
- **Time-to-hire** requires hires. There have been none, ever.

The real measures, once they exist: **time from `HIRING_TRIGGER_MET` to engagement**, and **whether self-pay is live once revenue is collected**. Neither is meaningful today.

## 8. Decision Log

- 2026-07-15 — **HR reframed as doctrine + trigger, not a staffing function** (owner brief). *"It's more about having the doctrines and having a monitor for when exactly we are going to get into having those people in."* There is no staff to administer; the department's job is to know **what the agency is made of and when that stops working.** — Claude Code (Opus 4.8)
- 2026-07-15 — **Self-pay: HR owns the doctrine, Finance owns the money** (owner-confirmed). The owner named self-pay as HR's — *"self-pay, because it's actually part of it"* — and it is, as a **capacity** question: `AGENCY_REVENUE_TARGETS.md` already treats targets *"the same way payroll/bills/KPIs would be"*, so **the owner IS the payroll**. An unpaid owner **hides the business's real cost of operation from itself**, and every pricing floor computed on free founder labour is wrong. Finance (09) executes; HR states the requirement. — Claude Code (Opus 4.8)
- 2026-07-15 — **No salary bands, rates, or "approximate" pay figures** (owner-confirmed). Real Kenyan **statutory mechanics** are researched and cited (`HR_RESEARCH.md` §3) — what any gross salary actually costs, remittance deadlines, employee-vs-contractor difference. **Market pay for the named roles is `[TO RESEARCH AT HIRE]`**: Kenyan market data is thin and fast-moving, and an invented band about real people's pay is exactly what `CLAUDE.md` bans — **and it would get quoted back.** — Claude Code (Opus 4.8)
- 2026-07-15 — **The next two people are professional engagements, not hires** (`PEOPLE_DOCTRINE.md` §5, owner-named): a **legal consultant** and an **accountant**. Both are **§3 constraints, not capacity** — work the doctrine forbids an agent from doing, ever. Both carry **no ~7.5% employer add-on and no payroll machinery**, which is why they are reachable at **zero revenue** when an employee is not. **Both briefs are already written.** — Claude Code (Opus 4.8)
- 2026-06-30 — Added a cross-reference to the Offer department's functional team-role labels (resolves Offer's tracker item 39) — explicitly not real hires yet, but a usable starting point once the agency needs to staff beyond solo+AI operation. — Claude Code (Sonnet 4.6)
- 2026-06-30 — Department created as part of v0.1 skeleton restructuring, addressing a confirmed gap. — Claude Code (Sonnet 4.6)

## 9. Risk / Incident Log

*(No incidents — no people.)*

### Standing risks

| # | Risk | Detail |
|---|---|---|
| 1 | **🔴 The delegability ceiling does not improve with automation** | Most of the agency gets cheaper to deliver as the runtime improves. **Advisory content (15), AI-governance design (17), legal review (10), and every Class 3 gate never do.** **More agents raise the volume arriving at the ceiling, not the ceiling** — each new agent adds gates to the same calendar |
| 2 | **🔴 Single point of failure: everything** | Every Class 3 gate, all sales, all delivery, all advisory. *"I am the salesperson, execution person, all of that."* **`mitigation_possible` is the useful question** — some are solvable by engaging someone, some by **not selling something**, some not at all (they must be **priced and bounded** instead — `15_Consulting_Advisory` §9) |
| 3 | **🔴 The Integration Test on creative contractors** | The owner intends freelance photographers for marketing. **But Arika sells creative production** — a photographer producing assets inside a client deliverable is arguably **integral to the business**, not ancillary. **The fact pattern most likely to be reclassified.** Structure must survive the test; counsel must confirm the structure, not the label (`HR_RESEARCH.md` §2.2) |
| 4 | **Misclassification cost** | Back wages, notice, leave, **severance**, unremitted deductions, penalties. **KRA and labour inspectors can audit proactively** — not only a risk if someone sues |
| 5 | **Payroll machinery is personal liability** | Remittance **by the 9th, monthly**, plus annual returns. **The real cost of a first employee is not the salary — it is the machinery.** And with the **entity unresolved**, employer obligations are **personal** |
| 6 | **Cross-border is not "remote"** | Anyone outside Kenya = **international employment**: their law may apply, PE and withholding arise, and contractor status is decided by **their** law. **Likely, not theoretical** — specialist developers are exactly who gets engaged internationally |
| 7 | **No capacity model** | Permanent `model_gap_flag`. **Not invented** (§7) |

## 10. Standards & SOPs Index

*(Was: "placeholder — role scorecards, hiring process, internal onboarding/training, compensation framework")*

| Standard | Where | Status |
|---|---|---|
| **People doctrine** — the 5 rules | [`PEOPLE_DOCTRINE.md`](PEOPLE_DOCTRINE.md) §2 | **Real, owner-sourced** |
| **The hiring map** — where AI genuinely cannot reach | [`PEOPLE_DOCTRINE.md`](PEOPLE_DOCTRINE.md) §3 | Real — **derived from other departments' own documented bans** |
| **Self-pay doctrine** | [`PEOPLE_DOCTRINE.md`](PEOPLE_DOCTRINE.md) §4 | Doctrine set; **figure + mechanism open** (accountant) |
| **Contractor doctrine** | [`PEOPLE_DOCTRINE.md`](PEOPLE_DOCTRINE.md) §6 | Set; **agreement not drafted** |
| **Remote doctrine** | [`PEOPLE_DOCTRINE.md`](PEOPLE_DOCTRINE.md) §7 | Set; **cross-border blocked on counsel** |
| **Role scorecard method** | `hr-role-architect` | Built; never used |
| **Classification method** | `hr-engagement-classifier` | Built; never used |
| Employment contract · contractor agreement | — | 🔴 **Do not exist** |
| Internal onboarding/training | — | Not written. **No one to onboard** |
| Compensation framework | — | **Deliberately not invented** (§8) |

## 11. RACI / Ownership

| Function | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| People doctrine | HR (11) | **Mary Thuo** | — | All departments |
| Hiring trigger / capacity signal | HR (11) | **Mary Thuo** | Operations (08), Finance (09) | All |
| Role definition | HR (11) | **Mary Thuo** | The offer's owning department | Operations (08) |
| **Engagement classification** | HR (11) | **Mary Thuo** | **External counsel — ⚠️ NOT ENGAGED**, Legal (10) | Finance (09) |
| **Self-pay — doctrine** | HR (11) | **Mary Thuo** | **Accountant — ⚠️ NOT ENGAGED** | Finance (09) |
| **Self-pay — money** | **Finance (09)** | **Mary Thuo** | Accountant *(not engaged)* | HR (11) |
| **Payroll machinery** | **🔴 Nobody** | **Mary Thuo** | **Accountant — ⚠️ NOT ENGAGED** | Finance (09) |
| Engaging anyone | **Mary Thuo** | **Mary Thuo** | — | All |

**Every "Accountable" cell is one person. That is the department's subject, stated in its own RACI.**

## 12. Triggers / Automation Hooks

4 agents on `arika-runtime` (`GLOBAL_OS.md` §5): two crons (`hr-capacity-monitor` weekly `11 8 * * 1`; `hr-owner-sustainability` monthly `19 8 1 * *`) and event triggers.

**Two real cross-department wires:**
- **`DEAL_CLOSED_WON` → `hr-capacity-monitor`.** The first closed deal is when human-gate load stops being theoretical.
- **`REVENUE_RECEIVED` → `hr-owner-sustainability`.** **The first collected cash is when self-pay stops being a doctrine and becomes a decision.** *"Revenue closed is not cash collected"* — this triggers on **collected**. **The failure mode is not refusing to pay; it is never noticing the moment arrived.**

**Known gaps:**
1. **`CAPACITY_STRAIN_DETECTED` and `ROLE_DEFINITION_REQUESTED` have no emitter** — manual today.
2. **⚠️ Both crons are declared, not scheduled.** The runtime isn't booted as a daemon, and its **28 cron triggers still have 1 approval-matrix row between them** (`16_Automation/AUTOMATION_OS.md` §12).
3. **`ENGAGEMENT_CLASSIFIED` routes to `legal-counsel-router` (10), which returns `blocked_no_reviewer`** — no counsel is engaged. **The chain is honest and terminates in the owner's decision to engage one.**

## 13. Existing OS Sub-Layer

No department-local code. The 4 agents (§5) run on the shared `arika-runtime`; their memory stream is `11_HR_People_Ops/_memory/runtime.jsonl`. The artifacts are `PEOPLE_DOCTRINE.md` and `HR_RESEARCH.md`.

## 14. Raw Archive Pointer

**None.** No inherited backlog. Everything here was created 2026-07-15 from: the **owner's direct brief**; the **owner's verbatim framing** preserved in `AGENCY_REVENUE_TARGETS.md` and `operations-capacity-planner`; the **offers' functional role labels** (§3); other departments' **own documented delegability bans** (`PEOPLE_DOCTRINE.md` §3); and public desk research (`HR_RESEARCH.md`).

## 15. Changelog

- 2026-07-15 — **Department built: a People Doctrine, Kenya labour + payroll research, and 4 agents** — **and every department in the agency now has an agent roster.** Reframed by the owner's brief as **doctrine + trigger, not a staffing function**. **The doctrine's most valuable section (§3 of `PEOPLE_DOCTRINE.md`) was not derived here** — it was already proven, department by department, by their own source material: **advisory content (15) and AI-governance design (17) are undelegable by their own doctrine; legal review (10) is Responsible: nobody; every Class 3 gate is the same person.** Read as a hiring plan, it is more honest than any headcount forecast — and its shape is **seniority- and licence-bound, not volume-bound**, which is exactly why the owner's own named next two are a **legal consultant and an accountant**. **Real payroll mechanics researched and cited**: an employee costs **~7.5% above gross** (employer NSSF + Housing + SHIF) **plus remittance by the 9th, monthly, personally liable** — *the real cost of a first hire is not the salary, it is the machinery*. **🔴 The Integration Test flagged as Arika's specific risk**: the owner intends freelance photographers, but **Arika sells creative production**, so that work is arguably integral rather than ancillary — the fact pattern most likely to be reclassified. **Never choose contractor status because it is cheaper: the ~7.5% gap IS the motive the KRA looks for.** **Self-pay boundary set** (owner-confirmed): HR owns the doctrine, Finance the money. **The owner IS the payroll** — an unpaid owner hides the business's real cost from itself, and **a pricing floor that assumes free founder labour is not a floor**. **No salary bands invented** (owner-confirmed) — `[TO RESEARCH AT HIRE]`. **§7 KPIs deliberately not proposed**: utilization needs a capacity model that does not exist and must not be faked; time-to-hire needs hires. — Claude Code (Opus 4.8)
- 2026-06-30 — Added a cross-reference to the Offer department's functional team-role labels. — Claude Code (Sonnet 4.6)
- 2026-06-30 — Department created as part of v0.1 skeleton restructuring, addressing a confirmed gap. — Claude Code (Sonnet 4.6)

## 16. Memory / Feedback Loop / Cadence

**Memory.** All 4 agents (§5) write to `11_HR_People_Ops/_memory/runtime.jsonl`. **Empty.** What this stream will hold once it matters: **when the hiring trigger first fired and what was done about it**, and **when self-pay first became due**. Both are moments that are easy to pass without noticing, which is the whole reason the agents exist.

**Feedback Loop.** Three loops, honestly scoped:
- `hr-capacity-monitor` → `HIRING_TRIGGER_MET` → `hr-role-architect` → `hr-engagement-classifier` → **`legal-counsel-router` (10) → `blocked_no_reviewer`.** The chain runs end-to-end and **terminates in the owner engaging counsel.** That is not a broken loop; it is an accurate one.
- `hr-owner-sustainability` → `SELF_PAY_DUE` → **Finance (09)** (`finance-cashflow-agent`, `finance-treasury-agent`). The doctrine hands the money question to the department that owns money.
- `hr-capacity-monitor` → `operations-capacity-planner` (08). HR's *"do we need another human?"* informs 08's *"can we deliver this?"* — and **both refuse to invent a number.**

**Cadence.** Weekly capacity check and monthly owner check, against the **Operational Calendar** (`00_Agency_Governance/AGENCY_REVENUE_TARGETS.md` §4). But the honest cadence is **event-driven, not calendared**: this department's real clocks are **`DEAL_CLOSED_WON`** (human-gate load becomes real) and **`REVENUE_RECEIVED`** (self-pay becomes a decision). Everything here is doctrine waiting for those two events.

**⚠️ Both crons are declared, not scheduled** (§12) — the runtime isn't booted, so these run only when a human runs them.
