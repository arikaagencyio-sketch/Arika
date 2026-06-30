# Human Operator Guide

Generated: 2026-05-12

This guide explains how to use the AI operations layer as a human operator.

## The Simple Rule

You do not need to know all 20 agents.

Start by saying what business outcome you want. The AI system routes the work to the right agent, subagent, skill, and tool path.

Good prompt pattern:

```text
Today I need to [business outcome].
Context: [what we know].
Constraints: [time, geography, sector, budget, tools, data limits].
Output I want: [list, plan, message sequence, CRM structure, call prep, etc.].
```

## Three Ways To Use The Agents

### 1. Natural Language Mode

Use this most of the time.

Example:

```text
Today I want to build pipeline in healthcare and logistics. Help me identify target sectors, decision makers, outreach angles, and a nurturing sequence.
```

Codex should route this through:

1. Planning Agent
2. Market Intelligence Agent
3. Demand Generation Agent
4. Lead Qualification and Discovery Agent
5. Offer Architecture Agent
6. Follow-Up and Recovery Agent
7. RevOps Performance Agent
8. Reflection and Quality Agent

### 2. Agent-Called Mode

Use this when you already know the agent.

Example:

```text
Use the Demand Generation Agent to build a 30-day outbound plan for logistics companies.
```

### 3. Daily Command Mode

Use this every morning when you do not know where to start.

Example:

```text
Run my Daily Sales Command. Tell me what to do today to move revenue, what leads to create, what deals to follow up, what calls to make, and what needs approval.
```

Codex should return:

- Top revenue priority
- Pipeline creation actions
- Follow-ups due
- Calls or conversations to prepare
- Research needed
- Assets to create
- Human decisions required
- End-of-day update format

## Morning Workflow

Use this sequence when you wake up.

1. Run Daily Sales Command.
2. Choose the highest leverage revenue action.
3. Ask Codex to route the action to the right agent.
4. Ask for the actual artifact: list, sequence, script, call prep, CRM fields, or follow-up message.
5. Execute the human part: call, send, decide, approve, or reject.
6. Return with results and ask Codex to update the learning loop.

Morning prompt:

```text
Run my Daily Sales Command for today.
Context: I am building pipeline from scratch.
Current focus:
- Target sectors:
- Offer:
- Geography:
- Existing leads:
- Available time today:
Output: Give me the top 5 actions, the agent route, and the exact first action to take.
```

## During The Day

Use plain activity prompts.

```text
I need to make a discovery call with [company/person]. Prepare me.
```

```text
This lead said [objection]. Diagnose the objection and write my response.
```

```text
I have 10 companies but no contacts. Build the decision-maker map and outreach plan.
```

```text
This deal has gone quiet. Build a recovery sequence.
```

```text
I finished this call. Here are my notes. Tell me what the next step is and update the pipeline logic.
```

## When To Name An Agent

You only need to name an agent when you want to force a specific mode.

| What You Need | Agent To Name |
|---|---|
| Strategic priority | Executive Intelligence Agent |
| Target sectors and market map | Market Intelligence Agent |
| Buyer pain and objections | Customer Psychology Agent |
| Offer or value proposition | Offer Architecture Agent |
| Leads and outreach | Demand Generation Agent |
| Audience/content/nurture | Audience and Community Agent |
| Discovery and qualification | Lead Qualification and Discovery Agent |
| Calls, objections, closing | Sales Execution and Closing Agent |
| Follow-up and stalled deals | Follow-Up and Recovery Agent |
| Customer onboarding or renewal | Customer Success and Expansion Agent |
| CRM, dashboards, KPIs | Revenue Operations and Performance Agent |
| Stakeholders and power | Power Navigation and Partnership Agent |
| Legal, trust, approval | Risk Trust and Governance Agent |
| SOPs, scripts, training | Enablement and Playbooks Agent |
| AI workflows and memory | AI Orchestration Agent |
| Complex task breakdown | Planning Agent |
| Tool or data operation | Tool-Use Agent |
| Review and confidence check | Reflection and Quality Agent |
| Many agents at once | Multi-Agent Orchestration Agent |

## End Of Day Workflow

Use this prompt:

```text
End-of-day sales update:
- Actions completed:
- Calls made:
- Replies received:
- Leads created:
- Objections heard:
- Deals moved:
- Things blocked:

Update the pipeline, extract lessons, tell me what to do tomorrow, and update the memory logs if needed.
```

## Human Role

Your job is not to memorize the agent system.

Your job is to bring:

- Business intent
- Real-world context
- Human judgment
- Customer conversations
- Approvals
- Execution

The AI system handles routing, structure, drafting, analysis, sequencing, memory, and reflection.
