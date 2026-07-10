import assert from "node:assert/strict";
import test from "node:test";
import { KieClient } from "../dist/integrations/kie-client.js";
import { NanoBananaProConnector } from "../dist/integrations/kie-nano-banana-pro.js";
import { SeedanceConnector } from "../dist/integrations/kie-seedance.js";

function mockFetchSequence(responses) {
  const calls = [];
  const queue = [...responses];
  globalThis.fetch = async (url, init) => {
    calls.push({ url: String(url), init });
    const next = queue.shift();
    if (!next) throw new Error("mockFetchSequence: ran out of queued responses");
    return {
      ok: next.ok ?? true,
      status: next.status ?? 200,
      json: async () => next.body
    };
  };
  return calls;
}

test("KieClient.isConfigured reflects whether an API key is present", () => {
  assert.equal(new KieClient({ apiKey: undefined }).isConfigured(), false);
  assert.equal(new KieClient({ apiKey: "key" }).isConfigured(), true);
});

test("getCredits returns the account's remaining credit balance", async () => {
  mockFetchSequence([{ body: { code: 200, msg: "success", data: 80 } }]);
  const client = new KieClient({ apiKey: "key" });
  assert.equal(await client.getCredits(), 80);
});

test("getCredits throws when the API reports a non-200 code", async () => {
  mockFetchSequence([{ body: { code: 500, msg: "Server Error", data: null } }]);
  const client = new KieClient({ apiKey: "key" });
  await assert.rejects(() => client.getCredits(), /did not return a balance/);
});

test("createTask throws when the client has no API key configured", async () => {
  const client = new KieClient({ apiKey: undefined });
  await assert.rejects(() => client.createTask("nano-banana-pro", { prompt: "x" }), /not configured/);
});

test("createTask returns the taskId from a successful response", async () => {
  mockFetchSequence([{ body: { code: 200, msg: "success", data: { taskId: "task_abc" } } }]);
  const client = new KieClient({ apiKey: "key" });
  const taskId = await client.createTask("nano-banana-pro", { prompt: "a lobby" });
  assert.equal(taskId, "task_abc");
});

test("createTask throws when the API reports a non-200 code", async () => {
  mockFetchSequence([{ body: { code: 400, msg: "bad request" } }]);
  const client = new KieClient({ apiKey: "key" });
  await assert.rejects(() => client.createTask("nano-banana-pro", { prompt: "a lobby" }), /did not return a taskId/);
});

test("waitForResult polls until state is success, parsing resultUrls from resultJson", async () => {
  mockFetchSequence([
    { body: { code: 200, data: { taskId: "task_1", model: "nano-banana-pro", state: "generating" } } },
    {
      body: {
        code: 200,
        data: {
          taskId: "task_1",
          model: "nano-banana-pro",
          state: "success",
          resultJson: JSON.stringify({ resultUrls: ["https://example.com/out.png"] }),
          creditsConsumed: 10
        }
      }
    }
  ]);
  const client = new KieClient({ apiKey: "key", pollIntervalMs: 1 });
  const detail = await client.waitForResult("task_1");
  assert.equal(detail.state, "success");
  assert.deepEqual(detail.resultUrls, ["https://example.com/out.png"]);
  assert.equal(detail.creditsConsumed, 10);
});

test("waitForResult surfaces a fail state without throwing itself", async () => {
  mockFetchSequence([
    { body: { code: 200, data: { taskId: "task_2", model: "nano-banana-pro", state: "fail", failMsg: "bad prompt" } } }
  ]);
  const client = new KieClient({ apiKey: "key", pollIntervalMs: 1 });
  const detail = await client.waitForResult("task_2");
  assert.equal(detail.state, "fail");
  assert.equal(detail.failMsg, "bad prompt");
});

test("NanoBananaProConnector.generateImage rejects an oversized prompt before calling the network", async () => {
  const connector = new NanoBananaProConnector(new KieClient({ apiKey: "key" }));
  await assert.rejects(() => connector.generateImage({ prompt: "x".repeat(10_001) }), /at most 10000 characters/);
});

test("NanoBananaProConnector.generateImage rejects more than 8 reference images", async () => {
  const connector = new NanoBananaProConnector(new KieClient({ apiKey: "key" }));
  await assert.rejects(
    () => connector.generateImage({ prompt: "ok", imageInputUrls: Array(9).fill("https://example.com/a.png") }),
    /at most 8 images/
  );
});

test("NanoBananaProConnector.generateImage returns image URLs on success", async () => {
  mockFetchSequence([
    { body: { code: 200, data: { taskId: "task_img" } } },
    {
      body: {
        code: 200,
        data: {
          taskId: "task_img",
          model: "nano-banana-pro",
          state: "success",
          resultJson: JSON.stringify({ resultUrls: ["https://example.com/out.png"] })
        }
      }
    }
  ]);
  const connector = new NanoBananaProConnector(new KieClient({ apiKey: "key", pollIntervalMs: 1 }));
  const result = await connector.generateImage({ prompt: "the executive lobby" });
  assert.equal(result.taskId, "task_img");
  assert.deepEqual(result.imageUrls, ["https://example.com/out.png"]);
});

test("NanoBananaProConnector.generateImage throws with the fail reason when generation fails", async () => {
  mockFetchSequence([
    { body: { code: 200, data: { taskId: "task_img_fail" } } },
    { body: { code: 200, data: { taskId: "task_img_fail", model: "nano-banana-pro", state: "fail", failMsg: "unsafe content" } } }
  ]);
  const connector = new NanoBananaProConnector(new KieClient({ apiKey: "key", pollIntervalMs: 1 }));
  await assert.rejects(() => connector.generateImage({ prompt: "the executive lobby" }), /unsafe content/);
});

test("SeedanceConnector.generateVideo rejects a duration outside 4-12 seconds", async () => {
  const connector = new SeedanceConnector(new KieClient({ apiKey: "key" }));
  await assert.rejects(
    () => connector.generateVideo({ prompt: "a pan across the war room", aspectRatio: "16:9", durationSeconds: 20 }),
    /between 4 and 12/
  );
});

test("SeedanceConnector.generateVideo rejects more than 2 input images", async () => {
  const connector = new SeedanceConnector(new KieClient({ apiKey: "key" }));
  await assert.rejects(
    () =>
      connector.generateVideo({
        prompt: "a pan across the war room",
        aspectRatio: "16:9",
        durationSeconds: 6,
        inputImageUrls: ["https://example.com/a.png", "https://example.com/b.png", "https://example.com/c.png"]
      }),
    /at most 2 images/
  );
});

test("SeedanceConnector.generateVideo returns video URLs on success", async () => {
  mockFetchSequence([
    { body: { code: 200, data: { taskId: "task_vid" } } },
    {
      body: {
        code: 200,
        data: {
          taskId: "task_vid",
          model: "bytedance/seedance-1.5-pro",
          state: "success",
          resultJson: JSON.stringify({ resultUrls: ["https://example.com/out.mp4"] }),
          creditsConsumed: 40
        }
      }
    }
  ]);
  const connector = new SeedanceConnector(new KieClient({ apiKey: "key", pollIntervalMs: 1 }));
  const result = await connector.generateVideo({ prompt: "a pan across the war room", aspectRatio: "16:9", durationSeconds: 6 });
  assert.equal(result.taskId, "task_vid");
  assert.deepEqual(result.videoUrls, ["https://example.com/out.mp4"]);
  assert.equal(result.creditsConsumed, 40);
});
