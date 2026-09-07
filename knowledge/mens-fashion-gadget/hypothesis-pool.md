# Hypothesis Pool: Mens Fashion Gadget

## Purpose

40代ファッション×ガジェットジャンルにおける投稿仮説を管理する。
仮説の優先度、状態、関連 run、リスクを一元的に把握する。

## Cold Start Rule

- 初期10投稿は探索期間。
- 1投稿だけで `signal_detected` や `no_signal` を確定させない。
- `winning-patterns.md` へ昇格するには、同系統を2〜3回試して再現性が必要。

## Status Definitions

| status | 意味 |
|--------|------|
| untested | 未検証 |
| testing | 検証中 |
| signal_detected | 強い兆候あり |
| weak_signal | 弱い兆候あり、再検証価値あり |
| no_signal | 反応なし、優先度を下げる |
| paused | 一時保留 |
| retired | 退役 |

## Hypothesis Table

| hypothesis_id | content_angle | target_reader | desired_reaction | expected_signal | risk | priority | status | related_runs | notes |
|---------------|---------------|---------------|------------------|-----------------|------|----------|--------|--------------|-------|
| H001 | バッグの中身 | 40代男性 / 経営者 / 営業職 | 自分もバッグの中身を整えたい / コメントしたい | replies / bookmarks | 投稿が似通いやすい | medium | testing | OPS-002, OPS-003 | OPS-002投稿済み、OPS-003は重複により保留 |
| H002 | 靴の手入れ | 40代男性 / 経営者 / 営業職 | 自分も靴を手入れしようと思う / 保存したい | bookmarks / replies | 説教臭くなる可能性 | high | untested | - | OPS-004候補 |
| H003 | 爪・髪・香り | 40代男性 / 経営者 / 営業職 | 身だしなみを見直したい / コメントしたい | replies / bookmarks | 清潔感訴求が上から目線になる可能性 | high | untested | - | OPS-004候補 |
| H004 | 薄型財布・キーケース | 40代男性 / 経営者 / 営業職 | 小物を買い替えたい / 保存したい | bookmarks / likes | H001と近く重複しやすい | medium | paused | OPS-002, OPS-003 | H001と近いため一時保留 |
| H005 | ガジェットポーチ・ケーブル整理 | 40代男性 / 経営者 / 営業職 | バッグの中を整理したい / 保存したい | bookmarks / replies | H001と近く重複しやすい | medium | paused | OPS-002, OPS-003 | H001と近いため一時保留 |
| H006 | ワイヤレスイヤホン | 40代男性 / 経営者 / 営業職 | 通勤・移動用ガジェットを見直したい | likes / bookmarks | ガジェット単体だと差別化が弱い | medium | untested | - | - |
| H007 | 若作りしないジャケット | 40代男性 / 経営者 / 営業職 | 服選びを見直したい / 保存したい | bookmarks / replies | ファッション助言が偉そうに見える可能性 | high | untested | - | - |
| H008 | 40代NGファッション | 40代男性 / 経営者 / 営業職 | 自分も気をつけようと思う / コメントしたい | impressions / replies | ネガティブ訴求が強くなりすぎる可能性 | medium | untested | - | - |
| H009 | 営業/経営者の第一印象 | 40代男性 / 経営者 / 営業職 | 仕事での見た目を整えたい / 保存したい | profile_clicks / follows / replies | ビジネス色が強すぎる可能性 | high | untested | - | - |
| H010 | 買ってよかった小物3選 | 40代男性 / 経営者 / 営業職 | 真似したい / 買いたい / 保存したい | bookmarks / likes | 実体験の捏造に注意 | medium | untested | - | 実際に使ったものに限定するのが望ましい |
