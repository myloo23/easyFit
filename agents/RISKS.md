# Risks

| Risk | Impact | Likelihood | Mitigation |
|---|---:|---:|---|
| HealthKit data unavailable or incomplete on founder devices | high | medium | Discover on real device before designing analytics |
| Running dynamics unavailable for many workouts | medium | medium | Treat as optional inputs with explicit confidence |
| Raw data accidentally mutated during import | high | medium | Separate raw storage and normalization |
| Duplicate or late-arriving samples corrupt trends | high | high | Design idempotency, source tracking, and recalculation early |
| Timezone and calendar boundaries distort sleep/training summaries | high | medium | Model timezone explicitly and test boundary cases |
| Sensitive health data committed or logged | very high | medium | Git ignores, redaction, local-only diagnostics, security review |
| Public GitHub repository exposes committed source and documentation | high | medium | Keep secrets and health data out of Git; revisit repository visibility as a founder/product decision |
| Local machine not ready for iOS development | high | high | Install/select full Xcode, configure Apple Development signing, and test on a real iPhone before implementation claims |
| Route diagnostics leak precise location data | very high | medium | Detect route availability without logging, displaying, exporting, or persisting GPS coordinates by default |
| Real Apple Health export accidentally committed | very high | medium | Keep exports in ignored private paths; audit before commits; never use real exports as fixtures |
| Large Apple Health export exhausts memory | high | medium | Use streaming XML parsing and batched local writes; avoid whole-file parsing by default |
| Step 1A parser passes synthetic fixtures but fails on real export variation | high | medium | Validate against the founder's ignored real export before designing SQLite ingestion, normalization, API, or dashboard |
| Manual export workflow becomes stale or inconvenient | medium | high | Use it for fast local value, then add native iOS synchronization later |
| Dashboard couples to raw Apple export XML | high | medium | Keep importer, raw layer, normalizer, API, and dashboard boundaries separate |
| Derived metrics imply medical certainty | high | medium | UX labeling, methodology notes, limitations |
| Premature dashboard work hides data quality issues | medium | high | Keep Phase 1 and Phase 2 focused on data foundation |
| Overengineering backend before data needs are known | medium | medium | Use ADRs and defer irreversible choices |
| Competitor formula or UI copying | high | low | Research public methods only and design original UX |
