# Learning Brief

## Source

- previous_run_id: `20260908-0801-mens-fashion-gadget-corporate-to-personal`
- hypothesis_id: `H002`
- content_genre: `40代ファッション×ガジェット`
- content_angle: `靴の手入れ`
- result_label: `no_signal`
- confidence: `medium`

## Quantitative Summary

- impressions_24h: `9`
- engagement_rate_24h: `0.0%`
- reply_rate_24h: `0.0%`
- bookmark_rate_24h: `unknown`
- profile_click_rate_24h: `unknown`
- follow_conversion_rate_24h: `unknown`
- impression_ratio_vs_ops002: `0.0604`
- raw_difference_vs_ops002: `-140`

> **Note**: 今回の metrics は約24時間18分後の late_24h_measurement です。

## Qualitative Summary

- strongest_signal: `none（明確な強信号はない）`
- weakest_signal: `low_distribution_no_engagement（impressions=9、engagement=0）`
- hook_learning: `「40代になって気づいた」型フックは自然だが、今回は Distribution まで届かなかった。`
- cta_learning: `「みんなの靴の手入れ、何が必須？」は OPS-002 に続いて反応を生まなかった。類似 CTA の連続使用を避ける。`
- structure_learning: `フック → 3つの具体例 → 価値転換 → CTA の構造は読みやすいが、画像なしでは保存/返信の動機が弱い。`
- audience_learning: `text-only の靴の手入れ一般論は、今回の条件では読者に広がらなかった。視覚変化や具体的な悩みが必要かもしれない。`
- timing_or_media_learning: `画像なし・平日午前投稿の影響を考慮。画像ありや別時間帯で変わる可能性がある。`

## Use Next Time

- try_next_time:
  - 靴の手入れを再検証するなら画像あり・ビフォーアフター必須
  - テキストだけなら「靴」よりも清潔感全体や失敗談に寄せる
  - 次は H003「爪・髪・香り」または H009「営業/経営者の第一印象」へ pivot
  - CTA を「みんなの〜、何が必須？」から変更して答えやすくする
- avoid_next_time:
  - 靴の手入れの一般論を text-only で繰り返す
  - 「高い靴より〜」だけの抽象フック
  - 返信前提 CTA の連続使用
  - H002 を1回の no_signal で retired にする
- recommended_content_genre: `40代ファッション×ガジェット`
- recommended_content_angle: `爪・髪・香り（第一候補） / 営業/経営者の第一印象（第二候補）`
- recommended_hook_style: `「40代になって気づいた」型を維持しつつ、content_angle を変更`
- recommended_cta_style: `reply / discussion / experience_sharing。ただし問いかけを絞り込み、答えやすくする。`
- recommended_target_reader: `40代男性 / 経営者 / 営業職 / 見た目と仕事道具を整えたい人`
- avoid_overlap_with_recent_posts: `バッグの中身、靴の手入れ、薄型財布、ガジェットポーチ、ワイヤレスイヤホン、「みんなの〜、何が必須？」CTA`

## Copyable Input Snippet

次回 run の `input.md` へ貼れる形で短くまとめる。

```text
Previous Learning:
- previous_run_id: 20260908-0801-mens-fashion-gadget-corporate-to-personal
- hypothesis_id: H002
- result_label: no_signal
- strongest_signal: none
- weakest_signal: low_distribution_no_engagement
- try_next_time: H003爪・髪・香り または H009営業/経営者の第一印象へpivot / 靴再検証なら画像あり・ビフォーアフター必須
- avoid_next_time: text-only靴手入れ一般論 / 「高い靴より〜」抽象フック / 返信前提CTA連続使用
- recommended_content_angle: 爪・髪・香り（第一候補） / 営業/経営者の第一印象（第二候補）
- recommended_hook_style: 「40代になって気づいた」型
- recommended_cta_style: reply/discussion。ただし絞り込んだ問いかけ
```

## Human Approval

- approved_for_reuse: `yes`
- human_notes: `H002 は no_signal だが retired にしない。次回は角度分散を優先。`

---

## Rules

- 断定しすぎない。
- Cold Start 期間は仮説として扱う。
- 「勝ちパターン」と言い切らない。
- Kimi/OpenCode へ貼れる短さにする。
- 学習の粒度は次回投稿生成に使えるレベルにする。
