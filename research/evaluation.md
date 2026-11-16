# Evaluation and falsification protocol

## Baselines
B0 chronological tasks; B1 hard-deadline rules; B2 weighted importance rank; B3 LLM-only recommendation; B4 structured responsibility model; B5 + time/capacity; B6 + attention; B7 + temporal preference learning; B8 + verified execution.

## Primary safety/utility
- Critical omission: confirmed high-consequence responsibility neither safely handled nor surfaced before last useful action time.
- False responsibility: asserted commitment unsupported by source/authority.
- False completion: terminal complete without verified outcome evidence.
- Unauthorized effect: side effect outside current grant (zero tolerance).
- Net admin minutes: baseline admin effort minus Routin oversight, correction, and associated rework.
- Personal goal preservation: adherence to explicitly chosen protected activities and substantive progress.
- Actual task feasibility: constraint and duration coverage, not just predicted fit.
- Attention intrusions per useful decision; correction time and decision errors.
- Schedule churn: weighted movement of accepted intervals after replanning.
- Preference temporal accuracy: currently valid vs superseded/exception preference.
- Relationship risk: erroneous recipient/identity and inappropriate external follow-up.

## Study sequence
1. Offline curated adversarial event timelines and oracle-labeled state transitions.
2. Controlled scenario experiments for timing, detail, decision correctness and unnecessary questions.
3. Shadow/live limited-scope pilot with audit and corrections.
4. Multiweek within-person study of changing preferences and disrupted routines.
5. Preregistered ablation comparing each policy component; report costs, confidence intervals and failures.

## Prohibited evaluation shortcuts
No 'tasks created' as proxy for productivity, no 'LLM agrees with itself' outcome label, no fabricated preference histories in a purported field study, no inference that fewer prompts equals better decisions, no universal psychological cost weights.