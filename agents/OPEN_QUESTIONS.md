# Open Questions

## Product

- How should the product phrase uncertainty so power users trust it without overwhelming casual users?

## Technical

- Which HealthKit types require special entitlements, route handling, or OS-version gating?
- How should raw HealthKit objects be serialized without losing source fidelity?
- What synthetic fixture format should represent workouts and streams before real data is stored?
- What exact structure does the founder's current Apple Health export contain?
- How should route GPX files be linked to `Workout` rows in the real export?
- Which malformed date, unknown element, or auxiliary file patterns appear in the founder's real export when Step 1A runs locally?
- Which Python local API framework should be used after the inventory milestone?
- Does the founder's real iPhone support the Phase 1 iOS 17.0 minimum deployment target?
- Which full Xcode version will be installed or selected for Phase 1 implementation?

## Data and analytics

- Which metrics are reliably available from Apple Watch during running workouts?
- How should overlapping sources be prioritized or represented?
- What confidence model should derived metrics use?
- Which training load methods are transparent, defensible, and non-proprietary?

## Privacy and operations

- What data is required for support debugging without exposing sensitive health details?
- What is the future account deletion and export model?
- Which third-party services, if any, are acceptable for analytics, crash reporting, and AI features?

These questions do not block the documentation bootstrap. Many should be answered through research or real-device testing instead of asking the founder prematurely.

## Resolved by ADR-0001

- Phase 1 diagnostics will use a tiered strategy: foundational health/workout types first, running metrics and routes second, optional categories later.
- The minimum useful local report is a redacted diagnostic summary with data-type states, counts, date ranges, units, safe source/device categories, and notes.
- Repository layout will be a structured monorepo with `apps/`, `services/`, `packages/`, `infrastructure/`, `fixtures/synthetic/`, and `agents/`.
- Phase 1 deployment target strategy is iOS 17.0 unless real founder-device testing proves this must change.
- Phase 1 will persist only a redacted local diagnostic summary, not raw HealthKit samples or route points.

## Resolved by ADR-0002

- The first useful product will be a Mac-local localhost dashboard, not a native iOS app.
- First real-data ingestion will use a manual Apple Health export.
- Native iOS HealthKit synchronization is deferred.
- The first local database recommendation is SQLite.
- The first importer and local API direction is Python.
- No cloud backend, App Store distribution, paid infrastructure, Docker, or authentication is required for the first local milestone.
- Step 1A is parser and safe inventory only; raw SQLite ingestion remains Step 1B, followed by Step 1C normalization/API/dashboard.
