# Adaptive Assistance, Tutoring, Coaching and Human Agency

## Scientific difference between operational delegation and behavior change

"Email the meeting agenda" requests an administrative outcome. "Help me learn calculus" requests user competence. "Help me exercise consistently" requests sustained behavior within constraints. "Review a symptom diary" requests data organization and possibly health expertise. Identical conversational prompting for these intents is conceptually wrong.

## Adaptive intervention contract

The JITAI framework identifies **distal objective, proximal outcome, decision point, intervention options, tailoring variables and decision rule**. It also emphasizes receptivity and intervention burden. This is substantial prior art. Routin should implement these elements *where the intervention hypothesis is justified*, including an explicit NOOP option; not every calendar request requires a behavioral intervention.

Example:
- Distal: retain a chosen mathematical concept after a month.
- Proximal: answer a practice item without assistance.
- Decision point: when the next feasible practice interval begins.
- Tailoring: past accuracy, selected topic, time availability and stated learning mode.
- Options: practice item, explanation, reschedule, no prompt.
- Rule: avoid interrupting a higher-stakes committed obligation, respect user availability and favor active practice when authorized.

In physical activity, "user is receptive" cannot be inferred safely from physiological data alone; optional self-report and explicit constraints are appropriate. A legitimate NOOP may be better than disruptive nudging.

## Learning competence model

A learner model must distinguish:
- **exposure:** material opened or summary requested;
- **participation:** user interacted or attended;
- **demonstrated mastery:** validated performance on independent retrieval or applied task;
- **retention/transfer:** subsequent performance after delay or new context;
- **user intention:** whether mastery or just completion is desired.

Zimmerman's self-regulated-learning cycle motivates forethought/planning -> performance -> reflection. Dunlosky et al. and Cepeda et al. support practice testing and distributed practice, subject to domain and task. AI tutoring experiments show heterogeneous and even contradictory educational results: some tested tutor designs improved outcomes, while an October 2026 randomized trial reported lower grades and reduced course-platform participation for access to another AI tutor. Therefore, tutoring must be pedagogically evaluated; avoid blanket claims that AI explanations improve learning.

Learning support should prefer user practice and feedback when *learning* is the goal, not immediately completing exercises for them. In *delegate* mode, doing the task may be correct. Mode selection is user intention, not a fixed style preference.

## Exercise and fitness

Fitness planning requires training intent, current level (if explicitly provided), available equipment, session feasibility, user preferences, recovery context and relevant safety restrictions. Typical support can include schedule, technique education from reliable sources, self-reported session logging, progress reflection and safe alternatives.

Do not infer injury status, readiness or diagnosis from steps/sleep alone. No unsolicited high-intensity progression or medically consequential recommendation based solely on weak sensor patterns. A specialist pack must specify data uncertainty, screening, contraindication, emergency escalation and professional review boundaries.

## Wellbeing and personal growth

Wellbeing goals are user-chosen; many are qualitative, private and cannot be optimized as a single productivity number. Support reflection and sustainable routines without pathologizing a missed practice or treating absence of tracking as absence of progress. Respect explicit pause, refusal and changes of priority.

No artificial "daily therapy" obligation; no inferential diagnosis from language sentiment. For distress or symptoms, provide information and appropriate professional pathways rather than autonomous treatment. Intervention timing requires evidence of receptivity and ethical appropriateness, not simply a predicted engagement score.

## Domain-specific longitudinal adaptation

Fast: monitor authorized observations and current obligations.
Medium: adjust schedule and intervention dose to actual availability and user corrections.
Slow: revise calibrated expectations, user-selected goals and effectiveness of support—without deleting user choice or generalizing a temporary exception.

A standardized cross-domain "habit streak" is not an acceptable universal outcome metric. Learning retention, exercise adherence, wellbeing experience, application outcomes and communication agreements must retain their own meanings.

## Candidate research problem

Learn **how much to intervene and how** while preserving the user's chosen support mode, domain-specific competence and safety constraints. Evaluate with individual goals and burden, not universal engagement. Existing JITAI and personalized-health-agent frameworks make broad novelty claims indefensible without new methods and experimental proof.

**Key sources:** Nahum-Shani et al. (2018); Michie et al. (2011); Zimmerman (2002); Dunlosky et al. (2013); Cepeda et al. (2006); Lin et al. (2026); GPTCoach (2025); Nature personal health agent (2026).
