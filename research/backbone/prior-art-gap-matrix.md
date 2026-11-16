# Prior Art and Non-Novelty Matrix — Adaptive Routin

| Existing technique | Evidence/reference | Already known | Routin remaining question | Reject proposed contribution if |
|---|---|---|---|---|
| HTN/PDDL-style decomposition | SHOP2, P081 | goal/task methods reduce to operators with preconditions | unknown-domain mapping to typed goals and verified operators | standard HTN with same evidence works equally well |
| Interleaved reasoning/action | ReAct, P080 | feedback changes a working plan | correct user-goal and permission grounding | ReAct + policy wrapper matches result |
| Dynamic tool discovery | P071/P072 | retrieval and abstract tool stubs can scale to large catalogs | selection with changing scope and external verification | existing hybrid retrieval performs equivalently |
| Planning diagnostics | APB, P073 | failure may be planning, tool noise, infeasible task | joint diagnostic of personal obligations and tool lifetime | APB-style pipeline covers all cases |
| Stateful tool execution | ToolSandbox/tau-bench, P077/P078 | end state and intermediate state matter | evidence-bound human agreement and long-running commitments | standard stateful tool agent matches outcome |
| Durable workflows | Temporal docs; Sagas P027 | replay/compensation are established | integration with uncertain social/permission evidence | off-the-shelf workflows resolve same failure cases |
| Continual learning and memory | CL-Bench/StreamMemBench/CLE, P074–P076 | storing facts may not yield later task improvement | verified procedure promotion and negative-transfer control | in-context baseline learns as well |
| Harness-oriented RL | Agent Lightning P079 | training loop can be decoupled from agent harness | only after audited, consented trace reward is reliable | reward or performance regressions outweigh gains |
| Real professional task evaluation | ALE P082 | real long-horizon tasks require outcome-based assessment | measurable user/coordination effects and held-out life domains | realistic users receive no net benefit |

## High-leverage unresolved issue

The field has strong components for planning, tool discovery, memory and workflows. The unresolved practical difficulty is **when all these components disagree**:
- tool search suggests a valid API that current policy forbids;
- an inferred habit conflicts with a stated personal goal;
- an acquired memory is valid but wrong for the present social relationship;
- a plan predicts completion while the world returns unknown;
- a feedback-driven skill applies to the wrong person/domain;
- the simplest task does not justify an extra multi-model planning cycle.

A useful Routin research contribution must resolve such contradictions in a formal, verifiable, and cost-effective manner. A diagram or taxonomy does not establish it.

## Proof standard

Primary source -> precise tested result -> boundary assumptions -> Routin's derived mechanism -> typed contract -> counterexample -> executable test -> baseline superiority -> measured end-user outcome. Do not assert novelty before independent related-work scrutiny and experiments.