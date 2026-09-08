# Step 02: Emotion Mapper Input

## Run Metadata

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
- status: `draft`
- current_step: `-`

## Source Input

The following content is the output from the previous step. Use it as the primary input for the next step.

## Structure Pattern

### Source Post Structure

```
フック（40代になって、高い靴よりちゃんと手入れしてる靴が大事だと気づいた）
  → テーマ提示（靴の手入れは週1回の小さな習慣）
  → 3つの具体的手入れ例（ブラシ・クリーム・乾拭き）
  → 価値転換（高級靴じゃなくても清潔感があれば十分）
  → CTA（共感・経験共有型の問いかけ）
```

### Observed Elements

1. **Hook**: Personal realization framing — "I noticed as a 40-something man." Low barrier, relatable.
2. **Theme**: Shoe care as a small weekly habit, not a big purchase.
3. **Concrete list**: 3 simple care examples (brush, cream, dry wipe).
4. **Value shift**: Expensive shoes matter less than well-maintained shoes.
5. **CTA**: Empathy/discussion prompt — easy yes/no or short reply.

### Reusable Framework

- **Pattern name**: "Small care habit beats expensive purchase"
- **Applicable when**: Target audience wants to look better without overspending.
- **Template**:
  1. Hook: personal realization about an overlooked habit
  2. Theme: this small habit is enough
  3. 3 concrete examples
  4. Insight: cleanliness/maintenance > luxury
  5. CTA: low-cost empathy question

## Emotion Drivers

### Primary Emotion

- **Empathy**: "I also thought I needed expensive shoes."

### Secondary Emotions

- **Relief**: "I don't need to buy expensive shoes."
- **Discovery**: "Simple care makes a difference."
- **Self-efficacy**: "I can do this."

### Engagement Driver

- The post offers a low-cost, actionable habit that feels immediately doable.

## Product-Specific Notes

- product_service: 40代男性向けファッション・ガジェット情報発信
- product_slug: mens-fashion-gadget
- source_account_type: corporate
- account_type: personal
- The source is corporate / media-style; the target is personal.
- Key items: shoe brush, shoe cream, dry wipe after rain.
- Value proposition: "well-maintained shoes beat expensive shoes."

## Risk Notes

- Do not save or copy the original corporate post text.
- Avoid sounding like a lecture or advice column.
- Avoid guaranteeing specific results.
- Avoid implying invented personal experience.
- Keep CTA aligned with personal account style (reply/discussion, not follow/purchase).
- Keep tone peer-to-peer, not instructor-like.


## Prompt To Apply

Apply the following prompt to the Source Input above.

## Role

Emotion Mapper（感情分類 AI）

## Objective

Pattern Miner が抽出した構造をもとに、その投稿が何の感情・行動ドライバーで伸びたかを分類する。

## Inputs

- Pattern Miner の構造分析
- 元バズ投稿（全文）
- `account_type`: 転用先アカウントの種別（`personal` / `corporate`）
- いいね・リプ・保存・シェアの傾向（あれば）

## Process

1. 構造の各セクションが読者に与える感情を特定する。
2. 以下の観点で分類する：保存・共感・議論・意外性・覚悟表明・UGC。
3. 主要な感情ドライバーを 1〜3 個選ぶ。
4. 読者心理の遷移を時系列で整理する。
5. 各感情がどのセクションで最も強く生まれているかを記録する。
6. `account_type` に適した反応設計かどうかを評価する。
   - `personal`: 共感・議論・本音・体験共有を重視。
   - `corporate`: 保存・信頼・問い合わせ導線・ノウハウ性を重視。
7. `account_type` に対して不自然な感情導線があれば警告する。

## Output Format

```markdown
## 感情マッピング

### account_type 適合性
- account_type: [personal / corporate]
- 適合する反応設計: [personal なら共感/議論/UGC、corporate なら保存/信頼/問い合わせ導線]
- 不自然な点（あれば）: [3 行以内]

### 感情ドライバー分類
| 分類 | 該当するセクション | 強度（1-5） | 理由 |
|------|---------------------|-------------|------|
| 保存 | ... | ... | ... |
| 共感 | ... | ... | ... |
| 議論 | ... | ... | ... |
| 意外性 | ... | ... | ... |
| 覚悟表明 | ... | ... | ... |
| UGC | ... | ... | ... |

### 主要ドライバー（1-3 個）
1. [ドライバー名]: [理由]

### 読者心理の遷移
1. [最初の感情]
2. [中盤の感情]
3. [最後の感情/行動]

### 感情コメント
[補足説明があれば 3 行以内]
```

## Do Not

- 数値の根拠なき拡大解釈をしない。
- 元投稿の感情を過剰に美化しない。
- 推測を断定で書かない。
- クライアント情報をここでは扱わない。
- `account_type` 未指定のまま感情評価を進めない。

## Quality Criteria

- [ ] 各感情がどのセクションで生まれているか明確
- [ ] 主要ドライバーの選択に理由がある
- [ ] 読者心理の遷移が自然である
- [ ] 強度は 1-5 の数値で示されている
- [ ] 元投稿の内容を再現せず、分析のみを行っている
- [ ] `account_type` に適した反応設計か評価されている


## Execution Instruction

1. Copy the entire content of this file (`step-02-emotion-mapper-input.md`).
2. Paste it into Kimi/OpenCode as a new request.
3. Save the AI response to `step-02-emotion-mapper.md` in the same run folder.
4. Review the output before proceeding to the next step.

> **Important:** This is a manual step. The script does not execute prompts, call APIs, or post automatically.
