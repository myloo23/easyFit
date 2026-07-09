from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from easyfit_importer.inputs import InputResolutionError, resolve_input
from easyfit_importer.parser import build_inventory

EXIT_SUCCESS = 0
EXIT_INPUT_ERROR = 2
EXIT_RUNTIME_ERROR = 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="easyfit_importer")
    subparsers = parser.add_subparsers(dest="command", required=True)
    inventory_parser = subparsers.add_parser("inventory", help="Inventory an Apple Health export")
    inventory_parser.add_argument(
        "--input",
        required=True,
        type=Path,
        help="Path to export.zip or extracted export folder",
    )
    inventory_parser.add_argument(
        "--output",
        type=Path,
        help="Optional ignored private path for safe JSON output",
    )
    inventory_parser.add_argument(
        "--no-progress",
        action="store_true",
        help="Disable periodic progress on stderr",
    )

    args = parser.parse_args(argv)
    if args.command != "inventory":
        parser.error("Unsupported command.")

    try:
        resolved = resolve_input(args.input)
        inventory = build_inventory(resolved, show_progress=not args.no_progress)
        safe = inventory.to_safe_dict()
        if args.output:
            _ensure_ignored_output(args.output)
            _write_json(args.output, safe)
        print(_format_human_summary(safe))
        return EXIT_SUCCESS
    except InputResolutionError as exc:
        print(f"Input error: {exc}", file=sys.stderr)
        return EXIT_INPUT_ERROR
    except OSError as exc:
        print(
            f"Filesystem error while reading or writing importer data: {exc.strerror or exc}",
            file=sys.stderr,
        )
        return EXIT_RUNTIME_ERROR
    except Exception as exc:
        print(
            f"Importer failed before inventory could complete: {type(exc).__name__}",
            file=sys.stderr,
        )
        return EXIT_RUNTIME_ERROR


def _write_json(path: Path, safe: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(safe, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _ensure_ignored_output(path: Path) -> None:
    try:
        repo_root_result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            check=True,
            capture_output=True,
            text=True,
        )
        repo_root = Path(repo_root_result.stdout.strip())
        output_path = path.resolve()
        relative_output = output_path.relative_to(repo_root)
        subprocess.run(
            ["git", "check-ignore", "-q", str(relative_output)],
            cwd=repo_root,
            check=True,
        )
    except (subprocess.CalledProcessError, ValueError) as exc:
        raise InputResolutionError(
            "--output must be inside a Git-ignored private path, "
            "for example personal-health-data/inventory-summary.json."
        ) from exc


def _format_human_summary(safe: dict[str, object]) -> str:
    workout = safe["workout_summary"]
    activity = safe["activity_summary"]
    routes = safe["route_file_summary"]
    date_range = safe["overall_date_range"]
    unknown = safe["unknown_element_summary"]
    stats = safe["parse_statistics"]
    warnings = safe["warnings"]
    assert isinstance(workout, dict)
    assert isinstance(activity, dict)
    assert isinstance(routes, dict)
    assert isinstance(date_range, dict)
    assert isinstance(unknown, dict)
    assert isinstance(stats, dict)
    assert isinstance(warnings, list)
    record_type_summaries = safe["record_type_summaries"]
    assert isinstance(record_type_summaries, list)
    route_extensions = routes["extensions"]
    assert isinstance(route_extensions, list | tuple)
    route_extension_text = ", ".join(str(extension) for extension in route_extensions)

    lines = [
        "easyFit Apple Health Inventory",
        f"Parser: {safe['parser_version']}",
        f"Input kind: {safe['input_kind']}",
        f"Safe file identity: {safe['safe_file_identity']}",
        f"Export XML size bytes: {safe['export_size_bytes']}",
        f"Records processed: {safe['total_health_records']}",
        f"Record types: {len(record_type_summaries)}",
        f"Workouts: {workout['total_count']}",
        f"Running workouts: {workout['running_count']}",
        f"Activity summaries: {activity['total_count']}",
        f"Route files detected: {routes['count']}",
        f"Route file extensions: {route_extension_text if route_extensions else 'none'}",
        f"Date coverage: {date_range['earliest']} to {date_range['latest']}",
        f"Unknown element types: {unknown['total_count']}",
        f"Malformed date count: {stats['malformed_date_count']}",
        f"Warnings: {len(warnings)}",
    ]
    return "\n".join(lines)
