# Functional and quality requirements

Status: proposed requirements, not delivered capabilities.

## Purpose
An observability project connecting infrastructure signals to user-visible service outcomes. The baseline targets Prometheus and Grafana with correlated logs and traces; a Dynatrace integration is an optional extension with separate account requirements.

## Target capabilities
- Define booking success and event freshness SLIs with denominators, exclusions, targets and measurement windows. Label targets as hypotheses until measured.
- Instrument latency histograms, counters, logs and trace propagation. Set cardinality and payload-redaction budgets.
- Build versioned Prometheus/Grafana dashboards for user outcomes and dependencies; provision them reproducibly.
- Implement actionable alerts and test both detection and false positives. Compare multi-window burn-rate alerts with simple static thresholds.
- Run an incident exercise, correlate signals, write a timeline and measure detection/recovery. Optionally reproduce equivalent views in Dynatrace without requiring it for the baseline.

## Acceptance criteria
- Each alert links a user impact, owner and runbook.
- SLI results can be recomputed from saved synthetic samples.
- Dashboards distinguish missing data from zero errors.
- The incident report includes timestamps and evidence, not invented improvements.

## Cross-cutting requirements
- Reproducible configuration and documented version requirements.
- Explicit invalid-input, authorization and dependency-failure behavior.
- Clearly defined durable state, retries and concurrency boundaries.
- Observable operations with bounded, non-sensitive diagnostic output.
- A documented resource lifecycle, recovery procedure and cleanup path.

## Scope control
This repository owns its implementation and contracts. Optional integrations with other personal projects use versioned interfaces. Sample data is synthetic. External accounts and paid services are not required for the current source checks.
