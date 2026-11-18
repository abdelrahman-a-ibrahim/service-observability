# ADR 0001: System boundaries and implementation approach

Status: proposed.

## Context
An observability project connecting infrastructure signals to user-visible service outcomes. The baseline targets Prometheus and Grafana with correlated logs and traces; a Dynatrace integration is an optional extension with separate account requirements.

## Questions
- Event versus time-based SLI
- Histogram buckets and cardinality budget
- Metric alert versus trace-based investigation

## Alternatives
- A local implementation with synthetic external adapters.
- An integrated deployment with real dependencies in an isolated environment.
- A smaller implementation that preserves the core invariant.

## Decision
Pending. Record the selected option, rejected alternatives and rationale before implementing external adapters.

## Consequences
Assess correctness, operational complexity, cost, security boundaries, recovery and maintenance. Define the concrete constraint that would justify revisiting the decision.
