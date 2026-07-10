import "dotenv/config";
import { AllocationEngine } from "../allocation-engine/index.js";
import { AuditSystem } from "../audit-system/index.js";
import { CashflowEngine } from "../cashflow-engine/index.js";
import { ComplianceEngine } from "../compliance-engine/index.js";
import { CoreLedgerService, InMemoryLedgerStore } from "../core-ledger/index.js";
import { DashboardSystem } from "../dashboard-system/index.js";
import { FinancialEventBus } from "../event-bus/index.js";
import { FinancialGovernanceService } from "../financial-governance/index.js";
import { ForecastingEngine } from "../forecasting-engine/index.js";
import { AgentRegistry } from "../ai-agents/index.js";
import { ClaudeAgentRuntime } from "../ai-agents/runtime.js";
import { IntegrationRegistry } from "../integrations/index.js";
import { ZohoBooksConnector } from "../integrations/zoho-books.js";
import { ProfitabilityEngine } from "../profitability-engine/index.js";
import { ReportingSystem } from "../reporting-system/index.js";
import { RiskEngine } from "../risk-engine/index.js";
import { money } from "../shared/money.js";
import type { AllocationRule } from "../shared/types.js";
import { TreasurySystem } from "../treasury-system/index.js";
import { FinancialWorkflowOrchestrator } from "../workflows/index.js";

const defaultEntityId = "agency-main";

const defaultAllocationRules: AllocationRule[] = [
  {
    id: "default-agency-revenue-allocation",
    entityId: defaultEntityId,
    name: "Default 360 Agency Revenue Allocation",
    priority: 100,
    effectiveFrom: "2026-01-01",
    enabled: true,
    allocations: [
      { bucket: "operations", percent: 35, targetAccountId: "reserve-operations" },
      { bucket: "payroll", percent: 15, targetAccountId: "reserve-payroll" },
      { bucket: "tax", percent: 15, targetAccountId: "reserve-tax", locked: true },
      { bucket: "emergency_reserve", percent: 10, targetAccountId: "reserve-emergency", minimumReserveMonths: 6, locked: true },
      { bucket: "growth_capital", percent: 15, targetAccountId: "reserve-growth" },
      { bucket: "profit_reserve", percent: 5, targetAccountId: "reserve-profit" },
      { bucket: "acquisition_reserve", percent: 5, targetAccountId: "reserve-acquisition" }
    ]
  }
];

export function createFinOsApplication() {
  const eventBus = new FinancialEventBus();
  const ledgerStore = new InMemoryLedgerStore();
  ledgerStore.seedAccounts([
    { id: "cash-operating", entityId: defaultEntityId, code: "1000", name: "Operating Cash", class: "asset", normalBalance: "debit", isControlAccount: true, isActive: true },
    { id: "revenue-services", entityId: defaultEntityId, code: "4000", name: "Agency Service Revenue", class: "revenue", normalBalance: "credit", isControlAccount: true, isActive: true },
    { id: "reserve-tax", entityId: defaultEntityId, code: "2100", name: "Tax Reserve", class: "tax_obligation", normalBalance: "credit", isControlAccount: true, isActive: true },
    { id: "reserve-payroll", entityId: defaultEntityId, code: "2200", name: "Payroll Reserve", class: "payroll_liability", normalBalance: "credit", isControlAccount: true, isActive: true },
    { id: "reserve-operations", entityId: defaultEntityId, code: "2300", name: "Operations Reserve", class: "reserve", normalBalance: "credit", isControlAccount: true, isActive: true },
    { id: "reserve-emergency", entityId: defaultEntityId, code: "2400", name: "Emergency Reserve", class: "reserve", normalBalance: "credit", isControlAccount: true, isActive: true },
    { id: "reserve-growth", entityId: defaultEntityId, code: "2500", name: "Growth Capital Reserve", class: "treasury_allocation", normalBalance: "credit", isControlAccount: true, isActive: true },
    { id: "reserve-profit", entityId: defaultEntityId, code: "2600", name: "Profit Reserve", class: "equity", normalBalance: "credit", isControlAccount: true, isActive: true },
    { id: "reserve-acquisition", entityId: defaultEntityId, code: "2700", name: "Acquisition Reserve", class: "treasury_allocation", normalBalance: "credit", isControlAccount: true, isActive: true }
  ]);

  const risk = new RiskEngine();
  const governance = new FinancialGovernanceService([
    {
      entityId: defaultEntityId,
      autoApproveMinor: 500_00,
      managerApprovalMinor: 5_000_00,
      cfoApprovalMinor: 25_000_00,
      executiveApprovalMinor: 100_000_00
    }
  ]);
  const compliance = new ComplianceEngine();
  const allocation = new AllocationEngine(defaultAllocationRules);
  const agents = new AgentRegistry();
  const agentRuntime = new ClaudeAgentRuntime(process.env.ANTHROPIC_API_KEY);
  const audit = new AuditSystem();

  const zohoBooks = new ZohoBooksConnector({ entityId: defaultEntityId });
  const integrations = new IntegrationRegistry();
  integrations.register(zohoBooks);

  const orchestrator = new FinancialWorkflowOrchestrator(
    eventBus,
    allocation,
    compliance,
    governance,
    risk,
    agents,
    agentRuntime,
    audit
  );
  orchestrator.register();

  return {
    defaultEntityId,
    eventBus,
    orchestrator,
    ledger: new CoreLedgerService(ledgerStore),
    allocation,
    treasury: new TreasurySystem(),
    cashflow: new CashflowEngine(),
    forecasting: new ForecastingEngine(),
    risk,
    profitability: new ProfitabilityEngine(),
    governance,
    compliance,
    reporting: new ReportingSystem(),
    dashboard: new DashboardSystem(),
    agents,
    agentRuntime,
    audit,
    integrations,
    zohoBooks,
    fixtures: {
      emptyCashPosition: () => new TreasurySystem().emptyPosition(defaultEntityId),
      starterCashPosition: () =>
        new TreasurySystem().calculateCashPosition({
          entityId: defaultEntityId,
          unrestrictedCash: [money(125_000_00)],
          restrictedCash: [money(25_000_00)],
          reserveCash: [money(75_000_00)],
          pendingInflows: [money(35_000_00)],
          pendingOutflows: [money(42_000_00)],
          averageDailyBurnMinor: 4_500_00
        })
    }
  };
}

export type FinOsApplication = ReturnType<typeof createFinOsApplication>;
