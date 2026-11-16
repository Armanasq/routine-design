# Routin: Cross-Disciplinary Mechanism Synthesis

**Research date:** 2026-11-16  
**Scope:** Addendum to `Routin_Research_Architecture_2026-11-16.md`; research and backend architecture only. No UI design or implementation.  
**Status:** Mechanism-oriented scoping review and experimentally testable architecture. Not a systematic review, proof of novelty, or a validated Routin intervention.

## Executive thesis

The most defensible evolution is a **closed-loop personal coordination controller** operating over a versioned belief state about obligations, relations, capacity, intentions, and preferences. It should decide whether to observe, compute, ask, prepare, schedule, protect focus, request authorization, act, or verify. The same policy must know when *not* to do these things.

The scientific value lies in connecting mechanisms from fields often studied separately: prospective memory, distributed cognition, implicit coordination, goal systems, stochastic operations research, active preference elicitation, rational metareasoning, causal feedback learning, and transaction-safe agent execution. Each connection below is a Routin design hypothesis, not a claim that the cited papers tested Routin.

## Method and evidence limits

Multiple targeted SciSpace scholarly searches and follow-up primary-source web searches were conducted across psychology, cognitive ergonomics, administrative work, operations research, machine learning, database systems, and agent safety. Relevant titles were triaged for methodological fit, examined via scholarly abstracts and metadata, and selected papers through publisher-accessible HTML and structured academic research extraction. Some publisher full texts are paywalled or blocked; do not label their abstracts as full-text reads. Formal studies, theory papers, benchmarks, preprints, and engineering specifications are separated. Sources below give persistent DOI/venue URLs wherever possible.

- **E1 empirical:** Controlled experimental or field studies and published quantitative research; valid within the studied population/task.
- **E2 conceptual:** Theory, ethnography, formal models, and review papers; useful mechanisms but no direct Routin effect estimate.
- **E3 computational:** Algorithmic guarantees under explicit assumptions or simulation/benchmark evaluations; not real-world user outcomes.
- **E4 engineering:** Official specifications and mature systems patterns; implementation evidence, not psychological efficacy.
- **E5 early:** Recent preprints or small exploratory studies; hypotheses only until replicated.

The labels describe evidence *type*, not numeric scientific quality scores.

## 1. Research-to-mechanism chains

### M01. Prospective memory + value of asking + interruption modeling -> Intent Externalization Controller

**Sources:** Gilbert (2015) [S04; experimental E1], Boutilier (2002) [S08; E2/E3], Chajewska et al. (2000) [S09; E3], Kapoor and Horvitz (2008) [S10; E1].

**What the papers actually establish.** Gilbert studied strategic external reminders across four web experiments (N=1196): offloading could improve remembering delayed intentions, and participants adapted offloading to burden and interruptions. Boutilier formalized preference elicitation as a POMDP; Chajewska et al. showed how to choose informative utility questions rather than exhaustively survey a user. Kapoor and Horvitz compared automated strategies for asking users about interruption cost, incorporating the cost of probing.

**Derived Routin mechanism:** Capture every candidate intention in an evidence-backed ledger, but choose a trigger, user question, or silence independently. Estimate the cost of forgetting and the potential value of clarifying what matters. Use an explicit non-LLM rule for critical deadlines even if the interruptibility model is uncertain. A reminder may be bound to a situation (before a meeting, when a document becomes ready, at a planned breakpoint), not just a clock.

**Inputs:** responsibility, deadline distribution, intent confidence, user context, data freshness, interruptibility estimate, potential cost of error. **Output:** `monitor | contextual_cue | ask | brief | interrupt`. **Mechanism:** ask only when `expected_loss_without_answer - expected_loss_with_answer > clarification_cost + delay_cost`, subject to critical-event safeguards. **Risk:** uncertain preferences, wrong location/context inference, missed cues. **Test:** compare missed intention rate and intrusions per correctly fulfilled intention versus clock reminders and static thresholds.

### M02. Task interruption + ready-to-resume planning + robust schedule stability -> Work-Resumption Guardian

**Sources:** Leroy and Glomb (2018) [S05; E1], Iqbal and Bailey (2008) [S06; E1], Herroelen and Leus (2004) [S17; E3], Lambrechts et al. (2008) [S18; E3].

