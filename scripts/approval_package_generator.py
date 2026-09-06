#!/usr/bin/env python3
"""
approval_package_generator.py

Phase 2-F helper: generate final-candidates.md and update approval.md
from step-09-market-judge.md and step-10-final-packager.md.

This script does NOT execute prompts, integrate with APIs, or post automatically.
It only formats existing step outputs into a human-review package.
"""

from __future__ import annotations

import argparse
import io
import json
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = REPO_ROOT / "templates"
RUNS_DIR = REPO_ROOT / "runs"


def setup_stdout() -> None:
    """Reconfigure stdout for UTF-8 output on Windows terminals."""
    try:
        if isinstance(sys.stdout, io.TextIOWrapper):
            sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate final approval package from step-09 and step-10 outputs."
    )
    parser.add_argument(
        "--run-id",
        required=True,
        help="Run ID (must match an existing run folder under runs/).",
    )
    parser.add_argument(
        "--step-09",
        default="step-09-market-judge.md",
        help="Filename of step 09 output inside the run folder.",
    )
    parser.add_argument(
        "--step-10",
        default="step-10-final-packager.md",
        help="Filename of step 10 output inside the run folder.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be generated without writing files.",
    )
    return parser.parse_args()


def validate_run_folder(run_id: str) -> Path:
    run_folder = RUNS_DIR / run_id
    if not run_folder.is_dir():
        print(f"Error: Run folder does not exist: {run_folder}", file=sys.stderr)
        sys.exit(1)
    return run_folder


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Error: Required file not found: {path}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading {path}: {e}", file=sys.stderr)
        sys.exit(1)


