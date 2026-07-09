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
- [ ] P0 Prepare local iOS environment: install/select full Xcode, configure Apple Development signing, and connect a real iPhone.

## Phase 1 - HealthKit Discovery

- [ ] P0 Scaffold minimal native iOS app after ADR-0001.
- [ ] P0 Configure HealthKit capability and permission request flow.
- [ ] P0 Build availability inspection for prioritized HealthKit types.
- [ ] P0 Build diagnostics view for permissions, sample counts, sources, units, and date ranges.
- [ ] P0 Implement redacted local diagnostic summary persistence.
- [ ] P1 Add optional redacted export strategy for diagnostics if needed.
- [ ] P1 Update `HEALTHKIT_CATALOG.md` with real-device findings.

## Phase 2 - Data Foundation

- [ ] P0 Research raw HealthKit serialization strategy.
- [ ] P0 Draft raw model contract.
- [ ] P0 Draft normalized workout and sample model contracts.
- [ ] P1 Choose database and migration tooling through ADR.
- [ ] P1 Create synthetic fixture conventions.

## Phase 3 - Reliable Synchronization

- [ ] P0 Design sync idempotency keys.
- [ ] P0 Design historical import and incremental sync strategy.
- [ ] P1 Define deletion and correction handling.
- [ ] P1 Define retry and durable queue behavior.

## Phase 4 - Workout Reconstruction

- [ ] P0 Reconstruct one synthetic run from normalized streams.
- [ ] P0 Reconstruct one real run locally after privacy review.
- [ ] P1 Document missing-data handling and stream confidence.
