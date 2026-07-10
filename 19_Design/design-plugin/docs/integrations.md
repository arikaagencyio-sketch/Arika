# Integration Architecture

Design (19)'s first real code layer (`19_Design/DESIGN_OS.md` §13, previously "none yet") — connectors for KIE.ai's job API, feeding the Production Engine (`19_Design/DESIGN_OS.md` §3) alongside OpenArt and Claude Design.

## KIE.ai (real, live) — added 2026-07-07

`src/integrations/kie-client.ts`'s `KieClient` is a thin wrapper around KIE's
model-agnostic job API (`createTask` / `recordInfo`). Two model-specific
connectors sit on top of it:

- `src/integrations/kie-nano-banana-pro.ts`'s `NanoBananaProConnector` —
  image generation via Google's Nano Banana Pro (Gemini 3 Pro Image) model.
- `src/integrations/kie-seedance.ts`'s `SeedanceConnector` — video generation
  via Bytedance's Seedance 1.5 Pro model.

Both need a single credential in `.env`:

- `KIE_API_KEY` — from the owner's real KIE.ai account (kie.ai/api-key).
- `KIE_API_BASE_URL` — defaults to `https://api.kie.ai/api/v1`; only override
  if KIE changes its base URL.

Usage:

```ts
import { NanoBananaProConnector } from "./src/integrations/kie-nano-banana-pro.js";
import { SeedanceConnector } from "./src/integrations/kie-seedance.js";

const image = await new NanoBananaProConnector().generateImage({
  prompt: "Executive Lobby, Deep Revenue Navy and Champagne Gold, no visible text",
  aspectRatio: "16:9",
  resolution: "2K"
});

const video = await new SeedanceConnector().generateVideo({
  prompt: "Slow dolly-in across the Strategy War Room",
  aspectRatio: "16:9",
  durationSeconds: 6
});
```

Both connectors submit a job (`createTask`) and poll (`waitForResult`) until
KIE reports `success` or `fail` — no callback server required for one-off
generations. A `callBackUrl` can be passed through either request if a
webhook receiver exists later.

Neither connector spends credits on its own initiative — same "don't spend
credits speculatively" doctrine as OpenArt (`19_Design/DESIGN_OS.md` §3):
call `generateImage`/`generateVideo` only from an actual production request,
never from a health-check or test that isn't mocking the network.

To verify `KIE_API_KEY` is real without spending a generation credit, call
`new KieClient().getCredits()` — a free, read-only balance check (`GET
/chat/credit`). Use this, not a real `generateImage`/`generateVideo` call,
to confirm the key works after first setting it up.

## Why alongside OpenArt, not instead of it

OpenArt remains the department's confirmed multi-model vendor (100+ models in
one account). KIE.ai gives direct, per-call API access to two specific models
(Nano Banana Pro, Seedance) without going through OpenArt's own credit pool or
UI — useful when OpenArt's Free-plan credits are exhausted (the real
constraint hit during the Arika website imagery pass, see
`20_Experience_Engineering/ARIKA_WEBSITE_PROJECT.md` §6) or when a caller
needs programmatic access outside the OpenArt MCP surface. The Production
Engine Coordinator (`.claude/agents/design-production-engine-coordinator.md`)
decides per-request which vendor to route to.

## Connector shape

Neither connector implements the finos-plugin's `IntegrationConnector`
interface (`09_Finance/finos-plugin/src/integrations/index.ts`) — that
contract is specific to normalizing external systems into `FinancialEvent`s
for Finance (09). These are plain generation clients: `generateImage` /
`generateVideo` in, a task id and result URL(s) out.

## Real operational constraints (from KIE's own docs, 2026-07-07)

- **14-day media retention.** Generated images/videos are auto-deleted from
  KIE's storage 14 days after creation (log/metadata records last 2 months).
  Every `imageUrls`/`videoUrls` result must be downloaded into this repo (or
  another durable store) promptly — same "download the real file, don't just
  reference the URL" discipline already used for the Arika website's OpenArt
  images (`20_Experience_Engineering/ARIKA_WEBSITE_PROJECT.md` §6). Do not
  treat a KIE result URL as a durable asset location.
- **Rate limit**: 20 new generation requests per 10 seconds per account
  (100+ concurrent tasks typically allowed). Exceeding it returns HTTP 429
  and the request is rejected outright, not queued. Not a concern at this
  department's current (manual, one-off) call volume — revisit if a batch
  pipeline starts firing many requests at once.
- **Auth failures** come back as `{"code":401,"msg":"You do not have access
  permissions"}` — `KieClient`'s generic HTTP-error surfacing (throws with the
  full response body) already exposes this; if you see it, re-check
  `KIE_API_KEY` in `.env` before assuming a code bug.
- **Logs/audit trail**: every real task (params, status, credits consumed,
  output) is inspectable at `https://kie.ai/logs` — the source of truth if
  credit usage ever looks wrong, same role Zoho Books' own dashboard plays for
  `finos-plugin`'s invoice connector.
