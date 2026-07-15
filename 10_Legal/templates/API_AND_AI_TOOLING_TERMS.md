> # 🔴 UNREVIEWED DRAFT — NOT LEGAL ADVICE
> Written by Claude Code (Opus 4.8) on 2026-07-15. **No lawyer has seen this.**
> §1–§4 are **client-facing terms** (attach to an MSA/SOW); §5–§8 are **internal policy**.
> See [`README.md`](README.md). Remove this banner only when replaced by:
> *Reviewed by [NAME], [FIRM], [DATE].*

---

# API & AI TOOLING TERMS

**Why this document exists:** Arika delivers with AI. Not as a side-tool — **100 agents on
`arika-runtime`**, a live cloud routine, real generated imagery shipped to production. That
creates three distinct exposures most agencies never write down:

1. **Vendor terms** — every API has a contract Arika is bound by
2. **Client disclosure** — does the client know, and did they agree?
3. **Data flow** — client data entering a vendor's system is a **sub-processing** event

---

# PART A — CLIENT-FACING TERMS

## 1. Disclosure of AI use

1.1 **Arika uses AI tools in the delivery of the Services.** This includes large language models,
image and video generation, and automated analysis.

1.2 Arika discloses this because the Client is entitled to know how its work is produced, and
because **some clients have policies restricting AI use in work delivered to them.**

1.3 `[SELECT ONE PER ENGAGEMENT:]`
- `[The Client consents to Arika's use of AI tools as described in this document.]`
- `[The Client restricts AI use as follows: [SPECIFY]. Arika will comply and will state in the SOW where this affects timeline or fee.]`

> ⚠️ **Ask early, not late.** *"Do you have an AI-use policy?"* belongs in the SOW's
> dependencies. A client who discovers after delivery that their deliverable was AI-generated —
> when their own policy forbade it — is a dispute Arika created by not asking a one-line
> question.

## 2. Human review

2.1 **AI output is reviewed by a human before it reaches the Client.** No AI output is delivered
unreviewed.

2.2 This mirrors Arika's own binding rule — `16_Automation`'s **`Draft 35` Phase 3 immutable**:
*"human-in-the-loop checkpoint on any client-facing AI output; no fully autonomous client-facing
AI without a review gate."* It is enforced in code: every agent is **advisory-first**, and
Class 3+ work requires human sign-off under the agency's Constitution.

2.3 **Review is not a warranty.** See §3.

## 3. What Arika does not warrant

3.1 Per **MSA Clause 8.5**, Arika does **not** warrant that AI output is accurate, original, or
fit for any purpose beyond that stated in the SOW.

3.2 **Rights position of generated material.** Per
[`IP_COPYRIGHT_TRADEMARK_TERMS.md`](IP_COPYRIGHT_TRADEMARK_TERMS.md) §4:
- Arika assigns **whatever rights it holds** in AI output — **which may be none**
- **The copyright status of AI-generated material is genuinely unsettled**; some jurisdictions
  require human authorship
- Arika cannot audit a model's training data and does not warrant output is free of third-party
  rights

3.3 **Arika will not** knowingly generate material imitating an identifiable third party's
protected work, trademarks, or likeness, and will decline a request to.

## 4. Client data and AI tools

4.1 Where the Services involve Arika processing Client personal data, **the AI vendors Arika uses
are Sub-processors** under [`DPA.md`](DPA.md) — see **DPA Annex B**.

4.2 **This is the clause clients should read most carefully, and it is stated plainly:** if an
Arika agent analyses the Client's CRM, that data is sent to the model vendor. **Anthropic is on
the critical path of nearly every offer Arika sells.**

4.3 The Client may object to a Sub-processor under **DPA Clause 5.2**.

---

# PART B — INTERNAL POLICY

## 5. Vendor terms bind Arika

Every tool in `13_Tech_Stack/TECHSTACK_OS.md` §3 has terms Arika agreed to. **Nobody has read
them against Arika's actual use.**

