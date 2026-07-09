# ADR-0002: Local Analytics Before Native HealthKit Synchronization

Status: Accepted
Date: 2026-07-09

## Context

The founder's highest-priority outcome has been clarified: open a localhost dashboard on the Mac and understand real Apple Health and Apple Watch data as quickly as possible.

ADR-0001 remains historically valid for the later native iOS HealthKit Discovery and synchronization path. However, starting with iOS is no longer the fastest path to founder value because the local development environment is not yet ready for real-device HealthKit work and the founder can manually export Apple Health data now.

The project should now optimize for a personal-local-first product while preserving a market-ready architecture.

## Decision

The first useful product will run entirely on the founder's Mac.

Initial implementation sequence:

```text
Apple Watch
  -> Apple Health
  -> Manual Apple Health export
  -> Mac local import pipeline
  -> Local database
  -> Local API
  -> Next.js localhost dashboard
  -> Analytics
  -> Native iOS automatic synchronization later
```

Explicit decisions:

- The first user-visible product is a localhost web dashboard at `http://localhost:3000`.
- First real-data ingestion uses a manual Apple Health export.
- Native iOS HealthKit sync is deferred.
- No cloud backend is required for the first useful product.
- No App Store distribution is required for the first useful product.
- No paid infrastructure is required for the first useful product.
- No authentication is required for localhost personal use.
- The architecture must preserve a later automated native iOS HealthKit sync path.
- The raw, normalized, and derived data layers remain mandatory.
- The dashboard must consume stable API/domain models, not parse Apple export XML directly.

Recommended first local stack:

- Importer: Python.
- Parser: Python standard library streaming XML parsing first.
- Database: SQLite initially.
- Local API: Python.
- Dashboard: Next.js, React, TypeScript, localhost on port 3000.
- Infrastructure: no Docker unless a later implementation step proves immediate value.

## Alternatives Considered

### Native iOS HealthKit app first

This was accepted in ADR-0001 as the first implementation path. It remains useful for later automated synchronization and HealthKit authorization learning, but it requires Xcode, signing, and real-device setup before data can be explored.

### Local Apple Health export first

Chosen. Manual export is less convenient, but it enables immediate progress on ingestion, inventory, data modeling, normalization, workout reconstruction, analytics, and dashboard UX using the founder's real data locally.

### Cloud backend first

Rejected. It adds cost, security exposure, deployment work, account concerns, and privacy review before the founder has local value.

### PostgreSQL first

Deferred. PostgreSQL is likely relevant for future multi-user production, but SQLite is faster for the first local inventory because it is local, portable, requires no server, and works well for deterministic import experiments. The schema design should avoid SQLite-specific assumptions that would block a later PostgreSQL migration.

## Benefits

- Gets real founder data visible faster.
- Avoids App Store, signing, TestFlight, and device-deployment blockers.
- Avoids cloud cost and infrastructure overhead.
- Lets the team learn the real Apple Health export shape before designing production sync.
- Enables early dashboard UX and analytics iteration.
- Keeps all real personal health data local.

## Trade-offs

- Manual export is inconvenient and not a long-term synchronization solution.
- Apple Health exports may be large and inconsistent across OS versions and data sources.
- Export files can contain highly sensitive health and GPS route data.
- SQLite is not the final production multi-user database.
- Localhost personal workflows do not validate future account, sync, or deletion flows.

## Privacy Impact

Positive if handled correctly. The founder's real data remains local and does not require cloud upload.

Strict constraints:

- Never commit Apple Health exports.
- Never commit GPS route files.
- Never paste raw health samples into documentation.
- Never copy real exports into `fixtures/`.
- Use synthetic fixtures later for source-controlled tests.
- First reports must contain safe summaries only: counts, type names, date ranges, units, source categories, and workout counts.

## Security Impact

The first useful system avoids cloud exposure and authentication complexity. The main risks shift to local file handling, accidental Git commits, local database storage, and localhost process exposure.

Mitigations:

- Keep real exports under ignored private local paths.
- Keep local database files ignored.
- Do not bind local services to public interfaces by default.
- Do not log raw samples, coordinates, or full metadata dictionaries.

## Scalability Impact

The approach prioritizes fast local learning over production scale. The three-layer data model, stable API boundary, and structured repository preserve a later path to PostgreSQL, cloud deployment, multi-user accounts, and native iOS synchronization.

## Reversal Strategy

- If manual export is too incomplete or unreliable, resume the ADR-0001 native iOS path earlier.
- If SQLite becomes limiting, migrate raw/normalized schemas to PostgreSQL after the first inventory milestone.
- If the local dashboard proves valuable, promote it toward a production web app once privacy, account, sync, and infrastructure decisions are made.
