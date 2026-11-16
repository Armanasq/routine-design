# Universal Routin — Falsifiable Research Program

## Prior art constraints

- Mixed-initiative timing and user control: Horvitz and interruption research.
- JITAI tailoring and decision-point policy: Nahum-Shani et al. 2018 and subsequent reviews.
- Cross-session coherence/continuity/adaptation/agency: Lin et al. 2026 longitudinal health agent.
- Specialized health analytics, domain expertise and coaching under a unified interface: *The anatomy of a personal health agent* (Nature 2026).
- COM-B and behavior-change intervention design: Michie et al. 2011.
- Self-regulated learning, spaced testing: Zimmerman, Dunlosky, Cepeda.
- Agent episodic/procedural/working memory: MemGPT, AdaMEM, MAGE, ExpeL, Memory-R1.
- Safety/assurance: WHO digital health and FDA domain-specific guidance.

Routin is not novel because it "does multiple things" or "has agents for each domain." Potential scientific contribution requires a new formal composition policy or convincing evidence that it improves cross-domain human outcomes with adequate authority and safety.

## Candidate hypotheses

U1. **Compositional transfer:** Shared responsibility primitives plus domain contracts can support unseen domains with fewer errors than a prompt-only assistant, without increasing data leaks or unsound inferences.
U2. **Correct support mode:** User-intent-dependent delegation, tutoring, coaching, collaboration and observation reduce errors and unnecessary interaction compared with a fixed "always automate" or "always coach" model.
U3. **Cross-domain resource protection:** Constraint-based portfolios with protected personal goals reduce overcommitment and unwanted goal displacement compared with calendar-gap and static priority approaches.
U4. **Intervention timing:** JITAI-inspired decision points and a NOOP option improve useful responses per intervention compared with scheduled reminders, while holding omissions and safety constant.
U5. **Domain-specific verification:** Typed outcome contracts reduce false completion (learning, applications, health navigation, social agreement) compared with universal "tool call succeeded" completion.
U6. **Privacy and negative transfer:** Scoped domain memories and capability compatibility reduce erroneous cross-domain reuse compared with global untyped memory.

## Mixed evidence must be part of design

Learning: Dunlosky/Cepeda provide general retrieval-practice/spacing support; one 2025 randomized AI tutoring trial reports improvements; an October 2026 multi-section university trial reports worse grades and participation. These results are not necessarily contradictory when interventions/populations differ. Routin must not infer that generic AI-tutor access improves learning.

Physical activity: GPTCoach (CHI 2025) reports a supervised single-session feasibility study and explicitly cannot establish long-term exercise behavior change. A universal assistant may coordinate routines without claiming validated exercise-treatment outcomes.

Health: Nature's 2026 personal health agent uses specialized evaluators and substantial expert/human annotations; the 2026 longitudinal framework is conceptual. Neither proves safe autonomous medical decision-making for Routin.

## Evaluation suites

**Shared-core tests:** ambiguous intent, conditional commitments, missing webhook, authorized vs unauthorized send, calendar overload, scope-limited preference, wrong recipient and verified outcomes.

**Pack conformance:** all declared capabilities must have data-source and risk contracts; unsupported specialist acts return bounded fallback. Unit/temporal consistency and source freshness are part of evidence rules.

**Cross-domain interference:** health fact present in work summarization; work meeting proposal conflicting with family and gym; tutor mode accidentally solves exam; scheduling habit learned from temporary emergency; application deadline changed at unofficial forum; health/wellbeing safety update leaves user goal intact.

**Longitudinal studies:** balanced domain portfolio and actual user-reported goals over time. Do not simulate precise psychological states. Include work, training, learning, health-navigation, relationship and application contexts where participant consent and representative evidence exist.

## Outcomes and guardrails

Primary: verified responsibility resolution, user administrative time net of oversight/corrections, missed critical obligations, domain-specific meaningful goal progress, unauthorized effects (zero tolerance), wrong-context data disclosure (zero tolerance).

Secondary: intervention burden, calibration, uptake where relevant, error recovery time, counterpart effort, user agency, protected goal capacity, impact of advanced memory features on total compute cost.

Never publish a global productivity score that sums incomparables. Report per-domain outcomes, Pareto tradeoffs and worst-case harm strata.

## Experimental design

1. Freeze domain-agnostic baseline with no specialist pack.
2. Add domain packs individually, evaluating in-domain and out-of-domain interference.
3. Add shared planner, then memory, then intervention timing; ablate each.
4. Introduce cross-domain scenarios with multiple simultaneous, partly conflicting commitments and limited observation.
5. Compare matched token/model/tools/permission budget.
6. After safety gates, use consented longitudinal human study; report subgroup differences and adverse effects.

A valid contribution must survive *unseen* domain compositions and maintain the safety properties of each component. A demo covering many categories is not enough.
