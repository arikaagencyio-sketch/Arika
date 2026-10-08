import { test } from "node:test";
import assert from "node:assert/strict";
import { finalizeRun, runAgent } from "../dist/executor.js";
import { isApprovalRefusal } from "../dist/approval.js";

const spec = (riskClass = 1, explicitGate = false) => ({
  name: "approval-dispatch-test", department: "02", execution: "prompt",
  risk_class: riskClass, requires_human_approval: explicitGate,
  emits: ["OFFER_BRIEF_RECEIVED"],
});

/**
 * REWRITTEN for D4 (2026-10-08), not loosened.
 *
 * This file previously asserted that a gated run COMPLETED while advertising no
 * downstream event — `status: "awaiting_review"`, `emitted: []`. That was true and
 * it was the whole defect: `humanGate` was computed, recorded and returned, and
 * nothing refused. Suppressing the emits narrowed the blast radius; it did not
 * close the gate.
 *
 * Under D4 a gated run is REFUSED, so there is no result to inspect. What these
 * tests now assert is stronger: that no result, no memory line and no emit exists
 * to inspect at all.
 */
test("D4: a gated run is refused outright — there is no awaiting_review result to dispatch", () => {
  for (const agent of [spec(3), spec(4), spec(1, true), spec(1)]) {
    let caught;
    try {
      finalizeRun(agent, { trigger: "manual" }, { requiresHumanApproval: true });
    } catch (err) {
      caught = err;
    }
    assert.ok(caught, `${agent.name} class ${agent.risk_class}: must refuse, not return`);
    assert.ok(isApprovalRefusal(caught), "must be the structured approval refusal");
    assert.equal(caught.refusal.code, "APPROVAL_REQUIRED");
    // The emits this file used to prove were suppressed are now unreachable:
    // nothing is returned, so nothing can advertise them.
    assert.ok(caught.refusal.refusedBefore.includes("advertised emits"));
    assert.ok(caught.refusal.refusedBefore.includes("event publication"));
  }
});

test("D4: an ordinary ungated advisory result still retains its permitted events", () => {
  // The scope limit, unchanged: Class 1 with no flag anywhere is advisory and keeps
  // its declared emits. D4 must not broaden into this path.
  const result = finalizeRun(spec(), { trigger: "manual" }, { requiresHumanApproval: false });
  assert.equal(result.status, "advisory_complete");
  assert.deepEqual(result.emitted, ["OFFER_BRIEF_RECEIVED"]);
  assert.equal(result.requiresHumanApproval, false);
});

test("D4: unattended dispatch still refuses gated specs before any model call", async () => {
  for (const trigger of ["event", "join", "schedule", "webhook"]) {
    for (const agent of [spec(3), spec(4), spec(1, true)]) {
      let caught;
      try {
        await runAgent(agent, { trigger });
      } catch (err) {
        caught = err;
      }
      assert.ok(isApprovalRefusal(caught), `${trigger} class ${agent.risk_class}: must refuse`);
      assert.equal(caught.refusal.stage, "pre_model");
      assert.ok(caught.refusal.refusedBefore.includes("model invocation"));
    }
  }
});

test("D4: a caller cannot mistake a refusal for a completed run", async () => {
  // The shape every caller in index.ts and cli.ts now branches on. A refusal has
  // no `status`, no `memoryPath` and no `emitted` — there is nothing on it that
  // reads as success, and `isApprovalRefusal` is the supported discriminator.
  let caught;
  try {
    await runAgent(spec(3), { trigger: "schedule" });
  } catch (err) {
    caught = err;
  }
  assert.ok(isApprovalRefusal(caught));
  assert.equal(caught.status, undefined, "a refusal carries no run status");
  assert.equal(caught.memoryPath, undefined, "a refusal carries no memory path");
  assert.equal(caught.emitted, undefined, "a refusal carries no emits");
  assert.equal(caught.recommendation, undefined, "a refusal carries no recommendation");
  // An ordinary failure must NOT be treated as an approval refusal.
  assert.equal(isApprovalRefusal(new TypeError("boom")), false);
});
