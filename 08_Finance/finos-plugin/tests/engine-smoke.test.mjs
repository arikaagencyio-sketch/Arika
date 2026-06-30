import assert from "node:assert/strict";
import test from "node:test";
import { createFinOsApplication } from "../dist/api-layer/application.js";

test("starter cash position exposes runway and liquidity", () => {
  const app = createFinOsApplication();
  const position = app.fixtures.starterCashPosition();
  assert.equal(position.entityId, app.defaultEntityId);
  assert.ok(position.netLiquidity.amountMinor > 0);
  assert.ok(position.runwayDays > 0);
});

test("revenue allocation totals to the source amount", async () => {
  const app = createFinOsApplication();
  const event = await app.eventBus.publish({
    type: "REVENUE_RECEIVED",
    entityId: app.defaultEntityId,
    source: "test",
    payload: {
      amount: { amountMinor: 1000000, currency: "USD" },
      revenueStream: "recurring",
      receivedAt: new Date().toISOString()
    }
  });

  const plan = app.allocation.planRevenueAllocation(event);
  const allocated = plan.targets.reduce((sum, target) => sum + target.amount.amountMinor, 0);
  assert.equal(allocated + plan.residual.amountMinor, 1000000);
});
