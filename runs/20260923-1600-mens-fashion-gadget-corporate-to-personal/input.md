# Run Input Template

## Run Identification

- run_id: `20260923-1600-mens-fashion-gadget-corporate-to-personal`
- created_at: `2026-09-23T19:37:20.459088+09:00`
- product_service: `40代男性向けファッション・ガジェット情報発信`
- product_slug: `mens-fashion-gadget`

> `product_slug` is a short identifier used for the run folder name.  
> Use lowercase English letters, numbers, and hyphens only. Avoid spaces, Japanese characters, and symbols.  
> Examples: `security-diagnosis`, `system-dev`, `line-ai-advisor`

## Client Context

- industry: `ファッション・ライフスタイル`
- target_audience: `40代男性 / 経営者 / 営業職 / 見た目と仕事道具を整えたい人`
- posting_purpose: `Measurement Recovery / Replication: H003 爪・髪・香りを OPS-005 と同一条件下で再実行し、初めての strict 24h comparable evidence を取得する。Performance ではなく測定成功が Primary Objective。`
- tone: `同年代の友人に話すような自然な個人口調。高級感より清潔感・実用性を重視。教科書的・啓発的・説教にならない。`
- character_limit: `200`
- hashtag_policy: `2タグ構成：#40代ファッション（Target Tag 固定） + #身だしなみ（Content Angle Tag）。OPS-005 actual execution と同一。追加・変更・削除禁止。`

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

## Source Post Structure Summary (Replication Source: OPS-005)

- hook_type: `observation / realization`
- structure_summary: `フック（40代になって、爪・髪・香りの小さな整え方が意外と大事だと気づいた） → テーマ提示（清潔感は見た目より「そこが整っているか」に出る） → 3つの具体例（爪のケア・髪の整え方・香りの選び方） → 価値転換（高級品じゃなくても、日々の小さな習慣で変わる） → CTA（共感・経験共有型の問いかけ）`
- main_sections: `対比フック（服 vs 身だしなみ） / 3つの具体例 / 価値転換 / 余韻型CTA`
- cta_type: `reply / discussion / experience_sharing（余韻型で終了）`

## Source Post Emotion Summary

- primary_emotion: `共感`
- secondary_emotions: `安心・発見・自己効力感`
- engagement_driver: `お金をかけなくても日々の小さな整え方で印象が変わる、安価で実行可能な改善の発見`
- reaction_design: `個人の観察・気づきを共有し、読者に「自分もできそう」と感じさせる`

## Target Configuration

- target_platform: `X`
- target_audience: `40代男性 / 経営者 / 営業職 / 見た目と仕事道具を整えたい人`
- business_goal: `40代男性向けファッション×ガジェット投稿の反応獲得`

## Constraints

- Do not copy the original post text.
- Do not invent personal or corporate experience.
- Do not make unsubstantiated performance claims.
- Do not use exaggerated or fear-mongering expressions.
- Confirm `account_type` and `source_account_type` at every step.
- CTA must match `desired_cta_style`.

## Replication Constraints (OPS-005 → OPS-009)

This is a **Measurement Recovery / Replication run**, not an optimization run.

| Control | OPS-005 Actual Value | OPS-009 Requirement |
|---------|----------------------|---------------------|
| hypothesis_id | H003 | **EXACT MATCH** |
| content_angle | 爪・髪・香り | **EXACT MATCH** |
| Target Tag | #40代ファッション | **EXACT MATCH** |
| Content Angle Tag | #身だしなみ | **EXACT MATCH** |
| hashtag_count | 2 | **EXACT MATCH** |
| image | none | **EXACT MATCH** |
| URL | none | **EXACT MATCH** |
| account_type | personal | **EXACT MATCH** |
| source_account_type | corporate | **EXACT MATCH** |
| platform | X | **EXACT MATCH** |
| CTA style | reply / discussion / experience_sharing | **EXACT MATCH** |
| information_structure | empathy / awareness | **EXACT MATCH** |
| posting_time_band | 22:41 JST | **NEAR MATCH** (22:40–22:45 JST planned) |
| tone | 観察・気づきの個人口調 | **NEAR MATCH** |
| hook strength | 穏やかな対比フック | **NEAR MATCH** |
| post length | 約130文字（本文） | **NEAR MATCH** |

### Prohibited Changes

- Do not add stronger hooks for virality.
- Do not add practical checklists.
- Do not add numerical claims.
- Do not change structure to a list format.
- Do not introduce a new CTA style.
- Do not change hashtags to #爪髪香り or any other tag.
- Do not optimize posting time to daytime; keep the same band as OPS-005.

### Permitted Variations

- Wording may be refreshed to avoid exact text duplication, as long as the above controls are preserved.
- Minor line-break variations are allowed if the rhythm and length remain similar.

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

- run_id: `20260923-1600-mens-fashion-gadget-corporate-to-personal`
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
- created_at: `2026-09-23T19:37:20.459088+09:00`
