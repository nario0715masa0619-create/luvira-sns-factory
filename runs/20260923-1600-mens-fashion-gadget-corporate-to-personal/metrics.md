# 24h Metrics Record

## Run Information

- run_id: `20260923-1600-mens-fashion-gadget-corporate-to-personal`
- platform: `X`
- post_url: `https://...`
- account_type: `personal`
- product_service: `40代男性向けファッション・ガジェット情報発信`
- selected_candidate_id: ``

## Timing

- planned_posting_time: `22:40–22:45 JST (same band as OPS-005 2026-09-11T22:41:00+09:00)`
- posted_at: `YYYY-MM-DDTHH:MM:SS+09:00`
- metrics_due_at: `YYYY-MM-DDTHH:MM:SS+09:00` (posted_at + 24h)
- metrics_recorded_at: `YYYY-MM-DDTHH:MM:SS+09:00`
- measurement_target: `strict_24h_preferred`
- measurement_status: `unmeasured`
- measurement_contract: `docs/measurement-contract-proposal.md (pilot; ±15min tolerance)`

## 24h Metrics

> **Measurement Recovery Run**: Primary objective is to obtain strict 24h metrics for H003 replication. Performance level is secondary.

| Metric | Value |
|--------|-------|
| impressions_24h | `` |
| likes_24h | `` |
| comments_24h | `` |
| reposts_24h | `` |
| saves_24h | `` |
| profile_clicks_24h | `` |
| link_clicks_24h | `` |
| engagement_rate_24h | `` |

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
- [x] **invalid_missing_metrics** — metrics could not be recorded.
- [ ] **invalid_changed_post** — the posted text differed from the approved candidate.

## Lessons Learned

[LESSONS_LEARNED]

## Next Prompt Adjustment

[NEXT_PROMPT_ADJUSTMENT]

---

## Generated Metadata

- run_id: `20260923-1600-mens-fashion-gadget-corporate-to-personal`
- product_service: `40代男性向けファッション・ガジェット情報発信`
- product_slug: `mens-fashion-gadget`
- source_account_type: `corporate`
- account_type: `personal`
- desired_cta_style: `reply / discussion / experience_sharing`
- allowed_persona_expression: `僕 / 私 / 自分 / 主語省略`
- risk_tolerance: `balanced`
- target_platform: `X`
- target_audience: `40代男性 / 経営者 / 営業職 / 見た目と仕事道具を整えたい人`
- business_goal: `40代男性向けファッション×ガジェット投稿の反応獲得`
- model: `kimi-k2.7-code`
- execution_mode: `file_based_semi_automation`
- created_at: `2026-09-23T19:37:20.459088+09:00`
