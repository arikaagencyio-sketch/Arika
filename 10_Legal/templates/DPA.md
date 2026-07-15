> # 🔴 UNREVIEWED DRAFT — NOT LEGAL ADVICE — HIGHEST-RISK DOCUMENT IN THIS FOLDER
> Written by Claude Code (Opus 4.8) on 2026-07-15. **No lawyer has seen this.**
> This document carries **regulatory** exposure, not just commercial: Kenya's Data Protection
> Act 2019 and, where applicable, the UK/EU GDPR. **A defective DPA is a regulatory problem,
> not a negotiation.** Do not sign or send until a Kenyan-qualified advocate — and, where an
> EU/UK client is involved, someone competent in GDPR — has reviewed it.
> See [`README.md`](README.md) and [`../LEGAL_RESEARCH.md`](../LEGAL_RESEARCH.md).
> Remove this banner only when replaced by: *Reviewed by [NAME], [FIRM], [DATE].*

---

# DATA PROCESSING AGREEMENT

**This Data Processing Agreement** (the "**DPA**") supplements the Master Services Agreement
dated `[MSA DATE]` (the "**MSA**") between **`[ARIKA LEGAL ENTITY]`** ("**Arika**", the
**Processor**) and **`[CLIENT LEGAL NAME]`** ("**Client**", the **Controller**).

Per **MSA Clause 1.3**, this DPA **takes precedence** over the MSA on any data-protection
matter.

## 1. Definitions

1.1 "**Data Protection Law**" means all applicable law on personal data, including Kenya's
**Data Protection Act 2019** (the "**Kenyan DPA**") and its Regulations, and where applicable
the **EU General Data Protection Regulation 2016/679** and the **UK GDPR**.

1.2 "**Personal Data**", "**Data Subject**", "**Controller**", "**Processor**", "**Processing**",
"**Sensitive Personal Data**" and "**Personal Data Breach**" have the meanings in Data Protection
Law.

1.3 "**Sub-processor**" means any third party engaged by Arika that Processes Client Personal
Data.

1.4 "**Client Personal Data**" means Personal Data Processed by Arika on the Client's behalf
under the MSA or a SOW.

## 2. Roles

2.1 The Client is the **Controller**. Arika is the **Processor**.

2.2 The Client warrants it has a lawful basis for the Processing it instructs, and that its
instructions comply with Data Protection Law.

2.3 The details required by **GDPR Article 28(3)** — subject matter, duration, nature and
purpose, types of Personal Data, categories of Data Subjects — are at **Annex A**. *Annex A is
part of this DPA and must be completed per engagement.*

## 3. Arika's obligations as Processor

Arika will:

3.1 **Process only on documented instructions** from the Client, including on transfers, unless
required otherwise by law — in which case Arika will notify the Client first, unless the law
prohibits it.

3.2 **Notify the Client** if, in its opinion, an instruction infringes Data Protection Law.
*Arika is not obliged to provide a legal opinion, and does not — see Clause 12.*

3.3 Ensure all persons authorized to Process Client Personal Data are **under a duty of
confidentiality**.

3.4 Implement **appropriate technical and organisational measures** (Annex C), per **GDPR
Article 32** and the Kenyan DPA's security obligations.

3.5 **Not engage a Sub-processor** except per Clause 5.

3.6 **Assist the Client**, taking into account the nature of Processing, in responding to
**Data Subject rights requests** (access, rectification, erasure, restriction, portability,
objection).

3.7 **Assist the Client** in complying with **GDPR Articles 32–36** — security, breach
notification, data protection impact assessments, prior consultation — and the Kenyan DPA
equivalents.

3.8 **Delete or return** all Client Personal Data at the end of the Services, at the Client's
election, and delete existing copies unless law requires retention. **The election is recorded
at Annex A §7; if not elected, Arika will delete.**

3.9 **Make available** the information necessary to demonstrate compliance with this DPA, and
allow and contribute to audits per Clause 8.

## 4. Personal Data Breach

4.1 Arika will notify the Client **without undue delay and in any event within `[24 / 48 / 72]`
hours** of becoming aware of a Personal Data Breach affecting Client Personal Data.

