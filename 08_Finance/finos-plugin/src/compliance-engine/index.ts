import type { FinancialEvent, Money, RevenueReceivedPayload } from "../shared/types.js";
import { percentOf } from "../shared/money.js";

export interface ComplianceChecklistResult {
  entityId: string;
  status: "ready" | "gaps_detected";
  missing: string[];
  checkedAt: string;
}

export class ComplianceEngine {
  calculateTaxReserve(event: FinancialEvent<RevenueReceivedPayload>, effectiveTaxRatePct: number): Money {
    return percentOf(event.payload.amount, effectiveTaxRatePct);
  }

  auditReadiness(input: {
    entityId: string;
    hasSourceDocument: boolean;
    hasAuthorization: boolean;
    hasLedgerEntry: boolean;
    hasReconciliation: boolean;
    hasAuditTrail: boolean;
  }): ComplianceChecklistResult {
    const missing: string[] = [];
    if (!input.hasSourceDocument) missing.push("source_document");
    if (!input.hasAuthorization) missing.push("authorization");
    if (!input.hasLedgerEntry) missing.push("ledger_entry");
    if (!input.hasReconciliation) missing.push("reconciliation");
    if (!input.hasAuditTrail) missing.push("audit_trail");

    return {
      entityId: input.entityId,
      status: missing.length ? "gaps_detected" : "ready",
      missing,
      checkedAt: new Date().toISOString()
    };
  }
}
