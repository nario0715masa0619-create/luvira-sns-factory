# 24h Metrics Record

## Run Information

- run_id: `20260920-1140-mens-fashion-gadget-corporate-to-personal`
- platform: `X`
- post_url: `https://x.com/ritsu_opt/status/2101693388466876709?s=20`
- account_type: `personal`
- product_service: `40代男性向けファッション・ガジェット情報発信`
- selected_candidate_id: `human-edited-final`

## Timing

- posted_at: `2026-09-21T00:22:00+09:00`
- metrics_due_at: `2026-09-22T00:22:00+09:00`
- metrics_recorded_at: `2026-09-22T01:04:00+09:00`
- measurement_window: `near_24h_observation`
- measurement_target: `strict_24h_preferred`
- measurement_status: `24h_missed_near_24h_observation_recorded`
- elapsed_since_post: `約24時間42分`

> **Important**: 本来の metrics_due_at は `2026-09-22T00:22:00+09:00` でしたが、計測が約42分遅延しました。したがって本記録は **strict 24h metrics ではなく near-24h observation** です。

## 24h Metrics

| Metric | Value |
|--------|-------|
| impressions_24h | `missed` |
| likes_24h | `missed` |
| replies_24h | `missed` |
| comments_24h | `missed` |
| reposts_24h | `missed` |
| saves_24h | `missed` |
| profile_clicks_24h | `missed` |
| link_clicks_24h | `missed` |
| engagement_rate_24h | `missed` |
| impression_ratio_vs_ops002 | `not_comparable` |
| raw_difference_vs_ops002 | `not_comparable` |
| impression_ratio_vs_ops007 | `not_comparable` |
| raw_difference_vs_ops007 | `not_comparable` |

### Engagement Rate Calculation

```text
engagement_rate_24h = (likes_24h + comments_24h + reposts_24h + saves_24h) / impressions_24h * 100
```

- 24h metrics が取得できなかったため、今回は算出不可。
- 推定・補間・改変は行わない。

## Near-24h Observation

> 以下の数値は **strict 24h 時点の値ではありません**。投稿後約24時間42分で確認できた値です。

| Metric | Observed Value |
|--------|----------------|
| observed_impressions_near_24h | `22` |
| observed_likes_near_24h | `0` |
| observed_replies_near_24h | `0` |
| observed_reposts_near_24h | `0` |
| observation_time | `2026-09-22T01:04:00+09:00（約24h42m後）` |

## Reference Comparison（Non-Comparable）

| Run | measurement_window | impressions | Comparable? |
|-----|--------------------|-------------|-------------|
| OPS-002 | late_measurement | 149 | no |
| OPS-004 | late_24h_measurement | 9 | no |
| OPS-005 | delayed_observation | 29 | no |
| OPS-006 | delayed_observation | 26 | no |
| OPS-007 | delayed_observation | 39 | no |
| OPS-008 | near_24h_observation | 22 | no |

- measurement window が一致しないため、OPS-002 / OPS-007 との formal ratio comparison は行わない。

## Qualitative Notes

- 約24h42m時点で 22 impressions、likes=0、replies=0、reposts=0。
- 実用情報型（information_structure）に変更したが、強い Distribution / Engagement は観測されなかった。
- ただし strict 24h measurement ではなく、1 run のみの観測であるため、情報密度・実用性仮説を confirmed / rejected にはしない。
- H007「若作りしないジャケット」、information_structure 共感型→実用型の効果は **inconclusive**。

## Result Verdict

Please check one:

- [ ] **strong** — significantly exceeded expectations.
- [ ] **acceptable** — met baseline expectations.
- [ ] **weak** — underperformed relative to expectations.
- [ ] **invalid_missing_metrics** — metrics could not be recorded.
- [x] **non_comparable** — near-24h observation only; strict 24h metrics missed.
- [ ] **invalid_changed_post** — the posted text differed from the approved candidate.

> Cold Start label: `inconclusive`（information_structure仮説は1 run・測定不完全のため断定不可）。

## Lessons Learned

- 24h 計測を厳守できなかった（今回は約42分遅延）。SNS Factory の measurement operations 改善が必要。
- 実用情報型にしても、即座に Distribution が上がるわけではない。
- 同じ H007 テーマで information_structure を変えた比較は、strict 24h measurement があっても数 run の再検証が必要。

## Next Prompt Adjustment

- 24h 計測を実験成立条件とする運用を徹底する。
- OPS-009 では、異なる content_angle または画像の有無など、より大きな変化を検討する。
- H007 / information_structure の再検証は将来の run に回し、次は新しい content_angle または distribution baseline 測定を優先する。

---

## Generated Metadata

- run_id: `20260920-1140-mens-fashion-gadget-corporate-to-personal`
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
- created_at: `2026-09-20T11:40:41.226950+09:00`
