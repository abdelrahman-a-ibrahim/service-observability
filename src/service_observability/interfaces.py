"""Initial application boundary for Service Observability.

The runtime is in development. Refine models and errors alongside the first
implementation; dict/list annotations mark contracts still to be formalized.
"""

class SliCalculator:
    def evaluate(self, samples: list, objective: float) -> dict:
        """Calculate good/eligible events and error-budget consumption."""
        raise NotImplementedError("Runtime implementation is in development.")

    def correlate(self, trace_id: str) -> dict:
        """Find related request, event and worker evidence without exposing sensitive payloads."""
        raise NotImplementedError("Runtime implementation is in development.")
