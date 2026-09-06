# Phase 2-H Step Input Composer

## 1. Executive Summary

Phase 2-H implements a helper that composes the input Markdown for the next step of the 10-step prompt chain.

The composer is implemented as a Python script:

- `scripts/step_input_composer.py`

It reads the run's `run.json`, `input.md`, the previous step output (for steps 02-10), and the target step's prompt file. It then generates a single Markdown file that a human can copy and paste into Kimi/OpenCode.

This script does **not** execute prompts, integrate with APIs, or post automatically.

---

## 2. Scope

### In Scope

- Read `run.json`, `input.md`, prompt file, and previous step output
- Generate `step-NN-{name}-input.md` for steps 01-10
- Provide run metadata, source input, prompt text, and execution instructions in one file
- Support `--dry-run`

### Out of Scope

- Prompt execution
- AI API integration
- SNS API integration
- n8n integration
- Automatic posting
- Modification of `run.json`, `approval.md`, or `metrics.md`
- Modification of `prompts/*`, `experiments/phase-1/*`, or `templates/*`
- Final candidate generation (handled by `approval_package_generator.py`)
- Index generation (handled by `run_index_generator.py`)

---

## 3. CLI Usage

```bash
python scripts/step_input_composer.py \
  --run-id 20260906-1000-system-dev-corporate-to-personal \
  --next-step 03
```

### Required Arguments

| Argument | Description |
|----------|-------------|
| `--run-id` | Existing run ID under `runs/`. |
| `--next-step` | Next step number (`01` to `10`). |

### Optional Arguments

| Argument | Default | Description |
|----------|---------|-------------|
| `--runs-dir` | `runs/` | Directory containing run folders. |
| `--prompts-dir` | `prompts/` | Directory containing prompt files. |
| `--output` | `runs/{run_id}/step-{next-step}-{name}-input.md` | Output file path. |
| `--dry-run` | `False` | Show what would be generated without writing the file. |

---

## 4. Step Mapping

| Step | Name | Prompt File | Previous Output | Generated Input File |
|------|------|-------------|-----------------|----------------------|
| 01 | pattern-miner | `prompts/01-pattern-miner.md` | none | `step-01-pattern-miner-input.md` |
| 02 | emotion-mapper | `prompts/02-emotion-mapper.md` | `step-01-pattern-miner.md` | `step-02-emotion-mapper-input.md` |
| 03 | skeleton-builder | `prompts/03-skeleton-builder.md` | `step-02-emotion-mapper.md` | `step-03-skeleton-builder-input.md` |
| 04 | adaptation-writer | `prompts/04-adaptation-writer.md` | `step-03-skeleton-builder.md` | `step-04-adaptation-writer-input.md` |
| 05 | variation-generator | `prompts/05-variation-generator.md` | `step-04-adaptation-writer.md` | `step-05-variation-generator-input.md` |
| 06 | hook-specialist | `prompts/06-hook-specialist.md` | `step-05-variation-generator.md` | `step-06-hook-specialist-input.md` |
| 07 | similarity-guard | `prompts/07-similarity-guard.md` | `step-06-hook-specialist.md` | `step-07-similarity-guard-input.md` |
| 08 | risk-filter | `prompts/08-risk-filter.md` | `step-07-similarity-guard.md` | `step-08-risk-filter-input.md` |
| 09 | market-judge | `prompts/09-market-judge.md` | `step-08-risk-filter.md` | `step-09-market-judge-input.md` |
| 10 | final-packager | `prompts/10-final-packager.md` | `step-09-market-judge.md` | `step-10-final-packager-input.md` |

---

## 5. Input Files

### For All Steps

- `runs/{run_id}/run.json`
- `runs/{run_id}/input.md`
- `prompts/{NN}-{name}.md`

### For Steps 02-10 Only

- `runs/{run_id}/step-{previous-step}-{previous-name}.md`

---

## 6. Output Files

Default output path:

```text
runs/{run_id}/step-{next-step}-{name}-input.md
```

Example:

```text
runs/20260906-1000-system-dev-corporate-to-personal/step-03-skeleton-builder-input.md
```

If the output file already exists, the script exits with an error to prevent accidental overwrites.

---

## 7. Generated Markdown Structure

Each generated input file has the following structure:

```markdown
# Step {NN}: {Name} Input

## Run Metadata

- run_id: `...`
- product_service: `...`
- product_slug: `...`
- source_account_type: `...`
- account_type: `...`
- desired_cta_style: `...`
- allowed_persona_expression: `...`
- risk_tolerance: `...`
- target_platform: `...`
- target_audience: `...`
- business_goal: `...`
- model: `...`
- execution_mode: `...`
- status: `...`
- current_step: `...`

## Source Input

{previous step output or input.md sections}

## Prompt To Apply

{full prompt text from prompts/NN-name.md}

## Execution Instruction

1. Copy the entire content of this file (`step-NN-name-input.md`).
2. Paste it into Kimi/OpenCode as a new request.
3. Save the AI response to `step-NN-name.md` in the same run folder.
4. Review the output before proceeding to the next step.

> **Important:** This is a manual step. The script does not execute prompts, call APIs, or post automatically.
```

### Source Input Details

- **Step 01**: Extracts `Source Post Structure Summary`, `Source Post Emotion Summary`, and `Step 01 Input for Pattern Miner` sections from `input.md`.
- **Steps 02-10**: Includes the entire content of the previous step's output file.

