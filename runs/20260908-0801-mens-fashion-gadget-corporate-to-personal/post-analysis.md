# Post Analysis

## Run Metadata

- run_id: `20260908-0801-mens-fashion-gadget-corporate-to-personal`
- hypothesis_id: `H002`
- content_genre: `40代ファッション×ガジェット`
- content_angle: `靴の手入れ`
- account_type: `personal`
- source_account_type: `corporate`
- platform: `X`
- posted_at: `2026-09-09T10:29:00+09:00`
- post_url: `https://x.com/ritsu_opt/status/2097497349392359722?s=20`
- analyzed_at: `2026-09-10T10:47:00+09:00`

## Posted Content

- final_post_text: `40代になって、高い靴よりちゃんと手入れしてる靴の方が大事だと気づいた。自分がやってるのは3つ：① 週1回ブラシでホコリを落とす ② 月1回クリームを塗る ③ 雨の日は翌日に乾拭きする。高い靴じゃなくても、手入れが行き届いてるだけで全然違う。みんなの靴の手入れ、何が必須？`
- image_attached: `no`
- image_type: `none`
- hashtags: `#40代ファッション #靴の手入れ`
- cta: `みんなの靴の手入れ、何が必須？`

## 24h Metrics

- impressions_24h: `9`
- likes_24h: `0`
- replies_24h: `0`
- comments_24h: `0`
- follows_24h: `0`
- reposts_24h: `unknown`
- bookmarks_24h: `unknown`
- profile_clicks_24h: `unknown`

> **Measurement Note**: これは late_24h_measurement です。strict 24h 時刻（2026-09-10T10:29:00+09:00）を約18分過ぎて計測しています。

## Comparison with OPS-002

| Metric | OPS-002 | OPS-004 | Ratio / Difference |
|--------|---------|---------|--------------------|
| impressions | 149 | 9 | 0.0604 |
| raw_difference | - | - | -140 |

OPS-002 比で約 6.0% の Distribution。大幅に低い。

## Calculated Metrics

- engagement_rate_24h: `0.0%`
- reply_rate_24h: `0.0%`
- bookmark_rate_24h: `unknown`
- profile_click_rate_24h: `unknown`
- follow_conversion_rate_24h: `unknown`

## Quantitative Review

| Signal | Level | Notes |
|--------|-------|-------|
| reach_signal | `weak` | impressions=9。OPS-002（149）と比較して大幅に低い。ほとんど配信されていない。 |
| engagement_signal | `weak` | likes / replies / comments / follows = 0。reposts / bookmarks / profile_clicks は unknown。 |
| conversation_signal | `weak` | replies=0。CTA に反応なし。 |
| save_signal | `unknown` | bookmarks=unknown。 |
| conversion_signal | `unknown` | profile_clicks / follows = unknown。 |

## Qualitative Review

| Aspect | Level | Notes |
|--------|-------|-------|
| hook_strength | `ok` | 「40代になって、高い靴よりちゃんと手入れしてる靴の方が大事だと気づいた」は自然な個人の気づき。 |
| readability | `ok` | 3つの手入れ例と価値転換が読みやすい。 |
| specificity | `ok` | ブラシ・クリーム・乾拭きと具体例がある。 |
| commentability | `weak` | CTA「みんなの靴の手入れ、何が必須？」に反応なし。回答コストが高い可能性。 |
| saveability | `weak` | 画像なしで視覚的インパクトがない。保存動機が弱い。 |
| target_fit | `ok` | 40代男性 / 経営者 / 営業職というターゲットに合致している。 |
| brand_fit | `ok` | 高級品ではなく清潔感・実用性という brand 軸を損なっていない。 |
| originality | `ok` | 個人アカウント口調への置換は適切。 |
| overlap_with_recent_posts | `low` | OPS-002/003 と content_angle は異なる。ただし CTA 形式が同一。 |

## Diagnosis

- strongest_signal: `none（明確な強信号はない）`
- weakest_signal: `low_distribution_no_engagement（impressions=9、engagement=0）`
- likely_reason_for_result: `text-only / 画像なしで、視覚的変化が伝わりにくい。靴の手入れ一般論が具体的な悩みや共感ポイントに結びつきにくかった。投稿時間帯・平日朝・平日夜の差異・アカウント状態の影響も考えられる。`
- what_worked: `個人の気づき型フック、3つの具体例、清潔感軸、個人アカウント口調。`
- what_did_not_work: `画像なしによる視覚的インパクトの欠如。抽象的な「手入れ一般論」が広がりにくかった。CTA が反応を誘発できなかった。`
- uncertainty: `1投稿のみなので、H002 靴の手入れ全体が弱いと断定できない。画像あり・ビフォーアフター・別時間帯で変わる可能性がある。late_24h_measurement（約24時間18分）であることも考慮。`
- external_factors: `投稿時間帯（平日午前10:29）、画像なし、ハッシュタグあり（#40代ファッション #靴の手入れ）、URLなし、text-only、計測遅延（約18分）、アカウント初期状態・フォロワー数・属性は確認していない。`

## Result Label

- cold_start_label: `no_signal`
- pdca_label: `weak`
- label_reason: `impressions=9 で OPS-002（149）比 0.0604。engagement も 0。Distribution Learning Run としても弱い結果。ただし1投稿だけで H002 を reject しない。`
- confidence: `medium`

> Cold Start 期間中は1投稿だけで `win` / `reject` を安易に使わない。H002 は `no_signal` だが、retired にはしない。

## Human Review

- reviewed_by: `human`
- human_notes: `OPS-004 は text-only 靴の手入れで Distribution・Engagement ともに弱い。次回は角度分散（H003 または H009）を優先。靴の手入れ再検証の場合は画像あり・ビフォーアフターが必須。`
- approved_for_learning: `yes`

---

## Rules

- `metrics.md` は事実記録、`post-analysis.md` は解釈に限定する。
- 1投稿だけで winning pattern と断定しない。
- 不明な値は `unknown` と書く。
- `0` と `unknown` を区別する。
- 実 metrics がない状態で断定しない。
