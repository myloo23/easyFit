# Open Questions

## Product

- Which first user workflow should Phase 1 diagnostics optimize for: all HealthKit availability, running-focused availability, or marathon-preparation availability?
- What is the minimum useful local report from the iOS discovery app?
- How should the product phrase uncertainty so power users trust it without overwhelming casual users?

## Technical

- What monorepo layout best supports Swift/iOS, Python backend/analytics, and later Next.js without adding unnecessary complexity?
- What iOS deployment target is appropriate for the founder's device and likely market?
- Which HealthKit types require special entitlements, route handling, or OS-version gating?
- How should raw HealthKit objects be serialized without losing source fidelity?
- What synthetic fixture format should represent workouts and streams before real data is stored?
- Should Phase 1 persist diagnostics locally, export a redacted report, or only render in-app?

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
