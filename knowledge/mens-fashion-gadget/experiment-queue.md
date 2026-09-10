# Experiment Queue: Mens Fashion Gadget

## Purpose

次にどの仮説を投稿/生成するかを管理する。
直近の投稿との重複を避けつつ、初期10投稿の探索を進める。

## Queue Rules

- 直近2投稿と同じ切り口を避ける。
- バッグの中身系を連投しない。
- 同じアイテムを連続使用しない。
- OPS-003 は OPS-002 metrics 確認まで保留。
- 初期10投稿は角度を分散させる。
- Experiment Control Principle: Observed Good Condition → Hold Constant Until Tested。良好だったRunの条件（CTA形式、画像有無、URL有無、ハッシュタグ構成、投稿構造、toneなど）は、検証対象でない限り可能な範囲で固定する。

## Queue Table

| queue_order | hypothesis_id | planned_run_id | content_angle | reason | avoid_overlap | planned_platform | planned_status | notes |
|-------------|---------------|----------------|---------------|--------|---------------|------------------|----------------|-------|
| 1 | H003 | OPS-005 | 爪・髪・香り | OPS-004 no_signal 後の角度分散。最優先 | バッグの中身・靴の手入れ系ではない | X | planned | 身だしなみケア軸。Target Tag固定 #40代ファッション、Content Angle Tag #爪髪香り（仮） |
| 2 | H009 | OPS-006 | 営業/経営者の第一印象 | ビジネス文脈での反応を検証するため | H003 とは異なる切り口 | X | planned | 仕事場印象軸 |
| 3 | H007 | OPS-007 | 若作りしないジャケット | ファッション寄りの反応を検証するため | H003/H009 とは異なる切り口 | X | planned | 服装選択軸 |
| 4 | H006 | OPS-008 | ワイヤレスイヤホン | ガジェット単体反応を検証するため | H007 とは異なる切り口 | X | planned | ガジェット軸 |
| 5 | H002 | OPS-009 | 靴の手入れ（画像あり） | text-only で弱かったため、画像ありで再検証の余地あり | H003/H009 から時間を空ける | X | planned | 画像あり・ビフォーアフター前提 |

## Notes

- キューは OPS-002 metrics 確認後に見直す。
- `planned_run_id` は仮の命名。実際の run_id は `new_run_folder.py` 生成時に決定。
- キューの順序は、分析結果によって変更可能。
- **2026-09-08 修正**: OPS-004（H002 靴の手入れ）は Distribution Learning Run。content_angle のみを変更し、OPS-002（impressions=137）との Distribution 比較を優先。評価指標は impression_ratio_vs_ops002 = OPS-004 impressions / 137 の生ratio。CTA形式・画像なし・URLなしは固定。ハッシュタグは OPS-002 と同じ2タグ構成（Target Tag `#40代ファッション` 固定 + Content Angle Tag `#靴の手入れ`）を維持。engagement は参考記録。現時点では success/weak/no_signal/higher/comparable/lower などの閾値分類を新規固定しない。複数 Distribution Learning Run 後に実測分布から導出。
- **2026-09-09 Phase 3-C 更新**: OPS-002 late measurement で impressions=149, engagement=0、result_label=no_signal。OPS-004（H002 靴の手入れ）を最優先、pivot 実施。OPS-003 は引き続き H001 overlap のため保留。
- **2026-09-10 Phase 3-D 更新**: OPS-004 late_24h_measurement で impressions=9, engagement=0、result_label=no_signal。impression_ratio_vs_ops002=0.0604。次回最優先は H003 爪・髪・香り、第二候補は H009 営業/経営者の第一印象。H002 は画像ありで再検証の余地あり。