| Vendor | Used for | Terms reviewed? | Question that must be answered |
|---|---|---|---|
| **Anthropic (Claude)** | All 100 agents; `arika-runtime`; the cloud routine | **`[NO — TO REVIEW]`** | Commercial use ✓? Are inputs used for training? Retention? Client data permitted? |
| **OpenArt** | Image/video generation | **`[NO — TO REVIEW]`** | Commercial rights on **Free plan**? Output ownership? |
| **KIE.ai** (Nano Banana Pro, Seedance) | Image/video generation | **`[NO — TO REVIEW]`** | Commercial use? Whose terms govern the underlying Google/Bytedance models? |
| **Canva / Claude Design** | Creative assembly | **`[NO — TO REVIEW]`** | Output licence for client work? Template redistribution? |
| **ClickUp / Notion / Zoho Books** | CRM, briefs, invoicing | **`[NO — TO REVIEW]`** | Sub-processor terms; DPA available? |
| **Relume** | Component library | **`[NO — TO REVIEW]`** | Licence for client deliverables? |
| **Vercel** | Hosting | **`[NO — TO REVIEW]`** | — |

> ### 🔴 The one to check first: **OpenArt's Free plan**
> `TECHSTACK_OS.md` §3 records OpenArt as **Free plan, 40 credits**, all spent on 2026-07-04
> generating imagery **now live on the Arika website**.
>
> **Free tiers commonly restrict commercial use.** If OpenArt's does, imagery generated under it
> is on a commercial site in breach of the licence it was made under. **This is checkable today,
> costs nothing, and concerns assets already published.** Check it first.

## 6. Rules for using AI in delivery

1. **Never paste client Confidential Information or personal data into a tool that is not a
   documented Sub-processor** (DPA Annex B). This includes personal accounts and consumer chat
   interfaces.
2. **Never paste credentials, API keys, or secrets** into any prompt.
3. **Human review before delivery** — always (§2.1).
4. **Check the vendor's commercial-use terms** before output reaches a client or a public
   channel.
5. **Prefer tools with a real DPA** where client data is involved.
6. **Record which tool produced what** — needed for §5's rights position and for any client
   asking.
7. **Never generate imitations** of an identifiable third party's work, marks, or likeness.
8. **A capability not attached cannot be misused** — the Creative Pipeline routine deliberately
   has **no OpenArt/Canva connector**, making credit-spend *technically impossible* rather than
   merely forbidden (`16_Automation/AUTOMATION_OS.md` §12). **Prefer that pattern to a rule.**

## 7. Credentials

7.1 API keys live in `.env` files, **gitignored, never committed** (`arika-runtime/.gitignore`,
`19_Design/design-plugin/.env`).

7.2 **`ANTHROPIC_API_KEY` is not set** — recorded across `TECHSTACK_OS.md` §9. When it is: it is
the credential behind all 100 agents. Treat accordingly.

7.3 `[TO ESTABLISH: rotation policy; who holds which credential; what happens on device loss.]`

## 8. The recursion, stated honestly

**Arika sells AI governance** — `17_AI_Enablement`'s offer #11 has *"the most rigorous compliance
immutable of any offer"*: a governance framework covering model risk, data privacy, and
bias/fairness **required before any production AI deployment**.

**Arika has never run that framework over its own 100-agent AI deployment.**

`16_Automation/AUTOMATION_OS.md` §12 records **25 cron triggers against 1 approval-matrix row**.
`17_AI_Enablement/AI_ENABLEMENT_OS.md` §13 states it directly:

> **Arika would not currently pass its own gate.**

**This is not fatal — nothing is in production against a real client's data, because there are no
clients.** It is, precisely, the window in which to fix it. **The first client engagement closes
that window**, and the agency will then be selling a discipline it does not practise, to buyers
whose first instinct — per `Draft 40` Phase 9's **Doubter** archetype — is to ask whether it
works.

**→ Counsel/owner action:** run Arika's own AI deployment through `ai-enablement-governance-gate`
before the first client. If it blocks, that is the answer.

---

## Open items — for the counsel brief

| # | Question | Urgency |
|---|---|---|
| 1 | **OpenArt Free-plan commercial-use terms** — imagery is already live on the site | **Check today. Free. Concerns published assets** |
| 2 | Anthropic's terms: commercial use, training on inputs, retention, client data | Before the first client's data reaches an agent |
| 3 | Do ClickUp / Notion / Zoho / Anthropic offer DPAs? Obtain and complete **DPA Annex B** | Before the first client |
| 4 | KIE.ai — whose terms govern the underlying models? | Before client imagery |
| 5 | Is AI-use disclosure (§1) sufficient, or does any client jurisdiction require more? | Before the first SOW |
