import { readdirSync, readFileSync } from "node:fs";
import { join } from "node:path";
import matter from "gray-matter";
import { agentsDir } from "./paths.js";
import { frontmatterSchema, type AgentSpec } from "./spec-schema.js";

export interface LoadResult {
  agents: Map<string, AgentSpec>;
  skipped: { file: string; reason: string }[];
}

/**
 * Read every `.md` in `.claude/agents/`, parse the YAML frontmatter, validate it,
 * and return the runnable agents keyed by name. Files that are legacy (2-key
 * frontmatter with no `triggers` block) or invalid are reported in `skipped`
 * rather than thrown — a half-migrated repo must still boot.
 */
export function loadAgents(dir: string = agentsDir): LoadResult {
  const agents = new Map<string, AgentSpec>();
  const skipped: { file: string; reason: string }[] = [];

  let files: string[];
  try {
    files = readdirSync(dir).filter((f) => f.endsWith(".md"));
  } catch (err) {
    throw new Error(`Cannot read agents directory ${dir}: ${(err as Error).message}`);
  }

  for (const file of files.sort()) {
    const full = join(dir, file);
    const parsed = matter(readFileSync(full, "utf8"));

    if (!parsed.data || !("triggers" in parsed.data)) {
      skipped.push({ file, reason: "no `triggers` block (legacy spec — not yet migrated)" });
      continue;
    }

    const result = frontmatterSchema.safeParse(parsed.data);
    if (!result.success) {
      skipped.push({
        file,
        reason: result.error.issues.map((i) => `${i.path.join(".")}: ${i.message}`).join("; "),
      });
      continue;
    }

    const spec: AgentSpec = { ...result.data, systemPrompt: parsed.content.trim(), filePath: full };

    if (spec.name !== file.replace(/\.md$/, "")) {
      skipped.push({ file, reason: `frontmatter name "${spec.name}" does not match filename` });
      continue;
    }
    if (agents.has(spec.name)) {
      skipped.push({ file, reason: `duplicate agent name "${spec.name}"` });
      continue;
    }
    agents.set(spec.name, spec);
  }

  return { agents, skipped };
}
