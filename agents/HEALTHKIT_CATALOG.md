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
| Heart rate | `HKQuantityTypeIdentifierHeartRate` | count/min | not investigated | Apple Watch | Effort, recovery context, workout streams | high | inspect via export in Phase 1; native HealthKit deferred |
| Resting heart rate | `HKQuantityTypeIdentifierRestingHeartRate` | count/min | not investigated | Apple Watch / Health | Recovery and trend context | high | inspect via export in Phase 1; native HealthKit deferred |
| Heart rate variability | `HKQuantityTypeIdentifierHeartRateVariabilitySDNN` | ms | not investigated | Apple Watch | Recovery trend signal | high | inspect via export in Phase 1; native HealthKit deferred |
| VO2 max | `HKQuantityTypeIdentifierVO2Max` | ml/(kg*min) | not investigated | Apple Watch / Health estimates | Aerobic fitness trend | high | inspect via export in Phase 1; native HealthKit deferred |
| Respiratory rate | `HKQuantityTypeIdentifierRespiratoryRate` | count/min | not investigated | Apple Watch | Recovery and sleep context | high | inspect via export in Phase 1; native HealthKit deferred |
| Sleep analysis | `HKCategoryTypeIdentifierSleepAnalysis` | category | not investigated | Apple Watch / sleep apps | Sleep duration, stages, consistency | high | inspect via export in Phase 1; native HealthKit deferred |
| Active energy | `HKQuantityTypeIdentifierActiveEnergyBurned` | kcal | not investigated | Apple Watch | Activity and load context | medium | inspect via export in Phase 1; native HealthKit deferred |
| Basal energy | `HKQuantityTypeIdentifierBasalEnergyBurned` | kcal | not investigated | Apple Watch / Health | Energy context | medium | inspect via export in Phase 1; native HealthKit deferred |
| Step count | `HKQuantityTypeIdentifierStepCount` | count | not investigated | iPhone / Apple Watch | Activity context | medium | inspect via export in Phase 1; native HealthKit deferred |
| Distance walking/running | `HKQuantityTypeIdentifierDistanceWalkingRunning` | m | not investigated | iPhone / Apple Watch | Volume context | medium | inspect via export in Phase 1; native HealthKit deferred |
| Workouts | `HKWorkoutType` | mixed | not investigated | Apple Watch / Fitness | Workout history and metadata | high | inspect via export in Phase 1; native HealthKit deferred |
| Workout routes | `HKSeriesType.workoutRoute()` | lat/lon stream | not investigated | Apple Watch | Route, elevation, run reconstruction | very high | inspect route presence via export in Phase 1; native HealthKit deferred |
| Running speed | `HKQuantityTypeIdentifierRunningSpeed` | m/s | not investigated | Apple Watch | Running stream analysis | high | inspect via export in Phase 1; native HealthKit deferred |
| Running power | `HKQuantityTypeIdentifierRunningPower` | W | not investigated | Apple Watch | Load and durability analysis | high | inspect via export in Phase 1; native HealthKit deferred |
| Running cadence | `HKQuantityTypeIdentifierRunningCadence` | steps/min | not investigated | Apple Watch | Form and durability analysis | high | inspect via export in Phase 1; native HealthKit deferred |
| Stride length | `HKQuantityTypeIdentifierRunningStrideLength` | m | not investigated | Apple Watch | Form degradation analysis | high | inspect via export in Phase 1; native HealthKit deferred |
| Ground contact time | `HKQuantityTypeIdentifierRunningGroundContactTime` | ms | not investigated | Apple Watch | Running dynamics | high | inspect via export in Phase 1; native HealthKit deferred |
| Vertical oscillation | `HKQuantityTypeIdentifierRunningVerticalOscillation` | cm | not investigated | Apple Watch | Running dynamics | high | inspect via export in Phase 1; native HealthKit deferred |
| Flights climbed | `HKQuantityTypeIdentifierFlightsClimbed` | count | not investigated | iPhone / Apple Watch | Elevation context | low | backlog |
| Body mass | `HKQuantityTypeIdentifierBodyMass` | kg | not investigated | Health / scale | Fitness context and VO2/load interpretation | high | backlog |

Do not request or implement access without a clear product purpose.
