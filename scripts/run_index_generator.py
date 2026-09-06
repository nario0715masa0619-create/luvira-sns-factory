#!/usr/bin/env python3
"""
run_index_generator.py

Phase 2-G helper: scan run folders under runs/ and generate runs/index.md
from each run.json file.

This script does NOT execute prompts, integrate with APIs, post automatically,
or modify any run.json / approval.md / metrics.md files.
It only reads run.json and writes runs/index.md.
"""

from __future__ import annotations

import argparse
import io
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_RUNS_DIR = REPO_ROOT / "runs"
DEFAULT_OUTPUT = REPO_ROOT / "runs" / "index.md"

REQUIRED_FIELDS = [
    "run_id",
    "product_service",
    "product_slug",
    "source_account_type",
    "account_type",
    "status",
]

SORT_OPTIONS = ["updated_at_desc", "created_at_desc", "run_id_desc", "status"]


def setup_stdout() -> None:
    """Reconfigure stdout for UTF-8 output on Windows terminals."""
    try:
        if isinstance(sys.stdout, io.TextIOWrapper):
            sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate runs/index.md from run.json files."
    )
    parser.add_argument(
        "--runs-dir",
        type=Path,
        default=DEFAULT_RUNS_DIR,
        help="Directory containing run folders. Default: runs/",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Output Markdown path. Default: runs/index.md",
    )
    parser.add_argument(
        "--include-archived",
        action="store_true",
        help="Include archived runs in the index.",
    )
    parser.add_argument(
        "--sort",
        default="updated_at_desc",
        choices=SORT_OPTIONS,
        help="Sort order for the Runs table. Default: updated_at_desc",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be generated without writing the file.",
    )
    return parser.parse_args()


def format_value(value) -> str:
    """Format a JSON value for Markdown table display."""
    if value is None or value == "":
        return "-"
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def parse_iso_datetime(value) -> datetime | None:
    """Parse an ISO 8601 datetime string, returning None on failure."""
    if not value:
        return None
    try:
        # Python 3.11+ handles timezone-aware ISO strings directly.
        return datetime.fromisoformat(value)
    except Exception:
        return None


def is_archived(record: dict) -> bool:
    """Determine whether a run should be treated as archived."""
    status = record.get("status", "")
    execution_mode = record.get("execution_mode", "")
    return status == "archived" or execution_mode == "archived_experiment"


def load_run_data(run_folder: Path) -> tuple[dict | None, list[str]]:
    """
    Read run.json from a run folder.

    Returns (data, warnings). data is None if the file is missing or invalid.
    """
    run_json_path = run_folder / "run.json"
    warnings: list[str] = []

    if not run_json_path.exists():
        warnings.append(
            f"run.json missing: `{run_folder.name}`"
        )
        return None, warnings

    try:
        text = run_json_path.read_text(encoding="utf-8")
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        warnings.append(
            f"invalid JSON in `{run_folder.name}/run.json`: {exc}"
        )
        return None, warnings
    except Exception as exc:
        warnings.append(
            f"failed to read `{run_folder.name}/run.json`: {exc}"
        )
        return None, warnings

    if not isinstance(data, dict):
        warnings.append(
            f"invalid JSON structure in `{run_folder.name}/run.json`: expected object"
        )
        return None, warnings

    missing_fields = [field for field in REQUIRED_FIELDS if field not in data]
    if missing_fields:
        warnings.append(
            f"missing required fields in `{run_folder.name}/run.json`: {', '.join(missing_fields)}"
        )

    run_id = data.get("run_id")
    if run_id and run_id != run_folder.name:
        warnings.append(
            f"run_id mismatch: folder `{run_folder.name}` vs run.json `{run_id}`"
        )

    return data, warnings


def scan_runs(runs_dir: Path, include_archived: bool) -> tuple[list[dict], list[str]]:
    """Scan run folders and collect run data."""
    if not runs_dir.exists():
        print(f"Error: runs directory does not exist: {runs_dir}", file=sys.stderr)
        sys.exit(1)

    if not runs_dir.is_dir():
        print(f"Error: path is not a directory: {runs_dir}", file=sys.stderr)
        sys.exit(1)

    records: list[dict] = []
    warnings: list[str] = []
    seen_run_ids: dict[str, str] = {}

    for entry in sorted(runs_dir.iterdir()):
        if not entry.is_dir():
            continue
        if entry.name in ("README.md", "index.md"):
            continue

        data, run_warnings = load_run_data(entry)
        warnings.extend(run_warnings)

        if data is None:
            continue

        record = {
            "folder_name": entry.name,
            "data": data,
        }

        if not include_archived and is_archived(data):
            continue

        records.append(record)

        run_id = data.get("run_id")
        if run_id:
            if run_id in seen_run_ids:
                warnings.append(
                    f"duplicate run_id `{run_id}`: `{seen_run_ids[run_id]}` and `{entry.name}`"
                )
            else:
                seen_run_ids[run_id] = entry.name

    return records, warnings


