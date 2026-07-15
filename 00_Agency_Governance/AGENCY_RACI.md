# Agency Cross-Department RACI

**Status:** v0.1-draft — structure complete. Named owner confirmed: Mary Thuo (sole owner across all departments, 2026-06-30).
**Last updated:** 2026-06-30

> Referenced from [`GLOBAL_OS.md`](../GLOBAL_OS.md) §11 (closes "Required Agency-Wide Closure Systems" item 3). See `AGENCY_OPERATING_CONSTITUTION.md` §4 for the decision-rights framework this RACI implements.

---

## How to read this

**R**esponsible — does the work. **A**ccountable — owns the outcome, signs off, answerable if it fails (exactly one per row). **C**onsulted — input sought before acting. **I**nformed — told after the fact.

All "Responsible/Accountable" cells below are department names, not individuals, by design — they describe the *functional* structure this RACI targets, independent of who currently staffs it. **Confirmed 2026-06-30: every department is currently owned by one person, Mary Thuo** (`GLOBAL_OS.md` §4) — so every cell below currently resolves to her in practice. The department-name structure is kept rather than collapsed to her name everywhere, so this table stays correct and ready to use once Arika Agency brings on additional people per department. This table covers *cross-department* functions only; department-local RACI lives in each `{DEPT}_OS.md` §11.

## Cross-Department Functions

| Function | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| New offer launch (Sector → Offer → Marketing/Content) | Offer (02) | Offer (02) | Sector (01), Marketing (03), Content (04) | Sales (05), Finance (09) |
| Audit/diagnostic delivery (Gateway Offer) | Audits & Diagnostics (14) | Audits & Diagnostics (14) | Offer (02) | Sales (05), Sector (01) |
| Advisory delivery (Embedded-Partnership stage) | Consulting & Advisory (15) | Consulting & Advisory (15) | Offer (02) | All departments |
| AI workflow / process automation delivery | Automation (16) | Automation (16) | Offer (02), AI Enablement (17) | Operations (08) |
| AI transformation roadmap & governance | AI Enablement (17) | AI Enablement (17) | Offer (02), Legal (10) | Automation (16), Operations (08) |
| Demand generation campaign | Marketing (03) | Marketing (03) | Branding (12), Offer (02), Content (04) | Sales (05) |
| Content creation & narrative/messaging execution | Content (04) | Content (04) | Marketing (03), Branding (12) | Sales (05) |
| Partner/referral channel acquisition | ClientPartner Acquisition (06) | ClientPartner Acquisition (06) | Sales (05), Legal (10) | Marketing (03) |
| Deal closing & contract handoff | Sales (05) | Sales (05) | Legal (10), Finance (09) | Client Success (07) |
| Client onboarding | Client Success (07) | Client Success (07) | Sales (05), Operations (08) | Finance (09) |
| Delivery execution & SOP adherence | Operations (08) | Operations (08) | Client Success (07) | Finance (09) |
| Invoicing & revenue recognition | Finance (09) | Finance (09) | Operations (08) | Agency Governance (00) |
| Contract drafting & legal review | Legal (10) | **Mary Thuo** | **External counsel — ⚠️ NOT ENGAGED**, Sales (05), Client Success (07) | Agency Governance (00) |
| Hiring & internal onboarding | HR/People Ops (11) | HR/People Ops (11) | Operations (08) | Agency Governance (00) |
| Brand standards enforcement across departments | Branding (12) | Branding (12) | Marketing (03), Content (04), Sales (05) | All departments |
| Tool/vendor selection & access management | Tech Stack (13) | Tech Stack (13) | Department requesting tool | Finance (09) (cost), Legal (10) (contract terms) |
| Agency-wide constitution amendments | Agency Governance (00) | Mary Thuo | All department owners | All departments |
| Risk Class 3+ approvals (per Constitution §5) | Department initiating action | Mary Thuo | Legal (10) if contractual | All affected departments |
| Cross-department KPI rollup & reporting | Agency Governance (00) | Mary Thuo | All departments | All departments |

## Open Items

- This table will need expansion as real workflows get built (each department's Workflow Index, `{DEPT}_OS.md` §4) and surface new cross-department handoffs not yet anticipated here.
- Once Arika Agency brings on people beyond Mary Thuo, revisit whether any department-name cell should split into a real named individual distinct from her.

## Changelog

- 2026-06-30 — Initial cross-department RACI structure created as part of governance-closure pass.
- 2026-06-30 — Owner confirmed: Mary Thuo, sole owner across all departments. "Agency owner" cells resolved to her name; added a note clarifying every department-name cell currently resolves to her in practice. — Claude Code (Sonnet 4.6)
- 2026-06-30 — Added 4 cross-department function rows for the new departments (Audits & Diagnostics 14, Consulting & Advisory 15, Automation 16, AI Enablement 17), created when the owner promoted 4 of the Offer catalog's divisions to real departments. — Claude Code (Sonnet 4.6)
