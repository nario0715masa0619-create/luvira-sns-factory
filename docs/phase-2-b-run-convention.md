# Phase 2-B Run Directory Convention and Operation Rules

## 1. Executive Summary

Phase 2-B establishes the **run directory convention** and **metadata templates** for file-based semi-automation of the Luvira SNS Factory 10-step prompt chain.

This phase does **not** implement scripts, CLIs, APIs, or automatic posting. It only creates:

- `runs/README.md`
- `templates/input.md`
- `templates/run.json`
- `templates/approval.md`
- `templates/metrics.md`
- `docs/phase-2-b-run-convention.md`

These files make it possible to start manual-but-standardized runs, track progress, enforce safety rules, and record 24h impressions for later evaluation.

---

## 2. Scope

### In Scope

- Run directory naming convention
- Required files per run
- Template files for input, metadata, approval, and metrics
- Run status lifecycle
- Human approval rules
- Metrics recording rules
- Safety and governance rules
- Git rules for run management
- Recommended manual workflow

### Out of Scope

- Automatic posting
- SNS API integration
- n8n integration
- CLI or batch scripts
- Real third-party post text storage
- Claude SNS system integration
- LuviraMemory integration
- Prompt text modifications
- Changes to Phase 1 result/test-case files

---

## 3. Directory Convention

```text
D:\OpenCode\luvira-sns-factory/
├── docs/
│   ├── phase-2-local-assist-design.md
│   ├── phase-2-b-run-convention.md   # this document
│   └── ...
├── templates/
│   ├── input.md
│   ├── run.json
│   ├── approval.md
│   └── metrics.md
├── runs/
│   ├── README.md
│   └── 20260906-0900-security-diagnosis-personal-to-corporate/
│       ├── input.md
│       ├── step-01-pattern-miner.md
│       ├── ...
│       ├── step-10-final-packager.md
│       ├── final-candidates.md
│       ├── approval.md
│       ├── metrics.md
│       └── run.json
└── experiments/
    └── phase-1/
        └── ...
```

---

## 4. Run Folder Naming

Each run folder must follow this convention:

```text
runs/YYYYMMDD-HHMM-{product-slug}-{source-account-type}-to-{account-type}/
```

### Components

| Component | Description |
|-----------|-------------|
| `YYYYMMDD` | Run creation date |
| `HHMM` | Run creation time (24-hour, local time) |
| `{product-slug}` | Short product identifier |
| `{source-account-type}` | `personal` or `corporate` |
| `{account-type}` | `personal` or `corporate` |

### Examples

- `runs/20260906-0900-security-diagnosis-personal-to-corporate/`
- `runs/20260906-0930-system-dev-corporate-to-personal/`
- `runs/20260906-1000-system-dev-personal-to-personal/`

---

## 5. Required Files per Run

Every run folder must contain the following files before it can be considered complete:

| File | Required Before Posting | Purpose |
|------|--------------------------|---------|
| `input.md` | Yes | Standardized run input |
| `step-01-pattern-miner.md` | Yes | Pattern analysis |
| `step-02-emotion-mapper.md` | Yes | Emotion mapping |
| `step-03-skeleton-builder.md` | Yes | Post skeleton |
| `step-04-adaptation-writer.md` | Yes | Style/CTA adaptation rules |
| `step-05-variation-generator.md` | Yes | 10 candidate posts |
| `step-06-hook-specialist.md` | Yes | Hook refinement |
| `step-07-similarity-guard.md` | Yes | Similarity judgment |
| `step-08-risk-filter.md` | Yes | Risk judgment |
| `step-09-market-judge.md` | Yes | Top-5 selection |
| `step-10-final-packager.md` | Yes | Proposal package |
| `final-candidates.md` | Yes | Condensed candidates |
| `approval.md` | Yes | Human approval record |
| `run.json` | Yes | Machine-readable metadata |
| `metrics.md` | No (after posting) | 24h performance record |

---

## 6. Template Usage

To create a new run:

1. Create a run folder following the naming convention.
2. Copy all files from `templates/` into the run folder.
3. Fill in `input.md` and `run.json` based on the test case.
4. Execute each step manually, saving outputs to `step-NN-*.md`.
5. Update `run.json` after each completed step.
6. After step 10, create or update `final-candidates.md`, `approval.md`, and `metrics.md`.
7. Do not post without a signed-off `approval.md`.

---

## 7. Run Metadata Rules

- `run_id` must match the run folder name.
- `source_account_type` and `account_type` must match the folder name and `input.md`.
- `status` must be updated after every major state change.
- `current_step` must reflect the latest completed or in-progress step.
- `selected_candidate_id` may only be set after Market Judge output exists.
- `human_approved` may only become `true` after a human signs `approval.md`.
- `posted_at` may only be set after actual manual posting.
- `metrics_due_at` must be `posted_at + 24 hours`.

---

## 8. Human Approval Rules

- No candidate may be posted without a completed `approval.md`.
- The approver must check one of:
  - Approved as-is
  - Approved with edits
  - Rejected
  - Regenerate required
- If "Approved with edits", the edited text must be recorded in `approval.md`.
- If "Regenerate required", the reason must be recorded, and the run returns to `in_progress`.
- The `Pre-Post Checklist` in `approval.md` must be fully checked before posting.

---

## 9. Metrics Recording Rules

- `metrics.md` is filled in after the post has been live for 24 hours.
- Metrics should be recorded as close to the 24-hour mark as possible.
- If metrics cannot be recorded, use `result_verdict: invalid_missing_metrics`.
- If the posted text differed from the approved candidate, use `result_verdict: invalid_changed_post`.
- Missing metrics do not invalidate the post, but they prevent reliable win/loss evaluation.