4.2 The notification will describe, so far as known: the nature of the breach; categories and
approximate numbers of Data Subjects and records; likely consequences; and measures taken or
proposed.

4.3 Arika will not make any public statement or notify any regulator or Data Subject about a
breach affecting Client Personal Data **without the Client's prior written consent**, unless
required by law.

> ⚠️ **Owner reality check.** This clause commits a **solo operator** to a `[24-72]`-hour
> notification window, **on a rolling basis, including holidays**. Arika has **no monitoring
> that would detect a breach at a sub-processor** — see `13_Tech_Stack/TECHSTACK_OS.md` §9,
> where the connection-verifier was built precisely because nothing was checking the stack.
> **Do not agree to 24 hours because a client asks. Agree to what is actually deliverable.**

## 5. Sub-processors

5.1 The Client **authorizes** the Sub-processors listed at **Annex B**.

5.2 Arika will notify the Client of any intended addition or replacement of a Sub-processor at
least `[14 / 30]` days in advance, giving the Client the opportunity to object **on reasonable
data-protection grounds**.

5.3 If the Client objects reasonably, the Parties will discuss in good faith. If no resolution
is reached, the Client may terminate the affected SOW without penalty for the unperformed part.

5.4 Arika will impose on each Sub-processor **the same data-protection obligations** as in this
DPA, by written contract.

5.5 **Arika remains fully liable to the Client for each Sub-processor's performance.**

> ### 🔴 Annex B is the most important page in this document. Read the note there.

## 6. International transfers

6.1 **Arika is established in Kenya.** Client Personal Data will be Processed in **Kenya** and
in the jurisdictions of the Sub-processors at **Annex B** — which include the **United States**
and other jurisdictions.

6.2 **Kenyan DPA — section 48.** Arika will not transfer Client Personal Data outside Kenya
unless the conditions of s.48 are met: **proof of appropriate safeguards** provided to the Data
Commissioner, and/or the receiving jurisdiction affords comparable protection, and/or another
lawful basis in s.48 applies. **Sensitive Personal Data will not be transferred out of Kenya
without the Data Subject's explicit consent**, in addition to safeguards.

6.3 **EU/UK transfers.** Where the Client is established in the EEA or UK, the Parties will
enter the applicable **Standard Contractual Clauses** / **UK International Data Transfer
Agreement** at **Annex D**. **Kenya is not the subject of an EU adequacy decision** — an
adequacy dialogue opened in May 2024 and, as at 2026-07-15, has not concluded.

6.4 Arika will assist the Client in documenting transfer risk assessments where required.

> ⚠️ **Counsel questions 3 and 4** (`LEGAL_RESEARCH.md` §6). The chain here is genuinely
> awkward and needs a real answer: **EU Controller → Kenyan Processor → US Sub-processors.**
> Which SCC module, who signs, and what does the Kenyan Data Commissioner need lodged? **This
> clause states an intention to comply. It does not, by itself, achieve compliance.**

## 7. Sensitive Personal Data

7.1 The Client will not instruct Processing of Sensitive Personal Data unless recorded at
**Annex A §4**, and warrants it has obtained any consent required — including the **explicit
consent** the Kenyan DPA requires for transfer of Sensitive Personal Data out of Kenya.

> **Default position: Arika should decline Sensitive Personal Data.** Arika's confirmed ICP is
> **B2B SaaS** (`01_Sector/SECTOR_OS.md`) — business contact data, not health, biometric, or
> financial-account data. **If a SOW would involve Sensitive Personal Data, that is an
> escalation, not a checkbox**, and it may pull Arika into a sector that must register with the
> ODPC regardless of size (`LEGAL_RESEARCH.md` §3.1).

## 8. Audit

8.1 Arika will make available information necessary to demonstrate compliance, and allow audits
by the Client or its mandated auditor on `[30]` days' notice, no more than `[once]` per year
unless required by a regulator or following a Personal Data Breach.

8.2 Audits will be during business hours, subject to confidentiality, and conducted so as not to
disrupt Arika's business.

8.3 The Client bears its own audit costs. `[Arika's reasonable costs of assisting beyond [N]
hours are chargeable.]`

