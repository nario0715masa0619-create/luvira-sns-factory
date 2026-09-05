# Phase 2-C Template Dry Run Review

## 1. Executive Summary

This document records the results of a manual dry-run of the Phase 2-B templates using a fictional sample run.

The dry run confirmed that the templates (`input.md`, `run.json`, `approval.md`, `metrics.md`) and the run folder convention are usable for manual operation. No actual step outputs were generated; only the template filling and operational flow were tested.

Overall, the templates are usable as-is for lightweight helper implementation, with minor refinements recommended.

---

## 2. Created Run Folder

```text
runs/20260906-0900-system-dev-corporate-to-personal/
```

### Naming Check

| Component | Value | OK |
|-----------|-------|----|
| Date | 20260906 | ✅ |
| Time | 0900 | ✅ |
| Product slug | system-dev | ✅ |
| Source account type | corporate | ✅ |
| Target account type | personal | ✅ |

The folder name matches the `runs/YYYYMMDD-HHMM-{product-slug}-{source-account-type}-to-{account-type}/` convention defined in `runs/README.md`.

---

## 3. Files Created

| File | Status | Notes |
|------|--------|-------|
| `input.md` | Created | Filled with sample values from templates/input.md. |
| `run.json` | Created | Filled with sample metadata from templates/run.json. |
| `approval.md` | Created | Left in pre-execution state with [TBD] placeholders. |
| `metrics.md` | Created | Left in pre-posting state with null values and invalid_missing_metrics. |
| `DRY-RUN-REVIEW.md` | Created | This review document. |

The following files were intentionally **not** created:

- `step-01-pattern-miner.md` through `step-10-final-packager.md`
- `final-candidates.md`

---

## 4. Template Fill Test

### 4.1 input.md

Filling `input.md` from `templates/input.md` was straightforward. The template clearly separates:

- Run identification
- Client context
- Account configuration (with required fields highlighted)
- Source post policy
- Source post structure summary
- Source post emotion summary
- Target configuration
- Constraints and non-goals
- Step 01 input

No fields were missing for the dry-run scenario. The explicit reminder not to paste real third-party post text is effective.

### 4.2 run.json

Filling `run.json` from `templates/run.json` was straightforward. The schema covers:

- Run identification and timestamps
- Client context
- Account types and styles
- Source post policy
- Target configuration
- Prompt/model metadata
- Status and current step
- Steps array (01-10) with status/path/notes
- Final verdict and approval state
- Posting and metrics fields

The `steps` array is verbose but useful for tracking progress. The `status` enum is clear.

### 4.3 approval.md

Filling `approval.md` from `templates/approval.md` was straightforward in the pre-execution state. The template includes:

- Run information
- Final candidates section
- Recommended candidate section
- Similarity review
- Risk review table
- Account type fit
- CTA fit
- Human approval decision checkboxes
- Required edits section
- Pre-post checklist
- Posting record
- 24h metrics record

### 4.4 metrics.md

Filling `metrics.md` from `templates/metrics.md` was straightforward. The template includes all necessary fields for 24h measurement.

---

## 5. Missing Fields

During the dry run, the following potentially useful fields were noted as missing or could be improved:

1. **input.md: `product_slug` field**
   - Currently inferred from `product_service`, but a short slug would help consistency with folder naming.
   - **Recommendation:** Add optional `product_slug` field.

2. **run.json: `run_folder_path` field**
   - Not strictly necessary since `run_id` matches folder name, but explicit path could help tooling.
   - **Recommendation:** Optional, low priority.

3. **approval.md: `final_candidate_scores` field**
   - Market Judge scores are not preserved in approval.md; they are only in `step-09-market-judge.md`.
   - **Recommendation:** Add a small table of candidate scores for context.

4. **metrics.md: `posted_text` field**
   - The actual posted text is not recorded in metrics.md; it is in approval.md and run.json.
   - **Recommendation:** Keep as-is; duplication risk is higher than benefit.

None of these are blockers.

---

## 6. Redundant Fields

The following fields felt redundant or overlapping:

1. **input.md and run.json both contain `target_audience` and `business_goal`**
   - This is intentional redundancy for human readability vs machine parsing.
   - **Verdict:** Acceptable. Keep both.

2. **approval.md and run.json both track `posted_at`, `post_url`, etc.**
   - Again intentional: approval.md for human record, run.json for machine index.
   - **Verdict:** Acceptable. Keep both but ensure consistency.

3. **input.md `client_context.target_audience` overlaps with top-level `target_audience`**
   - The top-level field is more specific to this run; client_context is reusable context.
   - **Verdict:** Acceptable. Keep both.

No major redundancy issues.

---

## 7. Ambiguous Fields

The following fields could be ambiguous for first-time users:

1. **run.json `execution_mode`**
   - Values like `manual_template_dry_run` are clear in this context, but future modes may need documentation.
   - **Recommendation:** Document allowed values in `docs/phase-2-b-run-convention.md`.

2. **approval.md Risk Review `Level` column**
   - `low / medium / high` is clear, but users may wonder when to use `pending`.
   - **Recommendation:** Add a note that `pending` is acceptable before step 08 output exists.

3. **metrics.md `engagement_rate_24h`**
   - Format (percentage vs decimal) is not specified.
   - **Recommendation:** Add example value or unit note.

