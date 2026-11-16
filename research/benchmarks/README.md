# Routin benchmark program

The cognitive coordination benchmark is a **specification**, not an executed benchmark. See [cognitive-coordination-benchmark.md](cognitive-coordination-benchmark.md).

It measures:
- Responsibility lifecycle correctness and social grounding.
- Temporal memory, scoped preferences and realized behavior.
- Memory utility versus construction and context costs.
- Step-level strategy validity, error isolation, procedural transfer.
- Constraint-aware attention, capacity, human agency and real-world outcome verification.

Existing public benchmarks (LongMemEval, Memora, MemPABench, MemoryArena, ALFWorld, WebShop) measure complementary slices but do not establish real-world secretary effectiveness. The proposed benchmark requires implementation, validation against human data, and reproducible baselines before any novelty or performance claims.

Initial [synthetic scenario fixtures](../../tests/scenarios/) are contracts only and currently lack a full simulation harness.