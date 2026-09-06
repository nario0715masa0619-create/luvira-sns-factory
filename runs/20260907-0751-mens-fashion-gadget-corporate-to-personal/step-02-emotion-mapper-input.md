# Step 02: Emotion Mapper Input

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

## Structure Pattern

### Source Post Structure

```
フック（身の回りを整えるだけで印象が変わる）
  → テーマ提示（服を買い足す前に小物・清潔感を整える）
  → 具体例リスト（靴・財布・ケーブル・イヤホン・ポーチ・スマホケース・爪・髪・香り）
  → 価値転換（高級品ではなく、整って見えること）
  → CTA（保存/フォロー）
```

### Observed Elements

1. **Hook**: A relatable, low-barrier promise — "small grooming/gadget habits change how you look."
2. **Theme**: Before buying more clothes, organize the small items and cleanliness around you.
3. **Concrete list**: 3–5 examples from the domain (shoes, wallet, cables, earphones, pouch, phone case, nails, hair, scent).
4. **Value shift**: Reassurance that expensive items are not required; being tidy is enough.
5. **CTA**: Save / follow / bookmark.

### Reusable Framework

- **Pattern name**: "Before buying more, tidy what you have"
- **Applicable when**: Target audience is 40s men who want to improve appearance without overspending.
- **Template**:
  1. Hook: small habit → visible change
  2. Theme: before adding clothes, organize small items / grooming
  3. 3 concrete examples
  4. Insight: cleanliness > luxury
  5. CTA: save/follow/discuss

## Emotion Drivers

### Primary Emotion

- **Hope**: "I can look better without a big purchase."

### Secondary Emotions

- **Discovery**: "I hadn't thought of these small items."
- **Relief**: "I don't need expensive clothes."
- **Empathy**: "Other 40s men struggle with this too."

### Engagement Driver

- The post gives an easy, low-cost action list that feels immediately doable.

## Product-Specific Notes

- product_service: 40代男性向けファッション・ガジェット情報発信
- product_slug: mens-fashion-gadget
- source_account_type: corporate
- account_type: personal
- The source is corporate / media-style; the target is personal.
- Key items: shoes care, slim wallet, cable management, wireless earphones, gadget pouch, phone case, nails, hair, scent.
- Value proposition: "look put-together without luxury items."

## Risk Notes

- Do not save or copy the original corporate post text.
- Avoid guaranteeing specific results (e.g., "sales will increase").
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
