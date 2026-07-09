# Architecture

## Current architecture direction

ADR-0002 changes the implementation order to personal-local-first, market-ready architecture.

The first useful system should run entirely on the founder's Mac:

```text
Apple Watch
  -> Apple Health
  -> Manual Apple Health export
  -> Mac local import pipeline
  -> Local database
  -> Local API
  -> Next.js localhost dashboard
```

Immediate stack direction:

- Importer: Python.
- Parser: Python standard library streaming XML parsing first.
- Database: SQLite initially.
- Local API: Python.
- Dashboard: Next.js, React, TypeScript at `http://localhost:3000`.
- Infrastructure: no cloud, no Docker, no paid services, no App Store distribution, and no authentication for localhost personal use.

The architecture remains layered:

```text
Apple export format
  -> Importer
  -> Raw layer
  -> Normalizer
  -> Stable internal models
  -> Analytics
  -> API
  -> Web dashboard
```

The dashboard must not parse Apple export XML directly and must not couple itself to raw export structures.

## Deferred iOS automation

ADR-0001 accepts a structured monorepo without monorepo orchestration tooling during Phase 1.

Reserved repository layout:

```text
apps/
  ios/
    easyFitDiscovery/
  web/
services/
  api/
  analytics/
packages/
infrastructure/
fixtures/
  synthetic/
agents/
```

ADR-0001 remains valid for the later native iOS HealthKit discovery/synchronization path, but `apps/ios/easyFitDiscovery/` is no longer the immediate implementation step. The next implementation should create only the local import/dashboard pieces required for ADR-0002.

The likely long-term system remains:

```text
Apple Watch
  -> Apple Health / HealthKit
  -> Native iOS application
  -> Secure synchronization API
  -> Raw data layer
  -> Normalization layer
  -> Analytics layer
  -> Web dashboard
```

Probable long-term technologies:

- iOS: Swift, SwiftUI, HealthKit.
- Web: Next.js, React, TypeScript.
- Backend: Python.
- Analytics: Python.
- Database: PostgreSQL.
- Repository: monorepo.

These long-term technologies remain assumptions except where ADR-0001 and ADR-0002 explicitly decide near-term shape.

## iOS app decision from ADR-0001

- One native SwiftUI iOS app under `apps/ios/easyFitDiscovery/`.
- One app target and one unit test target.
- No watchOS target yet.
- No backend, web app, networking, authentication, or production sync.
- No third-party dependencies during Phase 1.
- Apple frameworks only: SwiftUI, HealthKit, Foundation, and OSLog.
- Minimum deployment target strategy: iOS 17.0 for Phase 1, built with stable Xcode 26 and an iOS 26 SDK or later when upload requirements matter.
- Local data handling: raw HealthKit query results in memory only; redacted diagnostic summary persistence only.
- Discovery scope: tiered HealthKit discovery, with foundational health/workout types first, running metrics/routes second, and optional categories deferred.
- Current status: deferred until after local import, local dashboard, and initial analytics milestones.

## Architectural constraints

- Raw data must preserve source fidelity.
- Normalization must be explicit, testable, and unit-aware.
- Derived metrics must be versioned and recalculable.
- Health data must not leak through logs, fixtures, telemetry, or Git.
- The first implementation should optimize for local Apple Health export import and safe data inventory.
- Technical identifiers should not be unnecessarily coupled to the public product name. Expensive-to-change identifiers require deliberate decisions when needed.

## Initial ADR candidates

- Repository architecture and Phase 1 app layout: decided in `decisions/ADR-0001-repository-and-phase-1-app-architecture.md`.
- Local analytics before native HealthKit synchronization: decided in `decisions/ADR-0002-local-analytics-first.md`.
- iOS data acquisition approach for production sync.
- Raw/normalized/derived data model boundary.
- Backend framework.
- Database and migration tooling.
- Synchronization architecture and idempotency model.

Do not create superficial ADRs. Record them when enough context exists to make a defensible decision.
