# Final Candidates

## Run Information

- run_id: `20260914-1426-mens-fashion-gadget-corporate-to-personal`
- ops_id: `OPS-006`
- product_service: `40代男性向けファッション・ガジェット情報発信`
- product_slug: `mens-fashion-gadget`
- source_account_type: `corporate`
- account_type: `personal`
- hypothesis_id: `H009`
- content_angle: `営業/経営者の第一印象`
- desired_cta_style: `reply / discussion / experience_sharing`
- image: `none`
- url: `none`
- created_at: `2026-09-14T14:26:00+09:00`

## Experiment Control

OPS-006 で変更する変数は **content_angle のみ**。

| Condition | Value | Change? |
|-----------|-------|---------|
| account_type | personal | no |
| transformation | corporate-to-personal | no |
| Target Tag | #40代ファッション | no |
| hashtag count | 2 | no |
| Content Angle Tag | #第一印象 | yes（content_angle と連動） |
| image | none | no |
| URL | none | no |
| CTA style | reply / discussion / experience_sharing | no |
| posting time | existing Canonical Control | no |
| content_angle | H009 営業/経営者の第一印象 | **yes** |

---

## Candidate A — 共感型

```text
40代になって、営業先や経営者同士の場で、
服の値段より「そこが整ってるか」で第一印象が決まる気がする。

高いスーツより、袖の長さが合ってること。
革靴が手入れされてること。
髪が寝てないこと。
名刺を出す瞬間の爪の清潔さ。

こういうところが、相手に
「この人、仕事できそう」と思わせる前の
静かな説明をしてる気がする。

みんなが気をつけてる第一印象のポイント、何？

#40代ファッション #第一印象
```

## Candidate B — 経験談型（Human Edited Final）

```text
40代になって、商談の第一印象って
「高い服」より細かいところで決まる気がする。

ジャケットの袖丈。
手入れされた靴。
名刺を出すときの手元。

どれも派手じゃないけど、
こういう部分が整ってる人は、
それだけでちゃんとして見える。

営業や商談で、
みんなが気をつけてるポイントって何？

#40代ファッション #第一印象
```

- 修正履歴: `human edited before approval`
- 修正理由: 未確認の個人体験表現（「自分が意識してるのは3つ」）を避け、①②③形式を外してAI生成感を減らし、「信頼感が全然違う」等の強い因果表現を避け、H003「爪・髪・香り」との重複を弱めた。

## Candidate C — 問いかけ型

```text
40代の営業・経営者にとって、
第一印象はどこで決まってる？

自分が商談や会食で気にしてるのは、
袖の長さ、靴の手入れ、
髪の寝ぐせ、名刺を渡す時の爪。

高い服じゃなくて、
こういう細部が整ってるだけで、
相手の信頼感が変わる気がする。

第一印象で気になるのは、
服装それとも細部？

#40代ファッション #第一印象
```

---

## Candidate Evaluation

| Criteria | Candidate A | Candidate B | Candidate C |
|----------|-------------|-------------|-------------|
| Hook strength | 4 | 4 | 3 |
| 40代男性への刺さり | 4 | 4 | 4 |
| H009 一致度 | 4 | 5 | 4 |
| discussion 誘発力 | 4 | 4 | 4 |
| AI 感の少なさ | 4 | 4 | 3 |
| 既存 OPS との差別化 | 4 | 4 | 4 |
| **Total** | **24** | **25** | **22** |

### Evaluation Notes

- **Candidate A**: フックが自然で共感型。具体例にビジネス文脈（名刺交換）が入る。ただし「高いスーツより」が OPS-005 の「高い服より」と構造的に近い。
- **Candidate B**: H009 ビジネス文脈（商談・名刺交換）との一致度が最も高い。個人の経験談として自然。3つの具体例は AI 感を抑えつつ視覚的。CTA が経験共有型に適合。
- **Candidate C**: 問いかけ型フックは好奇心を誘うが、やや AI 生成感・抽象的になりがち。H009 一致度は高いが、自然さで Candidate B に劣る。

## Selected Candidate

**Candidate B**

### Selection Reason

- H009「営業/経営者の第一印象」というビジネス文脈との一致度が最も高い。
- 個人の経験談トーンが自然で、40代男性の共感を誘発しやすい。
- 具体例（袖丈・靴・爪）が視覚的で、text-only でも伝わりやすい。
- CTA「営業・商談で気をつけてるポイント、ある？」が desired_cta_style に適合。
- H003「爪・髪・香り」を単なる言い換えにせず、ビジネスシーン（商談・名刺交換）を付加している。
- human edited before approval: 未確認の個人体験表現・①②③形式・強い因果表現を避け、AI生成感を減らし、H003との重複を弱めた。

## Final Selected Text

```text
40代になって、商談の第一印象って
「高い服」より細かいところで決まる気がする。

ジャケットの袖丈。
手入れされた靴。
名刺を出すときの手元。

どれも派手じゃないけど、
こういう部分が整ってる人は、
それだけでちゃんとして見える。

営業や商談で、
みんなが気をつけてるポイントって何？

#40代ファッション #第一印象
```

## Hashtags

- Target Tag: `#40代ファッション`
- Content Angle Tag: `#第一印象`
- 理由: `knowledge/mens-fashion-gadget/hashtag-strategy.md` において、H009 の Content Angle Tag は「実施時に決定」とされている。#第一印象 はテーマに即しており、2タグ構成を維持する。

## Image / URL

- image: `none`
- url: `none`

## Posting Checklist

- [ ] 最終テキストを目視確認
- [ ] ハッシュタグが2タグであることを確認
- [ ] 画像・URLが含まれていないことを確認
- [ ] CTA が desired_cta_style に適合していることを確認
- [ ] 投稿時刻を記録
- [ ] 24時間後のインプレッションを記録

## Next Step

This candidate is ready for human approval. Please review `approval.md` and confirm posting.
