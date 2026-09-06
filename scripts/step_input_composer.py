#!/usr/bin/env python3
"""
step_input_composer.py

Phase 2-H helper: compose the input Markdown for the next step of the
10-step prompt chain. The generated file is intended to be copied and pasted
into Kimi/OpenCode by a human. This script does NOT execute prompts,
integrate with APIs, or post automatically.
"""

from __future__ import annotations

import argparse
import io
import json
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_RUNS_DIR = REPO_ROOT / "runs"
DEFAULT_PROMPTS_DIR = REPO_ROOT / "prompts"

STEP_MAPPING: dict[str, str] = {
    "01": "pattern-miner",
    "02": "emotion-mapper",
    "03": "skeleton-builder",
    "04": "adaptation-writer",
    "05": "variation-generator",
    "06": "hook-specialist",
    "07": "similarity-guard",
    "08": "risk-filter",
    "09": "market-judge",
    "10": "final-packager",
}

STEP_PROMPT_FILE: dict[str, str] = {
    step_id: f"{step_id}-{step_name}.md"
    for step_id, step_name in STEP_MAPPING.items()
}

STEP_OUTPUT_FILE: dict[str, str] = {
    step_id: f"step-{step_id}-{step_name}.md"
    for step_id, step_name in STEP_MAPPING.items()
}

REQUIRED_RUN_METADATA = [
    "run_id",
    "product_service",
    "product_slug",
    "source_account_type",
    "account_type",
    "desired_cta_style",
    "allowed_persona_expression",
    "risk_tolerance",
    "target_platform",
    "target_audience",
    "business_goal",
    "model",
    "execution_mode",
]


def setup_stdout() -> None:
    """Reconfigure stdout for UTF-8 output on Windows terminals."""
    try:
        if isinstance(sys.stdout, io.TextIOWrapper):
            sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compose the input Markdown for the next step of the prompt chain."
    )
    parser.add_argument(
        "--run-id",
        required=True,
        help="Run ID (must match an existing run folder under runs/).",
    )
    parser.add_argument(
        "--next-step",
        required=True,
        choices=list(STEP_MAPPING.keys()),
        help="Next step number (01-10).",
    )
    parser.add_argument(
        "--runs-dir",
        type=Path,
        default=DEFAULT_RUNS_DIR,
        help="Directory containing run folders. Default: runs/",
    )
    parser.add_argument(
        "--prompts-dir",
        type=Path,
        default=DEFAULT_PROMPTS_DIR,
        help="Directory containing prompt files. Default: prompts/",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output file path. Default: runs/{run_id}/step-{next-step}-{name}-input.md",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be generated without writing the file.",
    )
    return parser.parse_args()


def error(message: str) -> None:
    print(f"Error: {message}", file=sys.stderr)
    sys.exit(1)


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        error(f"Required file not found: {path}")
    except Exception as exc:
        error(f"Failed to read {path}: {exc}")
    return ""  # unreachable


def load_run_json(path: Path) -> dict:
    text = read_text(path)
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        error(f"Invalid JSON in {path}: {exc}")
        return {}  # unreachable

    if not isinstance(data, dict):
        error(f"Invalid JSON structure in {path}: expected object")
        return {}  # unreachable

    return data


def extract_sections(text: str, section_titles: list[str]) -> str:
    """Extract named markdown sections from text, preserving subsections."""
    # Build a list of (position, level, title) for all Markdown headers.
    header_pattern = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
    headers = [
        (match.start(), len(match.group(1)), match.group(2).strip())
        for match in header_pattern.finditer(text)
    ]

    extracted_parts: list[str] = []
    target_titles = {title.lower() for title in section_titles}

    for i, (pos, level, title) in enumerate(headers):
        if title.lower() not in target_titles:
            continue

        section_start = pos
        section_end = len(text)
        for next_pos, next_level, _ in headers[i + 1 :]:
            if next_level <= level:
                section_end = next_pos
                break

        extracted_parts.append(text[section_start:section_end].rstrip())

    return "\n\n".join(extracted_parts)


def get_step_01_source_input(input_md_text: str) -> str:
    """Extract relevant sections from input.md for Step 01."""
    sections = extract_sections(
        input_md_text,
        [
            "Source Post Structure Summary",
            "Source Post Emotion Summary",
            "Step 01 Input for Pattern Miner",
        ],
    )
    if not sections:
        return input_md_text
    return sections


def format_metadata_value(value) -> str:
    if value is None or value == "":
        return "-"
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def generate_run_metadata(run_data: dict) -> str:
    lines = ["## Run Metadata", ""]
    for key in REQUIRED_RUN_METADATA:
        value = run_data.get(key)
        lines.append(f"- {key}: `{format_metadata_value(value)}`")

    status = run_data.get("status")
    current_step = run_data.get("current_step")
    lines.append(f"- status: `{format_metadata_value(status)}`")
    lines.append(f"- current_step: `{format_metadata_value(current_step)}`")
    lines.append("")

    missing = [key for key in REQUIRED_RUN_METADATA if run_data.get(key) in (None, "")]
    if missing:
        lines.append(
            "> **Warning:** The following metadata fields are missing or empty: "
            f"{', '.join(missing)}"
        )
        lines.append("")

    return "\n".join(lines)


