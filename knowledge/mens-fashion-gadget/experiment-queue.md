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
| 1 | H002 | OPS-004 | 靴の手入れ | OPS-002 no_signal 後の角度分散。最優先 | バッグの中身系ではない | X | planned | 清潔感・手入れ軸。Target Tag固定 #40代ファッション、Content Angle Tag #靴の手入れ |
| 2 | H003 | OPS-005 | 爪・髪・香り | 清潔感軸を検証するため | H002 とは異なる切り口 | X | planned | 身だしなみケア軸 |
| 3 | H007 | OPS-006 | 若作りしないジャケット | ファッション寄りの反応を検証するため | H002/H003 とは異なる切り口 | X | planned | 服装選択軸 |
| 4 | H009 | OPS-007 | 営業/経営者の第一印象 | ビジネス属性との相性を見るため | H007 とは異なる切り口 | X | planned | 仕事場印象軸 |
| 5 | H006 | OPS-008 | ワイヤレスイヤホン | ガジェット単体反応を検証するため | H009 とは異なる切り口 | X | planned | ガジェット軸 |

## Notes

- キューは OPS-002 metrics 確認後に見直す。
- `planned_run_id` は仮の命名。実際の run_id は `new_run_folder.py` 生成時に決定。
- キューの順序は、分析結果によって変更可能。
- **2026-09-08 修正**: OPS-004（H002 靴の手入れ）は Distribution Learning Run。content_angle のみを変更し、OPS-002（impressions=137）との Distribution 比較を優先。評価指標は impression_ratio_vs_ops002 = OPS-004 impressions / 137 の生ratio。CTA形式・画像なし・URLなしは固定。ハッシュタグは OPS-002 と同じ2タグ構成（Target Tag `#40代ファッション` 固定 + Content Angle Tag `#靴の手入れ`）を維持。engagement は参考記録。現時点では success/weak/no_signal/higher/comparable/lower などの閾値分類を新規固定しない。複数 Distribution Learning Run 後に実測分布から導出。
- **2026-09-09 Phase 3-C 更新**: OPS-002 late measurement で impressions=149, engagement=0、result_label=no_signal。OPS-004（H002 靴の手入れ）を最優先、pivot 実施。OPS-003 は引き続き H001 overlap のため保留。
