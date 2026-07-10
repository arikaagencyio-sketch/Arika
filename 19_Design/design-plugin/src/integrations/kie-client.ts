export interface KieClientConfig {
  apiKey?: string;
  baseUrl?: string;
  pollIntervalMs?: number;
  pollTimeoutMs?: number;
}

export type KieTaskState = "waiting" | "queuing" | "generating" | "success" | "fail";

export interface KieTaskDetail {
  taskId: string;
  model: string;
  state: KieTaskState;
  resultUrls: string[];
  failMsg?: string;
  creditsConsumed?: number;
}

interface KieCreateTaskResponse {
  code: number;
  msg: string;
  data?: { taskId: string };
}

interface KieRecordInfoResponse {
  code: number;
  msg: string;
  data?: {
    taskId: string;
    model: string;
    state: KieTaskState;
    resultJson?: string;
    failMsg?: string;
    creditsConsumed?: number;
  };
}

interface KieCreditResponse {
  code: number;
  msg: string;
  data?: number;
}

const DEFAULT_BASE_URL = "https://api.kie.ai/api/v1";
const DEFAULT_POLL_INTERVAL_MS = 5_000;
const DEFAULT_POLL_TIMEOUT_MS = 10 * 60_000;

/**
 * Thin client for KIE.ai's model-agnostic job API (createTask / recordInfo) —
 * shared by every KIE-backed connector in Design (19)'s Production Engine
 * (`19_Design/DESIGN_OS.md` §3), so each model-specific connector only has to
 * shape its own `input` object, not re-implement auth/polling.
 */
export class KieClient {
  private readonly apiKey?: string;
  private readonly baseUrl: string;
  private readonly pollIntervalMs: number;
  private readonly pollTimeoutMs: number;

  constructor(config: KieClientConfig = {}) {
    this.apiKey = config.apiKey ?? process.env.KIE_API_KEY;
    this.baseUrl = config.baseUrl ?? process.env.KIE_API_BASE_URL ?? DEFAULT_BASE_URL;
    this.pollIntervalMs = config.pollIntervalMs ?? DEFAULT_POLL_INTERVAL_MS;
    this.pollTimeoutMs = config.pollTimeoutMs ?? DEFAULT_POLL_TIMEOUT_MS;
  }

  isConfigured(): boolean {
    return Boolean(this.apiKey);
  }

  private assertConfigured(): string {
    if (!this.apiKey) {
      throw new Error(
        "KIE client is not configured — set KIE_API_KEY (see 19_Design/design-plugin/docs/integrations.md)."
      );
    }
    return this.apiKey;
  }

  private async request<T>(path: string, init: RequestInit = {}): Promise<T> {
    const apiKey = this.assertConfigured();
    const response = await fetch(`${this.baseUrl}${path}`, {
      ...init,
      headers: {
        Authorization: `Bearer ${apiKey}`,
        "Content-Type": "application/json",
        ...(init.headers ?? {})
      }
    });

    const body = await response.json().catch(() => undefined);
    if (!response.ok) {
      throw new Error(`KIE API error (${path}): HTTP ${response.status} ${JSON.stringify(body)}`);
    }
    return body as T;
  }

  /**
   * Returns the account's remaining credit balance — a free, read-only call
   * (no generation, no credits spent), so this is the right way to confirm
   * `KIE_API_KEY` is real and working without triggering a paid generation
   * just to test the wiring.
   */
  async getCredits(): Promise<number> {
    const body = await this.request<KieCreditResponse>("/chat/credit");
    if (body.code !== 200 || typeof body.data !== "number") {
      throw new Error(`KIE getCredits did not return a balance: ${JSON.stringify(body)}`);
    }
    return body.data;
  }

  /** Submits a generation job. Returns the task id used to poll for the result. */
  async createTask(model: string, input: Record<string, unknown>, callBackUrl?: string): Promise<string> {
    const body = await this.request<KieCreateTaskResponse>("/jobs/createTask", {
      method: "POST",
      body: JSON.stringify({ model, input, ...(callBackUrl ? { callBackUrl } : {}) })
    });

    if (body.code !== 200 || !body.data?.taskId) {
      throw new Error(`KIE createTask (${model}) did not return a taskId: ${JSON.stringify(body)}`);
    }
    return body.data.taskId;
  }

  /** Fetches current task status, parsing `resultJson`'s `resultUrls` when present. */
  async getTaskDetail(taskId: string): Promise<KieTaskDetail> {
    const body = await this.request<KieRecordInfoResponse>(`/jobs/recordInfo?taskId=${encodeURIComponent(taskId)}`);
    if (!body.data) {
      throw new Error(`KIE recordInfo returned no data for task ${taskId}: ${JSON.stringify(body)}`);
    }

    let resultUrls: string[] = [];
    if (body.data.resultJson) {
      const parsed = JSON.parse(body.data.resultJson) as { resultUrls?: string[] };
      resultUrls = parsed.resultUrls ?? [];
    }

    return {
      taskId: body.data.taskId,
      model: body.data.model,
      state: body.data.state,
      resultUrls,
      failMsg: body.data.failMsg,
      creditsConsumed: body.data.creditsConsumed
    };
  }

  /** Polls `getTaskDetail` until the task reaches `success`/`fail` or the poll timeout elapses. */
  async waitForResult(taskId: string): Promise<KieTaskDetail> {
    const deadline = Date.now() + this.pollTimeoutMs;
    for (;;) {
      const detail = await this.getTaskDetail(taskId);
      if (detail.state === "success" || detail.state === "fail") {
        return detail;
      }
      if (Date.now() > deadline) {
        throw new Error(`KIE task ${taskId} did not complete within ${this.pollTimeoutMs}ms (last state: ${detail.state})`);
      }
      await new Promise((resolve) => setTimeout(resolve, this.pollIntervalMs));
    }
  }
}
