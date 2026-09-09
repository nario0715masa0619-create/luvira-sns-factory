# Human Approval Package

## Run Information

- run_id: `20260908-0801-mens-fashion-gadget-corporate-to-personal`
- product_service: `40代男性向けファッション・ガジェット情報発信`
- source_account_type: `corporate`
- account_type: `personal`
- desired_cta_style: `reply / discussion / experience_sharing`
- risk_tolerance: `balanced`
- created_at: `2026-09-08T08:01:44.360562+09:00`

---

## Final Candidates

### Candidate 01

```text

```

### Candidate 02

```text

```

### Candidate 03

```text

```

### Candidate 04

```text

```

### Candidate 05

```text

```

---

## Market Judge Summary

| candidate_id | market_score | judge_comment | selected |
|--------------|--------------|---------------|----------|
| 01 | `` | `` | `yes` |
| 02 | `` | `` | `no` |
| 03 | `` | `` | `no` |
| 04 | `` | `` | `no` |
| 05 | `` | `` | `no` |

### Notes

Auto-generated from step-09-market-judge.md. Recommended candidate: 01.

---

## Recommended Candidate

### Candidate 01

```text
40代になって、高い靴よりちゃんと手入れしてる靴の方が大事だと気づいた。

自分がやってるのは3つ：
① 週1回ブラシでホコリを落とす
② 月1回クリームを塗る
③ 雨の日は翌日に乾拭きする

高い靴じゃなくても、手入れが行き届いてるだけで全然違う。

みんなの靴の手入れ、何が必須？

#40代ファッション #靴の手入れ
```

### Selection Reason

- フックが個人の気づきで自然
- 3つの手入れ例が具体的で実行可能
- CTA「みんなの靴の手入れ、何が必須？」はOPS-002のCTA形式と同一で、Distribution比較を優先
- 画像なし・URLなし・text-only
- ハッシュタグは OPS-002 と同じ2タグ構成：`#40代ファッション`（Target Tag 固定） + `#靴の手入れ`（Content Angle Tag）

### Experiment Purpose

- **Run Type**: Distribution Learning Run
- **Primary KPI**: impressions
- **Goal**: 別 content angle（H002 靴の手入れ）でも、同一運用フレームで Distribution を確保できるかを検証する。corporate-to-personal 構造の再現性を単独Runで断定するのではなく、複数angleでの傾向を観察する。
- **Secondary Metrics**: likes / replies / reposts / bookmarks / profile_clicks / follows（参考記録。今回は最適化対象外）
- **Comparison Baseline**: OPS-002 impressions = 149（late measurement、投稿後約57時間計測）
- **Comparison Method**: impression_ratio_vs_ops002 = OPS-004 impressions / 149
- **Posting Conditions to Record**: 投稿時間帯、曜日、画像有無、URL有無、ハッシュタグ（Target Tag / Content Angle Tag）

### Distribution Comparison Recording

> 現時点ではサンプル数が1（OPS-002のみ）のため、`higher` / `comparable` / `lower` / `success` / `weak` / `no_signal` といった閾値分類を Canonical な評価基準として新規固定しない。
> OPS-004の観測値を蓄積し、Distribution Learning Runを複数回実施した後、実測分布から判定帯・winning pattern を導出する。

**OPS-002 baseline**

- impressions = 149
- hashtags: `#40代ファッション` `#バッグの中身`
- image: none
- URL: none
- measured_at: 2026-09-06T22:35:48+09:00（投稿後約33時間）

**OPS-004 計測後に記録する生データ**

| Item | Value / Formula |
|------|-----------------|
| OPS-004 impressions | 計測値 |
| OPS-002 impressions | 149 |
| impression_ratio_vs_ops002 | OPS-004 impressions / 149 |
| raw_difference | OPS-004 impressions - 149 |
| posting_time | 実際の投稿時刻 |
| weekday | 投稿した曜日 |
| hashtags | `#40代ファッション` `#靴の手入れ`（固定） |
| image | none（固定） |
| URL | none（固定） |
| other_condition_diffs | 明らかな条件差があれば記録 |

**Interpretation Rule**

- 単独Runの結果から「この構造が再現した」「このcontent angleが勝った」とは断定しない。
- 生ratioを中心に記録し、post-analysis では ratio と条件差を優先して議論する。
- 既存schemaで `result_label` などのlabel入力が必須の場合のみ、既存仕様に従って記録する。
- 判定帯・winning pattern は複数の Distribution Learning Run を蓄積した後に導出する。

