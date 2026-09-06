#!/usr/bin/env python3
"""
Luvira SNS Factory - Run Folder Generator

Creates a new run folder under runs/ from templates/.
Does NOT execute prompts, post automatically, or integrate with APIs.
Human-in-the-loop remains mandatory.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

# Reconfigure stdout for UTF-8 on Windows terminals when possible.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, OSError):
    pass


PROJECT_ROOT = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = PROJECT_ROOT / "templates"
RUNS_DIR = PROJECT_ROOT / "runs"

REQUIRED_TEMPLATES = ["input.md", "run.json", "approval.md", "metrics.md"]
VALID_ACCOUNT_TYPES = {"personal", "corporate"}
VALID_EXECUTION_MODES = {
    "manual",
    "manual_template_dry_run",
    "file_based_semi_automation",
    "assisted_generation",
    "archived_experiment",
}


def error(message: str, cleanup_path: Path | None = None) -> None:
    """Print an error message and optionally clean up a partially created run folder."""
    print(f"Error: {message}", file=sys.stderr)
    if cleanup_path and cleanup_path.exists():
        try:
            shutil.rmtree(cleanup_path)
            print(f"Cleaned up partial run folder: {cleanup_path}", file=sys.stderr)
        except OSError as exc:
            print(f"Warning: could not clean up {cleanup_path}: {exc}", file=sys.stderr)
    sys.exit(1)


def validate_product_slug(slug: str) -> None:
    """Ensure product_slug uses only lowercase letters, numbers, and hyphens."""
    if not slug:
        error("product_slug must not be empty.")
    if not re.fullmatch(r"[a-z0-9-]+", slug):
        error(
            f"Invalid product_slug '{slug}'. "
            "Use lowercase English letters, numbers, and hyphens only. "
            "Spaces, underscores, Japanese characters, and symbols are not allowed."
        )


def validate_account_type(name: str, value: str) -> None:
    """Validate source_account_type / account_type values."""
    if value not in VALID_ACCOUNT_TYPES:
        error(f"Invalid {name} '{value}'. Must be one of: {sorted(VALID_ACCOUNT_TYPES)}.")


def validate_execution_mode(mode: str) -> None:
    """Validate execution_mode value."""
    if mode not in VALID_EXECUTION_MODES:
        error(
            f"Invalid execution_mode '{mode}'. "
            f"Must be one of: {sorted(VALID_EXECUTION_MODES)}."
        )


def default_cta_style(account_type: str) -> str:
    if account_type == "personal":
        return "reply / discussion / experience_sharing"
    return "checklist / consultation / document_request"


def default_persona_expression(account_type: str) -> str:
    if account_type == "personal":
        return "僕 / 私 / 自分 / 主語省略"
    return "当社 / 弊社 / 主語省略"


def default_risk_tolerance(account_type: str) -> str:
    if account_type == "personal":
        return "balanced"
    return "conservative"


def generate_run_id(
    product_slug: str, source_account_type: str, account_type: str, created_at: datetime
) -> str:
    timestamp = created_at.strftime("%Y%m%d-%H%M")
    return f"{timestamp}-{product_slug}-{source_account_type}-to-{account_type}"


def ensure_templates_exist() -> None:
    missing = [name for name in REQUIRED_TEMPLATES if not (TEMPLATES_DIR / name).exists()]
    if missing:
        error(f"Missing required template files in {TEMPLATES_DIR}: {', '.join(missing)}")


def build_run_context(args: argparse.Namespace, created_at: datetime, run_id: str) -> dict:
    """Build the substitution context shared across markdown templates."""
    return {
        "RUN_ID": run_id,
        "PRODUCT_NAME": args.product_service,
        "PRODUCT_SLUG": args.product_slug,
        "SOURCE_ACCOUNT_TYPE": args.source_account_type,
        "ACCOUNT_TYPE": args.account_type,
        "DESIRED_CTA_STYLE": args.desired_cta_style,
        "PERSONA_OPTIONS": args.allowed_persona_expression,
        "RISK_TOLERANCE": args.risk_tolerance,
        "TARGET_PLATFORM": args.target_platform,
        "TARGET_AUDIENCE": args.target_audience or "",
        "BUSINESS_GOAL": args.business_goal or "",
        "MODEL": args.model,
        "EXECUTION_MODE": args.execution_mode,
        "SOURCE_POST_REFERENCE_TYPE": args.source_post_reference_type,
        "SOURCE_POST_STORAGE_POLICY": args.source_post_storage_policy,
        "CREATED_AT": created_at.isoformat(),
        "YYYY-MM-DDTHH:MM:SS+09:00": created_at.isoformat(),
        "YYYYMMDD-HHMM-{product-slug}-{source-account-type}-to-{account-type}": run_id,
        "personal_or_corporate": args.account_type,
        "CANDIDATE_ID": "",
        "NUMBER": "",
        "PERCENTAGE": "",
    }


def substitute_markdown(text: str, context: dict) -> str:
    """Replace placeholder tokens in markdown templates."""
    result = text
    for key, value in context.items():
        result = result.replace(f"`{key}`", f"`{value}`")
        result = result.replace(f"[{key}]", value)
    return result


def add_generated_metadata(text: str, context: dict) -> str:
    """Append a Generated Metadata section if the template did not contain obvious placeholders."""
    lines = [
        "",
        "---",
        "",
        "## Generated Metadata",
        "",
        f"- run_id: `{context['RUN_ID']}`",
        f"- product_service: `{context['PRODUCT_NAME']}`",
        f"- product_slug: `{context['PRODUCT_SLUG']}`",
        f"- source_account_type: `{context['SOURCE_ACCOUNT_TYPE']}`",
        f"- account_type: `{context['ACCOUNT_TYPE']}`",
        f"- desired_cta_style: `{context['DESIRED_CTA_STYLE']}`",
        f"- allowed_persona_expression: `{context['PERSONA_OPTIONS']}`",
        f"- risk_tolerance: `{context['RISK_TOLERANCE']}`",
        f"- target_platform: `{context['TARGET_PLATFORM']}`",
        f"- target_audience: `{context['TARGET_AUDIENCE']}`",
        f"- business_goal: `{context['BUSINESS_GOAL']}`",
        f"- model: `{context['MODEL']}`",
        f"- execution_mode: `{context['EXECUTION_MODE']}`",
        f"- created_at: `{context['CREATED_AT']}`",
        "",
    ]
    return text + "\n".join(lines)


def normalize_account_config_lines(text: str, context: dict) -> str:
    """Replace template hint lines with concrete values in input.md."""
    text = re.sub(
        r"^(- source_account_type:\s*)(?:`personal` or `corporate`|personal or corporate|PERSONA_OPTIONS)",
        rf"\1`{context['SOURCE_ACCOUNT_TYPE']}`",
        text,
        flags=re.MULTILINE,
    )
    text = re.sub(
        r"^(- account_type:\s*)(?:`personal` or `corporate`|personal or corporate|PERSONA_OPTIONS)",
        rf"\1`{context['ACCOUNT_TYPE']}`",
        text,
        flags=re.MULTILINE,
    )
    text = re.sub(
        r"^(- desired_cta_style:\s*)(?:`reply / discussion / experience_sharing` or `checklist / consultation / document_request`|reply / discussion / experience_sharing OR checklist / consultation / document_request|DESIRED_CTA_STYLE)",
        rf"\1`{context['DESIRED_CTA_STYLE']}`",
        text,
        flags=re.MULTILINE,
    )
    text = re.sub(
        r"^(- allowed_persona_expression:\s*)(?:`PERSONA_OPTIONS`|PERSONA_OPTIONS|`僕 / 私 / 自分 / 主語省略` or `当社 / 弊社 / 主語省略`)",
        rf"\1`{context['PERSONA_OPTIONS']}`",
        text,
        flags=re.MULTILINE,
    )
    text = re.sub(
        r"^(- risk_tolerance:\s*)(?:`balanced` or `conservative`|balanced or conservative|RISK_TOLERANCE)",
        rf"\1`{context['RISK_TOLERANCE']}`",
        text,
        flags=re.MULTILINE,
    )
    text = re.sub(
        r"^(- source_post_reference_type:\s*)(?:`fictional_sample` or `client_original`|fictional_sample or client_original|SOURCE_POST_REFERENCE_TYPE)",
        rf"\1`{context['SOURCE_POST_REFERENCE_TYPE']}`",
        text,
        flags=re.MULTILINE,
    )
    return text


def prefill_input_md(src: Path, dest: Path, context: dict) -> None:
    text = src.read_text(encoding="utf-8")
    text = substitute_markdown(text, context)
    text = normalize_account_config_lines(text, context)
    if "## Generated Metadata" not in text:
        text = add_generated_metadata(text, context)
    dest.write_text(text, encoding="utf-8")


def prefill_approval_md(src: Path, dest: Path, context: dict) -> None:
    text = src.read_text(encoding="utf-8")
    text = substitute_markdown(text, context)

    # Ensure Risk Review shows pending for pre-execution state.
    text = re.sub(
        r"^\| (Fabricated experience \| )pending / low / medium / high / rejected",
        r"| \1pending",
        text,
        flags=re.MULTILINE,
    )
    text = re.sub(
        r"^\| (Unsubstantiated claims \| )pending / low / medium / high / rejected",
        r"| \1pending",
        text,
        flags=re.MULTILINE,
    )
    text = re.sub(
        r"^\| (Effect guarantee \| )pending / low / medium / high / rejected",
        r"| \1pending",
        text,
        flags=re.MULTILINE,
    )
    text = re.sub(
        r"^\| (Fear-mongering \| )pending / low / medium / high / rejected",
        r"| \1pending",
        text,
        flags=re.MULTILINE,
    )
    text = re.sub(
        r"^\| (Account type mismatch \| )pending / low / medium / high / rejected",
        r"| \1pending",
        text,
        flags=re.MULTILINE,
    )
    text = re.sub(
        r"^\| (CTA mismatch \| )pending / low / medium / high / rejected",
        r"| \1pending",
        text,
        flags=re.MULTILINE,
    )
    text = re.sub(
        r"^\| (Product pushiness \| )pending / low / medium / high / rejected",
        r"| \1pending",
        text,
        flags=re.MULTILINE,
    )
    text = re.sub(
        r"^\| (Controversy risk \| )pending / low / medium / high / rejected",
        r"| \1pending",
        text,
        flags=re.MULTILINE,
    )

    if "## Generated Metadata" not in text:
        text = add_generated_metadata(text, context)
    dest.write_text(text, encoding="utf-8")


def prefill_metrics_md(src: Path, dest: Path, context: dict) -> None:
    text = src.read_text(encoding="utf-8")
    text = substitute_markdown(text, context)

    # Mark result verdict as invalid_missing_metrics in initial state.
    text = text.replace(
        "- [ ] **invalid_missing_metrics** — metrics could not be recorded.",
        "- [x] **invalid_missing_metrics** — metrics could not be recorded.",
    )

    # Ensure posted timing fields are blank/null placeholders, not creation time.
    text = re.sub(
        r"^- posted_at:\s*`[^`]+`",
        "- posted_at: `YYYY-MM-DDTHH:MM:SS+09:00`",
        text,
        flags=re.MULTILINE,
    )
    text = re.sub(
        r"^- metrics_due_at:\s*`[^`]+`",
        "- metrics_due_at: `YYYY-MM-DDTHH:MM:SS+09:00`",
        text,
        flags=re.MULTILINE,
    )
    text = re.sub(
        r"^- metrics_recorded_at:\s*`[^`]+`",
        "- metrics_recorded_at: `YYYY-MM-DDTHH:MM:SS+09:00`",
        text,
        flags=re.MULTILINE,
    )

    if "## Generated Metadata" not in text:
        text = add_generated_metadata(text, context)
    dest.write_text(text, encoding="utf-8")


def prefill_run_json(src: Path, dest: Path, context: dict) -> None:
    data = json.loads(src.read_text(encoding="utf-8"))

    now_iso = context["CREATED_AT"]

    data["run_id"] = context["RUN_ID"]
    data["created_at"] = now_iso
    data["updated_at"] = now_iso
    data["product_service"] = context["PRODUCT_NAME"]
    data["product_slug"] = context["PRODUCT_SLUG"]
    data["source_account_type"] = context["SOURCE_ACCOUNT_TYPE"]
    data["account_type"] = context["ACCOUNT_TYPE"]
    data["desired_cta_style"] = context["DESIRED_CTA_STYLE"]
    data["allowed_persona_expression"] = context["PERSONA_OPTIONS"]
    data["risk_tolerance"] = context["RISK_TOLERANCE"]
    data["source_post_reference_type"] = context["SOURCE_POST_REFERENCE_TYPE"]
    data["source_post_storage_policy"] = context["SOURCE_POST_STORAGE_POLICY"]
    data["target_platform"] = context["TARGET_PLATFORM"]
    data["target_audience"] = context["TARGET_AUDIENCE"]
    data["business_goal"] = context["BUSINESS_GOAL"]
    data["prompt_version"] = "phase-1-final"
    data["model"] = context["MODEL"]
    data["execution_mode"] = context["EXECUTION_MODE"]
    data["status"] = "draft"
    data["current_step"] = None
    data["final_verdict"] = None
    data["selected_candidate_id"] = None
    data["selected_candidate_text"] = None
    data["human_approved"] = False
    data["approval_status"] = "pending"
    data["approved_by"] = None
    data["approved_at"] = None
    data["posted_at"] = None
    data["post_url"] = None
    data["metrics_due_at"] = None
    data["impressions_24h"] = None
    data["engagement_24h"] = None
    data["clicks_24h"] = None
    data["replies_24h"] = None

    # Replace placeholder values in client_context if they were not pre-filled.
    client_context = data.get("client_context", {})
    if client_context.get("target_audience") == "TARGET_AUDIENCE":
        client_context["target_audience"] = context["TARGET_AUDIENCE"]
    if client_context.get("posting_purpose") == "POSTING_PURPOSE":
        client_context["posting_purpose"] = context["BUSINESS_GOAL"]
    if client_context.get("tone") == "TONE":
        client_context["tone"] = ""
    if client_context.get("industry") == "INDUSTRY":
        client_context["industry"] = ""

    # Normalize step input/output paths inside the run folder.
    for step in data.get("steps", []):
        step["status"] = "pending"
        step["completed_at"] = None
        step["notes"] = ""
        step_name_slug = step["name"].lower().replace(" ", "-")
        step["input_path"] = f"step-{step['step_id']}-{step_name_slug}-input.md"
        step["output_path"] = f"step-{step['step_id']}-{step_name_slug}.md"

    dest.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def create_run_folder(args: argparse.Namespace) -> tuple[Path, dict]:
    """Create and pre-fill a new run folder."""
    ensure_templates_exist()

    created_at = args.created_at or datetime.now(timezone.utc).astimezone()
    run_id = args.run_id or generate_run_id(
        args.product_slug, args.source_account_type, args.account_type, created_at
    )

    run_folder = RUNS_DIR / run_id
    if run_folder.exists():
        error(
            f"Run folder already exists: {run_folder}\n"
            "Use --run-id to specify a unique ID, or remove the existing folder first."
        )

    if args.dry_run:
        return run_folder, {
            "run_id": run_id,
            "run_folder": str(run_folder),
            "files": REQUIRED_TEMPLATES,
            "created_at": created_at.isoformat(),
        }

    try:
        run_folder.mkdir(parents=True, exist_ok=False)
    except OSError as exc:
        error(f"Could not create run folder {run_folder}: {exc}")

    context = build_run_context(args, created_at, run_id)

    try:
        prefill_input_md(TEMPLATES_DIR / "input.md", run_folder / "input.md", context)
        prefill_run_json(TEMPLATES_DIR / "run.json", run_folder / "run.json", context)
        prefill_approval_md(TEMPLATES_DIR / "approval.md", run_folder / "approval.md", context)
        prefill_metrics_md(TEMPLATES_DIR / "metrics.md", run_folder / "metrics.md", context)
    except Exception as exc:
        error(f"Failed to pre-fill run files: {exc}", cleanup_path=run_folder)

    return run_folder, context


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a new Luvira SNS Factory run folder from templates."
    )
    parser.add_argument("--product-service", required=True, help="Product or service name.")
    parser.add_argument(
        "--product-slug",
        required=True,
        help="Short folder-safe product slug (lowercase letters, numbers, hyphens only).",
    )
    parser.add_argument(
        "--source-account-type",
        required=True,
        choices=["personal", "corporate"],
        help="Source account type.",
    )
    parser.add_argument(
        "--account-type",
        required=True,
        choices=["personal", "corporate"],
        help="Target account type.",
    )
    parser.add_argument(
        "--desired-cta-style",
        help="Desired CTA style. Defaults based on account_type.",
    )
    parser.add_argument(
        "--allowed-persona-expression",
        help="Allowed persona expression. Defaults based on account_type.",
    )
    parser.add_argument(
        "--risk-tolerance",
        help="Risk tolerance. Defaults based on account_type.",
    )
    parser.add_argument("--target-platform", default="X", help="Target platform. Default: X")
    parser.add_argument("--target-audience", help="Target audience for this run.")
    parser.add_argument("--business-goal", help="Business goal for this run.")
    parser.add_argument(
        "--model", default="kimi-k2.7-code", help="Model name. Default: kimi-k2.7-code"
    )
    parser.add_argument(
        "--execution-mode",
        default="file_based_semi_automation",
        choices=list(VALID_EXECUTION_MODES),
        help="Execution mode. Default: file_based_semi_automation",
    )
    parser.add_argument(
        "--created-at",
        type=datetime.fromisoformat,
        help="Override creation timestamp (ISO 8601).",
    )
    parser.add_argument(
        "--run-id",
        help="Override run_id. If omitted, generated from timestamp and parameters.",
    )
    parser.add_argument(
        "--source-post-reference-type",
        default="structure_only",
        help="Source post reference type. Default: structure_only",
    )
    parser.add_argument(
        "--source-post-storage-policy",
        default="do_not_save_third_party_text",
        help="Source post storage policy. Default: do_not_save_third_party_text",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be created without creating files.",
    )

    return parser.parse_args()


def apply_defaults(args: argparse.Namespace) -> argparse.Namespace:
    """Apply account-type-dependent defaults after parsing."""
    if not args.desired_cta_style:
        args.desired_cta_style = default_cta_style(args.account_type)
    if not args.allowed_persona_expression:
        args.allowed_persona_expression = default_persona_expression(args.account_type)
    if not args.risk_tolerance:
        args.risk_tolerance = default_risk_tolerance(args.account_type)
    return args


def main() -> None:
    args = parse_args()
    args = apply_defaults(args)

    validate_product_slug(args.product_slug)
    validate_account_type("source_account_type", args.source_account_type)
    validate_account_type("account_type", args.account_type)
    validate_execution_mode(args.execution_mode)

    run_folder, context_or_info = create_run_folder(args)

    if args.dry_run:
        info = context_or_info
        print("Dry run - would create:")
        print(f"  run_id: {info['run_id']}")
        print(f"  run_folder: {info['run_folder']}")
        print("  files:")
        for filename in info["files"]:
            print(f"    - {filename}")
        print(f"  created_at: {info['created_at']}")
        print("\nNo files were created.")
        return

    context = context_or_info
    print("Created run folder:")
    print(f"  {run_folder}")
    print("\nGenerated files:")
    for filename in REQUIRED_TEMPLATES:
        print(f"  - {run_folder / filename}")
    print(f"\nrun_id: {context['RUN_ID']}")
    print(f"product_service: {context['PRODUCT_NAME']}")
    print(f"source_account_type: {context['SOURCE_ACCOUNT_TYPE']}")
    print(f"account_type: {context['ACCOUNT_TYPE']}")
    print("status: draft")
    print("\nNext manual step:")
    print(
        f"Open {run_folder / 'input.md'} and fill "
        "source_post_structure_summary / source_post_emotion_summary before running Step 01."
    )


if __name__ == "__main__":
    main()
