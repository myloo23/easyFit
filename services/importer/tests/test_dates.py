from __future__ import annotations

import pytest

from easyfit_importer.dates import parse_health_datetime


@pytest.mark.parametrize(
    ("value", "offset_seconds"),
    [
        ("2030-03-30 09:55:00 +0200", 7200),
        ("2030-01-01 23:30:00 -0500", -18000),
        ("2030-10-27 01:30:00 +0100", 3600),
    ],
)
def test_parse_health_datetime_preserves_numeric_offsets(value: str, offset_seconds: int) -> None:
    parsed = parse_health_datetime(value)
    offset = parsed.utcoffset()

    assert offset is not None
    assert offset.total_seconds() == offset_seconds


def test_parse_health_datetime_rejects_naive_timestamp() -> None:
    with pytest.raises(ValueError):
        parse_health_datetime("2030-03-30 09:55:00")
