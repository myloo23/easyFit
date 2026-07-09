# Phase 1 Local Health Import Specification

## Objective

Import the founder's real Apple Health export locally and prove that the data can be safely parsed, inventoried, and prepared for localhost analytics.

The first milestone is `LOCAL HEALTH DATA INVENTORY`, not deep analytics or a final dashboard.

## Non-goals

- No cloud upload.
- No App Store distribution.
- No native iOS app implementation.
- No production synchronization.
- No authentication.
- No final dashboard.
- No deep analytics or predictions.
- No real health data committed to Git.
- No GPS route data committed to Git.

## Input

- A manually generated Apple Health export archive from the founder's iPhone.
- Expected but not guaranteed contents:
  - `export.xml`
  - possible `export_cda.xml`
  - possible `workout-routes/` GPX files
  - possible ECG or clinical-record files

The real founder export is the implementation source of truth.

## Privacy Requirements

- Keep the export in an ignored private local directory, such as `AppleHealthExport/`, `apple_health_export/`, `health-export/`, or `personal-health-data/`.
- Never copy the export into `fixtures/`.
- Never commit `export.xml`, `export_cda.xml`, GPX route files, local database files, or raw diagnostic dumps.
- Never paste raw samples, exact GPS coordinates, or full metadata dictionaries into documentation.
- Inventory reports may contain only safe summaries.
- Local services should bind to localhost by default.

## Import Workflow

1. Place the Apple Health export archive or extracted folder in an ignored private local path.
2. Validate archive/folder structure.
3. Locate `export.xml`.
4. Stream-parse `export.xml`.
5. Produce a local raw inventory and safe summary report.
6. Store raw import records in a local ignored database only after the inventory parser is proven.
7. Normalize a narrow set of proven record types in later milestones.
8. Update project catalogs from safe summaries only.

## Data Inventory Requirements

The first report must include:

- Total record count.
- Record types.
- Counts by type.
- Earliest date by type.
- Latest date by type.
- Units encountered by type.
- Safe source categories or source names where acceptable.
- Workout count.
- Running workout count.
- Overall date range.
- Activity summary count if present.
- Route file count if present.
- Unknown top-level element types.
- Parse warnings and skipped malformed records.

The first report must not include raw values, full timestamps for individual sensitive events, coordinates, route traces, or full metadata dictionaries.

## Raw Storage Strategy

- Use SQLite for the first local inventory milestone.
- Store local database files under ignored private paths.
- Preserve enough raw source fidelity to re-run normalization deterministically.
- Keep import batch metadata: file path hash or stable local file identity, import time, parser version, source export size, and counts.
- Avoid schema choices that prevent later PostgreSQL migration.

## Parsing Strategy

- Prefer Python standard library first.
- Use `zipfile` for archive handling if importing directly from `.zip`.
- Use streaming XML parsing, such as `xml.etree.ElementTree.iterparse`, for `export.xml`.
- Clear parsed XML elements as streaming progresses to bound memory use.
- Parse dates as timezone-aware values.
- Treat units as source data and document canonical conversions later.
- Treat `sourceName`, `sourceVersion`, and `device` as provenance strings, not stable identity.

## Large-File Handling

- Do not load the whole XML file into memory by default.
- Report progress by bytes read or records processed where practical.
- Make the import interruptible without corrupting committed local state.
- Use batched SQLite writes.
- Log counts and error categories, not raw records.
- Support repeated imports deterministically.

## Error Handling

- Missing archive or export folder.
- Missing `export.xml`.
- Unexpected folder layout.
- XML parse errors.
- Unsupported or unknown element types.
- Missing expected attributes.
- Invalid dates.
- Unknown units.
- SQLite write failures.
- Interrupted import.

Errors must be visible and actionable without exposing sensitive payloads.

## Idempotency Expectations

- Re-importing the same export should not duplicate inventory rows.
- Import batches should have stable identifiers.
- Raw records should have deterministic local keys based on source attributes and import context where Apple does not provide stable IDs.
- The first milestone may start with inventory idempotency before full raw-record idempotency.

## Real-Data Validation

Validation uses the founder's real export locally, but only safe summaries may be recorded in project docs.

Validation should answer:

- Can the export be found and opened?
- How large is `export.xml`?
- Which top-level element families exist?
- How many `Record`, `Workout`, and `ActivitySummary` entries exist?
- Which HealthKit record types are present?
- Which units appear?
- What is the safe aggregate date range?
- Are running workouts present?
- Are route files present?
- Are parse errors or malformed entries present?

## Acceptance Criteria

- A real Apple Health export can be placed in an ignored local path.
- The importer can locate `export.xml`.
- The importer streams the XML rather than loading the full file by default.
- The importer produces total record count.
- The importer produces counts by record type.
- The importer produces earliest and latest dates by record type.
- The importer reports units encountered by record type.
- The importer counts workouts and running workouts.
- The importer detects whether route files are present without reading or printing coordinates.
- The importer handles unknown record types without crashing.
- The importer writes no real health data to tracked repository files.
- The safe inventory report contains no raw samples, GPS coordinates, or full metadata dictionaries.
- Re-running the inventory on the same export is deterministic.
