from __future__ import annotations

from dataclasses import dataclass
from heapq import heappop, heappush
from typing import Literal


@dataclass(frozen=True)
class Capability:
    name: str
    requires: frozenset[str]
    produces: frozenset[str]
    deletes: frozenset[str] = frozenset()
    grant: str | None = None
    kind: Literal["observe", "prepare", "external"] = "prepare"
    trusted: bool = True
    cost: int = 1

    def __post_init__(self) -> None:
        if not self.name or not self.produces:
            raise ValueError("capability requires a name and at least one effect")
        if self.cost <= 0:
            raise ValueError("capability cost must be positive")
        if self.kind == "external" and not self.grant:
            raise ValueError("external capabilities require a named grant")
        if any(not x for x in self.requires | self.produces | self.deletes):
            raise ValueError("fact names must not be empty")


@dataclass(frozen=True)
class CapabilityRegistry:
    revision: str
    capabilities: tuple[Capability, ...]

    def __post_init__(self) -> None:
        if not self.revision or len({c.name for c in self.capabilities}) != len(self.capabilities):
            raise ValueError("nonempty revision and unique capability names required")


@dataclass(frozen=True)
class PlanProposal:
    status: Literal["satisfied", "planned", "approval_required", "impossible", "search_exhausted"]
    steps: tuple[str, ...]
    registry_revision: str
    predicted_facts: frozenset[str]
    missing_grants: frozenset[str]
    total_cost: int | None


def _search(initial: frozenset[str], goal: frozenset[str], capabilities: tuple[Capability, ...],
            max_steps: int, max_states: int) -> tuple[tuple[tuple[str, ...], frozenset[str], int] | None, bool]:
    queue: list[tuple[int, int, tuple[str, ...], frozenset[str]]] = [(0, 0, (), initial)]
    best: dict[frozenset[str], tuple[int, int]] = {initial: (0, 0)}
    seen = 0
    depth_limited = False
    while queue and seen < max_states:
        cost, depth, steps, facts = heappop(queue)
        if best.get(facts) != (cost, depth):
            continue
        seen += 1
        if goal <= facts:
            return (steps, facts, cost), False
        if depth >= max_steps:
            depth_limited = True
            continue
        for cap in capabilities:
            if not cap.requires <= facts:
                continue
            next_facts = (facts - cap.deletes) | cap.produces
            if next_facts == facts:
                continue
            next_cost, next_depth = cost + cap.cost, depth + 1
            previous = best.get(next_facts)
            if previous is None or (next_cost, next_depth) < previous:
                best[next_facts] = (next_cost, next_depth)
                heappush(queue, (next_cost, next_depth, steps + (cap.name,), next_facts))
    return None, depth_limited or bool(queue)


def propose_plan(initial: frozenset[str], goal: frozenset[str], registry: CapabilityRegistry,
                 grants: frozenset[str] = frozenset(), max_steps: int = 12,
                 max_states: int = 10000) -> PlanProposal:
    if not goal:
        raise ValueError("at least one desired fact is required")
    if max_steps < 0 or max_states < 1:
        raise ValueError("invalid search budget")
    if goal <= initial:
        return PlanProposal("satisfied", (), registry.revision, initial, frozenset(), 0)
    trusted = tuple(sorted((c for c in registry.capabilities if c.trusted), key=lambda c: c.name))
    allowed = tuple(c for c in trusted if c.grant is None or c.grant in grants)
    solution, allowed_exhausted = _search(initial, goal, allowed, max_steps, max_states)
    if solution is not None:
        steps, facts, cost = solution
        return PlanProposal("planned", steps, registry.revision, facts, frozenset(), cost)
    candidate, all_exhausted = _search(initial, goal, trusted, max_steps, max_states)
    if candidate is not None:
        steps, facts, cost = candidate
        by_name = {c.name: c for c in trusted}
        missing = frozenset(by_name[name].grant for name in steps if by_name[name].grant and by_name[name].grant not in grants)
        return PlanProposal("approval_required", steps, registry.revision, facts, missing, cost)
    return PlanProposal("search_exhausted" if allowed_exhausted or all_exhausted else "impossible", (), registry.revision, initial, frozenset(), None)


def dispatch_eligibility(operation: str, registry: CapabilityRegistry, expected_revision: str,
                         observed_facts: frozenset[str], grants: frozenset[str],
                         source_current: bool) -> tuple[bool, str]:
    if registry.revision != expected_revision:
        return False, "registry_changed"
    if not source_current:
        return False, "source_stale"
    cap = next((c for c in registry.capabilities if c.name == operation), None)
    if cap is None or not cap.trusted:
        return False, "capability_unavailable"
    if not cap.requires <= observed_facts:
        return False, "precondition_unverified"
    if cap.grant and cap.grant not in grants:
        return False, "grant_missing"
    return True, "eligible_not_executed"


def outcome_verified(goal: frozenset[str], independently_observed_facts: frozenset[str]) -> bool:
    if not goal:
        raise ValueError("empty outcome goal")
    return goal <= independently_observed_facts
