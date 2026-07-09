from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import UTC, datetime
from typing import Any

from easyfit_importer.dates import safe_date


@dataclass
class DateRange:
    earliest: datetime | None = None
    latest: datetime | None = None

    def add(self, value: datetime | None) -> None:
        if value is None:
            return
        comparable = value.astimezone(UTC)
        if self.earliest is None or comparable < self.earliest.astimezone(UTC):
            self.earliest = value
        if self.latest is None or comparable > self.latest.astimezone(UTC):
            self.latest = value

    def to_safe_dict(self) -> dict[str, str | None]:
        return {"earliest": safe_date(self.earliest), "latest": safe_date(self.latest)}


@dataclass
class RecordTypeSummary:
    record_type: str
    count: int = 0
    date_range: DateRange = field(default_factory=DateRange)
    units: set[str] = field(default_factory=set)
    source_categories: set[str] = field(default_factory=set)
    device_categories: set[str] = field(default_factory=set)
    malformed_date_count: int = 0

    def to_safe_dict(self) -> dict[str, Any]:
        return {
            "record_type": self.record_type,
            "count": self.count,
            "date_range": self.date_range.to_safe_dict(),
            "units": sorted(self.units),
            "source_categories": sorted(self.source_categories),
            "device_categories": sorted(self.device_categories),
            "malformed_date_count": self.malformed_date_count,
        }


@dataclass
class WorkoutSummary:
    total_count: int = 0
    running_count: int = 0
    counts_by_activity_type: dict[str, int] = field(default_factory=dict)
    date_range: DateRange = field(default_factory=DateRange)
    duration_units: set[str] = field(default_factory=set)
    distance_units: set[str] = field(default_factory=set)
    source_categories: set[str] = field(default_factory=set)
    malformed_date_count: int = 0

    def to_safe_dict(self) -> dict[str, Any]:
        return {
            "total_count": self.total_count,
            "running_count": self.running_count,
            "counts_by_activity_type": dict(sorted(self.counts_by_activity_type.items())),
            "date_range": self.date_range.to_safe_dict(),
            "duration_units": sorted(self.duration_units),
            "distance_units": sorted(self.distance_units),
            "source_categories": sorted(self.source_categories),
            "malformed_date_count": self.malformed_date_count,
        }


@dataclass
class ActivitySummary:
    total_count: int = 0
    date_range: DateRange = field(default_factory=DateRange)
    malformed_date_count: int = 0

    def to_safe_dict(self) -> dict[str, Any]:
        return {
            "total_count": self.total_count,
            "date_range": self.date_range.to_safe_dict(),
            "malformed_date_count": self.malformed_date_count,
        }


@dataclass(frozen=True)
class RouteFileSummary:
    count: int
    extensions: tuple[str, ...]

    def to_safe_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class UnknownElementSummary:
    counts_by_element: dict[str, int] = field(default_factory=dict)

    def add(self, tag: str) -> None:
        self.counts_by_element[tag] = self.counts_by_element.get(tag, 0) + 1

    def to_safe_dict(self) -> dict[str, Any]:
        return {
            "total_count": sum(self.counts_by_element.values()),
            "counts_by_element": dict(sorted(self.counts_by_element.items())),
        }


@dataclass
class ParseStatistics:
    xml_elements_processed: int = 0
    malformed_date_count: int = 0
    recognized_auxiliary_elements: dict[str, int] = field(default_factory=dict)

    def to_safe_dict(self) -> dict[str, Any]:
        return {
            "xml_elements_processed": self.xml_elements_processed,
            "malformed_date_count": self.malformed_date_count,
            "recognized_auxiliary_elements": dict(
                sorted(self.recognized_auxiliary_elements.items())
            ),
        }


@dataclass
class InventorySummary:
    parser_version: str
    input_kind: str
    safe_file_identity: str
    export_size_bytes: int
    total_health_records: int
    overall_date_range: DateRange
    record_type_summaries: dict[str, RecordTypeSummary]
    workout_summary: WorkoutSummary
    activity_summary: ActivitySummary
    route_file_summary: RouteFileSummary
    unknown_element_summary: UnknownElementSummary
    warnings: list[str]
    parse_statistics: ParseStatistics

    def to_safe_dict(self) -> dict[str, Any]:
        return {
            "parser_version": self.parser_version,
            "input_kind": self.input_kind,
            "safe_file_identity": self.safe_file_identity,
            "export_size_bytes": self.export_size_bytes,
            "total_health_records": self.total_health_records,
            "overall_date_range": self.overall_date_range.to_safe_dict(),
            "record_type_summaries": [
                summary.to_safe_dict() for _, summary in sorted(self.record_type_summaries.items())
            ],
            "workout_summary": self.workout_summary.to_safe_dict(),
            "activity_summary": self.activity_summary.to_safe_dict(),
            "route_file_summary": self.route_file_summary.to_safe_dict(),
            "unknown_element_summary": self.unknown_element_summary.to_safe_dict(),
            "warnings": sorted(set(self.warnings)),
            "parse_statistics": self.parse_statistics.to_safe_dict(),
        }
