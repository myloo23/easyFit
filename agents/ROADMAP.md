# Roadmap

## Phase 0 - Foundation

Goal: Establish project memory, principles, and first technical direction.

Concrete outcomes:

- Create and maintain `agents/`.
- Record product and engineering principles.
- Define initial raw, normalized, and derived data architecture.
- Start risk register, open questions, and task system.
- Decide initial repository architecture through ADR.

Exit criteria:

- Foundation docs exist and match repository state.
- Next implementation task is small, concrete, and justified.

## Phase 1 - HealthKit Discovery

Goal: Build a minimal native iOS app that runs on the founder's real iPhone and discovers available HealthKit data.

Concrete outcomes:

- Configure a minimal Swift/SwiftUI app with HealthKit entitlement.
- Request only permissions tied to real product purposes.
- Inspect real available data categories from the founder's device.
- Produce diagnostics for availability, permissions, sample counts, source devices, units, date ranges, and representative metadata.
- Update `HEALTHKIT_CATALOG.md` with actual findings.

Exit criteria:

- The app can run on device.
- Discovery output is sufficient to design the raw data model.
- No real health export is committed to Git.

## Phase 2 - Data Foundation

Goal: Design raw and normalized domain models plus storage contracts.

Concrete outcomes:

- Define raw HealthKit payload preservation strategy.
- Define normalized models for workouts, samples, sleep, activity summaries, and running streams.
- Choose database and migration tooling.
- Define unit, source, device, timezone, deletion, and deduplication rules.
- Create test fixtures using synthetic or anonymized data only.

Exit criteria:

- Raw and normalized schema decisions are recorded.
- Recalculation and algorithm versioning requirements are documented.

## Phase 3 - Reliable Synchronization

Goal: Implement durable and idempotent data movement from iOS to backend storage.

Concrete outcomes:

- Historical import.
- Incremental sync.
- Durable local queue.
- Retry behavior.
- Idempotency keys.
- Deletion and correction handling.
- Structured sync diagnostics.

Exit criteria:

- Re-running sync does not duplicate or silently mutate data.
- Failures are observable and recoverable.

## Phase 4 - Workout Reconstruction

Goal: Reliably reconstruct one real run end to end.

Concrete outcomes:

- Import workout metadata.
- Align heart rate, route, pace/speed, cadence, power, elevation, and available running dynamics streams.
- Generate splits and stream diagnostics.
- Document gaps, confidence, and source limitations.

Exit criteria:

- One real run can be reconstructed with traceable raw inputs and normalized outputs.
- Known missing data is explicit.

## Later phases

- Analytics research and versioned derived metrics.
- Web dashboard and product workflows.
- Multi-user account model.
- Data export and deletion workflows.
- Subscription and App Store readiness.
- Production observability and support tooling.
