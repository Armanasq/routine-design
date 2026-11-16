# Universal cross-domain scenario test contracts

**All 16 scenarios are synthetic, design-level and NOT yet executed.** They specify expected invariants for future runtime harness and domain pack certification.

- [U001 — Learning exam vs work conflict](../../tests/scenarios/universal/u001-learning-exam-vs-work-conflict.json) — learning, work-projects
- [U002 — Learning mode versus delegated writing](../../tests/scenarios/universal/u002-learning-mode-versus-delegated-writing.json) — learning, applications
- [U003 — Fitness change with uncertain shoulder symptoms](../../tests/scenarios/universal/u003-fitness-change-with-uncertain-shoulder-symptoms.json) — fitness, health-navigation
- [U004 — Wellbeing and intervention fatigue](../../tests/scenarios/universal/u004-wellbeing-and-intervention-fatigue.json) — wellbeing, work-projects
- [U005 — Clinical record sorting without diagnosis](../../tests/scenarios/universal/u005-clinical-record-sorting-without-diagnosis.json) — health-navigation
- [U006 — Application eligibility uncertain](../../tests/scenarios/universal/u006-application-eligibility-uncertain.json) — applications, learning
- [U007 — Email sent without acceptance](../../tests/scenarios/universal/u007-email-sent-without-acceptance.json) — communication, work-projects
- [U008 — Family time and private event redaction](../../tests/scenarios/universal/u008-family-time-and-private-event-redaction.json) — family-life, work-projects
- [U009 — Travel booking financial side effect](../../tests/scenarios/universal/u009-travel-booking-financial-side-effect.json) — travel-logistics, finance-admin
- [U010 — Bill draft is not payment](../../tests/scenarios/universal/u010-bill-draft-is-not-payment.json) — finance-admin
- [U011 — Unknown domain fallback](../../tests/scenarios/universal/u011-unknown-domain-fallback.json) — core-coordination
- [U012 — Negative transfer of verified work skill](../../tests/scenarios/universal/u012-negative-transfer-of-verified-work-skill.json) — communication, health-navigation
- [U013 — Behavioral proximal outcome not clinical benefit](../../tests/scenarios/universal/u013-behavioral-proximal-outcome-not-clinical-benefit.json) — wellbeing, fitness, health-navigation
- [U014 — Tutor deployment outcomes conflict](../../tests/scenarios/universal/u014-tutor-deployment-outcomes-conflict.json) — learning
- [U015 — Cross-domain revocation and memory contamination](../../tests/scenarios/universal/u015-cross-domain-revocation-and-memory-contamination.json) — health-navigation, work-projects, communication
- [U016 — Open job application and gym during travel](../../tests/scenarios/universal/u016-open-job-application-and-gym-during-travel.json) — applications, fitness, travel-logistics

## Why scenarios span domains

A single-domain benchmark can conceal cross-domain mistakes: a learning tool might over-automate while the scheduling tool optimizes calendar utilization; a work email agent might leak health details; a generic completion checker might mark an application submitted when only its form was drafted. Domain composability is only real if these cases remain safe under unexpected combinations and time changes.

The scenario suite must eventually include negative controls, randomized reproducible event streams, source coverage uncertainty and independent outcome oracles. No automated tests are claimed here.
