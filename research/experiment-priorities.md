# Prioritized experiments: minimum proof before architectural complexity

| Order | Experiment | Competing explanations | Decision gate |
|---|---|---|---|
| 1 | Typed current state + cheap BM25 vs large RAG/graph | Complex memory may waste construction cost and still omit critical facts | Add additional retrieval only if measured downstream improvement |
| 2 | Working context mandatory facts + optional retrieval | Retrieval gains may be due to more context tokens rather than better selection | Match context budget; require no hard-constraint omissions |
| 3 | Explicit vs behavior-inferred preferences with drift | A user repeatedly attending an event is not evidence they like it | Require scoped inference and no incorrect promotion |
| 4 | Strategy refresh policies | Always-refresh gains may be compute rather than learning; model self-evaluation can become inertial | Match cost and test independent evidence triggers |
| 5 | Verified procedure learning vs static scripts | Success may be incidental or nontransferable | Demonstrate held-out task transfer and zero ungranted effects |
| 6 | Joint memory/attention/time policy | More modules may yield more prompts and churn | Compare total user burden, deadline coverage and goals |
| 7 | Longitudinal adaptation | Simulated habits may not reflect real preferences | Consented multiweek study with corrections, drift and choice outcomes |

Every study logs model/prompt version, memory revision, source-coverage version, policy candidate set, intervention timing, external postcondition and cost. Report failures stratified by severity. Never interpret a standard agent benchmark alone as evidence that Routin benefits a real person's wellbeing or productivity.
