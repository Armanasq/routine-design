# ADR-0005 — Bounded orchestration over agent swarms

Status: proposed.
Unbounded multi-agent planners increase latency, cost and cross-agent uncertainty without guaranteeing correctness. Prefer deterministic fast path, typed LLM proposal/validation when warranted, and bounded expensive reasoning on consequential ambiguity.

Alternatives: separate long-running LLM agents for each source (cross-agent race and opaque state); fully deterministic system (weak language understanding). Evaluate cost per verified resolution, recovery and state drift. Add specialist model only on measured improvement. Sources: bounded rationality and rational metareasoning.