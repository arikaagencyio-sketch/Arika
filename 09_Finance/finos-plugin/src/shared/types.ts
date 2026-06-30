export type CurrencyCode = string;

export interface Money {
  amountMinor: number;
  currency: CurrencyCode;
}

export type AccountClass =
  | "asset"
  | "liability"
  | "equity"
  | "revenue"
  | "expense"
  | "reserve"
  | "treasury_allocation"
  | "tax_obligation"
  | "payroll_liability";

export type NormalBalance = "debit" | "credit";

export interface LedgerAccount {
  id: string;
  entityId: string;
  code: string;
  name: string;
  class: AccountClass;
  normalBalance: NormalBalance;
  parentAccountId?: string;
  isControlAccount: boolean;
  isActive: boolean;
}

export interface LedgerLine {
  id: string;
  entityId: string;
  accountId: string;
  description: string;
  debitMinor: number;
  creditMinor: number;
  currency: CurrencyCode;
  clientId?: string;
  projectId?: string;
  departmentId?: string;
  metadata?: Record<string, unknown>;
}

export interface JournalEntry {
  id: string;
  entityId: string;
  eventId: string;
  description: string;
  postedAt: string;
  status: "draft" | "posted" | "reversed";
  lines: LedgerLine[];
  metadata?: Record<string, unknown>;
}

export const financialEventTypes = [
  "REVENUE_RECEIVED",
  "INVOICE_CREATED",
  "EXPENSE_SUBMITTED",
  "EXPENSE_APPROVED",
  "EXPENSE_REJECTED",
  "PAYROLL_EXECUTED",
  "TAX_RESERVED",
  "CASHFLOW_WARNING",
  "LOW_RUNWAY_ALERT",
  "MARGIN_DROP_DETECTED",
  "CLIENT_PROFITABILITY_UPDATED",
  "SUBSCRIPTION_RENEWED",
  "BUDGET_THRESHOLD_EXCEEDED",
  "CAPITAL_ALLOCATED",
  "RESERVE_TARGET_BREACHED",
  "LIQUIDITY_POSITION_UPDATED",
  "RISK_ESCALATED",
  "FINANCIAL_REPORT_GENERATED",
  "GROWTH_CAPACITY_EVALUATED",
  "AUDIT_TRAIL_RECORDED"
] as const;

export type FinancialEventType = (typeof financialEventTypes)[number];

export interface FinancialEvent<TPayload extends Record<string, unknown> = Record<string, unknown>> {
  id: string;
  type: FinancialEventType;
  entityId: string;
  occurredAt: string;
  source: string;
  actorId?: string;
  correlationId?: string;
  causationId?: string;
  payload: TPayload;
  metadata?: Record<string, unknown>;
}

export interface RevenueReceivedPayload extends Record<string, unknown> {
  amount: Money;
  clientId?: string;
  invoiceId?: string;
  revenueStream: "recurring" | "one_time" | "expansion" | "asset" | "capital";
  receivedAt: string;
}

export interface ExpensePayload extends Record<string, unknown> {
  amount: Money;
  vendorId?: string;
  category: string;
  departmentId?: string;
  expenseId: string;
  description: string;
  requestedBy: string;
  strategicJustification?: string;
}

export interface AllocationRule {
  id: string;
  entityId: string;
  name: string;
  priority: number;
  revenueStream?: RevenueReceivedPayload["revenueStream"];
  allocations: AllocationTarget[];
  effectiveFrom: string;
  effectiveTo?: string;
  enabled: boolean;
}

export interface AllocationTarget {
  bucket:
    | "operations"
    | "payroll"
    | "tax"
    | "emergency_reserve"
    | "growth_capital"
    | "profit_reserve"
    | "acquisition_reserve"
    | "debt_service"
    | "investment"
    | "owner_distribution";
  percent: number;
  targetAccountId: string;
  minimumReserveMonths?: number;
  locked?: boolean;
}

export interface AllocationPlan {
  id: string;
  entityId: string;
  sourceEventId: string;
  amount: Money;
  targets: Array<AllocationTarget & { amount: Money }>;
  residual: Money;
  decisionMode: "rules" | "ai_recommended" | "human_override";
  rationale: string[];
}

export interface CashPosition {
  entityId: string;
  asOf: string;
  unrestrictedCash: Money;
  restrictedCash: Money;
  reserveCash: Money;
  pendingInflows: Money;
  pendingOutflows: Money;
  netLiquidity: Money;
  runwayDays: number | null;
}

export interface CashflowForecastLine {
  date: string;
  inflow: Money;
  outflow: Money;
  net: Money;
  projectedCash: Money;
  confidence: number;
  drivers: string[];
}

export interface CashflowForecast {
  entityId: string;
  generatedAt: string;
  scenario: "base" | "upside" | "downside" | "crisis";
  horizonDays: number;
  openingCash: Money;
  closingCash: Money;
  runwayDays: number | null;
  lines: CashflowForecastLine[];
  assumptions: string[];
}

export type RiskSeverity = "info" | "watch" | "warning" | "critical";

export interface FinancialRiskSignal {
  id: string;
  entityId: string;
  type:
    | "liquidity"
    | "runway"
    | "burn_rate"
    | "margin"
    | "revenue_concentration"
    | "client_dependency"
    | "overspending"
    | "debt"
    | "receivables"
    | "forecast_variance"
    | "compliance"
    | "leakage";
  severity: RiskSeverity;
  title: string;
  message: string;
  metric: string;
  currentValue: number;
  threshold: number;
  detectedAt: string;
  recommendedActions: string[];
}

export interface ApprovalRequest {
  id: string;
  entityId: string;
  type: "expense" | "capital_deployment" | "payroll" | "vendor" | "budget_change";
  amount: Money;
  requestedBy: string;
  departmentId?: string;
  budgetId?: string;
  status: "submitted" | "auto_approved" | "ai_reviewed" | "approved" | "rejected" | "escalated";
  requiredApproverRole: string;
  reason: string;
  createdAt: string;
}

export interface ClientProfitability {
  clientId: string;
  entityId: string;
  revenue: Money;
  deliveryCost: Money;
  acquisitionCost: Money;
  grossMarginPct: number;
  contributionMarginPct: number;
  ltvToCac: number | null;
  paybackMonths: number | null;
  riskFlags: string[];
}

export interface DashboardKpi {
  id: string;
  label: string;
  value: number | string;
  unit?: string;
  cadence: "daily" | "weekly" | "monthly" | "quarterly" | "half_yearly" | "yearly";
  status: "healthy" | "watch" | "warning" | "critical";
  explanation: string;
}

export interface FinancialReport {
  id: string;
  entityId: string;
  reportType: "ceo" | "cfo" | "treasury" | "profitability" | "cashflow" | "risk" | "operations";
  generatedAt: string;
  periodStart: string;
  periodEnd: string;
  kpis: DashboardKpi[];
  risks: FinancialRiskSignal[];
  decisions: string[];
  narrative: string;
}

export interface Repository<TRecord extends { id: string }> {
  get(id: string): Promise<TRecord | undefined>;
  list(filter?: Record<string, unknown>): Promise<TRecord[]>;
  save(record: TRecord): Promise<TRecord>;
}
