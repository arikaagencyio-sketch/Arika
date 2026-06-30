# Vector Memory

This folder stores vector-memory adapters, embedding manifests, and external vector database connection notes.

## Current Local Mode

BOIS currently uses local hybrid retrieval:

- paragraph-preserving corpus index
- taxonomy tags
- reinforcement counts
- keyword scoring
- memory-event retrieval

This makes retrieval usable without external services.

## External Vector Mode

When embedding services are attached, each paragraph and memory event should receive:

- `embedding_id`
- `source_type`
- `source_path`
- `paragraph_id` or `memory_event_id`
- `client_id`
- `tags`
- `created_at`
- `model`
- `vector_db_collection`

## Required Collections

- `bois_source_corpus`
- `bois_client_memory`
- `bois_campaign_memory`
- `bois_visual_memory`
- `bois_narrative_memory`
- `bois_governance_memory`
- `bois_market_memory`
- `bois_trend_memory`

