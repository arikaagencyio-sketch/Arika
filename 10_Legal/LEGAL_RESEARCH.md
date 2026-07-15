# Legal Research — Kenya + Global

**Compiled:** 2026-07-15 by Claude Code (Opus 4.8), from public sources cited below.
**Status:** 🔴 **RESEARCH NOTES — NOT LEGAL ADVICE. NOT REVIEWED BY COUNSEL.**

> **Read this first.** This document is desk research by a language model, not a lawyer. It
> was compiled to tell Arika **what questions to take to counsel** and **what the templates
> in `templates/` are trying to satisfy**. It is not a compliance opinion, it may be
> incomplete, and law changes. **Nothing here should be relied on without a
> Kenyan-qualified advocate confirming it.**
>
> Arika has **zero clients** as of this date, so nothing here is yet urgent — which is
> precisely why it is the right moment to resolve it.

---

## 1. Why this document exists

`LEGAL_OS.md` §2 records the department as an **empty skeleton**: *"no MSA, SOW, DPA/privacy
policy, IP terms, or claims-substantiation policy exists anywhere in the repo."* §10 calls it
*"the highest-priority gap to close before onboarding any real client."*

Meanwhile **six live agents** across four departments defer to Legal (10) for decisions they
cannot make (see `LEGAL_OS.md` §3, the Demand Register), and **AI Enablement (17)'s entire
offer is blocked** at a governance gate whose required legal reviewer does not exist.

---

## 2. Arika's actual legal posture (facts, not inference)

| Fact | Source | Why it matters |
|---|---|---|
| Registered/trading base: **Kenya** | Zoho Books org `929138528`, country `KE`, currency **KES**, `13_Tech_Stack/TECHSTACK_OS.md` §3 | Kenya's Data Protection Act 2019 applies |
| **Solo operator** (Mary Thuo), no employees | `GLOBAL_OS.md`, `11_HR_People_Ops/HR_OS.md` | Directly relevant to the ODPC registration threshold (§3 below) |
| **Zero clients, zero revenue to date** | `AUDITS_DIAGNOSTICS_OS.md` §2 and every department OS | Turnover is below every threshold — today |
| Offers priced in **USD**, invoiced in **KES** | `00_Agency_Governance/CRM_SCHEMA.md` | A conversion calculator **has not been built**; FX terms need stating in the MSA |
| Confirmed ICP: **B2B SaaS**, 3-tier | `01_Sector/SECTOR_OS.md` | Clients likely sit in the **US/EU/UK** → GDPR/UK-GDPR reach Arika as a **processor** |
| Entire tool stack is **foreign SaaS** | `13_Tech_Stack/TECHSTACK_OS.md` §3 | **Arika already transfers data out of Kenya daily** — see §5 |
| **`arikaagency.com`** live mailboxes; registrar **unconfirmed** | `TECHSTACK_OS.md` §9 | Domain/IP ownership should be verifiable before it matters |

---

## 3. Kenya — Data Protection Act 2019 (DPA) and the ODPC

### 3.1 Registration: Arika is *probably* exempt today, and that is fragile

Per the **Data Protection (Registration of Data Controllers and Data Processors) Regulations
2021** and ODPC guidance:

- Entities with **annual turnover above KES 5,000,000 AND more than 10 employees** must
  register with the Office of the Data Protection Commissioner.
- Entities **below KES 5M and under 10 employees** are exempt — but must *"clearly identify
  that it falls within this category."*
- **Sector exceptions register regardless of size** — financial services, healthcare,
  telecommunications, among others.
- Certificates last **two years**; renewal is due **30 days before expiry**.
- The Act's baseline: **no person shall act as a data controller or data processor unless
  registered** with the Data Commissioner — the size test is the carve-out from that rule.

**Arika today:** 1 person, KES 0 turnover → almost certainly under both limbs.

**⚠️ Four reasons not to file this away:**
1. **The thresholds are conjunctive on their face ("and"), and that is exactly the kind of
   detail that is read differently in practice.** What happens at KES 6M with 1 employee is a
   question for counsel, not for a language model reading a guidance note. Arika's offers run
   to **$250,000+** (`02_Offer/OFFER_OS.md`) — **one Scale-tier engagement crosses KES 5M.**
