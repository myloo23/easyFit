from __future__ import annotations

import sys
import time
import xml.etree.ElementTree as ET
from datetime import UTC, datetime

from easyfit_importer.dates import parse_health_datetime
from easyfit_importer.inputs import ResolvedInput
from easyfit_importer.models import (
    ActivitySummary,
    DateRange,
    InventorySummary,
    ParseStatistics,
    RecordTypeSummary,
    UnknownElementSummary,
    WorkoutSummary,
)
from easyfit_importer.sources import categorize_device, categorize_source
from easyfit_importer.version import PARSER_VERSION

KNOWN_TOP_LEVEL = {
    "Record",
    "Workout",
    "ActivitySummary",
    "ClinicalRecord",
    "Correlation",
    "Audiogram",
    "Electrocardiogram",
}


def build_inventory(
    resolved: ResolvedInput,
    *,
    progress_interval: int = 100_000,
    show_progress: bool = False,
) -> InventorySummary:
    builder = _InventoryBuilder(resolved)
    last_progress = time.monotonic()
    depth = 0
    with resolved.open_export_xml() as export_xml:
        for event, elem in ET.iterparse(export_xml, events=("start", "end")):
            if event == "start":
                depth += 1
                continue

            builder.parse_statistics.xml_elements_processed += 1
            if depth == 2:
                builder.process_top_level_element(elem.tag, dict(elem.attrib))
            elem.clear()
            depth -= 1
            progress_due = builder.parse_statistics.xml_elements_processed % progress_interval == 0
            if show_progress and progress_due:
                now = time.monotonic()
                if now - last_progress >= 1:
                    print(
                        "Processed "
                        f"{builder.parse_statistics.xml_elements_processed} XML elements; "
                        f"{builder.total_health_records} records.",
                        file=sys.stderr,
                    )
                    last_progress = now
    return builder.finish()


class _InventoryBuilder:
    def __init__(self, resolved: ResolvedInput) -> None:
        self.resolved = resolved
        self.total_health_records = 0
        self.overall_date_range = DateRange()
        self.record_type_summaries: dict[str, RecordTypeSummary] = {}
        self.workout_summary = WorkoutSummary()
        self.activity_summary = ActivitySummary()
        self.unknown_element_summary = UnknownElementSummary()
        self.parse_statistics = ParseStatistics()
        self.warnings: list[str] = []

    def process_top_level_element(self, tag: str, attributes: dict[str, str]) -> None:
        match tag:
            case "Record":
                self._process_record(attributes)
            case "Workout":
                self._process_workout(attributes)
            case "ActivitySummary":
                self._process_activity_summary(attributes)
            case "HealthData" | "MetadataEntry" | "WorkoutEvent" | "WorkoutStatistics":
                return
            case "ClinicalRecord" | "Correlation" | "Audiogram" | "Electrocardiogram":
                self._count_auxiliary(tag)
            case _:
                if attributes:
                    self.unknown_element_summary.add(tag)

    def _process_record(self, attributes: dict[str, str]) -> None:
        self.total_health_records += 1
        record_type = attributes.get("type", "Unknown")
        summary = self.record_type_summaries.setdefault(
            record_type,
            RecordTypeSummary(record_type=record_type),
        )
        summary.count += 1

        if unit := attributes.get("unit"):
            summary.units.add(unit)
        summary.source_categories.add(
            categorize_source(attributes.get("sourceName"), attributes.get("device"))
        )
        summary.device_categories.add(categorize_device(attributes.get("device")))

        malformed = False
        for key in ("startDate", "endDate"):
            parsed = self._parse_date(attributes.get(key))
            if parsed is None and attributes.get(key):
                malformed = True
            summary.date_range.add(parsed)
            self.overall_date_range.add(parsed)
        if malformed:
            summary.malformed_date_count += 1

    def _process_workout(self, attributes: dict[str, str]) -> None:
        self.workout_summary.total_count += 1
        activity_type = attributes.get("workoutActivityType", "Unknown")
        self.workout_summary.counts_by_activity_type[activity_type] = (
            self.workout_summary.counts_by_activity_type.get(activity_type, 0) + 1
        )
        if is_running_workout(activity_type):
            self.workout_summary.running_count += 1
        if unit := attributes.get("durationUnit"):
            self.workout_summary.duration_units.add(unit)
        if unit := attributes.get("totalDistanceUnit"):
            self.workout_summary.distance_units.add(unit)
        self.workout_summary.source_categories.add(
            categorize_source(attributes.get("sourceName"), attributes.get("device"))
        )

        malformed = False
        for key in ("startDate", "endDate", "creationDate"):
            parsed = self._parse_date(attributes.get(key))
            if parsed is None and attributes.get(key):
                malformed = True
            self.workout_summary.date_range.add(parsed)
            self.overall_date_range.add(parsed)
        if malformed:
            self.workout_summary.malformed_date_count += 1

    def _process_activity_summary(self, attributes: dict[str, str]) -> None:
        self.activity_summary.total_count += 1
        parsed = self._parse_activity_date(attributes.get("dateComponents"))
        if parsed is None and attributes.get("dateComponents"):
            self.activity_summary.malformed_date_count += 1
        self.activity_summary.date_range.add(parsed)
        self.overall_date_range.add(parsed)

    def _parse_date(self, value: str | None) -> datetime | None:
        if not value:
            return None
        try:
            return parse_health_datetime(value)
        except ValueError:
            self.parse_statistics.malformed_date_count += 1
            self.warnings.append(
                "One or more timestamps could not be parsed and were excluded from date ranges."
            )
            return None

    def _parse_activity_date(self, value: str | None) -> datetime | None:
        if not value:
            return None
        try:
            return datetime.strptime(value, "%Y-%m-%d").replace(tzinfo=UTC)
        except ValueError:
            self.parse_statistics.malformed_date_count += 1
            self.warnings.append("One or more activity summary dates could not be parsed.")
            return None

    def _count_auxiliary(self, tag: str) -> None:
        counts = self.parse_statistics.recognized_auxiliary_elements
        counts[tag] = counts.get(tag, 0) + 1

    def finish(self) -> InventorySummary:
        if self.unknown_element_summary.counts_by_element:
            self.warnings.append(
                "Unknown top-level data elements were counted but not deeply parsed."
            )
        return InventorySummary(
            parser_version=PARSER_VERSION,
            input_kind=self.resolved.kind,
            safe_file_identity=self.resolved.safe_file_identity,
            export_size_bytes=self.resolved.export_size_bytes,
            total_health_records=self.total_health_records,
            overall_date_range=self.overall_date_range,
            record_type_summaries=self.record_type_summaries,
            workout_summary=self.workout_summary,
            activity_summary=self.activity_summary,
            route_file_summary=self.resolved.route_file_summary,
            unknown_element_summary=self.unknown_element_summary,
            warnings=self.warnings,
            parse_statistics=self.parse_statistics,
        )


def is_running_workout(activity_type: str) -> bool:
    return activity_type == "HKWorkoutActivityTypeRunning"
