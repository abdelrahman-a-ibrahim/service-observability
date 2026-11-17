# Observability & Reliability Lab

**Signals that explain user-visible failure**

> Status: foundation only / implementation not started. Independent educational project by Abdelrahman Ahmed. This repository is not a reconstruction of employer systems, a production deployment or proof of completed work.

## The engineering challenge

Instrument WorkshopHub booking and event processing. Build dashboards and alerts around user journeys, not only infrastructure health. Prometheus/Grafana are the local path; Dynatrace is an optional adapter requiring an account.

This is a capstone for an experienced engineer. The goal is to defend tradeoffs, investigate failure and produce reproducible evidence, not just get a happy-path demo running.

**Technical focus:** Prometheus · Grafana · Dynatrace · OpenTelemetry · SLIs/SLOs · Incidents.

## What exists in this first commit

- A project-specific architecture brief and decision questions.
- Five implementation milestones with explicit review gates.
- Failure experiments and acceptance criteria.
- Typed Python interface scaffolds. Methods deliberately raise `NotImplementedError`.
- One synthetic scenario fixture; it is an input, not a successful output or benchmark.
- Evidence and journal templates, an issue template, and syntax/JSON foundation checks.

## What you will build

1. Define booking success and event freshness SLIs with denominators, exclusions, targets and measurement windows. Label targets as hypotheses until measured.
2. Instrument latency histograms, counters, logs and trace propagation. Set cardinality and payload-redaction budgets.
3. Build versioned Prometheus/Grafana dashboards for user outcomes and dependencies; provision them reproducibly.
4. Implement actionable alerts and test both detection and false positives. Compare multi-window burn-rate alerts with simple static thresholds.
5. Run an incident exercise, correlate signals, write a timeline and measure detection/recovery. Optionally reproduce equivalent views in Dynatrace without requiring it for the baseline.

## Start here

1. Read [the architecture brief](docs/architecture.md) and record the first decision in [ADR 0001](docs/adr/0001-system-boundaries.md).
2. Inspect [the synthetic scenario](examples/scenario.json) and [the interface boundary](src/observability_and_reliability_lab/interfaces.py).
3. Run the foundation checks from the repository root:

   ```sh
   python3 tools/check_foundation.py
   ```

   Python 3.9+ is sufficient for these standard-library checks. They parse Python and JSON; they do **not** validate runtime behavior, deployment safety, protocol compliance or completion.
4. Create a feature branch, implement milestone 1 and add behavior tests before adapters.
5. Follow [the milestone backlog](docs/milestones.md). Select and pin implementation dependencies when you introduce them; none are installed by this scaffold.
6. Complete [the failure lab](docs/failure-lab.md), gather [evidence](docs/evidence/README.md) and review [acceptance criteria](docs/acceptance.md).

There is deliberately no `deploy`, `apply`, paid API call, installed cloud SDK or working runtime in this initial commit.

## Architecture at a glance

```text
API / workers -> metrics + traces + logs -> dashboards
                           |
                     SLI evaluation -> alerts -> incident runbook
```

This is a proposed lab architecture. [The design brief](docs/architecture.md) identifies decisions still to make.

## Learning prerequisites

- `application-engineering-lab` (a suggested learning prerequisite; no runtime dependency is wired in)
- `aws-live-events-lab` (a suggested learning prerequisite; no runtime dependency is wired in)

Repositories are separate and can evolve independently. If you connect them later, exchange versioned fixtures or contracts; do not rely on sibling-relative imports. You can implement a standalone synthetic adapter first.

## What makes this substantial

- Event versus time-based SLI
- Histogram buckets and cardinality budget
- Metric alert versus trace-based investigation

You must explain what happens on retries, partial failure, concurrent operations and recovery. Record what your test environment cannot prove. No result is accepted simply because a dashboard is green.

## Definition of done

- Each alert links a user impact, owner and runbook.
- SLI results can be recomputed from saved synthetic samples.
- Dashboards distinguish missing data from zero errors.
- The incident report includes timestamps and evidence, not invented improvements.

Also supply installation/reproduction instructions, dependency versions, meaningful behavior tests, cleanup instructions, an architecture decision log and evidence from a repeatable demonstration. A checklist or syntax check alone does not satisfy completion.

## Advanced extensions

- Exemplars and trace-linked dashboards
- Telemetry-pipeline resource budgeting
- Synthetic user journeys
- Compare measurement windows with controlled traffic

Extensions follow a working baseline; they are not requirements for the first milestone.

## Boundaries and costs

Use fictional services, synthetic inputs and a disposable sandbox. Do not copy employer repositories, runbooks, tickets, customer data, credentials or internal architecture. Real cloud/provider adapters are future work and may incur costs; [the operations plan](docs/operations.md) must identify account, region, budget, resource inventory and teardown before deployment. Budget alerts notify; they do not constitute a hard spending cap.

## Publishable evidence, when earned

A completed lab may support a portfolio case study labeled **independent project**. Share your original code, sanitized diagrams, measured results and a failure/recovery write-up. Employer experience and personal lab evidence remain separate. Never copy illustrative fixture values into a results claim.

## Primary references

- https://prometheus.io/docs/introduction/overview/
- https://grafana.com/docs/grafana/latest/
- https://opentelemetry.io/docs/
- https://docs.dynatrace.com/docs

Read current official documentation when selecting SDKs, images, tool versions and integrations. The scaffold intentionally does not guess compatible version combinations.

## Repository map

- `src/observability_and_reliability_lab/interfaces.py`
- `examples/scenario.json`
- `docs/architecture.md`
- `docs/milestones.md`
- `docs/failure-lab.md`
- `docs/acceptance.md`
- `docs/learning-journal.md`
- `docs/evidence/README.md`
- `docs/operations.md` — local/cloud boundaries and teardown plan.
- `docs/adr/` — decisions and alternatives.
- `tools/check_foundation.py` — syntax and fixture integrity only.

## Working agreement

Keep commits focused: `docs`, `feat`, `test`, `fix`, `ops`. Work on a feature branch and merge only after the milestone review. Consult [CONTRIBUTING.md](CONTRIBUTING.md). No open-source license has been chosen yet; see [NOTICE.md](NOTICE.md).
