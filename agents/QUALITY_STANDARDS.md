# Quality Standards

## Engineering standards

- Strict typing where available.
- Formatting and linting in every package.
- Versioned database migrations when a database exists.
- Documented units for every health metric.
- Structured error handling.
- Reproducible local development setup.
- Tests scaled to risk and blast radius.

## Data standards

- Do not silently drop samples.
- Do not mix raw and calculated data.
- Preserve provenance.
- Record units and timezone assumptions.
- Make deduplication explicit.
- Version derived algorithms.

## Product standards

- No fake AI insights.
- No unexplained scores.
- No medical claims.
- No hidden errors for sensitive data operations.
- No production logging of sensitive raw health data.
