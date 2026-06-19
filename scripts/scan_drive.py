#!/usr/bin/env python3
"""Read-only file scanner for tax evidence intake manifests."""

from __future__ import annotations

import argparse
import csv
import hashlib
import os
from collections.abc import Iterable
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from operations_log import append_operation_log

DEFAULT_HASH_CHUNK_SIZE_BYTES = 1024 * 1024


@dataclass(frozen=True)
class ScanRow:
    """Represents one scanned file record."""

    source_path: str
    file_name: str
    file_extension: str
    file_size_bytes: int
    modified_time_utc: str
    sha256: str


@dataclass(frozen=True)
class ScanError:
    """Represents one file that could not be scanned."""

    source_path: str
    error: str


def sha256_file(path: Path, chunk_size: int = DEFAULT_HASH_CHUNK_SIZE_BYTES) -> str:
    """Return sha256 hash for a file path."""
    digest = hashlib.sha256()
    with path.open("rb") as file_obj:
        while True:
            chunk = file_obj.read(chunk_size)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def iter_files(root: Path) -> Iterable[Path]:
    """Yield files under root recursively in sorted order, without following symlinks."""
    for dirpath, dirnames, filenames in os.walk(root, followlinks=False):
        dirnames.sort()
        for filename in sorted(filenames):
            yield Path(dirpath) / filename


def build_rows(root: Path) -> tuple[list[ScanRow], list[ScanError]]:
    """Build scan records for all files beneath root."""
    rows: list[ScanRow] = []
    errors: list[ScanError] = []
    for file_path in iter_files(root):
        try:
            stat = file_path.stat()
            file_hash = sha256_file(file_path)
            resolved_path = file_path.resolve()
        except (OSError, RuntimeError) as exc:
            print(f"Skipped unreadable file: {file_path} ({exc})")
            errors.append(ScanError(source_path=str(file_path), error=str(exc)))
            continue
        rows.append(
            ScanRow(
                source_path=str(resolved_path),
                file_name=file_path.name,
                file_extension=file_path.suffix.lower(),
                file_size_bytes=stat.st_size,
                modified_time_utc=datetime.fromtimestamp(
                    stat.st_mtime, tz=timezone.utc
                ).isoformat(),
                sha256=file_hash,
            )
        )
    return rows, errors


def write_manifest(rows: list[ScanRow], output_path: Path) -> None:
    """Write file scan results to CSV manifest."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as file_obj:
        writer = csv.writer(file_obj)
        writer.writerow(
            [
                "source_path",
                "file_name",
                "file_extension",
                "file_size_bytes",
                "modified_time_utc",
                "sha256",
            ]
        )
        for row in rows:
            writer.writerow(
                [
                    row.source_path,
                    row.file_name,
                    row.file_extension,
                    row.file_size_bytes,
                    row.modified_time_utc,
                    row.sha256,
                ]
            )


def derive_error_report_path(output_path: Path) -> Path:
    """Return the companion CSV path for scan errors."""
    return output_path.with_name(f"{output_path.stem}_errors.csv")


def write_error_report(errors: list[ScanError], output_path: Path) -> None:
    """Write skipped-file scan errors to CSV."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as file_obj:
        writer = csv.writer(file_obj)
        writer.writerow(["source_path", "error"])
        for error in errors:
            writer.writerow([error.source_path, error.error])


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser(
        description="Read-only scan of a source folder to produce a tax evidence manifest"
    )
    parser.add_argument("--source", required=True, help="Root folder to scan")
    parser.add_argument(
        "--output",
        default="logs/source_scan_manifest.csv",
        help="CSV manifest output path",
    )
    parser.add_argument(
        "--log",
        default="logs/operations_log.csv",
        help="Operations log CSV path",
    )
    parser.add_argument(
        "--operator",
        default="unknown-operator",
        help="Operator name for chain-of-custody logging",
    )
    return parser.parse_args()


def main() -> int:
    """CLI entry point."""
    args = parse_args()
    source = Path(args.source).expanduser().resolve()
    output = Path(args.output).expanduser().resolve()
    log = Path(args.log).expanduser().resolve()

    if not source.exists() or not source.is_dir():
        print(f"Source directory not found: {source}")
        return 1

    rows, errors = build_rows(source)
    write_manifest(rows, output)
    error_report = derive_error_report_path(output)
    if errors:
        write_error_report(errors, error_report)
    status = "success" if not errors else "partial_success"
    notes = (
        "Read-only scan completed"
        if not errors
        else (
            "Read-only scan completed with "
            f"{len(errors)} failure(s)/skip(s); error report: {error_report}"
        )
    )
    append_operation_log(
        log_path=log,
        action="scan",
        source_location=str(source),
        destination_location=str(output),
        file_count=len(rows),
        operator=args.operator,
        status=status,
        notes=notes,
    )

    print(f"Scanned {len(rows)} file(s)")
    if errors:
        print(f"Skipped {len(errors)} unreadable file(s)")
        print(f"Error report written to: {error_report}")
    print(f"Manifest written to: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
