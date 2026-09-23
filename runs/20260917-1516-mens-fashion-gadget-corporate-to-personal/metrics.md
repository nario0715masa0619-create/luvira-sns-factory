# 24h Metrics Record

## Run Information

- run_id: `20260917-1516-mens-fashion-gadget-corporate-to-personal`
- platform: `X`
- post_url: `https://...`
- account_type: `personal`
- product_service: `40代男性向けファッション・ガジェット情報発信`
- selected_candidate_id: `human-edited-final`

## Timing

- posted_at: `2026-09-17T15:26:00+09:00`
- metrics_due_at: `2026-09-18T15:26:00+09:00`
- metrics_recorded_at: `unknown（delayed observation only）`
- measurement_window: `delayed_observation`
- measurement_target: `strict_24h_preferred`
- measurement_status: `24h_missed_delayed_observation_recorded`

> **Important**: 本来の metrics_due_at は `2026-09-18T15:26:00+09:00` でしたが、24h 計測を失念しました。したがって本記録は **strict 24h metrics ではなく delayed observation** です。

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

### Engagement Rate Calculation

```text
engagement_rate_24h = (likes_24h + comments_24h + reposts_24h + saves_24h) / impressions_24h * 100
```

- 24h metrics が取得できなかったため、今回は算出不可。
- 推定・補間・改変は行わない。

## Delayed Observation

> 以下の数値は **24h 時点の値ではありません**。投稿後 24時間を超過した時点で確認できた値です。

| Metric | Observed Value |
|--------|----------------|
| observed_impressions_delayed | `39` |
| observed_likes_delayed | `1` |
| observed_replies_delayed | `1` |
| observed_reposts_delayed | `0` |
| observation_time | `exact time unknown（delayed observation only）` |

## Reference Comparison（Non-Comparable）

- OPS-002 canonical record: `impressions_24h=149` with `measurement_window=late_measurement`（strict 24h measurement ではない）
- OPS-007 delayed observation impressions: `39`
- **Status**: `non_comparable` — measurement window が異なるため、正式な `impression_ratio_vs_ops002` として扱わない。

## Qualitative Notes

- 24h 計測を失念したため、H007 共感・気づき型の厳密な評価は不可能。
- delayed observation で 39 impressions、likes=1、replies=1、reposts=0 を確認。
- この値は 24h 後の値ではないため、OPS-002（149 late measurement）との直接比較はできない。
- 共感・気づき型が強い Distribution を示したとは言えないが、1投稿（かつ測定不完全）で H007 を判断できない。

## Result Verdict

Please check one:

- [ ] **strong** — significantly exceeded expectations.
- [ ] **acceptable** — met baseline expectations.
- [ ] **weak** — underperformed relative to expectations.
- [ ] **invalid_missing_metrics** — metrics could not be recorded.
- [x] **non_comparable** — delayed observation only; 24h metrics missed.
- [ ] **invalid_changed_post** — the posted text differed from the approved candidate.

## Lessons Learned

- 24h 計測を忘れると、Distribution Learning の比較実験として価値が大きく損なわれる（OPS-005〜OPS-006 に続き4回目の測定問題）。
- delayed observation 値（39）だけでは、H007 共感・気づき型の効果を判断できない。

## Next Prompt Adjustment

- 24h 計測を厳守する運用ルールを強化する。
- OPS-008 では H007 を維持しつつ information_structure を実用情報型に変更。
- OPS-008 以降は 24h 計測を実験成立条件とする。

---

## Generated Metadata

- run_id: `20260917-1516-mens-fashion-gadget-corporate-to-personal`
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
- created_at: `2026-09-17T15:16:07.252835+09:00`
