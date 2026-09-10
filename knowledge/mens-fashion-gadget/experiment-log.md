# Experiment Log: Mens Fashion Gadget

## Purpose

40代ファッション×ガジェットジャンルにおける投稿実験の履歴と結果を管理する。
同ジャンル内での比較、重複チェック、winning pattern 候補の発見に使用する。

## Current Phase

Cold Start exploration.

## Rules

- 初期10投稿は探索期間とする。
- 1投稿だけで勝ち負けを決めない。
- 同じテーマを連投しない。
- `result_label` は metrics 確認後に更新する。
- `0` と `unknown` を区別する。
- 人間承認後に更新する。
- Experiment Control Principle: Observed Good Condition → Hold Constant Until Tested。良好だったRunの条件は、検証対象でない限り可能な範囲で固定する。

## Experiment Table

| run_id | hypothesis_id | content_angle | status | posted_at | post_url | impressions_24h | likes_24h | replies_24h | reposts_24h | bookmarks_24h | profile_clicks_24h | follows_24h | result_label | strongest_signal | weakest_signal | next_action |
|--------|---------------|---------------|--------|-----------|----------|-----------------|-----------|-------------|-------------|---------------|--------------------|-------------|--------------|------------------|----------------|-------------|
| 20260906-2132-mens-fashion-gadget-corporate-to-personal | H001 | バッグの中身 | analyzed | 2026-09-06T22:35:48+09:00 | https://x.com/ritsu_opt/status/2096593132653572341?s=20 | 149 | 0 | 0 | 0 | 0 | unknown | unknown | no_signal | impressions_only_149_late_measurement | no_engagement | pivot_to_H002_or_H003 |
| 20260907-0751-mens-fashion-gadget-corporate-to-personal | H001 | バッグの中身 | generated | - | - | unknown | unknown | unknown | unknown | unknown | unknown | unknown | pending | unknown | unknown | hold_due_to_overlap_with_OPS-002 |
| 20260908-0801-mens-fashion-gadget-corporate-to-personal | H002 | 靴の手入れ | analyzed | 2026-09-09T10:29:00+09:00 | https://x.com/ritsu_opt/status/2097497349392359722?s=20 | 9 | 0 | 0 | unknown | unknown | unknown | 0 | no_signal | none | low_distribution_no_engagement | pivot_to_H003_or_H009 |

## Notes

- OPS-002 は実投稿済み。metrics_due_at は `2026-09-07T22:35:48+09:00`。
- OPS-003 は OPS-002 とテーマが強く重複するため、metrics 確認後に判断。
- 次回の新規 run は H002 または H003 から開始予定。
- **2026-09-08 修正**: 現時点の Luvira SNS Factory は Distribution Learning Phase。OPS-004 は H002 靴の手入れで、content_angle のみを変更し、同一運用フレームでの Distribution 確保可能性を検証。CTA形式・画像なし・URLなしは OPS-002 と同一に保つ。ハッシュタグは OPS-002 と同じ2タグ構成（Target Tag `#40代ファッション` 固定 + Content Angle Tag `#靴の手入れ`）を維持。engagement は参考記録。成功基準は OPS-002（impressions=137）との生ratio（impression_ratio_vs_ops002）を中心に記録。現時点では閾値分類を新規固定しない。
- **2026-09-09 Phase 3-C 更新**: OPS-002 late measurement（投稿後約57時間10分）で impressions=149, engagement=0。result_label=no_signal。ただし1投稿だけで H001 を reject せず、次回は H002 靴の手入れまたは H003 爪・髪・香りへ pivot。
- **2026-09-10 Phase 3-D 更新**: OPS-004 late_24h_measurement（約24時間18分）で impressions=9, engagement=0。impression_ratio_vs_ops002=0.0604、raw_difference=-140。result_label=no_signal。H002 は1投稿だけで retired にせず、次回は H003 爪・髪・香りまたは H009 営業/経営者の第一印象へ pivot。
