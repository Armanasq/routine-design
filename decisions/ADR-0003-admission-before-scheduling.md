# ADR-0003 — Admission and negotiation precede scheduling

Status: proposed.
Scheduling a proposed request as if accepted makes overload look solvable. Before acceptance, simulate the effect of additional obligation and generate negotiate/defer/decline/ask alternatives under explicit goals, time constraints and uncertainty.

Trade-offs: additional inference/optimization cost; requires realistic duration distributions and permission model. Verify with counterfactual arrival streams and infeasible acceptance rate. Sources: robust scheduling; Little's Law only under its assumptions; planning fallacy.