**Papers:** A four-study program found ready-to-resume plans reduced attention residue when switching under anticipated time pressure; notification timing around task breakpoints matters. Operations research shows the value of resilient baseline schedules, planned buffers, and reactive rescheduling that minimizes disruptive departures from the plan.

**Derived mechanism:** If an interruption is authorized and valuable enough, capture `current_objective, next_step, unfinished_decisions, relevant_artifact, safe_return_condition` as a resumption capsule. Predict earliest feasible return, optionally create a protected recovery block, and re-optimize around it with a penalty for schedule churn. Do not demand that the user write a resume note; infer only when there is adequate evidence, otherwise use an optional one-line confirmation.

**Risk:** weak context inference, extra work caused by ritualizing every switch, false promise of successful cognitive recovery. **Experiment:** randomized introduction of optional resumption capsules with latency-to-resume, errors, completed work and correction effort; compare no interruption intervention and simple deferral.

### M03. Distributed cognition + secretarial work + implicit coordination -> Situational Coordination Graph

**Sources:** Hollan, Hutchins and Kirsh (2000) [S02; E2], Erickson et al. (2008) [S01; E2 ethnography], Rico et al. (2008) [S03; E2 theoretical].

**Papers:** Work and memory are distributed across people, artifacts and time. Skilled assistants coordinate, anticipate and maintain common situational knowledge; team coordination theory models shared situation awareness and implicit coordination.

**Derived mechanism:** Model *who expects what from whom*, not just what the user intends to do. Store `actor, counterpart, requested_outcome, evidence, deadline, expected_reply, external_state, authority`. Monitor non-events only if a reply was expected **and** the source has sufficiently fresh coverage. Prepare appropriate handoffs or follow-ups rather than automatically sending them. Existence of a sent message is not evidence that someone agreed.

**Risk:** silently assuming others' mental states or consent; communication providers give partial observability. **Experiment:** precision of predicted coordination gaps, correctly detected waiting states, unnecessary follow-ups, actual external acknowledgments.

### M04. Goal systems + goal shielding + adaptive disengagement -> Personal Goal Portfolio Controller

**Sources:** Kruglanski et al. (2002) [S11; E2], Shah et al. (2002) [S12; E1], Wrosch et al. (2003) [S13; E1 associations], Gollwitzer and Sheeran (2006) [S14; meta-analysis E1].

**Papers:** Goals form networks of alternatives, competing pursuits and multiple means; goal shielding can protect salient pursuits; disengagement and reengagement can be adaptive when goals become unattainable; if-then plans improve goal enactment in studied domains.

**Derived mechanism:** Represent a user-chosen goal as `desired_outcome + alternative_ways + boundaries + indicators + revision_policy`. Distinguish *ends* from *means*: learning robotics could be advanced through study, projects, mentoring or reading. A single failed routine does not imply failure of the goal. Shield explicit protected goals from routine administrative encroachment, while permitting renegotiation on genuinely urgent occasions. Model `pause | revise_means | continue | retire_with_consent` instead of endless streaks.

**Risk:** treating an inferred value as a normative goal; overprotecting a goal against changing needs. **Test:** continuity of self-chosen goals, preservation of consented constraints, perceived autonomy, goal progress after disruptions versus rigid routine planner.

### M05. Planning-fallacy research + stochastic scheduling + queueing -> Capacity and WIP Governor

**Sources:** Ahmetoglu et al. (2024) [S15; E1], Herroelen and Leus (2004) [S17; E3], Lambrechts et al. (2008) [S18; E3], Little (2011) [S16; E2 mathematical], and Routin's prior time-budget synthesis.

**Papers:** Human duration estimates can be biased; deterministic baseline schedules frequently fail under uncertainty; stable schedule methods protect coordination by absorbing disruptions. Little's Law relates average work in progress, throughput and flow time *under relevant queueing assumptions*.

**Derived mechanism:** Estimate conditional task-duration distributions from calibrated history (with shrinkage to population priors), not one fixed duration. Incorporate transition costs, hard constraints, protected time, source uncertainty and buffers. Limit simultaneous *active* work only where the measured process supports a WIP-based policy; never apply Little's Law mechanically to heterogeneous personal goals or assume reducing WIP always increases productivity. Use rolling-horizon feasible scheduling and penalize movement of previously accepted commitments.

