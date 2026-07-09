from __future__ import annotations

import zipfile
from pathlib import Path

import pytest

from easyfit_importer.inputs import InputResolutionError, resolve_input

FIXTURE_DIR = (
    Path(__file__).resolve().parents[3] / "fixtures/synthetic/apple-health/apple_health_export"
)


def test_resolve_directory_input() -> None:
    resolved = resolve_input(FIXTURE_DIR)

    assert resolved.kind == "directory"
    assert resolved.export_size_bytes > 0
    assert resolved.route_file_summary.count == 1
    assert resolved.route_file_summary.extensions == (".gpx",)


def test_resolve_zip_input(tmp_path: Path) -> None:
    archive_path = tmp_path / "export.zip"
    with zipfile.ZipFile(archive_path, "w") as archive:
        archive.write(FIXTURE_DIR / "export.xml", "apple_health_export/export.xml")
        archive.write(
            FIXTURE_DIR / "workout-routes/route_synthetic.gpx",
            "apple_health_export/workout-routes/route_synthetic.gpx",
        )

    resolved = resolve_input(archive_path)

    assert resolved.kind == "zip"
    assert resolved.route_file_summary.count == 1
    with resolved.open_export_xml() as export_xml:
        assert export_xml.read(5) == b"<?xml"


def test_resolve_localized_export_xml_in_zip(tmp_path: Path) -> None:
    archive_path = tmp_path / "localized-export.zip"

    with zipfile.ZipFile(archive_path, "w") as archive:
        archive.writestr(
            "apple_health_export/exportálás.xml",
            b"<?xml version='1.0'?><HealthData />",
        )
        archive.writestr(
            "apple_health_export/export_cda.xml",
            b"<?xml version='1.0'?><ClinicalDocument />",
        )

    resolved = resolve_input(archive_path)

    assert resolved.kind == "zip"
    with resolved.open_export_xml() as export_xml:
        assert b"HealthData" in export_xml.read()


def test_rejects_ambiguous_localized_xml_candidates(tmp_path: Path) -> None:
    archive_path = tmp_path / "ambiguous-export.zip"

    with zipfile.ZipFile(archive_path, "w") as archive:
        archive.writestr(
            "apple_health_export/egészség-export.xml",
            b"<?xml version='1.0'?><HealthData />",
        )
        archive.writestr(
            "apple_health_export/gesundheit-export.xml",
            b"<?xml version='1.0'?><HealthData />",
        )

    with pytest.raises(
        InputResolutionError,
        match="multiple ambiguous main export XML candidates",
    ):
        resolve_input(archive_path)


def test_missing_export_xml(tmp_path: Path) -> None:
    with pytest.raises(InputResolutionError, match="plausible main Apple Health export XML"):
        resolve_input(tmp_path)


def test_invalid_input_type(tmp_path: Path) -> None:
    invalid = tmp_path / "export.txt"
    invalid.write_text("not an export", encoding="utf-8")

    with pytest.raises(InputResolutionError, match="Unsupported input"):
        resolve_input(invalid)
