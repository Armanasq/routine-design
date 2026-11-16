# Routin: Second-Order Cognitive and Coordination Architecture

**Research synthesis | 16 November 2026 | Backend, reasoning, and behavior only. No UI design.**

**Status:** Architecture and hypotheses grounded in selected primary literature. Not a systematic review, independently verified novelty claim, or demonstrated real-world improvement.

## Executive thesis

The earlier approach was too additive: paper A suggested reminders, paper B suggested robust scheduling, and paper C suggested hierarchical memory. A working personal secretary needs something different: a causal account of how a decision made today changes the user's commitments, capacity, observations, preferences, social obligations, ability to work, and future available decisions. Those changes feed back into the system. Optimization without this feedback model produces a more sophisticated way to overload the person.

Routin should be a **bounded-rational, preference-sensitive, verifiable personal coordination controller**. Its function is to improve meaningful progress, reliability, and personal agency while reducing the administrative work needed to achieve those ends. It should not optimize visible productivity, maximize calendar occupancy, or learn user values from behavior alone.

The foundational separation is **descriptive reality, normative intent, operational commitments, and observability**:
- What happened? Evidence and bitemporal observed events.
- What is believed? Uncertain, context-scoped interpretations, including contradictions.
- What is owed or expected? Social/operational responsibilities, status, dependencies and evidence.
- What does the person want? Explicit goals, constraints, metapreferences and longer-term aspirations, not merely historical behavior.
- What is permitted? Independent, explicit, externally enforced authority grants.
- What can be observed? Provider-specific coverage and freshness; absence of an event is only meaningful when coverage is sufficient.

## 1. Why a simple paper-to-feature mapping was inadequate

The important cross-domain objects are feedback loops and **interaction effects**. Examples:

1. **Scheduling changes demand, not only supply.** Accepting a meeting creates preparation work, follow-up obligations, future interruptions, and social expectations. It is therefore a commitment-admission decision before it is a calendar-placement decision.
2. **The assistant changes its training distribution.** The things it reveals shape what the user touches; those interactions become the very feedback from which it learns. A prioritizer that initially hides growth tasks may manufacture evidence that growth tasks are unimportant.
3. **Preferences are jointly constructed.** Existing preferences, actual constrained choices, explicit values, and ambitions can conflict. Present choices may reflect pressures, not desired future behavior.
4. **Attention has a recovery cost.** A decision to interrupt can cause residue, require a return cue and trigger schedule churn. A single notification score does not capture its downstream effects.
5. **Reliability and convenience can conflict.** Fewer checks reduce friction but can hide unverified work. More approvals improve certain safety properties but can create approval fatigue and shadow administrative work.
6. **Efficiency can induce more demand.** Time saved from email can be reinvested into new commitments without improving wellbeing, competence, or meaningful goal progress. The controller must distinguish freed capacity from capacity that should be reallocated.

Each relation is a proposal about Routin, based on work in prospective memory, organizational coordination, decision theory, queueing, self-regulation, recommender feedback loops and reliable distributed systems. No single cited study tests their integration into Routin.

## 2. Deep mechanism A: commitment admission before scheduling

### Sources and inference

Erickson et al. (CSCW 2008) study assistants as coordinators of people, events and preparation; they do not merely manage time slots [1]. Hollan, Hutchins and Kirsh (TOCHI 2000) model cognition as distributed across people, artifacts and environments [2]. Star and Strauss (CSCW 1999) caution that substantial coordination work may be invisible to standard task measures [3]. Kingman's heavy-traffic queue research shows that delays can become large near capacity under assumptions about queue structure [4]; Lambrechts et al. show that robust baseline schedules trade some apparent efficiency for stability [5].

### Synthesized deduction

When a new request arrives, its true expected demand may include meeting time, preparation, context-switching, follow-up, uncertain rework, and downstream obligations. The person can respond by accepting, renegotiating time, declining, reducing scope, delegating, requesting missing inputs, or deferring. A scheduler that only selects an empty slot treats demand as fixed. A secretary can **shape demand** and negotiate it. This is not established as an outcome improvement by the cited papers; it is a testable mechanism composition.

### Backend mechanism: Commitment Admission Controller

For candidate commitment `k`, estimate:

`IncrementalDemand(k) = primary_duration + preparation + communication + expected_rework + context_transition + contingencies`.

Generate alternatives `accept`, `propose_time`, `propose_scope`, `delegate`, `request_input`, `decline`, `hold_tentative`. Use a calibrated duration distribution by task class and user history. Project each alternative into a rolling-horizon plan while preserving explicit hard constraints and risk budgets for existing obligations. Compute the **marginal impact** on existing critical commitments, protected goals and schedule stability. Reject actions requiring authority that has not been granted. A social meeting request is a proposal until acceptance; preparing a response does not itself accept it.

The objective is not maximizing acceptance. It is selecting a feasible and socially appropriate response that respects what the user chose to protect. If all reasonable alternatives are infeasible, surface the conflict explicitly rather than manufacturing an impossible schedule.

### Failure/assumption

A queueing theorem for stationary, homogeneous service processes is **not** proof of a particular utilization threshold for a heterogeneous human life. Do not prescribe an 80% target without data. Calendar duration and actual cognitive/coordination cost differ; estimates must be calibrated. Relationship norms cannot be inferred with certainty from sparse communications.

### Test

Compare scheduling-only and admission-aware policies over evolving requests: overload probability, missed existing deadlines, unnecessary commitment acceptance, acceptance quality judged by users, coordination friction, and adverse effects on protected time.

