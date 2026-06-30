import { z } from "zod";
import type { FinOsApplication } from "./application.js";
import { money } from "../shared/money.js";

export const toolSchemas = {
  getCashPosition: {
    entityId: z.string().optional()
  },
  forecastCashflow: {
    entityId: z.string().optional(),
    horizonDays: z.number().int().positive().max(365).optional(),
    scenario: z.enum(["base", "upside", "downside", "crisis"]).optional()
  },
  allocateCapital: {
    entityId: z.string().optional(),
    amountMinor: z.number().int().positive(),
    currency: z.string().default("USD"),
    revenueStream: z.enum(["recurring", "one_time", "expansion", "asset", "capital"]).default("recurring"),
    clientId: z.string().optional()
  },
  approveExpense: {
    entityId: z.string().optional(),
    expenseId: z.string(),
    amountMinor: z.number().int().positive(),
    currency: z.string().default("USD"),
    category: z.string(),
    description: z.string(),
    requestedBy: z.string(),
    departmentId: z.string().optional(),
    budgetRemainingMinor: z.number().int().nonnegative().optional()
  },
  detectFinancialRisk: {
    entityId: z.string().optional(),
    debtServiceCoverageRatio: z.number().optional()
  },
  calculateClientProfitability: {
    entityId: z.string().optional(),
    clientId: z.string(),
    revenueMinor: z.number().int().nonnegative(),
    deliveryCostMinor: z.number().int().nonnegative(),
    acquisitionCostMinor: z.number().int().nonnegative(),
    averageMonthlyRevenueMinor: z.number().int().positive().optional(),
    currency: z.string().default("USD")
  },
  generateFinancialReport: {
    entityId: z.string().optional(),
    reportType: z.enum(["ceo", "cfo", "treasury", "profitability", "cashflow", "risk", "operations"]).default("ceo"),
    periodStart: z.string(),
    periodEnd: z.string()
  },
  analyzeRunway: {
    entityId: z.string().optional()
  },
  monitorLiquidity: {
    entityId: z.string().optional()
  },
  evaluateGrowthCapacity: {
    entityId: z.string().optional(),
    minimumRunwayDays: z.number().int().positive().default(180),
    minimumGrossMarginPct: z.number().positive().default(40),
    forecastAccuracyPct: z.number().positive().max(100).default(85)
  }
};

