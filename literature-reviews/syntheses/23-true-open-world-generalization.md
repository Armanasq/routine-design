# S23 — A Generalist Should Transfer the Method, Not Memorize Cases

**Linked research:** P082 (Agents' Last Exam), P074 (CL-Bench), P076 (CLE), P073 (APB), P081 (HTN planning), P072 (tool retrieval).

## Fundamental distinction

One hundred examples across sixteen domains demonstrate breadth of desired use, but they do not establish a universal generalist. Hardcoding responses or prompts per example would produce a wide task router, not an adaptive secretary. A genuine generalist must solve **unseen combinations** of abstract goals, operators, evidence, time, constraints and user values.

ALE highlights poor performance on difficult sustained professional work despite strength on conventional benchmarks. CL-Bench and CLE show persistent difficulties in becoming more capable from prior experience. Planning and tool discovery research demonstrate useful components but do not guarantee end-to-end competence.

## Proposed research construction

Build a benchmark generator taking scenario seeds, world-state distributions, tool registries, user-intention rules, source visibility, permission grants and external outcome oracles. Train/design on known combinations; evaluate whole held-out domains, entirely new tool schemas/names, and changed-goal multi-week histories. Always include tasks that should proceed and tasks that should abstain.

## Core scientific hypothesis

A typed, verifiable capability-and-state backbone combined with selective dynamic tool discovery and evidence-certified experience learning improves cross-domain outcome reliability at the same compute/permission budget relative to a generic ReAct agent and static scripted/task-routed assistants. This is a hypothesis, not established novelty; study must disambiguate the benefit from access to more tools.

## Failure conditions

Overfitting to wording, invented tool bindings, wrong-context preference, source/permission mismatch, false claim of completion, negative skill transfer and excessive user-question burden. If a simple static coordinator performs equally well, reject unnecessary complexity.

**Test data:** research/scenarios/universal-100.json. None of these example IDs may be runtime dispatch conditions.