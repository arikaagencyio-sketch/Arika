// OFFER-F2 fixture authorisation - prepared, NOT enabled.
//
// Every test here is offline. Nothing calls runAgent with a passing
// configuration, nothing constructs a model client, and every memory write goes
// to a temp directory. The real registry is never mutated: tests that must pass
// the gate use an explicitly approved COPY of an authorisation.
import { test } from "node:test";
import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { existsSync, readFileSync, rmSync } from "node:fs";

import { finalizeRun } from "../dist/executor.js";
import { loadAgents } from "../dist/agent-registry.js";
import { writeMemory } from "../dist/memory-writer.js";
import { repoRoot } from "../dist/paths.js";
import {
  assertApprovedFixtureInput,
  assertApprovedFixtureStream,
  assertFixturePreconditions,
  FIXTURE_AUTHORISATIONS,
  FIXTURE_LANE_ENABLED,
  isSandboxStream,
  validateAuthorisations,
} from "../dist/fixture.js";

const D21 = FIXTURE_AUTHORISATIONS.find((a) => a.id === "A001-D21");
const F2 = FIXTURE_AUTHORISATIONS.find((a) => a.id === "OFFER-F2");
const approved = (...auths) => auths.map((a) => ({ ...a, status: "approved" }));
const neverResolve = () => join(tmpdir(), `arika-absent-${Math.random().toString(36).slice(2)}`);
const tmpDir = () => join(tmpdir(), `arika-f2-${process.pid}-${Math.random().toString(36).slice(2)}`);
const sha256 = (s) => createHash("sha256").update(s, "utf8").digest("hex");

// The one input the draft decision authorises, read from the decision record
// itself - so the record, the code pin and this test cannot silently diverge.
function recordedF2Input() {
  const text = readFileSync(join(repoRoot, "02_Offer", "OFFER_OS.md"), "utf8");
  const blocks = [...text.matchAll(/```json\r?\n([^\r\n]+)\r?\n```/g)]
    .map((m) => m[1])
    .filter((b) => b.includes("OFFER-F2"));
  assert.equal(blocks.length, 1, "OFFER_OS.md must hold exactly one OFFER-F2 input block");
  return JSON.parse(blocks[0]); // the same call cli.ts makes on --input
}

const entry = {
  trigger: "manual",
  input: { seed_brief: "x" },
  recommendation: { summary: "canned" },
  requiresHumanApproval: false,
  riskClass: 1,
};

test("f2: the registry holds D21 and OFFER-F2 both SPENT, and the lane is closed", () => {
  // State history: OFFER-F2 was `draft`, the owner approved it 2026-09-22, its one
  // attempt was made the same day, and it is now `spent` (OFFER_OS.md §8).
  assert.equal(FIXTURE_LANE_ENABLED, false);
  assert.equal(D21.status, "spent");
  assert.equal(F2.status, "spent");
  assert.equal(F2.agent, "offer-oeos-engineer");
  assert.equal(F2.stream, "02_Offer/_memory/sandbox-offer-f2.jsonl");
  assert.notEqual(F2.stream, D21.stream, "each authorisation has its own stream");
});

test("f2: even with the switch on, neither real authorisation can run", () => {
  // Two locks: the switch AND an approved status. Turning on only the switch is not enough.
  const input = recordedF2Input();
  assert.throws(
    () => assertFixturePreconditions("offer-oeos-engineer",
      { fixture: true, memoryStreamOverride: F2.stream, input }, { enabled: true, resolve: neverResolve }),
    /OFFER-F2 is SPENT/,
  );
  assert.throws(
    () => assertFixturePreconditions("offer-orchestrator",
      { fixture: true, memoryStreamOverride: D21.stream, input: { seed_brief: "TEST_FIXTURE A001-P07" } },
      { enabled: true, resolve: neverResolve }),
    /A001-D21 is SPENT/,
  );
});

test("f2: the recorded input matches the pinned hash and OEOS's actual input schema", () => {
  const input = recordedF2Input();
  // OEOS declares exactly one input, seed_brief: { type: string }.
  const { agents } = loadAgents();
  const oeos = agents.get("offer-oeos-engineer");
  assert.deepEqual(Object.keys(oeos.inputs), ["seed_brief"]);
  assert.equal(oeos.inputs.seed_brief.type, "string");
  // The approved object has exactly that key, with a string value.
  assert.deepEqual(Object.keys(input), ["seed_brief"]);
  assert.equal(typeof input.seed_brief, "string");
  // The record and the code pin agree byte for byte.
  assert.equal(sha256(input.seed_brief), F2.inputSha256);
  // And it passes the authorisation's own input rules.
  assertApprovedFixtureInput(input, F2);
});

test("f2: the exact input passes the full gate only when approved; one byte off fails", () => {
  const input = recordedF2Input();
  const opts = { enabled: true, resolve: neverResolve, authorisations: approved(F2) };
  assertFixturePreconditions("offer-oeos-engineer",
    { fixture: true, memoryStreamOverride: F2.stream, input }, opts); // passes
  const tampered = { seed_brief: input.seed_brief.replace("Q2. Price band: none approved.", "Q2. Price band: none approved!") };
  assert.throws(
    () => assertFixturePreconditions("offer-oeos-engineer",
      { fixture: true, memoryStreamOverride: F2.stream, input: tampered }, opts),
    /does not match the approved input for OFFER-F2/,
  );
});

