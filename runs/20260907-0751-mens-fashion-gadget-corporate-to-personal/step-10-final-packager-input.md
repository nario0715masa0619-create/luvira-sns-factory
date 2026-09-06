# Step 10: Final Packager Input

## Run Metadata

- run_id: `20260907-0751-mens-fashion-gadget-corporate-to-personal`
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
| 01 | 4 | 5 | 5 | 4 | 4 | 4 | 26 | ガジェット切り口は明確だが、やや限定的。 |
| 02 | 4 | 4 | 5 | 4 | 4 | 4 | 25 | 身だしなみテーマは共感しやすいが、抽象的。 |
| 03 | 5 | 5 | 5 | 5 | 5 | 5 | 30 | バランスが最も良い。感情フック+具体例+CTA。 |
| 04 | 4 | 5 | 5 | 4 | 4 | 4 | 26 | 若作りの対比が強いが、やや一般的。 |
| 05 | 4 | 4 | 5 | 4 | 4 | 4 | 25 | ストーリー性があるが、フックがやや弱い。 |

### 上位 5 本

1. **案 03**: 40代、バッグの中身を整えたら自信が出てきた。① 長財布から薄型財布へ ② 鍵はキーケースで静かに ③ ガジェットポーチでケーブルごちゃごちゃを防ぐ。中身が整うと、外見も整って見える。バッグの中身、何をこだわってる？
2. **案 01**: 40代、服を買う前にガジェット周りを整えたら印象変わった。① ケーブルはポーチに1つにまとめる ② 財布は薄型にしてポケットの膨らみを消す ③ スマホケースは汚れを落とす。高級品じゃなくても、身の回りが整ってるだけで清潔に見える。みんなの必須ガジェット小物、何かある？
3. **案 04**: 40代、小物と清潔感を整えるだけで若作りじゃなく見えるようになった。① イヤホンはワイヤレスに ② 財布は薄く ③ 靴は手入れ。高級品じゃなくても、整ってるかどうか。40代で整えてよかった小物、何？
4. **案 02**: 40代、服より先に手入れを整えた方が変わると気づいた。① 靴は週1回手入れ ② 爪は短く整える ③ 香りはボディソープと整髪料で統一。お金かけなくても、清潔感があれば十分。40代男性の身だしなみ、何から整えた？
5. **案 05**: 40代、服を買い足す前にやるべきこと。身の回りの小物と清潔感を整えるだけで、鏡を見るのが嫌じゃなくなった。特に効いたのは：① ガジェットポーチ ② 薄型財布 ③ 靴の手入れ。まずは買わずに整えてみる。みんなはどこから始めた？

### 最終おすすめ 1 本

**案 03**
40代、バッグの中身を整えたら自信が出てきた。

① 長財布から薄型財布へ
② 鍵はキーケースで静かに
③ ガジェットポーチでケーブルごちゃごちゃを防ぐ

中身が整うと、外見も整って見える。

バッグの中身、何をこだわってる？

**選定理由:**
- フックが感情訴求（自信）を含み、強い
- 具体例がバッグの中身という身近な切り口
- 3つのアイテムが明確で、保存・議論を誘発
- ブランド適合度が高く、商材訴求が過剰でない
- リスクが低く、炎上の可能性が少ない
- CTAが自然でリプライを誘発しやすい
- 「中身が整うと、外見も整って見える」という洞察が共感を呼ぶ

**予想される反応:**
- 「うちも長財布変えた」「キーケース必須」などの共感リプ
- 「おすすめの薄型財布教えて」などの質問リプ
- 「保存した」や「共有」などのエンゲージメント


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
