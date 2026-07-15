import cron from "node-cron";
import type { AgentSpec } from "../spec-schema.js";

export interface ScheduledJob {
  agent: string;
  cron: string;
}

/**
 * Register every `schedule` trigger across all specs with node-cron. On fire,
 * `onFire(spec)` is called. Invalid cron expressions are skipped with a warning
 * rather than crashing boot. (Production scheduling is mirrored into Anthropic
 * cloud routines; this local scheduler covers dev + self-hosted runs.)
 */
export function registerSchedules(specs: AgentSpec[], onFire: (spec: AgentSpec) => void): ScheduledJob[] {
  const jobs: ScheduledJob[] = [];
  for (const spec of specs) {
    for (const t of spec.triggers) {
      if (t.type !== "schedule" || !t.cron) continue;
      if (!cron.validate(t.cron)) {
        console.warn(`  ! ${spec.name}: invalid cron "${t.cron}" — skipped`);
        continue;
      }
      cron.schedule(t.cron, () => onFire(spec));
      jobs.push({ agent: spec.name, cron: t.cron });
    }
  }
  return jobs;
}
