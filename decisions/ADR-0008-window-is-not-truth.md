# ADR-0008 — Context Window Is a Cache, Not the Source of Truth

**Status:** adopted for research architecture; experimental validation pending.

## Context
Long context suffers cost and state staleness. MemGPT provides prior art for context paging; MAGE prioritizes execution path integrity; memory system benchmarks show retrieval and construction costs vary by task.

## Decision
Construct each inference's ContextCapsule from a consistent version of typed operational state. Mandatory constraints, identity, scope, grants and source health cannot be omitted merely to fit tokens. Optional memory is selected under a budget and access rules. A context summary cannot authorize external effects or overwrite database facts.

## Alternatives
Full chat history (expensive, obsolete facts), vector top-K (may omit critical constraints), monolithic "user profile" prompt (scope and drift ambiguity).

## Risks / tests
Higher complexity and possible abstentions. Test with deliberate low token budgets, masked critical grant, source revocation and contradictory preferences; require zero dropped hard constraints.