def sort_records(records: list[dict], sort_key: str) -> list[dict]:
    """Sort run records according to the selected key."""
    if sort_key == "updated_at_desc":
        return sorted(
            records,
            key=lambda r: parse_iso_datetime(r["data"].get("updated_at")) or datetime.min.replace(tzinfo=timezone.utc),
            reverse=True,
        )
    if sort_key == "created_at_desc":
        return sorted(
            records,
            key=lambda r: parse_iso_datetime(r["data"].get("created_at")) or datetime.min.replace(tzinfo=timezone.utc),
            reverse=True,
        )
    if sort_key == "run_id_desc":
        return sorted(records, key=lambda r: r["data"].get("run_id", ""), reverse=True)
    if sort_key == "status":
        return sorted(
            records,
            key=lambda r: (
                r["data"].get("status", ""),
                parse_iso_datetime(r["data"].get("updated_at")) or datetime.min.replace(tzinfo=timezone.utc),
            ),
            reverse=True,
        )
    return records


def count_metrics_due(records: list[dict]) -> int:
    """Count runs that have metrics due and not yet recorded."""
    now = datetime.now(timezone.utc)
    count = 0
    for record in records:
        data = record["data"]
        status = data.get("status", "")
        metrics_due_at = data.get("metrics_due_at")
        impressions = data.get("impressions_24h")

        if status in ("posted", "metrics_due") and metrics_due_at and impressions is None:
            count += 1
    return count


def count_metrics_recorded(records: list[dict]) -> int:
    """Count runs that already have 24h impressions recorded."""
    count = 0
    for record in records:
        if record["data"].get("impressions_24h") is not None:
            count += 1
    return count


def count_posted(records: list[dict]) -> int:
    """Count runs that have been posted."""
    count = 0
    for record in records:
        data = record["data"]
        if data.get("status") == "posted" or data.get("posted_at") is not None:
            count += 1
    return count


def count_pending_approval(records: list[dict]) -> int:
    """Count runs awaiting human approval."""
    return sum(1 for record in records if record["data"].get("status") == "pending_approval")


def count_archived(records: list[dict]) -> int:
    """Count archived runs among all scanned records."""
    return sum(1 for record in records if is_archived(record["data"]))


def make_run_link(run_id: str) -> str:
    """Create a Markdown relative link to a run folder."""
    return f"[{run_id}](./{run_id}/)"


def generate_summary(
    records: list[dict],
    all_records: list[dict],
    warnings: list[str],
    generated_at: str,
    include_archived: bool,
) -> str:
    """Generate the Summary section."""
    total_runs = len(all_records)
    visible_runs = len(records)
    archived_runs = count_archived(all_records)
    pending_approval = count_pending_approval(records)
    posted = count_posted(records)
    metrics_due = count_metrics_due(records)
    metrics_recorded = count_metrics_recorded(records)

    lines = [
        "## Summary",
        "",
        f"- generated_at: `{generated_at}`",
        f"- total_runs: `{total_runs}`",
        f"- visible_runs: `{visible_runs}`",
        f"- archived_runs: `{archived_runs}`",
        f"- warning_count: `{len(warnings)}`",
        f"- pending_approval_count: `{pending_approval}`",
        f"- posted_count: `{posted}`",
        f"- metrics_due_count: `{metrics_due}`",
        f"- metrics_recorded_count: `{metrics_recorded}`",
        "",
    ]
    if not include_archived:
        lines.append(
            "> Archived runs are excluded by default. Use `--include-archived` to show them."
        )
        lines.append("")
    return "\n".join(lines)


def generate_runs_table(records: list[dict]) -> str:
    """Generate the full Runs table."""
    header = (
        "| run_id | product_service | source | target | status | selected_candidate_id | "
        "human_approved | approval_status | posted_at | metrics_due_at | impressions_24h | updated_at |"
    )
    separator = (
        "|--------|-----------------|--------|--------|--------|-----------------------|"
        "----------------|-----------------|-----------|----------------|-----------------|------------|"
    )

    lines = ["## Runs", "", header, separator]

    for record in records:
        data = record["data"]
        row = (
            f"| {make_run_link(data.get('run_id', record['folder_name']))} "
            f"| {format_value(data.get('product_service'))} "
            f"| {format_value(data.get('source_account_type'))} "
            f"| {format_value(data.get('account_type'))} "
            f"| {format_value(data.get('status'))} "
            f"| {format_value(data.get('selected_candidate_id'))} "
            f"| {format_value(data.get('human_approved'))} "
            f"| {format_value(data.get('approval_status'))} "
            f"| {format_value(data.get('posted_at'))} "
            f"| {format_value(data.get('metrics_due_at'))} "
            f"| {format_value(data.get('impressions_24h'))} "
            f"| {format_value(data.get('updated_at'))} |"
        )
        lines.append(row)

    lines.append("")
    return "\n".join(lines)


