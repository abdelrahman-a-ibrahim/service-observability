# Service Observability

Service telemetry, SLO dashboards and actionable alerting using Prometheus, Grafana and trace correlation.

**Status: In development** · Personal project by Abdelrahman Ahmed

## Overview

An observability project connecting infrastructure signals to user-visible service outcomes. The baseline targets Prometheus and Grafana with correlated logs and traces; a Dynatrace integration is an optional extension with separate account requirements.

## Current state

The repository currently contains the system design, delivery requirements, a synthetic input fixture and initial Python interfaces. Runtime behavior, service integrations and deployment are planned. Interface methods raise `NotImplementedError`; there is no running application or published runtime benchmark yet.

## Planned capabilities

- Service-level indicators for booking success and event freshness.
- Correlated metrics, structured logs and distributed traces.
- Provisioned Prometheus/Grafana dashboards and actionable alerts.
- Telemetry cardinality controls and missing-data detection.
- Incident timelines and an optional Dynatrace integration.

Detailed scope is tracked in the [delivery roadmap](docs/roadmap.md) and [requirements](docs/requirements.md).

## Architecture

```text
API / workers -> metrics + traces + logs -> dashboards
                           |
                     SLI evaluation -> alerts -> incident runbook
```

This is the proposed component design. See [architecture](docs/architecture.md) for boundaries and [architecture decisions](docs/adr/0001-system-boundaries.md) for the choices still to resolve.

## Technology direction

Prometheus · Grafana · Dynatrace · OpenTelemetry · SLIs/SLOs · Incidents.

These technologies describe the intended implementation. Dependencies and compatible versions will be pinned when introduced. Optional services are not required by the current source checks.

## Working with the source

```sh
git clone https://github.com/abdelrahman-a-ibrahim/service-observability.git
cd service-observability
python3 tools/check_project.py
```

Python 3.9+ is sufficient for the current standard-library source check. It parses Python and JSON and checks required project files. It does **not** run an application, validate deployment behavior or establish feature completion.

The initial application boundary is in [`src/service_observability/interfaces.py`](src/service_observability/interfaces.py). [`examples/scenario.json`](examples/scenario.json) provides a synthetic development input. Installation and runtime commands will be added with the first executable release.

## Quality and reliability

- Each alert links a user impact, owner and runbook.
- SLI results can be recomputed from saved synthetic samples.
- Dashboards distinguish missing data from zero errors.
- The incident report includes timestamps and evidence, not invented improvements.

These are acceptance targets. Failure scenarios are specified in [reliability verification](docs/reliability.md); [results](docs/verification/README.md) will be recorded as implementation progresses. Correctness and performance claims must reference an actual environment, workload and commit.

## Development roadmap

- [ ] Contracts and system boundaries
- [ ] Core implementation and behavior tests
- [ ] External adapters and scoped access
- [ ] Failure recovery and operational visibility
- [ ] Reproducible deployment and release validation

See [delivery stages and future scope](docs/roadmap.md). For deployment prerequisites and resource lifecycle, see [operations](docs/operations.md).

## Repository structure

```text
src/service_observability/       Initial application interfaces
examples/                  Synthetic development inputs
tests/                     Behavior verification plan
docs/architecture.md       Component design and boundaries
docs/requirements.md       Functional and quality requirements
docs/roadmap.md            Delivery stages and future scope
docs/reliability.md        Failure and recovery scenarios
docs/operations.md         Runtime and deployment plan
docs/verification/         Results as implementation progresses
tools/check_project.py     Source integrity check
```

## Development

Use focused feature branches, add behavior tests with implementation changes and update the relevant architecture decision when guarantees change. Read [CONTRIBUTING.md](CONTRIBUTING.md).

This is an independent personal project. Examples use synthetic data. See [NOTICE.md](NOTICE.md) for licensing status.

## References

- https://prometheus.io/docs/introduction/overview/
- https://grafana.com/docs/grafana/latest/
- https://opentelemetry.io/docs/
- https://docs.dynatrace.com/docs
