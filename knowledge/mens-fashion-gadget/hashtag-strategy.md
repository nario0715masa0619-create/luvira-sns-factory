# Hashtag Strategy: Mens Fashion Gadget

## Purpose

40代ファッション×ガジェットジャンルにおける、Luvira SNS Factory の投稿ハッシュタグの Canonical Rule。

本ファイルは、次回以降の run 生成時に AI が必ず参照するルールである。

## Basic Structure

2タグ構成とする。

```text
[Target Tag] [Content Angle Tag]
```

### Target Tag

- `#40代ファッション`
- Distribution Learning Phase 中は原則固定。
- 将来、専用の Hashtag Experiment で変更・削除の効果を検証してから変更可能。

### Content Angle Tag

- content_angle / hypothesis に対応するタグを1つ選択する。
- 各 content_angle ごとに決定済みのタグを使用する。

## Tag Mapping by Content Angle

| content_angle | Content Angle Tag |
|---------------|-------------------|
| バッグの中身 | `#バッグの中身` |
| 靴の手入れ | `#靴の手入れ` |
| 爪・髪・香り | （未決定：実施時に決定） |
| 薄型財布・キーケース | （未決定：実施時に決定） |
| ガジェットポーチ・ケーブル整理 | （未決定：実施時に決定） |
| ワイヤレスイヤホン | （未決定：実施時に決定） |
| 若作りしないジャケット | （未決定：実施時に決定） |
| 40代のNGファッション | （未決定：実施時に決定） |
| 営業/経営者の第一印象 | （未決定：実施時に決定） |
| 買ってよかった小物3選 | （未決定：実施時に決定） |

## Example

### OPS-002

```text
#40代ファッション #バッグの中身
```

### OPS-004

```text
#40代ファッション #靴の手入れ
```

## Placement

- 本文末尾に半角スペース区切りで配置する。
- 例：

```text
みんなの靴の手入れ、何が必須？

#40代ファッション #靴の手入れ
```

## Rules

1. **Target Tag は固定**: Distribution Learning Phase 中は `#40代ファッション` を変更しない。
2. **Content Angle Tag のみ変更**: content_angle に対応するタグを1つ使用する。
3. **2タグ構成を維持**: 3つ以上のハッシュタグを追加しない。
4. **独自判断で変更しない**: 推測でタグを追加・削除・変更しない。
5. **Hashtag効果を因果関係として解釈しない**: 良好だったRunのタグ構成が原因で良かったと断定しない。あくまで「そのRunの実行条件の一部」として固定する。
6. **Hashtag効果は専用Experimentで検証**: 将来、Target Tag や Content Angle Tag、タグ数、タグ配置の効果は専用の Hashtag Experiment で検証する。

## Experiment Control Principle

> Observed Good Condition ≠ Proven Causal Factor
> Observed Good Condition → Hold Constant Until Tested

OPS-002 で `#40代ファッション` `#バッグの中身` の2タグ構成が使用され、137 impressions を獲得した。
しかし、この結果から「2タグ構成が有効」「#40代ファッション が効いた」「#バッグの中身 が伸ばした」とは断定しない。

現時点で正しく言えるのは、

> 「137 impressionsを獲得したOPS-002の実行条件の一部だった」

ということだけである。

したがって、Distribution Learning Run では、

- Target Tag `#40代ファッション` は固定
- Content Angle Tag は content_angle に対応するタグに変更
- その他の条件（画像なし、URLなし、CTA形式、投稿構造など）も可能な範囲で固定

として、content_angle の影響を測定する。

## Related Documents

- `docs/phase-3-a-cold-start-pdca-execution-design.md` - Cold Start PDCA と Anti-Overfitting Rules
- `knowledge/mens-fashion-gadget/experiment-queue.md` - 次回 run の予定
- `knowledge/mens-fashion-gadget/content-angle-map.md` - 各 content_angle の反応分布
- `knowledge/mens-fashion-gadget/experiment-log.md` - 実験結果の記録

## Update Rules

- 新しい content_angle を追加する際は、対応する Content Angle Tag を本ファイルに追記する。
- Hashtag Experiment の結果は本ファイルの「Experiment Control Principle」セクションに追記し、次のルール改訂に反映する。
- 単独Runの結果から本ファイルの基本構造を変更しない。
