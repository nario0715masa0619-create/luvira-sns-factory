# Run Input Template

## Run Identification

- run_id: `20260906-2132-mens-fashion-gadget-corporate-to-personal`
- created_at: `2026-09-06T21:32:45.702245+09:00`
- product_service: `40代男性向けファッション・ガジェット情報発信`
- product_slug: `mens-fashion-gadget`

> `product_slug` is a short identifier used for the run folder name.  
> Use lowercase English letters, numbers, and hyphens only. Avoid spaces, Japanese characters, and symbols.  
> Examples: `security-diagnosis`, `system-dev`, `line-ai-advisor`

## Client Context

- industry: `ファッション・ライフスタイル・ガジェット`
- target_audience: `40代男性 / 経営者 / 個人事業主 / 営業職 / 見た目と仕事道具を整えたい人`
- posting_purpose: `40代男性向けファッション×ガジェット投稿の反応獲得。保存したい・真似したい・これ欲しい・自分も整えたいと思わせる内容で、個人アカウントらしい信頼と親近感を構築。`
- tone: `個人アカウント向け：同年代の友達に自慢げに教えるような、でも押し付けがましくない自分語り。高級感より清潔感・実用性を重視。`
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

- hook_type: `「40代男性の見た目・身だしなみに関する意外な共通認識」や「あるある」を提示する問いかけ`
- structure_summary: `法人・メディア風の「おすすめアイテム紹介」または「身だしなみチェックリスト」。アイテムをカテゴリ別に紹介し、それぞれに「なぜ良いか」「誰に向いているか」を説明。最後はフォロー・保存・購入導線を促すCTAで締める。`
- main_sections: `1. フック：40代男性の見た目や身だしなみに関する意外性のある問いかけ / 2. テーマ提示：今回扱うアイテムや視点を列挙 / 3. アイテム紹介：ファッション・ガジェットをカテゴリ別に解説 / 4. 選び方のポイント：年齢に応じた清潔感や品質の基準 / 5. CTA：保存・フォロー・購入への誘導`
- cta_type: `保存・フォロー・購入導線（コーポレート/メディアアカウント向け）`

## Source Post Emotion Summary

- primary_emotion: `「今の自分も整えられる」という希望と、年齢に対する安心感`
- secondary_emotions: `共感（同じ悩みを持つ人）、発見（新しいアイテムや視点）、憧れ（理想の自分像）、実用感（すぐ使える情報）`
- engagement_driver: `「40代でも遅くない」「意外と簡単に変われる」「これなら自分もできる」という気づきと、チェックリストや具体的アイテム名による保存欲`
- reaction_design: `フックで「自分も当てはまるかも」と共感させ、アイテム紹介で「欲しい」「参考になる」と思わせ、CTAで保存・フォローを促す設計`

## Target Configuration

- target_platform: `X`
- target_audience: `40代男性 / 経営者 / 個人事業主 / 営業職 / 見た目と仕事道具を整えたい人`
- business_goal: `40代男性向けファッション×ガジェット投稿の反応獲得`

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

## Generated Metadata

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
- created_at: `2026-09-06T21:32:45.702245+09:00`
