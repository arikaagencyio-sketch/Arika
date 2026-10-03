import { test } from "node:test";
import assert from "node:assert/strict";
import { finalizeRun, runAgent } from "../dist/executor.js";

const spec = (riskClass = 1, explicitGate = false) => ({
  name: "approval-dispatch-test", department: "02", execution: "prompt",
  risk_class: riskClass, requires_human_approval: explicitGate,
  emits: ["OFFER_BRIEF_RECEIVED"],
});

test("approval: a recommendation awaiting review advertises no downstream event", () => {
  for (const agent of [spec(3), spec(4), spec(1, true), spec(1)]) {
    const result = finalizeRun(agent, { trigger: "manual" }, { requiresHumanApproval: true });
    assert.equal(result.status, "awaiting_review");
    assert.deepEqual(result.emitted, []);
    assert.equal(result.requiresHumanApproval, true);
  }
});

test("approval: an ordinary ungated advisory result retains its permitted events", () => {
  const result = finalizeRun(spec(), { trigger: "manual" }, { requiresHumanApproval: false });
  assert.equal(result.status, "advisory_complete");
  assert.deepEqual(result.emitted, ["OFFER_BRIEF_RECEIVED"]);
});

test("approval: unattended dispatch refuses gated specs before any model call", async () => {
  for (const trigger of ["event", "join", "schedule", "webhook"]) {
    for (const agent of [spec(3), spec(4), spec(1, true)]) {
      await assert.rejects(runAgent(agent, { trigger }), /Human review required/);
    }
  }
});
