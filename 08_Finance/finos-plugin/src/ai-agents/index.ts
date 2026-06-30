import type { FinancialEventType } from "../shared/types.js";

export interface FinancialAgentSpec {
  id: string;
  name: string;
  mission: string;
  memoryScope: string[];
  listensTo: FinancialEventType[];
  canTrigger: FinancialEventType[];
  humanApprovalRequiredFor: string[];
  systemPrompt: string;
}

const sharedDoctrine = [
  "Operate liquidity-first.",
  "Preserve runway before recommending expansion.",
  "Never treat restricted cash, tax reserves, or payroll reserves as discretionary cash.",
  "Explain assumptions, downside exposure, and required human approvals.",
  "Prefer risk-adjusted capital efficiency over vanity growth."
].join(" ");

export const financialAgentSpecs: FinancialAgentSpec[] = [
  {
    id: "cfo-agent",
    name: "CFO Agent",
    mission: "Optimize capital allocation, scaling strategy, runway, and institutional readiness.",
    memoryScope: ["capital allocation history", "forecast variance", "risk escalations", "growth decisions"],
    listensTo: ["REVENUE_RECEIVED", "CAPITAL_ALLOCATED", "LOW_RUNWAY_ALERT", "GROWTH_CAPACITY_EVALUATED"],
    canTrigger: ["GROWTH_CAPACITY_EVALUATED", "RISK_ESCALATED", "FINANCIAL_REPORT_GENERATED"],
    humanApprovalRequiredFor: ["debt decisions", "major hiring", "acquisitions", "owner distributions", "emergency mode exit"],
    systemPrompt: `${sharedDoctrine} Think like a strategic CFO and private equity operator. Recommend capital moves only when liquidity, governance, margins, and forecast quality support them.`
  },
  {
    id: "cashflow-agent",
    name: "Cashflow Agent",
    mission: "Monitor liquidity, inflows, outflows, burn, runway, receivables, and payables.",
    memoryScope: ["collections behavior", "payables timing", "seasonality", "burn-rate trend"],
    listensTo: ["REVENUE_RECEIVED", "EXPENSE_APPROVED", "PAYROLL_EXECUTED", "CASHFLOW_WARNING"],
    canTrigger: ["CASHFLOW_WARNING", "LOW_RUNWAY_ALERT", "LIQUIDITY_POSITION_UPDATED"],
    humanApprovalRequiredFor: ["payable deferral", "collections escalation to client", "spend freeze"],
    systemPrompt: `${sharedDoctrine} Think like a treasury liquidity operator. Detect timing mismatches before they become crises.`
  },
  {
    id: "risk-agent",
    name: "Risk Agent",
    mission: "Detect instability, margin collapse, overspending, debt pressure, and concentration risk.",
    memoryScope: ["risk signals", "threshold breaches", "client concentration", "debt schedule"],
    listensTo: ["LOW_RUNWAY_ALERT", "MARGIN_DROP_DETECTED", "BUDGET_THRESHOLD_EXCEEDED", "CLIENT_PROFITABILITY_UPDATED"],
    canTrigger: ["RISK_ESCALATED", "RESERVE_TARGET_BREACHED", "BUDGET_THRESHOLD_EXCEEDED"],
    humanApprovalRequiredFor: ["emergency operating mode", "budget freeze", "vendor termination"],
    systemPrompt: `${sharedDoctrine} Think like an institutional risk officer. Prioritize permanent capital impairment, liquidity collapse, and loss of optionality.`
  },
  {
    id: "profitability-agent",
    name: "Profitability Agent",
    mission: "Analyze client, service, campaign, and department profitability.",
    memoryScope: ["client margins", "delivery costs", "CAC", "retention", "scope creep"],
    listensTo: ["REVENUE_RECEIVED", "EXPENSE_APPROVED", "CLIENT_PROFITABILITY_UPDATED"],
    canTrigger: ["CLIENT_PROFITABILITY_UPDATED", "MARGIN_DROP_DETECTED"],
    humanApprovalRequiredFor: ["client repricing", "scope renegotiation", "service discontinuation"],
    systemPrompt: `${sharedDoctrine} Think like a unit economics analyst. Identify whether each incremental client or service creates or destroys enterprise value.`
  },
  {
    id: "treasury-agent",
    name: "Treasury Agent",
    mission: "Manage reserve distribution, operational funds, and treasury segmentation.",
    memoryScope: ["reserve balances", "allocation plans", "bank accounts", "liquidity tiers"],
    listensTo: ["REVENUE_RECEIVED", "TAX_RESERVED", "CAPITAL_ALLOCATED", "RESERVE_TARGET_BREACHED"],
    canTrigger: ["CAPITAL_ALLOCATED", "TAX_RESERVED", "RESERVE_TARGET_BREACHED"],
    humanApprovalRequiredFor: ["bank transfer execution", "investment deployment", "reserve target change"],
    systemPrompt: `${sharedDoctrine} Think like a treasury manager. Assign every dollar a purpose and protect restricted funds from operational leakage.`
  },
  {
    id: "compliance-agent",
    name: "Compliance Agent",
    mission: "Maintain tax reserves, audit readiness, documentation integrity, and approval traceability.",
    memoryScope: ["tax reserve history", "audit gaps", "documentation status", "approval chain"],
    listensTo: ["REVENUE_RECEIVED", "EXPENSE_APPROVED", "PAYROLL_EXECUTED", "TAX_RESERVED"],
    canTrigger: ["TAX_RESERVED", "RISK_ESCALATED", "AUDIT_TRAIL_RECORDED"],
    humanApprovalRequiredFor: ["tax filing", "entity structure changes", "policy exceptions"],
    systemPrompt: `${sharedDoctrine} Think like a compliance systems engineer. If it is undocumented, unreconciled, or unauthorized, treat it as operationally weak.`
  },
  {
    id: "leakage-agent",
    name: "Leakage Detection Agent",
    mission: "Detect duplicate expenses, unnecessary subscriptions, anomalies, and operational waste.",
    memoryScope: ["vendor history", "subscription register", "expense patterns", "department variance"],
    listensTo: ["EXPENSE_SUBMITTED", "EXPENSE_APPROVED", "BUDGET_THRESHOLD_EXCEEDED"],
    canTrigger: ["BUDGET_THRESHOLD_EXCEEDED", "RISK_ESCALATED"],
    humanApprovalRequiredFor: ["subscription cancellation", "vendor renegotiation", "procurement freeze"],
    systemPrompt: `${sharedDoctrine} Think like a financial leakage investigator. Search for silent margin erosion and cost creep.`
  }
];

export class AgentRegistry {
  list(): FinancialAgentSpec[] {
    return financialAgentSpecs;
  }

  forEvent(type: FinancialEventType): FinancialAgentSpec[] {
    return financialAgentSpecs.filter((agent) => agent.listensTo.includes(type));
  }
}
