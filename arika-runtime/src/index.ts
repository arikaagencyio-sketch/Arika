import { join } from "node:path";
import { config as loadEnv } from "dotenv";
import { loadAgents } from "./agent-registry.js";
import { runAgent } from "./executor.js";
import { isApprovalRefusal } from "./approval.js";
import { packageRoot } from "./paths.js";
import { eventBus } from "./triggers/event-bus.js";
import { JoinGate } from "./triggers/join-gate.js";
import { registerSchedules } from "./triggers/scheduler.js";
import { startWebhookServer } from "./triggers/webhook-server.js";

/**
 * D4 - every dispatch caller must branch on a refusal EXPLICITLY. A refusal is not
 * a failure to report and retry; it is a governed stop. Printing it through the
 * generic `failed:` path would let an operator read it as a transient error, so
 * each site prints REFUSED, names the stage and the reasons, and returns without
 * continuing. Nothing downstream of these call sites runs on a refusal, because
 * `runAgent` never returns one.
 */
function reportRefusal(where: string, agent: string, err: unknown): boolean {
  if (!isApprovalRefusal(err)) return false;
  const r = err.refusal;
  console.error(
    `[${where}] REFUSED ${agent} — ${r.code} at ${r.stage} (class ${r.riskClass}). ` +
      `Reasons: ${r.reasons.join("; ")}. Nothing was written, emitted or dispatched. ` +
      `No approval-resume path exists: this run cannot be continued by a flag.`,
  );
  return true;
}

async function main(): Promise<void> {
  loadEnv({ path: join(packageRoot, ".env") });

  const { agents, skipped } = loadAgents();

  // Wire event triggers → executor.
  let eventBindings = 0;
  for (const spec of agents.values()) {
    for (const t of spec.triggers) {
      if (t.type !== "event" || !t.on) continue;
      eventBindings += 1;
      eventBus.on(t.on, async (evt) => {
        try {
          const result = await runAgent(spec, { trigger: "event", eventType: evt.type, input: evt.payload });
          console.log(`[event ${evt.type}] ${spec.name} → approval:${result.requiresHumanApproval}`);
        } catch (err) {
          if (reportRefusal(`event ${evt.type}`, spec.name, err)) return;
          console.error(`[event ${evt.type}] ${spec.name} failed: ${(err as Error).message}`);
        }
      });
    }
  }

  // Wire join triggers → executor. Unlike an event binding, this fires once the
  // LAST awaited event lands, not once per arrival.
  const joinGate = new JoinGate(eventBus);
  let joinBindings = 0;
  for (const spec of agents.values()) {
    for (const t of spec.triggers) {
      if (t.type !== "join" || !t.waits_for) continue;
      joinBindings += 1;
      joinGate.register({
        name: spec.name,
        waitsFor: t.waits_for,
        correlateOn: t.correlate_on,
        onComplete: async (joined) => {
          try {
            const result = await runAgent(spec, {
              trigger: "join",
              eventType: t.waits_for!.join("+"),
              input: joined.payload,
            });
            console.log(`[join ${joined.key}] ${spec.name} → approval:${result.requiresHumanApproval}`);
          } catch (err) {
            if (reportRefusal(`join ${joined.key}`, spec.name, err)) return;
            console.error(`[join ${joined.key}] ${spec.name} failed: ${(err as Error).message}`);
          }
        },
      });
    }
  }

  // Wire schedule triggers → executor.
  const jobs = registerSchedules([...agents.values()], (spec) => {
    runAgent(spec, { trigger: "schedule" }).then(
      (r) => console.log(`[cron] ${spec.name} ran → approval:${r.requiresHumanApproval}`),
      (e: Error) => {
        if (reportRefusal("cron", spec.name, e)) return;
        console.error(`[cron] ${spec.name} failed: ${e.message}`);
      },
    );
  });

  const port = Number.parseInt(process.env.WEBHOOK_PORT ?? "8080", 10);
  await startWebhookServer(port, eventBus);

  console.log("──────────────────────────────────────────────────────────");
  console.log("  Arika Runtime — online");
  console.log(`  agents:     ${agents.size} registered`);
  console.log(`  events:     ${eventBindings} event binding(s) on the in-process bus`);
  console.log(`  joins:      ${joinBindings} barrier(s) — fire once all awaited events land (in-memory)`);
  console.log(`  scheduled:  ${jobs.length} cron trigger(s)`);
  for (const j of jobs) console.log(`               • ${j.agent}  (${j.cron})`);
  console.log(`  webhook:    POST http://localhost:${port}/webhook/:source`);
  if (skipped.length) console.log(`  skipped:    ${skipped.length} legacy/invalid spec(s) — run "arika list" for detail`);
  console.log(`  key:        ANTHROPIC_API_KEY ${process.env.ANTHROPIC_API_KEY ? "set" : "NOT set (runs will fail until provided)"}`);
  console.log("──────────────────────────────────────────────────────────");
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
