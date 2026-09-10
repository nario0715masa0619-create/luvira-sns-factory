# Next Run Recommendation

## Source

- based_on_run_id: `20260908-0801-mens-fashion-gadget-corporate-to-personal`
- based_on_hypothesis_id: `H002`
- based_on_result_label: `no_signal`
- generated_at: `2026-09-10T10:47:00+09:00`

## Recommendation

- recommended_next_run_type: `pivot`
- recommended_hypothesis_id: `H003 or H009`
- recommended_content_genre: `40代ファッション×ガジェット`
- recommended_content_angle: `爪・髪・香り（第一候補） / 営業/経営者の第一印象（第二候補）`
- recommended_target_reader: `40代男性 / 経営者 / 営業職 / 見た目と仕事道具を整えたい人`
- desired_reaction: `共感リプライ・経験共有。清潔感やビジネス文脈での共感を狙う。`
- hook_direction: `「40代になって気づいた」型を維持。content_angle を爪・髪・香り または 営業/経営者の第一印象に変更。`
- cta_direction: `reply / discussion / experience_sharing。ただし「みんなの〜、何が必須？」ではなく、より絞り込んだ問いかけにする。`
- post_format: `text + image（検証対象として画像ありを試す）`
- media_recommendation: `画像ありを推奨。清潔感テーマではビフォーアフターや具体的なアイテムが視覚的に伝わりやすい。`

## Reason

- why_this_next: `H001 バッグの中身（149 impressions / engagement 0）と H002 靴の手入れ（9 impressions / engagement 0）の両方が no_signal 寄りだったため、次は角度を分散する。H002 は OPS-002 より大幅に弱く、text-only では広がりにくい可能性がある。`
- evidence: `OPS-004 late_24h_measurement: impressions=9, likes=0, replies=0, comments=0, follows=0。impression_ratio_vs_ops002 = 0.0604, raw_difference = -140。`
- uncertainty: `1投稿のみ。画像あり・別時間帯・別フックで H002 の結果は変わる可能性がある。late_24h_measurement（約24時間18分）であることも考慮。`
- risk_notes: `H003 は身だしなみケアでプライベート感が強く、H009 はビジネス色が強い。どちらも「上から目線」にならないように注意。`

## Overlap Avoidance

- recent_related_runs: `OPS-002（バッグの中身、metrics_recorded）、OPS-003（バッグの中身、held）、OPS-004（靴の手入れ、metrics_recorded）`
- overlap_risk: `high`（バッグの中身系・靴の手入れ系を続ける場合）
- avoid_topics: `バッグの中身、靴の手入れ、薄型財布、ガジェットポーチ、ワイヤレスイヤホン`
- avoid_phrases: `「みんなのバッグの中身、何が必須？」、「みんなの靴の手入れ、何が必須？」`
- avoid_items: `財布、ガジェットポーチ、ワイヤレスイヤホン、靴磨きセットの同じ組み合わせ`
- required_difference_from_recent_posts: `content_angle を爪・髪・香り または 営業/経営者の第一印象に変更。Target Tag は固定（#40代ファッション）し、Content Angle Tag を切り替える。`

## Draft Input Snippet

次回 run の `input.md` に貼れる形で書く。

```text
content_genre: 40代ファッション×ガジェット
content_angle: 爪・髪・香り（第一候補） / 営業/経営者の第一印象（第二候補）
target_reader: 40代男性 / 経営者 / 営業職 / 見た目と仕事道具を整えたい人
desired_reaction: 共感リプライ・経験共有。清潔感やビジネス文脈での共感を狙う。
hook_direction: 「40代になって気づいた」型を維持。content_angle を変更。
cta_direction: reply/discussion。ただし「何が必須？」よりも絞り込んだ問いかけ。
avoid_overlap: バッグの中身、靴の手入れ、薄型財布、ガジェットポーチ、ワイヤレスイヤホン、「みんなの〜、何が必須？」CTA
previous_learning: OPS-004 H002 靴の手入れは no_signal（impressions=9, engagement=0）。OPS-002比0.0604。text-only靴手入れ一般論は今回広がらなかった。次は角度分散と画像ありを試す。
```

## Human Approval

- approved_for_next_run: `yes`
- human_notes: `H003 爪・髪・香りを最優先。画像あり/なしは別途判断。`

---

## Rules

- 直近2投稿と同じ切り口を避ける。
- バッグの中身系・靴の手入れ系を連投しない。
- OPS-002 の metrics が出るまでは OPS-003 は投稿保留。
- `repeat` は再現性確認目的の場合のみ。
- `pivot` は `no_signal` の場合に使う。
- `iterate` は `weak_signal / promising` の場合に使う。
