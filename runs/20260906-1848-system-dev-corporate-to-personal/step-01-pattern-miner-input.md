# Step 01: Pattern Miner Input

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

The following sections are extracted from `input.md`. They contain the source post summary and the instructions for Step 01.

## Source Post Structure Summary

- hook_type: `業界共通の落とし穴を指摘する問いかけ`
- structure_summary: `法人投稿風の「課題提起 → よくある見落とし → 確認項目 → 解決の方向性 → 資料請求CTA」。専門用語を適度に使いつつ、最後は自社サービスへの誘導で締める。`
- main_sections: `1. フック：業界の共通課題を数字や事例で提示 / 2. 問題：なぜその課題が起きるかを構造化 / 3. チェックリスト：読者がすぐ使える確認項目 / 4. 解決方向性：専門的なアプローチを提示 / 5. CTA：資料請求や相談への誘導`
- cta_type: `資料請求 / 相談予約（コーポレートアカウント向け）`

## Source Post Emotion Summary

- primary_emotion: `不安の共有と安心への導線`
- secondary_emotions: `共感（同じ失敗をした人）、発見（新しい視点）、信頼（専門性への期待）`
- engagement_driver: `「これ自分もやりそう」「このチェックリスト役立つかも」という実用感と、専門家からのアドバイスをもらっている感覚`
- reaction_design: `課題提示で「わかる」と共感させ、チェックリストで「保存したい」と思わせ、解決方向性で「この人に相談したい」と思わせる設計`

## Step 01 Input for Pattern Miner

### Source Post Reference

> **Reminder:** Store only structure, emotion, and reaction design. Do not paste full text of real posts.

- source_account_type: `corporate`
- account_type: `personal`
- product_service: `PRODUCT_SERVICE`
- source_post_structure_summary: `法人投稿風の「課題提起 → よくある見落とし → 確認項目 → 解決の方向性 → 資料請求CTA」。専門用語を適度に使いつつ、最後は自社サービスへの誘導で締める。`
- source_post_emotion_summary: `不安の共有と安心への導線。共感（同じ失敗をした人）、発見（新しい視点）、信頼（専門性への期待）を駆動。チェックリストで保存欲求、解決方向性で相談欲求を誘発。`
- target_audience: `中小企業経営者 / 事業責任者 / システム開発を検討している担当者`
- business_goal: `AI活用型短納期システム開発への関心獲得`

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