**Inputs:** duration samples, task class, precedence graph, time slots, deadlines, authority and protected intervals. **Output:** baseline plan, robustness distribution and safe alternatives. **Test:** feasible-plan rate, overdue critical commitments, percent of prior schedule displaced, capacity calibration, completion time and user satisfaction against deterministic planners.

### M06. Rational metareasoning + progressive escalation -> Computation and Question Budget

**Sources:** Horvitz (1987) [S19; E2], Chajewska et al. (2000) [S09; E3], Boutilier (2002) [S08; E2/E3].

**Papers:** Additional computation and additional user information both incur costs; more reasoning is rational only if the expected improvement to a decision offsets cost and latency.

**Derived mechanism:** Route trivial tasks to deterministic rules, non-urgent ambiguous tasks to delayed deeper computation, and high-impact uncertain tasks to bounded deliberation plus explicit confirmation. Define `EV_computation` and `EV_question` separately. Do not use a powerful multi-agent pipeline for a low-risk calendar lookup. Require cost ceilings and deadlines for deliberation; stop when marginal expected benefit falls below marginal cost or a time constraint is reached.

**Risk:** estimates of computation value are themselves expensive and uncalibrated. **Test:** latency, inference costs, failure severity and user corrections versus always-large-model and always-fast-model baselines.

### M07. Conservative online learning + selection-bias research -> Auditable Personalization Policy

**Sources:** Kazerouni et al. (2017) [S20; E3], Schnabel et al. (2016) [S21; E3/E1], Kapoor and Horvitz (2008) [S10; E1].

**Papers:** Conservative bandits formalize learning relative to a baseline under assumptions; recommendation feedback is biased because users can respond only to options they saw, and exposure is policy-dependent. Experience sampling can trade query value against user interruption.

**Derived mechanism:** For every suggested action record `context, candidates, filtering_reason, shown_actions, selection_probability, policy_version, stated_user_feedback, later_outcome`. Avoid treating clicks, silence, or dismissals as unambiguous preferences. Use staged rollout: static baseline -> shadow policy -> randomized low-risk comparisons where consented -> calibrated personalized policy. Never explore external side-effect permissions; those require explicit grants. Use propensity correction only where overlap and defensible exposure probabilities exist.

**Risk:** no counterfactual outcomes for hidden candidates; highly unbalanced propensities yield high-variance estimates; individual variation creates sparse data. **Test:** off-policy estimate calibration, critical miss regression, regret in simulated data, live randomized low-risk intervention comparisons.

### M08. Evolving memory benchmarks + temporal representation -> Belief Maintenance, not 'Chat Memory'

**Sources:** HorizonBench (2026) [S22; E5], Memora (ACL 2026) [S23; E3], Hollan et al. (2000) [S02; E2].

**Papers:** Memory benchmarks reveal serious errors when old preferences remain retrievable after being superseded; six-month simulated histories expose limitations of flat long-context recall. Distributed cognition indicates that useful memory resides in interactions and artifacts, not only a user's verbal profile.

**Derived mechanism:** Keep raw evidence, immutable-by-default event traces subject to deletion rules, current working state, episodic experience, semantic scoped beliefs, relational knowledge, procedural verified skills and uncertainty calibration. Each claim has valid time, observed time, source evidence, explicit/implicit origin, confidence and `supersedes` links. At retrieval, filter by context and valid time *before* semantic similarity. A memory write is a state transition with contradiction checks, not appending a sentence to a memory block. Never let an implicit habit silently override a current explicit constraint.

**Risk:** mistaken entity resolution, contradictory integrations, historical memory inaccessible due to revocation/deletion. **Test:** temporal preference queries, invalidation accuracy, abstention, old-evidence leakage, entity resolution error, replay determinism.

### M09. Autonomous convenience + skill preservation -> Competency-Preserving Delegation

**Sources:** Noessel (2026) [S24; exploratory E5], Wrosch et al. (2003) [S13; E1], Gollwitzer and Sheeran (2006) [S14; E1], self-determination literature [S25; E1].

**Papers:** Delegating cognitive work can lead to deskilling or overreliance; a small navigation intervention suggests ways to preserve independent judgment. Sustainable goal pursuit requires agency and potential for revision, not just tracking activity counts.

