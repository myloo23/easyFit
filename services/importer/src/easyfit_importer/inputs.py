from __future__ import annotations

import hashlib
import zipfile
from collections.abc import Iterator
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import IO

from easyfit_importer.models import RouteFileSummary

ROUTE_EXTENSIONS = {".gpx", ".tcx", ".fit"}


class InputResolutionError(Exception):
    """Raised when an Apple Health export input cannot be safely resolved."""


@dataclass(frozen=True)
class ResolvedInput:
    kind: str
    display_name: str
    export_size_bytes: int
    safe_file_identity: str
    route_file_summary: RouteFileSummary
    _path: Path
    _zip_member: str | None = None

    @contextmanager
    def open_export_xml(self) -> Iterator[IO[bytes]]:
        if self.kind == "zip":
            with zipfile.ZipFile(self._path) as archive:
                if self._zip_member is None:
                    raise InputResolutionError(
                        "Archive input did not resolve an export.xml member."
                    )
                with archive.open(self._zip_member) as export_xml:
                    yield export_xml
            return

        with self._path.open("rb") as export_xml:
            yield export_xml


def resolve_input(input_path: Path) -> ResolvedInput:
    path = input_path.expanduser()
    if not path.exists():
        raise InputResolutionError(
            "Input does not exist. Provide an Apple Health export ZIP or folder."
        )

    if path.is_file() and path.suffix.lower() == ".zip":
        return _resolve_zip(path)

    if path.is_dir():
        return _resolve_directory(path)

    raise InputResolutionError(
        "Unsupported input. Use export.zip or an extracted export directory."
    )


def _resolve_zip(path: Path) -> ResolvedInput:
    try:
        with zipfile.ZipFile(path) as archive:
            names = archive.namelist()
            unsafe = [name for name in names if _is_unsafe_archive_name(name)]
            if unsafe:
                raise InputResolutionError("Archive contains unsafe member paths and was not read.")

            candidates = [name for name in names if PurePosixPath(name).name == "export.xml"]
            if not candidates:
                raise InputResolutionError("Archive does not contain export.xml.")
            if len(candidates) > 1:
                raise InputResolutionError("Archive contains multiple export.xml candidates.")

            member = candidates[0]
            info = archive.getinfo(member)
            route_summary = _route_summary_from_names(names)
            identity = _hash_zip_member(archive, member)
            return ResolvedInput(
                kind="zip",
                display_name="Apple Health export ZIP",
                export_size_bytes=info.file_size,
                safe_file_identity=identity,
                route_file_summary=route_summary,
                _path=path,
                _zip_member=member,
            )
    except zipfile.BadZipFile as exc:
        raise InputResolutionError("Input ZIP could not be opened as a valid archive.") from exc


def _resolve_directory(path: Path) -> ResolvedInput:
    candidates = sorted(candidate for candidate in path.rglob("export.xml") if candidate.is_file())
    if not candidates:
        raise InputResolutionError("Directory does not contain export.xml.")
    if len(candidates) > 1:
        raise InputResolutionError("Directory contains multiple export.xml candidates.")

    export_xml = candidates[0]
    route_names = [candidate.name for candidate in path.rglob("*") if candidate.is_file()]
    return ResolvedInput(
        kind="directory",
        display_name="Apple Health export directory",
        export_size_bytes=export_xml.stat().st_size,
        safe_file_identity=_hash_file(export_xml),
        route_file_summary=_route_summary_from_names(route_names),
        _path=export_xml,
    )


def _is_unsafe_archive_name(name: str) -> bool:
    path = PurePosixPath(name)
    return path.is_absolute() or ".." in path.parts


def _route_summary_from_names(names: list[str]) -> RouteFileSummary:
    extensions = sorted(
        {
            PurePosixPath(name).suffix.lower()
            for name in names
            if PurePosixPath(name).suffix.lower() in ROUTE_EXTENSIONS
        }
    )
    count = sum(1 for name in names if PurePosixPath(name).suffix.lower() in ROUTE_EXTENSIONS)
    return RouteFileSummary(count=count, extensions=tuple(extensions))


def _hash_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return f"sha256:{digest.hexdigest()[:16]}"


def _hash_zip_member(archive: zipfile.ZipFile, member: str) -> str:
    digest = hashlib.sha256()
    with archive.open(member) as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return f"sha256:{digest.hexdigest()[:16]}"
