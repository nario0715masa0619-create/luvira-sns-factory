## Risk Filter Review

### Candidate 01: 要件整理フォーカス

```
AI活用の短納期開発、失敗の8割は要件定義に起因してる気がする。

「MVPでやりたい」と言いながら、気づいたら本開発の機能がどんどん増えてる。

自分がやってる対策は3つ：
① 必須機能とnice-to-haveを分ける
② 承認ゲートを設ける
③ 仕様変更のルールを事前に決める

これだけで、後戻りがかなり減る。

みんなの現場では、どこでスコープが膨らむ？
```

| Risk Category | Level | Notes |
|---------------|-------|-------|
| Fabricated experience | low | Uses "気がする" and general observation. No specific false personal story. |
| Unsubstantiated claims | low | "8割" is qualified with "気がする". No absolute claims. |
| Effect guarantee | low | "後戻りがかなり減る" is directional, not guaranteed. |
| Fear-mongering | low | Problem is framed as common issue, not exaggerated threat. |
| Account type mismatch | low | Personal voice, reply/discussion CTA, matches account_type=personal. |
| CTA mismatch | low | CTA invites reply/discussion, matches desired_cta_style. |
| Product pushiness | low | Service is implied through expertise, not directly pitched. |
| Controversy risk | low | Neutral technical topic. |

**Overall: low risk. Pass.**

### Candidate 02: AIレビューフォーカス

```
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

| Risk Category | Level | Notes |
|---------------|-------|-------|
| Fabricated experience | low | Personal workflow described in general terms. |
| Unsubstantiated claims | low | "理想は理想" is balanced. |
| Effect guarantee | low | No guarantee stated. |
| Fear-mongering | low | Reasonable caution. |
| Account type mismatch | low | Personal voice. |
| CTA mismatch | low | Reply/discussion CTA. |
| Product pushiness | low | No direct service pitch. |
| Controversy risk | low | Technical topic. |

**Overall: low risk. Pass.**

### Candidate 03: MVP定義フォーカス

```
「まずMVPで」って言って始めたのに、気づいたら本開発化してる案件、多くない？

自分も何度かあって、原因はだいたい「MVPの定義が曖昧」なこと。

MVPは「テストしたい仮説を検証する最小限の機能」じゃないと、後から機能が増え続ける。

AIを使う時は特に、生成速度が速い分、方向性がずれるリスクも高い。

だから最初に「何を検証したいか」を紙1枚で固めるようになった。

MVPの定義、みんなどうしてる？
```

| Risk Category | Level | Notes |
|---------------|-------|-------|
| Fabricated experience | low | "自分も何度かあって" is vague but acceptable as personal reflection. |
| Unsubstantiated claims | low | Definition of MVP is standard. |
| Effect guarantee | low | No guarantee. |
| Fear-mongering | low | Common caution. |
| Account type mismatch | low | Personal voice. |
| CTA mismatch | low | Reply/discussion CTA. |
| Product pushiness | low | No direct pitch. |
| Controversy risk | low | Standard topic. |

**Overall: low risk. Pass.**

### Candidate 04: 技術負債フォーカス

```
短納期でAIにコードをガンガン書かせると、後で技術負債が増えるって話。

自分も「とりあえず動けばいい」で進めた案件で、3ヶ月後に苦しんだことがある。

今は短納期でも3つのことを徹底してる：
① レビュー基準を事前に決める
② テスト方針をMVP段階から入れる
③ リファクタリングの工数を見積もる

速さと品質、両立させるのは難しいけど、無理のない線引きができると楽になる。

短納期開発での品質担保、どうしてる？
```

| Risk Category | Level | Notes |
|---------------|-------|-------|
| Fabricated experience | medium | "3ヶ月後に苦しんだことがある" implies specific experience without details. Acceptable if kept vague. |
| Unsubstantiated claims | low | No absolute claims. |
| Effect guarantee | low | No guarantee. |
| Fear-mongering | low | Reasonable caution. |
| Account type mismatch | low | Personal voice. |
| CTA mismatch | low | Reply/discussion CTA. |
| Product pushiness | low | No direct pitch. |
| Controversy risk | low | Technical topic. |

**Overall: low risk. Pass with note: keep the anecdote vague.**

### Candidate 05: 仕様変更フォーカス

```
システム開発で「仕様は決まってる」と言われると、大概どこかで変更が入る。

AIを使った短納期開発だと、変更に対応する速度は速いけど、方向性がブレやすい。

自分がやってるのは、変更が来た時に必ず3つを確認すること：
① なぜ変更が必要か
② MVPの範囲に影響するか
③ 他の機能に波及しないか

これをAIに整理させて、人間が最終判断する。

仕様変更への対応、みんなのベストプラクティスがあれば聞きたい。
```

| Risk Category | Level | Notes |
|---------------|-------|-------|
| Fabricated experience | low | General workflow description. |
| Unsubstantiated claims | low | No absolute claims. |
| Effect guarantee | low | No guarantee. |
| Fear-mongering | low | Reasonable observation. |
| Account type mismatch | low | Personal voice. |
| CTA mismatch | low | Reply/discussion CTA. |
| Product pushiness | low | Service implied through workflow. |
| Controversy risk | low | Technical topic. |

**Overall: low risk. Pass.**

### Summary

All 5 candidates pass risk filter.
- Lowest risk: Candidate 01, 03, 05
- Slightly higher but acceptable: Candidate 02, 04

Recommended for final selection: Candidate 01 (要件整理フォーカス) due to strongest balance of low risk, broad appeal, and clear personal account fit.
