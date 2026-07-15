import Fastify, { type FastifyInstance } from "fastify";
import type { EventBus } from "./event-bus.js";

/**
 * Fastify server that turns external HTTP callbacks (ClickUp, Zoho Books, Notion,
 * …) into internal runtime events. A POST to `/webhook/:source` with a JSON body
 * is published on the event bus; any agent whose spec declares
 * `{ type: event, on: <TYPE> }` then fires. If the body has no `type`, a
 * `WEBHOOK_<SOURCE>` event type is synthesised.
 */
export async function startWebhookServer(port: number, bus: EventBus): Promise<FastifyInstance> {
  const app = Fastify({ logger: false });

  app.get("/health", async () => ({ ok: true, service: "arika-runtime" }));

  app.post("/webhook/:source", async (req, reply) => {
    const source = (req.params as { source: string }).source;
    const body = (req.body ?? {}) as Record<string, unknown>;
    const type = (body.type as string) ?? `WEBHOOK_${source.toUpperCase()}`;
    await bus.publish({ type, payload: body, source });
    return reply.code(200).send({ received: true, source, type });
  });

  await app.listen({ port, host: "0.0.0.0" });
  return app;
}
