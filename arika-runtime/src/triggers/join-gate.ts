import type { EventBus, RuntimeEvent } from "./event-bus.js";

/**
 * The barrier the plain event bus can't express.
 *
 * An EventEmitter fans out and never joins, so a step that genuinely requires
 * several upstream steps to *all* finish had no honest wiring: subscribing it to
 * each upstream event fires it once per arrival instead of once per completion.
 * Two departments hit this — Experience Engineering (20)'s parallel UI/Motion/3D
 * work and its two launch gates, and Audits & Diagnostics (14)'s parallel
 * sub-audits feeding one synthesis step (`Draft 39` Phase 5).
 *
 * A JoinGate buffers arrivals per correlation key and fires exactly once, when
 * the last awaited event lands.
 *
 * **In-memory and per-process.** Pending joins do not survive a restart. A
 * 7-14 day audit therefore cannot rely on this to hold state across days — that
 * needs the durable bus `EventBus` was designed to be swapped for.
 */

export interface JoinRegistration {
  /** Agent name — used for logging and `pending()` inspection. */
  name: string;
  waitsFor: string[];
  /** Dot-path into the event payload. Omitted = one global join. */
  correlateOn?: string;
  onComplete: (joined: JoinedEvent) => void | Promise<void>;
}

export interface JoinedEvent {
  /** The correlation value these events shared, or `__global__`. */
  key: string;
  /** Each awaited event, by type. */
  events: Record<string, RuntimeEvent>;
  /** Every arrived payload merged, plus the correlation key. */
  payload: Record<string, unknown>;
}

export interface PendingJoin {
  agent: string;
  key: string;
  arrived: string[];
  waitingOn: string[];
}

const GLOBAL_KEY = "__global__";

/** Resolve a dot-path (`a.b.c`) against a payload; undefined if any hop is missing. */
function resolvePath(payload: Record<string, unknown> | undefined, path: string): unknown {
  if (!payload) return undefined;
  let cursor: unknown = payload;
  for (const segment of path.split(".")) {
    if (typeof cursor !== "object" || cursor === null) return undefined;
    cursor = (cursor as Record<string, unknown>)[segment];
  }
  return cursor;
}

export class JoinGate {
  /** registration → correlation key → arrived event type → event */
  private readonly buffers = new Map<JoinRegistration, Map<string, Map<string, RuntimeEvent>>>();

  constructor(private readonly bus: EventBus) {}

  register(reg: JoinRegistration): void {
    this.buffers.set(reg, new Map());
    for (const eventType of reg.waitsFor) {
      this.bus.on(eventType, (evt) => this.accept(reg, eventType, evt));
    }
  }

  /** Joins still waiting on at least one event — what a monitor should surface. */
  pending(): PendingJoin[] {
    const out: PendingJoin[] = [];
    for (const [reg, byKey] of this.buffers) {
      for (const [key, arrived] of byKey) {
        out.push({
          agent: reg.name,
          key,
          arrived: [...arrived.keys()],
          waitingOn: reg.waitsFor.filter((t) => !arrived.has(t)),
        });
      }
    }
    return out;
  }

  private accept(reg: JoinRegistration, eventType: string, evt: RuntimeEvent): void {
    let key = GLOBAL_KEY;
    if (reg.correlateOn) {
      const raw = resolvePath(evt.payload, reg.correlateOn);
      if (raw === undefined || raw === null || raw === "") {
        // Never guess. Merging two clients' audits because a correlation key was
        // missing is worse than dropping the event loudly.
        console.error(
          `[join] ${reg.name}: dropped ${eventType} — no "${reg.correlateOn}" in payload, ` +
            `so it cannot be attributed to a run.`,
        );
        return;
      }
      key = String(raw);
    }

    const byKey = this.buffers.get(reg);
    if (!byKey) return;
    const arrived = byKey.get(key) ?? new Map<string, RuntimeEvent>();
    arrived.set(eventType, evt); // a repeat of the same type replaces it; it never counts twice
    byKey.set(key, arrived);

    if (arrived.size < reg.waitsFor.length) return;

    // Last one in — fire once and clear, so a later stray arrival can't re-fire it.
    byKey.delete(key);

    const events: Record<string, RuntimeEvent> = {};
    let payload: Record<string, unknown> = {};
    for (const type of reg.waitsFor) {
      const e = arrived.get(type)!;
      events[type] = e;
      payload = { ...payload, ...(e.payload ?? {}) };
    }
    if (reg.correlateOn) payload[reg.correlateOn] = key;

    void Promise.resolve(reg.onComplete({ key, events, payload })).catch((err: Error) => {
      console.error(`[join] ${reg.name} failed after barrier ${key}: ${err.message}`);
    });
  }
}
