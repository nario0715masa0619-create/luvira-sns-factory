# Human Approval Package

## Run Information

- run_id: `RUN_ID`
- product_service: `PRODUCT_NAME`
- source_account_type: `SOURCE_ACCOUNT_TYPE`
- account_type: `ACCOUNT_TYPE`
- desired_cta_style: `DESIRED_CTA_STYLE`
- risk_tolerance: `RISK_TOLERANCE`
- created_at: `YYYY-MM-DDTHH:MM:SS+09:00`

---

## Final Candidates

### Candidate 01

```text
AI活用の短納期開発、失敗の8割は要件定義に起因してる気がする。「MVPでやりたい」と言いながら、気づいたら本開発の機能がどんどん増えてる。自分がやってる対策は3つ：① 必須機能とnice-to-haveを分ける ② 承認ゲートを設ける ③ 仕様変更のルールを事前に決める。これだけで、後戻りがかなり減る。みんなの現場では、どこでスコープが膨らむ？
```

### Candidate 02

```text
「まずMVPで」って言って始めたのに、気づいたら本開発化してる案件、多くない？
自分も何度かあって、原因はだいたい「MVPの定義が曖昧」なこと。
MVPは「テストしたい仮説を検証する最小限の機能」じゃないと、後から機能が増え続ける。
AIを使う時は特に、生成速度が速い分、方向性がずれるリスクも高い。
だから最初に「何を検証したいか」を紙1枚で固めるようになった。
MVPの定義、みんなどうしてる？
```

### Candidate 03

```text
短納期でAIにコードをガンガン書かせると、後で技術負債が増えるって話。
自分も「とりあえず動けばいい」で進めた案件で、3ヶ月後に苦しんだことがある。
今は短納期でも3つのことを徹底してる：
① レビュー基準を事前に決める
② テスト方針をMVP段階から入れる
③ リファクタリングの工数を見積もる
速さと品質、両立させるのは難しいけど、無理のない線引きができると楽になる。
短納期開発での品質担保、どうしてる？
```

### Candidate 04

```text
AIにコードを書かせて、人間が承認する。
この分担、理想は理想だけど現実は厳しい。
理由は単純で、AIの出力が正しいか判断する基準が人間側にないと、結局全部見直すことになる。
自分は「AIが下書き → 人間が要件と意図を確認 → 承認」って流れにしてる。
確認ポイントは主に3つ：
① セキュリティ
② 可読性
③ テスト観点
他にチェックしてる項目あったら教えて。
```

### Candidate 05

```text
システム開発で「仕様は決まってる」と言われると、大概どこかで変更が入る。
AIを使った短納期開発だと、変更に対応する速度は速いけど、方向性がブレやすい。
自分がやってるのは、変更が来た時に必ず3つを確認すること：
① なぜ変更が必要か
② MVPの範囲に影響するか
③ 他の機能に波及しないか
これをAIに整理させて、人間が最終判断する。
仕様変更への対応、みんなのベストプラクティスがあれば聞きたい。
```

---

## Market Judge Summary

| candidate_id | market_score | judge_comment | selected |
|--------------|--------------|---------------|----------|
| 01 | `29` | `最もバランスが取れている。個人アカウントに最適。` | `yes` |
| 02 | `22` | `専門性は高いが、対象層が狭い。` | `no` |
| 03 | `25` | `議論を誘発しやすいが、やや抽象的。` | `no` |
| 04 | `23` | `痛みを共有できるが、重め。` | `no` |
| 05 | `22` | `実務感はあるが、共感の幅が限定的。` | `no` |

### Notes

Auto-generated from step-09-market-judge.md. Recommended candidate: 01.

---

## Recommended Candidate

### Candidate 01

```text
AI活用の短納期開発、失敗の8割は要件定義に起因してる気がする。

「MVPでやりたい」と言いながら、気づいたら本開発の機能がどんどん増えてる。

自分がやってる対策は3つ：
① 必須機能とnice-to-haveを分ける
② 承認ゲートを設ける
③ 仕様変更のルールを事前に決める

これだけで、後戻りがかなり減る。

みんなの現場では、どこでスコープが膨らむ？
```

### Selection Reason

- フック力と共感度が両立
- 個人アカウントに最適な「自分の現場」感
- 3つの対策が具体的で保存・議論を誘発

---

## Similarity Review

- Overall similarity risk: `low`
- Source hook retention: `medium`
- Phrase copy risk: `low`
- Structural copy risk: `medium`

### Notes

元コーポレート投稿の「課題 → 対策 → CTA」構造を参考にしつつ、言い回し・トーン・CTAを完全に置換。フレーズコピーはなし。

---

## Risk Review

> **Note:** Before step 08 Risk Filter output exists, `pending` may be recorded.  
> After step 08, update each row to `low`, `medium`, `high`, or `rejected`.  
> Human approval is **not allowed** while any risk row remains `pending`.

| Risk Category | Level | Notes |
|---------------|-------|-------|
| Fabricated experience | low | 個人の観察として語っており、架空の体験を断定的に述べていない。 |
| Unsubstantiated claims | low | 「8割」は「気がする」で修飾。絶対的な主張は避けている。 |
| Effect guarantee | low | 「後戻りがかなり減る」は方向性であり、効果保証ではない。 |
| Fear-mongering | low | 問題を共有するが、煽りすぎていない。 |
| Account type mismatch | low | personalアカウント向けのトーン・一人称・CTA。 |
| CTA mismatch | low | 返信・議論を促すCTA。desired_cta_styleと一致。 |
| Product pushiness | low | 商材名を直接出しておらず、専門性で自然に接続。 |
| Controversy risk | low | 中立的な技術テーマ。炎上リスクは低い。 |

---

## Account Type Fit

- account_type: `personal`
- source_account_type: `corporate`
- Tone fit: `good`
- Persona fit: `good`
- CTA fit: `good`

### Notes

個人アカウント向けの自分語りトーン。source corporate から personal への転用調整は適切。

---

## CTA Fit

- desired_cta_style: `reply / discussion / experience_sharing`
- Actual CTA: `みんなの現場では、どこでスコープが膨らむ？`
- Fit: `good`

### Notes

CTAが返信・議論を誘発する問いかけになっており、desired_cta_styleと一致。

---

## Human Approval Decision

Please check one:

- [ ] **Approved as-is**
- [ ] **Approved with edits**
- [ ] **Rejected**
- [ ] **Regenerate required**

### Decision Notes

[APPROVER_DECISION_NOTES]

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

---

## Posting Record

- posted_at: `YYYY-MM-DDTHH:MM:SS+09:00`
- post_url: `https://...`
- posted_by: `NAME`
- platform: `X`

---

## 24h Metrics Record

- metrics_due_at: `YYYY-MM-DDTHH:MM:SS+09:00`
- impressions_24h: `NUMBER`
- engagement_24h: `NUMBER`
- replies_24h: `NUMBER`
- clicks_24h: `NUMBER`
- notes: `METRICS_NOTES`

---

## Final Notes

[ANY_ADDITIONAL_NOTES]
