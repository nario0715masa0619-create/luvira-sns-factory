# 24h Metrics Record

## Run Information

- run_id: `20260910-1149-mens-fashion-gadget-corporate-to-personal`
- platform: `X`
- post_url: `https://x.com/ritsu_opt/status/2098406679058797046?s=20`
- account_type: `personal`
- product_service: `40代男性向けファッション・ガジェット情報発信`
- selected_candidate_id: `candidate-01`

## Timing

- posted_at: `2026-09-11T22:41:00+09:00`
- metrics_due_at: `2026-09-12T22:41:00+09:00`
- metrics_recorded_at: `2026-09-14T15:00:00+09:00`（遅延計測）
- measurement_window: `delayed_observation`
- measurement_target: `strict_24h_preferred`
- measurement_status: `24h_missed_delayed_observation_recorded`
- elapsed_since_post: `24時間以上（正確な経過時間は未記録）`

> **Important**: 本来の 24h metrics_due_at は `2026-09-12T22:41:00+09:00` でしたが、計測を失念しました。したがって本記録は **strict 24h metrics ではなく delayed observation** です。

## 24h Metrics

| Metric | Value |
|--------|-------|
| impressions_24h | `missed` |
| likes_24h | `missed` |
| replies_24h | `missed` |
| comments_24h | `missed` |
| follows_24h | `missed` |
| reposts_24h | `missed` |
| bookmarks_24h | `missed` |
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
| observed_impressions_delayed | `29` |
| observed_likes_delayed | `1` |
| observed_replies_delayed | `1` |
| observed_reposts_delayed | `0` |
| observation_time | `24h 以降（具体的時刻未記録）` |

## Reference Comparison（Non-Comparable）

- OPS-002 canonical record: `impressions_24h=149` with `measurement_window=late_measurement`（strict 24h measurement ではない）
- OPS-005 delayed observation impressions: `29`
- **Status**: `non_comparable` — measurement window が異なるため、正式な `impression_ratio_vs_ops002` として扱わない。

> Note: 137 は過去に一時的に使用された pre-correction baseline。canonical run record の OPS-002 は 149（late measurement）で記録されている。OPS-005 の 29 は delayed observation のみなので、OPS-002 との参考 ratio は Canonical record には含めない。

## Qualitative Notes

- 24h 計測を失念したため、厳密な Distribution Learning 比較は不可能。
- 遅延観測時点で 29 impressions、likes 1、replies 1、reposts 0 を確認。
- この値は 24h 後の値ではないため、OPS-002（canonical record: 149 late measurement）との直接比較はできない。
- 投稿文は human edited 済み。実体験断定を減らし、余韻型で終了。
- 画像添付の有無、投稿時間帯、アカウント状態なども影響しうるが、今回は測定ミスにより判断材料として不十分。

## Result Verdict

Please check one:

- [ ] **strong** — significantly exceeded expectations.
- [ ] **acceptable** — met baseline expectations.
- [ ] **weak** — underperformed relative to expectations.
- [ ] **invalid_missing_metrics** — metrics could not be recorded.
- [x] **non_comparable** — delayed observation only; 24h metrics missed.
- [ ] **invalid_changed_post** — the posted text differed from the approved candidate.

> Cold Start label としては `non_comparable`。H003「爪・髪・香り」を 1 投稿（かつ測定不完全）で retired / losing pattern 確定にしない。

## Lessons Learned

- 24h 計測を忘れると、Distribution Learning の比較実験として価値が大きく損なわれる。
- 遅延観測値（29）だけでは、テーマの強弱や構造の効果を判断できない。
- 次回以降は、投稿時に metrics_due アラームまたはカレンダー登録を徹底する。

## Next Prompt Adjustment

- 24h 計測を厳守する運用ルールを強化する（アラーム・カレンダー登録）。

---

## Generated Metadata

- run_id: `20260910-1149-mens-fashion-gadget-corporate-to-personal`
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
- created_at: `2026-09-10T11:49:01.612313+09:00`