**Derived mechanism:** Partition work into `administrative overhead`, `expert judgment`, `practice/learning`, `high-stakes human decision`. Default to automation of low-risk overhead. For user-declared growth/skill targets, let the user choose deliberate practice; provide feedback only after the user's attempt if they opt in. Do not impose mandatory educational friction on unrelated administrative work. Include `ability_preservation` as a long-term evaluation guardrail, not a secret reward.

**Risk:** exploratory study is small, skill-protection prompts may undermine the busy-person value proposition. **Test:** longitudinal retention of chosen skills, effort saved, autonomy and task outcomes versus full-assistance group.

### M10. Goal-lapse research + adaptive self-regulation -> Exception-Aware Routine Learning

**Sources:** Wrosch et al. (2003) [S13; E1], Epstein et al. (2015) [S26; E2], Gilbert (2015) [S04; E1].

**Papers:** Lapses and changes in tracking are normal; goal reengagement may be adaptive; reminders are selectively useful. These do not show that AI can infer what a user truly wants without asking.

**Derived mechanism:** Model routine as a conditional policy with `trigger, time_window, goal_relation, context, suspension_conditions, preferred_recovery_options`. Distinguish one-time exception, repeated schedule conflict, seasonal shift, and actual goal change using changepoint hypotheses. `Missed` must never automatically mean `disliked`; if effect on future decisions matters, ask a short contextual question. Track progress against meaningful evidence, not streaks.

**Test:** false preference changes, resilience to disrupted weeks, goal continuation rates and perceived burden.

### M11. Saga transactions + agent planning validation + official execution semantics -> Verified Responsibility Closure

**Sources:** Garcia-Molina and Salem (1987) [S27; E2/E4], Chang and Geng (2025) [S28; E3], Temporal documentation [S29; E4].

**Papers/docs:** Sagas enable recovery for long-lived multi-step transactions using compensating actions; SagaLLM applies validation, memory and compensation to agent planning and reports stronger constraint consistency in its benchmark. Temporal explicitly warns that an Activity can execute multiple times on retry even if the workflow records only one completion.

**Derived mechanism:** Separate reasoning from execution. Every external effect has typed preconditions, authorization check, business idempotency key, expected postconditions, read-after-write verification, timeout and compensation or recovery procedure. `Provider accepted` is not `recipient agreed`; `calendar update requested` is not `verified on provider`. A reply expectation remains `waiting_external` until acknowledged, canceled or expired. On uncertain execution, reconcile before retrying. Compensation can be impossible for sent messages, so require an explicit pre-send gate.

**Test:** duplicate-send rate, false completion, partial transaction recovery, unknown-outcome time-to-resolution, authorization regression.

### M12. Bounded attention + long-term goals + secretary practice -> Focus Allocation with Critical-Omission Constraints

**Sources:** Erickson et al. (2008) [S01; E2], Shah et al. (2002) [S12; E1], Leroy and Glomb (2018) [S05; E1], Boutilier (2002) [S08; E2/E3].

**Derived mechanism:** Jointly choose `which responsibility`, `when to intervene`, `how much information`, and `who acts`. Never equate priority with interruptibility or user preference with authorization. Use a constrained decision objective, not a pure ranking. Preserve focus where possible, yet override it for high-consequence exceptions; use expected value of information for questions and a source-of-truth view for audit. Long-term goals can be protected via explicit reserved capacity rather than secretly weighting 'growth' as a universal value.

**Key hypothesis:** joint attention and capacity decisions can reduce manual coordination without increasing missed high-priority commitments. **Test:** ablate task-only priority, dynamic timing, capacity model, memory revision, and authority policies.

## 2. Proposed integrated policy

At event or scheduled decision epoch `t`, define belief state:

`b_t = {responsibilities, pending_relations, capacities, user_goals, scoped_preferences, observation_freshness, uncertainty, authority, policy_history}`.

For each candidate intervention `a` in `A = {watch, record, calculate_more, prepare, schedule_internal, ask, batch, surface, interrupt, execute_granted, request_approval}` construct a constraint-satisfying alternative using the currently valid evidence.

**Hard constraints first:** valid consent; action authority; source provenance/freshness for risky inferences; no forbidden external effect; protected user constraints where applicable; idempotency; deadline guardrails; no unverified completion.

Among admissible actions minimize expected, calibrated *loss*:

