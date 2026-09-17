# 24h Metrics Record

## Run Information

- run_id: `20260914-1426-mens-fashion-gadget-corporate-to-personal`
- platform: `X`
- post_url: `https://x.com/ritsu_opt/status/2099485363559624746?s=20`
- account_type: `personal`
- product_service: `40代男性向けファッション・ガジェット情報発信`
- selected_candidate_id: `candidate-b`

## Timing

- posted_at: `2026-09-14T22:08:00+09:00`
- metrics_due_at: `2026-09-15T22:08:00+09:00`
- metrics_recorded_at: `2026-09-17T15:00:00+09:00`（遅延計測）
- measurement_window: `delayed_observation`
- measurement_target: `strict_24h_preferred`
- measurement_status: `24h_missed_delayed_observation_recorded`
- elapsed_since_post: `約65時間`

> **Important**: 本来の metrics_due_at は `2026-09-15T22:08:00+09:00` でしたが、計測を失念しました。したがって本記録は **strict 24h metrics ではなく delayed observation** です。
>
> Note: posted_at は分単位まで確認（22:08）。秒は確認できていないため `00` としています。これは秒値の推定ではなく、ISO 8601 表記上のプレースホルダーです。

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
| observed_impressions_delayed | `26` |
| observed_likes_delayed | `1` |
| observed_replies_delayed | `1` |
| observed_reposts_delayed | `0` |
| observation_time | `2026-09-17T15:00:00+09:00（約65時間後）` |

## Reference Comparison（Non-Comparable）

- OPS-002 canonical record: `impressions_24h=149` with `measurement_window=late_measurement`（strict 24h measurement ではない）
- OPS-006 delayed observation impressions: `26`
- **Status**: `non_comparable` — measurement window が異なるため、正式な `impression_ratio_vs_ops002` として扱わない。

> Note: 137 は過去に一時的に使用された pre-correction baseline。canonical run record の OPS-002 は 149（late measurement）で記録されている。OPS-006 の 26 は delayed observation のみなので、OPS-002 との参考 ratio は Canonical record には含めない。

## Qualitative Notes

- 24h 計測を失念したため、厳密な Distribution Learning 比較は不可能。
- 遅延観測時点で 26 impressions、likes 1、replies 1、reposts 0 を確認。
- この値は 24h 後の値ではないため、OPS-002（149 late measurement）との直接比較はできない。
- H009「営業/経営者の第一印象」が現時点で強い Distribution を示したとは言えないが、1投稿（かつ測定不完全）で H009 の勝敗を断定できない。
- CTA は reply/discussion 型を維持。text-only / image none / URL none / 2タグ構成。

## Result Verdict

Please check one:

- [ ] **strong** — significantly exceeded expectations.
- [ ] **acceptable** — met baseline expectations.
- [ ] **weak** — underperformed relative to expectations.
- [ ] **invalid_missing_metrics** — metrics could not be recorded.
- [x] **non_comparable** — delayed observation only; 24h metrics missed.
- [ ] **invalid_changed_post** — the posted text differed from the approved candidate.

> Cold Start label としては `non_comparable`。H009「営業/経営者の第一印象」を 1 投稿（かつ測定不完全）で retired / losing pattern 確定にしない。

## Lessons Learned

- 24h 計測を忘れると、Distribution Learning の比較実験として価値が大きく損なわれる（OPS-005 に続き2回目）。
- 遅延観測値（26）だけでは、H009 の構造・CTA・content_angle の効果を判断できない。
- 次回以降は、投稿時に metrics_due アラームまたはカレンダー登録を徹底する。

## Next Prompt Adjustment

- 24h 計測を厳守する運用ルールを強化する（2回連続ミス）。
- OPS-007 では既存Control条件を維持したまま content_angle のみを変更。
- H009 は測定不完全のため、別の content_angle（H007 若作りしないジャケット 等）へ pivot して角度分散を進める。

---

## Generated Metadata

- run_id: `20260914-1426-mens-fashion-gadget-corporate-to-personal`
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
- created_at: `2026-09-14T14:26:30.605644+09:00`
