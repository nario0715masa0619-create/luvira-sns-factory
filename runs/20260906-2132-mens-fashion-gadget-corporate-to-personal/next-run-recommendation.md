# Next Run Recommendation

## Source

- based_on_run_id: `20260906-2132-mens-fashion-gadget-corporate-to-personal`
- based_on_hypothesis_id: `H001`
- based_on_result_label: `no_signal`
- generated_at: `2026-09-09T07:46:00+09:00`

## Recommendation

- recommended_next_run_type: `pivot`
- recommended_hypothesis_id: `H002 or H003`
- recommended_content_genre: `40代ファッション×ガジェット`
- recommended_content_angle: `靴の手入れ（第一候補） / 爪・髪・香り（第二候補）`
- recommended_target_reader: `40代男性 / 経営者 / 営業職 / 見た目と仕事道具を整えたい人`
- desired_reaction: `共感リプライ・経験共有。画像ありで保存も狙う。`
- hook_direction: `「40代になって気づいた」型を維持。content_angle を靴/清潔感に変更。`
- cta_direction: `reply / discussion / experience_sharing。ただし「何が必須？」よりも「まず何を減らす？」のように絞り込んで答えやすくする。`
- post_format: `text + image（検証対象として画像ありを試す）`
- media_recommendation: `画像ありを推奨。バッグの中身の実物感・ビフォーアフターを示す可能性を検証。ただしDistribution Learning Run では画像あり/なしを変数とする場合は比較計画を明確にする。`

## Reason

- why_this_next: `OPS-002/OPS-003がバッグの中身に偏っているため、次は角度を分散する。H001 は1回の no_signal では捨てないが、連投は避ける。`
- evidence: `OPS-002 late measurement: impressions=149, likes=0, replies=0, reposts=0, bookmarks=0。reach の可能性はあるが engagement は0。`
- uncertainty: `late measurement かつ1投稿のみ。149 impressions が構造の効果か、ハッシュタグの効果か、たまたまかは確定しない。`
- risk_notes: `画像ありに変更すると変数が増えて比較が複雑になる。Distribution Learning Run で画像を変数とする場合は、OPS-002（画像なし）との比較を明確に記録する。`

## Overlap Avoidance

- recent_related_runs: `OPS-002（バッグの中身、posted）、OPS-003（バッグの中身、generated/held）`
- overlap_risk: `high`（バッグの中身系を続ける場合）
- avoid_topics: `バッグの中身、薄型財布、ガジェットポーチ、ワイヤレスイヤホン`
- avoid_phrases: `「みんなのバッグの中身、何が必須？」`
- avoid_items: `財布、ガジェットポーチ、ワイヤレスイヤホンの同じ組み合わせ`
- required_difference_from_recent_posts: `content_angle を靴/清潔感に変更。Target Tag は固定（#40代ファッション）し、Content Angle Tag を切り替える。`

## Draft Input Snippet

次回 run の `input.md` に貼れる形で書く。

```text
content_genre: 40代ファッション×ガジェット
content_angle: 靴の手入れ（第一候補） / 爪・髪・香り（第二候補）
target_reader: 40代男性 / 経営者 / 営業職 / 見た目と仕事道具を整えたい人
desired_reaction: 共感リプライ・経験共有。画像ありで保存も狙う。
hook_direction: 「40代になって気づいた」型を維持。content_angle を靴/清潔感に変更。
cta_direction: reply/discussion。ただし「何が必須？」よりも絞り込んで答えやすくする。
avoid_overlap: バッグの中身、薄型財布、ガジェットポーチ、ワイヤレスイヤホン、「みんなの〜、何が必須？」CTA
previous_learning: OPS-002 H001 バッグの中身は no_signal（impressions=149, engagement=0）。reach の可能性はあるが反応獲得は未達。late measurement かつ1投稿のみ。次は角度分散と画像ありを試す。
```

## Human Approval

- approved_for_next_run: `yes`
- human_notes: `H002 靴の手入れを最優先。画像あり/なしは別途判断。`

---

## Rules

- 直近2投稿と同じ切り口を避ける。
- バッグの中身系を連投しない。
- OPS-002 の metrics が出るまでは OPS-003 は投稿保留。
- `repeat` は再現性確認目的の場合のみ。
- `pivot` は `no_signal` の場合に使う。
- `iterate` は `weak_signal / promising` の場合に使う。