`L = w1*critical_failure + w2*delay + w3*unnecessary_interruption + w4*manual_effort + w5*goal_displacement + w6*plan_churn + w7*execution_error + w8*resource_cost`.

This is a proposed engineering objective. The weights are not learned truths and should not be chosen arbitrarily; measure separate outcomes first, elicit values only when decisions depend on them, and use Pareto/constraint-based planning when trade-offs cannot be collapsed responsibly.

**Value of asking:** `E[L|no_question] - E[L|answer_policy] - question_cost`. **Value of computation:** `E[L|current_decision] - E[L|refined_decision] - compute_cost`. The cost of delay/irreversibility is included in both. Estimates may be unreliable at cold start; fall back to conservative thresholds and user rules.

**Scheduling:** rolling-horizon CP-SAT for interval and precedence feasibility, followed by scenario evaluation under uncertain durations. Protect explicitly chosen goals and penalize unnecessary changes. Re-optimize only after material change. Chance constraints require calibrated uncertainty models; otherwise report feasibility limits rather than guaranteeing completion.

**Exposure:** minimal attention action is an output of the backend decision policy, not a text summarization layer. Give the reason, the user decision required, an appropriate proof route, and any authorization request; stable presentation should not hide critical errors.

## 3. Minimal contracts and event flow

### Source observation
`Observation {id, provider, source_uri, revision, event_time, received_time, sync_watermark, permission_scope, subject_ids, raw_payload_ref, deletion_marker}`

### Interpreted claim
`Claim {id, proposition_type, actor, object, modality, evidence_ids, alternatives, confidence, valid_interval, inferred_at, superseded_by}`

### Responsibility
`Responsibility {id, goal_links, owner, counterparty, outcome_spec, dependencies, deadline_interval, state, actionability, failure_cost_class, verification_requirements}`

### Personal belief
`Belief {id, domain, proposition, source_class: explicit|confirmed|inferred|observed, scope, valid_interval, system_interval, evidence_ids, confidence, contradictions, supersession}`

### Decision record
`Decision {id, epoch, belief_version, considered_action_classes, constraints, selected_action, rejected_action_reasons, policy_version, learning_exposure_probability_if_applicable, expected_consequences, uncertainty, authorization_ref}`

### Execution receipt
`Execution {id, responsibility_id, intended_effect, precondition_snapshot, idempotency_key, provider_request_id, attempts, provider_response, observed_postcondition, verified_at, state, compensator}`

### Feedback
`Feedback {id, decision_id, explicit_correction, observed_behavior, later_outcome, learning_eligibility, evidence_quality}`

**Pipeline:** webhook/poll -> normalized observation -> extract hypotheses -> validate evidence and source state -> update responsibility and belief versions -> check outstanding timers/waiting dependencies -> time-budget feasibility -> intervention choice -> permission check -> prepare/execute/verify -> outcome event -> memory update candidate -> approved policy/model revision.

**Key non-event rule:** `No reply` can be inferred only when a reply was expected, coverage is sufficiently recent, and no matching acknowledgment is found. Missing webhook does not imply missing user action.

## 4. Worked synthetic scenario: cross-paper routing

**Scenario (invented to illustrate system behavior):** A proposal is due Friday. The user has a protected robotics-learning block, two inflexible meetings, and has previously indicated a dislike of late meetings. A new incoming request asks for a discussion at a conflicting time.

1. **Observation (S01/S02):** parse the request as a *proposal*, not a confirmed meeting. Reconcile people, thread and calendar with valid evidence.
2. **Belief maintenance (S22/S23):** consult the currently valid, scoped evening constraint. If older calendar history disagrees, preserve the observed pattern but do not overwrite the explicitly stated preference.
3. **Capacity forecast (S15/S17/S18):** estimate whether remaining feasible time with buffers permits proposal completion. Do not treat an empty 45-minute slot as guaranteed 45 minutes of usable work.
4. **Goal structure (S11/S12/S13):** the learning block is one means to a chosen goal; consider other feasible ways and times without silently deprioritizing the goal.
5. **Interruption decision (S05/S06):** if the user is in a long focus session and the proposal has not reached its last safe response time, prepare silently and wait for a breakpoint.
6. **Question value (S08/S09/S10):** if multiple available outcomes differ materially based on unknown meeting flexibility, ask one decision-relevant question. Otherwise produce a recommended alternative without a question.
7. **Authority (S20/S27/S28):** draft a reply; do not send unless a current grant or explicit approval permits the exact side effect.
8. **Verified follow-up (S28/S29):** if an approved reply is sent, record a provider-side send receipt but leave the meeting negotiation in `awaiting_external` until confirmation.
9. **Learning (S21/S22/S23):** record which options were visible and the explicit correction, not an assumed implicit preference from a single dismissal.
10. **Long-term improvement (S24/S26):** if the user chooses a new study slot, update a provisional routine hypothesis; do not apply punitive streak logic or take over the learning itself.

