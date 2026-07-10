import { randomUUID } from "node:crypto";
import type { ApprovalRequest, ExpensePayload, Money } from "../shared/types.js";

export interface GovernancePolicy {
  entityId: string;
  autoApproveMinor: number;
  managerApprovalMinor: number;
  cfoApprovalMinor: number;
  executiveApprovalMinor: number;
}

export class FinancialGovernanceService {
  constructor(private readonly policies: GovernancePolicy[]) {}

  approveExpense(input: { entityId: string; expense: ExpensePayload; budgetRemaining?: Money }): ApprovalRequest {
    const policy = this.policyFor(input.entityId);
    const amount = input.expense.amount.amountMinor;
    const budgetExceeded = input.budgetRemaining ? amount > input.budgetRemaining.amountMinor : false;
    const role = this.requiredRole(amount, policy);

    let status: ApprovalRequest["status"] = amount <= policy.autoApproveMinor && !budgetExceeded ? "auto_approved" : "submitted";
    if (budgetExceeded) status = "escalated";

    return {
      id: randomUUID(),
      entityId: input.entityId,
      type: "expense",
      amount: input.expense.amount,
      requestedBy: input.expense.requestedBy,
      departmentId: input.expense.departmentId,
      status,
      requiredApproverRole: role,
      reason: budgetExceeded ? "Budget threshold exceeded." : "Expense routed through approval matrix.",
      createdAt: new Date().toISOString()
    };
  }

  enforceSeparationOfDuties(actor: { id: string; roles: string[] }, action: "approve" | "pay" | "reconcile" | "report"): void {
    const incompatibleByAction: Record<typeof action, string[]> = {
      approve: ["payment_executor", "reconciler"],
      pay: ["approver", "reconciler"],
      reconcile: ["approver", "payment_executor"],
      report: []
    };
    const incompatible = incompatibleByAction[action];

    if (actor.roles.some((role) => incompatible.includes(role))) {
      throw new Error(`Segregation-of-duties violation for actor ${actor.id} performing ${action}.`);
    }
  }

  private policyFor(entityId: string): GovernancePolicy {
    const policy = this.policies.find((candidate) => candidate.entityId === entityId);
    if (!policy) throw new Error(`No governance policy for entity ${entityId}.`);
    return policy;
  }

  private requiredRole(amountMinor: number, policy: GovernancePolicy): string {
    if (amountMinor <= policy.autoApproveMinor) return "department_owner";
    if (amountMinor <= policy.managerApprovalMinor) return "manager";
    if (amountMinor <= policy.cfoApprovalMinor) return "cfo";
    if (amountMinor <= policy.executiveApprovalMinor) return "executive_committee";
    return "board";
  }
}
