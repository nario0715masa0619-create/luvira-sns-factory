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

## Experiment Table

| run_id | hypothesis_id | content_angle | status | posted_at | post_url | impressions_24h | likes_24h | replies_24h | reposts_24h | bookmarks_24h | profile_clicks_24h | follows_24h | result_label | strongest_signal | weakest_signal | next_action |
|--------|---------------|---------------|--------|-----------|----------|-----------------|-----------|-------------|-------------|---------------|--------------------|-------------|--------------|------------------|----------------|-------------|
| 20260906-2132-mens-fashion-gadget-corporate-to-personal | H001 | バッグの中身 | waiting_metrics | 2026-09-06T22:35:48+09:00 | https://x.com/ritsu_opt/status/2096593132653572341?s=20 | unknown | unknown | unknown | unknown | unknown | unknown | unknown | pending | unknown | unknown | wait_24h_metrics |
| 20260907-0751-mens-fashion-gadget-corporate-to-personal | H001 | バッグの中身 | generated | - | - | unknown | unknown | unknown | unknown | unknown | unknown | unknown | pending | unknown | unknown | hold_due_to_overlap_with_OPS-002 |

## Notes

- OPS-002 は実投稿済み。metrics_due_at は `2026-09-07T22:35:48+09:00`。
- OPS-003 は OPS-002 とテーマが強く重複するため、metrics 確認後に判断。
- 次回の新規 run は H002 または H003 から開始予定。
