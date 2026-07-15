#!/usr/bin/env node
import { existsSync, readFileSync } from "node:fs";
import { isAbsolute, join } from "node:path";
import { Command } from "commander";
import { config as loadEnv } from "dotenv";
import { loadAgents } from "../agent-registry.js";
import { runAgent } from "../executor.js";
import { packageRoot, repoRoot } from "../paths.js";

loadEnv({ path: join(packageRoot, ".env") });

const program = new Command();
program.name("arika").description("Arika Runtime — run and inspect agents").version("0.1.0");

program
  .command("list")
  .description("List every registered agent")
  .action(() => {
    const { agents, skipped } = loadAgents();
    console.log(`\nArika Runtime — ${agents.size} agent(s) registered\n`);
    for (const spec of [...agents.values()].sort((a, b) => a.name.localeCompare(b.name))) {
      const triggers = spec.triggers.map((t) => t.type).join(",");
      console.log(
        `  ${spec.name.padEnd(34)} dept ${spec.department}  class ${spec.risk_class}  ${spec.execution.padEnd(12)} [${triggers}]`,
      );
    }
    if (skipped.length) {
      console.log(`\n  Skipped ${skipped.length} file(s) (not yet migrated / invalid):`);
      for (const s of skipped) console.log(`    - ${s.file}: ${s.reason}`);
    }
    console.log("");
  });

program
  .command("run <name>")
  .description("Run one agent once with JSON input")
  .option("--input <json>", "JSON input for the agent", "{}")
  .action(async (name: string, opts: { input: string }) => {
    const { agents } = loadAgents();
    const spec = agents.get(name);
    if (!spec) {
      console.error(`Unknown agent: ${name}. Run "arika list" to see registered agents.`);
      process.exit(1);
    }
    let input: Record<string, unknown>;
    try {
      input = JSON.parse(opts.input);
    } catch {
      console.error("--input must be valid JSON.");
      process.exit(1);
      return;
    }
    try {
      const result = await runAgent(spec, { trigger: "manual", input });
      console.log(JSON.stringify(result, null, 2));
    } catch (err) {
      console.error(`Run failed: ${(err as Error).message}`);
      process.exit(1);
    }
  });

program
  .command("logs <name>")
  .description("Show the last N memory-log lines for an agent")
  .option("-n, --count <n>", "number of lines", "10")
  .action((name: string, opts: { count: string }) => {
    const { agents } = loadAgents();
    const spec = agents.get(name);
    if (!spec) {
      console.error(`Unknown agent: ${name}.`);
      process.exit(1);
      return;
    }
    if (!spec.memory_stream) {
      console.log(`Agent ${name} declares no memory_stream.`);
      return;
    }
    const path = isAbsolute(spec.memory_stream) ? spec.memory_stream : join(repoRoot, spec.memory_stream);
    if (!existsSync(path)) {
      console.log(`No log yet at ${spec.memory_stream}`);
      return;
    }
    const lines = readFileSync(path, "utf8").trim().split("\n").filter(Boolean);
    const n = Number.parseInt(opts.count, 10) || 10;
    for (const line of lines.slice(-n)) console.log(line);
  });

program.parseAsync(process.argv);