---

## 8. Safety / Governance

- **No prompt execution.** The generated file must be manually pasted into Kimi/OpenCode.
- **No AI API calls.** The script does not interact with any model or API.
- **No automatic posting.** Posting remains a manual step after human approval.
- **No modification of run.json / approval.md / metrics.md.** The script only reads these files.
- **Overwrite protection.** Existing input files are not overwritten.
- **Human-in-the-loop.** The output is clearly labeled as a manual copy-paste target.

---

## 9. Dry Run Usage

```bash
python scripts/step_input_composer.py \
  --run-id 20260906-1000-system-dev-corporate-to-personal \
  --next-step 03 \
  --dry-run
```

Expected output:

```text
Dry run - would generate:
  run folder: D:\OpenCode\luvira-sns-factory\runs\20260906-1000-system-dev-corporate-to-personal
  run.json: D:\OpenCode\luvira-sns-factory\runs\20260906-1000-system-dev-corporate-to-personal\run.json
  input.md: D:\OpenCode\luvira-sns-factory\runs\20260906-1000-system-dev-corporate-to-personal\input.md
  prompt file: D:\OpenCode\luvira-sns-factory\prompts\03-skeleton-builder.md
  previous step output: D:\OpenCode\luvira-sns-factory\runs\20260906-1000-system-dev-corporate-to-personal\step-02-emotion-mapper.md
  output file: D:\OpenCode\luvira-sns-factory\runs\20260906-1000-system-dev-corporate-to-personal\step-03-skeleton-builder-input.md

No files were written.
```

---

## 10. Error Handling

The script exits with a clear error message in the following cases:

- Run folder does not exist
- `run.json` is missing or invalid
- `input.md` is missing
- Prompt file is missing
- Previous step output is missing (for steps 02-10)
- Output file already exists

Stack traces are not printed; only the cause and suggested action are shown.

---

## 11. Acceptance Test Result

### Test 1: Step 01 Dry Run

Command:

```bash
python scripts/step_input_composer.py \
  --run-id 20260906-1000-system-dev-corporate-to-personal \
  --next-step 01 \
  --dry-run
```

Result: ✅ Passed. Output showed expected input/output paths.

### Test 2: Step 01 Actual Generation

Command:

```bash
python scripts/step_input_composer.py \
  --run-id 20260906-1000-system-dev-corporate-to-personal \
  --next-step 01
```

Result: ✅ Passed. Created `step-01-pattern-miner-input.md` with correct sections.

### Test 3: Step 10 Dry Run

Command:

```bash
python scripts/step_input_composer.py \
  --run-id 20260906-1000-system-dev-corporate-to-personal \
  --next-step 10 \
  --dry-run
```

Result: ✅ Passed. Output correctly referenced `step-09-market-judge.md` as previous output.

### Test 4: Overwrite Protection

Command:

```bash
python scripts/step_input_composer.py \
  --run-id 20260906-1000-system-dev-corporate-to-personal \
  --next-step 01
```

Result: ✅ Failed as expected because `step-01-pattern-miner-input.md` already exists.

### Test 5: Missing Previous Step Output

Command:

```bash
python scripts/step_input_composer.py \
  --run-id 20260906-1000-system-dev-corporate-to-personal \
  --next-step 02
```

Result: ✅ Failed as expected because `step-01-pattern-miner.md` does not exist.

### Test 6: run.json Unchanged

Verified that `runs/20260906-1000-system-dev-corporate-to-personal/run.json` was not modified.

---

## 12. Known Limitations

1. **Prompt execution is manual.**
   - The generated file must be copied and pasted into Kimi/OpenCode by a human.

2. **Previous step output must exist.**
   - For steps 02-10, the previous step's output file must already be saved.

3. **Source input extraction is heuristic.**
   - Step 01 extracts named Markdown sections. If `input.md` structure deviates, extraction may be incomplete.

4. **run.json is not updated.**
   - `current_step` and `status` are not updated by this script.

5. **approval.md / metrics.md are not updated.**
   - Those are handled by `approval_package_generator.py` and manual editing.

6. **Final package generation is separate.**
   - After step 10, use `approval_package_generator.py` to create the approval package.

7. **Index updates are separate.**
   - After significant state changes, run `run_index_generator.py` to update `runs/index.md`.

---

## 13. Recommended Next Phase

**Phase 2-I: Metrics Recording Helper**

After posting and 24h metrics collection, the next helper could assist with recording metrics.

- Reads manually collected 24h metrics
- Updates `metrics.md` and `run.json` with final numbers
- Computes the result verdict
- Does not fetch metrics automatically from SNS APIs

Alternatively, **Phase 2-I: Run Workflow Documentation** could consolidate the operating instructions for all Phase 2 helpers into a single runbook.

Recommended first choice: **Metrics Recording Helper** because it closes the loop from posting to evaluation.

---

## 14. References

- `docs/phase-2-local-assist-design.md`
- `docs/phase-2-b-run-convention.md`
- `docs/phase-2-e-run-folder-generator.md`
- `docs/phase-2-f-approval-package-generator.md`
- `docs/phase-2-g-run-index-generator.md`
- `scripts/step_input_composer.py`
- `prompts/01-pattern-miner.md` through `prompts/10-final-packager.md`
