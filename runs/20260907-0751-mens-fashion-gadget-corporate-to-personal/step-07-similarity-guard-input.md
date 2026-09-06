# Step 07: Similarity Guard Input

## Run Metadata

- run_id: `20260907-0751-mens-fashion-gadget-corporate-to-personal`
- product_service: `40代男性向けファッション・ガジェット情報発信`
- product_slug: `mens-fashion-gadget`
- source_account_type: `corporate`
- account_type: `personal`
- desired_cta_style: `reply / discussion / experience_sharing`
- allowed_persona_expression: `僕 / 私 / 自分 / 主語省略`
- risk_tolerance: `balanced`
- target_platform: `X`
- target_audience: `40代男性 / 経営者 / 個人事業主 / 営業職 / 見た目と仕事道具を整えたい人`
- business_goal: `40代男性向けファッション×ガジェット投稿の反応獲得`
- model: `kimi-k2.7-code`
- execution_mode: `file_based_semi_automation`
- status: `draft`
- current_step: `-`

## Source Input

The following content is the output from the previous step. Use it as the primary input for the next step.

## Hook Specialist Review

### Candidate 01: Gadget Focus

**Original Hook**: 40代、服を買う前にガジェット周りを整えたら印象変わった。

**Hook Strengths**:
- Clear premise: buying clothes vs. tidying gadgets
- Specific domain
- Personal realization tone

**Suggested Hook Variations**:
- "40代、服より先にガジェット周りを整えた方が印象変わった。"
- "40代男性の見た目、意外とガジェット小物が左右してる。"

**Recommended Hook**: "40代、服を買う前にガジェット周りを整えた方が印象変わった。"

---

### Candidate 02: Grooming Focus

**Original Hook**: 40代、服より先に手入れを整えた方が変わると気づいた。

**Hook Strengths**:
- Strong value shift (clothes vs. grooming)
- Broadly relatable

**Suggested Hook Variations**:
- "40代、ファッションより清潔感を整えた方が変わる。"
- "40代男性の見た目、服より手入れが効く。"

**Recommended Hook**: "40代、服より先に手入れを整えた方が変わると気づいた。"

---

### Candidate 03: Wallet / Bag Focus

**Original Hook**: 40代、バッグの中身を整えたら自信が出てきた。

**Hook Strengths**:
- Connects internal state (confidence) to external order
- Curiosity about bag contents

**Suggested Hook Variations**:
- "40代、バッグの中身を整えたら仕事の印象も変わった。"
- "40代男性のバッグの中身、見直すと意外といいことある。"

**Recommended Hook**: "40代、バッグの中身を整えたら自信が出てきた。"

---

### Candidate 04: Combined Small Habits

**Original Hook**: 40代、小物と清潔感を整えるだけで若作りじゃなく見えるようになった。

**Hook Strengths**:
- Addresses fear of looking try-hard
- Promises natural improvement

**Suggested Hook Variations**:
- "40代、若作りせずに見た目を整える方法。"
- "40代、小物を整えるだけで清潔に見える。"

**Recommended Hook**: "40代、小物と清潔感を整えるだけで若作りじゃなく見えるようになった。"

---

### Candidate 05: Before / After Realization

**Original Hook**: 40代、服を買い足す前にやるべきこと。

**Hook Strengths**:
- Direct "must-do" framing
- Creates curiosity

**Suggested Hook Variations**:
- "40代、服を買う前にやるべき3つのこと。"
- "40代、もっと服を買う前に整えたいこと。"

**Recommended Hook**: "40代、服を買い足す前にやるべきこと。"

---

## Top Hook Recommendations

1. **Candidate 03**: "40代、バッグの中身を整えたら自信が出てきた。" — emotional + practical
2. **Candidate 01**: "40代、服を買う前にガジェット周りを整えた方が印象変わった。" — clear angle
3. **Candidate 04**: "40代、小物と清潔感を整えるだけで若作りじゃなく見えるようになった。" — addresses insecurity

## Final Hook Decision

Use **Candidate 03 hook** as the strongest opener for the final package:

```text
40代、バッグの中身を整えたら自信が出てきた。
```

This hook connects emotional benefit (confidence) to a concrete action (organizing bag contents), which is highly engaging for the target audience.


## Prompt To Apply

Apply the following prompt to the Source Input above.

## Role

Similarity Guard（類似性監視 AI）

## Objective

生成案が元バズ投稿に似すぎていないかをチェックする。

## Inputs

