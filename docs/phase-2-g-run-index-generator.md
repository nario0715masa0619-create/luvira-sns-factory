# Phase 2-G Run Index Generator

## 1. Executive Summary

Phase 2-G implements a lightweight helper that scans `runs/` and generates `runs/index.md` from each run's `run.json`.

The generator is implemented as a Python script:

- `scripts/run_index_generator.py`

It creates/updates:

- `runs/index.md`

This script does **not** execute prompts, integrate with APIs, post automatically, or modify any `run.json` / `approval.md` / `metrics.md` files. It only reads `run.json` and writes a single Markdown summary.

---

## 2. Scope

### In Scope

- Scan subdirectories under `runs/`
- Read `run.json` from each run folder
- Extract metadata fields for visualization
- Generate `runs/index.md` with summary, runs table, pending approval, metrics due, and warnings
- Support sorting and archived-run filtering
- Support `--dry-run`

### Out of Scope

- Prompt execution
- AI API integration
- SNS API integration
- n8n integration
- Automatic posting
- Modification of `run.json`, `approval.md`, or `metrics.md`
- Modification of `prompts/`, `experiments/phase-1/`, or Phase 1 assets
- Modification of `templates/input.md`, `templates/run.json`, `templates/approval.md`, `templates/metrics.md`, or `templates/final-candidates.md`

---

## 3. CLI Usage

```bash
python scripts/run_index_generator.py
```

### Optional Arguments

| Argument | Default | Description |
|----------|---------|-------------|
| `--runs-dir` | `runs/` | Directory containing run folders. |
| `--output` | `runs/index.md` | Output Markdown path. |
| `--include-archived` | `False` | Include archived runs in the index. |
| `--sort` | `updated_at_desc` | Sort order for the Runs table. |
| `--dry-run` | `False` | Show what would be generated without writing the file. |

### Allowed `--sort` Values

- `updated_at_desc` — most recently updated first
- `created_at_desc` — most recently created first
- `run_id_desc` — run_id descending (string comparison)
- `status` — status alphabetically, then updated_at descending

---

## 4. Generated Output

`runs/index.md` contains the following sections.

### Summary

```markdown
## Summary

- generated_at: `2026-09-06T15:46:49+09:00`
- total_runs: `2`
- visible_runs: `2`
- archived_runs: `0`
- warning_count: `1`
- pending_approval_count: `1`
- posted_count: `0`
- metrics_due_count: `0`
- metrics_recorded_count: `0`
```

### Runs Table

```markdown
## Runs

| run_id | product_service | source | target | status | selected_candidate_id | human_approved | approval_status | posted_at | metrics_due_at | impressions_24h | updated_at |
|--------|-----------------|--------|--------|--------|-----------------------|----------------|-----------------|-----------|----------------|-----------------|------------|
| [20260906-1000-system-dev-corporate-to-personal](./20260906-1000-system-dev-corporate-to-personal/) | AI活用型短納期システム開発 | corporate | personal | pending_approval | candidate-03 | false | pending | - | - | - | 2026-09-06T13:42:55+09:00 |
```

`run_id` is rendered as a relative link to the run folder.

### Pending Approval

Lists runs where `status` is `pending_approval`.

```markdown
## Pending Approval

| run_id | product_service | selected_candidate_id | approval_status | updated_at |
|--------|-----------------|-----------------------|-----------------|------------|
```

### Metrics Due

Lists runs where `status` is `posted` or `metrics_due` and `metrics_due_at` is set.

```markdown
## Metrics Due

| run_id | posted_at | metrics_due_at | impressions_24h | result_hint |
|--------|-----------|----------------|-----------------|-------------|
```

`result_hint` values:

- `metrics recorded` — `impressions_24h` is present
- `overdue` — current time is past `metrics_due_at` and metrics are not recorded
- `metrics not yet recorded` — metrics due but not yet recorded

### Warnings

Records issues found during scanning.

```markdown
## Warnings

- missing required fields in `20260906-0900-system-dev-corporate-to-personal/run.json`: product_slug
```

If no warnings:

```markdown
## Warnings

No warnings.
```

---

## 5. Validation Rules

### Required Fields

Each `run.json` must contain at minimum:

- `run_id`
- `product_service`
- `product_slug`
- `source_account_type`
- `account_type`
- `status`

Missing required fields are recorded as warnings but do not stop index generation.

### Run ID Mismatch

If a folder name differs from `run_id` inside `run.json`, a warning is recorded.

### Duplicate Run ID

If the same `run_id` appears in multiple folders, a warning is recorded.

### Missing run.json

Folders without `run.json` are recorded as warnings and skipped.

