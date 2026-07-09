# HealthKit Catalog

This catalog tracks HealthKit data types considered or investigated for easyFit.

Status values:

- `not investigated`
- `planned`
- `available`
- `unavailable`
- `partial`
- `implemented`

| User-facing name | Technical identifier | Unit | Availability | Expected source | Product purpose | Privacy sensitivity | Implementation status |
|---|---|---:|---|---|---|---|---|
| Heart rate | `HKQuantityTypeIdentifierHeartRate` | count/min | not investigated | Apple Watch | Effort, recovery context, workout streams | high | planned for Phase 1 |
| Resting heart rate | `HKQuantityTypeIdentifierRestingHeartRate` | count/min | not investigated | Apple Watch / Health | Recovery and trend context | high | planned for Phase 1 |
| Heart rate variability | `HKQuantityTypeIdentifierHeartRateVariabilitySDNN` | ms | not investigated | Apple Watch | Recovery trend signal | high | planned for Phase 1 |
| VO2 max | `HKQuantityTypeIdentifierVO2Max` | ml/(kg*min) | not investigated | Apple Watch / Health estimates | Aerobic fitness trend | high | planned for Phase 1 |
| Respiratory rate | `HKQuantityTypeIdentifierRespiratoryRate` | count/min | not investigated | Apple Watch | Recovery and sleep context | high | planned for Phase 1 |
| Sleep analysis | `HKCategoryTypeIdentifierSleepAnalysis` | category | not investigated | Apple Watch / sleep apps | Sleep duration, stages, consistency | high | planned for Phase 1 |
| Active energy | `HKQuantityTypeIdentifierActiveEnergyBurned` | kcal | not investigated | Apple Watch | Activity and load context | medium | planned for Phase 1 |
| Basal energy | `HKQuantityTypeIdentifierBasalEnergyBurned` | kcal | not investigated | Apple Watch / Health | Energy context | medium | planned for Phase 1 |
| Step count | `HKQuantityTypeIdentifierStepCount` | count | not investigated | iPhone / Apple Watch | Activity context | medium | planned for Phase 1 |
| Distance walking/running | `HKQuantityTypeIdentifierDistanceWalkingRunning` | m | not investigated | iPhone / Apple Watch | Volume context | medium | planned for Phase 1 |
| Workouts | `HKWorkoutType` | mixed | not investigated | Apple Watch / Fitness | Workout history and metadata | high | planned for Phase 1 |
| Workout routes | `HKSeriesType.workoutRoute()` | lat/lon stream | not investigated | Apple Watch | Route, elevation, run reconstruction | very high | planned for Phase 1 |
| Running speed | `HKQuantityTypeIdentifierRunningSpeed` | m/s | not investigated | Apple Watch | Running stream analysis | high | planned for Phase 1 |
| Running power | `HKQuantityTypeIdentifierRunningPower` | W | not investigated | Apple Watch | Load and durability analysis | high | planned for Phase 1 |
| Running cadence | `HKQuantityTypeIdentifierRunningCadence` | steps/min | not investigated | Apple Watch | Form and durability analysis | high | planned for Phase 1 |
| Stride length | `HKQuantityTypeIdentifierRunningStrideLength` | m | not investigated | Apple Watch | Form degradation analysis | high | planned for Phase 1 |
| Ground contact time | `HKQuantityTypeIdentifierRunningGroundContactTime` | ms | not investigated | Apple Watch | Running dynamics | high | planned for Phase 1 |
| Vertical oscillation | `HKQuantityTypeIdentifierRunningVerticalOscillation` | cm | not investigated | Apple Watch | Running dynamics | high | planned for Phase 1 |
| Flights climbed | `HKQuantityTypeIdentifierFlightsClimbed` | count | not investigated | iPhone / Apple Watch | Elevation context | low | backlog |
| Body mass | `HKQuantityTypeIdentifierBodyMass` | kg | not investigated | Health / scale | Fitness context and VO2/load interpretation | high | backlog |

Do not request or implement access without a clear product purpose.
