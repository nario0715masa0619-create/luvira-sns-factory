# Step 10: Final Packager Input

## Run Metadata

- run_id: `20260906-2132-mens-fashion-gadget-corporate-to-personal`
- product_service: `40代男性向けファッション・ガジェット情報発信`
- product_slug: `mens-fashion-gadget`
- source_account_type: `corporate`
- account_type: `personal`
- desired_cta_style: `reply / discussion / experience_sharing`
- allowed_persona_expression: `僕 / 私 / 自分 / 主語省略`
- risk_tolerance: `balanced`
- target_platform: `X`
- target_audience: `40代男性 / 経営者 / 個人事業主 / 営業職 / 見た目と仕事道具を整えたい人`
- business_goal: `40代男性向けファッション×ガジェット投稿の反応獲得`
- model: `kimi-k2.7-code`
- execution_mode: `file_based_semi_automation`
- status: `draft`
- current_step: `-`

## Source Input

The following content is the output from the previous step. Use it as the primary input for the next step.

## 市場判定結果

### account_type

- account_type: personal
- desired_cta_style: reply / discussion / experience_sharing

### 採点基準

| 項目 | 満点 |
|------|------|
| インプレッション予測 | 5 |
| ブランド適合度 | 5 |
| パクリ感の少なさ | 5 |
| 共感度 | 5 |
| フック力 | 5 |
| account_type 適合性 | 5 |

### 各候補の採点

| 案 No | インプ | ブランド | パクリ感 | 共感 | フック | account_type | 合計 | 備考 |
|-------|--------|----------|----------|------|--------|--------------|------|------|
| 01 | 5 | 5 | 5 | 5 | 5 | 5 | 30 | 最もバランスが取れている。保存・返信両方期待できる。 |
| 02 | 4 | 4 | 5 | 4 | 4 | 4 | 25 | 議論を誘発しやすいが、やや抽象的。 |
| 03 | 4 | 4 | 5 | 4 | 4 | 4 | 25 | 親近感があるが、ターゲット層がやや限定される。 |
| 04 | 3 | 4 | 5 | 3 | 3 | 3 | 21 | 仕事色が強く、個人アカウント感が弱い。 |
| 05 | 4 | 4 | 5 | 4 | 4 | 4 | 25 | 感情訴求が強いが、やや重め。 |

### 上位 5 本

1. 案 01: 40代男性のバッグの中身、見直すと仕事の印象変わる。自分が最近整えた3つ：① 薄型長財布（膨らまない） ② ガジェットポーチ（ケーブルごちゃごちゃ防止） ③ ワイヤレスイヤホン（安いのを良品に）。高級品じゃなくても、清潔にまとまってるだけで自信が違う。みんなのバッグの中身、何が必須？
2. 案 02: 40代、ファッションより「清潔感」が大事だと気づいた。最近やってるのは3つ：① ジャケットは肩幅を意識する ② 靴は週1回手入れ ③ 香りを統一（整髪料＋ボディソープ）。若作りじゃなく、整って見えるだけで全然違う。40代男性の清潔感、何が大事だと思う？
3. 案 03: 40代になって買ってよかった小物、3つ。① 名刺入れ（昔の札入れ式から変えた） ② 革のキーケース（ポケットの膨らみ解消） ③ 小さめのモバイルバッテリー（重いのは持ち歩かない）。どれも高級品じゃないけど、使うたびに「整ってるな」と思える。40代の小物、何を変えたら生活変わった？
4. 案 05: 40代になって、「もう若くないから」って諦めてた。でも、ジャケット1着と靴1足を変えただけで、鏡を見るのが嫌じゃなくなった。大事なのは高級品じゃなくて、サイズ感と手入れ。年齢を重ねてからのファッション、無理なくできる範囲でいい。40代男性に似合うと思うアイテム、何かある？
5. 案 04: 営業回りが多くなって、仕事道具の見た目を気にするようになった。バッグの中身を整えたら、なぜか商談もスムーズになった気がする。特に効いたのは3つ：① 名刺入れ ② シンプルな手帳 ③ ガジェットポーチ。中身が整うと、頭も整う。仕事で気をつけてる身だしなみ、ある？

### 最終おすすめ 1 本

**案 01**
40代男性のバッグの中身、見直すと仕事の印象変わる。自分が最近整えた3つ：① 薄型長財布（膨らまない） ② ガジェットポーチ（ケーブルごちゃごちゃ防止） ③ ワイヤレスイヤホン（安いのを良品に）。高級品じゃなくても、清潔にまとまってるだけで自信が違う。みんなのバッグの中身、何が必須？

