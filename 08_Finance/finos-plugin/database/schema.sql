CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE SCHEMA IF NOT EXISTS finos;

CREATE TYPE finos.account_class AS ENUM (
  'asset',
  'liability',
  'equity',
  'revenue',
  'expense',
  'reserve',
  'treasury_allocation',
  'tax_obligation',
  'payroll_liability'
);

CREATE TYPE finos.normal_balance AS ENUM ('debit', 'credit');
CREATE TYPE finos.event_status AS ENUM ('recorded', 'processed', 'failed');
CREATE TYPE finos.approval_status AS ENUM ('submitted', 'auto_approved', 'ai_reviewed', 'approved', 'rejected', 'escalated');
CREATE TYPE finos.risk_severity AS ENUM ('info', 'watch', 'warning', 'critical');

CREATE TABLE finos.entities (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  parent_entity_id uuid REFERENCES finos.entities(id),
  legal_name text NOT NULL,
  display_name text NOT NULL,
  entity_type text NOT NULL,
  base_currency char(3) NOT NULL DEFAULT 'USD',
  jurisdiction text,
  active boolean NOT NULL DEFAULT true,
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE finos.clients (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  entity_id uuid NOT NULL REFERENCES finos.entities(id),
  name text NOT NULL,
  segment text,
  status text NOT NULL DEFAULT 'active',
  acquisition_channel text,
  concentration_limit_pct numeric(6, 3) NOT NULL DEFAULT 20,
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE finos.financial_events (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  entity_id uuid NOT NULL REFERENCES finos.entities(id),
  event_type text NOT NULL,
  source text NOT NULL,
  actor_id text,
  correlation_id uuid,
  causation_id uuid,
  payload jsonb NOT NULL,
  metadata jsonb NOT NULL DEFAULT '{}',
  status finos.event_status NOT NULL DEFAULT 'recorded',
  occurred_at timestamptz NOT NULL,
  recorded_at timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX financial_events_entity_type_idx ON finos.financial_events(entity_id, event_type, occurred_at DESC);
CREATE INDEX financial_events_payload_idx ON finos.financial_events USING gin(payload);

CREATE TABLE finos.ledger_accounts (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  entity_id uuid NOT NULL REFERENCES finos.entities(id),
  parent_account_id uuid REFERENCES finos.ledger_accounts(id),
  code text NOT NULL,
  name text NOT NULL,
  class finos.account_class NOT NULL,
  normal_balance finos.normal_balance NOT NULL,
  is_control_account boolean NOT NULL DEFAULT false,
  is_active boolean NOT NULL DEFAULT true,
  created_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE(entity_id, code)
);

CREATE TABLE finos.journal_entries (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  entity_id uuid NOT NULL REFERENCES finos.entities(id),
  event_id uuid NOT NULL REFERENCES finos.financial_events(id),
  description text NOT NULL,
  status text NOT NULL DEFAULT 'posted',
  metadata jsonb NOT NULL DEFAULT '{}',
  posted_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE finos.journal_lines (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  journal_entry_id uuid NOT NULL REFERENCES finos.journal_entries(id) ON DELETE CASCADE,
  entity_id uuid NOT NULL REFERENCES finos.entities(id),
  account_id uuid NOT NULL REFERENCES finos.ledger_accounts(id),
  client_id uuid REFERENCES finos.clients(id),
  project_id uuid,
  department_id uuid,
  currency char(3) NOT NULL,
  debit_minor bigint NOT NULL DEFAULT 0 CHECK (debit_minor >= 0),
  credit_minor bigint NOT NULL DEFAULT 0 CHECK (credit_minor >= 0),
  description text NOT NULL,
  metadata jsonb NOT NULL DEFAULT '{}',
  CHECK (NOT (debit_minor > 0 AND credit_minor > 0)),
  CHECK (debit_minor > 0 OR credit_minor > 0)
);

CREATE INDEX journal_lines_account_idx ON finos.journal_lines(entity_id, account_id);

CREATE OR REPLACE FUNCTION finos.assert_balanced_journal(entry_id uuid)
RETURNS void LANGUAGE plpgsql AS $$
DECLARE
  debit_total bigint;
  credit_total bigint;
BEGIN
  SELECT COALESCE(sum(debit_minor), 0), COALESCE(sum(credit_minor), 0)
    INTO debit_total, credit_total
    FROM finos.journal_lines
   WHERE journal_entry_id = entry_id;

  IF debit_total <> credit_total THEN
    RAISE EXCEPTION 'Unbalanced journal entry %, debit %, credit %', entry_id, debit_total, credit_total;
  END IF;
END;
$$;

CREATE TABLE finos.transactions (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  entity_id uuid NOT NULL REFERENCES finos.entities(id),
  event_id uuid REFERENCES finos.financial_events(id),
  journal_entry_id uuid REFERENCES finos.journal_entries(id),
  client_id uuid REFERENCES finos.clients(id),
  transaction_type text NOT NULL,
  source text NOT NULL,
  category text NOT NULL,
  amount_minor bigint NOT NULL,
  currency char(3) NOT NULL,
  payment_status text NOT NULL,
  transaction_at timestamptz NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE finos.invoices (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  entity_id uuid NOT NULL REFERENCES finos.entities(id),
  client_id uuid NOT NULL REFERENCES finos.clients(id),
  invoice_number text NOT NULL,
  status text NOT NULL,
  amount_minor bigint NOT NULL,
  currency char(3) NOT NULL,
  issued_at timestamptz NOT NULL,
  due_at timestamptz NOT NULL,
  paid_at timestamptz,
  terms text,
  UNIQUE(entity_id, invoice_number)
);

CREATE TABLE finos.budgets (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  entity_id uuid NOT NULL REFERENCES finos.entities(id),
  department_id uuid,
  name text NOT NULL,
  period_start date NOT NULL,
  period_end date NOT NULL,
  amount_minor bigint NOT NULL,
  currency char(3) NOT NULL,
  threshold_pct numeric(6, 3) NOT NULL DEFAULT 90,
  owner_role text NOT NULL,
  active boolean NOT NULL DEFAULT true
);

CREATE TABLE finos.allocation_rules (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  entity_id uuid NOT NULL REFERENCES finos.entities(id),
  name text NOT NULL,
  priority integer NOT NULL DEFAULT 0,
  revenue_stream text,
  effective_from date NOT NULL,
  effective_to date,
  enabled boolean NOT NULL DEFAULT true,
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE finos.allocation_rule_targets (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  allocation_rule_id uuid NOT NULL REFERENCES finos.allocation_rules(id) ON DELETE CASCADE,
  bucket text NOT NULL,
  percent numeric(8, 4) NOT NULL CHECK (percent >= 0 AND percent <= 100),
  target_account_id uuid NOT NULL REFERENCES finos.ledger_accounts(id),
  minimum_reserve_months numeric(8, 2),
  locked boolean NOT NULL DEFAULT false
);

CREATE TABLE finos.allocations (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  entity_id uuid NOT NULL REFERENCES finos.entities(id),
  source_event_id uuid NOT NULL REFERENCES finos.financial_events(id),
  allocation_rule_id uuid REFERENCES finos.allocation_rules(id),
  bucket text NOT NULL,
  amount_minor bigint NOT NULL,
  currency char(3) NOT NULL,
  decision_mode text NOT NULL,
  rationale jsonb NOT NULL DEFAULT '[]',
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE finos.reserves (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  entity_id uuid NOT NULL REFERENCES finos.entities(id),
  reserve_type text NOT NULL,
  ledger_account_id uuid NOT NULL REFERENCES finos.ledger_accounts(id),
  target_months numeric(8, 2),
  target_amount_minor bigint,
  currency char(3) NOT NULL,
  locked boolean NOT NULL DEFAULT false,
  active boolean NOT NULL DEFAULT true
);

CREATE TABLE finos.treasury_balances (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  entity_id uuid NOT NULL REFERENCES finos.entities(id),
  bank_account_ref text NOT NULL,
  treasury_bucket text NOT NULL,
  balance_minor bigint NOT NULL,
  currency char(3) NOT NULL,
  restricted boolean NOT NULL DEFAULT false,
  as_of timestamptz NOT NULL,
  metadata jsonb NOT NULL DEFAULT '{}'
);

CREATE TABLE finos.financial_state_snapshots (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  entity_id uuid NOT NULL REFERENCES finos.entities(id),
  snapshot_type text NOT NULL,
  as_of timestamptz NOT NULL,
  cash_position jsonb NOT NULL,
  ledger_trial_balance jsonb NOT NULL DEFAULT '[]',
  risk_summary jsonb NOT NULL DEFAULT '{}',
  forecast_summary jsonb NOT NULL DEFAULT '{}',
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX financial_state_snapshots_entity_asof_idx
  ON finos.financial_state_snapshots(entity_id, snapshot_type, as_of DESC);

CREATE TABLE finos.forecasts (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  entity_id uuid NOT NULL REFERENCES finos.entities(id),
  scenario text NOT NULL,
  horizon_days integer NOT NULL,
  opening_cash_minor bigint NOT NULL,
  closing_cash_minor bigint NOT NULL,
  currency char(3) NOT NULL,
  runway_days integer,
  assumptions jsonb NOT NULL DEFAULT '[]',
  generated_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE finos.forecast_lines (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  forecast_id uuid NOT NULL REFERENCES finos.forecasts(id) ON DELETE CASCADE,
  forecast_date date NOT NULL,
  inflow_minor bigint NOT NULL DEFAULT 0,
  outflow_minor bigint NOT NULL DEFAULT 0,
  net_minor bigint NOT NULL DEFAULT 0,
  projected_cash_minor bigint NOT NULL,
  confidence numeric(5, 4) NOT NULL,
  drivers jsonb NOT NULL DEFAULT '[]'
);

CREATE TABLE finos.approvals (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  entity_id uuid NOT NULL REFERENCES finos.entities(id),
  request_type text NOT NULL,
  resource_id text,
  amount_minor bigint NOT NULL,
  currency char(3) NOT NULL,
  requested_by text NOT NULL,
  required_approver_role text NOT NULL,
  status finos.approval_status NOT NULL,
  reason text NOT NULL,
  decided_by text,
  decided_at timestamptz,
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE finos.profitability_metrics (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  entity_id uuid NOT NULL REFERENCES finos.entities(id),
  client_id uuid REFERENCES finos.clients(id),
  service_id uuid,
  department_id uuid,
  period_start date NOT NULL,
  period_end date NOT NULL,
  revenue_minor bigint NOT NULL,
  delivery_cost_minor bigint NOT NULL,
  acquisition_cost_minor bigint NOT NULL,
  gross_margin_pct numeric(8, 4) NOT NULL,
  contribution_margin_pct numeric(8, 4) NOT NULL,
  ltv_to_cac numeric(10, 4),
  payback_months numeric(10, 4),
  currency char(3) NOT NULL,
  risk_flags jsonb NOT NULL DEFAULT '[]'
);

CREATE TABLE finos.risk_signals (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  entity_id uuid NOT NULL REFERENCES finos.entities(id),
  risk_type text NOT NULL,
  severity finos.risk_severity NOT NULL,
  title text NOT NULL,
  message text NOT NULL,
  metric text NOT NULL,
  current_value numeric NOT NULL,
  threshold numeric NOT NULL,
  recommended_actions jsonb NOT NULL DEFAULT '[]',
  detected_at timestamptz NOT NULL DEFAULT now(),
  resolved_at timestamptz
);

CREATE TABLE finos.audit_logs (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  entity_id uuid NOT NULL REFERENCES finos.entities(id),
  actor_id text NOT NULL,
  action text NOT NULL,
  resource_type text NOT NULL,
  resource_id text NOT NULL,
  metadata jsonb NOT NULL DEFAULT '{}',
  previous_hash text,
  hash text NOT NULL,
  occurred_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE finos.integration_connections (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  entity_id uuid NOT NULL REFERENCES finos.entities(id),
  kind text NOT NULL,
  name text NOT NULL,
  status text NOT NULL DEFAULT 'configured',
  scopes text[] NOT NULL DEFAULT '{}',
  last_synced_at timestamptz,
  metadata jsonb NOT NULL DEFAULT '{}'
);

CREATE TABLE finos.subscriptions (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  entity_id uuid NOT NULL REFERENCES finos.entities(id),
  vendor_name text NOT NULL,
  service_name text NOT NULL,
  amount_minor bigint NOT NULL,
  currency char(3) NOT NULL,
  cadence text NOT NULL,
  next_renewal_at date,
  owner_department_id uuid,
  strategic_justification text,
  status text NOT NULL DEFAULT 'active',
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE finos.payroll_runs (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  entity_id uuid NOT NULL REFERENCES finos.entities(id),
  period_start date NOT NULL,
  period_end date NOT NULL,
  gross_pay_minor bigint NOT NULL,
  tax_withheld_minor bigint NOT NULL DEFAULT 0,
  employer_cost_minor bigint NOT NULL DEFAULT 0,
  currency char(3) NOT NULL,
  status text NOT NULL DEFAULT 'scheduled',
  executed_at timestamptz,
  created_at timestamptz NOT NULL DEFAULT now()
);

INSERT INTO finos.entities (id, legal_name, display_name, entity_type, base_currency, jurisdiction)
VALUES ('00000000-0000-0000-0000-000000000001', 'Agency Main Entity', 'Agency Main', 'operating_company', 'USD', 'TBD')
ON CONFLICT DO NOTHING;
