# Step 01: Pattern Miner Input

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

The following sections are extracted from `input.md`. They contain the source post summary and the instructions for Step 01.

## Source Post Structure Summary

- hook_type: `「40代男性の見た目・身だしなみに関する意外な共通認識」や「あるある」を提示する問いかけ`
- structure_summary: `法人・メディア風の「おすすめアイテム紹介」または「身だしなみチェックリスト」。アイテムをカテゴリ別に紹介し、それぞれに「なぜ良いか」「誰に向いているか」を説明。最後はフォロー・保存・購入導線を促すCTAで締める。`
- main_sections: `1. フック：40代男性の見た目や身だしなみに関する意外性のある問いかけ / 2. テーマ提示：今回扱うアイテムや視点を列挙 / 3. アイテム紹介：ファッション・ガジェットをカテゴリ別に解説 / 4. 選び方のポイント：年齢に応じた清潔感や品質の基準 / 5. CTA：保存・フォロー・購入への誘導`
- cta_type: `保存・フォロー・購入導線（コーポレート/メディアアカウント向け）`

## Source Post Emotion Summary

- primary_emotion: `「今の自分も整えられる」という希望と、年齢に対する安心感`
- secondary_emotions: `共感（同じ悩みを持つ人）、発見（新しいアイテムや視点）、憧れ（理想の自分像）、実用感（すぐ使える情報）`
- engagement_driver: `「40代でも遅くない」「意外と簡単に変われる」「これなら自分もできる」という気づきと、チェックリストや具体的アイテム名による保存欲`
- reaction_design: `フックで「自分も当てはまるかも」と共感させ、アイテム紹介で「欲しい」「参考になる」と思わせ、CTAで保存・フォローを促す設計`

## Step 01 Input for Pattern Miner

### Source Post Reference

> **Reminder:** Store only structure, emotion, and reaction design. Do not paste full text of real posts.

- source_account_type: `corporate`
- account_type: `personal`
- product_service: `PRODUCT_SERVICE`
- source_post_structure_summary: `法人・メディア風の「おすすめアイテム紹介」または「身だしなみチェックリスト」。アイテムをカテゴリ別に紹介し、それぞれに「なぜ良いか」「誰に向いているか」を説明。最後はフォロー・保存・購入導線を促すCTAで締める。`
- source_post_emotion_summary: `「今の自分も整えられる」という希望と年齢に対する安心感。共感、発見、憧れ、実用感を駆動。チェックリストで保存欲求、理想像でフォロー欲求を誘発。`
- target_audience: `40代男性 / 経営者 / 個人事業主 / 営業職 / 見た目と仕事道具を整えたい人`
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