## 3. Deep mechanism B: learning what the user *wants to want*

### Sources and inference

Preference-construction research emphasizes that preferences can emerge during decision processes rather than exist as fixed constants [6]. Studies of recommender feedback loops discuss how prior recommendations can pollute subsequent preference observations [7]. Schnabel et al. (ICML 2016) formalize exposure/selection bias in recommender-system evaluation [8]. Su et al. (CHI 2026, 33 interviews) show that effective feedback depends on justifiability, timing, and clarity about how corrections will be used [9]. HorizonBench (2026) and Memora (ACL Findings 2026) document failure modes in maintaining changing personal preferences [10,11].

### Synthesized deduction

A user who works late may hate late work; a user who skips a study session may still care deeply about the goal; a user who opens work notifications may be responding to demands, not demonstrating a preference for more work. Observed selections are **behavior under constraints and prior system exposure**, not clean utility labels.

Routin must distinguish four representations:

- **Observed regularity:** User often attends late meetings.
- **Reported preference:** User says late meetings are undesirable.
- **Commitment/constraint:** User explicitly protects evenings except for defined emergencies.
- **Metapreference or aspiration:** User wants to become someone who studies robotics and preserves evenings for family.

A later event may invalidate a temporal rule, override it for a single week, or reflect constrained behavior rather than a changed value. The assistant should record competing interpretations instead of overwriting a canonical profile.

### Backend mechanism: Reflective Preference Model

Represent each belief with `{content, source_class, context, valid_interval, recorded_interval, scope, confidence, explicit_status, contradiction_links, evidence_refs, hypothesis_version}`. Treat explicit current preferences and user-authored boundaries as controlling unless specifically revoked. Store observed behavior separately. Detect distribution change but **do not promote a trend into a new norm** without a relevant explicit correction or an allowed low-risk application.

Ask a focused question only when competing hypotheses change a consequential decision. Record the question's decision context, alternatives, exposure mechanism, received correction and subsequent outcome. Use decision-contingent value-of-information estimates, not periodic preference surveys. When the user disagrees with Routin, update only the relevant scoped hypothesis; do not over-generalize.

### Non-obvious architecture requirement: exposure ledger

A learner cannot correctly infer the importance of growth activities from clicks if the policy almost never presents them. Every attention decision should record candidate set, actual exposure, sampling policy/probability if randomized, context, belief version and outcome. Off-policy estimators are valid only under causal identification/overlap assumptions; no magical debiasing of completely unseen counterfactuals.

### Test

Longitudinal histories with explicit value conflicts, enforced work pressures, temporary overrides, and true goal changes. Measure preference version accuracy, false promotion of observations, obsolete-belief use, and policy-induced feedback distortion. Compare flat memories, bitemporal memory, and reflective preference model on identical tasks.

## 4. Deep mechanism C: attention as an intervention, not presentation

### Sources and inference

Sellen et al. (Memory 1997) studied prospective intentions in workplaces; context/place cues were important, and remembering was not simply proportional to thinking about an intention [12]. Gilbert (2015) experimentally studies externalized delayed intentions [13]. Leroy and Glomb (Organization Science 2018) tested ready-to-resume planning for interruptions [14]. Horvitz (mixed initiative 1999) frames automated intervention in terms of uncertainty and utility [15]. Kapoor and Horvitz (CHI 2008) compare active feedback-query policies while charging for the interruptions they create [16].

### Synthesized deduction

A notice can help complete one responsibility while disrupting another. Therefore, "show now" is an action with a **counterfactual opportunity cost**, not simply a UI rendering decision. For each candidate problem, the agent should separately determine `importance`, `latest_safe_intervention`, `actionability`, `interruptibility`, and `recoverability`.

Routin should schedule or withhold interventions by their expected outcomes. A contextual cue can be better than a clock reminder; sometimes the correct action is a silent preparation. A critical obligation should not disappear because a classifier predicts that the user is busy.

### Backend mechanism: Intervention and Resumption Policy

- Represent delayed obligations with `trigger_conditions`, `failure_severity`, `last_safe_intervention`, `status_evidence` and `contingency_paths`.
- When an intervention can wait, estimate disruption cost across near-future breakpoints; consider background preparation before surfacing.
- When switching is justified, preserve a *resumption capsule*: what the user was doing, last verified state, unresolved decision, source artifact and next concrete step.
- Avoid compulsory resumption rituals; only prepare or show a capsule when useful. Reopening an item should restore context, not replay the entire conversation.
- Allow escalation when late intervention creates substantially greater expected harm; critical omissions are hard guardrails.

This creates a new causal link between attention and scheduling: interruptions change task-duration distributions and future feasibility. The scheduling system must price these effects.

### Test

Randomized low-risk comparison of static notifications, breakpoint delivery, and interruption-plus-resumption policies. Primary measures: missed consequential events, task resumption lag, work quality, unnecessary interruptions, and administrative corrections. Verify across devices, roles and cultural contexts.

## 5. Deep mechanism D: protect goals without turning the AI into a manager of the user's life

### Sources and inference

Shah et al. (JPSP 2002) experimentally study shielding focal goals from competing activation [17]. Wrosch et al. (2003) find associations among adaptive disengagement, reengagement and wellbeing [18]. Gollwitzer and Sheeran (2006) synthesize 94 implementation-intention tests [19]. Epstein et al. (UbiComp 2015) model normal lapsing and resuming in personal tracking [20]. Noessel (AI Magazine 2026) emphasizes deskilling and overreliance as risks of assistance [21].

