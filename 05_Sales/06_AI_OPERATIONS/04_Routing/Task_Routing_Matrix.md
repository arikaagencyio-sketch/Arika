# Task Routing Matrix

Generated: 2026-05-12

| User Intent | Primary Agent | Supporting Agents | Output | Approval Risk |
|---|---|---|---|---|
| Decide strategic revenue direction | Executive Intelligence Agent | Revenue Strategy Agent, Market Intelligence Agent | Strategic action brief | High |
| Build or revise pricing | Revenue Strategy Agent | Offer Architecture Agent, Risk Trust and Governance Agent | Pricing architecture | High |
| Research market, sector, or competitor | Market Intelligence Agent | Customer Psychology Agent | Intelligence brief | Medium |
| Understand buyer psychology or objections | Customer Psychology Agent | Lead Qualification and Discovery Agent | Buyer psychology map | Medium |
| Create an offer, value prop, or positioning | Offer Architecture Agent | Market Intelligence Agent, Customer Psychology Agent | Offer architecture | High if claims or pricing |
| Generate leads or channel plan | Demand Generation Agent | Audience and Community Agent, RevOps Agent | Channel action plan | Medium to High |
| Build audience or authority | Audience and Community Agent | Offer Architecture Agent, Risk Trust and Governance Agent | Audience system | Medium |
| Qualify a lead or structure discovery | Lead Qualification and Discovery Agent | Customer Psychology Agent | Qualification and discovery brief | Medium |
| Prepare close, negotiation, or objection response | Sales Execution and Closing Agent | Customer Psychology Agent, Power Navigation Agent | Deal strategy | High |
| Recover stalled deals or build follow-up | Follow-Up and Recovery Agent | Sales Execution Agent, RevOps Agent | Follow-up sequence | Medium |
| Onboard, retain, expand, or renew account | Customer Success and Expansion Agent | Revenue Strategy Agent, Risk Trust and Governance Agent | Account growth plan | High if terms change |
| Build CRM, metrics, dashboard, forecast | Revenue Operations and Performance Agent | Tool-Use Agent, Reflection Agent | RevOps spec/report | Medium to High |
| Navigate stakeholders, power, partners | Power Navigation and Partnership Agent | Sales Execution Agent, Revenue Strategy Agent | Power or partnership map | High |
| Check legal, trust, compliance, approvals | Risk Trust and Governance Agent | Reflection Agent | Approval or risk note | Critical if legal |
| Create SOP, playbook, script, training | Enablement and Playbooks Agent | Reflection Agent, Sales Execution Agent | Playbook/SOP/training asset | Medium |
| Coordinate AI workflow or memory | AI Orchestration Agent | Planning Agent, Multi-Agent Orchestration Agent | AI execution plan | Medium to High |
| Plan complex work | Planning Agent | Relevant operating agents | Execution plan | Depends on action |
| Use tools, query data, or activate systems | Tool-Use Agent | Risk Trust and Governance Agent | Tool result/audit | High for external/write actions |
| Review and improve output | Reflection and Quality Agent | Source-owning agent | Validation report | Low to Medium |
| Route work across many agents | Multi-Agent Orchestration Agent | All needed agents | Handoff/synthesis | Depends on highest-risk agent |

## Routing Rules

1. Route to the smallest capable agent first.
2. Add supporting agents only when the output needs their evidence or judgment.
3. Use Multi-Agent Orchestration when more than three agents are needed, agents disagree, or the task spans strategy, execution, RevOps, and governance.
4. Use Reflection and Quality before trusting any high-impact output.
5. Use Risk Trust and Governance before any external, legal, financial, sensitive, or irreversible action.
