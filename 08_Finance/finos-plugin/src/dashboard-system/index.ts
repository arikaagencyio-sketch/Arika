import type { DashboardKpi, FinancialReport } from "../shared/types.js";

export type DashboardName =
  | "ceo"
  | "cfo"
  | "treasury"
  | "profitability"
  | "cashflow"
  | "risk"
  | "operations";

export interface DashboardDefinition {
  name: DashboardName;
  purpose: string;
  primaryCadence: DashboardKpi["cadence"];
  kpiIds: string[];
  humanDecisionFocus: string[];
}

export const dashboardDefinitions: DashboardDefinition[] = [
  {
    name: "ceo",
    purpose: "Compress executive financial reality into survival, growth, risk, and capital decisions.",
    primaryCadence: "daily",
    kpiIds: ["cash-position", "runway", "burn-rate", "gross-margin", "revenue-predictability", "capital-efficiency"],
    humanDecisionFocus: ["spend freeze", "growth capacity", "capital deployment", "strategic escalation"]
  },
  {
    name: "cfo",
    purpose: "Manage forecasting, margins, capital allocation, governance, and institutional readiness.",
    primaryCadence: "weekly",
    kpiIds: ["forecast-variance", "ebitda", "working-capital", "dscr", "budget-variance"],
    humanDecisionFocus: ["forecast revision", "budget reallocation", "bankability improvements"]
  },
  {
    name: "treasury",
    purpose: "Control cash position, reserve adequacy, bank exposure, and 13-week liquidity.",
    primaryCadence: "daily",
    kpiIds: ["unrestricted-cash", "restricted-cash", "reserve-cash", "cash-conversion-cycle", "payroll-coverage"],
    humanDecisionFocus: ["reserve transfers", "payables timing", "emergency liquidity mode"]
  },
  {
    name: "profitability",
    purpose: "Expose client, service, department, and campaign margin quality.",
    primaryCadence: "weekly",
    kpiIds: ["gross-margin", "contribution-margin", "ltv-cac", "cac-payback", "revenue-per-client"],
    humanDecisionFocus: ["repricing", "delivery redesign", "client portfolio pruning"]
  },
  {
    name: "cashflow",
    purpose: "Track inflows, outflows, collections, payables, and runway under scenarios.",
    primaryCadence: "daily",
    kpiIds: ["13-week-closing-cash", "collections-velocity", "pending-inflows", "pending-outflows"],
    humanDecisionFocus: ["collections acceleration", "vendor negotiation", "spend timing"]
  },
  {
    name: "risk",
    purpose: "Detect runway deterioration, margin collapse, concentration, debt pressure, and leakage.",
    primaryCadence: "daily",
    kpiIds: ["risk-count", "critical-risk-count", "client-concentration", "margin-drift", "debt-exposure"],
    humanDecisionFocus: ["risk escalation", "control strengthening", "emergency operating mode"]
  },
  {
    name: "operations",
    purpose: "Connect operational execution to financial outcomes.",
    primaryCadence: "weekly",
    kpiIds: ["revenue-per-employee", "utilization", "delivery-cost", "payroll-ratio", "vendor-variance"],
    humanDecisionFocus: ["resource allocation", "workflow redesign", "automation investment"]
  }
];

export class DashboardSystem {
  view(report: FinancialReport): { dashboard: DashboardDefinition | undefined; report: FinancialReport } {
    return {
      dashboard: dashboardDefinitions.find((definition) => definition.name === report.reportType),
      report
    };
  }
}
