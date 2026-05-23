#!/usr/bin/env python3
"""Read-only file scanner for tax evidence intake manifests."""

from __future__ import annotations

import argparse
import csv
import hashlib
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class ScanRow:
    """Represents one scanned file record."""

    source_path: str
    file_name: str
    file_extension: str
    file_size_bytes: int
    modified_time_utc: str
    sha256: str


def utc_now() -> str:
    """Return current UTC timestamp in ISO 8601 format."""
    return datetime.now(timezone.utc).isoformat()


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
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
    """Yield files under root recursively in sorted order."""
    for item in sorted(root.rglob("*")):
        if item.is_file():
            yield item


def build_rows(root: Path) -> list[ScanRow]:
    """Build scan records for all files beneath root."""
    rows: list[ScanRow] = []
    for file_path in iter_files(root):
        stat = file_path.stat()
        rows.append(
            ScanRow(
                source_path=str(file_path.resolve()),
                file_name=file_path.name,
                file_extension=file_path.suffix.lower(),
                file_size_bytes=stat.st_size,
                modified_time_utc=datetime.fromtimestamp(
                    stat.st_mtime, tz=timezone.utc
                ).isoformat(),
                sha256=sha256_file(file_path),
            )
        )
    return rows


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


def append_operation_log(
    log_path: Path,
    action: str,
    source_location: str,
    destination_location: str,
    file_count: int,
    operator: str,
    status: str,
    notes: str,
) -> None:
    """Append an operational audit log row."""
    log_path.parent.mkdir(parents=True, exist_ok=True)
    needs_header = not log_path.exists() or log_path.stat().st_size == 0
    with log_path.open("a", newline="", encoding="utf-8") as file_obj:
        writer = csv.writer(file_obj)
        if needs_header:
            writer.writerow(
                [
                    "timestamp_utc",
                    "action",
                    "source_location",
                    "destination_location",
                    "file_count",
                    "operator",
                    "status",
                    "notes",
                ]
            )
        writer.writerow(
            [
                utc_now(),
                action,
                source_location,
                destination_location,
                file_count,
                operator,
                status,
                notes,
            ]
        )


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

    rows = build_rows(source)
    write_manifest(rows, output)
    append_operation_log(
        log_path=log,
        action="scan",
        source_location=str(source),
        destination_location=str(output),
        file_count=len(rows),
        operator=args.operator,
        status="success",
        notes="Read-only scan completed",
    )

    print(f"Scanned {len(rows)} file(s)")
    print(f"Manifest written to: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
