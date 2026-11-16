# Universal Cross-Domain Evaluation Protocol

**Status:** benchmark DESIGN, not an executed experiment.

## Purpose

Test whether Routin can coordinate multi-domain responsibilities under real permission, memory, time and competence constraints without giving specialist claims beyond its evidence.

## Benchmark units

- **Goal episode:** user-chosen goal across sessions and its measurable or partially observable distal outcome.
- **Responsibility episode:** owner/party/accepted commitment, dependencies, known source coverage and externally verified status.
- **Intervention decision:** whether to do nothing, prepare, ask, interrupt, draft, execute or escalate.
- **Capability-use episode:** pack selection, evidence requirements, current consent and specialist output.
- **Cross-domain interference:** unexpected effect on other goals, private data, relationships or capacity.

## Fixtures and oracles

16 synthetic adversarial scenarios live in \`tests/scenarios/universal/\`. Each must eventually specify a ground-truth event state, source visibility delays and role/grant model. A paper ID provides rationale, not a numeric weight. Test runner must assert mandatory safety invariants separately from useful suggestions.

## Baselines

B0 generic LLM with tools and no domain pack, within equivalent grants.
B1 independent specialist helpers with fragmented state.
B2 one coordinator + static packs without memory/attention learning.
B3 B2 + temporal belief and evidence.
B4 B3 + constrained cross-domain planner.
B5 B4 + intent-sensitive intervention/noop and procedure memory.

Compare at equal source visibility, external effect permissions, model budget and simulated environmental conditions. No benchmark score should conflate physical harm and time savings into one scalar.

## Metrics

Verified outcome accuracy and abstention; false completed state; unauthorized effects; sensitive data leaks; missed critical obligations; decision correction effort; total user coordination time; protected goals; human agency and selected support-mode adherence; delayed learning performance when defined; intervention burden; specialist competence violations; negative transfer rate; full lifecycle memory/tool cost.

For health/wellbeing, measure no unsupported clinical claims and reasonable professional escalation. Health outcome improvement requires validated clinical evidence and appropriate study design; do not claim it from simulation.

## Human external validation

After a safe sandbox and an approved privacy program, run longitudinal opt-in research across realistic user-selected domains. Avoid coercing health data collection or estimating mental states from routine activity. Evaluate real impact, hard negative outcomes and subgroup differences.

## Novelty gate

A configurable task taxonomy is not novelty. Domain composition must demonstrate superior error-controlled behavior in novel combinations. Report negative evidence and conditions where a simpler assistant is better.
