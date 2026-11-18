# Reliability and failure verification

Status: verification scenarios planned; no results recorded yet.

## Required scenarios
- Inject dependency latency without exhausting CPU.
- Stop a consumer while the API stays healthy.
- Introduce a high-cardinality metric label in a bounded experiment.
- Break telemetry export and distinguish missing data from healthy service.

## Verification protocol
For each implemented scenario, document:
1. Commit, runtime versions, environment and topology.
2. Input workload and the expected invariant.
3. Baseline observations, fault injection and timestamps.
4. Observed errors, duplicate effects or state inconsistencies.
5. Recovery steps and measured time to restore behavior.
6. Resource cleanup and remaining limitations.

A simulator establishes application behavior within its assumptions. Real service ordering, consistency, failover and durability claims require verification against the selected dependencies. Distinguish those results in reports.

## Release evidence
- Each alert links a user impact, owner and runbook.
- SLI results can be recomputed from saved synthetic samples.
- Dashboards distinguish missing data from zero errors.
- The incident report includes timestamps and evidence, not invented improvements.

Store concise reports in [verification results](verification/README.md). Targets and illustrative fixture values must not be reported as measurements.
