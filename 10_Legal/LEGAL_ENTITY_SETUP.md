# Legal Entity Setup — Arika Agency (First Operating Entity)

**Created:** 2026-07-19 · **Last updated:** 2026-08-09 · **Status:** 🔴 Pre-incorporation. **Neither entity exists yet.**
**Counsel engaged?** Not yet. **Sarah Ndwiga, Managing Partner, Ndwiga Law Advocates LLP** (Westlands, Nairobi; **Collins Wachira** assisting) has issued **two Letters of Engagement — v1 dated 29 July 2026 and v2 dated 6 August 2026. Neither is signed.**

**Engagement state — 2026-08-09: two letters received, decision pending.** Full cross-check in **[`COUNSEL_ENGAGEMENT_REVIEW.md`](COUNSEL_ENGAGEMENT_REVIEW.md)**; both letters preserved verbatim in [`_correspondence/`](_correspondence/).

**The short version:** the professional fee is **KES 185,000** in both letters (v1's stated total of 180,000 is an addition error — its own line items sum to 185,000). v2 additionally quantifies government charges at **KES 74,250**, for **KES 259,250** — *not* a fee increase. **But v2 also removed five things v1 had promised:** the two-phase trade-first structure, the **holding-company clause and the commitment to advise on sequencing between the two entities**, the eight operational matters and the promised separate estimate, **pre-incorporation marketing advice**, and the **instalment schedule**. It also downgraded the copyright work from *advice on what subsists in AI-assisted work* to *advice on how to file* — and changed the registrant from **the Company** to **Mary personally** (*"in your favour"*). **v1 addresses 7 of §6's 8 questions; v2 addresses 2.** The ask is v1's scope with v2's disbursement table.

🔴 **Two things are blocking and are not yet resolved by either letter:** **(1)** the holdco/IP-ownership question below (§4.1, §6 Q1) — **nothing should be filed at KIPI or KECOBO until it is closed**; and **(2)** Terms cl 4.4 excludes tax advice unless expressly agreed, and the IP-location question is substantially a tax question.

✅ **Two confirmations worth recording.** v1 §2.1.6 cites **COPTA/E001/2025** by name and unprompted, stating the human-authorship point correctly — **counsel has engaged with the case substantively.** It also relies on *"the version-controlled record of direction, specification and revision that you have indicated you can produce"* — **counsel has accepted this repository's commit history as the evidentiary record**, independently confirming §4.2 below. **Keep maintaining the decision logs and changelogs.**

*(Prior state, preserved: **2026-07-19 — instructing email SENT, awaiting reply.** Sent with `00 - Instruction Brief` attached. It corrected counsel's assumption of a co-shareholder (**Mary Thuo is sole owner**); asked whether the **holdco should be incorporated first** and **which entity holds the IP**; disclosed that the software is **predominantly AI-assisted and provider-agnostic**, citing **COPTA/E001/2025**, and asked what subsists before any copyright is registered; asked what falls inside the KES 180,000 versus the eight operational questions; asked for an **estimate of government charges**; and asked for a **phased instalment plan** plus confirmation of **what may lawfully be marketed before incorporation completes**. The letter of engagement was requested *reflecting that phasing*, not ahead of it. **v1 delivered nearly all of that. v2 withdrew most of it.**)*

> ⚠️ **This document is desk research, not legal advice.** Fees, timelines, and procedures below are from public sources (cited at the end) and were gathered to make the conversation with counsel informed and budgetable. **Every figure must be confirmed by counsel and against the live eCitizen/BRS invoice.** Nothing here is a substitute for Sarah's advice.

---

## 1. The starting position, stated plainly

| | |
|---|---|
| Holding company | **Does not exist.** Intended. |
| Arika Agency as a legal entity | **Does not exist.** No incorporation, no registration. |
| Current form | Unregistered. `[ARIKA LEGAL ENTITY]` is still a placeholder in all seven contract templates. |
| Ownership | **Mary Thuo, sole owner.** No partner, no co-founder, no shareholder — confirmed across `AGENCY_OPERATING_CONSTITUTION.md`, `AGENCY_RACI.md`, `AGENCY_KPI_DICTIONARY.md` (2026-06-30). |
| Clients / revenue | **Zero.** Pre-launch. |
| Owner's intent | **All IP ownership — not only trademark and copyright — to sit at holding-company level**, with the agency operating beneath it. |

**Everything below follows from one fact: nothing has been filed yet.** That is the most valuable position to be in, because sequencing is still free.

---

## 2. The agency-wide legal surface

A sweep of all 21 departments — not just `10_Legal` — for anything that creates a legal obligation. **These are gaps in the record, not accusations.**

### 🔴 Gaps that should be closed before or alongside incorporation

| # | Finding | Where | Why it matters |
|---|---|---|---|
| A | ~~Microsoft 365 unrecorded~~ → **RESOLVED 2026-07-19: Microsoft 365 was evaluated and rejected on cost** (owner-confirmed) — a per-seat monthly business subscription, not viable pre-revenue. **It must NOT be added to the inventory or to Annex B.** **🔴 But the underlying gap stands: three live mailboxes exist and their host is unidentified.** | `13_Tech_Stack/TECHSTACK_OS.md` §8–9 | A register naming a tool the agency doesn't use is as wrong as one omitting a tool it does. **Whatever serves `support@`, `growth@` and `mary.thuo@` holds the name and email of every client contact — that is a sub-processor and a cross-border transfer.** Identify it before the first client asks for the list. |
| B | **Sub-processor register is one row.** Annex B lists **ClickUp only**, with `[TO VERIFY]` in the Location and Transfer-mechanism columns. | `10_Legal/templates/DPA.md` | The real stack is ClickUp, Zoho Books, Notion, Anthropic, Microsoft 365, Vercel, Canva, OpenArt, Relume, KIE.ai. **Arika's tool stack *is* its sub-processor list.** |
| C | **Domain — partially resolved 2026-07-19 (owner-confirmed).** The **registrar account is held under an agency Gmail address**; the owner's intent is that **the agency owns the domain**, and counsel will supply the ownership framework. The specific registrar is still unnamed. | `13_Tech_Stack/TECHSTACK_OS.md` §9 | **The agency does not legally exist yet**, so the registrant of record is in practice a personal account. **Transferring it to the company is a Phase 1 action** (§5) — and doing it before value accrues is the cheap path, per §4.1. |
| D | **Speculative brand work appears in the counsel brief but nowhere in the OS.** The PDF proposes unsolicited redesigns of well-known brands to demonstrate capability. **Owner decision 2026-07-19: deferred pending counsel's response.** | `The First Entity.pdf` §15 | This is **third-party trademark use** — a real, publishable-risk activity with no policy behind it anywhere in the repo. **Until counsel replies, the safe default is that no speculative work using a third party's marks is published.** Not publishing costs nothing today; publishing and retracting does. |
| E | **Zoho Books org "Arika Agency" already exists** (org `929138528`, Kenya, KES), created 2026-06-26. | `13_Tech_Stack/TECHSTACK_OS.md` | Accounting records are being kept in the name of an entity **that does not legally exist yet**. On incorporation, confirm with the accountant which records belong to which entity from which date. |

### 🟡 Live now, already documented, unchanged by incorporation

- **Cross-border transfers** — the entire tool stack is foreign SaaS; personal data leaves Kenya daily with no documented s.48 basis (`LEGAL_RESEARCH.md` §5).
- **Seven unreviewed contract templates** — no lawyer has seen any of them (`templates/README.md`).
- **AI-governance reviewer** — none named, which blocks the highest-ceiling offer entirely (`17_AI_Enablement`).
- **Freelance contractors** — photographers intended for marketing, but Arika *sells* creative production, so the Integration Test bites (`11_HR_People_Ops/PEOPLE_DOCTRINE.md`).
- **Performance claims** — Class C claims banned outright; zero delivered engagements means nothing to substantiate them with (`templates/CLAIMS_SUBSTANTIATION_POLICY.md`).

### 🟢 Checked and clean

- **Partner revenue splits** are explicitly labelled *"Example Split"* and unset — **no partner commitments have been made** (`06_ClientPartner_Acquisition/CLIENTPARTNER_OS.md`).
- **Client Portal and Academy/Community** are Phase 2/3 roadmap only, deliberately unscoped — they will bring Terms of Service, privacy policy, and consumer obligations **when built, not now** (`20_Experience_Engineering/ARIKA_WEBSITE_PROJECT.md`).

### Commercial exposure the contracts must actually carry

Offers run **$7,500–$50,000 setup** with **$3,000–$25,000/month** retainers, rising to **$250,000+** on the largest. These are not small-agency numbers, and the MSA's liability cap is the only thing standing between an engagement going wrong and Mary's personal assets — **which is precisely why entity form comes before first signature.**

---

## 3. What each registration actually costs and takes

**All figures are public-source desk research (July 2026) and must be confirmed.** Government charges are *in addition* to counsel's KES 180,000.

| Step | Government cost | Timeline | Required to trade? |
|---|---|---|---|
| **Company incorporation** (BRS/eCitizen, private limited) | **~KES 10,650** registry fee. Stamp duty **1% of nominal share capital** on top. | BRS states 3–5 days; **realistically 5–10 working days, allow 2 weeks** | ✅ **Yes** |
| **KRA PIN** (company) | **Free** | Days | ✅ **Yes** |
| **County Single Business Permit** | **KES 5,000 – 50,000+** per year, varies by county and business size | Days–weeks | ✅ **Yes** — *"operating without a county business permit is illegal"*, and an online business with a physical presence still needs one |
| **Bank account** | Bank-dependent | Days–weeks | ✅ Practically yes |
| **ODPC registration** (data controller **and** processor) | **KES 4,000 per role** at the micro/small tier (turnover ≤ KES 5M). Certificate valid **24 months**; renewal KES 2,000 | Weeks | ⚠️ **Arika is currently exempt** — the exemption is turnover < KES 5M **and** fewer than 10 employees. Registering is a *choice*. |
| **KIPI trademark** | **~KES 13,000** for one class (search 2,000 + application 5,000 + registration 3,000 + publication 3,000). **~KES 25,000** for three classes | **8–18 months**; 18–24+ months if opposed | ❌ **No** |
| **KECOBO copyright registration** | **~KES 1,000 per work** | Weeks | ❌ **No — copyright arises automatically; registration is optional and evidentiary only** |

**Rough government-charge envelope for the trade-enabling set:** incorporation + stamp duty + permit ≈ **KES 20,000–65,000**, dominated by the county permit, which varies widely.

### 🔄 Reconciled against counsel's figures, 2026-08-09

The 6 August letter quotes disbursements for the first time. **Where counsel and this desk research disagree, counsel is the authority and the figures below are the ones to correct** — they are logged so they get asked, not so they get believed ([`COUNSEL_ENGAGEMENT_REVIEW.md`](COUNSEL_ENGAGEMENT_REVIEW.md) §4).

| Item | This research | Counsel (v2 §4.2) | Verdict |
|---|---|---|---|
| Incorporation registry fee | ~10,650 | **10,750** | ✅ Confirmed |
| ODPC, both roles | 8,000 (2 × 4,000) | **8,500** | ✅ Confirmed |
| KECOBO copyright | ~1,000 per work | **5,000**, stated as *"fixed"* | ❓ **Ask.** 5× gap |
| KIPI trademark, one class | ~13,000 | **50,000**, headed *"Costs per class"* | ❓ **Ask.** ~3.8×, and **the number of classes is stated nowhere in either letter.** Includes an undescribed **12,450** *"registry disbursements & costs & fast tracking"* line |
| Stamp duty on nominal capital | 1% of nominal capital | **Absent from v2's table entirely** | ❓ **Unknowable until capital is fixed** by §2.1.2 — so v2's *"all-inclusive"* figure cannot be complete |
| **County Single Business Permit** | **5,000–50,000+/yr, required to trade** | **Not mentioned in either letter** | 🔴 **Gap.** Neither letter's Phase 1 includes it, though this research lists it as required to trade lawfully |

**⚠️ Not in either letter's scope, and both are outside the KES 259,250:** the **county business permit** and the **bank account**. Phase 1 as scoped delivers incorporation + KRA PIN only. **Confirm with counsel whether the permit is genuinely required and who obtains it.**

---

## 4. 🔴 The three findings that change the sequence

### 4.1 Where the IP is first registered is the expensive decision

Mary's intent is that **all IP sits at holding-company level**. An IP holding company ring-fences the IP from the operating company's liabilities — that is exactly the point of the structure.

**But moving IP between entities later is not free.** Public sources on Kenyan practice identify: **capital gains tax at 5%** where the IP has appreciated since creation, **stamp duty** on a deed of assignment or licence, **withholding tax** on royalties once the operating company pays licence fees to the holder, and **transfer-pricing/arm's-length** requirements where a related non-resident entity is involved.

**Therefore: the holding company should exist before any IP is registered, and the IP should be registered in its name from the outset.** Registering the trademark to the operating company now and moving it later converts a free decision into a taxable one.

**🔄 Updated 2026-08-09 — still the single most important thing to settle before instructing, but the position has moved twice.** *(This paragraph previously read: "Sarah's reply does not say which entity will hold the IP, or mention the holding company at all.")*

- **v1 (29 July) §1.3 addressed it properly**: the holdco, the group structure, and IP ownership/licensing between holdco and Company are expressly **outside that letter**, with a written commitment to advise on them **and on the correct sequencing of incorporation between the two entities** once Mary supplies the information — *"under a separate letter of engagement or addendum."* **The ball is therefore in Mary's court on holdco information.**
- **v2 (6 August) deleted the clause entirely** and does not mention the holding company anywhere — while §2.1.6–2.1.7 commit to registering copyright and trademark **"in your favour"**, i.e. **to Mary personally**. That is **two** transfers away from the intended destination, not one.

**The tension that survives in both letters:** each incorporates the operating Company **first**, as Phase 1 priority, while the sequencing advice is still outstanding — so the advice arrives after the decision it governs has been executed. **The resolution is not to delay incorporation** (trading readiness is the priority and incorporation is not the problem) — **it is to decouple: incorporate now, and file nothing at KIPI or KECOBO until the holdco question closes.** v1's phasing already allows exactly that, since each Phase 2 stream is invoiced *"when you instruct us to commence it."* **v2 has no phasing, so nothing holds the filings back.**

**⚠️ And note Terms cl 4.4:** the firm's scope **excludes tax advice unless expressly agreed** — but the IP-location question is substantially a tax question. **It must be brought into scope in writing, or an accountant instructed alongside.**

*(The ongoing withholding tax on holdco→opco licence fees is a real running cost of the structure, and should be sized with the accountant before committing to it.)*

### 4.2 Kenya has ruled on AI-generated works — and it is directly on point

**_Aryeh Movement Limited v. Cynthia Beldina Akoth Okello_ (COPTA/E001/2025)** — the Kenya Copyright Tribunal held that **AI-generated works are not protected by copyright absent demonstrable human authorship and creative input.** The reasoning rests on **s.22(3) of the Copyright Act**, which requires that *"sufficient effort has been expended on making the work to give it an original character"* — a test the Tribunal read as presupposing human involvement. AI-assisted work qualifies **only where substantial human contribution shaping its original character can be shown.**

**This lands directly on Arika.** **45 of 46 commits in this repository are AI co-authored.** `arika-runtime`, the 106 agent specifications, the BOIS synthesis engine, and the seven legal templates were all produced by a language model working under Mary's direction.

**The point is provider-agnostic** — the ruling turns on *human contribution*, not on which model was used. It applies identically whether the tool is Claude, or any other LLM Arika adopts later.

**Two consequences:**
1. **Before paying to register copyright in the software**, Arika needs counsel's view on what subsists, who the author is, and what evidence is required.
2. **The mitigation is record-keeping, and it should start now** — direction given, specifications authored, review and correction applied, architectural decisions made. This repository's commit history, decision logs, and department changelogs are already a contemporaneous record of exactly that. **Its evidentiary value is a reason to keep maintaining it.**

### 4.3 Trademark is slow, so file early — but do not wait for it

**8–18 months.** It is not a blocker for trading, marketing, or signing clients, and it should not be allowed to hold up incorporation. But because the clock is long, the filing decision — which marks, which classes, which entity — should be made **early**, not after launch.

---

## 5. The phased plan

Sequenced so the agency can market and trade while the slower work proceeds in parallel — which is what the owner asked for.

### Phase 1 — Exist and be able to trade *(target: ~2–4 weeks)*
1. **Settle the structure**: holdco first, or opco first? Which entity holds IP? *(§4.1 — decide before filing)*
2. **Incorporate** — shareholding on a **sole-shareholder** basis.
3. **KRA PIN** → **bank account** → **county Single Business Permit**.
4. **Resolve `[ARIKA LEGAL ENTITY]`** in all seven templates.
5. **Assign the domain** and any other personally-held asset to the correct entity, *before* value accrues.

**At the end of Phase 1 Arika legally exists, can invoice, and can open a bank account.** It still cannot safely sign a client — that needs Phase 2.

### Phase 2 — Be able to sign a client safely *(parallel with Phase 1 where possible)*
6. **MSA + SOW reviewed** — the minimum signable pair.
7. **DPA + sub-processor register reviewed** — with the register actually completed (§2 gaps A and B).
8. **s.48 transfer basis** documented for Arika's own stack.
9. **FX terms** — USD pricing, KES invoicing, stated in the MSA.

### Phase 3 — Protect the asset base
10. **Trademark filing** — marks, classes, and **owning entity** (§4.1). Long clock: start early.
11. **Copyright position on AI-assisted works** (§4.2) — advice first, registration second.
12. **ODPC registration** — voluntary today; confirm trigger and whether to pre-register.

### Phase 4 — Unblock the largest offers
13. **Named AI-governance reviewer** — blocks the $250,000+ line entirely.
14. **SCCs** for EU/UK client chains.
15. Remaining templates: NDA, IP terms, AI tooling terms, claims policy.

**Trading needs Phase 1. Signing needs Phase 2. Everything else can run behind them.**

---

## 6. Open questions for counsel — scored against both letters (2026-08-09)

| # | Question | v1 (29 Jul) | v2 (6 Aug) |
|---|---|---|---|
| 1 | Holdco or opco first — and **which entity registers the IP**? | ⚠️ **Deferred, with a written commitment to advise** (§1.3) | 🔴 **Clause deleted. Not mentioned at all** |
| 2 | Sole shareholder: share structure and nominal capital *(stamp duty is 1% of it)*? | ✅ **Answered** — two classes, all held by Mary as sole shareholder, Class B reserved for future partners without later restructuring; capital to be sized *"having regard to the stamp duty"* (§2.1.1–2.1.2) | ⚠️ Structure stated, **reasoning, sole-shareholder confirmation and stamp-duty linkage all dropped** (§2.1.1–2.1.2) |
| 3 | AI-assisted works after **COPTA/E001/2025** — what subsists, and what records evidence it? | ✅ **Answered as a named deliverable, case cited** (§2.1.6) | 🔴 **Replaced with advice on the filing process** (§2.1.5) |
| 4 | Is KECOBO registration worth the fee, given it is optional and evidentiary? | ✅ **Asked explicitly**, and filing gated on the answer (§2.1.6–2.1.7) | 🔴 **Pre-answered by billing for an unconditional filing** (§2.1.6) |
| 5 | Estimated **government charges and disbursements**? | ⚠️ Deferred, honestly, until capital and classes are fixed (§4.3) | ✅ **Quantified at KES 74,250 — v2's genuine improvement** (§4.2) |
| 6 | **Instalment plan** against a phased timeline — pre-revenue, no clients | ✅ **Real schedule**: 50/50 on Phase 1; each Phase 2 stream invoiced on instruction (§5) | 🔴 **No payment terms whatsoever.** Reverts to Terms cl 8.1 / 9.2 — payments on account on demand, interim monthly bills |
| 7 | Which of the eight operational questions are inside the fee, and the marginal cost of the rest? | ✅ **Answered** — all eight named, scoped out, separate written estimate promised (§1.4, §2.3) | 🔴 **Silent** |
| 8 | Can Arika market itself online during Phase 1, and in what name? | ✅ **A named deliverable** (§2.1.4) | 🔴 **Service removed** |

**Scoreboard: v1 addresses 7 of 8. v2 addresses 2 of 8.** Question 1 is open in both and is the one that must close before any KIPI or KECOBO filing.

**The full question list to send counsel — 24 items, ordered by what they block — is in [`COUNSEL_ENGAGEMENT_REVIEW.md`](COUNSEL_ENGAGEMENT_REVIEW.md) §9**, together with the acceptance-reservation wording needed to keep clause 2.2 (*acceptance by continued communication*) from closing the negotiation early.

---

## Sources

Desk research, July 2026. **All figures to be confirmed by counsel and against live invoices.**

- [BRS Companies Registry — Fee Schedule](https://brs.go.ke/fee-schedule-companies-registry/) · [Cost of Company Registration in Kenya 2026](https://www.kazilegal.com/cost-of-company-registration-in-kenya.html) · [Company Registration 2026 — cost, requirements, timeline](https://www.bieastafrica.com/Kenya-company-registration.html)
- [KIPI Fees Schedules](https://www.kipi.go.ke/fees-schedules) · [Trade Mark Fees: Local and Foreign (PDF)](https://www.kipi.go.ke/sites/default/files/KIPI/Acts%20and%20Regulations/trade%20mark%20fees%20local%20and%20foreign.pdf) · [Trademark Registration in Kenya 2026](https://www.bizbrokerskenya.com/trademark.html)
- [Kenya Copyright Board](https://copyright.go.ke/) · [Copyright Act No. 12 of 2001 (PDF)](https://copyright.go.ke/sites/default/files/downloads/CopyrightAct12of2001.pdf) · [Copyrights Kenya FAQs — B M Musau & Co.](https://www.bmmusau.com/copyrights-kenya-faqs/)
- [CM Advocates — Copyright Tribunal affirms human-authorship requirement](https://cmadvocates.com/blog/the-copyright-tribunal-affirms-the-human-authorship-requirement-for-copyright-protection/) · [Kenya Tribunal rules AI works cannot be copyrighted — The EastAfrican](https://www.theeastafrican.co.ke/tea/business-tech/kenya-tribunal-rules-ai-works-cannot-be-copyrighted-5521436)
- [ODPC — Guidance Note on Registration (PDF)](https://www.odpc.go.ke/wp-content/uploads/2024/02/ODPC-Guidance-Note-on-Registration-of-Data-Controllers-and-Data-Processors.pdf) · [ODPC FAQs](https://www.odpc.go.ke/faqs/) · [ODPC registration — exemptions and mandatory requirements](https://datagovernance.africa/odpc-registration-in-kenya-understanding-exemptions-and-mandatory-requirements/)
- [Bowmans — Commercialization and monetization of IP rights in Kenya](https://bowmanslaw.com/insights/kenya-commercialization-and-monetization-of-intellectual-property-rights/) · [Tax implications of assigning and licensing IP in Kenya (IP holding companies)](https://www.mondaq.com/withholding-tax/1048562/tax-implications-of-assigning-and-licensing-intellectual-property-in-kenya-in-the-context-of-ip-holding-companies)
- [eRegulations Kenya — Obtain single business permit](https://eregulations.invest.go.ke/procedure/159/100?l=en) · [County business permit requirements and fees](https://hudumaglobal.com/blog/how-to-obtain-county-business-permit-kenya-requirements-fees)
