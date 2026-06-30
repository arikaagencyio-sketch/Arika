import { randomUUID } from "node:crypto";
import type { FinancialEvent, FinancialEventType } from "../shared/types.js";

export type EventHandler<TPayload extends Record<string, unknown> = Record<string, unknown>> = (
  event: FinancialEvent<TPayload>
) => Promise<void> | void;

export interface EventStore {
  append(event: FinancialEvent): Promise<void>;
  list(entityId: string, types?: FinancialEventType[]): Promise<FinancialEvent[]>;
}

export class InMemoryEventStore implements EventStore {
  private readonly events: FinancialEvent[] = [];

  async append(event: FinancialEvent): Promise<void> {
    this.events.push(event);
  }

  async list(entityId: string, types?: FinancialEventType[]): Promise<FinancialEvent[]> {
    return this.events.filter((event) => {
      const entityMatches = event.entityId === entityId;
      const typeMatches = !types?.length || types.includes(event.type);
      return entityMatches && typeMatches;
    });
  }
}

export class FinancialEventBus {
  private readonly handlers = new Map<FinancialEventType, EventHandler[]>();

  constructor(private readonly store: EventStore = new InMemoryEventStore()) {}

  subscribe<TPayload extends Record<string, unknown> = Record<string, unknown>>(
    type: FinancialEventType,
    handler: EventHandler<TPayload>
  ): void {
    const existing = this.handlers.get(type) ?? [];
    existing.push(handler as EventHandler);
    this.handlers.set(type, existing);
  }

  async publish<TPayload extends Record<string, unknown>>(
    event: Omit<FinancialEvent<TPayload>, "id" | "occurredAt"> & Partial<Pick<FinancialEvent<TPayload>, "id" | "occurredAt">>
  ): Promise<FinancialEvent<TPayload>> {
    const completed: FinancialEvent<TPayload> = {
      ...event,
      id: event.id ?? randomUUID(),
      occurredAt: event.occurredAt ?? new Date().toISOString()
    };

    await this.store.append(completed as FinancialEvent);

    const handlers = this.handlers.get(completed.type) ?? [];
    for (const handler of handlers) {
      await handler(completed);
    }

    return completed;
  }

  async history(entityId: string, types?: FinancialEventType[]): Promise<FinancialEvent[]> {
    return this.store.list(entityId, types);
  }
}
