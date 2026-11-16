# Second-order consequences and adverse feedback loops

## Causal hypotheses (not established effects)
1. **Overcommitment rebound:** automation saves minutes -> user accepts additional demands -> baseline load increases -> stress/overdue work returns. Countermeasure: admission policy that respects user-chosen capacity and recovery; measure total accepted load and actual out-of-hours work.
2. **Policy-induced preference bias:** show work items -> user clicks work -> algorithm interprets clicks as preference -> work becomes more visible. Countermeasure: separate explicit intent from exposure-mediated feedback; hold protected goals.
3. **Replan thrash:** frequent external changes -> repeated reschedules -> coordination overhead -> more changes. Countermeasure: stability penalty, hysteresis, soft freeze horizon, explicit replanning conditions.
4. **Delegation deskilling:** automate desired practice -> less practice -> weaker competence -> more demand for assistance. Countermeasure: optional user-declared practice goals, human-first mode for learning tasks.
5. **Evidence error cascade:** stale source -> false absence inference -> unnecessary follow-up -> relationship friction -> user corrects assistant -> overbroad preference change. Countermeasure: freshness-gated absence, identity check, scoped feedback.

## Why the feedback graph matters
An isolated module may optimize its own metric while degrading the system. A notification policy that minimizes prompts can hide dependencies; time utilization can make the user more overcommitted; model confidence can reinforce already-biased user observations.

## Tests
Longitudinal synthetic controlled environments with configurable event arrivals, goal shifts and policy changes; separate user-level field studies for true human effects. Report adverse loops explicitly even if total task completion rises.