2. **Sector exceptions may bite via clients.** Arika's ICP is B2B SaaS, but a SaaS client
   *in* fintech or healthtech may pull Arika's processing into a regulated orbit. Untested.
3. The exemption requires Arika to *clearly identify* it qualifies — i.e. **a positive,
   documented act**, not silence.
4. Registration is a **precondition to acting**, not a formality to catch up on later.

**→ Counsel question 1:** *Given a solo Kenyan agency with sub-KES-5M turnover today but
offers priced to exceed it in a single engagement, when exactly must Arika register, and
should it register voluntarily now?*

### 3.2 Section 48 — transfers out of Kenya

Transferring personal data outside Kenya is **prohibited unless** adequate safeguards exist.
Per s.48 and ODPC's *Guidance Note on Cross-border Data Transfers*:

- The controller/processor must give the Data Commissioner **proof of appropriate
  safeguards** *before* transfer — comparable data-protection law in the receiving
  jurisdiction, and/or **appropriate contractual clauses**.
- **Sensitive personal data** requires the data subject's **explicit consent** *in addition*
  to safeguards.
- Alternative bases: performance of a contract with the data subject; a contract in the data
  subject's interest; vital interests; **compelling legitimate interests**.

### 3.3 Kenya–EU adequacy

Kenya and the EU opened an **adequacy dialogue in May 2024** — the first on the African
continent — **still ongoing as of early 2026, not concluded.** If granted, EU→Kenya data
would flow without extra safeguards. **Do not plan around it. It does not exist yet.**

---

## 4. Global — where Arika is a *processor*, not a controller

For a US/EU/UK B2B SaaS client, **the client is the controller and Arika is the processor**.
That inverts the intuition: Arika's obligations are largely *contractual*, owed to the
client, and the client will hand Arika **their** DPA to sign.

### 4.1 GDPR Article 28(3) — the mandatory DPA content

A written contract must define: **subject matter · duration · nature and purpose · types of
personal data · categories of data subjects · the controller's rights and obligations.**

And it must impose these **eight processor obligations**:
1. Process **only on documented instructions** from the controller
2. Ensure **confidentiality** commitments from all authorized persons
3. Implement **Article 32** security measures
4. Respect the conditions for **engaging sub-processors** (prior written authorization)
5. **Assist** the controller in responding to data-subject rights requests
6. **Assist** with Articles 32–36 (security, breach notification, DPIAs)
7. **Delete or return** all personal data at the end of services — the DPA must say **which**
   and **by when**
8. Make available the information needed to **demonstrate compliance** and allow audits

### 4.2 Sub-processors — the finding that matters most for Arika

> **The same obligations must be imposed on every sub-processor by contract, and the
> processor remains fully liable for the sub-processor's performance.**

**🔴 Arika's tool stack IS a sub-processor list, and it has never been written down as one.**
From `13_Tech_Stack/TECHSTACK_OS.md` §3, every one of these would process client personal
data on Arika's behalf: **ClickUp** (the CRM — client contacts by definition), **Notion**,
**Zoho Books** (client billing data), **Anthropic/Claude** (whatever agents are fed),
**Canva**, **OpenArt**, **KIE.ai**, **Vercel**.

Under Art. 28 a client can **object to a sub-processor**. Arika cannot currently answer *"who
processes our data?"* with a list, and **Arika is fully liable for all of them.**

**→ Counsel question 2:** *Confirm the sub-processor register in `templates/DPA.md` Annex B is
complete and correctly characterized, and advise on each vendor's own transfer mechanism.*

### 4.3 Non-EEA processors and SCCs

An EEA-located processor needs a DPA. A **non-EEA** processor (Arika, in Kenya) generally
needs **a DPA *and* Standard Contractual Clauses**, unless an adequacy decision covers it —
and, per §3.3, **Kenya has none.**

**→ Counsel question 3:** *Which SCC module applies where an EU controller appoints a Kenyan
processor who onward-transfers to US sub-processors — and who signs what?*

---

## 5. 🔴 The finding this research produced

**Arika transfers personal data out of Kenya every single day, and has no s.48 basis
documented for any of it.**

Not hypothetically, and not once clients arrive — **now**. The moment a real name and email
enter ClickUp, personal data leaves Kenya for US infrastructure. The same is true of Zoho
Books (client billing), Notion, and every prompt sent to Anthropic.

