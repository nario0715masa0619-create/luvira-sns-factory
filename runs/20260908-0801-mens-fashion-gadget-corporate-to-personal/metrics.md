# 24h Metrics Record

## Run Information

- run_id: `20260908-0801-mens-fashion-gadget-corporate-to-personal`
- platform: `X`
- post_url: `https://x.com/ritsu_opt/status/2097497349392359722?s=20`
- account_type: `personal`
- product_service: `40代男性向けファッション・ガジェット情報発信`
- selected_candidate_id: `candidate-01`

## Timing

- posted_at: `2026-09-09T10:29:00+09:00`
- metrics_due_at: `2026-09-10T10:29:00+09:00`
- metrics_recorded_at: `2026-09-10T10:47:00+09:00`
- measurement_window: `late_24h_measurement`
- elapsed_since_post: `約24時間18分`
- measurement_status: `metrics_recorded`
- measurement_target: `strict_24h_preferred`

## Comparison Baseline

- OPS-002 impressions: `149`（late measurement）
- Comparison metric: `impression_ratio_vs_ops002 = OPS-004 impressions / 149`
- hashtags: `#40代ファッション #靴の手入れ`
- image: `none`
- url: `none`

## 24h Metrics

| Metric | Value |
|--------|-------|
| impressions_24h | `9` |
| likes_24h | `0` |
| replies_24h | `0` |
| comments_24h | `0` |
| follows_24h | `0` |
| reposts_24h | `unknown` |
| bookmarks_24h | `unknown` |
| profile_clicks_24h | `unknown` |
| link_clicks_24h | `unknown` |
| engagement_rate_24h | `0.0%` |
| impression_ratio_vs_ops002 | `0.0604` |
| raw_difference_vs_ops002 | `-140` |

### Engagement Rate Calculation

```text
engagement_rate_24h = (likes_24h + comments_24h + reposts_24h + bookmarks_24h) / impressions_24h * 100
```

- Record as a percentage, e.g. `3.5%`.
- If `impressions_24h` is 0 or not recorded, leave this field blank or use `result_verdict: invalid_missing_metrics`.

## Qualitative Notes

- impressions は 9 と、OPS-002（149）と比較して大幅に低い。
- 可視エンゲージメント（likes / replies / reposts / bookmarks）はすべて 0 または unknown。
- text-only / 画像なし / 投稿時間 / アカウント状態 / テーマの一般論感が影響した可能性がある。
- 「高い靴より手入れ」という主張は自然だが、画像なしでは視覚的変化が伝わりにくい。
- CTA「みんなの靴の手入れ、何が必須？」に反応がなかった。

## Result Verdict

Please check one:

- [ ] **strong** — significantly exceeded expectations.
- [ ] **acceptable** — met baseline expectations.
- [ ] **weak** — underperformed relative to expectations.
- [x] **invalid_missing_metrics** — metrics could not be recorded.

> Cold Start label としては `no_signal`。ただし1投稿だけで H002「靴の手入れ」を retired / losing pattern 確定にしない。

## Lessons Learned

- text-only の靴の手入れ一般論投稿は、今回ほとんど配信されなかった。
- 視覚変化が重要なテーマは画像なしだと弱い可能性がある。
- CTA「みんなの〜、何が必須？」は OPS-002 に続いて反応を誘発できなかった。
- 次回は角度分散を優先し、H003 爪・髪・香り または H009 営業/経営者の第一印象 を試す。

## Next Prompt Adjustment

- 靴の手入れを再検証するなら画像あり・ビフォーアフター必須。
- テキストだけなら「靴」よりも清潔感全体や失敗談に寄せる。
- 次は H003 または H009 へ pivot。
- 「みんなの〜、何が必須？」型 CTA の連続使用を避ける。

---

## Generated Metadata

- run_id: `20260908-0801-mens-fashion-gadget-corporate-to-personal`
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
- created_at: `2026-09-08T08:01:44.360562+09:00`
