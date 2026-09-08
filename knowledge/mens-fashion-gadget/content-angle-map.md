# Content Angle Map: Mens Fashion Gadget

## Purpose

40代ファッション×ガジェットジャンルにおける content_angle の分布と反応傾向を可視化する。

## Current Status

Cold Start 中のため、反応データは限定的。OPS-002 のみ late measurement であり、1投稿だけの結果。

## Content Angle Categories

```text
40代ファッション×ガジェット
├── 持ち物・EDC
│   ├── H001 バッグの中身 (no_signal)
│   ├── H004 薄型財布・キーケース (paused)
│   └── H005 ガジェットポーチ・ケーブル整理 (paused)
├── 身だしなみ・ケア
│   ├── H002 靴の手入れ (untested)
│   └── H003 爪・髪・香り (untested)
├── 服装
│   ├── H007 若作りしないジャケット (untested)
│   └── H008 40代NGファッション (untested)
├── ガジェット
│   └── H006 ワイヤレスイヤホン (untested)
└── 仕事・ビジネス
    └── H009 営業/経営者の第一印象 (untested)

その他:
└── H010 買ってよかった小物3選 (untested)
```

## Reaction Map

| content_angle | result_label | strongest_signal | weakest_signal | notes |
|---------------|--------------|------------------|----------------|-------|
| バッグの中身 | no_signal | impressions_only（late_measurement 149） | no_engagement（0） | 1投稿のみ。H001はrejectせず、即座の再投稿は避ける。画像あり・より具体的な実物感で再検証余地あり |
| 靴の手入れ | pending | unknown | unknown | OPS-004 予定。Distribution Learning Run。OPS-002（impressions=149 late_measurement）との生ratioで評価。CTA形式・画像なし・URLなし・ハッシュタグ2タグ構成はOPS-002と同一 |

## Update Rules

- 各 run の分析後に result_label を更新。
- 同カテゴリ内で複数 run が出揃ってから傾向を判断。
- 人間承認後に更新する。
