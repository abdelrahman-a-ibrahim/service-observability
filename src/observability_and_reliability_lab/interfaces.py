"""Proposed application boundary for Observability & Reliability Lab.

This is a design scaffold, not a functional SDK or service. Refine the return
models during milestone 1; dict/list types leave that decision open deliberately.
"""

class SliCalculator:
    def evaluate(self, samples: list, objective: float) -> dict:
        """Calculate good/eligible events and error-budget consumption."""
        raise NotImplementedError("Implement this boundary with behavior tests first.")

    def correlate(self, trace_id: str) -> dict:
        """Find related request, event and worker evidence without exposing sensitive payloads."""
        raise NotImplementedError("Implement this boundary with behavior tests first.")

