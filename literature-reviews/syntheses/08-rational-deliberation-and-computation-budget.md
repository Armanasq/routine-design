# S08 — A good assistant knows when not to think harder

**Intersection:** [P008](../active-elicitation/P008.md), [P009](../active-elicitation/P009.md), [P019](../metareasoning/P019.md), [P020](../conservative-learning/P020.md).

## Derivation
Decision-theoretic elicitation treats questions as costly actions; bounded rationality treats computation as costly too. A reasonable assistant must optimize not just what answer it gives, but also whether to spend more resources to get a better answer. The danger is recursively expensive deliberation over trivial updates.

## Routing
1. Deterministic event reconciliation first.
2. Cheap extractor and typed validation for ambiguous source text.
3. If there is material outcome sensitivity and evidence uncertainty: bounded additional computation, alternate-model check or external evidence query.
4. If uncertainty remains decision-relevant and answerable only by user: ask one focused question at appropriate time.
5. If deadline/risk too high: fail closed or use predefined critical guardrail; do not keep reasoning past last safe action time.

Estimate `VOC = expected reduction in decision loss - compute and delay cost` and `VOI = expected reduction after user response - query and delay cost`. At cold start use coarse thresholds and deterministic conservative policies; finely calibrated values are not assumed.

## Experimental contrast
Always-fast, always-expensive, agent-swarm and gated routing. Compare cost per verified responsibility, high-severity error, p95 latency, unnecessary user queries and corrections; record model/prompt versions.

## Architecture
[Attention policy](../../docs/algorithms/attention-and-initiative.md), [ADR-0005](../../decisions/ADR-0005-no-automatic-multiagent-swarm.md).