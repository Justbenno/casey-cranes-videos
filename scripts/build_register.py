#!/usr/bin/env python3
"""Classify scanned files into an evidence register."""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

HIGH_CONFIDENCE_THRESHOLD = 2
MEDIUM_CONFIDENCE_THRESHOLD = 1


KEYWORD_MAP: dict[str, tuple[str, ...]] = {
    "PAYG": ("payg", "income statement", "payslip", "salary"),
    "Bank Interest": ("interest", "bank statement", "savings"),
    "Dividends": ("dividend", "distribution", "franking"),
    "Crypto": ("crypto", "blockchain", "coin", "wallet"),
    "Fuel": ("fuel", "diesel", "petrol"),
    "Tolls": ("toll", "linkt", "etag"),
    "Vehicle Expenses": ("rego", "registration", "service", "repair", "tyre"),
    "Tools & Equipment": ("tool", "equipment", "rigging", "hardware"),
    "PPE": ("ppe", "boots", "uniform", "gloves", "hi-vis"),
    "Training & Education": ("course", "training", "seminar", "workshop"),
    "Phone & Internet": ("phone", "mobile", "internet", "telstra", "optus"),
    "Home Office": ("home office", "desk", "monitor", "chair"),
    "Insurance": ("insurance", "private health", "income protection"),
    "Subscriptions": ("subscription", "saas", "ai", "chatgpt", "copilot"),
    "Accountant Fees": ("accountant", "tax agent", "bookkeeping"),
    "Crane Operations": ("casey crane", "crane", "lift plan", "site"),
    "Compliance Expenses": ("compliance", "licence", "worksafe", "cranesafe"),
    "ATO Correspondence": ("ato", "notice of assessment", "mygov"),
    "Objection Evidence": ("objection", "dispute", "review"),
}
@dataclass(frozen=True)
class ClassifiedRow:
    """Classified evidence register row."""

    record_id: str
    category: str
    confidence_level: str
    source_system: str
    source_path: str
    file_name: str
    file_extension: str
    file_size_bytes: str
    modified_time_utc: str
    sha256: str
    evidence_status: str
    notes: str


def utc_now() -> str:
    """Return current UTC timestamp in ISO 8601 format."""
    return datetime.now(timezone.utc).isoformat()


def classify_text(text: str) -> tuple[str, str]:
    """Return category and confidence from deterministic keyword matching.

    Match counts are computed for each category from path and filename text.
    The category with the highest match count is selected. Confidence is then
    derived from thresholds:
    - high: matches >= HIGH_CONFIDENCE_THRESHOLD
    - medium: matches == MEDIUM_CONFIDENCE_THRESHOLD
    - low: no matches (Unknown / Review Required)
    """
    lowered = text.lower()
    best_category = "Unknown / Review Required"
    best_matches = 0

    for category, keywords in KEYWORD_MAP.items():
        matches = sum(1 for keyword in keywords if keyword in lowered)
        if matches > best_matches:
            best_matches = matches
            best_category = category

    if best_matches >= HIGH_CONFIDENCE_THRESHOLD:
        return best_category, "high"
    if best_matches == MEDIUM_CONFIDENCE_THRESHOLD:
        return best_category, "medium"
    return "Unknown / Review Required", "low"


def infer_source_system(path_text: str) -> str:
    """Infer source system from path content."""
    lowered = path_text.lower()
    if "onedrive" in lowered:
        return "OneDrive"
    if "google drive" in lowered or "gdrive" in lowered:
        return "Google Drive"
    if "downloads" in lowered:
        return "Downloads"
    if "desktop" in lowered:
        return "Desktop"
    return "Unknown"


def read_manifest(path: Path) -> list[dict[str, str]]:
    """Read source manifest rows from CSV."""
    with path.open("r", newline="", encoding="utf-8") as file_obj:
        return list(csv.DictReader(file_obj))


def build_register_rows(rows: list[dict[str, str]]) -> list[ClassifiedRow]:
    """Build classified register rows from scan manifest records."""
    register_rows: list[ClassifiedRow] = []
    for index, row in enumerate(rows, start=1):
        source_path = row.get("source_path", "")
        file_name = row.get("file_name", "")
        category, confidence = classify_text(f"{source_path} {file_name}")
        register_rows.append(
            ClassifiedRow(
                record_id=f"REG-{index:05d}",
                category=category,
                confidence_level=confidence,
                source_system=infer_source_system(source_path),
                source_path=source_path,
                file_name=file_name,
                file_extension=row.get("file_extension", ""),
                file_size_bytes=row.get("file_size_bytes", ""),
                modified_time_utc=row.get("modified_time_utc", ""),
                sha256=row.get("sha256", ""),
                evidence_status="unreviewed",
                notes="Auto-classified; requires operator review",
            )
        )
    return register_rows


def write_register(rows: list[ClassifiedRow], output_path: Path) -> None:
    """Write register CSV output."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as file_obj:
        writer = csv.writer(file_obj)
        writer.writerow(
            [
                "record_id",
                "category",
                "confidence_level",
                "source_system",
                "source_path",
                "file_name",
                "file_extension",
                "file_size_bytes",
                "modified_time_utc",
                "sha256",
                "evidence_status",
                "notes",
            ]
        )
        for row in rows:
            writer.writerow(
                [
                    row.record_id,
                    row.category,
                    row.confidence_level,
                    row.source_system,
                    row.source_path,
                    row.file_name,
                    row.file_extension,
                    row.file_size_bytes,
                    row.modified_time_utc,
                    row.sha256,
                    row.evidence_status,
                    row.notes,
                ]
            )


def append_operation_log(
    log_path: Path,
    source_location: str,
    destination_location: str,
    file_count: int,
    operator: str,
) -> None:
    """Append register build operation to the chain-of-custody log."""
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
                "classify_register",
                source_location,
                destination_location,
                file_count,
                operator,
                "success",
                "Register generated from manifest",
            ]
        )


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Build tax evidence register from scan manifest")
    parser.add_argument("--manifest", required=True, help="Input scan manifest CSV")
    parser.add_argument(
        "--output",
        default="logs/evidence_register.csv",
        help="Output evidence register CSV",
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

    manifest_rows = read_manifest(manifest)
    register_rows = build_register_rows(manifest_rows)
    write_register(register_rows, output)
    append_operation_log(
        log_path=log,
        source_location=str(manifest),
        destination_location=str(output),
        file_count=len(register_rows),
        operator=args.operator,
    )

    print(f"Register rows generated: {len(register_rows)}")
    print(f"Register written to: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
