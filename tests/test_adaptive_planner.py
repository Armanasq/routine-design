import unittest

from reference_kernel.adaptive_planner import (
    Capability, CapabilityRegistry, dispatch_eligibility, outcome_verified, propose_plan,
)


class AdaptivePlannerTests(unittest.TestCase):
    def test_unseen_domain_composes_tools(self):
        tools = (
            Capability("discover_habitat", frozenset(), frozenset({"habitat_researched"})),
            Capability("prepare_aquarium", frozenset({"habitat_researched"}), frozenset({"aquarium_prepared"})),
            Capability("log_readiness", frozenset({"aquarium_prepared"}), frozenset({"ready_checked"})),
        )
        result = propose_plan(frozenset(), frozenset({"ready_checked"}), CapabilityRegistry("1", tools))
        self.assertEqual(result.status, "planned")
        self.assertEqual(result.steps, ("discover_habitat", "prepare_aquarium", "log_readiness"))

    def test_new_tool_enables_previous_impossible_goal(self):
        start = CapabilityRegistry("a", (Capability("fetch", frozenset(), frozenset({"data"})),))
        self.assertEqual(propose_plan(frozenset(), frozenset({"report"}), start).status, "impossible")
        new = CapabilityRegistry("b", start.capabilities + (Capability("compose", frozenset({"data"}), frozenset({"report"})),))
        self.assertEqual(propose_plan(frozenset(), frozenset({"report"}), new).status, "planned")

    def test_external_effect_requires_grant(self):
        reg = CapabilityRegistry("1", (Capability("send", frozenset({"drafted"}), frozenset({"message_submitted"}), grant="send:alice", kind="external"),))
        no = propose_plan(frozenset({"drafted"}), frozenset({"message_submitted"}), reg)
        self.assertEqual(no.status, "approval_required")
        self.assertEqual(no.missing_grants, frozenset({"send:alice"}))
        self.assertEqual(propose_plan(frozenset({"drafted"}), frozenset({"message_submitted"}), reg, frozenset({"send:alice"})).status, "planned")

    def test_allows_less_costly_path(self):
        reg = CapabilityRegistry("1", (
            Capability("shortcut", frozenset(), frozenset({"ready"}), cost=5),
            Capability("part1", frozenset(), frozenset({"intermediate"}), cost=1),
            Capability("part2", frozenset({"intermediate"}), frozenset({"ready"}), cost=1),
        ))
        self.assertEqual(propose_plan(frozenset(), frozenset({"ready"}), reg).steps, ("part1", "part2"))

    def test_untrusted_tool_excluded(self):
        reg = CapabilityRegistry("1", (Capability("attack", frozenset(), frozenset({"ready"}), trusted=False),))
        self.assertEqual(propose_plan(frozenset(), frozenset({"ready"}), reg).status, "impossible")

    def test_missing_precondition_never_assumed(self):
        reg = CapabilityRegistry("1", (Capability("submit", frozenset({"approved"}), frozenset({"submitted"})),))
        self.assertEqual(propose_plan(frozenset(), frozenset({"submitted"}), reg).status, "impossible")

    def test_goal_already_satisfied(self):
        self.assertEqual(propose_plan(frozenset({"complete"}), frozenset({"complete"}), CapabilityRegistry("1", ())).status, "satisfied")

    def test_registry_change_blocks_dispatch(self):
        reg = CapabilityRegistry("new", (Capability("send", frozenset(), frozenset({"sent"}), grant="send:1", kind="external"),))
        self.assertEqual(dispatch_eligibility("send", reg, "old", frozenset(), frozenset({"send:1"}), True), (False, "registry_changed"))

    def test_grant_revocation_blocks_dispatch(self):
        reg = CapabilityRegistry("1", (Capability("send", frozenset(), frozenset({"sent"}), grant="send:1", kind="external"),))
        self.assertEqual(dispatch_eligibility("send", reg, "1", frozenset(), frozenset(), True), (False, "grant_missing"))

    def test_source_stale_blocks_dispatch(self):
        reg = CapabilityRegistry("1", (Capability("send", frozenset(), frozenset({"sent"}), grant="send:1", kind="external"),))
        self.assertEqual(dispatch_eligibility("send", reg, "1", frozenset(), frozenset({"send:1"}), False), (False, "source_stale"))

    def test_unverified_precondition_blocks_dispatch(self):
        reg = CapabilityRegistry("1", (Capability("send", frozenset({"confirmed"}), frozenset({"sent"}), grant="send:1", kind="external"),))
        self.assertEqual(dispatch_eligibility("send", reg, "1", frozenset(), frozenset({"send:1"}), True), (False, "precondition_unverified"))

    def test_provider_prediction_not_verified_outcome(self):
        reg = CapabilityRegistry("1", (Capability("send", frozenset(), frozenset({"recipient_agreed"}), grant="send:1", kind="external"),))
        result = propose_plan(frozenset(), frozenset({"recipient_agreed"}), reg, frozenset({"send:1"}))
        self.assertEqual(result.status, "planned")
        self.assertFalse(outcome_verified(frozenset({"recipient_agreed"}), frozenset({"message_sent"})))

    def test_cycle_is_bounded(self):
        reg = CapabilityRegistry("1", (
            Capability("a", frozenset(), frozenset({"x"})),
            Capability("b", frozenset({"x"}), frozenset({"y"}), deletes=frozenset({"x"})),
            Capability("c", frozenset({"y"}), frozenset({"x"}), deletes=frozenset({"y"})),
        ))
        self.assertEqual(propose_plan(frozenset(), frozenset({"unreachable"}), reg, max_steps=50).status, "impossible")

    def test_max_steps_bounds_search(self):
        reg = CapabilityRegistry("1", (
            Capability("a", frozenset(), frozenset({"x"})),
            Capability("b", frozenset({"x"}), frozenset({"y"})),
        ))
        self.assertEqual(propose_plan(frozenset(), frozenset({"y"}), reg, max_steps=1).status, "search_exhausted")

    def test_state_budget_exhaustion_is_not_infeasibility(self):
        reg = CapabilityRegistry("1", (
            Capability("a", frozenset(), frozenset({"x"})),
            Capability("b", frozenset({"x"}), frozenset({"goal"})),
        ))
        self.assertEqual(propose_plan(frozenset(), frozenset({"goal"}), reg, max_states=1).status, "search_exhausted")

    def test_invalid_registry_rejected(self):
        cap = Capability("a", frozenset(), frozenset({"x"}))
        with self.assertRaises(ValueError):
            CapabilityRegistry("1", (cap, cap))

    def test_external_missing_grant_rejected(self):
        with self.assertRaises(ValueError):
            Capability("send", frozenset(), frozenset({"sent"}), kind="external")

    def test_unseen_subdomain_works_without_category(self):
        operators = (
            Capability("find_permit", frozenset(), frozenset({"permit_identified"})),
            Capability("compile_package", frozenset({"permit_identified"}), frozenset({"package_ready"})),
        )
        a = propose_plan(frozenset(), frozenset({"package_ready"}), CapabilityRegistry("1", operators))
        b = propose_plan(frozenset(), frozenset({"package_ready"}), CapabilityRegistry("2", operators))
        self.assertEqual(a.steps, b.steps)

    def test_multiple_goals_share_preparation(self):
        tools = (
            Capability("research", frozenset(), frozenset({"research_done"})),
            Capability("write", frozenset({"research_done"}), frozenset({"draft_done"})),
            Capability("review", frozenset({"research_done"}), frozenset({"review_done"})),
        )
        outcome = propose_plan(frozenset(), frozenset({"draft_done", "review_done"}), CapabilityRegistry("1", tools))
        self.assertEqual(outcome.status, "planned")
        self.assertEqual(outcome.steps.count("research"), 1)


if __name__ == "__main__":
    unittest.main()
