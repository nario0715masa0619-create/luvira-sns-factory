# Run Input Template

## Run Identification

- run_id: `20260907-0751-mens-fashion-gadget-corporate-to-personal`
- created_at: `2026-09-07T07:51:40.500000+09:00`
- product_service: `40代男性向けファッション・ガジェット情報発信`
- product_slug: `mens-fashion-gadget`

> `product_slug` is a short identifier used for the run folder name.  
> Use lowercase English letters, numbers, and hyphens only. Avoid spaces, Japanese characters, and symbols.  
> Examples: `security-diagnosis`, `system-dev`, `line-ai-advisor`

## Client Context

- industry: `ファッション・ライフスタイル・ガジェット`
- target_audience: `40代男性 / 経営者 / 個人事業主 / 営業職 / 見た目と仕事道具を整えたい人`
- posting_purpose: `40代男性向けファッション×ガジェット投稿の反応獲得`
- tone: `同年代の友達に自慢げに教えるような、でも押し付けがましくない自分語り。高級感より清潔感・実用性を重視。`
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

- hook_type: `「見た目が変わる小さな習慣」型フック`
- structure_summary: `フック（身の回りを整えるだけで印象が変わる） → テーマ提示（服を買い足す前に小物・清潔感を整える） → 具体例リスト（靴・財布・ケーブル・イヤホン・ポーチ・スマホケース・爪・髪・香り） → 価値転換（高級品ではなく、整って見えること） → CTA（保存/フォロー）`
- main_sections: `フック / テーマ / 具体的小物・ケア例 / 価値転換 / CTA`
- cta_type: `save_or_follow`

## Source Post Emotion Summary

- primary_emotion: `希望`
- secondary_emotions: `発見, 共感, 安心`
- engagement_driver: `「高級品を買わなくても印象が変わる」という安価で実行可能な改善の発見`
- reaction_design: `「これなら私もできる」「参考になった」「同じこと思ってた」といった共感・保存反応を狙う`

## Target Configuration

- target_platform: `X`
- target_audience: `TARGET_AUDIENCE_FOR_THIS_RUN`
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
- product_service: `40代男性向けファッション・ガジェット情報発信`
- source_post_structure_summary: `フック（身の回りを整えるだけで印象が変わる） → テーマ提示（服を買い足す前に小物・清潔感を整える） → 具体例リスト（靴・財布・ケーブル・イヤホン・ポーチ・スマホケース・爪・髪・香り） → 価値転換（高級品ではなく、整って見えること） → CTA（保存/フォロー）`
- source_post_emotion_summary: `希望・発見・共感・安心。高級品を買わなくても印象が変わる、安価で実行可能な改善の発見。`
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
- created_at: `2026-09-07T07:51:40.500000+09:00`
