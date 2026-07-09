# Phase 1 iOS and HealthKit Architecture Research

Access date: 2026-07-09

## Research Questions

- What is required for a native iOS app to request HealthKit access?
- Which parts of Phase 1 require real-device testing?
- Is a watchOS target, backend, web app, networking, or local raw-data persistence required for HealthKit Discovery?
- What repository shape avoids early friction while preserving a path to iOS, web, API, analytics, infrastructure, and synthetic fixtures?
- What minimum iOS deployment target is reasonable for Phase 1?

## Environment Findings

- macOS: 26.5.1, build 25F80.
- Active developer directory: `/Library/Developer/CommandLineTools`.
- Xcode: not available through the active developer directory; `xcodebuild` reports Command Line Tools are selected instead of full Xcode.
- Swift: Apple Swift 6.3.2, target `arm64-apple-macosx26.0`.
- iOS SDK: not discoverable locally because full Xcode is not selected.
- Simulator runtimes: not discoverable locally because full Xcode tooling is unavailable through the active developer directory.
- Apple Development signing identity: none detected in the login keychain summary.
- Connected iPhone: none detected over USB by the local system profiler check.
- Git: 2.50.1 (Apple Git-155).

Architecture-relevant consequence: Phase 1 implementation requires full Xcode installation/selection, an Apple Development signing setup, and a connected or otherwise deployable iPhone before real HealthKit discovery can be validated.

## Primary Sources Consulted

### Setting up HealthKit

- Title: Setting up HealthKit
- Official source: Apple Developer Documentation
- URL: https://developer.apple.com/documentation/healthkit/setting-up-healthkit
- Relevant finding: A HealthKit app must enable the HealthKit capability in Xcode. Apple also documents HealthKit-related Info.plist usage-description keys.

### Authorizing access to health data

- Title: Authorizing access to health data
- Official source: Apple Developer Documentation
- URL: https://developer.apple.com/documentation/healthkit/authorizing-access-to-health-data
- Relevant finding: HealthKit authorization is fine-grained. Apps request access to specific data types before using them.

### HKHealthStore requestAuthorization

- Title: `requestAuthorization(toShare:read:completion:)`
- Official source: Apple Developer Documentation
- URL: https://developer.apple.com/documentation/healthkit/hkhealthstore/requestauthorization%28toshare%3Aread%3Acompletion%3A%29
- Relevant finding: Read and share permissions are separate. A single request can include all data types the app needs.

### NSHealthShareUsageDescription

- Title: `NSHealthShareUsageDescription`
- Official source: Apple Developer Documentation
- URL: https://developer.apple.com/documentation/bundleresources/information-property-list/nshealthshareusagedescription
- Relevant finding: Apps need a user-facing explanation for reading samples from the HealthKit store.

### HealthKit Entitlement

- Title: HealthKit Entitlement
- Official source: Apple Developer Documentation
- URL: https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.healthkit
- Relevant finding: The HealthKit entitlement controls whether the app may request authorization to access health and activity data.

### HKWorkoutRouteQuery

- Title: `HKWorkoutRouteQuery`
- Official source: Apple Developer Documentation
- URL: https://developer.apple.com/documentation/healthkit/hkworkoutroutequery
- Relevant finding: Workout route queries access location data associated with `HKWorkoutRoute`; route samples can contain many `CLLocation` values. Phase 1 must detect route availability without logging coordinates by default.

### Running quantity type identifiers

- Title: `HKQuantityTypeIdentifier` running metrics
- Official source: Apple Developer Documentation
- URLs:
  - https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/runningspeed
  - https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/runningpower
  - https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/runningstridelength
  - https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/runninggroundcontacttime
  - https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/runningverticaloscillation
- Relevant finding: Running-specific quantity identifiers exist and several are documented with iOS 16.0+ availability. Actual sample availability still depends on device, OS, source, and workouts.

### Health and fitness apps

- Title: Health and fitness apps
- Official source: Apple Developer
- URL: https://developer.apple.com/health-fitness/
- Relevant finding: Apple positions HealthKit as a central repository for health and fitness data across Apple platforms, with user permission and privacy control.

### App Review Guidelines

- Title: App Review Guidelines, Health and Health Research
- Official source: Apple Developer
- URL: https://developer.apple.com/app-store/review/guidelines/
- Relevant finding: Apple treats health, fitness, and medical data as especially sensitive. HealthKit data must not be used for advertising, marketing, or other use-based data mining, except for permitted health-management or research purposes with permission. Apps must not write false or inaccurate data to HealthKit.

