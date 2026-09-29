/**
 * OFFER-F3 — offline tests for the PREPARED, UNAPPROVED authorisation.
 *
 * F3 would run `offer-orchestrator` once on a brief rebuilt from three pinned artefacts: the
 * synthetic Sector record, and the S10 fixture packet and fixture skill-run record that
 * SECTOR-SF2 produced. Nothing here runs the agent: every test is a pure check of the gate, the
 * registry and the recorded input. No network, no model call, no connector.
 */
import { test } from "node:test";
import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { readFileSync } from "node:fs";
import { join } from "node:path";

import {
  FIXTURE_LANE_ENABLED,
  FIXTURE_AUTHORISATIONS,
  assertFixturePreconditions,
  assertApprovedFixtureInput,
  assertApprovedFixtureStream,
  validateAuthorisations,
} from "../dist/fixture.js";
import { repoRoot } from "../dist/paths.js";

const sha = (b) => createHash("sha256").update(b).digest("hex");
const readRepo = (p) => readFileSync(join(repoRoot, p));
const F3 = FIXTURE_AUTHORISATIONS.find((a) => a.id === "OFFER-F3");
const STREAM = "02_Offer/_memory/sandbox-offer-f3.jsonl";
const INPUT_FILE = "02_Offer/fixtures/OFFER-F3.input.json";
const input = JSON.parse(readRepo(INPUT_FILE).toString("utf8"));
const approved = (auth, status) => [{ ...auth, status }];
const run = (agent, ctx, auths, enabled = true) =>
  assertFixturePreconditions(agent, ctx, { enabled, authorisations: auths, resolve: (s) => join(repoRoot, s) });

// ---------------------------------------------------------------- the spent state --
// Until 2026-09-29 these two asserted the pre-run state (draft, no destination file). The owner
// approved F3, its ONE attempt was made, and the lane was closed again in the same turn.
const F3_LOG_SHA = "da0b7fe4368d1ef5f96a627ca41b75a9c354075acaa1f4b787daaadfd133ef46";

test("f3: the authorisation is SPENT and the lane is closed again", () => {
  assert.ok(F3, "OFFER-F3 must exist in the registry");
  assert.equal(F3.status, "spent", "its one attempt has been used");
  assert.equal(F3.agent, "offer-orchestrator");
  assert.equal(F3.stream, STREAM);
  assert.equal(FIXTURE_LANE_ENABLED, false, "the master switch is off again");
  assert.equal(
    FIXTURE_AUTHORISATIONS.filter((a) => a.status === "approved").length,
    0,
    "no authorisation may sit approved",
  );
  validateAuthorisations(FIXTURE_AUTHORISATIONS); // ids and streams stay unique
});

test("f3: the one attempt left exactly one marked line, unaltered", () => {
  const raw = readRepo(STREAM);
  assert.equal(sha(raw), F3_LOG_SHA, "the fixture log changed after the attempt");
  const lines = raw.toString("utf8").split("\n").filter(Boolean);
  assert.equal(lines.length, 1, "one attempt, one line");
  const rec = JSON.parse(lines[0]);
  assert.equal(rec.classification, "TEST_FIXTURE");
  assert.equal(rec.agent, "offer-orchestrator");
  assert.equal(rec.payload.recommendation.registry_action, "needs_more_seed_data");
  assert.equal(rec.payload.input.seed_brief, input.seed_brief, "the recorded input is the pinned one");
});

// ---------------------------------------------------------------- fails closed --
test("f3: a draft authorisation is refused before any model call", () => {
  // F3 itself is spent now, so the draft case is exercised on an explicitly drafted copy -
  // the guard must hold for any future authorisation, not just this one.
  assert.throws(
    () => run("offer-orchestrator", { fixture: true, memoryStreamOverride: STREAM, input }, approved(F3, "draft")),
    /DRAFT authorisation/,
  );
});

test("f3: a spent authorisation is refused too", () => {
  assert.throws(
    () => run("offer-orchestrator", { fixture: true, memoryStreamOverride: STREAM, input }, approved(F3, "spent")),
    /SPENT/,
  );
});

test("f3: even approved, the closed lane refuses first", () => {
  assert.throws(
    () =>
      assertFixturePreconditions(
        "offer-orchestrator",
        { fixture: true, memoryStreamOverride: STREAM, input },
        { enabled: FIXTURE_LANE_ENABLED, authorisations: approved(F3, "approved") },
      ),
    /prepared but NOT enabled/,
  );
});

// ---------------------------------------------------------------- only this agent, stream, input --
test("f3: only offer-orchestrator may use it", () => {
  const auths = approved(F3, "approved");
  assert.throws(
    () => run("offer-oeos-engineer", { fixture: true, memoryStreamOverride: STREAM, input }, auths),
    /not the approved agent/,
  );
  assert.throws(
    () => run("sector-icp-fit", { fixture: true, memoryStreamOverride: STREAM, input }, auths),
    /not the approved agent/,
  );
});