## 5. Evaluation program / ablations

**Experimental baseline ladder:** B0 chronological task list; B1 deterministic deadline/importance ranking; B2 LLM-only recommendations without typed state; B3 versioned belief and responsibility state; B4 + forecast/stability; B5 + attention/value-of-information; B6 + verified workflows and gradual learning.

**High-priority metrics:**

- `critical_omission_rate`: proportion of confirmed consequential responsibilities for which the intervention was too late or missing.
- `net_admin_minutes_saved`: baseline administrative minutes minus Routin-administered oversight/correction minutes; measure actual behavior, not self-reported automation counts alone.
- `unnecessary_interruptions_per_week`: events users consistently classify as interruptive without outcome value.
- `schedule_stability`: weighted start-time displacement for accepted commitments after changes.
- `temporal_preference_accuracy`: correct use of currently valid preferences, including superseded and contextual preferences.
- `external_outcome_verification`: rate of actions with evidence for specified postconditions, and separate false-completion rate.
- `protected_goal_retention`: adherence to user-agreed boundaries and meaningful long-term progress, not number of streaks.
- `query_efficiency`: decisions improved per costly clarification.
- `skill_agency`: autonomy, trust calibration and skill retention in domains explicitly chosen for personal development.
- `cost_per_verified_responsibility`: total provider/API/compute cost divided by externally verified useful resolution.

**Method:** synthetic replay and adversarial simulations for early correctness; controlled within-person decision tests for attention; short-term field pilots for intervention cost and correction; longitudinal tests for preference drift, habit adaptation and user growth. Log model, prompt, source revisions, belief version, decision, output and actual effects. Pre-register primary outcomes and hard failure thresholds before claiming benefits. Never treat benchmark performance alone as evidence of real-world wellbeing improvement.

**Failure-focused test cases:** edited/deleted emails; revoked scopes; missed Gmail/Calendar pushes; timezone ambiguity; reply sent but receipt lost; duplicate side effect on workflow retry; temporary preference reversal; changed goal; conflicts between stated values and observed schedules; candidate reminder ignored because user never saw it; low-confidence extraction of speculative promise; human uncertainty about counterpart intention; forced interruptions after resumed session.

## 6. Implementation ordering and scope discipline

1. **Responsibility reconciliation first:** evidence, source freshness and simple waiting states. Target actual miss/duplicate detection, not impressive chat demos.
2. **Belief versioning and explicit rules:** temporal claims, deletion semantics, contradiction handling, logged decisions. Begin with safe deterministic policy baselines.
3. **Capacity forecasting:** hierarchical task-duration priors, buffers, constrained schedule feasibility and churn penalty; validate calibration.
4. **Attention policy and value of asking:** rules -> estimated costs -> offline ablations -> narrow live low-risk tests; protect critical cases with deterministic fallbacks.
5. **Verified action execution:** durable workflows, grant checks, idempotent external effects where provider permits, read-after-write, recovery and negative acknowledgments.
6. **Continual learning:** staged evidence promotion, policy versioning, explicit correction preference, unbiased evaluation where logged exploration is justified. Avoid premature end-to-end RL or dynamic multi-agent swarms.
7. **Skill-preserving growth:** optional practice support on user-declared goals and longitudinal outcomes, no automatic optimization of human lives toward opaque weights.

**Architecture recommendation:** modular monolith with PostgreSQL as source of truth (versioned claims, evidence, permissions and audit trail); bounded event-driven adapters; durable workflows (e.g., Temporal) for externally effectful operations; a constraint solver only for scheduling problems that warrant it; LLMs for candidate extraction and dialog, with non-LLM validation and authority gates. A graph database, vector search, multi-agent orchestration, policy-gradient RL, and bespoke foundation model are conditional optimizations, not day-one requirements.

