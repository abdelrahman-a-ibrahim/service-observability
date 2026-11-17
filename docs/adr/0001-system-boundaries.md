# ADR 0001: System boundaries and implementation approach

Status: proposed / decision not yet made.

## Context
Instrument WorkshopHub booking and event processing. Build dashboards and alerts around user journeys, not only infrastructure health. Prometheus/Grafana are the local path; Dynatrace is an optional adapter requiring an account.

## Decision questions
- Event versus time-based SLI
- Histogram buckets and cardinality budget
- Metric alert versus trace-based investigation

## Options
1. Small local implementation with synthetic adapters.
2. Integrated lab with real dependencies in a disposable environment.
3. A justified alternative to be supplied during design.

## Decision
Pending. Start by evaluating the smallest approach that can demonstrate the core invariant.

## Consequences to assess
Correctness, complexity, cost, recovery, trust boundaries, portability and maintenance burden.

## Evidence needed
A failure experiment, a working implementation slice and a comparison of the alternatives.

## Revisit when
Document a concrete load, team, correctness or operational constraint that invalidates the selected approach.
