# Decision Log

Major decisions should be recorded as ADR files in `agents/decisions/`.

## 2026-07-09

- Bootstrap decision: create `agents/` as the project memory and operating system before application code.
- Bootstrap decision: do not build dashboards or application implementation during Phase 0.
- Bootstrap assumption: likely architecture is native iOS + HealthKit, secure sync API, raw/normalized/derived data layers, and later web dashboard. This requires ADR validation.

## ADR index

- `ADR-0001: Repository and Phase 1 Application Architecture` - accepted on 2026-07-09.
