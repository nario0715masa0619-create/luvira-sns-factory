# Run Input Template

## Run Identification

- run_id: `20260906-1000-system-dev-corporate-to-personal`
- created_at: `2026-09-06T13:25:15.126569+09:00`
- product_service: `AI活用型短納期システム開発`
- product_slug: `system-dev`

> `product_slug` is a short identifier used for the run folder name.  
> Use lowercase English letters, numbers, and hyphens only. Avoid spaces, Japanese characters, and symbols.  
> Examples: `security-diagnosis`, `system-dev`, `line-ai-advisor`

## Client Context

- industry: `INDUSTRY`
- target_audience: `中小企業経営者 / 事業責任者`
- posting_purpose: `POSTING_PURPOSE`
- tone: `TONE`
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

- hook_type: `HOOK_TYPE`
- structure_summary: `STRUCTURE_SUMMARY`
- main_sections: `MAIN_SECTIONS`
- cta_type: `CTA_TYPE`

## Source Post Emotion Summary

- primary_emotion: `PRIMARY_EMOTION`
- secondary_emotions: `SECONDARY_EMOTIONS`
- engagement_driver: `ENGAGEMENT_DRIVER`
- reaction_design: `REACTION_DESIGN`

## Target Configuration

- target_platform: `X`
- target_audience: `TARGET_AUDIENCE_FOR_THIS_RUN`
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
- source_post_structure_summary: `STRUCTURE_SUMMARY`
- source_post_emotion_summary: `EMOTION_SUMMARY`
- target_audience: `中小企業経営者 / 事業責任者`
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

- run_id: `20260906-1000-system-dev-corporate-to-personal`
- product_service: `AI活用型短納期システム開発`
- product_slug: `system-dev`
- source_account_type: `corporate`
- account_type: `personal`
- desired_cta_style: `reply / discussion / experience_sharing`
- allowed_persona_expression: `僕 / 私 / 自分 / 主語省略`
- risk_tolerance: `balanced`
- target_platform: `X`
- target_audience: `中小企業経営者 / 事業責任者`
- business_goal: `AI活用型短納期システム開発への関心獲得`
- model: `kimi-k2.7-code`
- execution_mode: `file_based_semi_automation`
- created_at: `2026-09-06T13:25:15.126569+09:00`
