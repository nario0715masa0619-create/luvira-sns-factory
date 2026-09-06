# Run Input Template

## Run Identification

- run_id: `20260906-1848-system-dev-corporate-to-personal`
- created_at: `2026-09-06T18:48:00.115154+09:00`
- product_service: `AI活用型短納期システム開発`
- product_slug: `system-dev`

> `product_slug` is a short identifier used for the run folder name.  
> Use lowercase English letters, numbers, and hyphens only. Avoid spaces, Japanese characters, and symbols.  
> Examples: `security-diagnosis`, `system-dev`, `line-ai-advisor`

## Client Context

- industry: `IT / システム開発`
- target_audience: `中小企業経営者 / 事業責任者 / システム開発を検討している担当者`
- posting_purpose: `AI活用型短納期システム開発への関心獲得と、要件定義・スコープ管理・AIレビュー・人間承認ゲートなどのサービス価値の認知向上`
- tone: `個人アカウント向け：親しみやすい技術者の自分語り。会社説明にならず、現場の気づきや実務あるあるを語る口調。`
- character_limit: `200`
- hashtag_policy: `MAX_2_HASHTAGS`

## Account Configuration

> **Required.** These two fields must always match the test-case and run folder name.

- source_account_type: `corporate`
- account_type: `personal`
- desired_cta_style: `reply / discussion / experience_sharing`
- allowed_persona_expression: `僕 / 私 / 自分 / 主語省略`
- risk_tolerance: `balanced`

## Source Post Policy

- source_post_reference_type: `structure_only`
- source_post_storage_policy: `do_not_save_third_party_text`

> **Do not paste the full text of a real third-party post here.**  
> Only record structure, emotion, and reaction-design summaries.

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

## Target Configuration

- target_platform: `X`
- target_audience: `中小企業経営者 / 事業責任者 / システム開発を検討している担当者`
- business_goal: `AI活用型短納期システム開発への関心獲得`

## Constraints

- Do not copy the original post text.
- Do not invent personal or corporate experience.
- Do not make unsubstantiated performance claims.
- Do not use exaggerated or fear-mongering expressions.
- Confirm `account_type` and `source_account_type` at every step.
- CTA must match `desired_cta_style`.

## Non-Goals

- Automatic posting.
- API integration.
- n8n workflow.
- Saving real third-party post text.
- Full automation.

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

## Generated Metadata

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
- created_at: `2026-09-06T18:48:00.115154+09:00`
