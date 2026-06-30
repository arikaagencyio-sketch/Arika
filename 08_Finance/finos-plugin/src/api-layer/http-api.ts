import Fastify from "fastify";
import { createFinOsApplication } from "./application.js";
import { createToolHandlers, toolSchemas } from "./contracts.js";
import { z } from "zod";

const app = createFinOsApplication();
const handlers = createToolHandlers(app);
const server = Fastify({ logger: true });

function body<TShape extends z.ZodRawShape>(shape: TShape, value: unknown): z.infer<z.ZodObject<TShape>> {
  return z.object(shape).parse(value);
}

server.get("/health", async () => ({
  ok: true,
  service: "finos",
  doctrine: "liquidity-first"
}));

server.get("/cash-position", async () => handlers.get_cash_position({}));

server.post("/forecast-cashflow", async (request) =>
  handlers.forecast_cashflow(body(toolSchemas.forecastCashflow, request.body))
);

server.post("/allocate-capital", async (request) =>
  handlers.allocate_capital(body(toolSchemas.allocateCapital, request.body))
);

server.post("/approve-expense", async (request) =>
  handlers.approve_expense(body(toolSchemas.approveExpense, request.body))
);

server.post("/detect-risk", async (request) =>
  handlers.detect_financial_risk(body(toolSchemas.detectFinancialRisk, request.body))
);

server.post("/client-profitability", async (request) =>
  handlers.calculate_client_profitability(body(toolSchemas.calculateClientProfitability, request.body))
);

server.post("/financial-report", async (request) =>
  handlers.generate_financial_report(body(toolSchemas.generateFinancialReport, request.body))
);

const host = process.env.FINOS_HTTP_HOST ?? "0.0.0.0";
const port = Number(process.env.FINOS_HTTP_PORT ?? "8787");
await server.listen({ host, port });
