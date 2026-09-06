# Step 10: Final Packager Input

## Run Metadata

- run_id: `20260906-1848-system-dev-corporate-to-personal`
- product_service: `AI活用型短納期システム開発`
- product_slug: `system-dev`
- source_account_type: `corporate`
- account_type: `personal`
- desired_cta_style: `reply / discussion / experience_sharing`
- allowed_persona_expression: `僕 / 私 / 自分 / 主語省略`
- risk_tolerance: `balanced`
- target_platform: `X`
- target_audience: `中小企業経営者 / 事業責任者 / システム開発を検討している担当者`
- business_goal: `AI活用型短納期システム開発への関心獲得`
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
| 01 | 4 | 5 | 5 | 5 | 5 | 5 | 29 | 最もバランスが取れている。個人アカウントに最適。 |
| 02 | 3 | 4 | 5 | 3 | 3 | 4 | 22 | 専門性は高いが、対象層が狭い。 |
| 03 | 4 | 4 | 5 | 4 | 4 | 4 | 25 | 議論を誘発しやすいが、やや抽象的。 |
| 04 | 3 | 4 | 5 | 4 | 3 | 4 | 23 | 痛みを共有できるが、重め。 |
| 05 | 3 | 4 | 5 | 3 | 3 | 4 | 22 | 実務感はあるが、共感の幅が限定的。 |

### 上位 5 本

1. 案 01: AI活用の短納期開発、失敗の8割は要件定義に起因してる気がする。「MVPでやりたい」と言いながら、気づいたら本開発の機能がどんどん増えてる。自分がやってる対策は3つ：① 必須機能とnice-to-haveを分ける ② 承認ゲートを設ける ③ 仕様変更のルールを事前に決める。これだけで、後戻りがかなり減る。みんなの現場では、どこでスコープが膨らむ？
2. 案 03: 「まずMVPで」って言って始めたのに、気づいたら本開発化してる案件、多くない？自分も何度かあって、原因はだいたい「MVPの定義が曖昧」なこと。MVPは「テストしたい仮説を検証する最小限の機能」じゃないと、後から機能が増え続ける。AIを使う時は特に、生成速度が速い分、方向性がずれるリスクも高い。だから最初に「何を検証したいか」を紙1枚で固めるようになった。MVPの定義、みんなどうしてる？
3. 案 04: 短納期でAIにコードをガンガン書かせると、後で技術負債が増えるって話。自分も「とりあえず動けばいい」で進めた案件で、3ヶ月後に苦しんだことがある。今は短納期でも3つのことを徹底してる：① レビュー基準を事前に決める ② テスト方針をMVP段階から入れる ③ リファクタリングの工数を見積もる。速さと品質、両立させるのは難しいけど、無理のない線引きができると楽になる。短納期開発での品質担保、どうしてる？
4. 案 02: AIにコードを書かせて、人間が承認する。この分担、理想は理想だけど現実は厳しい。理由は単純で、AIの出力が正しいか判断する基準が人間側にないと、結局全部見直すことになる。自分は「AIが下書き → 人間が要件と意図を確認 → 承認」って流れにしてる。確認ポイントは主に3つ：① セキュリティ ② 可読性 ③ テスト観点。他にチェックしてる項目あったら教えて。
5. 案 05: システム開発で「仕様は決まってる」と言われると、大概どこかで変更が入る。AIを使った短納期開発だと、変更に対応する速度は速いけど、方向性がブレやすい。自分がやってるのは、変更が来た時に必ず3つを確認すること：① なぜ変更が必要か ② MVPの範囲に影響するか ③ 他の機能に波及しないか。これをAIに整理させて、人間が最終判断する。仕様変更への対応、みんなのベストプラクティスがあれば聞きたい。

### 最終おすすめ 1 本

**案 01**
AI活用の短納期開発、失敗の8割は要件定義に起因してる気がする。「MVPでやりたい」と言いながら、気づいたら本開発の機能がどんどん増えてる。自分がやってる対策は3つ：① 必須機能とnice-to-haveを分ける ② 承認ゲートを設ける ③ 仕様変更のルールを事前に決める。これだけで、後戻りがかなり減る。みんなの現場では、どこでスコープが膨らむ？

**選定理由:**
- フック力と共感度が両立している
- 個人アカウントに最適な「自分の現場」感がある
- 3つの対策が具体的で保存・議論を誘発
- ブランド適合度が高く、商材訴求が過剰でない
- リスクが低く、炎上の可能性が少ない
- CTAが自然でリプライを誘発しやすい


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
