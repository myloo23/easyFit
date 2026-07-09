# Project Charter

## Product name

`easyFit` is the current working product and brand name. The product may be renamed before public market launch.

Architecture and technical identifiers should not be unnecessarily coupled to the public brand. Expensive-to-change identifiers, such as Apple bundle identifiers, database names, cloud resources, package namespaces, domain names, and API identifiers, should be chosen deliberately when they become necessary and recorded in an ADR or decision log entry.

## Mission

Build a serious Apple Watch and Apple Health analytics platform for endurance training, running, marathon preparation, recovery, sleep, training load, workout analysis, and long-term personal health and performance trends.

The product should turn fragmented health and training data into transparent, useful, and privacy-conscious insight.

## Initial user and market

The founder is the first power user: an Apple Watch and Apple Health user preparing for a marathon, familiar with Next.js, React, TypeScript, and Tailwind, and currently using a mix of Apple Fitness, Strava, and Livity-like tools.

The architecture must not be single-user-only. The eventual market may include serious Apple Watch runners, marathon trainees, endurance athletes, and data-driven fitness users.

## Priorities

1. Privacy.
2. Data integrity.
3. Correctness.
4. Security.
5. Maintainability.
6. Observability.
7. Product quality.
8. Development speed.

## Near-term mandate

The first technical milestone is a trustworthy data foundation, not a dashboard. The project must first discover which HealthKit data is actually available from the founder's real devices, document it, and design raw, normalized, and derived data layers before serious product UI work begins.

## Non-goals for the bootstrap phase

- No dashboard implementation.
- No arbitrary recovery or readiness score.
- No medical claims.
- No commercial subscription implementation.
- No real health data committed to Git.
- No superficial ADR set created before research.
