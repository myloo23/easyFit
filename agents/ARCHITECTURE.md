# Architecture

## Starting hypothesis

The likely long-term system is:

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

Probable technologies:

- iOS: Swift, SwiftUI, HealthKit.
- Web: Next.js, React, TypeScript.
- Backend: Python.
- Analytics: Python.
- Database: PostgreSQL.
- Repository: monorepo.

These are starting assumptions, not final decisions.

## Architectural constraints

- Raw data must preserve source fidelity.
- Normalization must be explicit, testable, and unit-aware.
- Derived metrics must be versioned and recalculable.
- Health data must not leak through logs, fixtures, telemetry, or Git.
- The first implementation should optimize for real-device HealthKit discovery.
- Technical identifiers should not be unnecessarily coupled to the public product name. Expensive-to-change identifiers require deliberate decisions when needed.

## Initial ADR candidates

- Repository architecture and package layout.
- iOS data acquisition approach.
- Raw/normalized/derived data model boundary.
- Backend framework.
- Database and migration tooling.
- Synchronization architecture and idempotency model.

Do not create superficial ADRs. Record them when enough context exists to make a defensible decision.
