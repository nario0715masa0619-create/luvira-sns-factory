# 24h Metrics Record

## Run Information

- run_id: `RUN_ID`
- platform: `X`
- post_url: `https://...`
- account_type: `personal_or_corporate`
- product_service: `PRODUCT_NAME`
- selected_candidate_id: `CANDIDATE_ID`

## Timing

- posted_at: `YYYY-MM-DDTHH:MM:SS+09:00`
- metrics_due_at: `YYYY-MM-DDTHH:MM:SS+09:00`
- metrics_recorded_at: `YYYY-MM-DDTHH:MM:SS+09:00`

## 24h Metrics

| Metric | Value |
|--------|-------|
| impressions_24h | `NUMBER` |
| likes_24h | `NUMBER` |
| comments_24h | `NUMBER` |
| reposts_24h | `NUMBER` |
| saves_24h | `NUMBER` |
| profile_clicks_24h | `NUMBER` |
| link_clicks_24h | `NUMBER` |
| engagement_rate_24h | `PERCENTAGE` |

### Engagement Rate Calculation

```text
engagement_rate_24h = (likes_24h + comments_24h + reposts_24h + saves_24h) / impressions_24h * 100
```

- Record as a percentage, e.g. `3.5%`.
- If `impressions_24h` is 0 or not recorded, leave this field blank or use `result_verdict: invalid_missing_metrics`.

## Qualitative Notes

[QUALITATIVE_NOTES]

## Result Verdict

Please check one:

- [ ] **strong** — significantly exceeded expectations.
- [ ] **acceptable** — met baseline expectations.
- [ ] **weak** — underperformed relative to expectations.
- [ ] **invalid_missing_metrics** — metrics could not be recorded.
- [ ] **invalid_changed_post** — the posted text differed from the approved candidate.

## Lessons Learned

[LESSONS_LEARNED]

## Next Prompt Adjustment

[NEXT_PROMPT_ADJUSTMENT]
