# ADR-0002 — Bitemporal evidence-backed beliefs

Status: proposed.
Event time and knowledge time differ; preferences and obligations can be invalidated. Plain vector memory retrieves stale facts.
Use `valid_time` and `recorded_time`, evidence references, contradictions, supersession and revocation/deletion handling. Retrieve current relevant beliefs by validity BEFORE similarity.

Trade-offs: indexing and conflict resolution complexity vs replayability and no stale decisions. Verify with Memora and evolving preference scenarios. Sources: Uddin et al. 2026; LongMemEval; temporal database principles.