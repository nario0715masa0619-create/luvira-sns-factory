# Post Analysis

## Run Metadata

- run_id: `20260906-2132-mens-fashion-gadget-corporate-to-personal`
- hypothesis_id: `H001`
- content_genre: `40代ファッション×ガジェット`
- content_angle: `バッグの中身`
- account_type: `personal`
- source_account_type: `corporate`
- platform: `X`
- posted_at: `2026-09-06T22:35:48+09:00`
- post_url: `https://x.com/ritsu_opt/status/2096593132653572341?s=20`
- analyzed_at: `2026-09-09T07:46:00+09:00`

## Posted Content

- final_post_text: `40代男性のバッグの中身、見直すと仕事の印象変わる。自分が最近整えた3つ：① 薄型長財布（膨らまない） ② ガジェットポーチ（ケーブルごちゃごちゃ防止） ③ ワイヤレスイヤホン（安いのを良品に）。高級品じゃなくても、清潔にまとまってるだけで自信が違う。みんなのバッグの中身、何が必須？`
- image_attached: `no`
- image_type: `none`
- hashtags: `#40代ファッション #バッグの中身`
- cta: `みんなのバッグの中身、何が必須？`

## 24h Metrics

- impressions_24h: `149`
- likes_24h: `0`
- replies_24h: `0`
- reposts_24h: `0`
- bookmarks_24h: `0`
- profile_clicks_24h: `unknown`
- follows_24h: `unknown`

> **Measurement Note**: これは late measurement です。本来の24h計測時刻（2026-09-07T22:35:48+09:00）を過ぎており、2026-09-09T07:46:00+09:00（投稿後約57時間10分）に計測しました。数値の解釈には注意が必要です。

## Calculated Metrics

- engagement_rate_24h: `0.0%`
- reply_rate_24h: `0.0%`
- bookmark_rate_24h: `0.0%`
- profile_click_rate_24h: `unknown`
- follow_conversion_rate_24h: `unknown`

## Quantitative Review

| Signal | Level | Notes |
|--------|-------|-------|
| reach_signal | `ok` | 149 impressions は当該アカウントの通常水準と比較して良好。ただし late measurement なので解釈に注意。 |
| engagement_signal | `weak` | likes / replies / reposts / bookmarks すべて 0。表示から反応への転換が全く機能していない。 |
| conversation_signal | `weak` | replies=0。CTA「みんなのバッグの中身、何が必須？」に反応がなかった。 |
| save_signal | `weak` | bookmarks=0。保存したくなる具体性や参考価値が不足している可能性。 |
| conversion_signal | `unknown` | profile_clicks / follows は未取得。判断不能。 |

## Qualitative Review

| Aspect | Level | Notes |
|--------|-------|-------|
| hook_strength | `ok` | 「40代男性のバッグの中身、見直すと仕事の印象変わる」はターゲットに刺さる切り口。reach に寄与した可能性。 |
| readability | `ok` | 3つの具体例と価値転換が読みやすい。 |
| specificity | `ok` | 薄型長財布、ガジェットポーチ、ワイヤレスイヤホンと具体例がある。 |
| commentability | `weak` | CTA は問いかけ型だが、回答の幅が広すぎて返信しにくい。「何が必須？」ではなく「まず何を減らす？」の方が答えやすい可能性。 |
| saveability | `weak` | 保存したくなる「参考リスト」感はあるが、画像がないため視覚的インパクトが弱い。 |
| target_fit | `ok` | 40代男性 / 経営者 / 営業職というターゲットに合致している。 |
| brand_fit | `ok` | 高級品ではなく清潔感・実用性という brand 軸を損なっていない。 |
| originality | `ok` | 似た構造の投稿は多いが、個人アカウント口調への置換は適切。 |
| overlap_with_recent_posts | `none` | 直近に同じテーマの投稿はない。OPS-003 は未投稿。 |

## Diagnosis

- strongest_signal: `impressions のみ（149）。当該アカウント水準では reach 獲得に一定の可能性がある。`
- weakest_signal: `engagement 全般（likes/replies/reposts/bookmarks=0）。表示から反応への転換が全く機能していない。`
- likely_reason_for_result: `フックとテーマは「見る」には十分だったが、「反応する」ための CTA と共感の深さが不足。画像の欠如も保存/共有の障壁になった可能性。late measurement なので時間経過による自然増も含まれている可能性。`
- what_worked: `ジャンル方向性（40代男性×ファッション×ガジェット）、清潔感軸、個人アカウント口調、具体的小物例、価値転換（高級品じゃなくても）。`
- what_did_not_work: `CTA が反応を誘発できていない。保存/返信の動機が弱い。画像がない。実体験が薄く「自信が違う」と言い切っている。`
- uncertainty: `1投稿のみなので、149 impressions が corporate-to-personal 転換の効果か、ハッシュタグの効果か、たまたまかは確定しない。計測も57時間後の late measurement なので純粋な24h値ではない。画像なし・投稿時間（平日夜）・アカウント初期状態・フォロワー状態の影響も考慮する必要がある。`
- external_factors: `投稿時間帯（平日夜）、画像なし、ハッシュタグあり（#40代ファッション #バッグの中身）、URLなし、計測遅延（57時間後）、アカウント初期状態・フォロワー数・属性は確認していない。`

## Result Label

- cold_start_label: `no_signal`
- pdca_label: `weak`
- label_reason: `Distribution（149 impressions）は当該アカウント水準で良好な可能性があるが、目標とする反応獲得（likes / replies / reposts / bookmarks）がすべて0だった。ただし、late measurement かつ1投稿のみなので、H001 を reject するには不十分。`
- confidence: `low`

> Cold Start 期間中は1投稿だけで `win` / `reject` を安易に使わない。H001 は `no_signal` 寄りだが、retired にはしない。

## Human Review

- reviewed_by: `human`
- human_notes: `OPS-002 は表示獲得には一定の可能性があるが、反応獲得は未達。late measurement のため解釈に注意。次回は角度を分散し、靴/清潔感へ pivot する。`
- approved_for_learning: `yes`

---

## Rules

- `metrics.md` は事実記録、`post-analysis.md` は解釈に限定する。
- 1投稿だけで winning pattern と断定しない。
- 不明な値は `unknown` と書く。
- `0` と `unknown` を区別する。
- 実 metrics がない状態で断定しない。
- late measurement の場合は confidence を低くし、解釈に注意を書く。
