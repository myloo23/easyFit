# Architecture

## Current architecture direction

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

Only `apps/ios/easyFitDiscovery/` should be created during the next implementation step. Other folders are architectural reservations and should be created only when useful.

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

These long-term technologies remain assumptions except where ADR-0001 explicitly decides the Phase 1 native iOS app shape.

## Phase 1 app decision

- One native SwiftUI iOS app under `apps/ios/easyFitDiscovery/`.
- One app target and one unit test target.
- No watchOS target yet.
- No backend, web app, networking, authentication, or production sync.
- No third-party dependencies during Phase 1.
- Apple frameworks only: SwiftUI, HealthKit, Foundation, and OSLog.
- Minimum deployment target strategy: iOS 17.0 for Phase 1, built with stable Xcode 26 and an iOS 26 SDK or later when upload requirements matter.
- Local data handling: raw HealthKit query results in memory only; redacted diagnostic summary persistence only.
- Discovery scope: tiered HealthKit discovery, with foundational health/workout types first, running metrics/routes second, and optional categories deferred.

## Architectural constraints

- Raw data must preserve source fidelity.
- Normalization must be explicit, testable, and unit-aware.
- Derived metrics must be versioned and recalculable.
- Health data must not leak through logs, fixtures, telemetry, or Git.
- The first implementation should optimize for real-device HealthKit discovery.
- Technical identifiers should not be unnecessarily coupled to the public product name. Expensive-to-change identifiers require deliberate decisions when needed.

## Initial ADR candidates

- Repository architecture and Phase 1 app layout: decided in `decisions/ADR-0001-repository-and-phase-1-app-architecture.md`.
- iOS data acquisition approach for production sync.
- Raw/normalized/derived data model boundary.
- Backend framework.
- Database and migration tooling.
- Synchronization architecture and idempotency model.

Do not create superficial ADRs. Record them when enough context exists to make a defensible decision.
