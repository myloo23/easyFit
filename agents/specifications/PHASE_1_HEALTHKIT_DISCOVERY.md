# Phase 1 HealthKit Discovery Specification

## Objective

Build a minimal native iOS app that runs on a real iPhone and discovers which justified HealthKit data types are available in the founder's actual Health store.

Phase 1 must produce knowledge for later data architecture. It is not the production easyFit app.

## Non-goals

- No production dashboard.
- No backend, web app, authentication, or sync.
- No watchOS target.
- No HealthKit writes.
- No raw data archive.
- No arbitrary recovery, readiness, load, or marathon score.
- No polished consumer UI requirement.

## User / Founder Workflow

1. Install and launch the internal discovery app on a real iPhone.
2. Read a concise explanation of why each tier of HealthKit data is requested.
3. Grant or deny HealthKit permissions.
4. Run discovery.
5. Review deterministic diagnostic states by data type and workout.
6. Optionally save or export a redacted summary that contains no raw samples, GPS coordinates, full metadata dictionaries, or personal identifiers.
7. Use the findings to update `HEALTHKIT_CATALOG.md` and later data architecture documents.

## Permission Strategy

- Request read access only.
- Do not request write access during Phase 1.
- Request permissions by justified tiers where practical.
- Explain product purpose before the system authorization sheet.
- Treat denied, unavailable, no-sample, query-failed, and query-success states separately.
- Do not imply that authorization success means data exists.

## Prioritized Data-Type Tiers

### Tier 1 - Foundation

- Heart rate.
- Resting heart rate.
- HRV SDNN.
- VO2 max.
- Respiratory rate.
- Sleep analysis.
- Active energy.
- Basal energy.
- Step count.
- Distance walking/running.
- Workouts.

Purpose: establish cardiovascular, recovery, sleep, activity, and workout context.

### Tier 2 - Running and Marathon

- Workout routes.
- Running speed.
- Running power.
- Running cadence.
- Running stride length.
- Running ground contact time.
- Running vertical oscillation.

Purpose: determine whether real workouts contain the streams needed for workout reconstruction, durability, cardiac drift, and marathon-specific analytics.

### Tier 3 - Later Optional Categories

- Flights climbed.
- Body mass.
- Other categories only after a documented product purpose exists.

Purpose: defer sensitive or lower-priority categories until justified.

## Diagnostic Information

For each data type, show:

- HealthKit identifier.
- Display name.
- Availability on current OS.
- Permission request inclusion.
- Query state.
- Error category, if any.
- Sample count.
- Earliest sample date.
- Latest sample date.
- Safe source names or source categories.
- Safe device categories where available.
- Unit.
- Notes.
- Privacy sensitivity.

Do not show raw sample values by default.

## Workout Discovery Requirements

For workouts, show:

- Total workout count.
- Running workout count.
- Activity type.
- Start and end dates.
- Duration.
- Distance if available.
- Safe source and device categories.
- Associated metric availability summary.
- Whether route objects are associated.

The default display should focus on recent representative workouts and aggregate counts, not exhaustive raw dumps.

## Route Discovery Requirements

- Detect whether workouts have associated route samples.
- Count route-capable workouts.
- Query route metadata only as needed to confirm availability.
- Do not display or log GPS coordinates by default.
- Do not persist route points in Phase 1.
- Represent route availability as a diagnostic state: unavailable, present-not-queried, query-success, query-failed, or permission-limited.

## Local Data Handling

- Keep raw HealthKit query results in memory only for the active diagnostic run.
- Persist only a redacted diagnostic summary locally.
- The summary may include counts, date ranges, units, data-type identifiers, query states, safe source categories, and notes.
- The summary must not include raw health samples, raw routes, GPS coordinates, full metadata dictionaries, personal identifiers, or credentials.
- Any exported summary must be reviewed before it is committed or copied into project docs.

## Logging Rules

May log:

- App lifecycle events.
- Authorization request started/completed.
- Data-type identifier.
- Query started/completed.
- Sample count.
- Error category and HealthKit error code category.
- Query duration.

Must not log:

- Raw heart-rate, HRV, sleep, respiratory, or workout streams.
- GPS coordinates.
- Detailed workout routes.
- Full metadata dictionaries.
- Personal identifiers.
- Precise location-derived route details.
- Secrets, credentials, signing data, or provisioning details.

Use `OSLog` with privacy-aware formatting.

## Error States

The UI must distinguish:

- Health data unavailable on device.
- HealthKit entitlement/capability missing.
- Permission not requested.
- Permission denied or limited.
- Data type unavailable on current OS.
- Query failed.
- Query succeeded with no samples.
- Query succeeded with samples.
- Route exists but route query failed.
- Environment not suitable for real-device discovery.

## Empty States

- No HealthKit availability: explain that real-device setup is required.
- No permission: show the data type as not authorized without blame.
- No samples: show "authorized or queryable, but no samples found" with date range empty.
- No workouts: show workout count zero and skip route assumptions.
- No running workouts: show total workouts separately from running workouts.
- No routes: show that routes were not found, not that routes are impossible.

## Real-Device Test Plan

1. Install/select full Xcode.
2. Configure Apple Development signing.
3. Connect or select a real iPhone that has Apple Health data.
4. Build and run the app on device.
5. Confirm HealthKit capability is present.
6. Complete the read-only permission flow.
7. Run Tier 1 diagnostics.
8. Run Tier 2 diagnostics.
9. Verify denied permissions and unavailable types are represented honestly.
10. Verify workouts can be counted.
11. Verify route availability can be detected without logging coordinates.
12. Save a redacted local summary and inspect it before using it in documentation.

## Acceptance Criteria

- The app launches on a real iPhone.
- HealthKit capability is configured for the app target.
- The app includes clear HealthKit read usage description text.
- The permission flow completes without crashing whether permissions are granted or denied.
- Each Tier 1 and Tier 2 type shows a deterministic diagnostic state.
- Unavailable types are shown honestly.
- Query errors are visible without exposing sensitive payloads.
- Sample count, earliest date, and latest date are shown when queryable.
- Real workouts can be counted.
- Running workouts can be counted separately.
- Route availability can be detected without logging or displaying GPS coordinates.
- The app does not write to HealthKit.
- The app does not use networking.
- The app does not require authentication.
- The app stores no raw health samples or route points.
- Unit-testable catalog and diagnostic-state logic has unit test coverage.
