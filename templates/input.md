# Run Input Template

## Run Identification

- run_id: `RUN_ID`
- created_at: `YYYY-MM-DDTHH:MM:SS+09:00`
- product_service: `PRODUCT_NAME`

## Client Context

- industry: `INDUSTRY`
- target_audience: `TARGET_AUDIENCE`
- posting_purpose: `POSTING_PURPOSE`
- tone: `TONE`
- character_limit: `200`
- hashtag_policy: `MAX_2_HASHTAGS`

## Account Configuration

> **Required.** These two fields must always match the test-case and run folder name.

- source_account_type: `personal` or `corporate`
- account_type: `personal` or `corporate`
- desired_cta_style: `reply / discussion / experience_sharing` or `checklist / consultation / document_request`
- allowed_persona_expression: `PERSONA_OPTIONS`
- risk_tolerance: `balanced` or `conservative`

## Source Post Policy

- source_post_reference_type: `fictional_sample` or `client_original`
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
- business_goal: `BUSINESS_GOAL`

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

- source_account_type: `SOURCE_ACCOUNT_TYPE`
- account_type: `ACCOUNT_TYPE`
- product_service: `PRODUCT_SERVICE`
- source_post_structure_summary: `STRUCTURE_SUMMARY`
- source_post_emotion_summary: `EMOTION_SUMMARY`
- target_audience: `TARGET_AUDIENCE`
- business_goal: `BUSINESS_GOAL`

### Instructions for Pattern Miner

Please analyze the source post structure and emotion drivers, then produce output in the standard Phase 1 format:

1. Structure pattern
2. Emotion drivers
3. Reusable framework
4. Product-specific notes
5. Risk notes

Ensure `source_account_type` and `account_type` are clearly stated.
