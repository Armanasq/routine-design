# Routin Cognitive Architecture — From Memory to Practical Judgment

**Status:** research proposal and architecture specification, 2026-11-16. No scientifically established novelty or user benefit is claimed.

## Fundamental objective

An AI personal secretary is valuable when it preserves the user's intentions, coordinates other people's contributions, protects time and attention, and accomplishes delegated outcomes with minimal supervision. It is not enough to sound natural, remember a fact, or perform a tool call.

The engineering challenge is to maintain a trustworthy model of what is true, what is intended, what is feasible, what Routin is allowed to do, and what actually happened while all five change asynchronously.

## Five different ways the assistant must improve

1. **Knowledge quality:** distinguish source coverage, observations, beliefs, intentions and authority; detect outdated and contradictory information.
2. **Operational skill:** reuse successful, verified procedures in comparable contexts; do not universalize an unexplained success.
3. **Decision quality:** allocate user attention and system computation in proportion to consequence and uncertainty.
4. **Relationship coordination:** distinguish messages, mutual understanding, agreement and fulfilled obligations.
5. **Human development:** respect aspirational goals, competence and preferred autonomy; efficiency alone is not the objective.

The central idea is an **evidence-gated, multi-timescale practical reasoning system**. State and memory are decision infrastructure, not a chatbot accessory.

## What counts as learning

Learning must show an observable difference in a subsequent decision and preferably a verified benefit. Examples:
- After the user explicitly changes evening-availability rules, new scheduling decisions honor the scoped constraint without affecting unrelated contexts.
- After a provider-side retry ambiguity, Routin remembers the *specific* recovery procedure and checks external state before sending again.
- After several late projects, duration forecasts become better calibrated without assuming the user prefers working late.
- After interrupted work, the assistant knows how to preserve an evidence-grounded return point without forcing a ritual on every task switch.
- After a repeated false assumption, its decision process asks for a missing fact rather than restating the same wrong inference.

Storing more text, giving longer answers, increasing autonomous actions, or satisfying a recall benchmark does not establish learning quality.

## The three-timescale model

**Fast, event-sensitive:** synchronizes evidence, maintains current responsibility state and enforces hard permissions. This must not depend on an LLM reflection job.

**Intermediate, task-local:** constructs a bounded working context, chooses or revises a strategy, negotiates commitments and verifies outcomes. Dynamic strategy adaptation is useful only when the state materially changes.

**Slow, longitudinal:** extracts candidate routines, builds calibrated task-duration priors, evaluates preferred interaction policy, updates versioned procedural skills and detects drift in long-term intentions. High-impact changes require user confirmation.

These loops can disagree. Hard permissions and verified source state override a probabilistic preference; an explicitly chosen goal can constrain a locally favorable schedule; an uncertain prediction cannot overwrite a confirmed commitment.

## Cross-paper synthesis

Baddeley's episodic buffer motivates binding modalities in a temporary workspace; complementary learning systems motivate retaining fresh episodes separately from slowly learned generalizations; MemGPT motivates context paging; AdaMEM motivates dynamic task-state-conditioned strategies; MAGE motivates execution-path integrity and selective rollback; Memory-R1 motivates distinct memory write actions; MemPABench separates memory retrieval from behavior realization; memory systems studies warn that complex construction may cost more without better downstream utility.

All analogies from neuroscience are **design inspirations**, not claims that an LLM implements the corresponding human brain mechanism.

## Non-goals

No memory omniscience. No arbitrary personalized life objective inferred from history. No background agent changing its own grants. No unbounded self-modifying prompts or unreviewed automatic fine-tuning on user data. No mandatory "coach" interactions when the user wants a secretary. No GUI work until information-contract and task-utility baselines are established.

## Definition of a potentially meaningful contribution

A joint policy for *which state to maintain, which experience to promote, when to deliberate or refresh a strategy, what the user must decide, and how to verify the resulting outcome*, while honoring constraints and preserving chosen goals. Each component exists in prior art; the joint formulation is a hypothesis requiring measurable advantage and an ablation.

See memory contracts, decision policy, experience promotion and research agenda in this directory.