def generate_pending_approval_section(records: list[dict]) -> str:
    """Generate the Pending Approval section."""
    pending = [r for r in records if r["data"].get("status") == "pending_approval"]

    lines = [
        "## Pending Approval",
        "",
        "| run_id | product_service | selected_candidate_id | approval_status | updated_at |",
        "|--------|-----------------|-----------------------|-----------------|------------|",
    ]

    for record in pending:
        data = record["data"]
        row = (
            f"| {make_run_link(data.get('run_id', record['folder_name']))} "
            f"| {format_value(data.get('product_service'))} "
            f"| {format_value(data.get('selected_candidate_id'))} "
            f"| {format_value(data.get('approval_status'))} "
            f"| {format_value(data.get('updated_at'))} |"
        )
        lines.append(row)

    lines.append("")
    return "\n".join(lines)


def generate_metrics_due_section(records: list[dict]) -> str:
    """Generate the Metrics Due section."""
    now = datetime.now(timezone.utc)

    candidates = []
    for record in records:
        data = record["data"]
        status = data.get("status", "")
        metrics_due_at = data.get("metrics_due_at")
        impressions = data.get("impressions_24h")

        if status in ("posted", "metrics_due") and metrics_due_at:
            candidates.append(record)

    lines = [
        "## Metrics Due",
        "",
        "| run_id | posted_at | metrics_due_at | impressions_24h | result_hint |",
        "|--------|-----------|----------------|-----------------|-------------|",
    ]

    for record in candidates:
        data = record["data"]
        metrics_due_at = data.get("metrics_due_at")
        impressions = data.get("impressions_24h")

        due_dt = parse_iso_datetime(metrics_due_at)
        if impressions is not None:
            hint = "metrics recorded"
        elif due_dt and due_dt < now:
            hint = "overdue"
        else:
            hint = "metrics not yet recorded"

        row = (
            f"| {make_run_link(data.get('run_id', record['folder_name']))} "
            f"| {format_value(data.get('posted_at'))} "
            f"| {format_value(metrics_due_at)} "
            f"| {format_value(impressions)} "
            f"| {hint} |"
        )
        lines.append(row)

    lines.append("")
    return "\n".join(lines)


def generate_warnings_section(warnings: list[str]) -> str:
    """Generate the Warnings section."""
    lines = ["## Warnings", ""]
    if warnings:
        for warning in warnings:
            lines.append(f"- {warning}")
    else:
        lines.append("No warnings.")
    lines.append("")
    return "\n".join(lines)


def generate_index(
    records: list[dict],
    all_records: list[dict],
    warnings: list[str],
    generated_at: str,
    include_archived: bool,
) -> str:
    """Generate the full index Markdown content."""
    sections = [
        "# Run Index",
        "",
        generate_summary(records, all_records, warnings, generated_at, include_archived),
        generate_runs_table(records),
        generate_pending_approval_section(records),
        generate_metrics_due_section(records),
        generate_warnings_section(warnings),
    ]
    return "\n".join(sections)


def main() -> int:
    setup_stdout()
    args = parse_args()

    all_records, warnings = scan_runs(args.runs_dir, include_archived=True)
    visible_records = [
        record for record in all_records
        if args.include_archived or not is_archived(record["data"])
    ]
    sorted_records = sort_records(visible_records, args.sort)

    generated_at = datetime.now(timezone.utc).astimezone().isoformat()
    markdown = generate_index(
        sorted_records,
        all_records,
        warnings,
        generated_at,
        args.include_archived,
    )

    if args.dry_run:
        print("Dry run - would generate:")
        print(f"  output: {args.output}")
        print(f"  total_runs: {len(all_records)}")
        print(f"  visible_runs: {len(sorted_records)}")
        print(f"  warning_count: {len(warnings)}")
        print(f"  pending_approval_count: {count_pending_approval(sorted_records)}")
        print(f"  metrics_due_count: {count_metrics_due(sorted_records)}")
        if warnings:
            print("\nWarnings:")
            for warning in warnings:
                print(f"  - {warning}")
        print("\nNo files were written.")
        return 0

    try:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(markdown, encoding="utf-8")
    except Exception as exc:
        print(f"Error writing index file: {exc}", file=sys.stderr)
        return 1

    print("Generated index:")
    print(f"  path: {args.output}")
    print(f"  total_runs: {len(all_records)}")
    print(f"  visible_runs: {len(sorted_records)}")
    print(f"  warning_count: {len(warnings)}")
    print(f"  pending_approval_count: {count_pending_approval(sorted_records)}")
    print(f"  metrics_due_count: {count_metrics_due(sorted_records)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
