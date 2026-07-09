# Data Architecture

The project conceptually separates data into raw, normalized, and derived layers.

## Raw layer

Purpose: preserve original source fidelity.

Examples:

- HealthKit samples.
- Workouts.
- Workout routes.
- Sleep segments.
- Source revisions.
- Device information.
- Metadata.

Rules:

- Do not silently modify raw data.
- Preserve source identifiers, timestamps, units, provenance, and metadata.
- Track import time separately from sample time.
- Account for deleted, corrected, and late-arriving data.

## Normalized layer

Purpose: provide stable internal domain models for product and analytics.

Examples:

- Heart rate.
- HRV.
- Resting heart rate.
- Sleep.
- Workouts.
- Running streams.
- Activity summaries.

Rules:

- Convert units deliberately and record canonical units.
- Keep source and confidence information.
- Handle duplicates and overlapping sources explicitly.
- Model timezone and calendar-day boundaries carefully.
- Make normalization deterministic and testable.

## Derived layer

Purpose: store calculated analytics.

Examples:

- Recovery indicators.
- Sleep quality analysis.
- Training load.
- Cardiac drift.
- Aerobic efficiency.
- Durability.
- Marathon readiness.
- Race predictions.
- Personal trends.

Rules:

- Version algorithms.
- Store input windows and dependencies.
- Support recalculation.
- Expose methodology, confidence, and limitations.
- Separate measured facts from estimates and recommendations.
