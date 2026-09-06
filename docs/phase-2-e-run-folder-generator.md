# Phase 2-E Run Folder Generator

## 1. Executive Summary

Phase 2-E implements a lightweight local helper that generates a new run folder from the Phase 2-B templates.

The generator is implemented as a Python script:

- `scripts/new_run_folder.py`

It does **not** execute prompts, integrate with APIs, or perform automatic posting. It only copies templates, pre-fills metadata, and creates a standardized run folder under `runs/`.

The goal is to reduce manual copy-paste friction while keeping the workflow human-in-the-loop.

---

## 2. Scope

### In Scope

- Generate a new run folder under `runs/`
- Copy templates from `templates/`
- Pre-fill `input.md`, `run.json`, `approval.md`, and `metrics.md`
- Validate required arguments and naming rules
- Support `--dry-run`
- Clean up partial folders on failure

### Out of Scope

- Prompt execution
- AI API integration
- SNS API integration
- n8n integration
- Automatic posting
- CLI that executes the 10-step chain automatically
- Modification of `prompts/`, `experiments/phase-1/`, or `templates/` content

---

## 3. CLI Usage

```bash
python scripts/new_run_folder.py \
  --product-service "AI活用型短納期システム開発" \
  --product-slug system-dev \
  --source-account-type corporate \
  --account-type personal \
  --target-audience "中小企業経営者 / 事業責任者" \
  --business-goal "AI活用型短納期システム開発への関心獲得"
```

---

## 4. Required Arguments

| Argument | Description |
|----------|-------------|
| `--product-service` | Product or service name (can include Japanese). |
| `--product-slug` | Short folder-safe slug. Lowercase English letters, numbers, hyphens only. |
| `--source-account-type` | `personal` or `corporate`. |
| `--account-type` | `personal` or `corporate`. |

---

## 5. Optional Arguments

| Argument | Default | Description |
|----------|---------|-------------|
| `--desired-cta-style` | Depends on `account_type` | See Defaults below. |
| `--allowed-persona-expression` | Depends on `account_type` | See Defaults below. |
| `--risk-tolerance` | Depends on `account_type` | See Defaults below. |
| `--target-platform` | `X` | Target SNS platform. |
| `--target-audience` | `None` | Target audience for this run. |
| `--business-goal` | `None` | Business goal for this run. |
| `--model` | `kimi-k2.7-code` | Model name. |
| `--execution-mode` | `file_based_semi_automation` | See Allowed Values below. |
| `--created-at` | Current time | Override creation timestamp (ISO 8601). |
| `--run-id` | Auto-generated | Override run_id. |
| `--source-post-reference-type` | `structure_only` | Source post reference policy. |
| `--source-post-storage-policy` | `do_not_save_third_party_text` | Storage policy. |
| `--dry-run` | `False` | Show what would be created without creating files. |

---

## 6. Defaults

### `--desired-cta-style`

- If `account_type=personal`: `reply / discussion / experience_sharing`
- If `account_type=corporate`: `checklist / consultation / document_request`

### `--allowed-persona-expression`

- If `account_type=personal`: `僕 / 私 / 自分 / 主語省略`
- If `account_type=corporate`: `当社 / 弊社 / 主語省略`

### `--risk-tolerance`

- If `account_type=personal`: `balanced`
- If `account_type=corporate`: `conservative`

### Other Defaults

- `--target-platform`: `X`
- `--model`: `kimi-k2.7-code`
- `--execution-mode`: `file_based_semi_automation`
- `--source-post-reference-type`: `structure_only`
- `--source-post-storage-policy`: `do_not_save_third_party_text`

---

## 7. Validation Rules

### `product_slug`

- Must use only lowercase English letters, numbers, and hyphens.
- Spaces, underscores, Japanese characters, and symbols are prohibited.
- Example valid values: `security-diagnosis`, `system-dev`, `line-ai-advisor`
- Example invalid values: `system dev`, `system_dev`, `システム開発`

### `source_account_type`

- Must be `personal` or `corporate`.

### `account_type`

- Must be `personal` or `corporate`.

### `execution_mode`

