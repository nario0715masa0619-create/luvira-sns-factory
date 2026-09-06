# Step 09: Market Judge Input

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

## Risk Filter Review

### Candidate 01: 要件整理フォーカス

```
AI活用の短納期開発、失敗の8割は要件定義に起因してる気がする。

「MVPでやりたい」と言いながら、気づいたら本開発の機能がどんどん増えてる。

自分がやってる対策は3つ：
① 必須機能とnice-to-haveを分ける
② 承認ゲートを設ける
③ 仕様変更のルールを事前に決める

これだけで、後戻りがかなり減る。

みんなの現場では、どこでスコープが膨らむ？
```

| Risk Category | Level | Notes |
|---------------|-------|-------|
| Fabricated experience | low | Uses "気がする" and general observation. No specific false personal story. |
| Unsubstantiated claims | low | "8割" is qualified with "気がする". No absolute claims. |
| Effect guarantee | low | "後戻りがかなり減る" is directional, not guaranteed. |
| Fear-mongering | low | Problem is framed as common issue, not exaggerated threat. |
| Account type mismatch | low | Personal voice, reply/discussion CTA, matches account_type=personal. |
| CTA mismatch | low | CTA invites reply/discussion, matches desired_cta_style. |
| Product pushiness | low | Service is implied through expertise, not directly pitched. |
| Controversy risk | low | Neutral technical topic. |

**Overall: low risk. Pass.**

### Candidate 02: AIレビューフォーカス

```
AIにコードを書かせて、人間が承認する。
この分担、理想は理想だけど現実は厳しい。

理由は単純で、AIの出力が正しいか判断する基準が人間側にないと、結局全部見直すことになる。

自分は「AIが下書き → 人間が要件と意図を確認 → 承認」って流れにしてる。

確認ポイントは主に3つ：
① セキュリティ
② 可読性
③ テスト観点

他にチェックしてる項目あったら教えて。
```

| Risk Category | Level | Notes |
|---------------|-------|-------|
| Fabricated experience | low | Personal workflow described in general terms. |
| Unsubstantiated claims | low | "理想は理想" is balanced. |
| Effect guarantee | low | No guarantee stated. |
| Fear-mongering | low | Reasonable caution. |
| Account type mismatch | low | Personal voice. |
| CTA mismatch | low | Reply/discussion CTA. |
| Product pushiness | low | No direct service pitch. |
| Controversy risk | low | Technical topic. |

**Overall: low risk. Pass.**

### Candidate 03: MVP定義フォーカス

```
「まずMVPで」って言って始めたのに、気づいたら本開発化してる案件、多くない？

自分も何度かあって、原因はだいたい「MVPの定義が曖昧」なこと。

MVPは「テストしたい仮説を検証する最小限の機能」じゃないと、後から機能が増え続ける。

AIを使う時は特に、生成速度が速い分、方向性がずれるリスクも高い。

だから最初に「何を検証したいか」を紙1枚で固めるようになった。

MVPの定義、みんなどうしてる？
```

| Risk Category | Level | Notes |
|---------------|-------|-------|
| Fabricated experience | low | "自分も何度かあって" is vague but acceptable as personal reflection. |
| Unsubstantiated claims | low | Definition of MVP is standard. |
| Effect guarantee | low | No guarantee. |
| Fear-mongering | low | Common caution. |
| Account type mismatch | low | Personal voice. |
| CTA mismatch | low | Reply/discussion CTA. |
| Product pushiness | low | No direct pitch. |
| Controversy risk | low | Standard topic. |

**Overall: low risk. Pass.**

### Candidate 04: 技術負債フォーカス

```
短納期でAIにコードをガンガン書かせると、後で技術負債が増えるって話。

自分も「とりあえず動けばいい」で進めた案件で、3ヶ月後に苦しんだことがある。

今は短納期でも3つのことを徹底してる：
① レビュー基準を事前に決める
② テスト方針をMVP段階から入れる
③ リファクタリングの工数を見積もる

速さと品質、両立させるのは難しいけど、無理のない線引きができると楽になる。

短納期開発での品質担保、どうしてる？
```

| Risk Category | Level | Notes |
|---------------|-------|-------|
| Fabricated experience | medium | "3ヶ月後に苦しんだことがある" implies specific experience without details. Acceptable if kept vague. |
| Unsubstantiated claims | low | No absolute claims. |
| Effect guarantee | low | No guarantee. |
| Fear-mongering | low | Reasonable caution. |
| Account type mismatch | low | Personal voice. |
| CTA mismatch | low | Reply/discussion CTA. |
| Product pushiness | low | No direct pitch. |
| Controversy risk | low | Technical topic. |

