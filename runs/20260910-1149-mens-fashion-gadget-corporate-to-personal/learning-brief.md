# Learning Brief

## Source

- previous_run_id: `20260910-1149-mens-fashion-gadget-corporate-to-personal`
- ops_id: `OPS-005`
- hypothesis_id: `H003`
- content_genre: `40代ファッション×ガジェット`
- content_angle: `爪・髪・香り`
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

> **Note**: 今回は 24h metrics を取得できず、delayed observation のみ。observed_impressions_delayed=29、observed_likes_delayed=1、observed_replies_delayed=1、observed_reposts_delayed=0。

## Qualitative Summary

- strongest_signal: `none（24h metrics なしのため）`
- weakest_signal: `measurement_missed`
- hook_learning: `「服より先に見られてる気がする」型フックは観察・気づきとして自然だったが、効果測定できなかった。`
- cta_learning: `今回は CTA を省略して余韻で終了。24h 反応は不明。次回は CTA 有無を意識的に比較したい。`
- structure_learning: `短い対比リズム（高い服を着るより〜）は OPS-002/004 の3箇条リストと異なる構造。効果は測定不可。`
- audience_learning: `判断不能。delayed observation 値だけでは読者反応を推定できない。`
- timing_or_media_learning: `投稿時間帯は 22:41 JST。画像有無は記録されていない。24h 計測がないため要因分離不可。`

## Use Next Time

- try_next_time:
  - 24h 計測を徹底する（アラーム・カレンダー登録）
  - OPS-006 は既存Control条件を維持したまま content_angle のみを H009 営業/経営者の第一印象 に変更
  - H007 若作りしないジャケット、H003 爪・髪・香り再検証は Experiment Queue に候補として残す
- avoid_next_time:
  - 24h metrics を取得せずに delayed observation だけで判断すること
  - OPS-005 の 29 impressions を 24h 値として扱うこと
  - H003 を 1 投稿（かつ測定不完全）で retired / losing pattern にすること
  - OPS-006 で content_angle 以外（image / CTA style / posting time 等）を同時に変更すること
- recommended_content_genre: `40代ファッション×ガジェット`
- recommended_content_angle: `H009 営業/経営者の第一印象`
- recommended_hook_style: `「40代になって気づいた」型を維持。content_angle のみ変更。`
- recommended_cta_style: `reply / discussion / experience_sharing（canonical CTA style を維持）`
- recommended_target_reader: `40代男性 / 経営者 / 営業職 / 見た目と仕事道具を整えたい人`
- avoid_overlap_with_recent_posts: `バッグの中身、靴の手入れ、爪・髪・香り（直近の再検証は避ける）`

## Copyable Input Snippet

次回 run の `input.md` へ貼れる形で短くまとめる。

```text
Previous Learning:
- previous_run_id: 20260910-1149-mens-fashion-gadget-corporate-to-personal
- hypothesis_id: H003
- result_label: non_comparable
- strongest_signal: none
- weakest_signal: measurement_missed
- try_next_time: 24h計測徹底 / OPS-006はcontent_angleのみH009営業・経営者の第一印象へ変更
- avoid_next_time: 24h metrics未取得でdelayed observationのみで判断 / H003を1投稿でretired扱い / OPS-006でimage・CTA style・posting timeを同時変更
- recommended_content_angle: H009営業/経営者の第一印象
- recommended_hook_style: 「40代になって気づいた」型を維持
- recommended_cta_style: reply/discussion/experience_sharing（canonical CTA styleを維持）
- experiment_control: image=none, URL=none, Target Tag=#40代ファッション, hashtag_count=2, posting_time=existing control
```

## Human Approval

- approved_for_reuse: `yes（測定不全として記録）`
- human_notes: `OPS-005 は 24h 計測を失念。H003 の評価は保留。次回は 24h 計測を徹底し、H003 再検証または H009/H007 へ pivot。`

---

## Rules

- 断定しすぎない。
- Cold Start 期間は仮説として扱う。
- 「勝ちパターン」と言い切らない。
- Kimi/OpenCode へ貼れる短さにする。
- 学習の粒度は次回投稿生成に使えるレベルにする。
- delayed observation を 24h metrics として扱わない。
