import assert from "node:assert/strict";
import test from "node:test";
import { convertUsdMinorToKesMinor, normalizeZohoInvoice } from "../dist/integrations/zoho-books.js";

test("USD->KES conversion applies the live rate to minor units", () => {
  assert.equal(convertUsdMinorToKesMinor(150000, 129.4381), 19415715);
});

test("conversion rejects a non-positive exchange rate", () => {
  assert.throws(() => convertUsdMinorToKesMinor(100000, 0));
  assert.throws(() => convertUsdMinorToKesMinor(100000, -1));
});

test("conversion rejects a negative USD amount", () => {
  assert.throws(() => convertUsdMinorToKesMinor(-100, 129.4381));
});

test("normalizes a paid Zoho invoice into INVOICE_CREATED + REVENUE_RECEIVED", () => {
  const events = normalizeZohoInvoice("agency-main", {
    invoice_id: "9001",
    invoice_number: "INV-000123",
    customer_id: "cust-1",
    customer_name: "Acme",
    status: "paid",
    total: 50000,
    balance: 0,
    currency_code: "KES",
    date: "2026-07-04",
    last_modified_time: "2026-07-04T10:00:00Z",
    reference_number: "OPP-42"
  });

  assert.equal(events.length, 2);
  assert.equal(events[0].id, "zoho-invoice-9001");
  assert.equal(events[0].type, "INVOICE_CREATED");
  assert.equal(events[0].payload.amount.amountMinor, 5000000);
  assert.equal(events[1].id, "zoho-invoice-9001-revenue");
  assert.equal(events[1].type, "REVENUE_RECEIVED");
  assert.equal(events[1].causationId, "zoho-invoice-9001");
});

test("normalizes an unpaid invoice into just INVOICE_CREATED", () => {
  const events = normalizeZohoInvoice("agency-main", {
    invoice_id: "9002",
    invoice_number: "INV-000124",
    customer_id: "cust-2",
    customer_name: "Beta",
    status: "sent",
    total: 20000,
    balance: 20000,
    currency_code: "KES",
    date: "2026-07-04",
    last_modified_time: "2026-07-04T10:00:00Z"
  });

  assert.equal(events.length, 1);
  assert.equal(events[0].type, "INVOICE_CREATED");
});

test("repeated normalization of the same invoice yields identical event ids (idempotent)", () => {
  const record = {
    invoice_id: "9003",
    invoice_number: "INV-000125",
    customer_id: "cust-3",
    customer_name: "Gamma",
    status: "paid",
    total: 10000,
    balance: 0,
    currency_code: "KES",
    date: "2026-07-04",
    last_modified_time: "2026-07-04T10:00:00Z"
  };

  const first = normalizeZohoInvoice("agency-main", record);
  const second = normalizeZohoInvoice("agency-main", record);
  assert.deepEqual(first.map((e) => e.id), second.map((e) => e.id));
});
