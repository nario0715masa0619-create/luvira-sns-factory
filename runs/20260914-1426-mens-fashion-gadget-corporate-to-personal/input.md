# Run Input Template

## Run Identification

- run_id: `20260914-1426-mens-fashion-gadget-corporate-to-personal`
- created_at: `2026-09-14T14:26:00+09:00`
- product_service: `40代男性向けファッション・ガジェット情報発信`
- product_slug: `mens-fashion-gadget`

> `product_slug` is a short identifier used for the run folder name.  
> Use lowercase English letters, numbers, and hyphens only. Avoid spaces, Japanese characters, and symbols.  
> Examples: `security-diagnosis`, `system-dev`, `line-ai-advisor`

## Client Context

- industry: `ファッション・ライフスタイル`
- target_audience: `40代男性 / 経営者 / 営業職 / 見た目と仕事道具を整えたい人`
- posting_purpose: `Distribution Learning: H009 営業/経営者の第一印象で、40代男性向け個人アカウントにおけるビジネス文脈content_angleの反応を検証。content_angleのみ変更し、既存Control条件は維持。`
- tone: `同年代の友人に話すような自然な個人口調。ビジネス文脈でありながら法人公式調・教科書調・上から目線にならない。`
- character_limit: `200`
- hashtag_policy: `2タグ構成：#40代ファッション（Target Tag 固定） + Content Angle Tag（H009に応じて #第一印象 を使用）。詳細は knowledge/mens-fashion-gadget/hashtag-strategy.md。`

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

- hook_type: `「40代になって気づいた」型 / ビジネスシーンでの気づき`
- structure_summary: `フック（40代の商談で、高い服より細かいところで第一印象が決まる） → 具体例の列挙（ジャケットの袖丈・手入れされた靴・名刺を出すときの手元） → 価値転換（派手じゃないが、こういう部分が整っているとちゃんとして見える） → CTA（経験・共感を誘発する問いかけ）`
- main_sections: `フック / 具体例 / 価値転換 / CTA`
- cta_type: `reply / discussion / experience_sharing`

## Source Post Emotion Summary

- primary_emotion: `共感`
- secondary_emotions: `発見, ビジネス文脈での安心`
- engagement_driver: `「高い服じゃなくて、細部が整っていると仕事の場でちゃんとして見える」という発見`
- reaction_design: `「自分も気をつけてる」「同じこと思う」という共感リプライや経験共有を誘発する`

## Target Configuration

- target_platform: `X`
- target_audience: `40代男性 / 経営者 / 営業職 / 見た目と仕事道具を整えたい人`
- business_goal: `40代男性向けファッション×ガジェット投稿の反応獲得`

## Constraints

- Do not copy the original post text.
- Do not invent personal or corporate experience.
- Do not make unsubstantiated performance claims.
- Do not use exaggerated or fear-mongering expressions.
- Avoid: 「成功者は全員〜」「40代なら絶対」「やらないと終わり」「モテる」「若返る」「清潔感がない人はダメ」「信頼感が全然違う」等の強い因果・効果保証表現
- Avoid: 未確認の個人体験（「自分が意識してるのは3つ」）や ①②③ 形式の箇条書き
- H003「爪・髪・香り」をそのまま言い換えるだけにしない。
- ビジネスシーン固有の文脈（商談、名刺交換、会食、営業先等）を含める。
- Confirm `account_type` and `source_account_type` at every step.
- CTA must match `desired_cta_style`.
- Image: none, URL: none.

## Non-Goals

- Automatic posting.
- API integration.
- n8n workflow.
- Saving real third-party post text.
- Full automation.

## Previous Learning

```text
Previous Learning:
- previous_run_id: 20260910-1149-mens-fashion-gadget-corporate-to-personal
- hypothesis_id: H003
- result_label: non_comparable
- strongest_signal: none
- weakest_signal: measurement_missed
- try_next_time: OPS-006は既存Control条件を維持したままcontent_angleのみH009営業・経営者の第一印象へ変更
- avoid_next_time: 24h metrics未取得でdelayed observationのみで判断 / H003を1投稿でretired扱い / OPS-006でimage・CTA style・posting timeを同時変更
- recommended_content_angle: H009営業/経営者の第一印象
- recommended_hook_style: 「40代になって気づいた」型を維持
- recommended_cta_style: reply/discussion/experience_sharing（canonical CTA styleを維持）
- experiment_control: image=none, URL=none, Target Tag=#40代ファッション, hashtag_count=2, posting_time=existing control
```

## Step 01 Input for Pattern Miner

### Source Post Reference

> **Reminder:** Store only structure, emotion, and reaction design. Do not paste full text of real posts.

- source_account_type: `corporate`
- account_type: `personal`
- product_service: `40代男性向けファッション・ガジェット情報発信`
- source_post_structure_summary: `フック（40代の商談で、高い服より細かいところで第一印象が決まる） → 具体例の列挙（ジャケットの袖丈・手入れされた靴・名刺を出すときの手元） → 価値転換（派手じゃないが、こういう部分が整っているとちゃんとして見える） → CTA（経験・共感を誘発する問いかけ）`
- source_post_emotion_summary: `共感・発見・ビジネス文脈での安心。高い服じゃなくて細部が整っていると仕事の場でちゃんとして見える、という発見。`
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

- run_id: `20260914-1426-mens-fashion-gadget-corporate-to-personal`
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
- created_at: `2026-09-14T14:26:00+09:00`
