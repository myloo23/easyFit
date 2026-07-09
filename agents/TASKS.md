# Tasks

Priority: P0 is highest.

## Phase 0 - Foundation

- [x] P0 Inspect repository contents and Git status.
- [x] P0 Create `agents/` memory structure.
- [x] P0 Populate project charter, vision, current state, roadmap, architecture, data architecture, privacy/security, risks, open questions, and task list.
- [x] P0 Create ADR template in `agents/decisions/README.md`.
- [x] P0 Review Phase 0 foundation for quality, naming consistency, and current-state accuracy.
- [x] P0 Create root `.gitignore` for expected stack, secrets, and local health-data protection.
- [x] P0 Record public GitHub repository visibility as a project risk.
- [x] P0 Research Apple HealthKit and current iOS platform requirements using primary sources.
- [x] P0 Draft ADR-0001 for repository architecture and Phase 1 app layout.
- [x] P1 Define Phase 1 HealthKit discovery scope and permission rationale.
- [x] P1 Create Phase 1 HealthKit Discovery specification.
- [x] P0 Record strategy pivot to local analytics before native HealthKit synchronization.
- [x] P0 Create ADR-0002 for local analytics first.
- [x] P0 Research Apple Health export format.
- [x] P0 Create Phase 1 Local Health Import specification.

## Phase 1 - Local Apple Health Import and Inventory

- [ ] P0 Review `.gitignore` protections before placing any real Apple Health export in the workspace.
- [ ] P0 Create ignored private local path for the founder's Apple Health export.
- [x] P0 Implement Python archive/folder locator for Apple Health export.
- [x] P0 Implement streaming parser for `export.xml`.
- [x] P0 Produce safe inventory report: total record count, record types, counts by type, date ranges, units, source categories, workout count, running workout count, and route-file presence.
- [x] P0 Ensure inventory report excludes raw samples, GPS coordinates, full metadata dictionaries, and personal identifiers.
- [x] P0 Add deterministic re-run behavior for the same export.
- [x] P1 Create synthetic fixture strategy based on representative structures, not real data.
- [ ] P0 Run Step 1A importer against the founder's real export after it is placed at `personal-health-data/export.zip`.
- [ ] P1 Add SQLite-backed local import state after the streaming inventory path is proven on real data.

## Phase 2 - Local Data Model and Normalization

- [ ] P0 Research raw HealthKit serialization strategy.
- [ ] P0 Draft raw model contract.
- [ ] P0 Draft normalized workout and sample model contracts.
- [ ] P1 Choose production database and migration tooling through later ADR.
- [ ] P1 Create synthetic fixture conventions.

## Phase 3 - Localhost API and First Dashboard

- [ ] P0 Create local Python API design after inventory exists.
- [ ] P0 Create Next.js localhost dashboard design after API shape exists.
- [ ] P0 Show only metrics proven available in the real export.
- [ ] P1 Define localhost dashboard runbook.

## Later - Reliable Synchronization

- [ ] P0 Design sync idempotency keys.
- [ ] P0 Design historical import and incremental sync strategy.
- [ ] P1 Define deletion and correction handling.
- [ ] P1 Define retry and durable queue behavior.

## Phase 4 - Workout Reconstruction

- [ ] P0 Reconstruct one synthetic run from normalized streams.
- [ ] P0 Reconstruct one real run locally after privacy review.
- [ ] P1 Document missing-data handling and stream confidence.

## Phase 6 - Native iOS HealthKit Automatic Synchronization

- [ ] P0 Prepare local iOS environment: install/select full Xcode, configure Apple Development signing, and connect a real iPhone.
- [ ] P0 Scaffold minimal native iOS app after ADR-0001.
- [ ] P0 Configure HealthKit capability and permission request flow.
- [ ] P0 Build availability inspection for prioritized HealthKit types.
- [ ] P0 Build diagnostics view for permissions, sample counts, sources, units, and date ranges.
- [ ] P0 Implement redacted local diagnostic summary persistence.
- [ ] P1 Add optional redacted export strategy for diagnostics if needed.
- [ ] P1 Update `HEALTHKIT_CATALOG.md` with real-device findings.
