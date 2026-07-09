from __future__ import annotations

import json
from pathlib import Path

from easyfit_importer.inputs import resolve_input
from easyfit_importer.parser import build_inventory, is_running_workout
from easyfit_importer.version import PARSER_VERSION

FIXTURE_DIR = (
    Path(__file__).resolve().parents[3] / "fixtures/synthetic/apple-health/apple_health_export"
)


def _safe_inventory() -> dict[str, object]:
    resolved = resolve_input(FIXTURE_DIR)
    return build_inventory(resolved, show_progress=False).to_safe_dict()


def test_inventory_counts_records_workouts_activity_unknowns_and_routes() -> None:
    safe = _safe_inventory()
    workout = safe["workout_summary"]
    activity = safe["activity_summary"]
    routes = safe["route_file_summary"]
    unknown = safe["unknown_element_summary"]

    assert safe["parser_version"] == PARSER_VERSION
    assert safe["total_health_records"] == 5
    record_type_summaries = safe["record_type_summaries"]
    assert isinstance(record_type_summaries, list)
    assert len(record_type_summaries) == 4
    assert isinstance(workout, dict)
    assert workout["total_count"] == 2
    assert workout["running_count"] == 1
    assert workout["counts_by_activity_type"] == {
        "HKWorkoutActivityTypeCycling": 1,
        "HKWorkoutActivityTypeRunning": 1,
    }
    assert isinstance(activity, dict)
    assert activity["total_count"] == 1
    assert isinstance(routes, dict)
    assert routes["count"] == 1
    assert routes["extensions"] == (".gpx",)
    assert isinstance(unknown, dict)
    assert unknown["counts_by_element"] == {"MysteryTopLevel": 1}


def test_inventory_date_aggregation_and_malformed_warning() -> None:
    safe = _safe_inventory()
    stats = safe["parse_statistics"]
    date_range = safe["overall_date_range"]

    assert isinstance(stats, dict)
    assert stats["malformed_date_count"] == 1
    assert isinstance(date_range, dict)
    assert date_range["earliest"] == "2030-01-01"
    assert date_range["latest"] == "2030-10-27"
    assert safe["warnings"] == [
        "One or more timestamps could not be parsed and were excluded from date ranges.",
        "Unknown top-level data elements were counted but not deeply parsed.",
    ]


def test_running_workout_detection_is_exact() -> None:
    assert is_running_workout("HKWorkoutActivityTypeRunning")
    assert not is_running_workout("HKWorkoutActivityTypeWalking")
    assert not is_running_workout("SyntheticRunningAdjacent")


def test_safe_inventory_excludes_private_content() -> None:
    serialized = json.dumps(_safe_inventory(), sort_keys=True)

    assert "value" not in serialized
    assert "123" not in serialized
    assert "124" not in serialized
    assert str(FIXTURE_DIR) not in serialized
    assert "MetadataEntry" not in serialized
    assert "route_synthetic" not in serialized
    assert "latitude" not in serialized.lower()
    assert "longitude" not in serialized.lower()


def test_inventory_is_deterministic() -> None:
    assert _safe_inventory() == _safe_inventory()