### Synthesized deduction

The secretary's duty is not to keep the person maximally busy or enforce every old goal indefinitely. The user must be able to change the goal, change the method, or abandon it. Some assistance should *remove drudgery* while other assistance should preserve the user's opportunity to practice. Thus "do it for me" and "help me learn to do it" are different **delegation intents**.

### Backend mechanism: Goal Ecology / Delegation Intent

Model goals as user-authored `ends`, with multiple optional `means`, priority boundaries, tradeoff policies, context windows, review triggers and status (`active, suspended, revised, retired`). Protect an explicitly chosen time budget where possible, but offer alternatives on material conflict. Do not punish missed routines or blindly keep streaks. Ask for re-consent after large changes rather than silently optimizing against obsolete objectives.

For each responsibility, store `delegation_mode`: `full_service`, `collaborative`, `deliberate_practice`, `human_decision`. Administrative logistics default toward full service within authority; activities selected for learning should preserve meaningful practice if the user wants that. The agent should not inject forced teaching into routine administration.

### Test

Evaluate goal continuity after disruptions, self-rated autonomy, consent-boundary compliance, meaningful milestone evidence, recovery from lapses, and retained ability in deliberately practiced skills, not just task-completion counts.

## 6. Deep mechanism E: care about the work that is not in a calendar

### Sources and inference

Distributed cognition [2], secretarial ethnography [1] and invisible-work literature [3] establish that work extends beyond visible artifacts. Social exchanges contain proposals, obligations, courtesy, negotiated expectations, counterparty constraints, and unobserved events. Work-as-done resilience research emphasizes differences between prescribed plans and actual adaptations in complex sociotechnical systems [22].

### Synthesized deduction

An operational model must distinguish **an expected event that did not occur** from **an event the system failed to observe**. These cases require different responses. A missing reply might be meaningful, but a disconnected email source is not evidence that nobody replied. Likewise, a confirmed outgoing email means a message was sent, not that a counterpart agreed.

### Backend mechanism: Expectation and Coverage Ledger

For pending expectation `e`, maintain `{counterparty, expected_outcome, earliest_expected, latest_expected, evidence, coverage_window, source_freshness, escalation_norm, relation_sensitivity}`. Only assert a verified non-event after a successfully covered observation window. For outdated sync watermarks issue a reconciliation job rather than a follow-up. After approved outreach, distinguish `submitted`, `provider_acknowledged`, `awaiting_counterparty`, `counterparty_confirmed`, `fulfilled`.

Measure false missing-reply alerts and unnecessary social pressure from follow-ups. Communication actions must be appropriate to the relationship; no automated guilt, pressure, or manipulation.

## 7. Deep mechanism F: optimize for human welfare, not for proxy productivity

### Sources and inference

Goodhart/Campbell analyses show that intensive optimization of imperfect proxies can produce perverse outcomes [23,24]. The NBER field experiment across 66 firms and 7,137 knowledge workers observed specific time savings from AI email/meeting/writing integration, without detecting accompanying changes in overall task composition from individual-level access [25]. It does not prove that all AI agents lack productivity benefits; it warns against conflating an activity-level saving with a life-level improvement.

### Synthesized deduction

A productivity assistant can create a treadmill: faster email -> more accepted obligations -> higher utilization -> more interruptions -> less goal time -> more AI-driven acceleration. A conventional algorithm that minimizes idle time could produce worse human outcomes. Explicitly define **capacity released** as an opportunity for the user, not a vacuum to fill.

### Backend mechanism: Welfare and Capacity Guardrails

Measure a balanced vector rather than one reward: `unmet consequential responsibilities`, `admin minutes incl. oversight`, `deadline robustness`, `protected goal continuity`, `unplanned work growth`, `communication quality`, `user control`, `error burden`. Do not optimize generic wellbeing via surveillance. Protected personal time and explicit boundaries should act as user-configurable hard constraints when applicable. Measure whether recovered time actually remains available to the user.

Use Pareto analysis and minimum acceptable outcomes rather than one scalar 'productivity score'. Test for shifts in demand, not just completed-item velocity.

## 8. Deep mechanism G: trust-aware execution is part of cognition

### Sources and inference

Memora [11] and HorizonBench [10] demonstrate memory revision failures in simulated long interactions; PAUSE (2026) tests persistent state, tools and permissions in integrated environments [26]. The Saga transaction pattern and agentic workflow research motivate explicit compensation and recovery in multi-step execution [27]. A message sent is not a promise fulfilled, and a retry is not harmless when an external action is irreversible.

### Backend mechanism: Executable Decision Certificate

Each effectful candidate action must carry `{decision_id, evidence_ids, belief_version, intent, preconditions, authorization_ref, risk_class, idempotency_key, predicted_effect, verification_plan, recovery_plan, deadline}`. Policy engine, not LLM, checks authority and current preconditions. Execution records `attempted/accepted/verified/unknown/failed`, reconciling remote state after ambiguous failures before retry.

This certificate is the machine-executable bridge from *reasoning* to *accountable action* and prevents an adaptive preference model from silently expanding permissions. Do not claim that compensations undo messages recipients already read.

## 9. Deep mechanism H: rational allocation of questions, computation, and attention

