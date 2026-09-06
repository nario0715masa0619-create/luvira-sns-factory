# Step 08: Risk Filter Input

## Run Metadata

- run_id: `20260906-1848-system-dev-corporate-to-personal`
- product_service: `AI活用型短納期システム開発`
- product_slug: `system-dev`
- source_account_type: `corporate`
- account_type: `personal`
- desired_cta_style: `reply / discussion / experience_sharing`
- allowed_persona_expression: `僕 / 私 / 自分 / 主語省略`
- risk_tolerance: `balanced`
- target_platform: `X`
- target_audience: `中小企業経営者 / 事業責任者 / システム開発を検討している担当者`
- business_goal: `AI活用型短納期システム開発への関心獲得`
- model: `kimi-k2.7-code`
- execution_mode: `file_based_semi_automation`
- status: `draft`
- current_step: `-`

## Source Input

The following content is the output from the previous step. Use it as the primary input for the next step.

## Similarity Guard Review

### Reviewed Candidates

All candidate drafts are based on the same source structure:
- corporate source structure: problem → oversight → checklist → solution direction → document request CTA
- Transformed into personal account style: insight → real-world example → hypothesis → light product connection → reply/discussion CTA

### Overall Similarity Risk: low

### Source Hook Retention: medium

- The original hook pattern "industry-wide pitfall" is retained but converted to personal language.
- Example: "失敗の8割は要件定義に起因してる気がする" keeps the "problem-first" hook but uses personal observation.

### Phrase Copy Risk: low

- No direct copying of the original corporate post phrases.
- All wording is rewritten in personal account voice.
- Technical terms (MVP, 要件定義, 承認ゲート) are generic industry terms, not original expressions.

### Structural Copy Risk: medium

- The overall structure (hook → problem → checklist/items → insight → CTA) is intentionally retained as the reusable framework.
- However, the tone, perspective, and CTA are significantly transformed.
- The structural similarity is acceptable because it is the intended transposition pattern.

### Per-Candidate Assessment

| Candidate | Hook Similarity | Phrase Copy | Structure Copy | Overall |
|-----------|-----------------|-------------|----------------|---------|
| 01 要件整理 | medium | low | medium | low |
| 02 AIレビュー | low | low | low | low |
| 03 MVP定義 | medium | low | medium | low |
| 04 技術負債 | low | low | low | low |
| 05 仕様変更 | low | low | low | low |

### Notes

- Candidates share the same structural DNA (problem-first + numbered list + CTA), which is the licensed framework.
- No candidate copies specific wording from the original corporate source.
- All candidates use personal voice and first-person observation.
- The transformation from "document request CTA" to "reply/discussion CTA" is maintained across all candidates.

### Recommendations

- All 5 candidates pass similarity review.
- To further reduce structural copy risk, consider varying the CTA phrasing or adding more unique personal anecdotes in final refinement.
- Avoid over-reliance on the "3 things" numbered list format in future runs; rotate with story-based or question-based formats.


## Prompt To Apply

Apply the following prompt to the Source Input above.

## Role

Risk Filter（リスクフィルタ AI）

## Objective

Similarity Guard 通過後の候補から、炎上、誇大広告、事実誤認、法務リスクをチェックする。

## Inputs

- Similarity Guard 通過後の候補
- クライアントの NG 表現・注意事項
- `account_type`: 投稿先アカウントの種別（`personal` / `corporate`）
- `risk_tolerance`: リスク許容度（`personal` / `corporate`）
- 業種特有の規制情報（医療、金融、景品表示法等）

## Process

1. `account_type` が未指定の場合は FAIL とし、人間に確認を求める。
2. 各候補を以下の観点でチェックする：
   - 誇大広告（絶対、最安、誰でも等）
   - 事実誤認（検証できない断定）
   - 炎上誘発（攻撃的、煽情的、分裂を促す表現）
   - 法務リスク（医療、金融、景品表示法、著作権、商標等）
   - クライアント NG 表現
    - `account_type` 別リスク
      - `personal`: 虚偽の実体験・確認不能な実績・過度な不安煽り・攻撃的表現を禁止
      - `corporate`: 保証表現・誇大表現・過度な煽り・一人称体験談・ブランド毀損リスクをより厳格に判定
       - `risk_tolerance=conservative` の場合はさらに以下を徹底する：
         - 根拠のない調査風表現（「当社の調査では」「弊社の実績では」「導入企業では」「多くの企業で」「業界では」等）は medium 以上とする。
   - `source_account_type` と `account_type` が異なる場合の追加リスク:
     - account_type 不適合リスク：変換先 `account_type` に合わない構造・CTA・フックが残っている場合は medium 以上とする。
     - 個人構造残存リスク：personal → corporate で失敗談構造・感情吐露・リプ誘導が残る場合は medium/high とする。
     - 企業版一人称体験リスク：「当社も」「当社でも」「弊社も」「弊社でも」が個人の「僕も」「私も」の置換として使われている場合は medium/high とする。
     - CTA不一致リスク：personalのリプ募集CTAがcorporateの資料請求・無料相談・チェックリストCTAに変換されていない場合は medium 以上とする。
      - 根拠不明な法人実績化リスク：個人の体験を「当社の事例」や「導入企業の例」のように法人実績化している場合は high とする。
      - 煽情表現・personal 由来表現リスク：「痛い目」「本番で気づく」「失敗してから」「放置すると危険」「取り返しがつかない」「今すぐやらないと」「あとでやると危ない」等が corporate + conservative に残る場合は medium 以上とする。効果保証に接続される場合は high とする。
        - personal 由来の失敗談・本音・反省表現（「僕も」「私も」「自分も」「失敗談」「後悔」等）が法人投稿に残る場合は medium 以上とする。
      - corporate → personal の追加リスク:
        - 確認不能な本人経験（「僕も経験した」「私も失敗した」「自分もやらかした」「うちでもあった」等）は high とする。
        - 確認不能な他社経験・伝聞（「個人的な話だけど」「知り合いの会社で」「友達の現場で」「前に見た現場で」「ある会社で」「以前相談を受けた」「実際にあった」「現場でよくある」等）は medium 以上とする。
        - 実在事例のように読める表現（具体的な会社名・人物・状況を示唆する表現）は medium 以上とする。
        - personal 向けでも、実績・相談実績・現場経験を匂わせる場合は人間確認必須とする。
        - 「〜かもしれない」「〜な気がする」「〜って意外と大事そう」などの仮説表現は OK 寄りとする。
        - ただし仮説表現でも、具体事例のように読める場合は要注意とする。
    - 根拠のない実績風表現は high とする。
    - 効果保証に見える表現（「防げます」「漏洩しません」「安心です」「解決します」等）は high とする。
    - 「リスク低減につながる」は OK 寄りだが、文脈によって要注意とする。
    - 「事故防止につながる」は効果保証に近くなる場合があるため要注意とする。
    - 投稿前に人間が根拠確認すべき表現を明示する。
