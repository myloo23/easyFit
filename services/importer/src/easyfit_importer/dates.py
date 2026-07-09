from __future__ import annotations

from datetime import datetime


def parse_health_datetime(value: str) -> datetime:
    """Parse an Apple Health timestamp while requiring explicit timezone offset."""
    parsed = datetime.strptime(value, "%Y-%m-%d %H:%M:%S %z")
    if parsed.tzinfo is None:
        raise ValueError("timestamp has no timezone offset")
    return parsed


def safe_date(value: datetime | None) -> str | None:
    """Return a day-level date for safe reporting."""
    if value is None:
        return None
    return value.date().isoformat()
