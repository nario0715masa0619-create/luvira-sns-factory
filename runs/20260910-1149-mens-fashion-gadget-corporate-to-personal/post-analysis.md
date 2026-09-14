# Post Analysis

## Run Metadata

- run_id: `20260910-1149-mens-fashion-gadget-corporate-to-personal`
- ops_id: `OPS-005`
- hypothesis_id: `H003`
- content_genre: `40代ファッション×ガジェット`
- content_angle: `爪・髪・香り`
- account_type: `personal`
- source_account_type: `corporate`
- platform: `X`
- posted_at: `2026-09-11T22:41:00+09:00`
- post_url: `https://x.com/ritsu_opt/status/2098406679058797046?s=20`
- analyzed_at: `2026-09-14T15:00:00+09:00`

## Posted Content

- final_post_text: `40代になってから、服より先に見られてる気がするものがある。爪、髪、香り。高い服を着るより、爪が伸びてないこと。寝ぐせのまま出ないこと。香りが強すぎないこと。このへんが整ってるだけで、清潔感ってかなり変わる気がする。まず見直すなら、服より身だしなみかもしれない。`
- image_attached: `unknown`（投稿時の画像有無は記録されていない）
- image_type: `unknown`
- hashtags: `#40代ファッション #身だしなみ`
- cta: `（なし / 余韻型で終了）`

## Measurement Classification

- measurement_window: `delayed_observation`
- measurement_target: `strict_24h_preferred`
- measurement_status: `24h_missed_delayed_observation_recorded`
- 24h_metrics: `missed`

> **Important**: 以下の observed values は 24h 時点の値ではありません。

## Delayed Observation Values

| Metric | Observed Value |
|--------|----------------|
| observed_impressions_delayed | `29` |
| observed_likes_delayed | `1` |
| observed_replies_delayed | `1` |
| observed_reposts_delayed | `0` |

## Comparison with OPS-002

| Metric | OPS-002 Canonical | OPS-005 Delayed | Comparable? |
|--------|-------------------|-----------------|-------------|
| impressions | 149（late measurement） | 29（delayed） | no |
| raw_difference | - | - | non-comparable |

- OPS-002 canonical record: `impressions_24h=149`, `measurement_window=late_measurement`。strict 24h measurement ではない。
- OPS-005 は delayed observation のみ。
- measurement window が一致しないため、正式な ratio 比較（`impression_ratio_vs_ops002`）として扱わない。
- 137 は過去に一時的に使用された pre-correction baseline。OPS-005 の Canonical record には参考 ratio を含めない。

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
| reach_signal | `unknown` | 24h impressions missed。delayed observation で 29。公式比較不可。 |
| engagement_signal | `unknown` | 24h engagement missed。delayed observation で likes=1, replies=1, reposts=0。 |
| conversation_signal | `unknown` | delayed observation で replies=1 だが、24h 値ではない。 |
| save_signal | `unknown` | bookmarks unknown。 |
| conversion_signal | `unknown` | profile_clicks / follows unknown。 |

## Qualitative Review

| Aspect | Level | Notes |
|--------|-------|-------|
| hook_strength | `ok` | 「服より先に見られてる気がする」は個人の観察として自然。 |
| readability | `ok` | 短い対比リズムで読みやすい。 |
| specificity | `ok` | 爪・髪・香りを具体的に挙げている。 |
| commentability | `unknown` | 今回は CTA を省略して余韻で終了。反応の有無は 24h 計測がないため判断不可。 |
| saveability | `unknown` | 画像有無・保存数が不明。 |
| target_fit | `ok` | 40代男性 / 経営者 / 営業職に合致。 |
| brand_fit | `ok` | 清潔感・実用性軸を損なっていない。 |
| originality | `ok` | 個人アカウント口調への置換は適切。 |
| overlap_with_recent_posts | `low` | OPS-002/004 と content_angle は異なる。 |

## Diagnosis

- strongest_signal: `none（24h metrics なしのため）`
- weakest_signal: `measurement_missed（24h 計測失念により Distribution/Engagement の正式評価不可）`
- likely_reason_for_result: `判断不能。delayed observation 値（29）だけでは、構造・フック・CTA・画像・時間帯の効果を分離できない。`
- what_worked: `判断不能。ただし human edited により実体験断定を減らし、余韻型で終了した点は記録として残る。`
- what_did_not_work: `24h metrics の取得を失念したこと。これにより Distribution Learning 比較が不可能になった。`
- uncertainty: `高い。24h metrics がないため、H003 爪・髪・香りの強弱は全く判断できない。`
- external_factors: `投稿時間帯（2026-09-11 22:41 JST）、画像有無不明、ハッシュタグあり（#40代ファッション #身だしなみ）、URLなし、CTAなし、24h 計測ミス、アカウント状態・フォロワー数・属性は確認していない。`

## Result Label

- cold_start_label: `non_comparable`
- pdca_label: `non_comparable`
- label_reason: `24h metrics missed。delayed observation で impressions=29, likes=1, replies=1, reposts=0 を確認したが、measurement window が異なるため OPS-002 や過去 Run との正式比較不可。H003 を retired にする根拠にならない。`
- confidence: `low`

> Cold Start 期間中は1投稿だけで `win` / `reject` を安易に使わない。今回は測定不全のため `non_comparable` とする。

## Human Review

- reviewed_by: `human`
- human_notes: `OPS-005 は 24h 計測を失念したため、H003 の評価はできない。delayed observation 値は参考記録に留める。次回は 24h 計測を徹底する。`
- approved_for_learning: `yes（測定不全として記録する）`

---

## Next Prompt Adjustment

- 24h 計測を厳守する運用ルールを強化。
- OPS-006 では既存Control条件を維持したまま content_angle のみを H009 営業/経営者の第一印象 に変更。
- 変更変数は content_angle のみ。image / URL / CTA style / posting time / hashtag count / Target Tag は固定。
- H007 若作りしないジャケット、H003 爪・髪・香り再検証は Experiment Queue に候補として残すが、OPS-006 としては確定しない。

---

## Rules

- `metrics.md` は事実記録、`post-analysis.md` は解釈に限定する。
- 1投稿だけで winning pattern と断定しない。
- 不明な値は `unknown` と書く。
- `0` と `unknown` を区別する。
- 24h metrics がない状態で因果関係を断定しない。
- delayed observation 値を 24h 値として扱わない。