- Must be one of:
  - `manual`
  - `manual_template_dry_run`
  - `file_based_semi_automation`
  - `assisted_generation`
  - `archived_experiment`

### Run Folder

- `runs/{run_id}/` must not already exist.
- Existing run folders are never overwritten.

### Templates

- The following files must exist in `templates/`:
  - `input.md`
  - `run.json`
  - `approval.md`
  - `metrics.md`

If any are missing, the script exits with an error before creating the run folder.

---

## 8. Generated Files

For a run with id `20260906-1000-system-dev-corporate-to-personal`, the generator creates:

```text
runs/20260906-1000-system-dev-corporate-to-personal/
├── input.md
├── run.json
├── approval.md
└── metrics.md
```

### Pre-filled Fields

#### `input.md`

- run_id
- created_at
- product_service
- product_slug
- source_account_type
- account_type
- desired_cta_style
- allowed_persona_expression
- risk_tolerance
- source_post_reference_type
- source_post_storage_policy
- target_platform
- target_audience
- business_goal
- model / execution_mode (in Generated Metadata section)

Fields that require human input remain as placeholders:

- industry
- posting_purpose (partial)
- tone
- source_post_structure_summary
- source_post_emotion_summary

#### `run.json`

- run_id
- created_at / updated_at
- product_service / product_slug
- source_account_type / account_type
- desired_cta_style / allowed_persona_expression / risk_tolerance
- source_post_reference_type / source_post_storage_policy
- target_platform / target_audience / business_goal
- prompt_version: `phase-1-final`
- model / execution_mode
- status: `draft`
- current_step: `null`
- final_verdict / selected_candidate_id / human_approved / approval_status reset
- posted_at / post_url / metrics_due_at reset
- impressions_24h / engagement_24h reset
- steps array normalized with pending status and local paths

#### `approval.md`

- Run information pre-filled
- Final Candidates remain as `[TBD]` placeholders
- Recommended Candidate remains as `[TBD]` placeholder
- Risk Review set to `pending`
- Market Judge Summary table present but empty
- Human Approval Decision unchecked
- Pre-Post Checklist unchecked
- Posting Record and 24h Metrics Record remain as placeholders

#### `metrics.md`

- Run information pre-filled
- posted_at / metrics_due_at / metrics_recorded_at reset to placeholder
- All metrics values blank
- result_verdict pre-selected as `invalid_missing_metrics`

---

## 9. Run Folder Naming

If `--run-id` is not specified, the generator creates:

```text
YYYYMMDD-HHMM-{product-slug}-{source-account-type}-to-{account-type}
```

Example:

```text
20260906-1000-system-dev-corporate-to-personal
```

The folder name follows the convention documented in `docs/phase-2-b-run-convention.md`.

---

## 10. Safety / Governance

- **No automatic posting.** The script only creates files.
- **No AI execution.** It does not call any model or API.
- **No real third-party post text storage.** The templates remind users to store only structure/emotion summaries.
- **Human approval remains mandatory.** `approval.md` is generated in an unapproved state.
- **Existing runs are protected.** The script fails if the target folder already exists.
- **Partial runs are cleaned up.** If file generation fails, the newly created run folder is removed.

---

## 11. Dry Run Usage

Use `--dry-run` to preview what would be created:

```bash
python scripts/new_run_folder.py \
  --product-service "AI活用型短納期システム開発" \
  --product-slug system-dev \
  --source-account-type corporate \
  --account-type personal \
  --target-audience "中小企業経営者 / 事業責任者" \
  --business-goal "AI活用型短納期システム開発への関心獲得" \
  --dry-run
```

Expected output:

```text
Dry run - would create:
  run_id: 20260906-1322-system-dev-corporate-to-personal
  run_folder: D:\OpenCode\luvira-sns-factory\runs\20260906-1322-system-dev-corporate-to-personal
  files:
    - input.md
    - run.json
    - approval.md
    - metrics.md
  created_at: 2026-09-06T13:22:15.505552+09:00

No files were created.
```

---

## 12. Example Commands

### Generate with defaults

