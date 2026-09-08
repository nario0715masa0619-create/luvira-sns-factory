# Step 03: Skeleton Builder Input

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

## Emotion Map

### Primary Emotion: Empathy

- **Why it matters**: 40s men often feel pressure to upgrade their wardrobe with expensive items. The realization that simple shoe care is enough creates a shared relief.
- **How to evoke**: Use phrases like "気づいたら」「ちゃんと手入れしてるだけで」「高い靴じゃなくても」.
- **Risk**: Avoid sounding like "I know better than you."

### Secondary Emotion: Relief

- **Why it matters**: Many 40s men worry that looking good requires money.
- **How to evoke**: Emphasize that regular care, not expensive purchases, is enough.
- **Risk**: Avoid dismissing the value of quality shoes entirely.

### Secondary Emotion: Self-Efficacy

- **Why it matters**: The audience wants to feel they can improve their appearance.
- **How to evoke**: Show simple, specific actions that take little time.
- **Risk**: Avoid making it sound like too much work.

### Secondary Emotion: Discovery

- **Why it matters**: The audience enjoys learning small, overlooked tips.
- **How to evoke**: Introduce specific care habits they may not have considered.
- **Risk**: Avoid sounding like a manual.

## Emotion → Post Element Mapping

| Emotion | Hook | Body | CTA |
|---------|------|------|-----|
| Empathy | "40代になって気づいた" | "高い靴じゃなくても、手入れしてる靴の方が大事" | "同じ人いる？" |
| Relief | "お金をかけなくても大丈夫" | "週1回の小さな習慣だけで変わる" | "まずは1つからでいい？" |
| Self-Efficacy | "誰でもできる" | "ブラシ・クリーム・乾拭きの3つ" | "みんなはどうしてる？" |
| Discovery | "意外と見られてる靴" | 具体的な手入れ例 | "他にもある？" |

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
- "〜すべきだ" / "〜しなければならない" (lecturing tone)

## CTA Emotion

- Desired reaction: 共感 / 経験共有 / 保存
- CTA style: reply / discussion / experience_sharing
- Example CTAs:
  - "靴磨き、ちゃんとやってる人どれくらいいる？"
  - "同じ人いる？"
  - "みんなは週1回やってる？"
  - "雨の日の手入れ、やってる？"


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
