# Architecture

Status: proposed. Components shown below are implementation targets.

## Product context
An observability project connecting infrastructure signals to user-visible service outcomes. The baseline targets Prometheus and Grafana with correlated logs and traces; a Dynatrace integration is an optional extension with separate account requirements.

## Component view
```text
API / workers -> metrics + traces + logs -> dashboards
                           |
                     SLI evaluation -> alerts -> incident runbook
```

## Design decisions
- Event versus time-based SLI
- Histogram buckets and cardinality budget
- Metric alert versus trace-based investigation

Record decisions and alternatives in [ADR 0001](adr/0001-system-boundaries.md). Define authoritative state, acknowledgement boundaries, identities, retry behavior and recovery ownership before implementing adapters.

## Interface boundary
`src/service_observability/interfaces.py` defines the initial application boundary. Return models and error contracts remain to be specified. These interfaces do not implement the component graph.

## Integration boundaries
Local adapters and synthetic fixtures precede external integrations. Every live adapter needs an explicit identity, permission scope, timeout strategy and observability contract. Separate user-supplied content from execution authority.

## Deployment design
Document topology, dependency versions, configuration and state persistence alongside the first executable delivery. Record what local environments cannot establish about availability, ordering or durability.

## Compatibility
Version interfaces and fixtures when their semantics change. Sibling projects are optional integrations, not implicit filesystem dependencies.
