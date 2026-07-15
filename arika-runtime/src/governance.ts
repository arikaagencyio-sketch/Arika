/**
 * Risk model. The Constitution's Class 0–4 (00_Agency_Governance/
 * AGENCY_OPERATING_CONSTITUTION.md §5) is SUPREME. The finos/Sales
 * low/medium/high/critical labels map onto it.
 */

export type RiskLevel = "low" | "medium" | "high" | "critical";

const LEVEL_TO_CLASS: Record<RiskLevel, number> = { low: 1, medium: 2, high: 3, critical: 4 };
// Index by Constitution class 0–4. Class 0 (informational) surfaces as "low".
const CLASS_TO_LEVEL: RiskLevel[] = ["low", "low", "medium", "high", "critical"];

export function levelToClass(level: RiskLevel): number {
  return LEVEL_TO_CLASS[level];
}

export function classToLevel(riskClass: number): RiskLevel {
  const clamped = Math.max(0, Math.min(4, Math.round(riskClass)));
  return CLASS_TO_LEVEL[clamped]!;
}

/**
 * Human sign-off is mandatory at Constitution Class 3+ — "with no exceptions
 * carved out by convenience or urgency" (Constitution §3 #5). A spec may also
 * opt in at a lower class, but can never opt out at class 3+.
 */
export function requiresHumanApproval(riskClass: number, specFlag = false): boolean {
  return riskClass >= 3 || specFlag;
}
