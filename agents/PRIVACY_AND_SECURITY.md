# Privacy and Security

Health data is highly sensitive. Privacy and security are product requirements.

## Principles

- No secrets in Git.
- No real health exports committed to Git.
- Encrypt data in transit.
- Use appropriate encryption at rest.
- Do not include sensitive raw health data in production logs.
- Use least-privilege access.
- Support account deletion that deletes associated health data before market release.
- Support user data export before market release.
- Do not send identifiable health data to third-party AI or analytics services without explicit architectural and privacy review.

## Development rules

- Use synthetic fixtures by default.
- If real-device diagnostics are needed, keep outputs local and excluded from Git.
- The root `.gitignore` must protect common local health exports, workout route files, private diagnostics, local health databases, credentials, certificates, provisioning profiles, and environment files.
- Synthetic fixtures may be committed under an explicit synthetic fixture path when they contain no real personal health, workout, route, credential, or diagnostic data.
- Safe examples such as `.env.example` may be committed when they contain no real secrets.
- Prefer structured logs with redaction.
- Avoid logging coordinates, full timestamps tied to sensitive events, or raw sample payloads unless explicitly in local debug mode.
- Keep secrets in platform keychains, local environment files excluded from Git, or managed secret stores.

## Repository visibility

The GitHub repository is currently public. After code is pushed, source files and documentation will be publicly visible.

Implications:

- No personal health data may ever be committed.
- No secrets, credentials, certificates, provisioning profiles, or private diagnostics may ever be committed.
- Public repository visibility may need to be revisited as a founder/product decision before commercial launch.

## Future production requirements

- Threat model for iOS, sync API, database, analytics jobs, and web dashboard.
- Access controls and audit logs for backend operations.
- Data retention policy.
- Deletion and export runbooks.
- Incident response runbook.
- Privacy review for third-party processors.
