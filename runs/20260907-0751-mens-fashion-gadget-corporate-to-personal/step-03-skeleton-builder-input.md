# Step 03: Skeleton Builder Input

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

## Emotion Map

### Primary Emotion: Hope

- **Why it matters**: 40s men often feel they are past the age for fashion experimentation. The promise that small, inexpensive changes can improve appearance gives hope.
- **How to evoke**: Use phrases like "気づいたら」「整えるだけで」「高級品じゃなくても」.
- **Risk**: Avoid overpromising a dramatic transformation.

### Secondary Emotion: Discovery

- **Why it matters**: The audience enjoys learning practical, overlooked tips.
- **How to evoke**: Introduce small items or habits they may not have considered (e.g., cable management, gadget pouch, nail care).
- **Risk**: Avoid sounding like a product catalog.

### Secondary Emotion: Relief

- **Why it matters**: Many 40s men worry about needing expensive clothes or complex routines.
- **How to evoke**: Emphasize that being tidy is enough, not luxury.
- **Risk**: Avoid dismissing fashion entirely; maintain balance.

### Secondary Emotion: Empathy / Shared Experience

- **Why it matters**: The topic of appearance and aging is personal.
- **How to evoke**: Use first-person experience or rhetorical questions like "同じ人いる？」.
- **Risk**: Do not fabricate personal experience.

## Emotion → Post Element Mapping

| Emotion | Hook | Body | CTA |
|---------|------|------|-----|
| Hope | "服を買う前に、身の回りを整えるだけで変わる" | "高級品じゃなくても、清潔にまとまるだけで" | "まずは1つから試してみない？" |
| Discovery | "意外と見られてる小物" | List of overlooked items | "他にもある？" |
| Relief | "お金をかけなくても大丈夫" | Emphasize low-cost habits | "無理なく始められる" |
| Empathy | "40代、見た目に気を使い始めた" | Share relatable observation | "みんなどうしてる？" |

## Persona-Appropriate Tone

- Use modest, peer-to-peer language.
- Prefer 「自分」/「僕」 or subject-drop.
- Avoid commanding or preachy tone.
- Keep it conversational: as if chatting with a friend who has similar concerns.

## Forbidden Expressions

- "絶対に変わる" / "これをやれば成功する"
- "誰でもできる" (too generic)
- Specific brand recommendations without evidence
- Invented testimonials or experiences
- "保存しておけ" (corporate-style CTA)

## CTA Emotion

- Desired reaction: 保存したい / 真似したい / これ欲しい / 自分も整えたいと思う
- CTA style: reply / discussion / experience_sharing
- Example CTAs:
  - "みんなの必須小物、何？"
  - "40代の身だしなみ、何から整えた？"
  - "意外と効く小物、あったら教えて"


## Prompt To Apply

Apply the following prompt to the Source Input above.

## Role

Skeleton Builder（骨格作成 AI）

## Objective

Pattern Miner と Emotion Mapper の分析結果から、クライアント用に置換可能な「投稿骨格」を作成する。

## Inputs

- Pattern Miner の構造分析
- Emotion Mapper の感情分類
- クライアント商材・業種・ターゲット（簡易情報）

## Process

1. 構造分析からテンプレート化できる要素を抽出する。
2. 可変部分と固定部分を明確に分ける。
3. 各セクションの役割を簡潔に書く。
4. 感情導線を骨格に組み込む。
5. クライアントの商材・ターゲットに置換しやすい形にする。

## Output Format

```markdown
## 投稿骨格

### 前提
- 対象プラットフォーム:
- 想定文字数:
- 想定業種:

### 骨格テンプレート
```
[フック]: {読者の注意を引く問いかけまたは宣言}
[セクション 1]: {共感を誘発する導入}
[セクション 2]: {具体例・事例を 1 つ目}
[セクション 3]: {具体例・事例を 2 つ目}
[セクション 4]: {結論・メッセージ}
[CTA]: {読者に促す小さな行動}
```

### 可変部分
- {フックの対象}
- {具体例の内容}
- {CTA の内容}

### 固定部分
- セクションの順序
- 各セクションの役割
- 感情導線の流れ

### 感情導線
1. [感情 A]: [どのセクションで生まれるか]
2. [感情 B]: [どのセクションで生まれるか]
3. [感情 C]: [どのセクションで生まれるか]
```

## Do Not

- 具体的な商品名やキャンペーン名を勝手に入れない。
- 元投稿の固有名詞をそのまま使わない。
- 骨格を特定のクライアントに過度に寄せない。
- 元投稿の文章をコピーしない。

## Quality Criteria

- [ ] 可変部分と固定部分が明確
- [ ] 各セクションの役割が明確
- [ ] 感情導線が骨格に組み込まれている
- [ ] クライアント情報に置換しやすい
- [ ] 元投稿の文言を含まない


## Execution Instruction

1. Copy the entire content of this file (`step-03-skeleton-builder-input.md`).
2. Paste it into Kimi/OpenCode as a new request.
3. Save the AI response to `step-03-skeleton-builder.md` in the same run folder.
4. Review the output before proceeding to the next step.

> **Important:** This is a manual step. The script does not execute prompts, call APIs, or post automatically.
