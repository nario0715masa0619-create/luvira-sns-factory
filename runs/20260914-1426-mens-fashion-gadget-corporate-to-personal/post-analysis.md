# Post Analysis

## Run Metadata

- run_id: `20260914-1426-mens-fashion-gadget-corporate-to-personal`
- ops_id: `OPS-006`
- hypothesis_id: `H009`
- content_genre: `40代ファッション×ガジェット`
- content_angle: `営業/経営者の第一印象`
- account_type: `personal`
- source_account_type: `corporate`
- platform: `X`
- posted_at: `2026-09-14T22:08:00+09:00`
- post_url: `https://x.com/ritsu_opt/status/2099485363559624746?s=20`
- analyzed_at: `2026-09-17T15:00:00+09:00`

## Posted Content

- final_post_text: `40代になって、商談の第一印象って「高い服」より細かいところで決まる気がする。ジャケットの袖丈。手入れされた靴。名刺を出すときの手元。どれも派手じゃないけど、こういう部分が整ってる人は、それだけでちゃんとして見える。営業や商談で、みんなが気をつけてるポイントって何？`
- image_attached: `no`
- image_type: `none`
- hashtags: `#40代ファッション #第一印象`
- cta: `営業や商談で、みんなが気をつけてるポイントって何？`

## Measurement Classification

- measurement_window: `delayed_observation`
- measurement_target: `strict_24h_preferred`
- measurement_status: `24h_missed_delayed_observation_recorded`
- 24h_metrics: `missed`

> **Important**: 以下の observed values は 24h 時点の値ではありません。

## Delayed Observation Values

| Metric | Observed Value |
|--------|----------------|
| observed_impressions_delayed | `26` |
| observed_likes_delayed | `1` |
| observed_replies_delayed | `1` |
| observed_reposts_delayed | `0` |
| observation_time | `2026-09-17T15:00:00+09:00（約65時間後）` |

## Comparison with OPS-002

| Metric | OPS-002 Canonical | OPS-006 Delayed | Comparable? |
|--------|-------------------|-----------------|-------------|
| impressions | 149（late measurement） | 26（delayed） | no |
| raw_difference | - | - | non-comparable |

- OPS-002 canonical record: `impressions_24h=149`, `measurement_window=late_measurement`。strict 24h measurement ではない。
- OPS-006 は delayed observation のみ。
- measurement window が一致しないため、正式な ratio 比較（`impression_ratio_vs_ops002`）として扱わない。

## Calculated Metrics

- engagement_rate_24h: `missed`
- reply_rate_24h: `missed`
- bookmark_rate_24h: `missed`
- profile_click_rate_24h: `missed`
- follow_conversion_rate_24h: `missed`
- impression_ratio_vs_ops002: `not_comparable`
- raw_difference_vs_ops002: `not_comparable`

## Quantitative Review

| Signal | Level | Notes |
|--------|-------|-------|
| reach_signal | `unknown` | 24h impressions missed。delayed observation で 26。公式比較不可。 |
| engagement_signal | `unknown` | 24h engagement missed。delayed observation で likes=1, replies=1, reposts=0。 |
| conversation_signal | `unknown` | delayed observation で replies=1 だが、24h 値ではない。 |
| save_signal | `unknown` | bookmarks unknown。 |
| conversion_signal | `unknown` | profile_clicks / follows unknown。 |

## Qualitative Review

| Aspect | Level | Notes |
|--------|-------|-------|
| hook_strength | `ok` | 「商談の第一印象って『高い服』より細かいところで決まる気がする」は個人の観察として自然。 |
| readability | `ok` | 短い対比リズムで読みやすい。 |
| specificity | `ok` | 袖丈・靴・手元と具体的に挙げている。 |
| commentability | `unknown` | 経験共有型CTAを使用。24h 反応は不明。 |
| saveability | `unknown` | 画像なし・保存数不明。 |
| target_fit | `ok` | 40代男性 / 経営者 / 営業職に合致。 |
| brand_fit | `ok` | 清潔感・実用性軸を損なっていない。 |
| originality | `ok` | 個人アカウント口調への置換は適切。H003 との単純な言い換えを避けた。 |
| overlap_with_recent_posts | `low` | OPS-005 H003 / OPS-006 H009 と content_angle は異なる。 |

## Diagnosis

- strongest_signal: `none（24h metrics なしのため）`
- weakest_signal: `measurement_missed（24h 計測失念により Distribution/Engagement の正式評価不可）`
- likely_reason_for_result: `判断不能。delayed observation 値（26）だけでは、構造・フック・CTA・content_angleの効果を分離できない。`
- what_worked: `判断不能。ただし human edited により AI 生成感・強い因果表現・H003 重複を抑えた点は記録として残る。`
- what_did_not_work: `24h metrics の取得を失念したこと。これにより H009 の評価が不可能になった。`
- uncertainty: `高い。24h metrics がないため、H009 の強弱は全く判断できない。`
- external_factors: `投稿時間帯（2026-09-14 22:08 JST）、画像なし、ハッシュタグあり（#40代ファッション #第一印象）、URLなし、text-only、24h 計測ミス（2回連続）、アカウント状態・フォロワー数・属性は確認していない。`

## Result Label

- cold_start_label: `non_comparable`
- pdca_label: `non_comparable`
- label_reason: `24h metrics missed。delayed observation で impressions=26, likes=1, replies=1, reposts=0 を確認したが、measurement window が異なるため OPS-002 や過去 Run との正式比較不可。H009 を retired にする根拠にならない。`
- confidence: `low`

> Cold Start 期間中は1投稿だけで `win` / `reject` を安易に使わない。今回は測定不全のため `non_comparable` とする。

## Human Review

- reviewed_by: `human`
- human_notes: `OPS-006 は 24h 計測を失念したため、H009 の評価はできない。delayed observation 値は参考記録に留める。次回は 24h 計測を徹底し、H007 若作りしないジャケット へ pivot。`
- approved_for_learning: `yes（測定不全として記録する）`

---

## Next Prompt Adjustment

- 24h 計測を厳守する運用ルールを強化（2回連続ミス）。
- OPS-007 では既存Control条件を維持したまま content_angle のみを H007 若作りしないジャケット に変更。
- 変更変数は content_angle のみ。image / URL / CTA style / posting time / hashtag count / Target Tag は固定。
- H009 は測定不完全のため retired にせず、将来の再検証候補として保持。

---

## Rules

- `metrics.md` は事実記録、`post-analysis.md` は解釈に限定する。
- 1投稿だけで winning pattern と断定しない。
- 不明な値は `unknown` と書く。
- `0` と `unknown` を区別する。
- 24h metrics がない状態で因果関係を断定しない。
- delayed observation 値を 24h 値として扱わない。
