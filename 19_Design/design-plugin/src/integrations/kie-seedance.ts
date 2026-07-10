import { KieClient } from "./kie-client.js";

export type SeedanceAspectRatio = "1:1" | "4:3" | "3:4" | "16:9" | "9:16" | "21:9";
export type SeedanceResolution = "480p" | "720p" | "1080p";

export interface GenerateVideoRequest {
  prompt: string;
  /** 0-2 reference image URLs, for image-to-video generation. */
  inputImageUrls?: string[];
  aspectRatio: SeedanceAspectRatio;
  /** 4-12 seconds. */
  durationSeconds: number;
  resolution?: SeedanceResolution;
  /** Locks the camera for a static shot instead of dynamic movement. */
  fixedLens?: boolean;
  generateAudio?: boolean;
  nsfwChecker?: boolean;
  callBackUrl?: string;
}

export interface GenerateVideoResult {
  taskId: string;
  videoUrls: string[];
  creditsConsumed?: number;
}

const MIN_PROMPT_LENGTH = 3;
const MAX_PROMPT_LENGTH = 20_000;
const MAX_INPUT_IMAGES = 2;
const MIN_DURATION_SECONDS = 4;
const MAX_DURATION_SECONDS = 12;

/**
 * KIE.ai's Bytedance Seedance 1.5 Pro connector — a video generator
 * alongside OpenArt in Design (19)'s Production Engine
 * (`19_Design/DESIGN_OS.md` §3), added 2026-07-07.
 */
export class SeedanceConnector {
  readonly id = "kie-seedance";
  readonly model = "bytedance/seedance-1.5-pro";

  constructor(private readonly client: KieClient = new KieClient()) {}

  async generateVideo(request: GenerateVideoRequest): Promise<GenerateVideoResult> {
    if (!request.prompt || request.prompt.length < MIN_PROMPT_LENGTH || request.prompt.length > MAX_PROMPT_LENGTH) {
      throw new Error(`prompt is required and must be ${MIN_PROMPT_LENGTH}-${MAX_PROMPT_LENGTH} characters`);
    }
    if (request.inputImageUrls && request.inputImageUrls.length > MAX_INPUT_IMAGES) {
      throw new Error(`inputImageUrls supports at most ${MAX_INPUT_IMAGES} images`);
    }
    if (request.durationSeconds < MIN_DURATION_SECONDS || request.durationSeconds > MAX_DURATION_SECONDS) {
      throw new Error(`durationSeconds must be between ${MIN_DURATION_SECONDS} and ${MAX_DURATION_SECONDS}`);
    }

    const taskId = await this.client.createTask(
      this.model,
      {
        prompt: request.prompt,
        ...(request.inputImageUrls ? { input_urls: request.inputImageUrls } : {}),
        aspect_ratio: request.aspectRatio,
        resolution: request.resolution ?? "720p",
        duration: request.durationSeconds,
        fixed_lens: request.fixedLens ?? false,
        generate_audio: request.generateAudio ?? false,
        nsfw_checker: request.nsfwChecker ?? false
      },
      request.callBackUrl
    );

    const detail = await this.client.waitForResult(taskId);
    if (detail.state === "fail") {
      throw new Error(`Seedance generation failed (${taskId}): ${detail.failMsg ?? "unknown error"}`);
    }

    return { taskId, videoUrls: detail.resultUrls, creditsConsumed: detail.creditsConsumed };
  }
}