test("f2: the input rules refuse A001, real pilot IDs, currency and missing markers", () => {
  const brief = recordedF2Input().seed_brief;
  const check = (seed_brief) => () => assertApprovedFixtureInput({ seed_brief }, F2);
  assert.throws(check(`${brief} See A001-P07.`), /names an A001 sandbox record/);
  assert.throws(check(`${brief} See PILOT-H-001.`), /names a real pilot ID/);
  assert.throws(check(`${brief} About $500.`), /contains a currency figure/);
  assert.throws(check(`${brief} In KES.`), /contains a currency figure/);
  assert.throws(check(brief.replace("NON-PRICING", "PRICING")), /does not declare NON-PRICING/);
  assert.throws(check(brief.replace("PHASE 11: BLOCKED", "PHASE 11: OPEN")), /does not declare PHASE 11: BLOCKED/);
  assert.throws(check(""), /non-empty string/);
});

test("f2: each authorisation is pinned to its own agent", () => {
  const opts = { enabled: true, resolve: neverResolve, authorisations: approved(D21, F2) };
  const input = recordedF2Input();
  // OEOS may not run on D21's stream, and the orchestrator may not run on F2's.
  assert.throws(
    () => assertFixturePreconditions("offer-oeos-engineer",
      { fixture: true, memoryStreamOverride: D21.stream, input }, opts),
    /not the approved agent for A001-D21/,
  );
  assert.throws(
    () => assertFixturePreconditions("offer-orchestrator",
      { fixture: true, memoryStreamOverride: F2.stream, input }, opts),
    /not the approved agent for OFFER-F2/,
  );
});

test("f2: this fixture cannot reach a real or unregistered stream", () => {
  const opts = { enabled: true, resolve: neverResolve, authorisations: approved(F2) };
  const input = recordedF2Input();
  for (const dest of [
    "02_Offer/_memory/runtime.jsonl",                // the real Offer stream
    "02_Offer/_memory/sandbox-other.jsonl",          // sandbox-named but unregistered
    "01_Sector/_memory/sandbox-offer-f2.jsonl",      // right name, wrong department
    "02_Offer/_memory/../_memory/sandbox-offer-f2.jsonl",
    "C:/x/sandbox-offer-f2.jsonl",
  ]) {
    assert.throws(
      () => assertFixturePreconditions("offer-oeos-engineer",
        { fixture: true, memoryStreamOverride: dest, input }, opts),
      /not the approved destination|traversal|absolute path/,
      dest,
    );
  }
  // And at the writer: a fixture line aimed at a real stream is refused before any write.
  const dir = tmpDir();
  const real = join(dir, "runtime.jsonl");
  assert.throws(
    () => writeMemory({ name: "offer-oeos-engineer", department: "02", memory_stream: real }, entry, { fixture: true }),
    /fixture run refused/,
  );
  assert.equal(existsSync(real), false);
});

test("f2: ordinary runs cannot write to EITHER fixture stream", () => {
  assert.equal(isSandboxStream(F2.stream), true);
  assert.equal(isSandboxStream(D21.stream), true);
  const dir = tmpDir();
  for (const name of ["sandbox-offer-f2.jsonl", "sandbox.jsonl"]) {
    const file = join(dir, name);
    const spec = { name: "offer-oeos-engineer", department: "02", execution: "prompt", risk_class: 1,
                   requires_human_approval: false, memory_stream: file, emits: [] };
    // Directly at the writer...
    assert.throws(() => writeMemory(spec, entry), /ordinary run refused/, name);
    // ...and through the normal finalize path.
    assert.throws(() => finalizeRun(spec, { trigger: "manual", input: {} }, { summary: "x" }),
      /ordinary run refused/, name);
    assert.equal(existsSync(file), false, `${name} must not be created`);
  }
  rmSync(dir, { recursive: true, force: true });
});

test("f2: a fixture stream is only ever a registered path, never a basename match", () => {
  // Reserved names are wide on purpose (any sandbox*.jsonl blocks ordinary runs)...
  assert.equal(isSandboxStream("x/sandbox-anything.jsonl"), true);
  assert.equal(isSandboxStream("x/runtime.jsonl"), false);
  // ...but a fixture may run only on a path the registry names.
  assert.throws(() => assertApprovedFixtureStream("02_Offer/_memory/sandbox-anything.jsonl"),
    /not the approved destination/);
  assert.equal(assertApprovedFixtureStream(F2.stream).id, "OFFER-F2");
});

