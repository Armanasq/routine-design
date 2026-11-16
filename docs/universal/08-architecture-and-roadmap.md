# Universal Routin — Systems Architecture and Delivery Gates

## Runtime topology

\`\`\`mermaid
flowchart TD
 UI[Voice or text intention] --> INT[Intent and support-mode resolver]
 INT --> ORC[Shared responsibility coordinator]
 SRC[Authorized sources] --> EV[Event and source-health ledger]
 EV --> RECON[Typed claim/entity/time reconciliation]
 RECON --> ORC
 ORC --> MEM[Temporal memory and goals]
 ORC --> CAP[Capability resolver]
 CAP --> PACK[Versioned domain capability packs]
 PACK --> KNOW[Specialist knowledge and tools]
 ORC --> PLAN[Cross-domain capacity and planning]
 PLAN --> ATT[Attention and initiative policy]
 ATT --> AUTH[Independent permission gate]
 AUTH --> EXEC[Durable workflow execution]
 EXEC --> VERIFY[Pack-specific postcondition verifier]
 VERIFY --> EV
 VERIFY --> LEARN[Qualified feedback and adaptive learning]
 LEARN --> MEM
 LEARN --> PACK
 \`\`\`

The domain pack outputs *requirements and candidate actions*, not unrestricted tool calls. Shared coordinator is the single owner of responsibility status. The permission gate is external to the LLM policy. Specialist tools may internally use models or deterministic engines; they do not create their own account-spanning grant.

## Data flows

**Instruction:** transcript/text -> intent and support-mode classification -> proposed goal/commitment -> versioned memory -> capability selection -> plan -> approval/authorized execution -> outcome evidence.

**Background event:** provider change -> dedupe and source coverage -> typed claim -> impact analysis -> selective capacity/attention re-evaluation -> silence/prepare/ask/execute within permission -> verification.

**Learning:** verified episode -> evaluate whether it was actual progress or proxy activity -> domain-specific interpretation -> candidate preference/procedure -> shadow simulation -> scoped promotion/rollback.

**Cross-domain change:** new clinical appointment -> update hard calendar resource without disclosing medical content to work-domain pack -> work deadlines reforecast -> prepare neutral scheduling alternative -> user approved communication if needed.

## Minimal backend information contract

For every candidate item, compute:
- Is there an actual need for user intervention?
- What is the last safe opportunity?
- What can be prepared invisibly and reversibly?
- What specific user decision remains?
- What is the minimal evidence to understand the trade-off?
- What information may legally and ethically be disclosed?
- Which domain pack defines the verification?
- If no trustworthy action is possible, is the correct result NOOP, resync, safe fallback or professional escalation?

This contract precedes UI design.

## Engineering sequence

**G0 Foundation:** typed shared ontology, identity, evidence, source freshness and separate authority model.

**G1 Domain pack SDK:** versioned manifests, outcome contracts, validators, risk envelopes and capability selection; begin with non-effectful work/task/communications.

**G2 Learning/application support:** learning objectives, practice evidence, current official deadlines, document workflow, and no unsolicited external submissions.

**G3 Wellbeing/fitness:** optional tracking and adaptive time allocation, voluntary goals, user-reported constraints, safe boundaries, no medical inference.

**G4 Health navigation:** explicit sensitive data partitions, source reconciliation, document/appointment support, specialist evaluation and clinician escalation; no autonomous medical decision-making.

**G5 Cross-domain planner:** conflict-aware capacity admission, protected goal constraints, negotiated alternatives and error-safe attention timing.

**G6 Adaptive learning:** behavioral feedback only when source/exposure and goal context are valid; qualified procedural transfer, drift monitoring and long-horizon evaluation.

**G7 Validated user surface:** only after information and safety contracts stabilize, design exceptionally minimal interaction and progressive disclosure.

## Implementation tradeoffs

One shared DB and modular architecture by default, not microservices per domain. Domain semantics and policy are configured/data-driven but critical checks are deterministic code. Optional semantic retrieval must never bypass temporal/permission filters. Specialist models and clinical toolchains are invoked only when justified by domain safety and evaluation. Durable workflows isolate side effects and verify provider outcomes; multi-agent debates are not substitutes for actual state.

## Acceptance gates

Every new pack must demonstrate: (a) no cross-domain private data leakage; (b) correct response to unsupported request; (c) no ungranted external effect; (d) correct outcome semantics; (e) reversible learning behavior and memory invalidation; (f) task-level usefulness against an existing baseline.

**Research gaps:** pack compatibility/negative transfer formalization, cross-domain causal planning under uncertainty, a realistic testbed that includes interpersonal and health-data constraints, and longitudinal human outcome validation.
