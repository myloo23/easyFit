# Test Strategy

## Phase 0

- Documentation review against repository state.
- Ensure task list and current state stay aligned.

## Phase 1

- Unit tests for HealthKit type catalog helpers where practical.
- Manual real-device verification for permissions and availability.
- Diagnostics using synthetic or redacted outputs only.
- Confirm denied permissions and unavailable data are handled explicitly.

## Phase 2

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