---

## Similarity Review

- Overall similarity risk: `low`
- Source hook retention: `medium`
- Phrase copy risk: `low`
- Structural copy risk: `medium`

### Notes

元コーポレート/メディア投稿の「フック → テーマ → 具体例 → 価値転換 → CTA」構造を参考にしつつ、言い回し・トーン・CTAを完全に置換。フレーズコピーはなし。

---

## Risk Review

> **Note:** Before step 08 Risk Filter output exists, `pending` may be recorded.  
> After step 08, update each row to `low`, `medium`, `high`, or `rejected`.  
> Human approval is **not allowed** while any risk row remains `pending`.

| Risk Category | Level | Notes |
|---------------|-------|-------|
| Fabricated experience | low | 個人の習慣として語っており、架空の購入経験を断定的に述べていない。 |
| Unsubstantiated claims | low | 「大事だと気づいた」「変わる」は個人の体感。絶対的な主張ではない。 |
| Effect guarantee | low | 効果保証をしていない。 |
| Fear-mongering | low | 中立的。 |
| Account type mismatch | low | personalアカウント向けのトーン・一人称・CTA。 |
| CTA mismatch | low | 返信・共感を促すCTA。desired_cta_styleと一致。 |
| Product pushiness | low | 特定ブランドを推奨していない。 |
| Controversy risk | low | 中立的なライフスタイルテーマ。 |

---

## Account Type Fit

- account_type: `personal`
- source_account_type: `corporate`
- Tone fit: `good`
- Persona fit: `good`
- CTA fit: `good`

### Notes

個人アカウント向けの自分語りトーン。source corporate から personal への転用調整は適切。高級感より清潔感を重視。説教臭くない。

---

## CTA Fit

- desired_cta_style: `reply / discussion / experience_sharing`
- Actual CTA: `みんなの靴の手入れ、何が必須？`
- Fit: `good`

### Notes

CTAはOPS-002「みんなのバッグの中身、何が必須？」と同一形式。Distribution Learning Run ではCTAを比較変数とせず、content_angleの影響を測定するため固定。engagement最適化目的では変更していない。

ハッシュタグも OPS-002 と同一の2タグ構成（Target Tag 固定 + Content Angle Tag）を維持。詳細は `knowledge/mens-fashion-gadget/hashtag-strategy.md` を参照。

---

## Human Approval Decision

Please check one:

- [x] **Approved as-is**
- [ ] **Approved with edits**
- [ ] **Rejected**
- [ ] **Regenerate required**

### Decision Notes

Approved and posted as-is. Baseline corrected to OPS-002 impressions=149 before posting.

---

## Required Edits

If "Approved with edits" or "Regenerate required" is selected, describe the required changes here:

[EDIT_INSTRUCTIONS]

---

## Pre-Post Checklist

Before posting, confirm all of the following:

- [ ] `account_type` is correct.
- [ ] `source_account_type` is correct.
- [ ] CTA matches `desired_cta_style`.
- [ ] No fabricated personal or corporate experience.
- [ ] No rumor or consultation-track-record implication.
- [ ] No unsubstantiated performance claims.
- [ ] No effect guarantee or exaggeration.
- [ ] No full-text copy of the original post.
- [ ] Controversy risk is within acceptable range.
- [ ] Final poster has performed a last visual check.
- [ ] Distribution Learning Run としての目的を理解している。
- [ ] 画像・URLを追加していない。
- [ ] ハッシュタグは `#40代ファッション` `#靴の手入れ` の2つのみを使用している。
- [ ] 独自判断でタグを追加・削除・変更していない。
- [ ] OPS-002 との比較可能性を損なっていない。

---

## Posting Record

- posted_at: `2026-09-09T10:29:00+09:00`
- post_url: `https://x.com/ritsu_opt/status/2097497349392359722?s=20`
- posted_by: `human`
- platform: `X`

---

## 24h Metrics Record

- metrics_due_at: `2026-09-10T10:29:00+09:00`
- measurement_target: `strict_24h_preferred`
- impressions_24h: ``
- engagement_24h: ``
- replies_24h: ``
- clicks_24h: ``
- notes: `METRICS_NOTES`

---

## Final Notes

[ANY_ADDITIONAL_NOTES]

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
