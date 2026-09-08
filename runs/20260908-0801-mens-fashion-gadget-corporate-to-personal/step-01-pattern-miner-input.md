# Step 01: Pattern Miner Input

## Run Metadata

- run_id: `20260908-0801-mens-fashion-gadget-corporate-to-personal`
- product_service: `40代男性向けファッション・ガジェット情報発信`
- product_slug: `mens-fashion-gadget`
- source_account_type: `corporate`
- account_type: `personal`
- desired_cta_style: `reply / discussion / experience_sharing`
- allowed_persona_expression: `僕 / 私 / 自分 / 主語省略`
- risk_tolerance: `balanced`
- target_platform: `X`
- target_audience: `40代男性 / 経営者 / 営業職 / 見た目と仕事道具を整えたい人`
- business_goal: `40代男性向けファッション×ガジェット投稿の反応獲得`
- model: `kimi-k2.7-code`
- execution_mode: `file_based_semi_automation`
- status: `draft`
- current_step: `-`

## Source Input

The following sections are extracted from `input.md`. They contain the source post summary and the instructions for Step 01.

## Source Post Structure Summary

- hook_type: `「40代になって気づいた」型フック`
- structure_summary: `フック（40代になって、高い靴よりちゃんと手入れしてる靴が大事だと気づいた） → テーマ提示（靴の手入れは週1回の小さな習慣） → 3つの具体的手入れ例（ブラシ・クリーム・乾拭き） → 価値転換（高級靴じゃなくても清潔感があれば十分） → CTA（共感・経験共有型の問いかけ）`
- main_sections: `フック / テーマ / 3つの手入れ例 / 価値転換 / CTA`
- cta_type: `reply / discussion / experience_sharing`

## Source Post Emotion Summary

- primary_emotion: `共感`
- secondary_emotions: `安心, 発見, 自己効力感`
- engagement_driver: `「お金をかけなくても、手入れするだけで印象が変わる」という安価で実行可能な改善の発見`
- reaction_design: `「自分もやってる」「同じこと思ってた」という共感リプライや経験共有を誘発する`

## Step 01 Input for Pattern Miner

### Source Post Reference

> **Reminder:** Store only structure, emotion, and reaction design. Do not paste full text of real posts.

- source_account_type: `corporate`
- account_type: `personal`
- product_service: `40代男性向けファッション・ガジェット情報発信`
- source_post_structure_summary: `フック（40代になって、高い靴よりちゃんと手入れしてる靴が大事だと気づいた） → テーマ提示（靴の手入れは週1回の小さな習慣） → 3つの具体的手入れ例（ブラシ・クリーム・乾拭き） → 価値転換（高級靴じゃなくても清潔感があれば十分） → CTA（共感・経験共有型の問いかけ）`
- source_post_emotion_summary: `共感・安心・発見・自己効力感。お金をかけなくても手入れするだけで印象が変わる、安価で実行可能な改善の発見。`
- target_audience: `40代男性 / 経営者 / 営業職 / 見た目と仕事道具を整えたい人`
- business_goal: `40代男性向けファッション×ガジェット投稿の反応獲得`

### Instructions for Pattern Miner

Please analyze the source post structure and emotion drivers, then produce output in the standard Phase 1 format:

1. Structure pattern
2. Emotion drivers
3. Reusable framework
4. Product-specific notes
5. Risk notes

Ensure `source_account_type` and `account_type` are clearly stated.

---

## Prompt To Apply

Apply the following prompt to the Source Input above.

## Role

Pattern Miner（構造抽出 AI）

## Objective

与えられたバズ投稿から、文言ではなく「構造」と「反応設計」を抽出する。

## Inputs

- 元バズ投稿（全文）
- 出典プラットフォーム（X, Instagram, Threads 等）
- 業種・ジャンル
- `source_account_type`: 元投稿アカウントの種別（`personal` / `corporate`）
- `account_type`: 転用先アカウントの種別（`personal` / `corporate`）

## Process

1. 投稿をセクションに分割する（導入・展開・結論・CTA 等）。
2. 各セクションが何をしているかを 1 行で説明する。
3. 情報の配置順序を整理する。
4. 読者の反応を誘発している箇所を特定する。
5. 使用されている技法（問いかけ、対比、列挙、具体例、意外性、共感等）をリストアップする。
6. `source_account_type` に基づき、元投稿の構造が個人発信か法人発信かを判定する。
7. `source_account_type` と `account_type` が異なる場合、転用時に調整が必要な箇所を明示する。
8. `account_type` に適した構造要素（personal なら本音・体験談、corporate なら客観性・信頼性）を重点的に抽出する。

## Output Format

```markdown
## 構造分析

### 元投稿概要
- プラットフォーム:
- 業種/ジャンル:
- source_account_type:
- account_type:
- 推定文字数:

### アカウント種別判定
- source_account_type: [personal / corporate / 不明]
- 判定理由: [3 行以内]
- account_type との差異: [差異があれば記載。なければ「なし」]
- 転用時の調整ポイント: [差異があれば記載]

### セクション分け
1. [セクション名]: [役割を 1 行で]
2. [セクション名]: [役割を 1 行で]
3. ...

### 情報配置の順序
1. ...
2. ...

### 反応設計
- [反応の種類]: [どのセクションで、どう誘発しているか]

### 使用技法
- [技法名]: [どこで使われているか]

### 構造の要約
[3 行以内で構造を要約]
```

## Do Not

- 元投稿の文章をそのままコピーしない。
- 元投稿にない情報を推測で追加しない。
- 感想や評価を入れない。
- クライアント情報をここでは扱わない。
- `account_type` 未指定のまま分析を進めない。

## Quality Criteria

- [ ] セクション分けが論理的である
- [ ] 各セクションの役割が明確である
- [ ] 反応設計が具体的に特定されている
- [ ] 元投稿の文言を含めていない
- [ ] 客観的に構造を記述している
- [ ] `source_account_type` と `account_type` の整合性が確認されている


## Execution Instruction

1. Copy the entire content of this file (`step-01-pattern-miner-input.md`).
2. Paste it into Kimi/OpenCode as a new request.
3. Save the AI response to `step-01-pattern-miner.md` in the same run folder.
4. Review the output before proceeding to the next step.

> **Important:** This is a manual step. The script does not execute prompts, call APIs, or post automatically.