**Overall: low risk. Pass with note: keep the anecdote vague.**

### Candidate 05: 仕様変更フォーカス

```
システム開発で「仕様は決まってる」と言われると、大概どこかで変更が入る。

AIを使った短納期開発だと、変更に対応する速度は速いけど、方向性がブレやすい。

自分がやってるのは、変更が来た時に必ず3つを確認すること：
① なぜ変更が必要か
② MVPの範囲に影響するか
③ 他の機能に波及しないか

これをAIに整理させて、人間が最終判断する。

仕様変更への対応、みんなのベストプラクティスがあれば聞きたい。
```

| Risk Category | Level | Notes |
|---------------|-------|-------|
| Fabricated experience | low | General workflow description. |
| Unsubstantiated claims | low | No absolute claims. |
| Effect guarantee | low | No guarantee. |
| Fear-mongering | low | Reasonable observation. |
| Account type mismatch | low | Personal voice. |
| CTA mismatch | low | Reply/discussion CTA. |
| Product pushiness | low | Service implied through workflow. |
| Controversy risk | low | Technical topic. |

**Overall: low risk. Pass.**

### Summary

All 5 candidates pass risk filter.
- Lowest risk: Candidate 01, 03, 05
- Slightly higher but acceptable: Candidate 02, 04

Recommended for final selection: Candidate 01 (要件整理フォーカス) due to strongest balance of low risk, broad appeal, and clear personal account fit.


## Prompt To Apply

Apply the following prompt to the Source Input above.

## Role

Market Judge（市場判定 AI）

## Objective

Risk Filter 通過後の候補を採点し、上位 5 本と最終おすすめ 1 本を選ぶ。

## Inputs

- リスク通過後の候補群
- 元構造分析
- 感情分類
- クライアントコンテキスト
- `account_type`: 投稿先アカウントの種別（`personal` / `corporate`）
- `desired_cta_style`: 希望 CTA スタイル
- 評価基準（インプレッション予測、ブランド適合度、パクリ感、共感度、`account_type` 適合性等）

## Process

1. `account_type` が未指定の場合は採点を行わず、人間に確認を求める。
2. 各候補を以下の観点で採点する：
   - インプレッション予測（1-5）
   - ブランド適合度（1-5）
   - パクリ感の少なさ（1-5）
   - 共感度（1-5）
   - フック力（1-5）
   - `account_type` 適合性（1-5）
3. `account_type` に応じた重み付けを行う。
   - `personal`: 共感・本音・リプ誘発・体験共有を加点要素とする。
   - `corporate`: 保存・信頼・問い合わせ導線・ノウハウ性を加点要素とする。
4. `account_type` と明らかに不一致な案は上位候補から除外する。
5. 合計点で上位 5 本を選ぶ。
6. 上位 5 本の中から最終おすすめ 1 本を選ぶ。
7. 各案の採点理由を簡潔に述べる。

## Output Format

```markdown
## 市場判定結果

### account_type
- account_type: [personal / corporate]
- desired_cta_style: [reply / experience_sharing / discussion / consultation / document_request / checklist]

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
| 01 | 4 | 5 | 5 | 4 | 4 | 5 | 27 | ... |
| 02 | ... | ... | ... | ... | ... | ... | ... | ... |

### 上位 5 本
1. 案 [No]: [本文]
2. 案 [No]: [本文]
3. 案 [No]: [本文]
4. 案 [No]: [本文]
5. 案 [No]: [本文]

### 最終おすすめ 1 本
**案 [No]**
[本文]

**選定理由:**
[理由を 3 行以内]
```

## Do Not

- 自分の好みだけで選ばない。
- 根拠なき高評価をしない。
- リスク medium 以上の案を選ばない。
- ブランド適合度が低い案を最終おすすめにしない。
- `account_type` に合わない案を最終おすすめにしない。
- `account_type` 未指定のまま採点を進めない。

## Quality Criteria

- [ ] 各案に数値スコアが付いている
- [ ] 上位 5 本が明確
- [ ] 最終おすすめに理由がある
- [ ] ブランド適合度を重視している
- [ ] リスク通過案のみを対象としている
- [ ] `account_type` 適合性が評価されている


## Execution Instruction

1. Copy the entire content of this file (`step-09-market-judge-input.md`).
2. Paste it into Kimi/OpenCode as a new request.
3. Save the AI response to `step-09-market-judge.md` in the same run folder.
4. Review the output before proceeding to the next step.

> **Important:** This is a manual step. The script does not execute prompts, call APIs, or post automatically.