## 9. Liability

9.1 **MSA Clause 9** applies.

> ⚠️ **Counsel.** Regulatory fines are frequently carved **out** of contractual liability caps,
> and clients often push for uncapped liability on data protection. **Whether Arika can survive
> uncapped data-protection liability is an owner decision that must be made before signing, not
> during a negotiation** — and it interacts with **counsel question 7** (entity structure): a
> sole proprietorship puts personal assets behind any uncapped exposure.

## 10. Term

10.1 This DPA runs for as long as Arika Processes Client Personal Data, and survives the MSA's
termination to that extent.

## 11. Governing law

11.1 As **MSA Clause 13**, unless Data Protection Law requires otherwise.

## 12. Not legal advice

12.1 Nothing in this DPA, and no assistance given under Clauses 3.2, 3.6, 3.7 or 6.4,
constitutes legal advice. **Arika is not a law firm and does not provide legal or regulatory
opinions.** The Client remains responsible for its own compliance as Controller.

---

# ANNEX A — Details of Processing (GDPR Art. 28(3))

*Complete per engagement. Attach to the SOW.*

| | |
|---|---|
| **1. Subject matter** | `[e.g. Revenue infrastructure audit of the Client's CRM and funnel]` |
| **2. Duration** | `[e.g. the term of SOW-2026-01, plus 30 days for return/deletion]` |
| **3. Nature and purpose** | `[e.g. Read-only analysis of CRM records to identify process gaps. No profiling. No automated decision-making with legal effects.]` |
| **4. Types of Personal Data** | `[e.g. business contact data: name, work email, job title, company. NO Sensitive Personal Data.]` |
| **5. Categories of Data Subjects** | `[e.g. the Client's leads, customers, and employees whose records appear in the systems audited]` |
| **6. Controller obligations/rights** | `[per this DPA and the MSA]` |
| **7. End-of-services election** | `[DELETE / RETURN]` — *if not elected, Arika deletes (Clause 3.8)* |

---

# ANNEX B — Authorized Sub-processors

> ## 🔴 THE FINDING. Read this before completing the table.
>
> **Arika's tool stack IS its sub-processor list, and it had never been written down as one
> until 2026-07-15.**
>
> Under **GDPR Article 28**, every third party that Processes Client Personal Data on Arika's
> behalf is a Sub-processor. The Client can **object** to any of them. Arika is **fully liable
> for all of them** (Clause 5.5). And each one that sits outside Kenya is a **s.48 transfer**.
>
> Every tool below is drawn from `13_Tech_Stack/TECHSTACK_OS.md` §3. **The moment a real client
> name and email enter ClickUp, personal data leaves Kenya for US infrastructure.** That is true
> today, and Arika has **no documented s.48 basis for any of it** (`LEGAL_RESEARCH.md` §5).
>
> **The table below is Claude's best reconstruction from the Tech Stack inventory. It is
> unverified against each vendor's actual terms, and it is counsel question 2.** Vendor
> locations and transfer mechanisms are **stated as "to verify" rather than asserted** —
> guessing them would be exactly the invention this repo forbids.

| Sub-processor | Purpose | Personal Data reaches it? | Location | Transfer mechanism |
|---|---|---|---|---|
| **ClickUp** | CRM — Lead/Opportunity/Client/Partner records | **Yes, by definition.** Contact name, work email, company | `[TO VERIFY — US]` | `[TO VERIFY]` |
| **Zoho Books** | Invoicing, client billing records | **Yes.** Client contact + billing data | `[TO VERIFY]` | `[TO VERIFY]` |
| **Anthropic (Claude)** | Agent execution across all departments | **Yes, if a prompt contains it.** See note below | `[TO VERIFY — US]` | `[TO VERIFY]` |
| **Notion** | Content brief database | `[Possibly — depends on brief content]` | `[TO VERIFY — US]` | `[TO VERIFY]` |
| **Canva** | Creative assembly | `[Possibly — if client assets contain it]` | `[TO VERIFY]` | `[TO VERIFY]` |
| **OpenArt** | AI image/video generation | `[Unlikely, but verify prompts]` | `[TO VERIFY]` | `[TO VERIFY]` |
| **KIE.ai** | AI image/video generation (Nano Banana Pro, Seedance) | `[Unlikely, but verify prompts]` | `[TO VERIFY]` | `[TO VERIFY]` |
| **Vercel** | Website hosting | `[Only if forms collect it]` | `[TO VERIFY — US]` | `[TO VERIFY]` |
| **`[Email/domain provider]`** | `arikaagency.com` mailboxes | **Yes.** All client correspondence | `[TO VERIFY — registrar unconfirmed, TECHSTACK_OS.md §9]` | `[TO VERIFY]` |