3. リスクレベルを low / medium / high で判定する。
4. high の案は削除対象とする。
5. medium の案は修正提案を出す。

## Output Format

```markdown
## リスクチェック結果

### 判定基準
- low: 問題なし
- medium: 微修正推奨
- high: 削除必須

### account_type
- account_type: [personal / corporate]
- risk_tolerance: [personal / corporate]

### 各案の判定
| 案 No | リスク | 該当項目 | 理由 | 対応 |
|-------|--------|----------|------|------|
| 01 | low | - | ... | 採用可 |
| 02 | medium | 誇大広告 | ... | 「〜かもしれない」に変更 |
| 03 | high | 事実誤認 | ... | 削除 |

### 通過候補
#### 案 01
[通過後の本文]

#### 案 02（修正版）
[修正後の本文]
```

## Do Not

- 曖昧な表現をそのまま通さない。
- 医療・金融・景品表示法等の規制を無視しない。
- クライアントの NG 表現を見逃さない。
- 修正後に新たなリスクを生み出さない。
- `account_type` 未指定でリスク判定を進めない。
- `corporate` で一人称体験談を安易に通さない。
- `personal` で虚偽体験・捏造実績を通さない。
- `source_account_type` ≠ `account_type` の場合、個人構造の残存や単なる文体置換を安易に通さない。
- `risk_tolerance=conservative` の場合、煽情表現や personal 由来表現（「痛い目」「本番で気づく」「失敗してから」「放置すると危険」「取り返しがつかない」「今すぐやらないと」「あとでやると危ない」等）を安易に通さない。
- フックが強くても法人ブランド毀損の可能性がある場合は除外候補にする。
- `risk_tolerance=conservative` の場合、以下の表現を安易に通さない：
  - 調査風・実績風表現：「当社の調査では」「弊社の実績では」「導入企業では」「多くの企業で」「業界では」
  - 効果保証的表現：「必ず」「完全」「防げます」「漏洩しません」「安心です」「解決します」
  - 過度な効果示唆：「事故防止につながる」（文脈によっては high）
- corporate → personal の場合、以下の表現を安易に通さない：
  - 確認不能な本人経験：「僕も経験した」「私も失敗した」「自分もやらかした」「うちでもあった」
  - 確認不能な他社経験・伝聞：「個人的な話だけど」「知り合いの会社で」「友達の現場で」「前に見た現場で」「ある会社で」「以前相談を受けた」「実際にあった」「現場でよくある」
  - 実在事例のように読める表現（具体的な会社名・人物・状況を示唆する表現）
  - 仮説表現を装った具体事例（「〜かもしれない」と言いつつ、特定の状況を示唆する表現）

## Quality Criteria

- [ ] 各案のリスクレベルが明確
- [ ] high の案が削除されている
- [ ] medium の案に具体的な修正提案がある
- [ ] 誇大広告・事実誤認・法務リスクがチェックされている
- [ ] 修正後の案が新たなリスクを含まない
- [ ] `account_type` 別のリスク基準が適用されている
- [ ] `source_account_type` ≠ `account_type` の場合、個人構造残存・CTA不一致・法人実績化リスクをチェックしている
- [ ] corporate → personal の場合、確認不能な本人経験・他社経験・伝聞表現を high/medium で判定している
- [ ] corporate → personal の場合、実在事例のように読める表現を medium 以上で判定している
- [ ] corporate → personal の場合、仮説表現を装った具体事例を検出している
- [ ] `risk_tolerance=conservative` の場合、煽情表現・personal 由来表現が medium 以上で判定されている
- [ ] `risk_tolerance=conservative` の場合、根拠のない調査風・実績風表現が medium 以上で判定されている
- [ ] `risk_tolerance=conservative` の場合、効果保証に見える表現が high で判定されている
- [ ] フックが強くても法人ブランド毀損の可能性がある場合は除外候補にしている


## Execution Instruction

1. Copy the entire content of this file (`step-08-risk-filter-input.md`).
2. Paste it into Kimi/OpenCode as a new request.
3. Save the AI response to `step-08-risk-filter.md` in the same run folder.
4. Review the output before proceeding to the next step.

> **Important:** This is a manual step. The script does not execute prompts, call APIs, or post automatically.
