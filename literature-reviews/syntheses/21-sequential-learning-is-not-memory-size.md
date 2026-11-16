# S21 — The Agent Must Improve on the NEXT Problem

**Linked research:** P074 (CL-Bench), P075 (StreamMemBench), P076 (Continual Learning Exam), P050 (Reflexion), P055 (Memory-R1).

## Derivation

CL-Bench finds that dedicated memory architectures do not automatically give higher sequential improvement and may be beaten by simpler in-context approaches in the tested six domains. StreamMemBench finds agents fail to reliably turn recorded feedback into future assistance. CLE tests five-stage task sequences and shows large remaining gaps after diagnostic feedback. These findings identify the same failure at different timescales: storing a trace, reflecting on it and genuinely becoming more competent are not equivalent.

## Proposed mechanism

Episode records retain goal, context and source visibility, chosen policy, alternative actions, independent outcome and human correction. Only an outcome-supported lesson can become a proposed *scoped* strategy. The agent then tests it on different but related future cases. Failed transfer is retained as negative evidence, not suppressed to inflate learning scores.

Keep separate memory stages: observe, interpret, retrieve, select, realize, verify, learn and invalidate. A step can be correct individually and the final personal outcome can still be wrong.

## Anti-self-deception

A user clicks a work task because Routin exposed only work. That observation cannot establish a value preference for work over their explicitly selected learning goal. A completed AI-generated answer cannot establish the user learned to produce that answer. Outcome attribution remains unknown without appropriate comparisons.

## Experiment

Fixed backbone, tools and permissions; reset-state controls; identical latent environment over sequential tasks; held-out subjects and tool names. Compare text memory, scoped episodic memory, certified procedures and an adaptive meta-controller. Measure incremental gain and negative transfer, plus critical errors, not recall and narrative quality alone.

**Architecture:** docs/backbone/04-experience-and-continual-learning.md.