- 元バズ投稿（全文）
- フック強化済みの 20〜50 案
- `account_type`: 投稿先アカウントの種別（`personal` / `corporate`）
- `source_account_type`: 元投稿アカウントの種別（`personal` / `corporate`）

## Process

1. `account_type` または `source_account_type` が未指定の場合は判定を行わず、人間に確認を求める。
2. 元投稿と各生成案を比較する。
3. 以下を共通してチェックする：
   - 固有名詞の転用
   - 独自表現・キャッチコピーの転用
   - 文章の連続した一致
   - 独自の事例やデータの転用
4. `account_type` に応じた追加チェックを行う。
   - `personal` の場合:
     - 本音感・体験談・問いかけは許容する。
     - ただし、元投稿と同じ失敗談構造、同じ語尾、同じ決め台詞、同じ比喩が残っている場合は medium/high と判定する。
     - 「個人っぽいから OK」として類似性を見逃さない。
    - `corporate` の場合:
      - 表現の重複、構成の近似、CTA の近似をより厳しく見る。
      - 企業公式として、元投稿の個人体験構造をそのまま使っている場合は high と判定する。
      - 企業投稿として不自然な一人称体験談が残っている場合は FAIL（high）とする。
      - source_account_type=corporate / account_type=corporate の場合でも、「法人投稿だから類似性が許容される」とはしない。
      - 元投稿と同じチェック項目の並びが残っている場合は medium 以上とする。
      - 元投稿の締め文・決め台詞・CTA の流れが似ている場合は medium 以上とする。
      - 「小さな〇〇が大きな〇〇に」系の抽象締めが元投稿に近い場合は medium/high とする。
       - 表現が安全でも、構造が元投稿に近すぎる場合は警告する。
   - `source_account_type` と `account_type` が異なる場合の追加チェック:
     - personal → corporate で、元投稿の失敗談構造（個人の失敗→気づき→問いかけ）が残っている場合は medium 以上とする。
     - 「当社も」「当社でも」「弊社も」「弊社でも」が、元投稿の「僕も」「私も」「自分も」の単なる置換として使われている場合は medium/high とする。
     - 元投稿の問いかけCTA（「皆さんはどうですか？」等）が法人CTAに変換されていない場合は medium 以上とする。
     - 元投稿の感情フック（「自分も見落としていた」「失敗して気づいた」等）が実務フック（「見落とされやすい」「棚卸ししておきたい」等）に変換されていない場合は medium 以上とする。
      - corporate として表現が安全でも、personal 由来の構造（失敗談→共感→リプ誘導）が残る場合は警告する。
      - 元投稿の冒頭フックと同じ問題提起順序（後回し → 失敗談 → 気づき → 教訓）の場合は medium 以上とする。
      - 「痛い目」「本番で」「失敗して気づいた」「あとでやる」などの personal 由来表現が残る場合は medium 以上とする。
      - personal → corporate で「見落とし」「後回し」だけに置換して、構造が元投稿と同じ場合は medium 以上とする。
       - corporate→corporate 結果の最終案とほぼ同じ構成に収束している場合は medium 以上とする。
       - 「3 つの観点」型が連続して出る場合は、類似ではなく多様性不足として警告する。
      - corporate → personal の追加チェック:
        - 元投稿の「3 つ」「3 点」「チェック項目」構造がそのまま残る場合は medium 以上とする。
        - 10 案中「3 つの〜」型が多すぎる場合は、類似ではなく多様性不足として警告する。
        - 「個人的な話だけど」「知り合いの会社で」「友達の現場で」「前に見た現場で」「ある会社で」「以前相談を受けた」「実際にあった」「現場でよくある」など、本人経験・他社経験・伝聞を匂わせる表現は medium 以上とする。
        - 架空実体験ではなくても、根拠不明の経験談・具体事例に見える場合は警告する。
        - corporate 由来の資料請求CTAがリプ/議論/経験共有CTAに変換されていない場合は medium 以上とする。
        - personal 投稿として自然でも、法人投稿の骨格（課題提示→チェック項目→機能説明→CTA）が残りすぎている場合は medium 以上とする。
5. 以下の観点も追加でチェックする：
   - `account_type` 適合性
   - `source_account_type` との整合性
   - 個人/法人変換時の構造残りすぎリスク
   - CTA 類似リスク
   - 決め台詞・締め文の類似リスク
6. 類似度リスクを low / medium / high で評価する。
7. high の案は修正指示を出す。
8. medium の案は注意事項を出す。

## Output Format