The system has three limited resources: the user's attention, available compute, and time before decisions become costly. Chajewska/Koller/Parr (AAAI 2000) derive adaptive utility elicitation [28]; Horvitz's bounded rational reasoning examines time/compute tradeoffs [29]; Kapoor/Horvitz [16] empirically compare user-model probing policies. Their joint implication is to treat an additional model call and an additional user question as alternate ways to reduce uncertainty.

For any proposed question `q`:

`EVQ(q) = E[loss without asking] - E[loss after possible answers and updated action] - user interruption cost - waiting cost`.

For any computation `c`:

`EVC(c) = E[loss under current best action] - E[loss after c] - model/latency cost - time lost waiting`.

These are *modeling definitions*; true expected values require calibration and cannot be known exactly. Use simple safe heuristics at cold start. More important, recognize different uncertainty types:

| Type | Example | Appropriate remedy | Wrong remedy |
|---|---|---|---|
| Source/coverage | Gmail sync is stale | Resync before inferring absence | Ask user if colleague replied |
| Epistemic interpretation | 'Maybe by Friday' ambiguous | Read context or clarify | Treat as firm deadline |
| Preference/value | User may want evenings protected | Ask only when choice depends on answer | Learn from calendar frequency |
| Aleatoric duration | Proposal may take 3-6 hours | Robust schedule scenarios | Extra LLM reasoning alone |
| Execution state | Provider timed out after send | Query remote idempotency/status | Retry blindly |
| Social uncertainty | Counterpart has not agreed | Wait/prepare/follow up within authority | Mark commitment complete |

A single "confidence" score collapses uncertainties that require categorically different responses.

## 10. Coupled dynamics and conflicts across the entire architecture

### Timescale A: event and safety loop (seconds/minutes)

Receive source changes, validate permissions, extract typed hypotheses, reconcile versioned evidence and responsibility state, check last-safe-decision times. These operations should be deterministic where possible and can run without a heavyweight model.

### Timescale B: coordination and capacity loop (hours/days)

Forecast workload and interruption costs, accept or renegotiate new commitments, protect previously chosen blocks, prepare handoffs, choose low-disruption intervention times and verify external results. Changes to obligations alter effective available capacity; availability then affects the acceptance of new obligations.

### Timescale C: reflection and personal growth loop (weeks/months)

Review preference hypotheses, goal progress and intentional changes in life circumstances. Separate drift from a one-off exception. Ask for validation only when the outcome would change materially. Check whether automation is displacing activities the user intended to learn.

### Timescale D: governance and evaluation loop (continuous and periodic)

Audit critical misses, false completions, authority violations, policy-induced preference drift, schedule churn, and unplanned expansion of commitments. Changes to model/policy are staged, replayed, and rolled out cautiously. Do not silently change permission grants through learning.

**Conflict rule:** Permission and explicit constraints gate action first; consequential errors and critical omissions constrain the feasible set; the coordination policy negotiates time and workload; the preference model supplies scoped context but never overrides authorization; the attention layer determines presentation or intervention; the execution layer verifies result. Any unresolved normative value conflict may require the human, not another agent.

## 11. Proposed planning and decision architecture

A full POMDP over human life is neither identifiable nor computationally practical. Use a factored, event-sourced belief state and hierarchical decision policy:

`B_t = (E_t, R_t, X_t, G_t, P_t, C_t, A_t, U_t, H_t)`

- `E`: observations and source coverage; `R`: responsibility/dependency graph; `X`: interpersonal expectation graph;
- `G`: explicit chosen goals and delegation intent; `P`: scoped/temporal beliefs about preferences;
- `C`: resource/time availability and task duration forecasts; `A`: authority grants and external-tool capabilities;
- `U`: type-specific uncertainty estimates; `H`: logged history of policy exposures, decisions and outcomes.

Generate admissible actions (`resync`, `monitor`, `prepare`, `negotiate`, `ask`, `schedule`, `surface`, `interrupt`, `request approval`, `execute allowed`). Apply hard gates before optimizing. Use robust candidate planning for time-dependent problems and bounded value-of-information assessment for expensive questions. Optimize a **constrained multi-objective** outcome rather than globally increasing an opaque score.

Conceptual candidate action selection:

`a* in ParetoOptimal({ feasible(a) and authorized(a) and low_critical_risk(a) })`,

with explicit tie-breaking priorities previously approved by the user, or ask when two options have consequential but genuinely subjective tradeoffs.

For scheduling define `S` as currently accepted commitments, and let `S+a` reflect the entire newly proposed obligation including preparation and expected follow-up. Evaluate changes in deadline risk, protected-time loss, and plan displacement. Choose a stable plan that meets required constraints over duration scenarios; when no feasible plan exists, negotiate scope/dates rather than fabricate feasibility.

For intervention time `t`, compare expected missed/late consequences against interruption and resumption cost, subject to the latest safe intervention time. Delay low-consequence alerts until natural breakpoints; never permit the user state classifier to suppress hard safety triggers.

## 12. Worked integrated scenario: what changes when Routin thinks causally

**Synthetic example; durations and events are illustrative, not field data.**

- On Monday, a research proposal is due Thursday. The user has two fixed meetings, a protected weekly robotics learning session, and a stated preference not to accept evening meetings. Historical calendar data nonetheless shows many evening meetings.
- The proposal requires several hours of uncertain work and a missing figure from a collaborator. A new request invites the user to an evening meeting, and a messaging sync has not been verified since morning.

**Naive calendar chatbot:** sees a gap, schedules the meeting, sends a generic reminder, and moves robotics study into an already crowded night. A later missing-reply alert assumes the collaborator failed to respond, even though the connector is stale. It records 'user works evenings' as a preference after observing similar schedules.

