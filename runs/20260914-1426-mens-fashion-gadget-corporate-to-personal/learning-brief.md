# Learning Brief

## Source

- previous_run_id: `20260914-1426-mens-fashion-gadget-corporate-to-personal`
- ops_id: `OPS-006`
- hypothesis_id: `H009`
- content_genre: `40代ファッション×ガジェット`
- content_angle: `営業/経営者の第一印象`
- result_label: `non_comparable`
- confidence: `low`

## Quantitative Summary

- impressions_24h: `missed`
- engagement_rate_24h: `missed`
- reply_rate_24h: `missed`
- bookmark_rate_24h: `missed`
- profile_click_rate_24h: `missed`
- follow_conversion_rate_24h: `missed`
- impression_ratio_vs_ops002: `not_comparable`
- raw_difference_vs_ops002: `not_comparable`

> **Note**: 今回は 24h metrics を取得できず、delayed observation のみ。observed_impressions_delayed=26、observed_likes_delayed=1、observed_replies_delayed=1、observed_reposts_delayed=0。

## Qualitative Summary

- strongest_signal: `none（24h metrics なしのため）`
- weakest_signal: `measurement_missed`
- hook_learning: `「商談の第一印象って『高い服』より細かいところで決まる気がする」は個人の観察として自然だったが、効果測定できなかった。`
- cta_learning: `今回は経験共有型CTAを使用。24h 反応は不明。`
- structure_learning: `短い対比リズム（高い服より〜）と具体例の列挙は読みやすい。効果は測定不可。`
- audience_learning: `判断不能。delayed observation 値だけでは読者反応を推定できない。`
- timing_or_media_learning: `投稿時間帯は 22:08 JST。画像なし。24h 計測がないため要因分離不可。`

## Use Next Time

- try_next_time:
  - 24h 計測を徹底する（アラーム・カレンダー登録）
  - OPS-007 は既存Control条件を維持したまま content_angle のみを H007 若作りしないジャケット に変更
  - H009 営業/経営者の第一印象 は測定不完全のため、将来の再検証候補として保持
- avoid_next_time:
  - 24h metrics を取得せずに delayed observation だけで判断すること
  - OPS-006 の 26 impressions を 24h 値として扱うこと
  - H009 を 1 投稿（かつ測定不完全）で retired / losing pattern にすること
  - OPS-007 で content_angle 以外（image / CTA style / posting time 等）を同時に変更すること
- recommended_content_genre: `40代ファッション×ガジェット`
- recommended_content_angle: `H007 若作りしないジャケット`
- recommended_hook_style: `「40代になって気づいた」型を維持。content_angle のみ変更。`
- recommended_cta_style: `reply / discussion / experience_sharing（canonical CTA style を維持）`
- recommended_target_reader: `40代男性 / 経営者 / 営業職 / 見た目と仕事道具を整えたい人`
- avoid_overlap_with_recent_posts: `バッグの中身、靴の手入れ、爪・髪・香り、営業/経営者の第一印象`

## Copyable Input Snippet

次回 run の `input.md` へ貼れる形で短くまとめる。

```text
Previous Learning:
- previous_run_id: 20260914-1426-mens-fashion-gadget-corporate-to-personal
- hypothesis_id: H009
- result_label: non_comparable
- strongest_signal: none
- weakest_signal: measurement_missed
- try_next_time: 24h計測徹底 / OPS-007はcontent_angleのみH007若作りしないジャケットへ変更
- avoid_next_time: 24h metrics未取得でdelayed observationのみで判断 / H009を1投稿でretired扱い / OPS-007でimage・CTA style・posting timeを同時変更
- recommended_content_angle: H007若作りしないジャケット
- recommended_hook_style: 「40代になって気づいた」型を維持
- recommended_cta_style: reply/discussion/experience_sharing（canonical CTA styleを維持）
- experiment_control: image=none, URL=none, Target Tag=#40代ファッション, hashtag_count=2, posting_time=existing control
```

## Human Approval

- approved_for_reuse: `yes（測定不全として記録）`
- human_notes: `OPS-006 は 24h 計測を失念。H009 の評価は保留。次回は 24h 計測徹底と H007 若作りしないジャケット へ pivot。`

---

## Rules

- 断定しすぎない。
- Cold Start 期間は仮説として扱う。
- 「勝ちパターン」と言い切らない。
- Kimi/OpenCode へ貼れる短さにする。
- 学習の粒度は次回投稿生成に使えるレベルにする。
- delayed observation を 24h metrics として扱わない。