## 7. Claims we do NOT make

- We do not claim the cited psychological experiments tested Routin or demonstrated productivity improvements for this product.
- We do not claim constant reminders are proven harmful or that context-aware cues are always better; optimize against measured counterexamples.
- We do not assert that Little's Law alone proves a WIP policy for heterogeneous, nonstationary personal work.
- We do not say conservative bandits guarantee safe autonomous external actions; they only establish mathematical properties in the studied model.
- We do not assume more autonomy equals more personal growth: efficiency and human competence can conflict.
- We do not assume a task is completed merely because a provider confirmed a request or message was sent.
- We do not claim there is an unexplored standalone novelty in personalized memory, progressive disclosure, goal management or attention-aware scheduling.
- We do not infer behavior change, preferences or intent from private data beyond authorized access and carefully scoped evidence.

## 8. Verified reference register

[S01] Erickson, Danis, Kellogg & Helander (2008). *Assistance: The Work Practices of Human Administrative Assistants and their Implications for IT and Organizations*. ACM CSCW. [IBM](https://research.ibm.com/publications/assistance-the-work-practices-of-human-administrative-assistants-and-their-implications-for-it-and-organizations).

[S02] Hollan, Hutchins & Kirsh (2000). *Distributed Cognition: Toward a New Foundation for HCI Research*. ACM TOCHI. [University of California record](https://escholarship.org/uc/item/8sb9s5rm). doi:10.1145/353485.353487.

[S03] Rico, Sanchez-Manzanares, Gil & Gibson (2008). *Team Implicit Coordination Processes: A Team Knowledge-Based Approach*. Academy of Management Review. [Publisher](https://doi.org/10.5465/AMR.2008.27751276).

[S04] Gilbert (2015). *Strategic Offloading of Delayed Intentions into the External Environment*. Quarterly Journal of Experimental Psychology. [Publisher](https://doi.org/10.1080/17470218.2014.972963).

[S05] Leroy & Glomb (2018). *Tasks Interrupted: Ready-to-Resume Plans and Attention Residue*. Organization Science. [Publisher](https://doi.org/10.1287/orsc.2017.1184).

[S06] Iqbal & Bailey (2008). *Effects of Intelligent Notification Management on Users and Their Tasks*. ACM CHI. [Scholarly record](https://scispace.com/papers/effects-of-intelligent-notification-management-on-users-and-2zxy8frbl7).

[S07] Czerwinski, Horvitz & Wilhite (2004). *A Diary Study of Task Switching and Interruptions*. ACM CHI. [Scholarly record](https://scispace.com/papers/a-diary-study-of-task-switching-and-interruptions-58tueenh8f).

[S08] Boutilier (2002). *A POMDP Formulation of Preference Elicitation Problems*. AAAI. [AAAI record](https://www.aaaipress.org/Library/AAAI/2002/aaai02-037.php).

[S09] Chajewska, Koller & Parr (2000). *Making Rational Decisions Using Adaptive Utility Elicitation*. AAAI. [Bibliographic record](https://mlanthology.org/aaai/2000/chajewska2000aaai-making/).

[S10] Kapoor & Horvitz (2008). *Experience Sampling for Building Predictive User Models: A Comparative Study*. ACM CHI. [Scholarly record](https://scispace.com/papers/experience-sampling-for-building-predictive-user-models-a-hhn0y3dxk9).

[S11] Kruglanski et al. (2002). *A Theory of Goal Systems*. Advances in Experimental Social Psychology. [Scholarly record](https://scispace.com/papers/a-theory-of-goal-systems-1bs5psp83t).

[S12] Shah, Friedman & Kruglanski (2002). *Forgetting All Else: On the Antecedents and Consequences of Goal Shielding*. Journal of Personality and Social Psychology. [PubMed](https://pubmed.ncbi.nlm.nih.gov/12500810/).

[S13] Wrosch et al. (2003). *Adaptive Self-Regulation of Unattainable Goals*. Personality and Social Psychology Bulletin. [PubMed](https://pubmed.ncbi.nlm.nih.gov/15018681/).

[S14] Gollwitzer & Sheeran (2006). *Implementation Intentions and Goal Achievement: Meta-Analysis*. Advances in Experimental Social Psychology. [Scholarly record](https://scispace.com/papers/implementation-intentions-and-goal-achievement-a-meta-4awoi9wm93).

[S15] Ahmetoglu, Brumby & Cox (2024). *Planning Fallacy Mitigation Strategies in Task Management Apps*. ACM CHIWORK. [Publisher](https://doi.org/10.1145/3663384.3663404).

[S16] Little (2011). *Little's Law as Viewed on Its 50th Anniversary*. Operations Research. [Publisher](https://doi.org/10.1287/opre.1110.0940).

[S17] Herroelen & Leus (2004). *The Construction of Stable Project Baseline Schedules*. European Journal of Operational Research. [Publisher](https://doi.org/10.1016/S0377-2217(03)00130-9).

[S18] Lambrechts, Demeulemeester & Herroelen (2008). *A Tabu Search Procedure for Developing Robust Predictive Project Schedules*. International Journal of Production Economics. [Publisher](https://doi.org/10.1016/j.ijpe.2007.02.003).

[S19] Horvitz (1987). *Reasoning About Beliefs and Actions under Computational Resource Constraints*. UAI. [Author publication](https://www.erichorvitz.com/u87.htm).

[S20] Kazerouni et al. (2017). *Conservative Contextual Linear Bandits*. NeurIPS. [Publisher](https://proceedings.neurips.cc/paper_files/paper/2017/hash/bdc4626aa1d1df8e14d80d345b2a442d-Abstract.html).

[S21] Schnabel et al. (2016). *Recommendations as Treatments: Debiasing Learning and Evaluation*. ICML. [PMLR](https://proceedings.mlr.press/v48/schnabel16.html).

[S22] Li et al. (2026). *HorizonBench: Long-Horizon Personalization with Evolving Preferences*. arXiv preprint. [arXiv](https://arxiv.org/abs/2604.17283).

[S23] Uddin et al. (2026). *From Recall to Forgetting: Benchmarking Long-Term Memory for Personalized Agents*. Findings of ACL. [ACL](https://aclanthology.org/2026.findings-acl.1337/).

[S24] Noessel (2026). *Deskilling and Overreliance: Two Long-Term Risks of AI Assistance*. AI Magazine. Small exploratory navigation evidence. [Wiley](https://doi.org/10.1002/aaai.70096).

[S25] Ntoumanis et al. (2021). *Meta-Analysis of Self-Determination Theory-Informed Intervention Studies in the Health Domain*. Health Psychology Review. [Scholarly record](https://scispace.com/papers/a-meta-analysis-of-self-determination-theory-informed-2z1w4ufe5r).

[S26] Epstein et al. (2015). *A Lived Informatics Model of Personal Informatics*. UbiComp. [Scholarly record](https://scispace.com/papers/a-lived-informatics-model-of-personal-informatics-3wgkrrzyks).

[S27] Garcia-Molina & Salem (1987). *Sagas*. Princeton technical report. [Princeton](https://www.cs.princeton.edu/research/techreps/598).

[S28] Chang & Geng (2025). *SagaLLM: Context Management, Validation, and Transaction Guarantees for Multi-Agent LLM Planning*. PVLDB. [Publisher](https://doi.org/10.14778/3750601.3750611).

[S29] Temporal (2026). *Activity retry and idempotency documentation*. [Official docs](https://docs.temporal.io/activity-definition).

[S30] Google (2026). *Gmail Push API Guide*. [Official docs](https://developers.google.com/workspace/gmail/api/guides/push).

[S31] Google (2026). *Google Calendar Push Notifications*. [Official docs](https://developers.google.com/workspace/calendar/api/guides/push).

[S32] Google OR-Tools (2026). *CP-SAT Scheduling*. [Official code/docs](https://github.com/google/or-tools/blob/stable/ortools/sat/docs/scheduling.md).

## Final research disposition

**Already established fields:** reminders, coordination, goal hierarchy, scheduling robustness, value of information, conservative learning, preference memory, interruption control, and transaction recovery. **Proposed integrated mechanism:** a personal responsibility controller linking them through a common evidence-and-belief state, with constrained attention allocation, resilient time planning, skill-preserving delegation and verified execution. **Not established:** product effectiveness, improvement in real-world productivity, novelty of the integrated policy, or sufficient signal for fully autonomous preference learning. Those require staged deployment and longitudinal evaluation.