**Routin's proposed reasoning:**

1. Treat the invitation as a *request*, not a commitment. Extract parties and social response obligations, with evidence links.
2. Reconcile sync state before inferring that the collaborator has not replied. If coverage is stale, issue a targeted read/repair job.
3. Keep evening-meeting frequency as an observed constraint pattern. Apply the user's active explicit boundary as the normative rule.
4. Model the proposal as an outcome with several subdependencies, not only one task; estimate time-to-last-useful-action for obtaining the figure.
5. Run a duration-scenario feasibility test with existing appointments, preparation time, buffers and protected learning. Evaluate the marginal cost of accepting the evening meeting, including follow-ups and work displacement.
6. Candidate strategies: request the missing figure, propose a daytime meeting, reduce meeting scope, or defer the request. Prefer a strategy that preserves critical obligations and the user's chosen boundary.
7. If all safe options depend on a subjective relationship tradeoff, ask one short question at an appropriate moment. Otherwise draft the proposed resolution and request approval if authority does not include sending.
8. If an authorized message is sent, record `provider_accepted`; keep the proposal negotiation in `awaiting_external` until the counterpart responds.
9. Before an unavoidable interruption, preserve a minimal resumption capsule so the user's proposal work can be resumed without reconstructing context.
10. After later events, learn only from explicit feedback and verifiable outcomes; do not infer 'evening meetings are preferred' or 'robotics no longer matters' from coerced schedule changes.

**Second-order effect:** An early negotiation avoids a newly accepted commitment; that prevents future work compression; less compression reduces interruption urgency; lower interruption burden creates an opportunity for the original proposal *and* user-chosen growth. This long causal chain is the intended architecture hypothesis. It must be measured, not asserted as a proven effect.

## 13. Data contracts needed for this theory

`Evidence {source_id, version, source_time, ingestion_time, coverage_interval, explicit_scope, subject, provenance, deletion_status}`

`Claim {proposition, modality, actors, alternatives, evidence_ids, belief_confidence, valid_from, valid_to, learned_at, supersession}`

`Responsibility {owner, counterparty, outcome, acceptance_status, dependencies, expected_events, deadline, last_safe_decision, fulfillment_evidence, state}`

`Preference {kind: observed|explicit|inferred|aspirational, domain_scope, context_scope, validity, evidence, confidence, conflict_links, confirmation_status}`

`Goal {desired_outcome, owner_confirmation, alternative_means, protected_constraints, delegation_intent, review_condition, status}`

`CapacityForecast {horizon, fixed_commitments, uncertain_duration_distributions, preparation, buffers, protected_intervals, feasible_scenarios, schedule_stability}`

`AttentionDecision {candidates, belief_version, selected_exposure, alternatives, missed-risk_estimate, intervention_cost, reason, learning_policy, exposure_probability_if_randomized}`

`ExecutionCertificate {preconditions, approval, permission_scope, idempotency_key, intended_postcondition, observed_postcondition, retry_policy, compensation_possible, verification_state}`

`Outcome {user_effort, observed_effect, unknown_status, error_class, agency_feedback, policy_version, source_freshness}`

## 14. Engineering architecture: a hierarchy of decisions, not a swarm

Modular monolith with bounded asynchronous workers is preferable until throughput and operational boundaries justify splitting services. Use relational event/evidence tables and temporal versions as source of truth; graph edges are logical links, not a mandatory graph database. A small task-conditioned LLM parses utterances and messages into typed candidate claims; deterministic validators and state machines reconcile and guard them. A solver handles high-consequence capacity decisions; simple rules handle routine sync and deadlines. External side effects run through durable workflows with provider-specific idempotency, preconditions and read-after-write checks. Speech and text are input modalities sharing one task and memory state; realtime voice must not bypass safe action gates.

Routing policy:

- Routine read-only fact lookup -> fast deterministic or retrieval path.
- Uncertain candidate commitment -> typed extraction + validation and optional clarification.
- Scheduling conflict -> capacity forecast + alternatives + safe policy decision.
- Multi-step external action -> durable workflow + grant + verification.
- Preference drift -> delayed belief revision; no instant global profile rewrite.
- Consequential subjective tradeoff -> one targeted, justifiable human question.
- High-impact uncertainty or source outage -> conservative fallback / resync / human review.

Not recommended initially: fully autonomous RL over user lives, unbounded multiple agent debates, life-utility scoring, automatic generation/execution of tool code, intensive continuous biometric monitoring, forced self-improvement programs, speculative emotion inference.

## 15. Causal evaluation, ablations and negative tests

**Primary outcome is not interaction count.** Define a balanced scorecard and guardrails. The principal estimand is net human administrative burden reduction **among equally good or better responsibility outcomes**, not the number of AI actions or calendar slots filled.

- Missed critical commitments, false inferred obligations, stale-data false alarms.
- Net admin effort: time saved minus review, correction, and coordination effort introduced.
- Commitment admission: new obligations accepted, infeasible workload prevented, unnecessary declines, social costs.
- Schedule realism: calibrated deadline probability, on-time performance, baseline stability, buffer protection.
- Attention intervention: critical omission, interruption burden, work-resumption lag, quality of resumed work.
- Preference learning: explicit-vs-observed separation, temporary-overrides, invalidation, action-induced feedback bias.
- Growth: continuity of voluntarily selected goals, consent and ability preservation, pause/resume flexibility.
- Reliability: provider-side verification, false completion, duplicate irreversible actions and recoverability.
- Value: actual improvement in user-valued outcomes, not proxy completion counts.

