# Roadmap

The current strategy is personal-local-first, market-ready architecture. The founder needs useful local analytics quickly; commercial readiness remains a constraint but should not slow the first localhost product.

## Phase 0 - Foundation

Goal: Establish project memory, principles, architecture decisions, privacy rules, and first implementation plan.

Completed outcomes:

- Created and maintained `agents/`.
- Recorded product and engineering principles.
- Defined raw, normalized, and derived data architecture.
- Created risk register, open questions, task system, and ADR process.
- Accepted ADR-0001 for later native iOS HealthKit discovery.
- Accepted ADR-0002 for local analytics before native synchronization.

Exit criteria:

- Foundation docs exist and match repository state.
- Next implementation task is small, concrete, local, and privacy-safe.

## Phase 1 - Local Apple Health Import and Inventory

Goal: Import the founder's real Apple Health export locally and prove that the data can be safely parsed, inventoried, and prepared for localhost analytics.

Concrete outcomes:

- Keep the real export outside Git in an ignored private local path.
- Locate and stream-parse `export.xml`.
- Inventory record types, counts, date ranges, units, sources, workouts, running workouts, and route-file presence.
- Store safe local import state in SQLite only after the inventory parser is proven.
- Produce a safe local summary report with no raw samples, coordinates, full metadata dictionaries, or personal identifiers.

Exit criteria:

- A real export can be parsed locally without loading the whole XML into memory by default.
- Local inventory is deterministic across repeated runs.
- No real health data enters Git.

## Phase 2 - Local Data Model and Normalization

Goal: Create stable internal models from proven export structures.

Concrete outcomes:

- Define raw import tables.
- Define normalized models for core records, workouts, sleep, activity summaries, and running metrics proven present.
- Define unit, source, device, timezone, and deduplication rules.
- Create synthetic fixtures representing observed structures.

Exit criteria:

- The dashboard and analytics can use stable internal models instead of raw Apple export XML.
- Synthetic tests cover representative structures without using real data.

## Phase 3 - Localhost API and First Dashboard

Goal: Show useful personal health and training summaries at `http://localhost:3000`.

Concrete outcomes:

- Create local Python API.
- Create Next.js dashboard.
- Show overview, inventory, recent workouts, and only metrics proven available.
- Do not fabricate demo data in founder mode.

Exit criteria:

- Founder can run the local stack and view safe summaries from real data.
- Dashboard reads through API/domain models, not raw XML.

## Phase 4 - Workout Reconstruction and Analytics

Goal: Reconstruct real workouts and produce trustworthy early analytics.

Concrete outcomes:

- Reconstruct running workouts from normalized streams.
- Handle route-file presence without exposing coordinates by default.
- Generate basic splits and stream availability diagnostics.
- Begin transparent analytics for weekly volume, workout frequency, duration, and trends.

Exit criteria:

- At least one real run can be reconstructed with traceable source data and explicit missing-data handling.

## Phase 5 - Marathon Analytics

Goal: Support marathon preparation insights from proven data.

Concrete outcomes:

- Weekly running distance and consistency.
- Long-run progression.
- Workout frequency and duration.
- Recovery context using available HRV, resting heart rate, sleep, and VO2 max.
- Transparent limitations and confidence.

Exit criteria:

- Marathon-related insights are useful without unsupported claims or proprietary copied formulas.

## Phase 6 - Native iOS HealthKit Automatic Synchronization

Goal: Replace or complement manual export with native HealthKit access and automated local or backend synchronization.

Concrete outcomes:

- Resume ADR-0001 iOS path.
- Build native iOS HealthKit discovery/sync app.
- Add durable incremental sync, retries, idempotency, and deletion handling.

Exit criteria:

- Automated sync can reproduce the trusted local data model without corrupting raw, normalized, or derived layers.

## Phase 7 - Market and Production Infrastructure

Goal: Prepare for commercial release only after local value and data correctness are proven.

Concrete outcomes:

- Multi-user architecture.
- Production database and backend.
- Account deletion and export.
- Subscriptions if justified.
- App Store and TestFlight flows.
- Production observability and support runbooks.
