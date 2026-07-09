# ADR-0001: Repository and Phase 1 Application Architecture

Status: Accepted
Date: 2026-07-09

## Context

easyFit is in Phase 0 and is preparing for Phase 1: HealthKit Discovery. The first implementation must answer what Apple Health data is actually available from the founder's real devices. It must not become the production app, dashboard, backend, or analytics platform yet.

Research in `agents/research/2026-07-09-phase-1-ios-healthkit-architecture.md` confirmed that HealthKit requires native Apple platform capability/entitlement setup, user authorization, privacy usage descriptions, and careful handling of sensitive health and route data. Local environment inspection also found that full Xcode is not currently selected, no Apple Development signing identity was detected, and no iPhone was detected, so implementation requires environment setup before real-device validation.

## Decision

Use a structured monorepo without monorepo orchestration tooling during Phase 1.

Reserved repository layout:

```text
easyFit/
├── apps/
│   ├── ios/
│   │   └── easyFitDiscovery/
│   └── web/
├── services/
│   ├── api/
│   └── analytics/
├── packages/
├── infrastructure/
├── fixtures/
│   └── synthetic/
└── agents/
```

Only `apps/ios/easyFitDiscovery/` should be created during the next implementation step. Other folders are architectural reservations and should be created only when useful.

Phase 1 app shape:

- Location: `apps/ios/easyFitDiscovery/`.
- Xcode project location: `apps/ios/easyFitDiscovery/easyFitDiscovery.xcodeproj`.
- Product role: internal HealthKit Discovery app, not the production consumer app.
- Application targets: one native iOS app target.
- Test targets: one unit test target from the beginning.
- UI test target: not created initially.
- watchOS target: excluded for Phase 1.
- Backend: excluded for Phase 1.
- Web app: excluded for Phase 1.
- Networking and authentication: excluded for Phase 1.
- Swift Package Manager modularization: excluded initially.
- Local persistence: redacted local diagnostic summary only; no raw HealthKit samples, full metadata dictionaries, GPS coordinates, or route point streams.
- Third-party dependencies: none during Phase 1 unless a later decision demonstrates a concrete need.
- Apple frameworks: SwiftUI, HealthKit, Foundation, and OSLog.
- Minimum deployment target: iOS 17.0 for Phase 1, built with the current stable Xcode 26 toolchain and iOS 26 SDK or later when App Store/TestFlight upload becomes relevant.

Phase 1 discovery scope uses a tiered strategy:

- Tier 1: foundational cardiovascular, sleep, activity, and workout data.
- Tier 2: running-specific workout metrics and route availability.
- Tier 3: optional health categories deferred until justified.

## Alternatives Considered

### Flat repository

```text
ios/
web/
api/
analytics/
```

This is simple, but it loses useful separation between applications, services, shared packages, infrastructure, fixtures, and project memory as the product grows.

### Structured monorepo

Chosen. It keeps near-term development simple while reserving clear homes for future iOS, web, API, analytics, shared contracts, infrastructure, and synthetic fixtures. It does not require Nx, Turborepo, Bazel, or other orchestration tooling during Phase 1.

### Separate repositories

Separate repositories could improve security boundaries and team ownership later, but they add coordination overhead too early. The project currently needs fast local architecture learning and shared documentation more than repository isolation.

### Broad HealthKit inventory

Rejected for Phase 1 because it would increase permission surface and privacy burden before product purpose is clear.

### Running-only HealthKit inventory

Rejected for Phase 1 because marathon analytics depend on recovery, sleep, cardiovascular baselines, activity context, workouts, and routes, not just running streams.

### Memory-only diagnostics

Rejected because it weakens reproducibility and makes it harder to compare discovery runs.

### Persisted raw diagnostics

Rejected because it creates unnecessary privacy risk and resembles premature raw-data archive design.

## Benefits

- Keeps Phase 1 focused on learning from real HealthKit data.
- Avoids premature backend, web, authentication, watchOS, and synchronization work.
- Preserves future paths for multi-user backend, web dashboard, analytics, infrastructure, and synthetic fixtures.
- Keeps HealthKit permission requests more explainable through tiering.
- Reduces privacy risk by forbidding raw sample and route persistence in Phase 1.
- Starts unit-test coverage where catalog, authorization mapping, and diagnostic state logic can be tested without real health data.

## Trade-offs

- The structured monorepo creates reserved concepts before all code exists.
- Excluding watchOS means Phase 1 discovers existing Health data but does not test watch-first workout recording.
- Excluding backend sync means Phase 1 will not validate production ingestion, idempotency, or deletion handling.
- Excluding UI tests saves setup effort but leaves full interaction coverage manual initially.
- Redacted summary persistence requires care to avoid accidentally storing sensitive details.

## Privacy Impact

Positive. The decision minimizes data movement and rejects backend sync, raw exports, GPS-coordinate logging, and raw sample persistence during Phase 1.

The app must request only read access for justified HealthKit types. It must not write to HealthKit in Phase 1. Diagnostic output must show counts, ranges, source categories, device categories, units, and states, but not raw sample streams, full metadata dictionaries, personal identifiers, or coordinates.

## Security Impact

Positive. No networking, authentication, backend, or cloud resources are introduced. The main risks are local logs and local diagnostic summaries, which must remain redacted and protected by repository ignore policy.

## Scalability Impact

The monorepo layout supports future growth into iOS, web, API, analytics, shared packages, infrastructure, and synthetic fixtures without deciding production backend, database, cloud provider, or CI orchestration now.

## Reversal Strategy

- Repository layout can be changed before substantial code accumulates.
- If Phase 1 shows a watchOS target is necessary, add it through a new ADR or decision-log entry.
- If redacted summary persistence proves risky or unnecessary, remove it before production.
- If iOS 17.0 excludes the founder's actual test device, revise the deployment target before scaffolding or in the implementation commit.
