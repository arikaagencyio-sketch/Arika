/**
 * D4 — dispatch fails closed when human approval is required.
 *
 * THE DEFECT THIS CLOSES. `finalizeRun` computed `humanGate` after the agent
 * answered, wrote it to memory, returned it — and nothing acted on it. The only
 * consumers were `console.log` calls in `index.ts`. Evidence it was live rather
 * than latent: all five 2026-09-13 Offer production records carry
 * `recommendation.requiresHumanApproval: true` and all five ran to completion.
 *
 * WHAT A REFUSAL IS HERE. A thrown `ApprovalRequiredError`, not a boolean and not
 * a logged warning. A boolean return can be read and dropped; a throw cannot be
 * reached past. It carries a structured, serialisable `refusal` so a caller can
 * branch on `code` and `stage` without parsing a message. This matches the
 * runtime's existing fail-closed convention (`assertFixturePreconditions`,
 * `assertStreamMatchesMode`), and the receiver pattern in
 * `01_Sector/delivery/offer_inbox_receiver.py`, which enforces its OWN approval
 * before any side effect rather than inheriting a reported flag.
 *
 * TWO STAGES, because the two requirements are knowable at different times:
 *   pre_model      — `risk_class >= 3` or `spec.requires_human_approval`. Known
 *                    from the spec alone, so it is refused BEFORE the model call:
 *                    a gated operation must cost nothing to discover.
 *   post_response  — the recommendation's own `requiresHumanApproval: true`.
 *                    Unknowable before the call, so it is refused immediately
 *                    after response validation and BEFORE the memory write, the
 *                    advertised emits, and anything downstream.
 *
 * WHY THE MEMORY WRITE IS ON THE FAR SIDE OF THE GATE. A memory line in this
 * runtime is what the estate counts as a dated execution record (AEIT_11 §5).
 * Writing one for a run that was stopped would manufacture execution evidence
 * for something that did not complete. A refusal is reported to the caller; it
 * does not leave a run record behind.
 *
 * NO APPROVAL-RESUME PATH EXISTS, DELIBERATELY. There is no parameter, flag or
 * token that satisfies these gates — see `02_Offer`/`16_Automation` notes and
 * DECISIONS.md. A boolean `approved: true` would be exactly the bypass D4 exists
 * to remove. The repository's three authorisation registries
 * (`skill-fixture-authorisations.json`, `provisioning-authorisations.json`,
 * `delivery-authorisations.json`) show the shape real evidence would take — a
 * one-attempt row naming the exact target, pinned and spent on use — but owner
 * item 58 (how the runtime's 30 schedule triggers get governance rows) is
 * UNDECIDED, so the rows such a registry would hold do not exist. Building the
 * resume path now would pre-empt that decision and add a bypass surface with no
 * live consumer, since `executor.ts` publishes nothing. Refusal only, and the
 * gap is reported.
 */

/**
 * The three spec fields this module reads, declared structurally rather than as
 * `Pick<AgentSpec, ...>`.
 *
 * `AgentSpec` is `z.infer<>` over a Zod schema carrying `superRefine` and
 * transforms. `Pick<>` on it forced tsc to expand that inferred type once per
 * signature, and three signatures was enough to end the compile in
 * "FATAL ERROR: Zone Allocation failed - process out of memory". A structural
 * interface compiles in constant time, `AgentSpec` is assignable to it, and the
 * approval rules have no business depending on the whole spec shape.
 */
export interface ApprovalSubject {
  readonly name: string;
  readonly risk_class: number;
  readonly requires_human_approval?: boolean;
}

export const APPROVAL_REFUSAL_CODE = "APPROVAL_REQUIRED" as const;

export type ApprovalStage = "pre_model" | "post_response";

/** The machine-checkable refusal. Serialisable, so a caller may log it whole. */
export interface ApprovalRefusal {
  readonly code: typeof APPROVAL_REFUSAL_CODE;
  readonly stage: ApprovalStage;
  readonly agent: string;
  readonly riskClass: number;
  /** Every rule that raised the gate, named. More than one may apply. */
  readonly reasons: readonly string[];
  /** What this refusal prevented. Asserted by the tests, not decorative. */
  readonly refusedBefore: readonly string[];
  /**
   * Always null. There is no evidence shape that satisfies these gates today;
   * see the module header. A non-null value here would be a bypass.
   */
  readonly approvalEvidence: null;
}

/**
 * Thrown, never returned. `isApprovalRefusal` is the supported way to branch on
 * it; callers must not match on the message.
 */
export class ApprovalRequiredError extends Error {
  readonly isApprovalRefusal = true as const;
  readonly refusal: ApprovalRefusal;

  constructor(refusal: ApprovalRefusal) {
    super(
      `Human review required: ${refusal.agent} is gated at ${refusal.stage} ` +
        `(${refusal.reasons.join("; ")}). Refused before: ${refusal.refusedBefore.join(", ")}. ` +
        `No approval-resume path exists — this run cannot be continued by a flag.`,
    );
    this.name = "ApprovalRequiredError";
    this.refusal = refusal;
  }