test("f2: a malformed registry fails closed", () => {
  const ok = { ...F2 };
  assert.throws(() => validateAuthorisations([ok, { ...ok, id: "X" }]), /share/);
  assert.throws(() => validateAuthorisations([ok, { ...ok, stream: "02_Offer/_memory/other.jsonl", id: "Y" }]),
    /not sandbox-named/);
  assert.throws(() => validateAuthorisations([{ ...ok, stream: "/abs/sandbox-z.jsonl" }]), /repo-relative/);
  assert.throws(() => validateAuthorisations([ok, { ...ok, stream: "02_Offer/_memory/sandbox-z.jsonl" }]),
    /duplicate id/);
  assert.throws(
    () => validateAuthorisations([{ ...ok, forbidden: [{ pattern: /A001/, reason: "r" }] }]),
    /lacks the g flag/,
  );
  validateAuthorisations(FIXTURE_AUTHORISATIONS); // the real one is valid
});

test("f2: the OEOS output-schema limits the draft records still hold", () => {
  // These are facts the draft's 'cannot prove' list depends on. If the contract
  // changes, this test fails and the limits must be re-read.
  const { agents } = loadAgents();
  const out = agents.get("offer-oeos-engineer").output_schema;
  assert.equal(out.additionalProperties, false);
  const fields = Object.keys(out.properties);
  assert.equal(fields.some((f) => /question/i.test(f)), false, "no field holds unresolved questions");
  assert.ok(out.properties.tiers.items.required.includes("investment"), "every tier must carry an investment string");
  assert.equal(out.properties.tiers.minItems, undefined, "tiers may be empty");
  assert.equal(out.properties.phases.minItems, undefined, "Phase 11 may be omitted");
  const phaseFields = Object.keys(out.properties.phases.items.properties);
  assert.equal(phaseFields.some((f) => /status|block/i.test(f)), false, "no phase carries a status field");
});

// ---------------------------------------------------------------------------
// Isolation rule: a TEST_FIXTURE run advertises no emits. Driven through the
// normal finalizeRun path with canned recommendations - no model is called, and
// every line goes to a temp directory.
// ---------------------------------------------------------------------------

const PAYLOAD_KEYS = ["trigger", "input", "recommendation", "requiresHumanApproval", "riskClass"];

function realSpec(name, streamFile) {
  const { agents } = loadAgents();
  return { ...agents.get(name), memory_stream: streamFile };
}

test("f2: an OFFER-F2 fixture run returns emitted: [] - OFFER_ENGINEERED included", () => {
  const dir = tmpDir();
  const fixtureStream = join(dir, "sandbox-offer-f2.jsonl");
  const spec = realSpec("offer-oeos-engineer", join(dir, "runtime.jsonl"));
  // The agent's declared contract is unchanged: it still declares the emit.
  assert.deepEqual(spec.emits, ["OFFER_ENGINEERED"]);
  const input = recordedF2Input();
  const recommendation = { summary: "structural only", requiresHumanApproval: false };
  const result = finalizeRun(
    spec,
    { trigger: "manual", input, fixture: true, memoryStreamOverride: fixtureStream },
    recommendation,
  );
  assert.deepEqual(result.emitted, [], "a fixture must not advertise OFFER_ENGINEERED");
  assert.equal(result.recommendation, recommendation, "recommendation returned unmutated");
  // The memory payload is exactly what it was before this rule existed.
  const line = JSON.parse(readFileSync(fixtureStream, "utf8").trim());
  assert.equal(line.classification, "TEST_FIXTURE");
  assert.deepEqual(Object.keys(line.payload), PAYLOAD_KEYS);
  assert.deepEqual(line.payload.input, input);
  assert.equal(existsSync(join(dir, "runtime.jsonl")), false, "nothing reached the spec's own stream");
  rmSync(dir, { recursive: true, force: true });
});

test("f2: ordinary OEOS output keeps its advertised emits", () => {
  const dir = tmpDir();
  const stream = join(dir, "runtime.jsonl");
  const result = finalizeRun(
    realSpec("offer-oeos-engineer", stream),
    { trigger: "manual", input: { seed_brief: "x" } },
    { summary: "ordinary" },
  );
  assert.deepEqual(result.emitted, ["OFFER_ENGINEERED"], "ordinary behaviour is unchanged");
  const line = JSON.parse(readFileSync(stream, "utf8").trim());
  assert.equal(line.classification, undefined);
  assert.deepEqual(Object.keys(line.payload), PAYLOAD_KEYS);
  rmSync(dir, { recursive: true, force: true });
});

test("f2: the rule covers every fixture run, not only OEOS", () => {
  // The orchestrator's add_new_offer advertises OFFER_BRIEF_RECEIVED when ordinary,
  // and nothing when it is a fixture.
  const dir = tmpDir();
  const rec = { summary: "x", requiresHumanApproval: false, registry_action: "add_new_offer" };
  const ordinary = finalizeRun(realSpec("offer-orchestrator", join(dir, "runtime.jsonl")),
    { trigger: "manual", input: {} }, rec);
  assert.deepEqual(ordinary.emitted, ["OFFER_BRIEF_RECEIVED"]);
  const fixture = finalizeRun(realSpec("offer-orchestrator", join(dir, "runtime.jsonl")),
    { trigger: "manual", input: {}, fixture: true, memoryStreamOverride: join(dir, "sandbox.jsonl") }, rec);
  assert.deepEqual(fixture.emitted, []);
  rmSync(dir, { recursive: true, force: true });
});
