# S09 — An integrated test that exposes superficially correct agents

## Synthetic story
On Monday, a collaborator requests a Friday proposal. The user's calendar includes fixed meetings and a protected Thursday learning block. Tuesday's email says the collaborator *might* move the deadline, but no confirmation follows. Wednesday the user explicitly says they would rather keep evenings free. A notification outage occurs Thursday. The agent has already generated a draft follow-up; the provider times out after the request may have been sent.

## Required decisions
1. Extract Friday as initial claimed deadline, then hold Tuesday's conditional statement as a hypothesis rather than a confirmed extension.
2. Preserve Thursday protected study, model proposal duration and preparation uncertainty, propose an alternative to a new meeting before accepting it.
3. Keep evening preference scoped and effective from Wednesday; do not overfit to older late-calendar observations.
4. Avoid claiming no reply during source outage; trigger source reconciliation.
5. Timeout after send must produce `verification_unknown` and provider-side reconciliation—not a second blind send.
6. If response already sent, `submitted` is not `recipient_agreed`; keep handoff waiting.
7. If interrupting is necessary, preserve source-backed work resume point; otherwise batch.
8. Logging must show which candidate actions were considered, suppressed and why.

## What fails in weaker designs
Chat memory conflates a proposed extension with a confirmed deadline; naive RAG retrieves older evenings preference; greedy calendar scheduler displaces protected time; notification ranker interprets silence as low priority; retrying workflows double-send; LLM verbally claims completion with no evidence.

## Test assertions
No unauthorized effect, no double-send, no false completion, no premature deadline revision, no stale-preference use, no unsupported negative-inference during stale sync. Compare attention burden and feasible rescheduling against baselines.