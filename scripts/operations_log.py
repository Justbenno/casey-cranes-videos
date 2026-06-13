"""Shared helpers for writing chain-of-custody operation logs."""

from __future__ import annotations

import csv
from datetime import datetime, timezone
from pathlib import Path

OPERATION_LOG_HEADER = [
    "timestamp_utc",
    "action",
    "source_location",
    "destination_location",
    "file_count",
    "operator",
    "status",
    "notes",
]


def utc_now() -> str:
    """Return current UTC timestamp in ISO 8601 format."""
    return datetime.now(timezone.utc).isoformat()


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
            writer.writerow(OPERATION_LOG_HEADER)
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