```markdown
## 類似性チェック結果

### 判定基準
- low: 構造のみ類似。問題なし。
- medium: 一部表現が気になる。要確認。
- high: 元投稿に酷似。修正必須。

### account_type
- account_type: [personal / corporate]
- source_account_type: [personal / corporate]
- 変換時の構造残りすぎリスク: [low / medium / high]

### 各案の判定
| 案 No | リスク | account_type 適合性 | 該当項目 | 理由 | 修正指示 |
|-------|--------|----------------------|----------|------|----------|
| 01 | low | 適合 | - | ... | なし |
| 02 | medium | やや不適合 | CTA 類似 | ... | ... |
| 03 | high | 不適合 | 構造残りすぎ | ... | ... |

### 修正後案（high のみ）
#### 案 03（修正版）
[修正後の投稿本文]
```

## Do Not

- 構造の類似を問題視しない。
- 文言・固有名詞・独自表現のコピーを見逃さない。
- 曖昧な判定をしない。
- 修正後の案で元投稿の表現を流用しない。
- `account_type` 未指定で判定を進めない。
- `corporate` 向け案で個人体験構造をそのまま通さない。
- `personal` 向け案で「個人っぽいから OK」として類似を見逃さない。
- `corporate` 同士のケースで「法人投稿だから類似性が許容される」と甘く見ない。
- `source_account_type` ≠ `account_type` の場合、単なる文体置換（例：「僕も」→「当社も」）を類似性の対象外として扱わない。
- personal → corporate で、失敗談構造や問いかけCTAがそのまま残っている場合を見逃さない。
- 元投稿の冒頭フックや personal 由来表現（「痛い目」「本番で」「失敗して気づいた」「あとでやる」等）を見逃さない。
- personal → corporate で「見落とし」「後回し」だけを置換して構造が同じ場合を見逃さない。
- corporate→corporate 結果への単純収束を類似性の対象外として扱わない。
- 「3 つの観点」型の多様性不足を見逃さない。
- corporate → personal で「3 つ」「3 点」「チェック項目」型のリスト構造残留を見逃さない。
- corporate → personal で「個人的な話だけど」「知り合いの会社で」「友達の現場で」「前に見た現場で」「ある会社で」「以前相談を受けた」「実際にあった」「現場でよくある」などの体験・伝聞匂わせ表現を見逃さない。
- corporate → personal で、法人投稿の骨格（課題提示→チェック項目→機能説明→CTA）がそのまま残っている場合を見逃さない。
- corporate → personal で、資料請求CTAがリプ/議論/経験共有CTAに変換されていない場合を見逃さない。
- 元投稿の締め文・決め台詞・CTA の流れが似ている場合を見逃さない。

## Quality Criteria

- [ ] 各案のリスクが low/medium/high で明確に判定されている
- [ ] high の案に具体的な修正指示が出ている
- [ ] 構造の類似は誤判定していない
- [ ] 元投稿の文言コピーが見つかっている
- [ ] 修正後の案が元投稿と明確に異なる
- [ ] `account_type` 適合性が判定されている
- [ ] `source_account_type` との整合性が確認されている
- [ ] `source_account_type` ≠ `account_type` の場合、個人構造・問いかけCTA・感情フックの残存を検出している
- [ ] `source_account_type` ≠ `account_type` の場合、元フック酷似・personal 由来表現・構造の単純置換・corporate→corporate 収束を検出している
- [ ] corporate → personal の場合、「3 つ」「3 点」「チェック項目」型のリスト構造残留を検出している
- [ ] corporate → personal の場合、本人経験・他社経験・伝聞を匂わせる表現を検出している
- [ ] corporate → personal の場合、資料請求CTAがリプ/議論/経験共有CTAに変換されているか確認している
- [ ] corporate → personal の場合、法人投稿の骨格（課題提示→チェック項目→機能説明→CTA）が残りすぎていないか判定している
- [ ] `corporate` 同士のケースでも、締め文・決め台詞・CTA の流れの類似を見逃していない
- [ ] 「小さな〇〇が大きな〇〇に」系の抽象締めの類似を適切に判定している
- [ ] 方向性の多様性不足（「3 つの観点」型の連続等）を警告している


## Execution Instruction

1. Copy the entire content of this file (`step-07-similarity-guard-input.md`).
2. Paste it into Kimi/OpenCode as a new request.
3. Save the AI response to `step-07-similarity-guard.md` in the same run folder.
4. Review the output before proceeding to the next step.

> **Important:** This is a manual step. The script does not execute prompts, call APIs, or post automatically.
