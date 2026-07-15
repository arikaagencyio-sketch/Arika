import { EventEmitter } from "node:events";

export interface RuntimeEvent {
  type: string;
  payload?: Record<string, unknown>;
  source?: string;
  occurredAt?: string;
}

/**
 * In-process pub/sub. The interface deliberately mirrors finos's
 * `FinancialEventBus` so it can be swapped for a durable bus (NATS/Redis) later
 * without touching callers.
 */
export class EventBus {
  private readonly emitter = new EventEmitter();

  constructor() {
    // Agents may fan a single event out to many handlers.
    this.emitter.setMaxListeners(0);
  }

  on(type: string, handler: (event: RuntimeEvent) => void | Promise<void>): void {
    this.emitter.on(type, handler);
  }

  async publish(event: RuntimeEvent): Promise<void> {
    const full: RuntimeEvent = { ...event, occurredAt: event.occurredAt ?? new Date().toISOString() };
    this.emitter.emit(full.type, full);
  }
}

/** Shared singleton used by the booted runtime. */
export const eventBus = new EventBus();