**Ablation ladder:**
B0 Manual/calendar-driven workflow; B1 task-only detection/ranking; B2 responsibility reconciliation with source freshness; B3 + admission and robust time budgeting; B4 + attention/resumption; B5 + reflective preference learning; B6 + verified delegation and growth-aware policies. Test each incremental mechanism; remove expensive mechanisms with no reliable incremental benefit.

**Counterfactual issue:** The system's choices influence what feedback is observed. Randomized low-risk exposure and logged propensities may allow off-policy evaluation under assumptions; not all high-consequence actions can or should be randomized. Human field studies with informed consent are required to establish behavioral impact. Synthetic traces validate software invariants but not mental wellbeing or social relationships.

**Critical failure scenarios:** deleted/edited emails; stale sync; two contradictory commitments; proposed vs accepted meeting; sender asks a question rather than requesting action; different timezones; draft sent but receipt missing; temporary family crisis; old preference superseded; high rank from agent-caused exposure; a learning goal intentionally abandoned; preserved focus causing missed obligation; automatic follow-up damaging a relationship; idempotency unsupported by provider.

## 16. Scientific contribution and falsification

### Proposed hypothesis H1: Admission-aware coordination

Coupling prospective commitments, uncertain capacity, and explicit goal protection produces fewer severe overcommitment failures than scheduling-only assistants, without unacceptable social costs or increased correction effort.

### Proposed hypothesis H2: Reflective preference tracking

Separating observations, explicit choices and metapreferences, together with exposure logging and temporal belief revision, improves consequential preference decisions over memory retrieval alone.

### Proposed hypothesis H3: Intervention-aware planning

Jointly accounting for task dependency, last-safe-intervention time and interruption/resumption cost reduces unnecessary interruptions without increasing missed critical responsibilities.

### Proposed hypothesis H4: Verified delegation with capacity preservation

Receipt-aware external workflows and conservative authority policies reduce false completion and admin overhead; any time saved remains available for user-chosen priorities rather than automatically filling with more obligations.

### Falsification conditions

Abandon or redesign a mechanism if it produces no controlled improvement after accounting for noise and user variation, substantially increases critical misses, worsens informed consent, imposes material maintenance costs, or creates self-reinforcing biases that cannot be calibrated. Do not declare novelty merely because the architecture contains several literatures. A defensible research contribution requires a precise algorithm, valid baselines, causal evaluation and independent replication.

## 17. Priority engineering decisions

1. Build **evidence, coverage and responsibility reconciliation** before autonomous writes. Every known non-event must carry a coverage proof.
2. Add **commitment admission** before advanced schedule filling. Model preparation and downstream obligations.
3. Separate **observed vs desired vs aspirational preferences** before learning from integrations.
4. Maintain **event exposure and outcome logs** before using implicit feedback to adapt ranking.
5. Add **robust capacity planning and schedule-stability penalties** before optimizing calendar utilization.
6. Add **intervention/last-safe-decision logic** and optional resumption support with strict critical-miss safeguards.
7. Implement **authority and verified execution certificates** before proactive actions become externally effectful.
8. Test longitudinal impact on goals, skills, and real workload before claiming that more autonomy creates greater benefit.

## 18. Source register: primary and high-quality references

[1] Erickson, Danis, Kellogg & Helander (2008), *Assistance: The Work Practices of Human Administrative Assistants and Their Implications for IT and Organizations*, CSCW. IBM: https://research.ibm.com/publications/assistance-the-work-practices-of-human-administrative-assistants-and-their-implications-for-it-and-organizations

[2] Hollan, Hutchins & Kirsh (2000), *Distributed Cognition: Toward a New Foundation for Human-Computer Interaction Research*, TOCHI. https://escholarship.org/uc/item/8sb9s5rm

[3] Star & Strauss (1999), *Layers of Silence, Arenas of Voice: The Ecology of Visible and Invisible Work*, CSCW. https://doi.org/10.1023/A:1008651105359

[4] Kingman (1962), *On Queues in Heavy Traffic*. https://doi.org/10.1111/j.2517-6161.1962.tb00465.x

[5] Lambrechts, Demeulemeester & Herroelen (2008), *A Tabu Search Procedure for Developing Robust Predictive Project Schedules*. https://doi.org/10.1016/j.ijpe.2007.02.003

[6] *Towards Psychology-Aware Preference Construction in Recommender Systems* (2021/22). https://link.springer.com/article/10.1007/s10844-021-00674-5

[7] *Recommender Systems, Ground Truth, and Preference Pollution*, AI Magazine (2022). https://onlinelibrary.wiley.com/doi/10.1002/aaai.12055

[8] Schnabel et al. (2016), *Recommendations as Treatments*, ICML. https://proceedings.mlr.press/v48/schnabel16.html

[9] Su et al. (2026), *Tell Me Why You're Asking*, CHI. https://doi.org/10.1145/3772318.3790950

[10] Li et al. (2026), *HorizonBench*, arXiv. https://arxiv.org/abs/2604.17283

[11] Uddin et al. (2026), *From Recall to Forgetting*, Findings of ACL. https://aclanthology.org/2026.findings-acl.1337/

[12] Sellen et al. (1997), *What Brings Intentions to Mind?*, Memory. https://pubmed.ncbi.nlm.nih.gov/9282220/

