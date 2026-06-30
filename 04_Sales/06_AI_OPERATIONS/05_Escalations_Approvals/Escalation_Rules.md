# Escalation and Approval Rules

Generated: 2026-05-12

## Risk Classes

| Class | Definition | Required Control |
|---|---|---|
| Low | Internal drafting, summarization, classification, or planning with no external effect. | Agent can proceed and report assumptions. |
| Medium | Internal decision support that may influence sales activity, messaging, CRM structure, or workflows. | Reflection check and clear assumptions. |
| High | Pricing, negotiation, legal exposure, external messaging, relationship-sensitive moves, budget, data changes, or strategy shifts. | Human approval before execution. |
| Critical | Contract terms, destructive actions, compliance risk, sensitive data, financial commitments, or irreversible customer-facing commitments. | Human approval and audit log required. |

## Always Escalate

- Legal, compliance, privacy, contract, or payment risk.
- External communication to leads, customers, partners, vendors, or public channels.
- Pricing, discounting, compensation, guarantee, or refund decisions.
- CRM, automation, database, or file changes that are destructive or hard to reverse.
- Low confidence with material business impact.
- Conflicting source evidence or conflicting human instructions.
- Any agent disagreement that cannot be resolved by source evidence.

## Approval Packet

Every approval request must include:

- Proposed action
- Reason
- Evidence
- Risk class
- Options
- Recommendation
- Downside
- Rollback or mitigation plan

## Human Override

Human instruction wins when it is explicit, lawful, and within authority. If a human instruction conflicts with the constitution, source evidence, safety boundary, or prior approval rule, stop and ask for clarification.