def generate_source_input_section(
    next_step: str,
    input_md_text: str,
    previous_output_text: str | None,
) -> str:
    lines = ["## Source Input", ""]

    if next_step == "01":
        lines.append(
            "The following sections are extracted from `input.md`. "
            "They contain the source post summary and the instructions for Step 01."
        )
        lines.append("")
        source_input = get_step_01_source_input(input_md_text)
    else:
        lines.append(
            "The following content is the output from the previous step. "
            "Use it as the primary input for the next step."
        )
        lines.append("")
        source_input = previous_output_text or ""

    lines.append(source_input)
    lines.append("")
    return "\n".join(lines)


def generate_prompt_section(prompt_text: str) -> str:
    lines = [
        "## Prompt To Apply",
        "",
        "Apply the following prompt to the Source Input above.",
        "",
        prompt_text,
        "",
    ]
    return "\n".join(lines)


def generate_execution_instruction(next_step: str, output_path: Path) -> str:
    step_name = STEP_MAPPING[next_step]
    output_file = STEP_OUTPUT_FILE[next_step]
    return (
        "## Execution Instruction\n"
        "\n"
        f"1. Copy the entire content of this file (`{output_path.name}`).\n"
        "2. Paste it into Kimi/OpenCode as a new request.\n"
        f"3. Save the AI response to `{output_file}` in the same run folder.\n"
        "4. Review the output before proceeding to the next step.\n"
        "\n"
        "> **Important:** This is a manual step. The script does not execute prompts, "
        "call APIs, or post automatically.\n"
    )


def compose_input(
    next_step: str,
    run_data: dict,
    input_md_text: str,
    previous_output_text: str | None,
    prompt_text: str,
    output_path: Path,
) -> str:
    step_name = STEP_MAPPING[next_step]
    sections = [
        f"# Step {next_step}: {step_name.replace('-', ' ').title()} Input",
        "",
        generate_run_metadata(run_data),
        generate_source_input_section(next_step, input_md_text, previous_output_text),
        generate_prompt_section(prompt_text),
        generate_execution_instruction(next_step, output_path),
    ]
    return "\n".join(sections)


def main() -> int:
    setup_stdout()
    args = parse_args()

    run_folder = args.runs_dir / args.run_id
    if not run_folder.is_dir():
        error(f"Run folder does not exist: {run_folder}")

    run_json_path = run_folder / "run.json"
    input_md_path = run_folder / "input.md"
    prompt_path = args.prompts_dir / STEP_PROMPT_FILE[args.next_step]

    previous_step = None
    previous_output_path = None
    if args.next_step != "01":
        prev_num = str(int(args.next_step) - 1).zfill(2)
        previous_step = prev_num
        previous_output_path = run_folder / STEP_OUTPUT_FILE[prev_num]

    output_path = args.output
    if output_path is None:
        output_path = run_folder / f"step-{args.next_step}-{STEP_MAPPING[args.next_step]}-input.md"

    if args.dry_run:
        print("Dry run - would generate:")
        print(f"  run folder: {run_folder}")
        print(f"  run.json: {run_json_path}")
        print(f"  input.md: {input_md_path}")
        print(f"  prompt file: {prompt_path}")
        if previous_output_path:
            print(f"  previous step output: {previous_output_path}")
        print(f"  output file: {output_path}")
        print("\nNo files were written.")
        return 0

    if output_path.exists():
        error(
            f"Output file already exists: {output_path}\n"
            "Remove it first or specify a different --output path."
        )

    run_data = load_run_json(run_json_path)
    input_md_text = read_text(input_md_path)
    prompt_text = read_text(prompt_path)

    previous_output_text = None
    if previous_output_path:
        previous_output_text = read_text(previous_output_path)

    composed = compose_input(
        args.next_step,
        run_data,
        input_md_text,
        previous_output_text,
        prompt_text,
        output_path,
    )

    try:
        output_path.write_text(composed, encoding="utf-8")
    except Exception as exc:
        error(f"Failed to write {output_path}: {exc}")

    print("Composed step input:")
    print(f"  output: {output_path}")
    print(f"  run_id: {args.run_id}")
    print(f"  next_step: {args.next_step}")
    print(f"  prompt: {prompt_path.name}")
    if previous_output_path:
        print(f"  previous_output: {previous_output_path.name}")
    print("\nNext manual step:")
    print(f"  Copy the content of {output_path.name} and paste it into Kimi/OpenCode.")
    print(f"  Save the response to {STEP_OUTPUT_FILE[args.next_step]}.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
