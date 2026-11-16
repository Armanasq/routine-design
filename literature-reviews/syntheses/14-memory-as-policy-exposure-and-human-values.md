# S14 — Learning the User Without Reproducing the Agent's Own Bias

**Research:** MemPABench P041 + MAGE P046 + Complementary Learning Systems P057 + Schnabel et al. P021 + goal-systems P011 + intent theory P039.

## Why this interconnection matters

A user may repeatedly engage with the items the agent surfaces because those are the only available choices. If the agent labels such activity a stable preference, a feedback loop emerges and may progressively displace the user's stated long-term goals.

Rapid episodic learning and slowly consolidated preferences must distinguish:
- what the user *actually did*;
- what they explicitly *want*;
- what they are *trying to become*;
- what the assistant *showed them*;
- what the assistant was *authorized* to do.

These are different evidence categories, not different confidence levels of the same statement.

## Architecture

Record the considered candidate set and display/selection policy version. Promote explicit corrections immediately within scope; inferred behavior stays provisional. For contested value tradeoffs, ask a focused question only if it changes the best allowable plan. Protected personal goals are preserved by declared constraints, not by a learned engagement score.

The long-term adaptation policy must be evaluated against older intentions and current explicit preferences, with user-controlled change and retirement. A skipped routine does not mean the underlying goal is unwanted.

## Experiment

Simulate two users with identical observed click histories but different explicit aspirational goals. A naive preference learner collapses their states; Routin's model should preserve distinct goals and recommend different feasible coordination decisions. Inject one-week exceptions and changing standing instructions; measure preference spillover and repeated unnecessary questions.

## Boundary

Personal growth is not an AI-determined objective. The agent learns how to help the person pursue chosen goals; it does not infer their ideal life from behavior or optimize engagement.