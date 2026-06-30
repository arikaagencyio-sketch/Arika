import type { FinancialEvent } from "../shared/types.js";

export type IntegrationKind = "crm" | "payments" | "banking" | "accounting" | "payroll" | "marketing" | "internal_ops";

export interface IntegrationConnector {
  id: string;
  kind: IntegrationKind;
  name: string;
  pull(since?: string): Promise<FinancialEvent[]>;
  push?(event: FinancialEvent): Promise<void>;
  health(): Promise<{ ok: boolean; message: string }>;
}

export class IntegrationRegistry {
  private readonly connectors = new Map<string, IntegrationConnector>();

  register(connector: IntegrationConnector): void {
    this.connectors.set(connector.id, connector);
  }

  list(): IntegrationConnector[] {
    return [...this.connectors.values()];
  }

  async ingestAll(since?: string): Promise<FinancialEvent[]> {
    const events: FinancialEvent[] = [];
    for (const connector of this.connectors.values()) {
      events.push(...(await connector.pull(since)));
    }
    return events;
  }
}