This is not a client-facing risk yet, because there are no clients. **It becomes one on day
one of the first engagement**, and the safeguards s.48 requires are *contractual and
pre-transfer* — they cannot be applied retroactively to data already moved.

**→ Counsel question 4:** *What s.48 basis covers Arika's own use of foreign SaaS, and what
proof must be lodged with the Data Commissioner, before the first client's data is entered?*

---

## 6. The counsel brief — take exactly this

1. **Registration** (§3.1) — must Arika register now? Voluntarily? At what trigger?
2. **Sub-processor register** (§4.2) — is `DPA.md` Annex B complete and correct?
3. **SCCs** (§4.3) — which module for EU controller → Kenyan processor → US sub-processors?
4. **s.48 basis for Arika's own stack** (§5) — before the first client.
5. **Review every template in `templates/`** — all seven are unreviewed Claude drafts.
6. **AI-governance reviewer** — `17_AI_Enablement`'s Class 3 gate needs a **named** reviewer.
   Counsel, or an external firm, recorded by name. Until then that gate blocks and offer #11
   (setup ceiling **$250,000+**, the only path to Draft 28's **$500K–$5M** whale tier) cannot
   lawfully reach production.
7. **Entity** — is a sole proprietorship right, or is a limited company needed before signing
   MSAs with liability caps? *(Not researched here. Deliberately: it is an entity-structuring
   question with tax consequences, and desk research would be actively misleading.)*
8. **FX** — offers in USD, invoices in KES, **no conversion calculator built**
   (`CRM_SCHEMA.md`). Which rate, at what date, stated where in the MSA?

---

## 7. What was deliberately NOT researched

- **Entity structure / tax.** Consequential, jurisdiction-specific, and irresponsible to
  desk-research.
- **Employment law.** No employees; see `11_HR_People_Ops/HR_OS.md`.
- **Sector-specific regimes** (health, finance) — depends on clients that do not exist.
- **US state privacy law** (CCPA et al.) — reachable via clients, but speculative with zero
  clients. Revisit when a real client's jurisdiction is known.

---

## Sources

- [ODPC — Guidance Note on Registration of Data Controllers and Data Processors](https://www.odpc.go.ke/wp-content/uploads/2024/02/ODPC-Guidance-Note-on-Registration-of-Data-Controllers-and-Data-Processors.pdf)
- [ODPC — Data Protection (Registration of Data Controllers and Data Processors) Regulations, 2021 (Legal Notice No. 265)](https://www.odpc.go.ke/wp-content/uploads/2024/03/THE-DATA-PROTECTION-REGISTRATION-OF-DATA-CONTROLLERS-AND-DATA-PROCESSORS-REGULATIONS-2021.pdf)
- [ODPC — Guidance Note on Cross-border Data Transfers](https://www.odpc.go.ke/wp-content/uploads/2026/04/Guidance-Note-on-Cross-border-Data-Transfers.pdf)
- [ODPC — General Regulations, 2021](https://www.odpc.go.ke/wp-content/uploads/2024/03/THE-DATA-PROTECTION-GENERAL-REGULATIONS-2021-1.pdf)
- [ODPC — FAQs](https://www.odpc.go.ke/faqs/)
- [DLA Piper — Data Protection Laws of the World: Kenya](https://www.dlapiperdataprotection.com/index.html?t=law&c=KE)
- [DLA Piper — Transfer of personal data in Kenya](https://www.dlapiperdataprotection.com/?t=transfer&c=KE)
- [CMS — Transfer of Personal Data Outside Kenya](https://cms.law/en/ken/news-information/transfer-of-personal-data-outside-kenya)
- [Council of Europe — Regulation of Cross Border Data Transfers: Examples from Kenya](https://rm.coe.int/coe-on-data-transfers/1680a20d55)
- [Securiti — Kenya Data Protection Act 2019 Compliance Guide](https://securiti.ai/kenya-data-protection-act-dpa/)
- [Art. 28 GDPR — Processor (gdpr-info.eu)](https://gdpr-info.eu/art-28-gdpr/)
- [ICO — What needs to be included in the contract?](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/contracts-and-liabilities-between-controllers-and-processors-multi/what-needs-to-be-included-in-the-contract/)