[13] Gilbert (2015), *Strategic Offloading of Delayed Intentions*, Quarterly Journal of Experimental Psychology. https://doi.org/10.1080/17470218.2014.972963

[14] Leroy & Glomb (2018), *Tasks Interrupted*, Organization Science. https://doi.org/10.1287/orsc.2017.1184

[15] Horvitz (1999), *Principles of Mixed-Initiative User Interfaces*, CHI. https://www.microsoft.com/en-us/research/publication/principles-of-mixed-initiative-user-interfaces/

[16] Kapoor & Horvitz (2008), *Experience Sampling for Building Predictive User Models*, CHI. https://www.microsoft.com/en-us/research/publication/experience-sampling-for-building-predictive-user-models-a-comparative-study/

[17] Shah, Friedman & Kruglanski (2002), *Forgetting All Else*, JPSP. https://pubmed.ncbi.nlm.nih.gov/12500810/

[18] Wrosch et al. (2003), *Adaptive Self-Regulation of Unattainable Goals*. https://pubmed.ncbi.nlm.nih.gov/15018681/

[19] Gollwitzer & Sheeran (2006), *Implementation Intentions and Goal Achievement: A Meta-analysis*. https://doi.org/10.1016/S0065-2601(06)38002-1

[20] Epstein et al. (2015), *A Lived Informatics Model of Personal Informatics*. https://pmc.ncbi.nlm.nih.gov/articles/PMC12435389/

[21] Noessel (2026), *Deskilling and Overreliance*, AI Magazine. https://doi.org/10.1002/aaai.70096

[22] *Assessing Resilience in Everyday Work Through Observations* (2024), Safety Science. https://www.sciencedirect.com/science/article/pii/S0925753524000511

[23] *Reliance on Metrics Is a Fundamental Challenge for AI* (2022). https://pmc.ncbi.nlm.nih.gov/articles/PMC9122957/

[24] *Building Less-Flawed Metrics* (2023), perspective. https://pmc.ncbi.nlm.nih.gov/articles/PMC10591122/

[25] Dillon, Jaffe, Immorlica & Stanton (2025), *Shifting Work Patterns with Generative AI*, NBER Working Paper w33795. https://www.nber.org/papers/w33795

[26] Chen et al. (2026), *PAUSE: A User-Centric Benchmark for Personal AI Assistants*. https://arxiv.org/abs/2607.27354

[27] Chang & Geng (2025), *SagaLLM*, PVLDB. https://doi.org/10.14778/3750601.3750611

[28] Chajewska, Koller & Parr (2000), *Making Rational Decisions Using Adaptive Utility Elicitation*, AAAI. https://aaai.org/Papers/AAAI/2000/AAAI00-056.pdf

[29] Horvitz (1987), *Reasoning About Beliefs and Actions Under Computational Resource Constraints*. https://www.erichorvitz.com/u87.htm

[30] Chen et al. (2026), *VitaBench 2.0*. https://vitabench2.github.io/

[31] *Are You Sure This Is What You Really Want? Conversational Recommender Systems for Enhancing Human Autonomy* (2026). https://pubmed.ncbi.nlm.nih.gov/42862501/

## Evidence-access and novelty disclaimer

This synthesis reviewed original available HTML text for selected studies (including CHI 2026 preference feedback, lived informatics, VitaBench project page, Wiley deskilling, and supporting research), plus official publisher abstracts and bibliographic records for others. It does not claim complete full-text appraisal of every listed paper or a systematic exhaustive search. The engineered mechanisms are **deductions and hypotheses**. They are not presented as outcomes proven by the cited studies, and source-context limitations must be accounted for in any experimental deployment.

## 19. Causal loops the architecture must actively regulate

These are proposed system-level loops, **not causal effects measured in Routin**. Source studies establish parts of some links; the complete pathways require testing.

### Loop R1: the recovered-time treadmill (reinforcing, potentially harmful)

`automation -> email/admin time saved -> perceived extra capacity -> accept additional requests -> increased commitments -> future coordination load -> more demand for automation`

The secretary can unintentionally increase dependence by repeatedly reinvesting saved time in further obligations. **Countermeasure:** represent capacity returned to the user as unallocated; do not auto-commit it. Track request admission, protected time and workload growth, not just task throughput. **Falsification:** observe whether admin time falls but total unwanted work rises after the agent's intervention. Based on distributed work, admission-control hypothesis and empirical AI-work time-use research [1,4,5,25].

### Loop R2: preference pollution (reinforcing, harmful)

`work prioritized -> work shown more frequently -> user interacts with shown work -> model infers stronger work preference -> work prioritized even more`

**Countermeasure:** explicit values separate from exposure-biased revealed behavior; preserve candidate/exposure logs and measure unseen class coverage. Distinguish correction from reactive action. Do not claim unbiased estimation without logged propensity and overlap. **Falsification:** after simulated exposure asymmetry, see whether Routin shifts inferred preferences despite unchanged explicit goals. Grounded in [7,8,9].

### Loop R3: schedule thrashing (reinforcing, harmful)

`new event -> total schedule recomputation -> movement of agreed blocks -> changed habits / missed appointments -> more uncertainty -> more recomputation`

**Countermeasure:** stable baseline, change thresholds, localized repair, only update affected subgraphs, optional co-scheduling with user. **Falsification:** compare total weighted reassignments and actual deadline outcomes with full-rescheduling baselines [5].

### Loop R4: silent omission from over-minimalism (harmful cascade)