These are minor documentation issues.

---

## 8. Manual Operation Friction

The following friction points were observed during the dry run:

1. **Copying templates manually**
   - Copying 4 files from `templates/` to a new run folder is repetitive.
   - **Mitigation:** Phase 2-D run folder generator will automate this.

2. **run.json steps array is long**
   - 10 step objects make the JSON file 138 lines.
   - **Mitigation:** Acceptable for manual editing; generator can pre-fill.

3. **approval.md placeholders require cleanup**
   - `[TBD]` placeholders are numerous before step execution.
   - **Mitigation:** Phase 2-D approval generator can fill these from step outputs.

4. **No explicit link between input.md and step-01 input**
   - The `step_01_input` section in `input.md` duplicates some fields from earlier sections.
   - **Mitigation:** Acceptable for clarity; generator can deduplicate.

No critical friction. All are automatable in Phase 2-D/E.

---

## 9. Safety / Governance Check

| Rule | Status | Notes |
|------|--------|-------|
| No real third-party post text saved | ✅ | Only structure/emotion summaries stored. |
| account_type required | ✅ | Explicitly marked in input.md and run.json. |
| source_account_type required | ✅ | Explicitly marked in input.md and run.json. |
| Human approval required | ✅ | approval.md has decision checkboxes. |
| No automatic posting | ✅ | No posting logic in any file. |
| CTA style recorded | ✅ | desired_cta_style in input.md and run.json. |
| Risk tolerance recorded | ✅ | risk_tolerance in input.md and run.json. |
| Source post storage policy recorded | ✅ | do_not_save_third_party_text. |
| Metrics recording planned | ✅ | metrics.md exists. |

All safety and governance rules are maintained.

---

## 10. Metrics Readiness

The metrics recording flow is ready:

1. `approval.md` has a Posting Record section for `posted_at` and `post_url`.
2. `approval.md` has a 24h Metrics Record section.
3. `metrics.md` is dedicated to metrics with a result verdict.
4. `run.json` has `posted_at`, `metrics_due_at`, `impressions_24h`, and `engagement_24h`.

Potential improvement:
- Add a calculated `metrics_due_at` example in templates based on `posted_at + 24h`.

---

## 11. Recommendation Before Generator Implementation

Before implementing Phase 2-D lightweight helpers, the following minor refinements are recommended:

1. **Add `product_slug` field to `templates/input.md` and `templates/run.json`**
   - Improves consistency with run folder naming.

2. **Document `execution_mode` allowed values**
   - In `docs/phase-2-b-run-convention.md`.

3. **Add `pending` guidance to approval.md Risk Review**
   - Clarify that `pending` is acceptable before step outputs exist.

4. **Add engagement_rate unit note to metrics.md**
   - Example: "Enter as percentage, e.g., 3.5%".

5. **Add `final_candidate_scores` table to approval.md**
   - Help approvers understand Market Judge context.

These changes are optional and do not block generator implementation.

---

## 12. Phase 2-C Verdict

**PASS with concerns — minor template refinements recommended**

The templates and run folder convention are usable for manual operation and ready for lightweight helper implementation. The concerns are minor documentation/usability issues that can be addressed in Phase 2-D or as part of generator implementation.

No template redesign is required.

---

## 13. Recommended Phase 2-D

**B. run folder generator implementation**

### Reason

- The dry run confirmed that the templates work, but manual copying is the biggest friction.
- A run folder generator is the safest next step because it:
  - Automates file copying from `templates/`
  - Pre-fills `run.json` and `input.md` with run_id, timestamps, account types, etc.
  - Does not execute prompts or perform any AI operations
  - Maintains human-in-the-loop workflow
  - Reduces copy-paste errors

### Phase 2-D Scope

1. Create a lightweight run folder generator (e.g., PowerShell one-liner or simple Python script).
2. Accept parameters:
   - product_service
   - product_slug
   - source_account_type
   - account_type
   - desired_cta_style
   - risk_tolerance
3. Generate:
   - `runs/YYYYMMDD-HHMM-{slug}-{source}-to-{target}/`
   - Copy `templates/*` into the run folder
   - Pre-fill `run.json` with run_id, created_at, account types, status
   - Pre-fill `input.md` with run_id, account types, product_service
4. Keep `approval.md` and `metrics.md` in their initial pre-execution state.

### Phase 2-D Out of Scope

- Prompt execution
- Step input/output generation
- API integration
- Automatic posting
- n8n
- Changes to templates/docs

---

## 14. Appendices

### A. Reference Files

- `runs/README.md`
- `templates/input.md`
- `templates/run.json`
- `templates/approval.md`
- `templates/metrics.md`
- `docs/phase-2-b-run-convention.md`
- `docs/phase-2-local-assist-design.md`

### B. Dry Run Sample Values

- run_id: `20260906-0900-system-dev-corporate-to-personal`
- product_service: `AI活用型短納期システム開発`
- source_account_type: `corporate`
- account_type: `personal`
- desired_cta_style: `reply / discussion / experience_sharing`
- risk_tolerance: `balanced`
- model: `kimi-k2.7-code`
- execution_mode: `manual_template_dry_run`
- status: `draft`

### C. Review Date

- 2026-09-06
