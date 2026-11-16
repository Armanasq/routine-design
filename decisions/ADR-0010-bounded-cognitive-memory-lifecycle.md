# ADR-0010 — Memory Construction, Recall and Maintenance Have Separate Budgets

**Status:** proposed.

## Problem
Complex memory systems can spend more computation constructing memories than is justified by downstream action volume. Asynchronous indexing can leave stale personalized decisions.

## Decision
Synchronously maintain canonical event and essential current state. Schedule optional episodic reflection, semantic linking and procedure extraction based on expected usefulness and cost. Permission revocation and explicit preference supersession invalidate active derived context immediately. Keep lifecycle accounting and compare against typed SQL + BM25 baseline before deploying expensive graph or LLM-memory infrastructure.

## Trade-offs / verification
Sophisticated retrieval may help relational tasks, but cost and complexity can dominate. Measure write/read/maintenance cost, update freshness, downstream task correctness and personal outcome value; abort architectural expansion without measured utility.