  toJSON(): ApprovalRefusal {
    return this.refusal;
  }
}

/** The supported discriminator. Narrower than `instanceof` across module realms. */
export function isApprovalRefusal(err: unknown): err is ApprovalRequiredError {
  return (
    typeof err === "object" &&
    err !== null &&
    (err as { isApprovalRefusal?: unknown }).isApprovalRefusal === true &&
    (err as { refusal?: { code?: unknown } }).refusal?.code === APPROVAL_REFUSAL_CODE
  );
}

/**
 * Approval requirements knowable from the spec alone, before any model call.
 * Class 0-2 with no spec flag returns [] and is untouched by D4 — the approval
 * matrix requires no hard gate there, and broadening to it is out of scope.
 */
export function staticApprovalReasons(spec: Omit<ApprovalSubject, "name">): string[] {
  const reasons: string[] = [];
  if (spec.risk_class >= 3) {
    reasons.push(
      `Constitution class ${spec.risk_class} requires human sign-off (§3 #5: no exceptions carved out by convenience or urgency)`,
    );
  }
  if (spec.requires_human_approval) {
    reasons.push("the spec sets requires_human_approval: true");
  }
  return reasons;
}

/**
 * A TEST_FIXTURE run is exempt from both gates, and the exemption is narrow and
 * evidenced rather than a convenience:
 *
 *  1. a fixture advertises NO emits at all, unconditionally
 *     (`emitted: ctx.fixture || humanGate ? [] : …`), so it dispatches nothing —
 *     the risk D4 addresses does not exist on this path;
 *  2. the lane is gated HARDER already: `FIXTURE_LANE_ENABLED` is false, and
 *     even when open `assertFixturePreconditions` requires an `approved`
 *     authorisation naming a registered sandbox stream — which is the closest
 *     thing to real approval evidence the repository has;
 *  3. two of the three existing fixture records (OFFER-F2, OFFER-F3) carry
 *     `requiresHumanApproval: true`. Applying the post-response gate to fixtures
 *     would have made those runs impossible, leaving the lane unable to exercise
 *     precisely the agents that most need exercising.
 *
 * D4 therefore does not relax the fixture lane and does not extend into it.
 */
function isFixtureRun(ctx: { fixture?: boolean }): boolean {
  return ctx.fixture === true;
}

/**
 * Stage 1. Refuses a statically gated agent BEFORE the model is invoked, for
 * EVERY trigger including `manual`.
 *
 * Until D4 this fired only when `ctx.trigger !== "manual"`, on the reasoning that
 * a human typing a command is a human in the loop. That is presence, not
 * recorded approval, and Constitution §3 #5 allows no exception for convenience.
 * The change affects 17 agents — 11 at class >= 3 and 10 with the spec flag, 4 in
 * both — and NONE of the nine agents with a dated execution record is among them,
 * so it closes a path nothing has used.
 */
export function assertStaticApproval(
  spec: ApprovalSubject,
  ctx: { trigger: string; fixture?: boolean },
): void {
  if (isFixtureRun(ctx)) return;
  const reasons = staticApprovalReasons(spec);
  if (reasons.length === 0) return;
  throw new ApprovalRequiredError({
    code: APPROVAL_REFUSAL_CODE,
    stage: "pre_model",
    agent: spec.name,
    riskClass: spec.risk_class,
    reasons,
    refusedBefore: [
      "model invocation",
      "memory write",
      "advertised emits",
      "event publication",
      "receiver invocation",
      "registry mutation",
      "connector or downstream action",
    ],
    approvalEvidence: null,
  });
}

/**
 * Stage 2. Refuses after response validation and BEFORE the memory write, when
 * the gate is raised by anything — including the recommendation's own flag, which
 * could not have been known at stage 1.
 *
 * `humanGate` is passed in rather than recomputed so that this cannot drift from
 * the value the caller recorded.
 */
export function assertDispatchApproval(
  spec: ApprovalSubject,
  ctx: { trigger: string; fixture?: boolean },
  recommendation: Record<string, unknown>,
  humanGate: boolean,
): void {
  if (isFixtureRun(ctx)) return;
  if (!humanGate) return;
  const reasons = staticApprovalReasons(spec);
  if (recommendation.requiresHumanApproval === true) {
    reasons.push("the agent's own recommendation returned requiresHumanApproval: true");
  }
  if (reasons.length === 0) {
    // humanGate true with no nameable reason would mean the rule and its
    // explanation had diverged. Refuse rather than guess.
    reasons.push("human approval was required but no rule could be named — refusing rather than guessing");
  }
  throw new ApprovalRequiredError({
    code: APPROVAL_REFUSAL_CODE,
    stage: "post_response",
    agent: spec.name,
    riskClass: spec.risk_class,
    reasons,
    refusedBefore: [
      "memory write",
      "advertised emits",
      "event publication",
      "receiver invocation",
      "registry mutation",
      "connector or downstream action",
    ],
    approvalEvidence: null,
  });
}