> ### ⚠️ Anthropic is the one to think hardest about
> Arika runs **100 agents** on `arika-runtime`, all of which call Claude. **Whatever an agent is
> fed goes to Anthropic.** `audits-subaudit-analyst` analyses a client's CRM;
> `clientpartner-acquisition-diagnostic` runs a 12-input intake on a client's business;
> `consulting-advisory-prep` assembles client data for a session. **If those prompts contain
> real client personal data, Anthropic is a Sub-processor on the critical path of nearly every
> offer Arika sells.**
>
> This is not hypothetical — it is how the agency is designed to work. **Counsel question 2
> must cover it specifically**, including Anthropic's own commercial terms, data-retention
> settings, and whether inputs are used for training.

---

# ANNEX C — Technical and organisational measures (GDPR Art. 32)

> ⚠️ **Do not fill this in with aspirations.** Every line becomes a contractual warranty. State
> only what is **actually true today**. `[TO CONFIRM]` is honest; a measure Arika does not
> actually operate is a misrepresentation the first time a client audits (Clause 8).

| Measure | Status |
|---|---|
| Access control (least privilege, unique accounts) | `[TO CONFIRM]` |
| Multi-factor authentication on all systems holding Client Personal Data | `[TO CONFIRM]` |
| Encryption in transit (TLS) | `[TO CONFIRM — vendor-provided]` |
| Encryption at rest | `[TO CONFIRM — vendor-provided]` |
| Secrets management (API keys not committed to source control) | `[Partially true: .env files are gitignored — arika-runtime/.gitignore, design-plugin]` |
| Backup and recovery | `[TO CONFIRM]` |
| Personnel confidentiality obligations | `[Solo operator; MSA Clause 6 applies]` |
| Security training | `[TO CONFIRM]` |
| Breach detection and response | **`[NOT ESTABLISHED — see Clause 4 note]`** |
| Sub-processor due diligence | **`[NOT ESTABLISHED — see Annex B]`** |
| Data deletion on request | `[TO CONFIRM per system]` |
| Device security (disk encryption, screen lock) | `[TO CONFIRM]` |

---

# ANNEX D — Standard Contractual Clauses

`[ATTACH where the Client is established in the EEA or UK.]`

`[EU SCCs (Commission Implementing Decision (EU) 2021/914) — Module [TO BE CONFIRMED BY
COUNSEL: likely Module Two (Controller to Processor)]. UK: International Data Transfer Agreement
or the UK Addendum.]`

> ⚠️ **Counsel question 3.** Do not select a module by guesswork. The chain is EU Controller →
> Kenyan Processor → US Sub-processors, and the module choice determines who signs what and
> which onward-transfer obligations bite.

---

## Completion checklist (delete before sending)

- [ ] **Annex A completed for this specific engagement** — not copied from the last one
- [ ] **Annex B verified against every vendor's actual terms** — locations and mechanisms filled, no `[TO VERIFY]` left
- [ ] **Annex C states only measures that are actually true**
- [ ] Annex D attached if the Client is EEA/UK, with the module confirmed by counsel
- [ ] Clause 4 notification window is one a **solo operator can actually meet**
- [ ] Clause 7: does this engagement touch Sensitive Personal Data? If yes — **escalate, don't proceed**
- [ ] Clause 9: is data-protection liability capped, and can Arika survive it uncapped?
- [ ] **Kenyan advocate has reviewed this document**
- [ ] `LEGAL_RESEARCH.md` §5 resolved: **what is the s.48 basis for Arika's own stack?**