`aggressive attention suppression -> missed consequential commitment -> reduced trust -> manual app checking -> greater user admin burden -> lower observed trust`

**Countermeasure:** severity-aware independent guardrails, last safe intervention deadlines, discoverable unresolved responsibilities, source coverage/freshness and post-hoc audit. **Falsification:** any decrease in surface interactions accompanied by a clinically/operationally meaningful increase in critical misses disqualifies the policy [12-16].

### Loop R5: incomplete information creates social damage

`stale source -> false "no reply" claim -> unnecessary follow-up -> damaged relationship / extra correspondence -> new coordination work`

**Countermeasure:** no non-event without coverage proof; read-after-write reconciliation, respect social norms, ask for consent to send. **Falsification:** force connector outages and delayed events; quantify false non-events and social overreach [1,2,3].

### Loop R6: overdelegation degrades chosen competence

`automation of learning task -> less deliberate practice -> declining independent skill -> need for more automatic assistance`

**Countermeasure:** distinguish administrative work from deliberately practiced skills, with user-chosen collaborative mode; no unwanted training prompts. **Falsification:** longitudinal skills tests and task-quality evaluation versus full-service automation [18-21].

### Loop R7: misinterpretation of a temporary exception as changed identity

`temporary crisis -> skipped routine -> inferred dislike of goal -> goal deprioritized -> fewer opportunities -> further skipped sessions`

**Countermeasure:** model temporary constraints separately from long-term goal intention; require explicit review before goal retirement. **Falsification:** simulated unusual weeks should not overwrite enduring goals [10,11,18,20].

### Loop B1: balanced, constructive coordination

`reconcile evidence -> prevent overcommitment -> reduce deadline risk -> lower emergency interruptions -> preserve meaningful time -> fewer avoidable scheduling conflicts`

This is a *hypothesized beneficial feedback loop*, not evidence that the complete effect exists. It suggests why the smallest viable intervention is sometimes **renegotiate one request before accepting it**, rather than reminders and rescheduling for every downstream consequence.

### Loop B2: preference correction reduces future interruption

`justifiable clarification -> explicit contextual preference -> better future decision -> fewer erroneous prompts -> lower user effort`

Potential negative side effect: repeated clarifications can become intrusive; optimize question value and stop when incremental improvement is low [9,16,28].

## 20. Open scientific problems, not solved merely by adding algorithms

**User-specific value estimation:** The true welfare utility function may be incoherent, changing, or inexpressible. Hard boundaries plus preference-sensitive Pareto decisions are more defensible than inferring a scalar value from engagement data.

**Social reciprocity:** A personal secretary acts in relationships where other people have their own rights and expectations. Coordinating cannot be reduced to optimizing one person's calendar; sending messages can create new obligations or unwanted pressure.

**Counterfactual identifiability:** One user experiences one history. Learning causal benefit from their responses is difficult because the policy alters their exposure, preferences and environment. Simulations and off-policy correction do not eliminate this challenge.

**Observation gaps:** Messages outside supported provider APIs, off-platform conversations, unlogged decisions and missed events mean the belief state is structurally incomplete. The system needs abstention and correction, not an omniscience narrative.

**Co-adaptation and power:** A proactive AI can shape what a person considers urgent or desirable. Its role should be support for user-selected values, not normative substitution or persuasion toward a provider-chosen productivity function.

**Generalization:** Findings from offices, tasks, students, health behavior and simulated agent benchmarks cannot automatically establish effectiveness for diverse individuals, cultures, occupations and family structures. A personal secretary needs longitudinal and participatory evaluation, including explicit opt-out and control.

## 21. Final design principles as testable invariants

1. **No inferred aspiration:** observed habit does not silently become a valued goal.
2. **No new commitment without admissibility:** a task that fits in a calendar gap may still cause infeasible work later.
3. **No unobserved non-event as fact:** assert absence only with appropriate source coverage.
4. **No action without current authority:** personalization never expands permissions.
5. **No completion by declaration:** external postconditions are required for verified completion.
6. **No optimizing engagement or completed-task count as primary reward:** measure human-valued outcomes and negative externalities.
7. **No quiet screen at the cost of missed obligations:** critical omission is a hard safety/evaluation requirement.
8. **No preference update from policy-selected exposure alone:** log selection and request explicit corrections when consequential.
9. **No forced growth:** preserve chosen skill practice and allow goal retirement or pause.
10. **No unbounded reasoning:** route routine cases to deterministic execution and escalate computation only for meaningful uncertainty.
11. **No blind rescheduling:** preserve accepted plans unless a material change justifies repair.
12. **No magic omniscience:** communicate unknowns, disconnected sources and uncertainty precisely.

**Recommended next research experiment:** Compare a baseline that only schedules accepted tasks against an admission-aware coordination controller. Seed identical synthetic multi-source histories containing meeting requests, shifting deadlines, explicit protected time, missing-reply events, and ambiguous messages. Test whether admission-awareness improves *feasible existing obligations and the user's chosen goal time*, not merely activity count. This is the simplest high-leverage experiment that exercises several connected mechanisms without a complex autonomous agent stack.

## 22. Companion causal research graph

The companion `Routin_Causal_Hypothesis_Graph_2026-11-16.json` encodes the concepts, signed and conditional proposed relations, sources, countermeasures, validation protocols, and a distinction between feedback cycles and one-way causal cascades. This is a traceable **hypothesis map**, not an empirically estimated structural causal model or proof of scientific novelty. In particular, a cited paper may support only one segment of a longer hypothesized pathway.