**選定理由:**
- フック力と共感度が両立している
- 個人アカウントに最適な「自分の体験」感
- 3つのアイテムが具体的で保存・議論を誘発
- ブランド適合度が高く、商材訴求が過剰でない
- リスクが低く、炎上の可能性が少ない
- CTAが自然でリプライを誘発しやすい
- 「高級品じゃなくても」という謙虚さが40代男性に刺さる


## Prompt To Apply

Apply the following prompt to the Source Input above.

## Role

Final Packager（最終整備 AI）

## Objective

Market Judge が選定した上位 5 本と最終おすすめ 1 本を、人間が確認しやすい形に整える。

## Inputs

- Market Judge の上位 5 本 + 最終おすすめ 1 本
- Pattern Miner の構造分析
- Emotion Mapper の感情分類
- Similarity Guard / Risk Filter のコメント
- クライアントコンテキスト
- `account_type`: 投稿先アカウントの種別（`personal` / `corporate`）
- `source_account_type`: 元投稿アカウントの種別（`personal` / `corporate`）
- `allowed_persona_expression`: 許可される一人称表現
- `desired_cta_style`: 希望 CTA スタイル

## Process

1. `account_type` が未指定の場合は最終パッケージを作成せず、人間に確認を求める。
2. 最終提案書のテンプレートに情報を埋める。
3. `account_type` を最終パッケージに明記する。
4. `personal` / `corporate` 別の投稿可否コメントを出す。
5. 各案の背景（構造・感情・リスク）を簡潔に説明する。
6. 人間承認用のチェック欄を作成する。
7. `account_type` に合った最終目視確認項目を追加する。
8. 投稿手順メモを作成する。
9. 必要に応じて、ハッシュタグや画像の有無を記載する。

## Output Format

```markdown
# SNS 投稿提案書

## クライアント情報
- account_type:
- source_account_type:
- 業種:
- 商材:
- ターゲット:
- 投稿目的:
- 口調:
- 文字数条件:
- ハッシュタグ方針:
- allowed_persona_expression:
- desired_cta_style:

## 元バズ投稿の構造（参考）
- 出典プラットフォーム:
- source_account_type:
- account_type:
- 構造の要約:
- 主要感情ドライバー:

## account_type 別投稿可否コメント
- account_type: [personal / corporate]
- 適合した点: [3 行以内]
- 注意点: [3 行以内]

## 上位 5 本

### 案 1（推奨順位: 1）
[本文]

**選定理由:**
[理由]

**リスクコメント:**
[リスクフィルタからのコメント]

### 案 2（推奨順位: 2）
...

## 最終おすすめ 1 本

### 案 [No]
[本文]

**採用理由:**
[理由]

**予想される反応:**
[反応予測]

## 人間承認チェック欄

- [ ] ブランド適合度に問題がない
- [ ] 事実誤認・誇大広告がない
- [ ] 元投稿に酷似していない
- [ ] 炎上リスクがない
- [ ] `account_type` に適した文体・CTA・一人称になっている
- [ ] `source_account_type` からの転用調整が適切である
- [ ] 投稿日時・画像・ハッシュタグを確認した
- [ ] 最終承認

## 投稿手順メモ
1. 上記「最終おすすめ 1 本」をコピーする。
2. 必要に応じて画像を添付する。
3. ハッシュタグを 2 つ以内で追加する。
4. 投稿前に最終目視確認を行う。
5. 投稿時刻を記録する。
6. 24 時間後にインプレッション数を記録する。

## 注意事項
- 本提案はあくまで候補です。必ず人間が最終判断してください。
- 自動投稿は行わないでください。
```

## Do Not

- 自動投稿を前提にした出力を作らない。
- 人間が判断するための情報を欠落させない。
- リスクコメントを省略しない。
- 元バズ投稿の文章を提案書にそのまま含めない。
- `account_type` 未指定のまま最終パッケージを作成しない。

## Quality Criteria

- [ ] 人間が承認しやすい形式になっている
- [ ] 各案の選定理由が明確
- [ ] リスクコメントが含まれている
- [ ] 承認チェック欄がある
- [ ] 投稿手順メモがある
- [ ] 自動投稿を促唆していない
- [ ] `account_type` が明記されている
- [ ] `account_type` に合った確認コメントが出ている


## Execution Instruction

1. Copy the entire content of this file (`step-10-final-packager-input.md`).
2. Paste it into Kimi/OpenCode as a new request.
3. Save the AI response to `step-10-final-packager.md` in the same run folder.
4. Review the output before proceeding to the next step.

> **Important:** This is a manual step. The script does not execute prompts, call APIs, or post automatically.
