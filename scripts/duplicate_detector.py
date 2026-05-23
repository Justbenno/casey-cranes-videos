#!/usr/bin/env python3
"""Detect duplicate evidence records using sha256 hashes."""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ManifestRow = dict[str, str]
DuplicateGroup = tuple[str, list[ManifestRow]]


def utc_now() -> str:
    """Return current UTC timestamp in ISO 8601 format."""
    return datetime.now(timezone.utc).isoformat()


def read_manifest(path: Path) -> list[ManifestRow]:
    """Read input manifest CSV rows."""
    with path.open("r", newline="", encoding="utf-8") as file_obj:
        return list(csv.DictReader(file_obj))


def detect_duplicates(rows: list[ManifestRow]) -> list[DuplicateGroup]:
    """Return duplicate groups keyed by sha256 hash."""
    grouped: dict[str, list[ManifestRow]] = defaultdict(list)
    for row in rows:
        file_hash = row.get("sha256", "").strip()
        if not file_hash:
            continue
        grouped[file_hash].append(row)

    duplicates: list[DuplicateGroup] = []
    for file_hash, hash_rows in grouped.items():
        if len(hash_rows) > 1:
            duplicates.append((file_hash, hash_rows))
    return sorted(duplicates, key=lambda item: item[0])


def write_duplicates(
    duplicate_groups: list[DuplicateGroup],
    output_path: Path,
) -> int:
    """Write duplicate report and return duplicate record count."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    duplicate_count = 0
    with output_path.open("w", newline="", encoding="utf-8") as file_obj:
        writer = csv.writer(file_obj)
        writer.writerow(
            [
                "duplicate_group_id",
                "sha256",
                "file_count",
                "source_path",
                "file_name",
                "file_extension",
                "file_size_bytes",
                "modified_time_utc",
            ]
        )
        for index, (file_hash, rows) in enumerate(duplicate_groups, start=1):
            group_id = f"DUP-{index:04d}"
            file_count = len(rows)
            for row in rows:
                writer.writerow(
                    [
                        group_id,
                        file_hash,
                        file_count,
                        row.get("source_path", ""),
                        row.get("file_name", ""),
                        row.get("file_extension", ""),
                        row.get("file_size_bytes", ""),
                        row.get("modified_time_utc", ""),
                    ]
                )
                duplicate_count += 1
    return duplicate_count


def append_operation_log(
    log_path: Path,
    source_location: str,
    destination_location: str,
    file_count: int,
    operator: str,
) -> None:
    """Append duplicate detection operation to chain-of-custody log."""
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
                "duplicate_detection",
                source_location,
                destination_location,
                file_count,
                operator,
                "success",
                "Duplicate report generated from manifest",
            ]
        )


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Detect duplicate files using scan manifest")
    parser.add_argument("--manifest", required=True, help="Input scan manifest CSV")
    parser.add_argument(
        "--output",
        default="logs/duplicate_report.csv",
        help="Output duplicate report CSV",
    )
    parser.add_argument(
        "--log",
        default="logs/operations_log.csv",
        help="Operations log CSV path",
    )
    parser.add_argument(
        "--operator",
        default="unknown-operator",
        help="Operator name for audit logging",
    )
    return parser.parse_args()


def main() -> int:
    """CLI entry point."""
    args = parse_args()
    manifest = Path(args.manifest).expanduser().resolve()
    output = Path(args.output).expanduser().resolve()
    log = Path(args.log).expanduser().resolve()

    if not manifest.exists():
        print(f"Manifest not found: {manifest}")
        return 1

    rows = read_manifest(manifest)
    duplicate_groups = detect_duplicates(rows)
    duplicate_record_count = write_duplicates(duplicate_groups, output)
    append_operation_log(
        log_path=log,
        source_location=str(manifest),
        destination_location=str(output),
        file_count=duplicate_record_count,
        operator=args.operator,
    )

    print(f"Duplicate groups: {len(duplicate_groups)}")
    print(f"Duplicate rows written: {duplicate_record_count}")
    print(f"Report written to: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