```bash
python scripts/new_run_folder.py \
  --product-service "AI活用型短納期システム開発" \
  --product-slug system-dev \
  --source-account-type corporate \
  --account-type personal
```

### Generate with full context

```bash
python scripts/new_run_folder.py \
  --product-service "AI活用型短納期システム開発" \
  --product-slug system-dev \
  --source-account-type corporate \
  --account-type personal \
  --target-audience "中小企業経営者 / 事業責任者" \
  --business-goal "AI活用型短納期システム開発への関心獲得" \
  --model kimi-k2.7-code \
  --execution-mode file_based_semi_automation
```

### Generate with explicit run_id

```bash
python scripts/new_run_folder.py \
  --product-service "AIエージェントセキュリティ診断" \
  --product-slug security-diagnosis \
  --source-account-type personal \
  --account-type corporate \
  --run-id 20260906-1100-security-diagnosis-personal-to-corporate
```

---

## 13. Acceptance Test Result

The following acceptance tests were performed during Phase 2-E.

### Test 1: Dry Run

Command:

```bash
python scripts/new_run_folder.py \
  --product-service "AI活用型短納期システム開発" \
  --product-slug system-dev \
  --source-account-type corporate \
  --account-type personal \
  --target-audience "中小企業経営者 / 事業責任者" \
  --business-goal "AI活用型短納期システム開発への関心獲得" \
  --dry-run
```

Result: ✅ Passed. Output showed expected run_id, folder, and files. No files created.

### Test 2: Actual Folder Generation

Command:

```bash
python scripts/new_run_folder.py \
  --product-service "AI活用型短納期システム開発" \
  --product-slug system-dev \
  --source-account-type corporate \
  --account-type personal \
  --target-audience "中小企業経営者 / 事業責任者" \
  --business-goal "AI活用型短納期システム開発への関心獲得" \
  --run-id 20260906-1000-system-dev-corporate-to-personal
```

Result: ✅ Passed. Created `runs/20260906-1000-system-dev-corporate-to-personal/` with all four files.

### Test 3: Validation - Invalid product_slug

Command:

```bash
python scripts/new_run_folder.py --product-service test --product-slug "test slug" --source-account-type personal --account-type personal
```

Result: ✅ Failed as expected with clear error message about invalid slug.

### Test 4: Validation - Existing Run Folder

Command (run twice with same run_id):

```bash
python scripts/new_run_folder.py --product-service test --product-slug test --source-account-type personal --account-type personal --run-id 20260906-1000-system-dev-corporate-to-personal
```

Result: ✅ Failed as expected because the folder already exists. No overwrite occurred.

### Generated Test Run

The following test run folder is kept as an acceptance artifact:

- `runs/20260906-1000-system-dev-corporate-to-personal/`

---

## 14. Known Limitations

1. **Prompt execution is not automated.**
   - The script only creates files. Humans still execute each step via Kimi/OpenCode.

2. **Step output files are not generated.**
   - `step-01-pattern-miner.md` through `step-10-final-packager.md` must be created manually.

3. **`approval.md` and `metrics.md` are skeletons only.**
   - They contain placeholders and must be completed after step execution and posting.

4. **Source post structure/emotion summaries require human input.**
   - The generator cannot know the source post content.

5. **Actual posting is performed by a human.**
   - No SNS integration exists.

6. **Terminal encoding on Windows.**
   - The script attempts to reconfigure stdout to UTF-8. On some terminals, Japanese output may still appear garbled, but files are always written in UTF-8 and are correct.

---

## 15. Recommended Next Phase

**Phase 2-F: Approval Package Generator**

After the run folder generator is in place, the next safe helper is the approval package generator.

- Reads `step-09-market-judge.md` and `step-10-final-packager.md`.
- Fills `final-candidates.md` and `approval.md` placeholders.
- Does not perform approval or posting.

See `docs/phase-2-f-approval-package-generator.md` for details.

---

## 16. References

- `docs/phase-2-local-assist-design.md`
- `docs/phase-2-b-run-convention.md`
- `runs/README.md`
- `templates/input.md`
- `templates/run.json`
- `templates/approval.md`
- `templates/metrics.md`
- `scripts/new_run_folder.py`
