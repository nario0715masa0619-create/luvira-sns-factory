# Human Approval Package

## Run Information

- run_id: `RUN_ID`
- product_service: `PRODUCT_NAME`
- source_account_type: `SOURCE_ACCOUNT_TYPE`
- account_type: `ACCOUNT_TYPE`
- desired_cta_style: `DESIRED_CTA_STYLE`
- risk_tolerance: `RISK_TOLERANCE`
- created_at: `YYYY-MM-DDTHH:MM:SS+09:00`

---

## Final Candidates

### Candidate 01

```text
[CANDIDATE_01_TEXT]
```

### Candidate 02

```text
[CANDIDATE_02_TEXT]
```

### Candidate 03

```text
[CANDIDATE_03_TEXT]
```

### Candidate 04

```text
[CANDIDATE_04_TEXT]
```

### Candidate 05

```text
[CANDIDATE_05_TEXT]
```

---

## Market Judge Summary

| candidate_id | market_score | judge_comment | selected |
|--------------|--------------|---------------|----------|
| 01 | `SCORE` | `COMMENT` | `yes / no` |
| 02 | `SCORE` | `COMMENT` | `yes / no` |
| 03 | `SCORE` | `COMMENT` | `yes / no` |
| 04 | `SCORE` | `COMMENT` | `yes / no` |
| 05 | `SCORE` | `COMMENT` | `yes / no` |

### Notes

[MARKET_JUDGE_SUMMARY_NOTES]

---

## Recommended Candidate

### Candidate 01

```text
[RECOMMENDED_CANDIDATE_TEXT]
```

### Selection Reason

- [SELECTION_REASON_01]
- [SELECTION_REASON_02]
- [SELECTION_REASON_03]

---

## Similarity Review

- Overall similarity risk: `low / medium / high`
- Source hook retention: `low / medium / high`
- Phrase copy risk: `low / medium / high`
- Structural copy risk: `low / medium / high`

### Notes

[SIMILARITY_REVIEW_NOTES]

---

## Risk Review

> **Note:** Before step 08 Risk Filter output exists, `pending` may be recorded.  
> After step 08, update each row to `low`, `medium`, `high`, or `rejected`.  
> Human approval is **not allowed** while any risk row remains `pending`.

| Risk Category | Level | Notes |
|---------------|-------|-------|
| Fabricated experience | pending / low / medium / high / rejected | |
| Unsubstantiated claims | pending / low / medium / high / rejected | |
| Effect guarantee | pending / low / medium / high / rejected | |
| Fear-mongering | pending / low / medium / high / rejected | |
| Account type mismatch | pending / low / medium / high / rejected | |
| CTA mismatch | pending / low / medium / high / rejected | |
| Product pushiness | pending / low / medium / high / rejected | |
| Controversy risk | pending / low / medium / high / rejected | |

---

## Account Type Fit

- account_type: `ACCOUNT_TYPE`
- source_account_type: `SOURCE_ACCOUNT_TYPE`
- Tone fit: `good / needs edit / poor`
- Persona fit: `good / needs edit / poor`
- CTA fit: `good / needs edit / poor`

### Notes

[ACCOUNT_TYPE_FIT_NOTES]

---

## CTA Fit

- desired_cta_style: `DESIRED_CTA_STYLE`
- Actual CTA: `[ACTUAL_CTA_TEXT]`
- Fit: `good / needs edit / poor`

### Notes

[CTA_FIT_NOTES]

---

## Human Approval Decision

Please check one:

- [ ] **Approved as-is**
- [ ] **Approved with edits**
- [ ] **Rejected**
- [ ] **Regenerate required**

### Decision Notes

[APPROVER_DECISION_NOTES]

---

## Required Edits

If "Approved with edits" or "Regenerate required" is selected, describe the required changes here:

[EDIT_INSTRUCTIONS]

---

## Pre-Post Checklist

Before posting, confirm all of the following:

- [ ] `account_type` is correct.
- [ ] `source_account_type` is correct.
- [ ] CTA matches `desired_cta_style`.
- [ ] No fabricated personal or corporate experience.
- [ ] No rumor or consultation-track-record implication.
- [ ] No unsubstantiated performance claims.
- [ ] No effect guarantee or exaggeration.
- [ ] No full-text copy of the original post.
- [ ] Controversy risk is within acceptable range.
- [ ] Final poster has performed a last visual check.

---

## Posting Record

- posted_at: `YYYY-MM-DDTHH:MM:SS+09:00`
- post_url: `https://...`
- posted_by: `NAME`
- platform: `X`

---

## 24h Metrics Record

- metrics_due_at: `YYYY-MM-DDTHH:MM:SS+09:00`
- impressions_24h: `NUMBER`
- engagement_24h: `NUMBER`
- replies_24h: `NUMBER`
- clicks_24h: `NUMBER`
- notes: `METRICS_NOTES`

---

## Final Notes

[ANY_ADDITIONAL_NOTES]
