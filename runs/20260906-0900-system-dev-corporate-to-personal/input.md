# Run Input

## Run Identification

- run_id: `20260906-0900-system-dev-corporate-to-personal`
- created_at: `2026-09-06T09:00:00+09:00`
- product_service: `AI活用型短納期システム開発`

## Client Context

- industry: `IT / システム開発`
- target_audience: `中小企業経営者 / 事業責任者 / システム開発を検討している担当者`
- posting_purpose: `AI活用型短納期システム開発への関心獲得`
- tone: `個人的・自然・柔らかい。仮説や違和感を共有し、読者の意見を求める。`
- character_limit: `200`
- hashtag_policy: `最大2つ`

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

- hook_type: `法人投稿風の課題提起`
- structure_summary: `課題提起 → よくある見落とし → 確認項目 → 解決の方向性 → 資料請求CTA`
- main_sections: `AI活用型短納期開発の課題 / MVPと本開発の区別 / レビュー体制 / 資料請求`
- cta_type: `document_request`

## Source Post Emotion Summary

- primary_emotion: `短納期開発への期待`
- secondary_emotions: `要件整理不足への不安、スコープ膨張への不安、AIコード生成レビュー不足への不安`
- engagement_driver: `課題認識と解決方向性への関心`
- reaction_design: `資料請求や無料相談への誘導`

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
- product_service: `AI活用型短納期システム開発`
- source_post_structure_summary: `課題提起 → よくある見落とし → 確認項目 → 解決の方向性 → 資料請求CTA`
- source_post_emotion_summary: `短納期開発への期待と、要件整理不足・スコープ膨張・AIコード生成レビュー不足への不安を喚起する`
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
