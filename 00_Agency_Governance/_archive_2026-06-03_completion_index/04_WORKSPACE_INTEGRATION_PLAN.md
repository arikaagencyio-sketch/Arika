# Workspace Integration Plan

Generated: 2026-06-03

## Placement Doctrine

Artifacts must live at the closest authoritative layer. Local domain truth lives inside the domain workspace. Cross-domain rules, source IDs, enterprise governance, dashboards, and dependency maps live in the agency root intelligence layer. Repetition is avoided by references: local registries point upward to the agency registry, and the agency registry points back to local owners.

## Authoritative Workspace Placement

| Workspace | Domain | Authoritative Location | Owner | Upstream | Downstream |
| --- | --- | --- | --- | --- | --- |
| The Agency Drafts Root | Agency | 00_Agency_Workspace_Intelligence | Agency Operating Council / Founder | All domain workspaces, market reality, client outcomes, financial controls | All domain operating systems, governance, orchestration, dashboards, memory, automation |
| Sales Drafts | Sales | Sales Drafts | Sales OS Owner / Revenue Conversion Lead | Sector, Offer, Marketing, Branding, ClientPartner Acquisition, Legal | Client, Finance, Management, Offer refinement, delivery promise memory |
| Marketing Drafts | Marketing | Marketing Drafts | Marketing OS Owner / Demand Generation Lead | Sector, Offer, Branding, Finance, Management | Sales, ClientPartner Acquisition, CRM, Revenue forecasting, Brand feedback |
| The Sector Drafts | Sector | The Sector Drafts | Sector Intelligence Owner / Market Strategy Lead | Market data, client context, competitive research, management priorities | Offer, Marketing, Sales, Client, Branding, Automation |
| The ClientPartner Draft | ClientPartner Acquisition | The ClientPartner Draft | ClientPartner Acquisition Owner / Partnership Growth Lead | Sector, Offer, Branding, Marketing, Sales | Sales, Partnerships, Distribution, Revenue channels, Client acquisition memory |
| Offer Drafts | Offer | Offer Drafts | Offer OS Owner / Value Architecture Lead | Sector, Client, Finance, Sales, Branding, Management | Marketing, Sales, Client Delivery, Finance, ClientPartner Acquisition |
| Branding Drafts | Branding | Branding Drafts | Brand OS Owner / Trust and Narrative Lead | Sector, Client, Offer, Culture, Management | Marketing, Sales, Client experience, Authority building, Agency positioning |
| Financial Drafts | Finance | Financial Drafts | Finance OS Owner / Financial Control Lead | Sales revenue, Client delivery economics, Operations spend, Legal/tax, Management priorities | Management decisions, Offer pricing, Operations capacity, Hiring, Risk controls |
| The Agency Client. Drafts | Client | The Agency Client. Drafts | Client OS Owner / Client Success Lead | Sales, Offer, Legal, Finance, Branding, Operations | Operations, Finance, Management, Retention, Expansion, Referrals, Case studies |
| The Agency Draft 1.2 | Management | The Agency Draft 1.2 | Management OS Owner / Agency Strategy Lead | All domain intelligence, finance, market reality, client outcomes, founder direction | All domains, governance, resource allocation, cadence, roadmap, risk management |

## Registry Relationships

- Local Source Registry: owns local document IDs, status, owner, cadence, dependencies, and source evidence.
- Local Master Registry: owns workflows, artifacts, schemas, events, agents, tools, automations, metrics, decisions, and memory.
- Agency Global Source Registry: owns cross-domain source routing, active/superseded/archive state, duplication decisions, and agency-level lineage.
- Agency Dependency Registry: owns cross-workspace dependencies and required handoff packets.
- Agency KPI Registry: owns formulas, thresholds, dashboard locations, and decision consequences.

## Orchestration Rules

1. Source work starts in the local workspace and is registered locally.
2. Any cross-domain output must create or update a handoff packet.
3. Handoffs are accepted only when entry/exit criteria, source evidence, owner, and KPI impact are present.
4. Automation can execute only when the action has a risk class, approval route, rollback, fallback, and log destination.
5. Every material decision updates the decision log and version log.
6. Every completed workflow updates operational memory and learning memory.

## Dependency Graph

Sector -> Offer -> Marketing -> Sales -> Client -> Operations -> Finance -> Management.

Branding supports Sector, Offer, Marketing, Sales, Client, and Management.

ClientPartner Acquisition feeds Marketing, Sales, and distribution.

Automation, Legal/Governance, Observability, Memory, Security, and Change Management apply across all domains.
