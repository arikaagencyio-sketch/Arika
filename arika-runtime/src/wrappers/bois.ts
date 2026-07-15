import { spawn } from "node:child_process";
import { existsSync } from "node:fs";
import { join } from "node:path";
import { repoRoot } from "../paths.js";
import type { AgentSpec } from "../spec-schema.js";
import type { RunContext } from "../executor.js";

/**
 * Wraps Branding's BOIS ("Brand Operating Intelligence System") without porting it.
 *
 * BOIS is Python and owns its own reasoning — `bois/core/synthesis/engine.py`'s
 * `BrandAgentRuntime`, the same relationship finos-plugin has with its
 * `ClaudeAgentRuntime`. This runtime therefore *delegates* rather than
 * reimplementing the model call: a TS process cannot import Python in-process, so we
 * shell out to `bois/executions/run_brand_task.py`, which speaks JSON in / JSON out.
 *
 * Why the LLM call lives in Python and not here: BOIS' governance validation, 15-dimension
 * scoring, and append-only memory store are all Python, and `EXECUTION_STAGES` places
 * `output_synthesis` *between* `agent_activation` and `governance_validation` — inside
 * BOIS' own pipeline. Calling Claude from TS would split that pipeline across two
 * languages and round-trip every result back into Python anyway.
 *
 * BOIS is left structurally intact; the only additions were its missing synthesis stage
 * and this entry point.
 */

const BOIS_ROOT = join(repoRoot, "12_Branding", "bois");
const ENTRY_POINT = join(BOIS_ROOT, "executions", "run_brand_task.py");
const TIMEOUT_MS = 180_000;

interface BoisRequest {
  mode: string;
  client_id: string;
  task: string;
  deliverable: string;
  positioning_objective?: string;
  communication_goal?: string;
  campaign_objective?: string;
  synthesize: boolean;
}

function pythonBin(): string {
  return process.env.BOIS_PYTHON ?? (process.platform === "win32" ? "python" : "python3");
}

function buildRequest(spec: AgentSpec, ctx: RunContext): BoisRequest {
  const input = (ctx.input ?? {}) as Record<string, unknown>;
  const str = (key: string, fallback = ""): string => {
    const value = input[key];
    return typeof value === "string" && value.length > 0 ? value : fallback;
  };

  return {
    mode: spec.bois_mode ?? "define",
    client_id: str("client_id", "arika-agency"),
    task: str("task", `Run ${spec.bois_mode ?? "define"} for ${spec.name}.`),
    deliverable: str("deliverable", "brand_identity_definition"),
    positioning_objective: str("positioning_objective"),
    communication_goal: str("communication_goal"),
    campaign_objective: str("campaign_objective"),
    // Advisory-first still holds: synthesis only produces a recommendation. Callers can
    // pass synthesize:false to run routing/retrieval/governance with no model call at all.
    synthesize: input.synthesize === false ? false : true,
  };
}

export async function runBoisAgent(
  spec: AgentSpec,
  ctx: RunContext,
): Promise<Record<string, unknown>> {
  if (!existsSync(ENTRY_POINT)) {
    throw new Error(
      `BOIS entry point not found at ${ENTRY_POINT}. Branding (12)'s bois/ must be present to run ${spec.name}.`,
    );
  }

  const request = buildRequest(spec, ctx);

  return new Promise((resolve, reject) => {
    const child = spawn(pythonBin(), [ENTRY_POINT, JSON.stringify(request)], {
      cwd: repoRoot,
      env: process.env,
    });

    let stdout = "";
    let stderr = "";
    const timer = setTimeout(() => {
      child.kill();
      reject(new Error(`BOIS run for ${spec.name} timed out after ${TIMEOUT_MS}ms.`));
    }, TIMEOUT_MS);

    child.stdout.on("data", (chunk) => (stdout += chunk.toString()));
    child.stderr.on("data", (chunk) => (stderr += chunk.toString()));

    child.on("error", (err) => {
      clearTimeout(timer);
      reject(
        new Error(
          `Could not start Python for ${spec.name}: ${err.message}. ` +
            `Set BOIS_PYTHON to your interpreter path if it is not on PATH.`,
        ),
      );
    });

    child.on("close", (code) => {
      clearTimeout(timer);
      // run_brand_task.py always emits exactly one JSON object, including on failure —
      // a non-zero exit still carries a structured, readable envelope.
      try {
        resolve(JSON.parse(stdout) as Record<string, unknown>);
      } catch {
        reject(
          new Error(
            `BOIS returned unparseable output for ${spec.name} (exit ${code}).\n` +
              `stdout: ${stdout.slice(0, 400)}\nstderr: ${stderr.slice(0, 400)}`,
          ),
        );
      }
    });
  });
}