### Invalid JSON

Folders with invalid `run.json` are recorded as warnings and skipped.

### Archived Runs

Runs are treated as archived when:

- `status` is `archived`, or
- `execution_mode` is `archived_experiment`

Archived runs are excluded by default. Use `--include-archived` to include them.

---

## 6. Safety / Governance

- **Read-only to run data.** The script only reads `run.json`; it never writes to it.
- **No automatic posting.** Posting Record and metrics remain untouched.
- **No AI execution.** The script does not call any model or API.
- **Human approval remains mandatory.** The index visualizes status but does not approve anything.
- **Safe to re-run.** Re-running regenerates `runs/index.md` from the latest `run.json` files.

---

## 7. Dry Run Usage

```bash
python scripts/run_index_generator.py --dry-run
```

Expected output:

```text
Dry run - would generate:
  output: D:\OpenCode\luvira-sns-factory\runs\index.md
  total_runs: 2
  visible_runs: 2
  warning_count: 1
  pending_approval_count: 1
  metrics_due_count: 0

Warnings:
  - missing required fields in `20260906-0900-system-dev-corporate-to-personal/run.json`: product_slug

No files were written.
```

---

## 8. Example Commands

### Default execution

```bash
python scripts/run_index_generator.py
```

### Include archived runs

```bash
python scripts/run_index_generator.py --include-archived
```

### Sort by creation date

```bash
python scripts/run_index_generator.py --sort created_at_desc
```

### Custom output path

```bash
python scripts/run_index_generator.py --output reports/run-index.md
```

---

## 9. Acceptance Test Result

### Test 1: Dry Run

Command:

```bash
python scripts/run_index_generator.py --dry-run
```

Result: ✅ Passed. Output showed expected counts and the single expected warning.

### Test 2: Normal Execution

Command:

```bash
python scripts/run_index_generator.py
```

Result: ✅ Passed. `runs/index.md` was created with all required sections.

### Test 3: Sort Options

Commands:

```bash
python scripts/run_index_generator.py --sort updated_at_desc --dry-run
python scripts/run_index_generator.py --sort created_at_desc --dry-run
python scripts/run_index_generator.py --sort run_id_desc --dry-run
python scripts/run_index_generator.py --sort status --dry-run
```

Result: ✅ All passed without errors.

### Test 4: Include Archived

Command:

```bash
python scripts/run_index_generator.py --include-archived --dry-run
```

Result: ✅ Passed without errors.

### Test 5: run.json Unchanged

Command:

```bash
python scripts/run_index_generator.py
```

Result: ✅ `runs/20260906-0900-system-dev-corporate-to-personal/run.json` and `runs/20260906-1000-system-dev-corporate-to-personal/run.json` were not modified.

### Known Warning

- `20260906-0900-system-dev-corporate-to-personal/run.json` is missing `product_slug` because it was created as a Phase 2-C dry-run sample before the field was finalized. This is a valid historical artifact and is not modified.

---

## 10. Known Limitations

1. **run.json is read-only.**
   - The generator never modifies `run.json`.

2. **approval.md / metrics.md are not parsed.**
   - The index uses only `run.json` fields.

3. **No prompt execution.**
   - The generator does not execute any step prompts.

4. **No automatic posting.**
   - Posting and metrics recording remain manual.

5. **24h metrics are not fetched automatically.**
   - `impressions_24h` is read from `run.json` only if a human has already recorded it.

6. **Index is a local Markdown table.**
   - It is not a database or web dashboard.

7. **Historical runs may produce warnings.**
   - Older sample runs may lack fields added after their creation. These are recorded as warnings, not errors.

---

## 11. Recommended Next Phase

**Phase 2-H: Step Input Composer**

After the run index is in place, the next safe helper is a step input composer that reads the previous step's output and formats the next step's input Markdown for copy-paste.

- Reads `step-NN-*.md` and `input.md`
- Generates `step-(NN+1)-*-input.md`
- Does not execute prompts
- Keeps the workflow human-in-the-loop

Alternatively, **Phase 2-H: Metrics Recording Helper** could assist with updating `metrics.md` and `run.json` after 24h metrics are collected manually.

Recommended first choice: **Step Input Composer** because it reduces friction during the 10-step chain, which is the most frequent manual task.

---

## 12. References

- `docs/phase-2-local-assist-design.md`
- `docs/phase-2-b-run-convention.md`
- `docs/phase-2-e-run-folder-generator.md`
- `docs/phase-2-f-approval-package-generator.md`
- `scripts/run_index_generator.py`
- `runs/index.md`
- `runs/README.md`
