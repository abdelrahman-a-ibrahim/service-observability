# Verification plan

Runtime behavior tests will be added with the implementation. The current source integrity check does not provide runtime coverage.

## Required behavior coverage
- Each alert links a user impact, owner and runbook.
- SLI results can be recomputed from saved synthetic samples.
- Dashboards distinguish missing data from zero errors.
- The incident report includes timestamps and evidence, not invented improvements.

## Failure coverage
- Inject dependency latency without exhausting CPU.
- Stop a consumer while the API stays healthy.
- Introduce a high-cardinality metric label in a bounded experiment.
- Break telemetry export and distinguish missing data from healthy service.

Add domain tests, adapter contract tests and integration tests as those components are implemented. Include relevant invalid input, unauthorized access, concurrency, retry and restart scenarios. Real dependency guarantees require real integration evidence; mocks alone cannot establish ordering, replication, consistency or durability.

See [reliability](../docs/reliability.md) for execution/reporting requirements.