test("f3: the destination is exact — no other sandbox, no traversal, no absolute path", () => {
  const auths = approved(F3, "approved");
  for (const bad of [
    "02_Offer/_memory/sandbox.jsonl",
    "02_Offer/_memory/sandbox-offer-f2.jsonl",
    "02_Offer/_memory/runtime.jsonl",
    "01_Sector/_memory/skill_runs-sandbox.jsonl",
  ]) {
    assert.throws(() => assertApprovedFixtureStream(bad, auths), /not the approved destination/);
  }
  assert.throws(() => assertApprovedFixtureStream("/tmp/sandbox-offer-f3.jsonl", auths), /absolute path/);
  assert.throws(() => assertApprovedFixtureStream("02_Offer/../sandbox-offer-f3.jsonl", auths), /traversal/);
  assert.equal(assertApprovedFixtureStream(STREAM, auths).id, "OFFER-F3");
});

test("f3: the input is pinned by hash — a single edited character is refused", () => {
  assertApprovedFixtureInput(input, { ...F3, status: "approved" }); // the exact recorded brief passes
  assert.equal(sha(Buffer.from(input.seed_brief, "utf8")), F3.inputSha256);
  const tampered = { seed_brief: input.seed_brief.replace("SIMULATED_VERDICT: in scope", "VERDICT: in scope") };
  assert.throws(() => assertApprovedFixtureInput(tampered, F3), /sha256 mismatch|does not declare/);
  assert.throws(() => assertApprovedFixtureInput({ seed_brief: "" }, F3), /non-empty string/);
  assert.throws(() => assertApprovedFixtureInput({}, F3), /non-empty string/);
});

test("f3: the brief carries no forbidden content", () => {
  for (const f of F3.forbidden) {
    assert.equal(input.seed_brief.match(f.pattern), null, `brief ${f.reason}`);
  }
});

// ---------------------------------------------------------------- provenance cannot drift --
test("f3: the brief names the CURRENT hashes of the three artefacts it was built from", () => {
  const record = sha(readRepo("01_Sector/fixtures/SYN-S10-01.sector-record.json"));
  const packet = sha(readRepo("01_Sector/fixtures/SYN-S10-01.s10-packet-sf2.json"));
  const sf2Line = sha(
    readRepo("01_Sector/_memory/skill_runs-sandbox.jsonl").toString("utf8").split("\n").filter(Boolean)[1] + "\n",
  );
  for (const [name, hash] of [["Sector record", record], ["S10 fixture packet", packet], ["fixture skill run", sf2Line]]) {
    assert.ok(input.seed_brief.includes(hash), `the brief must name the current ${name} hash — it drifted`);
    assert.ok(F3.requiredMarkers.includes(hash), `${name} hash must be a required marker`);
  }
});

test("f3: the brief states the fixture's limits rather than claiming a hand-off", () => {
  const b = input.seed_brief;
  for (const phrase of [
    "FIXTURE EVIDENCE, NOT A REAL HAND-OFF",
    "no real CRM lead record was tagged",
    "nothing was delivered to any destination",
    "remain unresolved",
    "cannot satisfy or bypass readiness gates PG1, PG2 or PG3",
    "not a fit verdict",
    "authorises no registry change",
  ]) {
    assert.ok(b.includes(phrase), `the brief must state: ${phrase}`);
  }
  assert.equal(/\bdelivered\b(?!.*(nothing|not))/.test(b.split("\n")[0]), false);
});

// ---------------------------------------------------------------- neighbours untouched --
test("f3: the D21 and F2 fixture logs, and the real runtime log, are byte-unchanged", () => {
  assert.equal(sha(readRepo("02_Offer/_memory/sandbox.jsonl")).slice(0, 16), "5c7aa1d7ae47207a");
  assert.equal(sha(readRepo("02_Offer/_memory/sandbox-offer-f2.jsonl")).slice(0, 16), "61772b957730cae7");
  assert.equal(sha(readRepo("02_Offer/_memory/runtime.jsonl")).slice(0, 16), "0295b17389134e3c");
});

test("f3: the earlier authorisations stay spent and keep their own streams", () => {
  const byId = Object.fromEntries(FIXTURE_AUTHORISATIONS.map((a) => [a.id, a]));
  assert.equal(byId["A001-D21"].status, "spent");
  assert.equal(byId["OFFER-F2"].status, "spent");
  assert.notEqual(byId["OFFER-F2"].stream, F3.stream);
  assert.notEqual(byId["A001-D21"].stream, F3.stream);
});

// ---------------------------------------------------------------- ordinary runs unaffected --
test("f3: an ordinary run is untouched by the new authorisation", () => {
  assert.doesNotThrow(() => run("offer-orchestrator", { input }, FIXTURE_AUTHORISATIONS, false));
  assert.throws(
    () => run("offer-orchestrator", { memoryStreamOverride: STREAM, input }, FIXTURE_AUTHORISATIONS, false),
    /memoryStreamOverride requires fixture mode/,
  );
});