### Xcode SDK and system requirements

- Title: SDK and system requirements
- Official source: Apple Developer
- URL: https://developer.apple.com/xcode/system-requirements/
- Relevant finding: Current Xcode 26 releases support iOS SDK 26.x and deployment targets down to iOS 15. Xcode 27 beta supports iOS SDK 27 and deployment targets down to iOS 15, but should not be the default for this project.

### SDK minimum requirements

- Title: SDK minimum requirements
- Official source: Apple Developer News / Upcoming Requirements
- URL: https://developer.apple.com/news/upcoming-requirements/?id=02032026a
- Relevant finding: Since 2026-04-28, apps uploaded to App Store Connect must be built with Xcode 26 or later using an iOS 26 SDK or later. This is an upload SDK requirement, not the same thing as the app's minimum deployment target.

## Confirmed Facts

- Confirmed by Apple documentation: HealthKit requires app capability/entitlement setup and user-facing privacy usage descriptions.
- Confirmed by Apple documentation: HealthKit authorization is per data type and distinguishes read and share permissions.
- Confirmed by Apple documentation: workout routes are location data and require careful handling.
- Confirmed by Apple documentation: running-specific HealthKit quantity types exist; several relevant running metrics are iOS 16.0+ APIs.
- Confirmed locally: the current machine is not yet ready to build/sign/run an iOS HealthKit app because full Xcode is not selected, no Apple Development identity was detected, and no iPhone was detected.
- Confirmed by Apple platform requirements: App Store uploads currently require Xcode 26 or later with an iOS 26 SDK or later; deployment target may be lower.

## Architectural Consequences

- Phase 1 should be a native iOS app because HealthKit discovery must happen on Apple platforms with user permission.
- A watchOS target is not required to read existing HealthKit data from the iPhone Health store for discovery. It may become useful later for recording workouts or watch-first experiences.
- No backend, web app, authentication, or production sync is required for Phase 1 because the goal is local discovery and knowledge capture.
- The Phase 1 app should request read access only for justified discovery types. It should not write to HealthKit.
- The default diagnostic UI/logs must never show raw sample streams, full metadata dictionaries, or GPS coordinates.
- Repository structure should reserve space for future apps/services/packages without introducing monorepo orchestration tooling.
- Minimum deployment target should be set separately from the development SDK. Phase 1 should target iOS 17.0 minimum unless real founder-device testing shows the founder device requires a different target.

## Unknowns Requiring Real-Device Testing

- Whether HealthKit data is available and authorized on the founder's actual iPhone.
- Which Apple Watch and Apple Health sources exist in the Health store.
- Whether historical samples exist for each prioritized type.
- Whether running speed, power, cadence, stride length, ground contact time, and vertical oscillation exist for the founder's real workouts.
- Whether workout routes are available for real runs and can be associated with `HKWorkout` records.
- Whether simulator behavior is useful for anything beyond UI and permission-flow smoke testing.

## Risks

- Full Xcode, signing, and real-device deployment are not currently available locally.
- Requesting too many HealthKit permissions at once can undermine trust.
- Treating "authorization request completed" as "data available" would be incorrect.
- Route diagnostics can easily leak precise location data if logs or exports are careless.
- Setting the deployment target too low adds legacy complexity; setting it too high may unnecessarily exclude the founder's device or future users.

## Recommendation

Use a structured monorepo with no orchestration tooling during Phase 1:

```text
apps/ios/easyFitDiscovery/
apps/web/
services/api/
services/analytics/
packages/
infrastructure/
fixtures/synthetic/
agents/
```

For Phase 1, create one native SwiftUI iOS app under `apps/ios/easyFitDiscovery/`, with one app target and one unit test target. Do not create a watchOS target, backend, web app, authentication, networking, production sync, or third-party dependencies. Use Apple frameworks only: SwiftUI, HealthKit, Foundation, and OSLog.

Use a tiered HealthKit discovery strategy:

- Tier 1: foundational cardiovascular, sleep, activity, and workouts.
- Tier 2: running-specific workout metrics and route detection.
- Tier 3: optional categories deferred until justified.

Use local redacted summary persistence only. Do not persist raw samples, raw routes, GPS coordinates, or complete metadata dictionaries.
