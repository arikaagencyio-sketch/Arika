import { test } from "node:test";
import assert from "node:assert/strict";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { readFileSync, rmSync } from "node:fs";

import { requiresHumanApproval, classToLevel, levelToClass } from "../dist/governance.js";
import { frontmatterSchema } from "../dist/spec-schema.js";
import { loadAgents } from "../dist/agent-registry.js";
import { writeMemory } from "../dist/memory-writer.js";

test("governance: human approval is forced at Constitution class 3+", () => {
  assert.equal(requiresHumanApproval(0), false);
  assert.equal(requiresHumanApproval(1), false);
  assert.equal(requiresHumanApproval(2), false);
  assert.equal(requiresHumanApproval(3), true);
  assert.equal(requiresHumanApproval(4), true);
  assert.equal(requiresHumanApproval(1, true), true, "a spec may opt in at a lower class");
  assert.equal(requiresHumanApproval(4, false), true, "a spec can never opt out at class 3+");
});

test("governance: risk level <-> class mapping", () => {
  assert.equal(levelToClass("high"), 3);
  assert.equal(levelToClass("critical"), 4);
  assert.equal(classToLevel(4), "critical");
  assert.equal(classToLevel(1), "low");
});

test("schema: a valid prompt spec passes and applies defaults", () => {
  const r = frontmatterSchema.safeParse({
    name: "x-test",
    department: "01",
    description: "d",
    risk_class: 1,
    triggers: [{ type: "manual" }],
  });
  assert.equal(r.success, true);
  assert.equal(r.data.model, "claude-opus-4-8");
  assert.equal(r.data.execution, "prompt");
  assert.equal(r.data.requires_human_approval, false);
});

test("schema: execution finos-plugin requires a finos_id", () => {
  const r = frontmatterSchema.safeParse({
    name: "x",
    department: "09",
    description: "d",
    execution: "finos-plugin",
    risk_class: 3,
    triggers: [{ type: "manual" }],
  });
  assert.equal(r.success, false);
});

test("schema: execution bois requires a bois_mode", () => {
  const base = {
    name: "x",
    department: "12",
    description: "d",
    execution: "bois",
    risk_class: 2,
    triggers: [{ type: "manual" }],
  };
  // Without a mode, the bois wrapper would not know which pipeline to run.
  assert.equal(frontmatterSchema.safeParse(base).success, false);
  assert.equal(frontmatterSchema.safeParse({ ...base, bois_mode: "define" }).success, true);
  assert.equal(frontmatterSchema.safeParse({ ...base, bois_mode: "nonsense" }).success, false);
});

test("schema: schedule trigger requires a cron expression", () => {
  const r = frontmatterSchema.safeParse({
    name: "x",
    department: "01",
    description: "d",
    risk_class: 1,
    triggers: [{ type: "schedule" }],
  });
  assert.equal(r.success, false);
});

test("schema: risk_class must be 0-4", () => {
  const r = frontmatterSchema.safeParse({
    name: "x",
    department: "01",
    description: "d",
    risk_class: 7,
    triggers: [{ type: "manual" }],
  });
  assert.equal(r.success, false);
});

test("registry: loads every agent; the legacy migration is complete", () => {
  const { agents, skipped } = loadAgents();
  assert.ok(agents.has("design-storyboard-generator"));
  assert.ok(agents.has("finance-cfo-agent"));
  assert.ok(agents.has("sales-lead-qualification"));
  assert.ok(agents.size >= 9, `expected >= 9 agents, got ${agents.size}`);
  // This assertion was `skipped.length >= 1` ("legacy specs should be skipped, not
  // thrown") until 2026-07-15, when the last 11 legacy specs (Experience Engineering)
  // gained frontmatter and the count reached zero. The tolerance itself still matters —
  // `skipped` must stay an array the loader populates rather than a throw — but the
  // meaningful invariant now is that nothing is left behind.
  assert.ok(Array.isArray(skipped), "loader must report skipped specs, not throw on them");
  assert.equal(skipped.length, 0, `migration complete: expected 0 legacy specs, got ${skipped.length}: ${skipped.join(", ")}`);
  assert.equal(agents.get("finance-cfo-agent").execution, "finos-plugin");
  assert.equal(agents.get("finance-treasury-agent").risk_class, 4);
});

test("memory-writer: appends a bois-compatible JSONL line", () => {
  const file = join(tmpdir(), `arika-mem-${Date.now()}.jsonl`);
  const spec = { name: "t-agent", department: "05", memory_stream: file };
  const path = writeMemory(spec, {
    trigger: "manual",
    input: { a: 1 },
    recommendation: { summary: "ok" },
    requiresHumanApproval: false,
    riskClass: 1,
  });
  assert.equal(path, file);
  const line = JSON.parse(readFileSync(file, "utf8").trim());
  assert.equal(line.agent, "t-agent");
  assert.equal(line.department, "05");
  assert.equal(line.source, "arika-runtime");
  assert.equal(line.event_type, "agent_run");
  assert.equal(line.payload.trigger, "manual");
  assert.equal(line.payload.recommendation.summary, "ok");
  rmSync(file, { force: true });
});
