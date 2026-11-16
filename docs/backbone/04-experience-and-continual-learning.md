# Experience-Driven Adaptation Without Hardcoded Behavior

## Why better memory is not better learning

CL-Bench (2026) evaluates sequential improvement across six expert-validated domains and finds substantial limitations in memory-oriented systems; in its evaluated conditions simple in-context learning outperformed dedicated memory approaches.

StreamMemBench (Findings of EMNLP 2026) tests whether observed streaming evidence and interaction feedback improve subsequent future-oriented personal assistance. Systems often store evidence or feedback without reliably using it in the follow-up.

Continual Learning Exam (October 2026 preprint) spans 600 levels across 89 roles in 12 occupational domains, finding that failure-feedback revision helps some configurations but long-horizon competence remains difficult. These results are evidence against equating retained text with sustained skill improvement.

Canonical references:
- https://arxiv.org/abs/2606.05661
- https://aclanthology.org/2026.findings-emnlp.992/
- https://arxiv.org/abs/2610.33956

## Four learning targets

1. **World model:** what is currently true or unknown about sources, events, relationships and obligations.
2. **Personal model:** how the user explicitly wants to be helped, chosen goals, recurring conditions and changing scoped preferences. Observed behavior is not assumed desired.
3. **Skill/process model:** which verified procedure helps under which preconditions and what failures disqualify transfer.
4. **Meta-policy:** when to deliberate more, ask, retrieve experience, trust a procedure, reduce intervention frequency, or refresh strategy.

Learning one class must not automatically change the others. A successful scheduling procedure can improve action selection but cannot confer standing communication rights.

## Evidence-to-learning algorithm

(1) Record source-backed episode including original intent, candidate actions, presented options, policy/version, actual tool effects, verification evidence and user correction.

(2) Separate observable outcomes from inferred causes and from the assistant's own exposure effects (e.g., work task clicked because only work tasks were displayed).

(3) Identify what a prior strategy predicted versus what occurred; assign a *candidate cause*, keeping alternate explanations and context scope.

(4) Test whether the candidate learning would improve decisions in counterexamples and held-out, nonidentical situations. Avoid turning one unusual episode into a global preference.

(5) Promote only validated scoped facts, procedure candidates or metacognitive thresholds. New procedures enter shadow/sandbox phase, not immediate privileged execution.

(6) Version all learned state; preserve correction and rollback paths; invalidate derived memory when underlying permissions or evidence are revoked.

(7) Measure improvement in **later** tasks from the same underlying latent structure, not just immediate feedback satisfaction. Report negative transfer and regressions.

## When to update model weights

External memory/state and procedural catalog should come first. Online fine-tuning or RL on personal data adds privacy, non-stationarity, catastrophic interference, reward gaming and evaluation challenges. Agent Lightning (2025) establishes harness/training separation; it is a possible future offline research path, not justification for uncontrolled self-training from users.

Only consider trained update policies after a consented corpus, external validity, explicit reward and attribution study, baseline superiority, model rollback, and hard constraints kept outside the learned policy.

## A hard problem: determining whether the agent improved

For a repeated task sequence, define incremental learning gain relative to the same backbone with state reset. Keep task difficulty, available tools and grants comparable. A stronger base model can solve more without learning. A memory system that helps on old cases but impairs new ones has poor transfer.

Measure: verified later success, critical failure, adaptation latency, newly learned reusable procedures, false preference generalization, regret versus a competent static baseline, user correction burden, lost-goal capacity, cost per outcome.

## Receptivity and autonomy

Learning "do not interrupt me when I am working" can inform timing, but may not override the last-safe moment for a confirmed critical obligation. A user can choose learning mode, collaboration, or delegation per goal. The model must not infer implicit permission from ease of task completion.

## Testing

New intent variants and unseen domains, experience with a failed provider and a later safe task, contradictory one-week preference exceptions, policy-exposure feedback, reversible and irreversible tool errors, unknown recipient, repeated failed strategy and evidence invalidation. Compare no memory, flat RAG, typed temporal memory, dynamic strategy retrieval, certified procedure reuse, and full system.

The core contribution would be a measured *coupling* between memory validity, plan improvement and actual low-burden user outcomes; each individual component has established prior art.