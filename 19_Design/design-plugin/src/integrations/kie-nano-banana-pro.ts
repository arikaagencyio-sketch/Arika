import { KieClient } from "./kie-client.js";

export type NanoBananaProAspectRatio =
  | "1:1"
  | "2:3"
  | "3:2"
  | "3:4"
  | "4:3"
  | "4:5"
  | "5:4"
  | "9:16"
  | "16:9"
  | "21:9"
  | "auto";

export type NanoBananaProResolution = "1K" | "2K" | "4K";

export interface GenerateImageRequest {
  prompt: string;
  /** Up to 8 reference image URLs, for image-to-image edits. */
  imageInputUrls?: string[];
  aspectRatio?: NanoBananaProAspectRatio;
  resolution?: NanoBananaProResolution;
  outputFormat?: "png" | "jpg";
  callBackUrl?: string;
}

export interface GenerateImageResult {
  taskId: string;
  imageUrls: string[];
  creditsConsumed?: number;
}

const MAX_PROMPT_LENGTH = 10_000;
const MAX_IMAGE_INPUTS = 8;

/**
 * KIE.ai's Nano Banana Pro (Gemini 3 Pro Image) connector — an image
 * generator alongside OpenArt in Design (19)'s Production Engine
 * (`19_Design/DESIGN_OS.md` §3), added 2026-07-07.
 */
export class NanoBananaProConnector {
  readonly id = "kie-nano-banana-pro";
  readonly model = "nano-banana-pro";

  constructor(private readonly client: KieClient = new KieClient()) {}

  async generateImage(request: GenerateImageRequest): Promise<GenerateImageResult> {
    if (!request.prompt || request.prompt.length > MAX_PROMPT_LENGTH) {
      throw new Error(`prompt is required and must be at most ${MAX_PROMPT_LENGTH} characters`);
    }
    if (request.imageInputUrls && request.imageInputUrls.length > MAX_IMAGE_INPUTS) {
      throw new Error(`imageInputUrls supports at most ${MAX_IMAGE_INPUTS} images`);
    }

    const taskId = await this.client.createTask(
      this.model,
      {
        prompt: request.prompt,
        ...(request.imageInputUrls ? { image_input: request.imageInputUrls } : {}),
        aspect_ratio: request.aspectRatio ?? "1:1",
        resolution: request.resolution ?? "1K",
        output_format: request.outputFormat ?? "png"
      },
      request.callBackUrl
    );

    const detail = await this.client.waitForResult(taskId);
    if (detail.state === "fail") {
      throw new Error(`Nano Banana Pro generation failed (${taskId}): ${detail.failMsg ?? "unknown error"}`);
    }

    return { taskId, imageUrls: detail.resultUrls, creditsConsumed: detail.creditsConsumed };
  }
}
