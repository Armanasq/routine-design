# Open-World Agent Research Program and Quality Gates

## The right scientific question

Can a general personal secretary **solve unfamiliar combinations of goals, tools and conditions** more accurately, economically and safely through continual experience, without requiring users to configure a rigid workflow?

There is substantial prior art for generic planning, retrieval, dynamic tool selection, skill learning and durable execution. Routin must measure a new integration or distinct method to claim contribution, not assert novelty because it has many modules.

## Benchmark foundations

APB (Findings EMNLP 2026): 4,209 diagnostic planning cases over 22 domains including broken/misleading tools and unsolvable tasks. https://aclanthology.org/2026.findings-emnlp.1041/

ToolSandbox (2024): stateful tool-dependent and user-interactive trajectories; milestone correctness rather than only final text. https://arxiv.org/abs/2408.04682

tau-bench (2024): simulated user-tool interactions with policy adherence and database goal-state verification; repeated trials expose instability. https://arxiv.org/abs/2406.12045

CL-Bench (2026): improvement from sequential experience in six latent-structure domains, where dedicated memory is not uniformly better than simple in-context learning. https://arxiv.org/abs/2606.05661

StreamMemBench (Findings EMNLP 2026): streaming perception/feedback to later assistance with separate evidence use and reuse metrics. https://aclanthology.org/2026.findings-emnlp.992/

Continual Learning Exam (Oct 2026): five-stage ladders and user feedback across professional disciplines; scores remain far from sustained full competence. https://arxiv.org/abs/2610.33956

Agents' Last Exam (2026): long-horizon expert-sourced economic work and verified outcomes; task taxonomy rather than short chat QA. https://arxiv.org/abs/2606.05405

## Our 100 scenarios are evaluation seeds

The corpus is NOT proof of domain coverage. For each seed generate:
- a world with explicit goals and hidden/partly visible state;
- multiple possible action sequences (including valid NOOP and abstention);
- a mutable registry with some missing, irrelevant, malicious or renamed capabilities;
- strong and revoked permission variants;
- official and unreliable source evidence, with time and gaps;
- related future tasks in which correct feedback reuse is measurable;
- externally checkable outcome predicates.

Hold out entire categories, provider schemas and new goal combinations during development. Paraphrasing an already seen prompt is weak evidence of transfer.

## Pre-registered baselines

B0: rule-based deterministic coordinator for known valid operations.
B1: one-shot LLM answer plus fixed static tools.
B2: ReAct iterative model with full tools in prompt.
B3: retrieve-first tool recommendation with static planner.
B4: plan-first abstract capability stubs and retrieval.
B5: goal/effect planner + immutable registry + validation, no learned memory.
B6: B5 plus scoped evidence and episodic memory.
B7: B6 plus experience-validated skills and independent strategy revision.

Match model, total tokens, available trusted tools, user grants, source visibility and simulated event stream. Compare both raw utility and a fixed-budget Pareto front; agentic extra deliberation may only pay on complex cases.

## Critical metrics

1. Verified end-to-end outcome, not generative answer confidence.
2. Tool/operation coverage: did discovery find every necessary real capability?
3. Correct planning under preconditions, dependencies, available resources and changing state.
4. Dynamic adaptation to a new tool/removed tool or changed user end.
5. Source correctness: absence versus unknown, conflicting/expired facts, recipient identity.
6. Authorized operation count and sensitive-data disclosure count (zero tolerance for ungranted effects).
7. False completion and duplicate provider side effects.
8. Later-task *incremental learning gain* vs reset/no-memory baseline.
9. Negative transfer across different domains, people, permissions and goals.
10. Unnecessary user questions, interruptions and correction time.
11. Goal/skill autonomy preserved, including wellbeing and user-protected commitments.
12. Total inference, tool, memory construction, deployment and recovery costs per verified success.

Report separately, not as one invented universal productivity score. Hard safety gates exclude unsafe runs from aggregate "success".

## Main discriminating tests

- **Unknown capability:** new provider exposes equivalent effect under random name; no new branch in application code.
- **Tool removal:** goal remains; planner finds alternative or returns credible unsupported state.
- **Plan vs registry drift:** registry changes between plan and dispatch; call blocked and rebound.
- **Partial observability:** webhook gap prevents conclusion that a person has not responded.
- **Conflicting goals:** work deadline collides with user-selected study, family and recovery; plan does not silently choose life values.
- **Adaptation:** after observing a failed plan and verified reason, later related task should improve without harming unrelated tasks.
- **Procedural transfer:** prior successful "send email" skill cannot transfer its authority to medical notes or payment.
- **Out-of-domain:** new physical/clinical/legal tasks receive safe partial coordination, not fictional expertise.
- **Budget effects:** extra model calls improve quality only when their incremental value outweighs expense.
- **Unsolvable:** insufficient tool coverage vs search budget exhausted vs missing permission clearly differentiated.

## Causal claim discipline

Experiments compare the same capabilities on paired random event streams. If the new policy performs better, ablate memory, abstract tool decomposition, search policy, validation, context refresh and strategy repair. Report confidence intervals, cost and failures. Do not claim agent improvement because the underlying LLM model was upgraded.

## Roadmap

R0: source-traceable domain-independent formal state and 100 scenario corpus.
R1: dynamic registry, typed operator schema, isolated reference planner and failure cases.
R2: goal interpreter + external language model proposals and deterministic validation.
R3: stateful, fault-injected tool simulator with withheld domain/registry splits.
R4: episodic memory, later-task learning and negative-transfer comparisons.
R5: durable workflow, provider reconciliation and explicit user grants.
R6: consented, longitudinal human pilot with meaningful goal outcomes and administrative burden measurement.

Only R0 plus a narrow R1 demonstrator are present in this repository as of this specification. The other stages require implementation and validation.