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
| Derived metrics imply medical certainty | high | medium | UX labeling, methodology notes, limitations |
| Premature dashboard work hides data quality issues | medium | high | Keep Phase 1 and Phase 2 focused on data foundation |
| Overengineering backend before data needs are known | medium | medium | Use ADRs and defer irreversible choices |
| Competitor formula or UI copying | high | low | Research public methods only and design original UX |
