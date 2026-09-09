# Run Input Template

## Run Identification

- run_id: `20260908-0801-mens-fashion-gadget-corporate-to-personal`
- created_at: `2026-09-08T08:01:44.360562+09:00`
- product_service: `40代男性向けファッション・ガジェット情報発信`
- product_slug: `mens-fashion-gadget`

> `product_slug` is a short identifier used for the run folder name.  
> Use lowercase English letters, numbers, and hyphens only. Avoid spaces, Japanese characters, and symbols.  
> Examples: `security-diagnosis`, `system-dev`, `line-ai-advisor`

## Client Context

- industry: `ファッション・ライフスタイル`
- target_audience: `40代男性 / 経営者 / 営業職 / 見た目と仕事道具を整えたい人`
- posting_purpose: `Distribution Learning: H002 靴の手入れで、同一運用フレームでの Distribution 確保可能性を検証。OPS-002（impressions=149、late measurement）との比較基準で評価。engagement は参考記録。`
- tone: `同年代の友人に話すような自然な個人口調。高級感より清潔感・実用性を重視。教科書的・啓発的にならない。`
- character_limit: `200`
- hashtag_policy: `2タグ構成：#40代ファッション（Target Tag 固定） + #靴の手入れ（Content Angle Tag）。詳細は knowledge/mens-fashion-gadget/hashtag-strategy.md。`

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

- hook_type: `「40代になって気づいた」型フック`
- structure_summary: `フック（40代になって、高い靴よりちゃんと手入れしてる靴が大事だと気づいた） → テーマ提示（靴の手入れは週1回の小さな習慣） → 3つの具体的手入れ例（ブラシ・クリーム・乾拭き） → 価値転換（高級靴じゃなくても清潔感があれば十分） → CTA（共感・経験共有型の問いかけ）`
- main_sections: `フック / テーマ / 3つの手入れ例 / 価値転換 / CTA`
- cta_type: `reply / discussion / experience_sharing`

## Source Post Emotion Summary

- primary_emotion: `共感`
- secondary_emotions: `安心, 発見, 自己効力感`
- engagement_driver: `「お金をかけなくても、手入れするだけで印象が変わる」という安価で実行可能な改善の発見`
- reaction_design: `「自分もやってる」「同じこと思ってた」という共感リプライや経験共有を誘発する`

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

## Generated Metadata

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
- created_at: `2026-09-08T08:01:44.360562+09:00`
