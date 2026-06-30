import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { createFinOsApplication } from "./application.js";
import { createToolHandlers, jsonContent, toolSchemas } from "./contracts.js";

const app = createFinOsApplication();
const handlers = createToolHandlers(app);

const server = new McpServer({
  name: "finos",
  version: "0.1.0"
});

server.tool("get_cash_position", toolSchemas.getCashPosition, async (input) => jsonContent(handlers.get_cash_position(input)));
server.tool("forecast_cashflow", toolSchemas.forecastCashflow, async (input) => jsonContent(handlers.forecast_cashflow(input)));
server.tool("allocate_capital", toolSchemas.allocateCapital, async (input) => jsonContent(await handlers.allocate_capital(input)));
server.tool("approve_expense", toolSchemas.approveExpense, async (input) => jsonContent(handlers.approve_expense(input)));
server.tool("detect_financial_risk", toolSchemas.detectFinancialRisk, async (input) => jsonContent(handlers.detect_financial_risk(input)));
server.tool(
  "calculate_client_profitability",
  toolSchemas.calculateClientProfitability,
  async (input) => jsonContent(handlers.calculate_client_profitability(input))
);
server.tool("generate_financial_report", toolSchemas.generateFinancialReport, async (input) =>
  jsonContent(handlers.generate_financial_report(input))
);
server.tool("analyze_runway", toolSchemas.analyzeRunway, async (input) => jsonContent(handlers.analyze_runway(input)));
server.tool("monitor_liquidity", toolSchemas.monitorLiquidity, async (input) => jsonContent(handlers.monitor_liquidity(input)));
server.tool("evaluate_growth_capacity", toolSchemas.evaluateGrowthCapacity, async (input) =>
  jsonContent(handlers.evaluate_growth_capacity(input))
);

await server.connect(new StdioServerTransport());
