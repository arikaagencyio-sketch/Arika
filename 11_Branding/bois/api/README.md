# API Layer

BOIS API adapters should expose the cognitive infrastructure without bypassing retrieval or governance.

## Required Endpoints

- `POST /clients`: create client object and workspace.
- `POST /clients/{client_id}/ingest`: ingest onboarding documents and notes.
- `POST /clients/{client_id}/context`: assemble Dynamic Brand Context.
- `POST /clients/{client_id}/execute`: activate agents and produce governed output.
- `POST /clients/{client_id}/score`: run brand scoring.
- `GET /clients/{client_id}/memory`: read memory streams.
- `GET /clients/{client_id}/governance`: read audit history.

## API Rule

No API route should generate strategic output unless the Retrieval Gate has passed and governance validation is scheduled.

