import { test } from "node:test";
import assert from "node:assert/strict";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { existsSync, readFileSync, rmSync, writeFileSync } from "node:fs";

import { requiresHumanApproval, classToLevel, levelToClass } from "../dist/governance.js";
import { frontmatterSchema, MAX_NONSTREAMING_TOKENS } from "../dist/spec-schema.js";
import {
  advertisedEmits,
  DEFAULT_MAX_TOKENS,
  finalizeRun,
  parseStructuredOutput,
  runAgent,
} from "../dist/executor.js";
import {
  APPROVAL_REFUSAL_CODE,
  ApprovalRequiredError,
  assertDispatchApproval,
  assertStaticApproval,
  isApprovalRefusal,
  staticApprovalReasons,
} from "../dist/approval.js";
import { loadAgents } from "../dist/agent-registry.js";
import { writeMemory } from "../dist/memory-writer.js";
import {
  assertApprovedFixtureStream,
  assertFixturePreconditions,
  assertStreamMatchesMode,
  buildFixtureOptions,
  FIXTURE_AUTHORISATIONS,
  FIXTURE_CLASSIFICATION,
  FIXTURE_LANE_ENABLED,
  isSandboxStream,
} from "../dist/fixture.js";
import { EventBus } from "../dist/triggers/event-bus.js";
import { JoinGate } from "../dist/triggers/join-gate.js";

