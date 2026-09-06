# runs/ Directory

## Purpose

`runs/` is the working directory for **individual post-generation experiments** in Luvira SNS Factory.

Each run represents **one attempt to generate SNS post candidates** for a specific product, source account type, and target account type.

A run is **not** a deployment. It is a sandbox for:

- Capturing the 10-step manual prompt chain inputs and outputs
- Recording risk/similarity/market judgments
- Packaging final candidates for human approval
- Tracking posting decisions and 24h metrics

---

## Principles

1. **One run = one experiment**
   - Do not mix multiple products or account-type pairs in a single run.

2. **Human approval required**
   - No post may be published without human review of `approval.md`.

3. **No automatic posting**
   - This directory does not contain any auto-posting logic. Actual posting is performed manually by a human.

4. **No storage of real third-party post text**
   - Do not paste the full text of real viral posts into this directory.
   - Only structural summaries, emotional drivers, and reaction-design notes are stored.

5. **Metrics are recorded after posting**
   - `metrics.md` is updated by a human after the post has been live for 24 hours.
   - Missing metrics do not invalidate the post, but they prevent win/loss evaluation.

---

## Run Folder Naming Convention

```text
runs/YYYYMMDD-HHMM-{product-slug}-{source-account-type}-to-{account-type}/
```

### Components

| Component | Description | Example |
|-----------|-------------|---------|
| `YYYYMMDD` | Run creation date | `20260906` |
| `HHMM` | Run creation time (24h, local time) | `0900` |
| `{product-slug}` | Short product identifier | `security-diagnosis`, `system-dev` |
| `{source-account-type}` | Source account type | `personal`, `corporate` |
| `{account-type}` | Target account type | `personal`, `corporate` |

### Examples

- `runs/20260906-0900-security-diagnosis-personal-to-corporate/`
- `runs/20260906-0930-system-dev-corporate-to-personal/`
- `runs/20260906-1000-security-diagnosis-corporate-to-corporate/`

---

## Files in Each Run Folder

| File | Purpose |
|------|---------|
| `input.md` | Standardized input context for the run, derived from the test case. |
| `step-01-pattern-miner.md` | Output of Pattern Miner. |
| `step-02-emotion-mapper.md` | Output of Emotion Mapper. |
| `step-03-skeleton-builder.md` | Output of Skeleton Builder. |
| `step-04-adaptation-writer.md` | Output of Adaptation Writer. |
| `step-05-variation-generator.md` | Output of Variation Generator (10 candidates). |
| `step-06-hook-specialist.md` | Output of Hook Specialist. |
| `step-07-similarity-guard.md` | Similarity judgment output. |
| `step-08-risk-filter.md` | Risk judgment output. |
| `step-09-market-judge.md` | Market scoring and top-5 selection. |
| `step-10-final-packager.md` | Human-ready proposal output. |
| `final-candidates.md` | Condensed final 5 candidates + 1 recommendation. |
| `approval.md` | Human approval package with decision checkboxes. |
| `metrics.md` | 24h post-performance record. |
| `run.json` | Machine-readable metadata for the run. |

---

## Run Status Values

A run may pass through the following statuses (recorded in `run.json`):

| Status | Meaning |
|--------|---------|
| `draft` | Run folder created but input not finalized. |
| `ready_for_step_01` | `input.md` is ready. |
| `in_progress` | One or more steps are being executed. |
| `pending_review` | All 10 steps complete, awaiting human review. |
| `pending_approval` | `approval.md` generated, awaiting human decision. |
| `approved` | Human approved the final candidate. |
| `rejected` | Human rejected or requested regeneration. |
| `posted` | Human manually posted the approved candidate. |
| `metrics_due` | 24h measurement window has started. |
| `metrics_recorded` | 24h metrics recorded in `metrics.md`. |
| `archived` | Run closed, no further action expected. |

---

## Safety and Governance

- **Automatic posting is prohibited.**
- **Human approval is mandatory** before any candidate becomes publishable.
- **Do not save the full text of real third-party posts.** Only store structure, emotion, and reaction-design summaries.
- **Always confirm `account_type` and `source_account_type`** in `input.md` and `run.json`.
- **Do not publish without a completed `approval.md`.**
- **24h impressions are the primary evaluation metric**, but missing metrics do not invalidate the post itself.

---

## How to Create a New Run

1. Copy `templates/` files into a new run folder.
2. Name the folder according to the convention above.
3. Fill in `input.md` and `run.json` from the test case.
4. Execute the 10 steps manually, saving outputs to `step-NN-*.md`.
   Use `scripts/step_input_composer.py` to prepare each step's input:

   ```bash
   python scripts/step_input_composer.py --run-id RUN_ID --next-step 01
   ```
5. Generate or update `final-candidates.md`, `approval.md`, and `metrics.md`.
   Use `scripts/approval_package_generator.py` to auto-fill from step-09/10 outputs:

   ```bash
   python scripts/approval_package_generator.py --run-id RUN_ID
   ```
6. Update `run.json` status after each significant state change.
7. Regenerate `runs/index.md` to keep the run list visible:

   ```bash
   python scripts/run_index_generator.py
   ```

8. Obtain human approval before posting.
9. After posting, record `posted_at` and 24h metrics.

---

## Note

This directory intentionally contains **no executable scripts**. Phase 2-C and later may introduce lightweight helpers, but the core workflow remains human-in-the-loop.
