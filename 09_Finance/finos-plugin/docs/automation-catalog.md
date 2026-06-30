# Automation Catalog

FinOS automations are event-aware and governance-bound.

| Automation | Trigger | System action | Human control |
|---|---|---|---|
| Invoice generation | Deal closed or billing milestone reached | Create invoice event and receivable schedule | Contract or pricing exceptions |
| Payment reminders | Invoice due date approaching or overdue | Send reminder, update collections risk | Escalation tone and client relationship actions |
| Reserve allocation | `REVENUE_RECEIVED` | Allocate tax, payroll, emergency, operations, growth, profit, acquisition buckets | Rule changes and bank movement execution |
| Tax allocation | `REVENUE_RECEIVED` | Calculate tax reserve using effective rate | Tax rate and filing decisions |
| Expense approval | `EXPENSE_SUBMITTED` | Route by amount, budget, and role | Manager/CFO/executive approval |
| Payroll execution | Scheduled payroll cycle | Verify payroll reserve, emit payroll event | Final payroll release |
| Recurring billing | Subscription renewal date | Create invoice/payment expectation | Pricing, discounts, churn-risk intervention |
| Subscription tracking | Vendor renewal approaching | Flag unused or duplicate subscription | Cancellation or vendor renegotiation |
| Financial reporting | Daily, weekly, monthly, quarterly | Generate dashboard/report event | Strategic decisions and board reporting |
| Liquidity alerts | Runway, reserve, or forecast threshold breach | Emit warning, escalate risk, recommend protection | Emergency mode activation |
| Risk escalation | Critical risk signal | Notify owner/CFO, open workflow, require decision | Risk acceptance or mitigation approval |
| Budget enforcement | Spend threshold crossed | Block or escalate approval | Override by authorized role |

## Emergency Operating Mode

Emergency mode activates when runway, liquidity, or forecast thresholds become critical. The system recommends:

- freeze discretionary spending
- protect payroll core
- accelerate collections
- renegotiate vendor terms
- pause non-essential growth spend
- run downside and crisis forecast refresh

Exiting emergency mode requires human approval from CFO/executive authority.
