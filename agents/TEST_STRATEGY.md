# Test Strategy

## Phase 0

- Documentation review against repository state.
- Ensure task list and current state stay aligned.

## Phase 1 - Local Apple Health Import

- Unit tests for archive/folder discovery and parser helpers.
- Streaming parser tests using synthetic XML fixtures only.
- Inventory aggregation tests for counts, date ranges, units, workouts, running workouts, and route-file presence.
- Idempotency tests for repeated inventory runs.
- Manual local validation with the founder's real export, recording only safe summaries.
- Confirm malformed or unknown records are reported without exposing sensitive payloads.

## Phase 2 - Local Data Model and Normalization

- Schema tests for raw and normalized model contracts.
- Unit conversion tests.
- Timezone and calendar boundary tests.
- Duplicate and overlapping-source tests.
- Synthetic fixture coverage for workouts, samples, sleep, and streams.

## Phase 3

- Idempotency tests.
- Retry and queue durability tests.
- Deletion/correction handling tests.
- Partial sync failure tests.

## Phase 4

- Workout reconstruction tests with synthetic streams.
- Alignment tests for samples with different timestamps and frequencies.
- Split-generation tests.
- Missing-data and confidence tests.

## Phase 6 - Native iOS HealthKit Automation

- Unit tests for HealthKit type catalog helpers where practical.
- Manual real-device verification for permissions and availability.
- Diagnostics using synthetic or redacted outputs only.
- Confirm denied permissions and unavailable data are handled explicitly.
