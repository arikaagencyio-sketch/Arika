# Agency KPI Dictionary

**Status:** v0.1-draft — standard metric definitions only; no real values, owners, or thresholds populated yet.
**Last updated:** 2026-06-30

> Referenced from [`GLOBAL_OS.md`](../GLOBAL_OS.md) §11 (closes "Required Agency-Wide Closure Systems" item 5). Department-local KPIs live in each `{DEPT}_OS.md` §7; this file is for metrics that roll up *across* departments.

---

## How to read this

This dictionary defines **standard industry-framework metrics** relevant to an agency operating this flow (Sector → Offer → Marketing/Content → Sales → Client Success → Operations → Finance). The formulas are real and field-tested; the **owner, cadence, and threshold columns are placeholders** — populating those with real numbers requires actual agency data and is explicitly not invented here, per the constitution's no-silent-invention rule (`AGENCY_OPERATING_CONSTITUTION.md` §3).

## Acquisition Metrics

| Metric | Formula | Primary source department | Owner | Cadence | Threshold |
|---|---|---|---|---|---|
| CAC (Customer Acquisition Cost) | Total acquisition spend ÷ new clients closed in period | Sales (05) + Finance (09) | *(unassigned)* | Monthly | *(unset)* |
| Lead Volume | Count of qualified leads entering pipeline | Marketing (03) / Content (04) / ClientPartner Acquisition (06) | *(unassigned)* | Weekly | *(unset)* |
| Conversion Rate | Closed deals ÷ qualified leads in period | Sales (05) | *(unassigned)* | Monthly | *(unset)* |
| Sales Cycle Length | Avg. days from first contact to closed deal | Sales (05) | *(unassigned)* | Monthly | *(unset)* |
| Pipeline Velocity | (Qualified leads × win rate × avg deal value) ÷ sales cycle length | Sales (05) | *(unassigned)* | Monthly | *(unset)* |
| Partner-Sourced Revenue % | Revenue from ClientPartner-sourced deals ÷ total revenue | ClientPartner Acquisition (06) + Finance (09) | *(unassigned)* | Quarterly | *(unset)* |

## Revenue & Financial Metrics

| Metric | Formula | Primary source department | Owner | Cadence | Threshold |
|---|---|---|---|---|---|
| MRR (Monthly Recurring Revenue) | Sum of active monthly recurring contract value | Finance (09) | *(unassigned)* | Monthly | *(unset)* |
| ARR (Annual Recurring Revenue) | MRR × 12 | Finance (09) | *(unassigned)* | Monthly | *(unset)* |
| LTV (Client Lifetime Value) | Avg. revenue per client × avg. client lifespan | Finance (09) + Client Success (07) | *(unassigned)* | Quarterly | *(unset)* |
| LTV:CAC Ratio | LTV ÷ CAC | Finance (09) | *(unassigned)* | Quarterly | *(unset)* |
| Gross Margin | (Revenue − direct delivery cost) ÷ Revenue | Finance (09) + Operations (08) | *(unassigned)* | Monthly | *(unset)* |
| Burn Rate | Net monthly cash outflow | Finance (09) | *(unassigned)* | Monthly | *(unset)* |

## Delivery & Retention Metrics

| Metric | Formula | Primary source department | Owner | Cadence | Threshold |
|---|---|---|---|---|---|
| Client Retention Rate | Clients retained ÷ clients at period start | Client Success (07) | *(unassigned)* | Quarterly | *(unset)* |
| Churn Rate | 1 − Retention Rate | Client Success (07) | *(unassigned)* | Quarterly | *(unset)* |
| NPS (Net Promoter Score) | % promoters − % detractors (client survey) | Client Success (07) | *(unassigned)* | Quarterly | *(unset)* |
| On-Time Delivery Rate | Deliverables shipped within SLA ÷ total deliverables | Operations (08) | *(unassigned)* | Monthly | *(unset)* |
| Utilization Rate | Billable hours ÷ available hours | Operations (08) + HR/People Ops (11) | *(unassigned)* | Monthly | *(unset)* |

## How to extend this dictionary

When a department's content-migration pass surfaces a real, recurring metric not listed here, add it as a new row under the most relevant section (or a new section if none fits) rather than burying it in a department-local KPI table only — if more than one department references the same metric, it belongs here, not just locally.

## Changelog

- 2026-06-30 — Initial agency-wide KPI dictionary structure created as part of governance-closure pass: standard formulas defined across acquisition, revenue/financial, and delivery/retention categories; owners/cadence/thresholds left unset pending real agency data. — Claude Code (Sonnet 4.6)
