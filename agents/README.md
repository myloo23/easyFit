# easyFit Agents Memory

This directory is the persistent operating system for the project. Future agents and contributors should use it before relying on chat history.

## Start-of-session protocol

1. Read `PROJECT_CHARTER.md`.
2. Read `CURRENT_STATE.md`.
3. Read `TASKS.md`.
4. Read relevant architecture, privacy, data, and catalog documents.
5. Inspect the actual repository state before editing.

## End-of-session protocol

1. Update `CURRENT_STATE.md`.
2. Update `TASKS.md`.
3. Append a concise entry to `SESSION_LOG.md`.
4. Record major decisions in `DECISION_LOG.md` or an ADR.
5. Update risks, open questions, and catalogs when new facts are learned.

## Ground rules

- Do not commit real personal health data or exports.
- Do not build dashboards before the data foundation is trustworthy.
- Do not invent HealthKit availability or analytics formulas.
- Preserve raw source fidelity and keep derived metrics versioned.
- Treat privacy, data integrity, and correctness as product requirements.
