# ADR-0017 — Reasoning, Dispatch, Verification and Approval Are Separate Services

**Status:** design principle; execution adapter not implemented.

The LLM can interpret goals, propose capabilities, select candidate strategies and communicate. It cannot invent provider state, grant authority, generate arbitrary effectful URLs or call operations outside schema/identity policy. A separate executor rechecks current state, grant and registry revision immediately before effect. Provider ACK and actual user/counterparty outcomes are independently verified.

Prior art: ToolSandbox P078, tau-bench P077, APB P073, Saga P027 and Temporal official activity guidance. Distinguish planning search exhaustion from infeasibility; retry ambiguous remote effects only after reconciliation. A simulated planner "success" is not an actual completed action.