export function createToolHandlers(app: FinOsApplication) {
  const entity = (entityId?: string) => entityId ?? app.defaultEntityId;

  return {
    get_cash_position(input: z.infer<z.ZodObject<typeof toolSchemas.getCashPosition>>) {
      void entity(input.entityId);
      return app.fixtures.starterCashPosition();
    },

    forecast_cashflow(input: z.infer<z.ZodObject<typeof toolSchemas.forecastCashflow>>) {
      void entity(input.entityId);
      const position = app.fixtures.starterCashPosition();
      const base = app.cashflow.forecast(position, [], input.horizonDays ?? 91);
      return app.forecasting.scenario(base, input.scenario ?? "base");
    },

    async allocate_capital(input: z.infer<z.ZodObject<typeof toolSchemas.allocateCapital>>) {
      const entityId = entity(input.entityId);
      const event = await app.eventBus.publish({
        type: "REVENUE_RECEIVED",
        entityId,
        source: "mcp.allocate_capital",
        payload: {
          amount: money(input.amountMinor, input.currency),
          clientId: input.clientId,
          revenueStream: input.revenueStream,
          receivedAt: new Date().toISOString()
        }
      });
      return app.allocation.planRevenueAllocation(event);
    },

    approve_expense(input: z.infer<z.ZodObject<typeof toolSchemas.approveExpense>>) {
      const entityId = entity(input.entityId);
      return app.governance.approveExpense({
        entityId,
        expense: {
          amount: money(input.amountMinor, input.currency),
          category: input.category,
          departmentId: input.departmentId,
          expenseId: input.expenseId,
          description: input.description,
          requestedBy: input.requestedBy
        },
        budgetRemaining:
          input.budgetRemainingMinor === undefined ? undefined : money(input.budgetRemainingMinor, input.currency)
      });
    },

    detect_financial_risk(input: z.infer<z.ZodObject<typeof toolSchemas.detectFinancialRisk>>) {
      void entity(input.entityId);
      const position = app.fixtures.starterCashPosition();
      const forecast = app.cashflow.forecast(position, [], 91);
      return app.risk.detectFinancialRisk({
        position,
        forecast,
        debtServiceCoverageRatio: input.debtServiceCoverageRatio
      });
    },

    calculate_client_profitability(input: z.infer<z.ZodObject<typeof toolSchemas.calculateClientProfitability>>) {
      return app.profitability.calculateClientProfitability({
        entityId: entity(input.entityId),
        clientId: input.clientId,
        revenue: money(input.revenueMinor, input.currency),
        deliveryCost: money(input.deliveryCostMinor, input.currency),
        acquisitionCost: money(input.acquisitionCostMinor, input.currency),
        averageMonthlyRevenue:
          input.averageMonthlyRevenueMinor === undefined ? undefined : money(input.averageMonthlyRevenueMinor, input.currency)
      });
    },

    generate_financial_report(input: z.infer<z.ZodObject<typeof toolSchemas.generateFinancialReport>>) {
      const position = app.fixtures.starterCashPosition();
      const risks = app.risk.detectFinancialRisk({ position });
      return app.reporting.generateExecutiveReport({
        entityId: entity(input.entityId),
        reportType: input.reportType,
        periodStart: input.periodStart,
        periodEnd: input.periodEnd,
        position,
        risks
      });
    },

    analyze_runway(input: z.infer<z.ZodObject<typeof toolSchemas.analyzeRunway>>) {
      void entity(input.entityId);
      const position = app.fixtures.starterCashPosition();
      return {
        entityId: position.entityId,
        runwayDays: position.runwayDays,
        status: position.runwayDays !== null && position.runwayDays >= 180 ? "scale_ready" : "protect_liquidity",
        recommendedActions:
          position.runwayDays !== null && position.runwayDays < 90
            ? ["Freeze discretionary spend", "Accelerate receivables", "Increase reserve allocation"]
            : ["Maintain 13-week forecast", "Monitor reserve adequacy"]
      };
    },

    monitor_liquidity(input: z.infer<z.ZodObject<typeof toolSchemas.monitorLiquidity>>) {
      void entity(input.entityId);
      const position = app.fixtures.starterCashPosition();
      const risks = app.risk.detectFinancialRisk({ position });
      return {
        position,
        riskCount: risks.length,
        criticalRisks: risks.filter((risk) => risk.severity === "critical"),
        nextReviewCadence: "daily"
      };
    },

    evaluate_growth_capacity(input: z.infer<z.ZodObject<typeof toolSchemas.evaluateGrowthCapacity>>) {
      void entity(input.entityId);
      const position = app.fixtures.starterCashPosition();
      const runwayPass = (position.runwayDays ?? 0) >= input.minimumRunwayDays;
      const marginPass = input.minimumGrossMarginPct >= 40;
      const forecastPass = input.forecastAccuracyPct >= 85;
      const approved = runwayPass && marginPass && forecastPass;
      return {
        approved,
        status: approved ? "growth_capacity_available" : "growth_capacity_constrained",
        gates: {
          runwayPass,
          marginPass,
          forecastPass
        },
        doctrine: approved
          ? "Growth can be considered after maintaining reserve discipline."
          : "Liquidity, margin quality, or forecast discipline is insufficient for aggressive expansion."
      };
    }
  };
}

export function jsonContent(value: unknown) {
  return {
    content: [
      {
        type: "text" as const,
        text: JSON.stringify(value, null, 2)
      }
    ]
  };
}
