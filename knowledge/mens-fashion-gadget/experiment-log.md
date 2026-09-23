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
| 20260910-1149-mens-fashion-gadget-corporate-to-personal | H003 | 爪・髪・香り | analyzed | 2026-09-11T22:41:00+09:00 | https://x.com/ritsu_opt/status/2098406679058797046?s=20 | missed | missed | missed | missed | missed | missed | missed | non_comparable | none | measurement_missed | 24h計測徹底 / OPS-006はH009へcontent_angleのみ変更 |
| 20260914-1426-mens-fashion-gadget-corporate-to-personal | H009 | 営業/経営者の第一印象 | analyzed | 2026-09-14T22:08:00+09:00 | https://x.com/ritsu_opt/status/2099485363559624746?s=20 | missed | missed | missed | missed | missed | missed | missed | non_comparable | none | measurement_missed | 24h計測徹底（2回連続）/ OPS-007はH007へcontent_angleのみ変更 |
| 20260917-1516-mens-fashion-gadget-corporate-to-personal | H007 | 若作りしないジャケット | analyzed | 2026-09-17T15:26:00+09:00 | - | missed | missed | missed | missed | missed | missed | missed | non_comparable | delayed 39 imp / 1 like / 1 reply | measurement_missed | 3回連続測定問題; OPS-008はinformation_structure変更 |
| 20260920-1140-mens-fashion-gadget-corporate-to-personal | H007 | 若作りしないジャケット | analyzed | 2026-09-21T00:22:00+09:00 | https://x.com/ritsu_opt/status/2101693388466876709?s=20 | missed | missed | missed | missed | missed | missed | missed | non_comparable | near-24h 22 imp / 0 engagement | measurement_missed | information_structure=practical_information; inconclusive |

## Notes

- OPS-002 は実投稿済み。metrics_due_at は `2026-09-07T22:35:48+09:00`。
- OPS-003 は OPS-002 とテーマが強く重複するため、metrics 確認後に判断。
- 次回の新規 run は H002 または H003 から開始予定。
- **2026-09-08 修正**: 現時点の Luvira SNS Factory は Distribution Learning Phase。OPS-004 は H002 靴の手入れで、content_angle のみを変更し、同一運用フレームでの Distribution 確保可能性を検証。CTA形式・画像なし・URLなしは OPS-002 と同一に保つ。ハッシュタグは OPS-002 と同じ2タグ構成（Target Tag `#40代ファッション` 固定 + Content Angle Tag `#靴の手入れ`）を維持。engagement は参考記録。成功基準は OPS-002（impressions=149、late measurement）との生ratio（impression_ratio_vs_ops002）を中心に記録。現時点では閾値分類を新規固定しない。
- **2026-09-09 Phase 3-C 更新**: OPS-002 late measurement（投稿後約57時間10分）で impressions=149, engagement=0。result_label=no_signal。ただし1投稿だけで H001 を reject せず、次回は H002 靴の手入れまたは H003 爪・髪・香りへ pivot。
- **2026-09-10 Phase 3-D 更新**: OPS-004 late_24h_measurement（約24時間18分）で impressions=9, engagement=0。impression_ratio_vs_ops002=0.0604、raw_difference=-140。result_label=no_signal。H002 は1投稿だけで retired にせず、次回は H003 爪・髪・香りまたは H009 営業/経営者の第一印象へ pivot。
- **2026-09-14 Phase 3-E 更新**: OPS-005 は 24h 計測を失念し、delayed observation で impressions=29, likes=1, replies=1, reposts=0 を確認。measurement window が OPS-002 と異なるため、impression_ratio_vs_ops002 は計算しない。result_label=non_comparable。H003 を1投稿（かつ測定不完全）で retired / losing pattern にしない。OPS-006 では既存Control条件を維持したまま content_angle のみを H009 営業/経営者の第一印象 に変更。H007 若作りしないジャケット、H003 爪・髪・香り再検証は Experiment Queue に候補として残す。人間承認後に確定。
- **2026-09-17 Phase 3-F 更新**: OPS-006 は 24h 計測を失念（2回連続）。delayed observation（約65時間後）で impressions=26, likes=1, replies=1, reposts=0 を確認。measurement window が OPS-002 と異なるため、formal ratio 比較不可。result_label=non_comparable。H009 を1投稿（かつ測定不完全）で retired / losing pattern にしない。OPS-007 では既存Control条件を維持したまま content_angle のみを H007 若作りしないジャケット に変更。24h 計測を徹底する。
- **2026-09-23 Phase 3-G 更新**: OPS-007 / OPS-008 も測定不完全。OPS-007 は delayed observation（39 imp / 1 like / 1 reply / 0 repost）、OPS-008 は near-24h observation（22 imp / 0 engagement）。両方 `non_comparable`。直近4 run（OPS-005〜008）で 24h metrics を取得できず、測定プロセスが最大のボトルネック。OPS-009 では H006 ワイヤレスイヤホン を採用し、strict 24h measurement を実験成立条件とする。詳細は `docs/pilots/ops009-autonomous-hypothesis-cycle-pilot.md`。
