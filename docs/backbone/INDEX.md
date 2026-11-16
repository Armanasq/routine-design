# Adaptive Routin Backbone — Reading Path

1. [Vision and component contracts](00-practical-intelligence-architecture.md)
2. [Goal interpretation and abstract capability model](01-intention-and-capability-model.md)
3. [Dynamic registry and tool retrieval](02-dynamic-tool-discovery.md)
4. [Planning and meta-decision loop](03-adaptive-planning-and-control.md)
5. [Experience, adaptation and continual learning](04-experience-and-continual-learning.md)
6. [Durable workflow execution, unknown side effects and verified outcomes](05-durable-execution-and-unknown-outcomes.md)
7. [Unseen domain admission without scripts](06-unseen-domains-and-competence.md)
8. [Production architecture and tool interfaces](07-production-technology-and-interfaces.md)
9. [Open-world evaluation and research gates](08-research-and-acceptance-benchmarks.md)
10. [Personal secretary judgment and attention policy](09-assistant-identity-and-initiative.md)

## Implementation and evidence

- [Reference dynamic planner](../../reference_kernel/adaptive_planner.py) and [verification contract](../../reference_kernel/ADAPTIVE.md).
- [100 case seeds, human-readable](../../research/scenarios/universal-100.md) and [JSON corpus](../../research/scenarios/universal-100.json).
- [82 individual paper reviews](../../literature-reviews/README.md), [23 cross-paper syntheses](../../literature-reviews/syntheses/), [34 mechanism graph](../../research/knowledge-map.json).
- [Prior-art gap analysis](../../research/backbone/prior-art-gap-matrix.md), [experiments](../../research/backbone/experimental-hypotheses.md).
- [6 new typed schemas](../../schemas/) and ADR-0015–0017 under [architecture decisions](../../decisions/).

## Scope

The dynamic Python kernel is a **tested reference**; runtime LLM inference, actual MCP discovery, verified tool grants, real workflows, learned policy updates and longitudinal evaluations remain future work. The 100 scenarios are not executable templates.