# S13 — The Operational Cost of Learning From Everything

**Research:** Agent Memory P047 + Mem0 P054 + A-MEM P053 + Memory-R1 P055 + AdaMEM P045 + complementary learning P057.

## Synthesis

A memory store has a write path, read path, maintenance path, invalidation path and serving path. State can be correct but not yet indexed; an asynchronous memory update can lag behind a new verified instruction. LLM-based construction can consume more compute than users' actual queries, depending on workload.

Routin is a continuous-ingestion, often sparse-query agent. It should not run a multi-model extraction/reflection/embedding pipeline on every webhook. Instead, the operational event/state ledger is committed synchronously; optional knowledge construction is enqueued and coalesced; critical invalidations bypass consolidation queues.

## Proposed strategy

Immediate: write canonical event, source freshness, responsibility transition, explicit preference override and permission revocation.

Deferred: extract candidate routine hypotheses, episodic summary, optional semantic links and learned procedure from already verified episode.

Conditional: run heavier analysis on detected contradiction, new deadline, failure, user correction or anticipated decision value.

Discard or quarantine: untrusted, unsupported, revoked, obsolete or harmful memories. No rule based solely on frequency or recency.

## Scientific challenge

There is a Pareto frontier among accuracy, responsiveness, storage footprint, write energy, query latency and update freshness. A more complex graph may help relational tasks but fail on cheap fact lookup.

## Test

Vary event rates, real decision query frequencies, memory update workloads, model sizes and retention policies. Report total lifecycle expense *per verified useful action*, stale-write delays, false memory selection and memory influence on external behavior. Baseline a simple current-state DB + BM25 to justify additional components.