def parse_step_09(text: str) -> dict:
    """Parse step-09-market-judge.md output."""
    result: dict = {
        "account_type": None,
        "desired_cta_style": None,
        "scores": {},
        "top5": [],
        "recommended": {
            "candidate_id": None,
            "text": None,
            "reason": None,
        },
    }

    # account_type and desired_cta_style
    m = re.search(r"[-*]\s*account_type:\s*`?\s*(personal|corporate)\s*`?", text, re.IGNORECASE)
    if m:
        result["account_type"] = m.group(1).lower()

    m = re.search(
        r"[-*]\s*desired_cta_style:\s*`?\s*([^`\n]+?)\s*`?",
        text,
        re.IGNORECASE,
    )
    if m:
        result["desired_cta_style"] = m.group(1).strip()

    # Score table
    score_table_pattern = re.compile(
        r"^\|\s*案\s*No\s*\|.*?\|\s*備考\s*\|\s*\n"
        r"^\|[-\s|]+\|\s*\n"
        r"((?:^\|\s*\d+\s*\|.*?\|\s*\n)+)",
        re.MULTILINE | re.IGNORECASE,
    )
    m = score_table_pattern.search(text)
    if m:
        rows_text = m.group(1)
        for row in rows_text.strip().splitlines():
            cells = [cell.strip() for cell in row.split("|")]
            # cells[0] is empty leading cell, cells[1] is 案 No, etc.
            if len(cells) < 10:
                continue
            candidate_id = cells[1].strip().zfill(2)
            try:
                total = int(cells[8]) if cells[8].isdigit() else cells[8]
            except Exception:
                total = cells[8]
            result["scores"][candidate_id] = {
                "インプ": cells[2],
                "ブランド": cells[3],
                "パクリ感": cells[4],
                "共感": cells[5],
                "フック": cells[6],
                "account_type": cells[7],
                "合計": total,
                "備考": cells[9],
            }

    # Top 5 section
    top5_match = re.search(
        r"###\s*上位\s*5\s*本\s*\n(.*?)(?=###\s*最終おすすめ\s*1\s*本|$)",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if top5_match:
        section = top5_match.group(1)
        for line in section.splitlines():
            m = re.match(r"^\s*\d+\.\s*案\s*(\d+)\s*[:：]\s*(.+)$", line)
            if m:
                candidate_id = m.group(1).zfill(2)
                candidate_text = m.group(2).strip()
                result["top5"].append(
                    {
                        "candidate_id": candidate_id,
                        "text": candidate_text,
                    }
                )

    # Recommended candidate
    rec_match = re.search(
        r"###\s*最終おすすめ\s*1\s*本\s*\n(.*)",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if rec_match:
        section = rec_match.group(1)
        m = re.search(r"\*\*案\s*(\d+)\*\*", section)
        if m:
            result["recommended"]["candidate_id"] = m.group(1).zfill(2)

        # Text is between **案 No** and **選定理由:**
        text_match = re.search(
            r"\*\*案\s*\d+\*\*\s*\n(.*?)(?=\*\*選定理由[:：]?\*\*|$)",
            section,
            re.DOTALL,
        )
        if text_match:
            result["recommended"]["text"] = text_match.group(1).strip()

        reason_match = re.search(
            r"\*\*選定理由[:：]?\*\*\s*\n(.*?)(?=\*\*|$)",
            section,
            re.DOTALL,
        )
        if reason_match:
            result["recommended"]["reason"] = reason_match.group(1).strip()

    return result


def parse_step_10(text: str) -> dict:
    """Parse step-10-final-packager.md output."""
    result: dict = {
        "account_type": None,
        "source_account_type": None,
        "top5": {},
        "recommended": {
            "candidate_id": None,
            "text": None,
            "reason": None,
            "expected_reaction": None,
        },
    }

    m = re.search(r"[-*]\s*account_type:\s*`?\s*(personal|corporate)\s*`?", text, re.IGNORECASE)
    if m:
        result["account_type"] = m.group(1).lower()

    m = re.search(
        r"[-*]\s*source_account_type:\s*`?\s*(personal|corporate)\s*`?",
        text,
        re.IGNORECASE,
    )
    if m:
        result["source_account_type"] = m.group(1).lower()

    # Top 5 section
    top5_match = re.search(
        r"##\s*上位\s*5\s*本\s*\n(.*?)(?=##\s*最終おすすめ\s*1\s*本|$)",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if top5_match:
        section = top5_match.group(1)
        # Split by candidate headings
        candidate_blocks = re.split(
            r"\n###\s*案\s*(\d+)\s*（推奨順位:\s*(\d+)）\s*\n",
            section,
        )
        # candidate_blocks[0] is preamble, then [candidate_id, rank, content, ...]
        i = 1
        while i + 2 <= len(candidate_blocks):
            candidate_num = candidate_blocks[i].zfill(2)
            rank = candidate_blocks[i + 1]
            content = candidate_blocks[i + 2]

            text_match = re.search(r"^(.*?)(?=\*\*選定理由[:：]?\*\*|$)", content, re.DOTALL)
            candidate_text = text_match.group(1).strip() if text_match else content.strip()

            reason_match = re.search(
                r"\*\*選定理由[:：]?\*\*\s*\n(.*?)(?=\*\*リスクコメント[:：]?\*\*|$)",
                content,
                re.DOTALL,
            )
            reason = reason_match.group(1).strip() if reason_match else ""

            risk_match = re.search(
                r"\*\*リスクコメント[:：]?\*\*\s*\n(.*?)(?=\n###\s*案|$)",
                content,
                re.DOTALL,
            )
            risk = risk_match.group(1).strip() if risk_match else ""

            result["top5"][candidate_num] = {
                "rank": rank,
                "text": candidate_text,
                "reason": reason,
                "risk_comment": risk,
            }
            i += 3

    # Recommended candidate
    rec_match = re.search(
        r"##\s*最終おすすめ\s*1\s*本\s*\n(.*)",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if rec_match:
        section = rec_match.group(1)
        m = re.search(r"###\s*案\s*(\d+)", section)
        if m:
            result["recommended"]["candidate_id"] = m.group(1).zfill(2)

        text_match = re.search(
            r"###\s*案\s*\d+\s*\n(.*?)(?=\*\*採用理由[:：]?\*\*|$)",
            section,
            re.DOTALL,
        )
        if text_match:
            result["recommended"]["text"] = text_match.group(1).strip()

        reason_match = re.search(
            r"\*\*採用理由[:：]?\*\*\s*\n(.*?)(?=\*\*予想される反応[:：]?\*\*|$)",
            section,
            re.DOTALL,
        )
        if reason_match:
            result["recommended"]["reason"] = reason_match.group(1).strip()

        reaction_match = re.search(
            r"\*\*予想される反応[:：]?\*\*\s*\n(.*?)(?=\n##|$)",
            section,
            re.DOTALL,
        )
        if reaction_match:
            result["recommended"]["expected_reaction"] = reaction_match.group(1).strip()

    return result


def merge_candidates(step09: dict, step10: dict) -> dict:
    """Merge step-09 (scores, ranking) and step-10 (full texts, reasons)."""
    merged: dict = {
        "account_type": step10.get("account_type") or step09.get("account_type"),
        "source_account_type": step10.get("source_account_type"),
        "desired_cta_style": step09.get("desired_cta_style"),
        "candidates": {},
        "recommended": {
            "candidate_id": None,
            "text": None,
            "reason": None,
            "expected_reaction": None,
        },
    }

    # Build candidates from step-09 top5 order (rank 1 = candidate_id "01")
    for rank_index, cand09 in enumerate(step09.get("top5", [])):
        candidate_id = str(rank_index + 1).zfill(2)
        # Prefer step-09 candidate_id if it matches the rank order
        if cand09.get("candidate_id"):
            candidate_id = cand09["candidate_id"]

        text = cand09.get("text", "")
        reason = ""
        risk_comment = ""

        cand10 = step10.get("top5", {}).get(candidate_id)
        if cand10:
            text = cand10.get("text") or text
            reason = cand10.get("reason", "")
            risk_comment = cand10.get("risk_comment", "")

        score = step09.get("scores", {}).get(candidate_id, {})

        merged["candidates"][candidate_id] = {
            "rank": rank_index + 1,
            "text": text,
            "market_score": score.get("合計", ""),
            "judge_comment": score.get("備考", ""),
            "detailed_reason": reason,
            "risk_comment": risk_comment,
            "score_breakdown": {
                "インプ": score.get("インプ", ""),
                "ブランド": score.get("ブランド", ""),
                "パクリ感": score.get("パクリ感", ""),
                "共感": score.get("共感", ""),
                "フック": score.get("フック", ""),
                "account_type": score.get("account_type", ""),
            },
        }

    # Recommended candidate
    rec_id = step10.get("recommended", {}).get("candidate_id") or step09.get("recommended", {}).get("candidate_id")
    if rec_id:
        rec_id = rec_id.zfill(2)
        merged["recommended"]["candidate_id"] = rec_id

        rec10 = step10.get("recommended", {})
        rec09 = step09.get("recommended", {})

        merged["recommended"]["text"] = rec10.get("text") or rec09.get("text") or ""
        merged["recommended"]["reason"] = rec10.get("reason") or rec09.get("reason") or ""
        merged["recommended"]["expected_reaction"] = rec10.get("expected_reaction") or ""

    return merged


def load_run_context(run_folder: Path) -> dict:
    """Load basic context from run.json."""
    run_json_path = run_folder / "run.json"
    context = {
        "run_id": run_folder.name,
        "product_service": "",
        "source_account_type": "",
        "account_type": "",
        "desired_cta_style": "",
        "created_at": "",
    }
    if run_json_path.exists():
        try:
            data = json.loads(run_json_path.read_text(encoding="utf-8"))
            context["product_service"] = data.get("product_service", "")
            context["source_account_type"] = data.get("source_account_type", "")
            context["account_type"] = data.get("account_type", "")
            context["desired_cta_style"] = data.get("desired_cta_style", "")
            context["created_at"] = data.get("created_at", "")
        except Exception:
            pass
    return context


def generate_final_candidates_md(run_id: str, context: dict, candidates: dict) -> str:
    """Generate final-candidates.md from template."""
    template_path = TEMPLATES_DIR / "final-candidates.md"
    if not template_path.exists():
        print(f"Error: Template not found: {template_path}", file=sys.stderr)
        sys.exit(1)

    text = template_path.read_text(encoding="utf-8")

    # Basic placeholders
    text = text.replace("RUN_ID", run_id)
    text = text.replace("PRODUCT_NAME", context.get("product_service", ""))
    text = text.replace("SOURCE_ACCOUNT_TYPE", context.get("source_account_type", ""))
    text = text.replace("ACCOUNT_TYPE", context.get("account_type", ""))
    text = text.replace("DESIRED_CTA_STYLE", context.get("desired_cta_style", ""))
    text = text.replace("YYYY-MM-DDTHH:MM:SS+09:00", context.get("created_at", ""))

    # Candidate texts and comments
    for i in range(1, 6):
        candidate_id = str(i).zfill(2)
        cand = candidates["candidates"].get(candidate_id, {})
        text = text.replace(f"[CANDIDATE_0{i}_TEXT]", cand.get("text", ""))
        text = text.replace(f"[CANDIDATE_0{i}_SCORE]", str(cand.get("market_score", "")))
        text = text.replace(f"[CANDIDATE_0{i}_COMMENT]", cand.get("judge_comment", ""))

        score_breakdown = cand.get("score_breakdown", {})
        text = text.replace(f"[SCORE_0{i}_インプ]", str(score_breakdown.get("インプ", "")))
        text = text.replace(f"[SCORE_0{i}_ブランド]", str(score_breakdown.get("ブランド", "")))
        text = text.replace(f"[SCORE_0{i}_パクリ感]", str(score_breakdown.get("パクリ感", "")))
        text = text.replace(f"[SCORE_0{i}_共感]", str(score_breakdown.get("共感", "")))
        text = text.replace(f"[SCORE_0{i}_フック]", str(score_breakdown.get("フック", "")))
        text = text.replace(f"[SCORE_0{i}_account_type]", str(score_breakdown.get("account_type", "")))
        text = text.replace(f"[SCORE_0{i}_合計]", str(cand.get("market_score", "")))
        text = text.replace(f"[COMMENT_0{i}]", cand.get("judge_comment", ""))

    # Recommended candidate
    rec = candidates["recommended"]
    rec_id = rec.get("candidate_id", "")
    text = text.replace("[RECOMMENDED_CANDIDATE_NUMBER]", rec_id)
    text = text.replace("[RECOMMENDED_CANDIDATE_TEXT]", rec.get("text", ""))

    reason_lines = rec.get("reason", "").splitlines()
    for i in range(3):
        placeholder = f"[SELECTION_REASON_0{i + 1}]"
        value = reason_lines[i].strip("- ") if i < len(reason_lines) else ""
        text = text.replace(placeholder, value)

    text = text.replace("[EXPECTED_REACTION]", rec.get("expected_reaction", ""))

    return text


def update_approval_md(path: Path, candidates: dict) -> str:
    """Update approval.md placeholders with candidate data."""
    text = read_text(path)

    # Final candidate texts
    for i in range(1, 6):
        candidate_id = str(i).zfill(2)
        cand = candidates["candidates"].get(candidate_id, {})
        text = text.replace(f"[CANDIDATE_0{i}_TEXT]", cand.get("text", ""))

    # Recommended candidate
    rec = candidates["recommended"]
    rec_id = rec.get("candidate_id", "")

    # Update recommended candidate heading
    text = re.sub(
        r"(## Recommended Candidate\s*\n)###\s*Candidate\s*\d+",
        rf"\1### Candidate {rec_id}",
        text,
    )
    text = text.replace("[RECOMMENDED_CANDIDATE_TEXT]", rec.get("text", ""))

    reason_lines = rec.get("reason", "").splitlines()
    for i in range(3):
        placeholder = f"[SELECTION_REASON_0{i + 1}]"
        value = reason_lines[i].strip("- ") if i < len(reason_lines) else ""
        text = text.replace(placeholder, value)

    # Market Judge Summary table
    # Replace each row's SCORE, COMMENT, and selected column
    for i in range(1, 6):
        candidate_id = str(i).zfill(2)
        cand = candidates["candidates"].get(candidate_id, {})
        score = str(cand.get("market_score", ""))
        comment = cand.get("judge_comment", "")
        selected = "yes" if candidate_id == rec_id else "no"

        # Match row like: | 01 | `SCORE` | `COMMENT` | `yes / no` |
        pattern = re.compile(
            rf"^(\|\s*{candidate_id}\s*\|)\s*`SCORE`\s*\|\s*`COMMENT`\s*\|\s*`yes / no`\s*(\|)",
            re.MULTILINE,
        )
        text = pattern.sub(
            rf"\1 `{score}` | `{comment}` | `{selected}` \2",
            text,
        )

    # Update [MARKET_JUDGE_SUMMARY_NOTES] with a brief summary
    summary_notes = "Auto-generated from step-09-market-judge.md."
    if rec_id:
        summary_notes += f" Recommended candidate: {rec_id}."
    text = text.replace("[MARKET_JUDGE_SUMMARY_NOTES]", summary_notes)

    return text


def update_run_json(run_json_path: Path, candidates: dict) -> None:
    """Update run.json status and selected_candidate_id."""
    if not run_json_path.exists():
        return

    try:
        data = json.loads(run_json_path.read_text(encoding="utf-8"))
    except Exception:
        return

    rec_id = candidates.get("recommended", {}).get("candidate_id")
    if rec_id:
        data["selected_candidate_id"] = f"candidate-{rec_id}"

    data["status"] = "pending_approval"
    data["current_step"] = "step-10-final-packager"
    data["updated_at"] = datetime.now(timezone.utc).astimezone().isoformat()

    try:
        run_json_path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    except Exception as e:
        print(f"Warning: failed to update run.json: {e}", file=sys.stderr)


def main() -> int:
    setup_stdout()
    args = parse_args()

    run_folder = validate_run_folder(args.run_id)
    step_09_path = run_folder / args.step_09
    step_10_path = run_folder / args.step_10

    step_09_text = read_text(step_09_path)
    step_10_text = read_text(step_10_path)

    step_09_data = parse_step_09(step_09_text)
    step_10_data = parse_step_10(step_10_text)
    candidates = merge_candidates(step_09_data, step_10_data)

    context = load_run_context(run_folder)

    final_candidates_md = generate_final_candidates_md(args.run_id, context, candidates)
    updated_approval_md = update_approval_md(run_folder / "approval.md", candidates)

    final_candidates_path = run_folder / "final-candidates.md"
    approval_md_path = run_folder / "approval.md"

    if args.dry_run:
        print("Dry run - would create/update:")
        print(f"  {final_candidates_path}")
        print(f"  {approval_md_path}")
        print(f"  selected_candidate_id: candidate-{candidates['recommended']['candidate_id']}")
        print(f"  status: pending_approval")
        print("\nNo files were written.")
        return 0

    try:
        final_candidates_path.write_text(final_candidates_md, encoding="utf-8")
        approval_md_path.write_text(updated_approval_md, encoding="utf-8")
    except Exception as e:
        print(f"Error writing files: {e}", file=sys.stderr)
        return 1

    update_run_json(run_folder / "run.json", candidates)

    print("Approval package generated:")
    print(f"  {final_candidates_path}")
    print(f"  {approval_md_path}")
    print(f"  selected_candidate_id: candidate-{candidates['recommended']['candidate_id']}")
    print(f"  status: pending_approval")
    print("\nNext manual step:")
    print("  Review Risk Review, Similarity Review, Account Type Fit, and CTA Fit sections.")
    print("  Check the Human Approval Decision box when ready.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
