# 24h Metrics Record

## Run Information

- run_id: `20260906-2132-mens-fashion-gadget-corporate-to-personal`
- platform: `X`
- post_url: `https://x.com/ritsu_opt/status/2096593132653572341?s=20`
- account_type: `personal`
- product_service: `40代男性向けファッション・ガジェット情報発信`
- selected_candidate_id: `candidate-01`

## Timing

- posted_at: `2026-09-06T22:35:48+09:00`
- metrics_due_at: `2026-09-07T22:35:48+09:00`
- metrics_recorded_at: `2026-09-09T07:46:00+09:00`
- measurement_window: `late_measurement`
- elapsed_since_post: `約57時間10分`

> **Note**: 本来の metrics_due_at は 2026-09-07T22:35:48+09:00 でしたが、計測が遅れました。そのため strict 24h metrics ではなく late measurement として記録します。Cold Start 初回の参考データとして PDCA 分析には使用します。

## 24h Metrics

| Metric | Value |
|--------|-------|
| impressions_24h | `149` |
| likes_24h | `0` |
| replies_24h | `0` |
| reposts_24h | `0` |
| bookmarks_24h | `0` |
| profile_clicks_24h | `unknown` |
| follows_24h | `unknown` |
| engagement_rate_24h | `0.0%` |

### Engagement Rate Calculation

```text
engagement_rate_24h = (likes_24h + replies_24h + reposts_24h + bookmarks_24h) / impressions_24h * 100
```

- Record as a percentage, e.g. `3.5%`.
- If `impressions_24h` is 0 or not recorded, leave this field blank or use `result_verdict: invalid_missing_metrics`.

## Qualitative Notes

- impressions は当該アカウントの通常水準と比較して良好（149）。
- 一方、可視エンゲージメント（likes / replies / reposts / bookmarks）は 0。
- corporate-to-personal / genre correction 後に表示獲得が改善した可能性があるが、1投稿のみなので因果関係は確定しない。
- 計測は投稿後約57時間後の late measurement であるため、厳密な24h metrics ではない。
- CTA「みんなのバッグの中身、何が必須？」に対して返信が生まれなかった。
- 画像なし・投稿時間（平日夜）・アカウント初期状態・フォロワー状態の影響を考慮する必要がある。

## Result Verdict

Please check one:

- [ ] **strong** — significantly exceeded expectations.
- [ ] **acceptable** — met baseline expectations.
- [x] **weak** — underperformed relative to expectations.
- [ ] **invalid_missing_metrics** — metrics could not be recorded.
- [ ] **invalid_changed_post** — the posted text differed from the approved candidate.

> Cold Start label としては `no_signal` に近い。ただし1投稿だけで H001「バッグの中身」を reject しない。

## Lessons Learned

- 表示獲得は改善の兆候があるが、エンゲージメント（likes / replies / reposts / bookmarks）が0だった。
- フックやCTAが「見る」には十分だった可能性があるが、「反応する」には不十分だった可能性がある。
- バッグの中身テーマは、画像あり・より具体的なアイテム比較・ブランドなし実物感で再検証余地がある。
- 同ジャンル内での重複を避けつつ、次回は角度を分散する（靴/清潔感へ）。

## Next Prompt Adjustment

- 次回は角度を分散し、靴の手入れまたは爪・髪・香りを試す。
- CTAを「あなたの必須は？」よりも「まず何を減らす？」のように答えやすくする。
- 画像添付の有無を記録し、次回以降の比較材料にする。
- バッグの中身系をすぐ連投しない。

---

## Generated Metadata

- run_id: `20260906-2132-mens-fashion-gadget-corporate-to-personal`
- product_service: `40代男性向けファッション・ガジェット情報発信`
- product_slug: `mens-fashion-gadget`
- source_account_type: `corporate`
- account_type: `personal`
- desired_cta_style: `reply / discussion / experience_sharing`
- allowed_persona_expression: `僕 / 私 / 自分 / 主語省略`
- risk_tolerance: `balanced`
- target_platform: `X`
- target_audience: `40代男性 / 経営者 / 個人事業主 / 営業職 / 見た目と仕事道具を整えたい人`
- business_goal: `40代男性向けファッション×ガジェット投稿の反応獲得`
- model: `kimi-k2.7-code`
- execution_mode: `file_based_semi_automation`
- created_at: `2026-09-06T21:32:45.702245+09:00`