test("governance: human approval is forced at Constitution class 3+", () => {
  assert.equal(requiresHumanApproval(0), false);
  assert.equal(requiresHumanApproval(1), false);
  assert.equal(requiresHumanApproval(2), false);
  assert.equal(requiresHumanApproval(3), true);
  assert.equal(requiresHumanApproval(4), true);
  assert.equal(requiresHumanApproval(1, true), true, "a spec may opt in at a lower class");
  assert.equal(requiresHumanApproval(4, false), true, "a spec can never opt out at class 3+");
  assert.equal(requiresHumanApproval(1, false, true), true, "the agent's own output may opt in");
  assert.equal(requiresHumanApproval(4, false, false), true, "the agent can never opt out at class 3+");
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

test("schema: max_tokens is optional, a positive integer, and capped at the non-streaming ceiling", () => {
  const base = { name: "x", department: "02", description: "d", risk_class: 1, triggers: [{ type: "manual" }] };
  const ok = (max_tokens) => frontmatterSchema.safeParse({ ...base, max_tokens }).success;

  assert.equal(frontmatterSchema.safeParse(base).data.max_tokens, undefined, "omitted → executor default");
  assert.equal(ok(16000), true);
  assert.equal(ok(MAX_NONSTREAMING_TOKENS), true);
  // Above the ceiling the SDK refuses a non-streaming call outright.
  assert.equal(ok(MAX_NONSTREAMING_TOKENS + 1), false);
  assert.equal(ok(0), false);
  assert.equal(ok(1.5), false);
  assert.ok(DEFAULT_MAX_TOKENS <= MAX_NONSTREAMING_TOKENS, "the default itself must be callable");
});

test("executor: a max_tokens stop is reported as truncation, not a JSON parse error", () => {
  // The 2026-09-13 offer-orchestrator failure: partial JSON, cut mid-string.
  const truncated = { stop_reason: "max_tokens", content: [{ type: "text", text: '{"summary":"Hospitality intake, the OTA' }] };
  assert.throws(
    () => parseStructuredOutput("offer-orchestrator", truncated, 2048),
    (err) => /truncated/.test(err.message) && /2048/.test(err.message) && !/Unterminated/.test(err.message),
  );

  // Truncated during thinking — no text block at all — is still truncation.
  assert.throws(
    () => parseStructuredOutput("offer-orchestrator", { stop_reason: "max_tokens", content: [{ type: "thinking" }] }, 2048),
    /truncated/,
  );

  const complete = { stop_reason: "end_turn", content: [{ type: "thinking" }, { type: "text", text: '{"summary":"ok"}' }] };
  assert.deepEqual(parseStructuredOutput("offer-orchestrator", complete, DEFAULT_MAX_TOKENS), { summary: "ok" });
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
  // A static success event on an agent whose verdict can be negative announces a result
  // that never happened. Until the runtime has conditional emits, the pricing analyst
  // declares none (02_Offer/OFFER_OS.md §12).
  assert.deepEqual(
    agents.get("offer-pricing-floor-analyst").emits,
    [],
    "offer-pricing-floor-analyst must not statically emit OFFER_PRICED",
  );
});

test("registry: offer-orchestrator does not subscribe to an event it emits", () => {
  // It listened on OFFER_BRIEF_RECEIVED, the event it emits, so the first published brief
  // would have re-triggered it: the bus has no cycle detection (AEIT_11 §3.2). Intake is
  // now the human-invoked OFFER_INTAKE_REQUESTED, and the brief still flows on.
  const { agents } = loadAgents();
  const subscriptions = (spec) =>
    new Set(
      (spec.triggers ?? []).flatMap((t) =>
        t.type === "event" ? [t.on] : t.type === "join" ? (t.waits_for ?? []) : [],
      ),
    );
  const orchestrator = agents.get("offer-orchestrator");
  const heard = subscriptions(orchestrator);
  const emitted = orchestrator.emits ?? [];
  const reentrant = emitted.filter((e) => heard.has(e));
  assert.deepEqual(reentrant, [], `offer-orchestrator re-enters itself on: ${reentrant.join(", ")}`);
  assert.ok(heard.has("OFFER_INTAKE_REQUESTED"), "intake must be the human-invoked OFFER_INTAKE_REQUESTED");
  assert.ok(emitted.includes("OFFER_BRIEF_RECEIVED"), "the orchestrator must still emit OFFER_BRIEF_RECEIVED");
  assert.ok(
    subscriptions(agents.get("offer-oeos-engineer")).has("OFFER_BRIEF_RECEIVED"),
    "offer-oeos-engineer must still receive OFFER_BRIEF_RECEIVED",
  );
});

test("schema: join trigger requires 2+ distinct events", () => {
  const base = {
    name: "x",
    department: "14",
    description: "d",
    risk_class: 1,
  };
  const join = (waits_for) =>
    frontmatterSchema.safeParse({ ...base, triggers: [{ type: "join", waits_for }] }).success;

  // One event is just `type: event` — a barrier of 1 is a barrier of none.
  assert.equal(join(["A"]), false);
  assert.equal(join(undefined), false);
  // A repeated event can never produce a second arrival, so it would deadlock.
  assert.equal(join(["A", "A"]), false);
  assert.equal(join(["A", "B"]), true);
});

test("join-gate: fires once, only after every awaited event lands", async () => {
  const bus = new EventBus();
  const gate = new JoinGate(bus);
  const fired = [];
  gate.register({
    name: "t-join",
    waitsFor: ["A", "B", "C"],
    correlateOn: "engagement_id",
    onComplete: (joined) => fired.push(joined),
  });

  await bus.publish({ type: "A", payload: { engagement_id: "e1", from_a: 1 } });
  await bus.publish({ type: "B", payload: { engagement_id: "e1", from_b: 2 } });
  assert.equal(fired.length, 0, "must not fire while still waiting on C");
  assert.deepEqual(gate.pending()[0].waitingOn, ["C"]);

  await bus.publish({ type: "C", payload: { engagement_id: "e1", from_c: 3 } });
  assert.equal(fired.length, 1, "fires exactly once, on the last arrival");
  // The synthesis step needs every sub-audit's payload, merged.
  assert.equal(fired[0].payload.from_a, 1);
  assert.equal(fired[0].payload.from_b, 2);
  assert.equal(fired[0].payload.from_c, 3);
  assert.equal(fired[0].payload.engagement_id, "e1");
  assert.equal(gate.pending().length, 0, "a completed join is cleared");

  // A stray late arrival must not re-fire a completed barrier.
  await bus.publish({ type: "C", payload: { engagement_id: "e1", from_c: 99 } });
  assert.equal(fired.length, 1);
});

test("join-gate: correlation keys never bleed across runs", async () => {
  const bus = new EventBus();
  const gate = new JoinGate(bus);
  const fired = [];
  gate.register({
    name: "t-join",
    waitsFor: ["A", "B"],
    correlateOn: "engagement_id",
    onComplete: (joined) => fired.push(joined),
  });

  // Two audits in flight at once. A's from client 1 + B's from client 2 is NOT
  // a completed audit — merging them would report one client's findings on
  // another's report.
  await bus.publish({ type: "A", payload: { engagement_id: "e1" } });
  await bus.publish({ type: "B", payload: { engagement_id: "e2" } });
  assert.equal(fired.length, 0, "different engagements must not satisfy one barrier");

  await bus.publish({ type: "B", payload: { engagement_id: "e1" } });
  assert.equal(fired.length, 1);
  assert.equal(fired[0].key, "e1");
});

test("join-gate: an uncorrelatable event is dropped, not guessed", async () => {
  const bus = new EventBus();
  const gate = new JoinGate(bus);
  const fired = [];
  gate.register({
    name: "t-join",
    waitsFor: ["A", "B"],
    correlateOn: "engagement_id",
    onComplete: (joined) => fired.push(joined),
  });

  await bus.publish({ type: "A", payload: { engagement_id: "e1" } });
  await bus.publish({ type: "B", payload: {} }); // no key — unattributable
  assert.equal(fired.length, 0, "must not attribute a keyless event to an in-flight run");
  assert.deepEqual(gate.pending()[0].waitingOn, ["B"]);
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

// Runs the real post-agent path (gate + memory write) with a canned recommendation,
// returning both the top-level result and the line it logged.
function approvalSpec(riskClass, file, specFlag = false) {
  return {
    name: "t-offer",
    department: "02",
    execution: "prompt",
    risk_class: riskClass,
    requires_human_approval: specFlag,
    memory_stream: file,
    emits: [],
  };
}

function finalizeWith(riskClass, recommendation) {
  const file = join(tmpdir(), `arika-approval-${process.pid}-${Math.random().toString(36).slice(2)}.jsonl`);
  try {
    const result = finalizeRun(approvalSpec(riskClass, file), { trigger: "manual", input: {} }, recommendation);
    const logged = JSON.parse(readFileSync(file, "utf8").trim());
    return { result, logged };
  } finally {
    rmSync(file, { force: true });
  }
}

/**
 * D4. Runs `finalizeRun` expecting a REFUSAL, and returns the structured refusal
 * together with whether a memory line was written. The memory check is the point:
 * a refusal that still left a run record behind would be a half-closed gate.
 */
function refusalFrom(riskClass, recommendation, specFlag = false) {
  const file = join(tmpdir(), `arika-refuse-${process.pid}-${Math.random().toString(36).slice(2)}.jsonl`);
  try {
    let caught;
    try {
      finalizeRun(approvalSpec(riskClass, file, specFlag), { trigger: "manual", input: {} }, recommendation);
    } catch (err) {
      caught = err;
    }
    assert.ok(caught, "finalizeRun must REFUSE a gated run, not return a result");
    assert.ok(isApprovalRefusal(caught), "the refusal must be an ApprovalRequiredError");
    return { refusal: caught.refusal, wroteMemory: existsSync(file), error: caught };
  } finally {
    rmSync(file, { force: true });
  }
}

test("D4: a low-risk agent that asks for sign-off is REFUSED after the response, before memory", () => {
  // REWRITTEN for D4, not loosened. This asserted that the gate was RECORDED
  // (top-level + memory line both true) - which was the 2026-09-13 fix, and which
  // left the run completing. The five 2026-09-13 Offer records are exactly this
  // shape: class 1, recommendation true, run completed. D4 refuses instead, and
  // this test now additionally proves NO memory line is left behind.
  for (const riskClass of [0, 1, 2]) {
    const { refusal, wroteMemory } = refusalFrom(riskClass, {
      summary: "quote-bound",
      requiresHumanApproval: true,
    });
    assert.equal(refusal.code, APPROVAL_REFUSAL_CODE);
    assert.equal(refusal.stage, "post_response", `class ${riskClass}: only knowable after the call`);
    assert.equal(refusal.riskClass, riskClass);
    assert.ok(
      refusal.reasons.some((r) => r.includes("recommendation returned requiresHumanApproval")),
      `class ${riskClass}: the agent's own flag must be named as the reason`,
    );
    assert.equal(wroteMemory, false, `class ${riskClass}: a refused run writes NO memory line`);
    assert.ok(refusal.refusedBefore.includes("memory write"));
    assert.ok(refusal.refusedBefore.includes("advertised emits"));
    assert.ok(refusal.refusedBefore.includes("event publication"));
    assert.ok(refusal.refusedBefore.includes("receiver invocation"));
    assert.ok(refusal.refusedBefore.includes("registry mutation"));
    assert.equal(refusal.approvalEvidence, null, "no approval-resume path may appear here");
  }
});

test("approval: a low-risk agent that does not ask for sign-off stays ungated", () => {
  const { result, logged } = finalizeWith(1, { summary: "internal", requiresHumanApproval: false });
  assert.equal(result.requiresHumanApproval, false);
  assert.equal(logged.payload.requiresHumanApproval, false);
  // An output without the flag cannot raise the gate either.
  assert.equal(finalizeWith(1, { summary: "no flag" }).result.requiresHumanApproval, false);
});

test("D4: class 3 and 4 are REFUSED even when the agent says false", () => {
  // REWRITTEN for D4. This asserted that class 3+ FORCED the recorded gate while
  // the run still completed. Now the run is refused - and at class 3+ the reason
  // is static, so the refusal is also available before any model call.
  for (const riskClass of [3, 4]) {
    const { refusal, wroteMemory } = refusalFrom(riskClass, { summary: "x", requiresHumanApproval: false });
    assert.equal(refusal.code, APPROVAL_REFUSAL_CODE);
    assert.equal(refusal.riskClass, riskClass);
    assert.ok(
      refusal.reasons.some((r) => r.includes(`class ${riskClass} requires human sign-off`)),
      `class ${riskClass}: the Constitution rule must be named`,
    );
    assert.equal(wroteMemory, false, `class ${riskClass}: no memory line on refusal`);
  }
});

test("D4: the Class 3 static gate refuses BEFORE the model is invoked, on every trigger", async () => {
  // `runAgent` would call the model for a `prompt` agent. A refusal that arrives
  // first is the only reason these assertions can run with no API key set.
  for (const trigger of ["manual", "event", "join", "schedule", "webhook"]) {
    const spec = approvalSpec(3, undefined);
    let caught;
    try {
      await runAgent(spec, { trigger, input: {} });
    } catch (err) {
      caught = err;
    }
    assert.ok(isApprovalRefusal(caught), `${trigger}: class 3 must be refused`);
    assert.equal(caught.refusal.stage, "pre_model", `${trigger}: refused before the model call`);
    assert.ok(caught.refusal.refusedBefore.includes("model invocation"));
  }
});

test("D4: the Class 4 static gate refuses BEFORE the model is invoked, on every trigger", async () => {
  for (const trigger of ["manual", "event", "join", "schedule", "webhook"]) {
    let caught;
    try {
      await runAgent(approvalSpec(4, undefined), { trigger, input: {} });
    } catch (err) {
      caught = err;
    }
    assert.ok(isApprovalRefusal(caught), `${trigger}: class 4 must be refused`);
    assert.equal(caught.refusal.stage, "pre_model");
    assert.equal(caught.refusal.riskClass, 4);
  }
});

test("D4: a manual run no longer bypasses the static gate", async () => {
  // Until D4 the pre-model gate read `ctx.trigger !== "manual"`, treating a human
  // typing a command as approval. Presence is not recorded approval, and
  // Constitution section 3 #5 carves out no exception for convenience.
  let caught;
  try {
    await runAgent(approvalSpec(3, undefined), { trigger: "manual", input: {} });
  } catch (err) {
    caught = err;
  }
  assert.ok(isApprovalRefusal(caught), "a manual class 3 run must be refused too");
  assert.equal(caught.refusal.stage, "pre_model");
});

test("D4: a spec-flagged Class 1 agent is refused before the model call", async () => {
  let caught;
  try {
    await runAgent(approvalSpec(1, undefined, true), { trigger: "manual", input: {} });
  } catch (err) {
    caught = err;
  }
  assert.ok(isApprovalRefusal(caught), "spec requires_human_approval must gate statically");
  assert.equal(caught.refusal.stage, "pre_model");
  assert.ok(caught.refusal.reasons.some((r) => r.includes("requires_human_approval: true")));
});

test("D4: Class 0-2 advisory behaviour is untouched", () => {
  // The scope limit. No spec flag, no agent flag -> no gate, a memory line, and
  // the declared emits survive. D4 must not broaden into these.
  for (const riskClass of [0, 1, 2]) {
    assert.deepEqual(staticApprovalReasons({ risk_class: riskClass, requires_human_approval: false }), []);
    const { result, logged } = finalizeWith(riskClass, { summary: "internal", requiresHumanApproval: false });
    assert.equal(result.requiresHumanApproval, false);
    assert.equal(result.status, "advisory_complete");
    assert.equal(logged.payload.requiresHumanApproval, false);
  }
  // And the static gate lets them reach the model.
  for (const riskClass of [0, 1, 2]) {
    assert.doesNotThrow(() =>
      assertStaticApproval({ name: "t", risk_class: riskClass, requires_human_approval: false }, { trigger: "manual" }),
    );
  }
});

test("D4: a refusal is structured and machine-checkable, not a message or a boolean", () => {
  const { refusal, error } = refusalFrom(1, { requiresHumanApproval: true });
  // A caller branches on the contract, never on prose.
  assert.equal(refusal.code, "APPROVAL_REQUIRED");
  assert.ok(["pre_model", "post_response"].includes(refusal.stage));
  assert.equal(typeof refusal.agent, "string");
  assert.equal(typeof refusal.riskClass, "number");
  assert.ok(Array.isArray(refusal.reasons) && refusal.reasons.length > 0);
  assert.ok(Array.isArray(refusal.refusedBefore) && refusal.refusedBefore.length > 0);
  assert.equal(refusal.approvalEvidence, null);
  // Serialisable whole, so a caller may log the refusal rather than retype it.
  assert.deepEqual(JSON.parse(JSON.stringify(error)), refusal);
  // It is an Error, so it cannot be dropped the way a returned boolean can.
  assert.ok(error instanceof Error);
  assert.ok(error instanceof ApprovalRequiredError);
  assert.equal(error.isApprovalRefusal, true);
  // And the guard must not fire on an ordinary failure.
  assert.equal(isApprovalRefusal(new Error("ordinary")), false);
  assert.equal(isApprovalRefusal(undefined), false);
  assert.equal(isApprovalRefusal({ isApprovalRefusal: true }), false, "a lookalike without the code is not a refusal");
});

test("D4: no approval flag, token or parameter can satisfy the gate", () => {
  // Requirement: passing `true` must not create a bypass. There is no parameter
  // to pass, and these prove the shapes someone might reach for do nothing.
  for (const ctx of [
    { trigger: "manual" },
    { trigger: "manual", approved: true },
    { trigger: "manual", approval: "owner", humanApproved: true },
    { trigger: "manual", requiresHumanApproval: false },
  ]) {
    assert.throws(
      () => assertStaticApproval({ name: "t", risk_class: 4, requires_human_approval: false }, ctx),
      isApprovalRefusal,
      `class 4 must refuse regardless of ${JSON.stringify(ctx)}`,
    );
  }
  assert.throws(
    () =>
      assertDispatchApproval(
        { name: "t", risk_class: 1, requires_human_approval: false },
        { trigger: "manual", approved: true },
        { requiresHumanApproval: true, approved: true },
        true,
      ),
    isApprovalRefusal,
    "an `approved` key in the recommendation is not approval evidence",
  );
});

test("D4: the fixture lane is exempt, and the exemption is narrow", () => {
  // A fixture advertises NO emits at all, so it dispatches nothing - the risk D4
  // addresses does not exist there. Two of the three existing fixture records
  // (OFFER-F2, OFFER-F3) carry requiresHumanApproval true; gating fixtures would
  // have made those runs impossible.
  assert.doesNotThrow(() =>
    assertStaticApproval({ name: "t", risk_class: 4, requires_human_approval: true }, { trigger: "manual", fixture: true }),
  );
  assert.doesNotThrow(() =>
    assertDispatchApproval(
      { name: "t", risk_class: 4, requires_human_approval: true },
      { trigger: "manual", fixture: true },
      { requiresHumanApproval: true },
      true,
    ),
  );
  // ...and `fixture` must be a literal true, not merely truthy.
  for (const notFixture of [1, "yes", {}]) {
    assert.throws(
      () => assertStaticApproval({ name: "t", risk_class: 4 }, { trigger: "manual", fixture: notFixture }),
      isApprovalRefusal,
      `fixture: ${JSON.stringify(notFixture)} must not exempt anything`,
    );
  }
});

// ---------------------------------------------------------------------------
// TEST_FIXTURE lane (fixture.ts). Prepared, not enabled — these tests exercise
// the guard and the CLI mapping without running an agent or calling an API.
// ---------------------------------------------------------------------------

const sandboxPath = () =>
  join(tmpdir(), `arika-fx-${process.pid}-${Math.random().toString(36).slice(2)}`, "sandbox.jsonl");
const realPath = () =>
  join(tmpdir(), `arika-real-${process.pid}-${Math.random().toString(36).slice(2)}`, "runtime.jsonl");

const fxEntry = {
  trigger: "manual",
  input: { seed_brief: "TEST_FIXTURE" },
  recommendation: { summary: "ok" },
  requiresHumanApproval: false,
  riskClass: 1,
};

test("fixture: an ordinary line is unchanged — no classification key, same key order", () => {
  const file = realPath();
  const spec = { name: "t-agent", department: "02", memory_stream: file };
  writeMemory(spec, fxEntry);
  const line = JSON.parse(readFileSync(file, "utf8").trim());
  assert.equal(line.classification, undefined);
  assert.deepEqual(Object.keys(line), [
    "timestamp",
    "agent",
    "department",
    "stream",
    "event_type",
    "source",
    "payload",
  ]);
  rmSync(file, { force: true });
});

test("fixture: a fixture run writes to the sandbox stream and is marked TEST_FIXTURE", () => {
  const file = sandboxPath();
  const spec = { name: "t-agent", department: "02", memory_stream: realPath() };
  const path = writeMemory(spec, fxEntry, { fixture: true, memoryStreamOverride: file });
  assert.equal(path, file);
  const line = JSON.parse(readFileSync(file, "utf8").trim());
  assert.equal(line.classification, FIXTURE_CLASSIFICATION);
  assert.equal(line.stream, "sandbox");
  rmSync(file, { force: true });
});

test("fixture: a fixture run aimed at a real stream throws and writes nothing", () => {
  const file = realPath();
  const spec = { name: "t-agent", department: "02", memory_stream: file };
  assert.throws(
    () => writeMemory(spec, fxEntry, { fixture: true }),
    (e) => /fixture run refused/.test(e.message) && /Nothing was written/.test(e.message),
  );
  assert.equal(existsSync(file), false);
});

test("fixture: an ordinary run aimed at a sandbox stream throws and writes nothing", () => {
  const file = sandboxPath();
  const spec = { name: "t-agent", department: "02", memory_stream: file };
  assert.throws(
    () => writeMemory(spec, fxEntry),
    (e) => /ordinary run refused/.test(e.message) && /Nothing was written/.test(e.message),
  );
  assert.equal(existsSync(file), false);
});

test("fixture: the direct executor path honours the lane, not just the CLI", () => {
  const file = sandboxPath();
  const spec = {
    name: "t-offer",
    department: "02",
    execution: "prompt",
    risk_class: 1,
    requires_human_approval: false,
    memory_stream: realPath(),
    emits: [],
  };
  const result = finalizeRun(
    spec,
    { trigger: "manual", input: {}, fixture: true, memoryStreamOverride: file },
    { summary: "structural only" },
  );
  assert.equal(result.memoryPath, file);
  const line = JSON.parse(readFileSync(file, "utf8").trim());
  assert.equal(line.classification, FIXTURE_CLASSIFICATION);
  rmSync(file, { force: true });
});

test("fixture: a direct executor call cannot smuggle a fixture into a real stream", () => {
  const file = realPath();
  const spec = {
    name: "t-offer",
    department: "02",
    execution: "prompt",
    risk_class: 1,
    requires_human_approval: false,
    memory_stream: file,
    emits: [],
  };
  assert.throws(
    () => finalizeRun(spec, { trigger: "manual", input: {}, fixture: true }, { summary: "x" }),
    /fixture run refused/,
  );
  assert.equal(existsSync(file), false);
});

test("fixture: the lane is CLOSED - D21's single attempt is spent", () => {
  // D21 authorised one attempt; it was made 2026-09-21. The lane is shut again and
  // re-opening needs a fresh owner decision, so the global must read false.
  assert.equal(FIXTURE_LANE_ENABLED, false);
  // Refused through the global, with no explicit override needed.
  assert.throws(
    () => buildFixtureOptions({ fixture: true, memoryStream: "02_Offer/_memory/sandbox.jsonl" }),
    /prepared but NOT enabled/,
  );
});

test("fixture: CLI option mapping is fail-closed", () => {
  // Ordinary invocation stays empty, so nothing reaches the run context.
  assert.deepEqual(buildFixtureOptions({}), {});
  // A stream without the flag is refused rather than silently honoured.
  assert.throws(() => buildFixtureOptions({ memoryStream: sandboxPath() }), /requires --fixture/);
  // With the lane enabled, --fixture still demands an explicit destination.
  assert.throws(() => buildFixtureOptions({ fixture: true }, true), /requires --memory-stream/);
  // Only the one approved destination is accepted (see the exact-path test below).
  const approved = "02_Offer/_memory/sandbox.jsonl";
  const opts = buildFixtureOptions({ fixture: true, memoryStream: approved }, true);
  assert.deepEqual(opts, { fixture: true, memoryStreamOverride: approved });
});

test("fixture: sandbox streams are identified by filename, on both separators", () => {
  assert.equal(isSandboxStream("02_Offer/_memory/sandbox.jsonl"), true);
  assert.equal(isSandboxStream(String.raw`02_Offer\_memory\sandbox.jsonl`), true);
  assert.equal(isSandboxStream("02_Offer/_memory/runtime.jsonl"), false);
  assert.throws(() => assertStreamMatchesMode("a/runtime.jsonl", true), /fixture run refused/);
  assert.throws(() => assertStreamMatchesMode("a/sandbox.jsonl", false), /ordinary run refused/);
});

// ---------------------------------------------------------------------------
// Pre-approval hardening: exact destination, entry-point gate, input pins.
// ---------------------------------------------------------------------------

const APPROVED = "02_Offer/_memory/sandbox.jsonl";
const goodBrief = [
  "TEST_FIXTURE - simulated sandbox unit.",
  "Unit: A001-P07. Group: A001.",
  "SR-1 unresolvable archetype. SR-2 anti-ICP. SR-3 above every H-band.",
].join("\n");
const neverResolve = () => join(tmpdir(), `arika-absent-${Math.random().toString(36).slice(2)}`);

// D21 is SPENT in the real registry, so it cannot pass the gate. Tests that
// exercise its rules pass an explicitly approved COPY - proving the rules without
// re-opening it. (OFFER-F2's tests live in fixture-f2.test.mjs.)
const D21 = FIXTURE_AUTHORISATIONS.find((a) => a.id === "A001-D21");
const approved = (...auths) => auths.map((a) => ({ ...a, status: "approved" }));

test("fixture: the approved destination is the exact path, not just the basename", () => {
  assertApprovedFixtureStream(APPROVED); // the one allowed value
  // Another department's sandbox passes a basename check and must still be refused.
  assert.throws(() => assertApprovedFixtureStream("01_Sector/_memory/sandbox.jsonl"), /not the approved destination/);
  assert.throws(() => assertApprovedFixtureStream("04_Content/_memory/sandbox.jsonl"), /not the approved destination/);
});

test("fixture: absolute paths and traversals are refused", () => {
  assert.throws(() => assertApprovedFixtureStream("C:/tmp/sandbox.jsonl"), /absolute path/);
  assert.throws(() => assertApprovedFixtureStream("/tmp/sandbox.jsonl"), /absolute path/);
  assert.throws(() => assertApprovedFixtureStream(String.raw`C:\tmp\sandbox.jsonl`), /absolute path/);
  assert.throws(() => assertApprovedFixtureStream("02_Offer/_memory/../../sandbox.jsonl"), /traversal/);
  assert.throws(() => assertApprovedFixtureStream("../02_Offer/_memory/sandbox.jsonl"), /traversal/);
});

test("fixture: the entry gate fires BEFORE any model call", async () => {
  // A prompt agent needs ANTHROPIC_API_KEY to reach the model, so if the gate ran
  // late the failure here would be a key error. It is not - it is the refused
  // config, proving the gate runs first and costs no API call.
  //
  // A NON-approved agent is used deliberately: if the lane were ever re-opened, an
  // approved-agent spec here would pass the gate and call the model for real. This
  // test must never be able to do that, whatever the switch says.
  //
  // The assertion accepts either refusal - closed lane, or wrong agent - so it stays
  // correct in both switch states. What it pins is the ordering: the failure is a
  // gate refusal, never a missing-key error, which is only possible if the gate runs
  // before the model call.
  const spec = { name: "sector-icp-fit", department: "01", execution: "prompt", risk_class: 1,
                 requires_human_approval: false, memory_stream: APPROVED, emits: [] };
  await assert.rejects(
    () => runAgent(spec, { trigger: "manual", input: { seed_brief: goodBrief },
                           fixture: true, memoryStreamOverride: APPROVED }),
    (e) =>
      /prepared but NOT enabled|not the approved agent/.test(e.message) &&
      !/ANTHROPIC_API_KEY/.test(e.message),
  );
});

test("safety: no test can reach a model - every runAgent call is gate-refused", async () => {
  // A standing guard on the suite itself. runAgent is the only path to the model,
  // and the fixture lane is the only way a test could legitimately drive it. With
  // the lane closed, any fixture invocation is refused before the model; an
  // ordinary-mode invocation of a prompt agent is not attempted anywhere in this
  // file. If someone later adds one, this test is the reminder to check it.
  assert.equal(FIXTURE_LANE_ENABLED, false, "a closed lane is what keeps the suite offline");
  const spec = { name: "offer-orchestrator", department: "02", execution: "prompt", risk_class: 1,
                 requires_human_approval: false, memory_stream: APPROVED, emits: [] };
  await assert.rejects(
    () => runAgent(spec, { trigger: "manual", input: { seed_brief: goodBrief },
                           fixture: true, memoryStreamOverride: APPROVED }),
    /prepared but NOT enabled/,
  );
});

test("fixture: an ordinary run is untouched by the gate", () => {
  assertFixturePreconditions("any-agent", { trigger: "manual" });
  assertFixturePreconditions("any-agent", { input: { a: 1 } });
  // An override without the flag is a mistake, not a silent promotion.
  assert.throws(() => assertFixturePreconditions("any-agent", { memoryStreamOverride: APPROVED }),
    /requires fixture mode/);
});

test("fixture: the gate pins the agent and the destination", () => {
  const ok = { fixture: true, memoryStreamOverride: APPROVED, input: { seed_brief: goodBrief } };
  const opts = { enabled: true, resolve: neverResolve, authorisations: approved(D21) };
  assertFixturePreconditions("offer-orchestrator", ok, opts); // passes
  assert.throws(() => assertFixturePreconditions("sector-icp-fit", ok, opts), /not the approved agent/);
  assert.throws(
    () => assertFixturePreconditions("offer-orchestrator",
      { ...ok, memoryStreamOverride: "01_Sector/_memory/sandbox.jsonl" }, opts),
    /not the approved destination/,
  );
  assert.throws(() => assertFixturePreconditions("offer-orchestrator", { fixture: true, input: {} }, opts),
    /a destination is required/);
});

test("fixture: the brief must declare the marker and exactly one sandbox unit", () => {
  const opts = { enabled: true, resolve: neverResolve, authorisations: approved(D21) };
  const run = (seed_brief) =>
    assertFixturePreconditions("offer-orchestrator",
      { fixture: true, memoryStreamOverride: APPROVED, input: { seed_brief } }, opts);
  assert.throws(() => run(""), /non-empty string/);
  assert.throws(() => run("A001-P07 only, no marker"), /does not declare TEST_FIXTURE/);
  assert.throws(() => run("TEST_FIXTURE but no unit named"), /does not declare A001-P07/);
  assert.throws(() => run(`${goodBrief} and A001-P08 linked`), /names other sandbox units \(A001-P08\)/);
  assert.throws(() => run(`${goodBrief} see PILOT-H-001`), /names a real pilot ID/);
  assert.throws(
    () => assertFixturePreconditions("offer-orchestrator",
      { fixture: true, memoryStreamOverride: APPROVED, input: {} }, opts),
    /non-empty string/,
  );
});

test("fixture: the lane is single-use - a destination that exists is refused", () => {
  const used = join(tmpdir(), `arika-used-${process.pid}-${Math.random().toString(36).slice(2)}.jsonl`);
  writeFileSync(used, "{}\n");
  assert.throws(
    () => assertFixturePreconditions("offer-orchestrator",
      { fixture: true, memoryStreamOverride: APPROVED, input: { seed_brief: goodBrief } },
      { enabled: true, resolve: () => used, authorisations: approved(D21) }),
    /one-run lane is spent/,
  );
  rmSync(used, { force: true });
});

test("fixture: CLI mapping validates the destination too", () => {
  assert.throws(() => buildFixtureOptions({ fixture: true, memoryStream: "/tmp/sandbox.jsonl" }, true), /absolute path/);
  assert.throws(() => buildFixtureOptions({ fixture: true, memoryStream: "01_Sector/_memory/sandbox.jsonl" }, true), /not the approved destination/);
  assert.deepEqual(buildFixtureOptions({ fixture: true, memoryStream: APPROVED }, true),
    { fixture: true, memoryStreamOverride: APPROVED });
});

// ---------------------------------------------------------------------------
// A rejected brief must not advertise the event that would advance it.
// Found by the A001 D21 fixture run (OFFER_OS.md §12). No model is called: every
// case below drives finalizeRun with a canned recommendation.
// ---------------------------------------------------------------------------

const tmpStream = () =>
  join(tmpdir(), `arika-emit-${process.pid}-${Math.random().toString(36).slice(2)}.jsonl`);

// The real orchestrator spec, re-pointed at a temp file so no real log is touched.
function orchestratorWith(file) {
  const { agents } = loadAgents();
  const spec = agents.get("offer-orchestrator");
  return { ...spec, memory_stream: file };
}

const rec = (registry_action) => ({
  summary: "canned",
  recommendedActions: [],
  requiresHumanApproval: false,
  approvalReasons: [],
  riskLevel: "low",
  registry_action,
});

test("emits: a reject withholds OFFER_BRIEF_RECEIVED and nothing else", () => {
  assert.deepEqual(advertisedEmits(["OFFER_BRIEF_RECEIVED"], { registry_action: "reject" }), []);
  // Only the named event is withheld; an unrelated emit survives a reject.
  assert.deepEqual(advertisedEmits(["OFFER_ENGINEERED"], { registry_action: "reject" }), ["OFFER_ENGINEERED"]);
  // No registry_action at all: nothing is withheld.
  assert.deepEqual(advertisedEmits(["OFFER_BRIEF_RECEIVED"], {}), ["OFFER_BRIEF_RECEIVED"]);
  assert.deepEqual(advertisedEmits(undefined, { registry_action: "reject" }), []);
});

test("emits: reject through the normal finalize path, with the real orchestrator spec", () => {
  const file = tmpStream();
  const spec = orchestratorWith(file);
  // The contract itself is unchanged: the spec still declares the emit.
  assert.deepEqual(spec.emits, ["OFFER_BRIEF_RECEIVED"]);
  const recommendation = rec("reject");
  try {
    const result = finalizeRun(spec, { trigger: "manual", input: { seed_brief: "x" } }, recommendation);
    assert.deepEqual(result.emitted, [], "a rejected brief must not advertise OFFER_BRIEF_RECEIVED");
    // The recommendation is preserved, unmutated.
    assert.equal(result.recommendation, recommendation);
    assert.equal(result.recommendation.registry_action, "reject");
    // And the memory record is still written, with the reject intact.
    const logged = JSON.parse(readFileSync(file, "utf8").trim());
    assert.equal(logged.agent, "offer-orchestrator");
    assert.equal(logged.payload.recommendation.registry_action, "reject");
  } finally {
    rmSync(file, { force: true });
  }
});

test("emits: other registry actions still advertise - no broadening, no automatic approval", () => {
  // Each has a human-reviewed path forward (PG3; RD7 for needs_more_seed_data), so
  // the event stays advertised. Advertising is not approval: nothing publishes it,
  // and the approval gate is decided independently of it.
  for (const action of ["add_new_offer", "update_existing_offer", "needs_more_seed_data"]) {
    const file = tmpStream();
    try {
      const result = finalizeRun(orchestratorWith(file), { trigger: "manual", input: {} }, rec(action));
      assert.deepEqual(result.emitted, ["OFFER_BRIEF_RECEIVED"], `${action} should be unchanged`);
      assert.equal(result.recommendation.registry_action, action);
      assert.equal(result.requiresHumanApproval, false, `${action}: no approval was invented`);
    } finally {
      rmSync(file, { force: true });
    }
  }
});