---

## 10. Status Lifecycle

A run progresses through the following statuses:

```text
draft
  ↓
ready_for_step_01
  ↓
in_progress
  ↓
pending_review
  ↓
pending_approval
  ↓
approved / rejected
  ↓ (if approved)
posted
  ↓
metrics_due
  ↓
metrics_recorded
  ↓
archived
```

### Status Definitions

| Status | Meaning |
|--------|---------|
| `draft` | Run folder created, input not finalized. |
| `ready_for_step_01` | `input.md` ready. |
| `in_progress` | Steps are being executed. |
| `pending_review` | All 10 steps complete; awaiting human review. |
| `pending_approval` | `approval.md` generated; awaiting decision. |
| `approved` | Human approved the candidate. |
| `rejected` | Human rejected or requested regeneration. |
| `posted` | Human manually posted the approved candidate. |
| `metrics_due` | 24h measurement window active. |
| `metrics_recorded` | 24h metrics recorded. |
| `archived` | Run closed. |

---

## 11. Safety and Governance Rules

1. **Automatic posting is prohibited.**
2. **Human approval is mandatory** before posting.
3. **Do not save the full text of real third-party posts.** Only store structure, emotion, and reaction-design summaries.
4. **Use only structure, emotion, and reaction design** from source posts.
5. **Do not fabricate personal or corporate experience.**
6. **Do not use unsubstantiated performance claims.**
7. **Do not use effect guarantees or exaggeration.**
8. **`account_type` must be confirmed at every step.**
9. **`source_account_type` must be confirmed at every step, especially for cross-type runs.**
10. **Do not post without a completed `approval.md`.**
11. **24h impressions are an important final evaluation metric**, but missing metrics do not invalidate the post.
12. **AI scores alone do not determine the winner.** Human judgment remains final.

---

## 12. Error Handling

### Step failure
- Review the step input/output.
- Re-execute the failed step.
- Update the output file and `run.json`.

### Output format corruption
- Fix the output file manually.
- Restart from the corrupted step.

### account_type mismatch
- Re-execute from `Adaptation Writer` or earlier.
- Verify `input.md` and `run.json` match the intended direction.

### CTA mismatch
- Re-execute `Variation Generator` or `Adaptation Writer` with stronger CTA instructions.

### Similarity Guard medium/high
- Revise or exclude affected candidates.
- Re-run `Hook Specialist` or `Variation Generator` as needed.

### Risk Filter medium/high
- Remove or revise affected candidates.
- Document the reason in `run.json`.

### Market Judge scores too low
- Return to step 5 and adjust directionality.
- Or revisit the test-case conditions.

### Human approval rejected
- Record the reason in `approval.md`.
- Return to the appropriate step for revision or regeneration.

### Missing posted_at
- Record immediately after manual posting.
- Missing `posted_at` makes 24h metrics tracking unreliable.

### Missing 24h metrics
- Record as soon as possible.
- Use `invalid_missing_metrics` if unavailable.

---

## 13. Git Rules

1. **Confirm working tree is clean before starting a new phase.**
2. **One phase = one commit** is the basic rule.
3. **Check `git status` before committing.**
4. **Do not proceed to the next phase if `git push` fails.** Resolve authentication or network issues first.
5. **`git reset`, `git rebase`, `git amend`, and force push are prohibited unless explicitly approved.**
6. **Do not leave untracked files uncommitted when moving to the next phase.**
7. `runs/` folders for actual experiments may be added to `.gitignore` if they contain sensitive client data. If they contain only fictional samples, they may be committed.

---

## 14. Recommended Manual Workflow

1. Verify working tree is clean.
2. Create a new run folder from `templates/`.
3. Fill in `input.md` and `run.json`.
4. Execute Pattern Miner (step 01) and save output.
5. Execute Emotion Mapper (step 02) and save output.
6. Execute Skeleton Builder (step 03) and save output.
7. Execute Adaptation Writer (step 04) and save output.
8. Execute Variation Generator (step 05) and save output.
9. Execute Hook Specialist (step 06) and save output.
10. Execute Similarity Guard (step 07) and save output.
11. Execute Risk Filter (step 08) and save output.
12. Execute Market Judge (step 09) and save output.
13. Execute Final Packager (step 10) and save output.
14. Create/update `final-candidates.md`, `approval.md`, and `metrics.md`.
15. Obtain human approval via `approval.md`.
16. Manually post the approved candidate.
17. Record `posted_at` in `run.json` and `metrics.md`.
18. After 24 hours, record metrics in `metrics.md` and update `run.json`.
19. Archive the run.

---

## 15. Phase 2-C Candidate Work

Phase 2-C may introduce lightweight helpers that do **not** perform automatic posting or API calls.

Possible candidates:

1. **run folder generator**
   - Create a run folder and copy templates from `templates/`.

2. **test-case to input converter**
   - Read a Phase 1 test-case file and generate `input.md` + `run.json`.

3. **step input composer**
   - Read the previous step output and format the next step input for copy-paste.

4. **approval.md generator**
   - Fill `approval.md` placeholders from `step-09-market-judge.md` and `step-10-final-packager.md`.

5. **run index updater**
   - Scan `runs/` and update `runs/index.md` with status summary.

### Phase 2-C Non-Goals

- No CLI that executes prompts automatically.
- No API integration.
- No n8n workflow.
- No automatic posting.
- No modification to prompts or Phase 1 assets.

---

## 16. References

- `docs/phase-2-local-assist-design.md`
- `experiments/phase-1/PHASE-1-CLOSURE-REVIEW.md`
- `runs/README.md`
- `templates/input.md`
- `templates/run.json`
- `templates/approval.md`
- `templates/metrics.md`
