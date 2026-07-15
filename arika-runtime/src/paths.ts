import { fileURLToPath } from "node:url";
import { dirname, resolve } from "node:path";

// This file compiles to `<repo>/arika-runtime/dist/paths.js` (or runs from
// `<repo>/arika-runtime/src/paths.ts` under tsx). Either way it sits one level
// below the package root, so the package root is one up and the repo root two up.
const here = dirname(fileURLToPath(import.meta.url));

/** `<repo>/arika-runtime` */
export const packageRoot = resolve(here, "..");

/** `<repo>` — the Arika OS repository root. */
export const repoRoot = resolve(here, "..", "..");

/** `<repo>/.claude/agents` — where every agent spec lives. */
export const agentsDir = resolve(repoRoot, ".claude", "agents");
