# Step 03: Skeleton Builder Input

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

## 感情マッピング結果

### 元構造の感情導線

| セクション | 主要感情 | 誘発する反応 |
|------------|----------|--------------|
| フック | 不安・関心 | 「これ、自分も当てはまるかも」 |
| 問題 | 共感・自己投影 | 「うちもそうだった」 |
| チェックリスト | 実用感・自己効力感 | 「後で確認したい」「保存」 |
| 解決方向性 | 信頼・期待 | 「この人に相談したい」 |
| CTA | 行動意欲 | 「資料請求/相談」 |

### 各感情の強度（1-5）

- 不安: 4
- 共感: 4
- 発見: 3
- 信頼: 4
- 期待: 3
- 行動意欲: 3

### 個人アカウント向け感情設計

#### 元の感情（corporate）

- 読者は「企業からのアドバイス」を受ける立場
- 感情の流れ: 不安 → 共感 → 信頼 → 行動

#### 転用後の感情（personal）

- 読者は「同じ現場で働く人/経験者」のような親近感
- 感情の流れ: 気づき → 共感 → 発見 → 参加欲（リプ）

### personal アカウントで強調すべき感情

1. **同じ目線の共感**
   - 「自分も経験した」という親近感
   - 法人投稿の「業界課題」→ 個人の「現場のあるある」

2. **発見の喜び**
   - 「こう考えればよかったのか」という気づき
   - チェックリストではなく「自分の気づき」を共有

3. **議論への参加欲**
   - 「あなたはどうしてる？」という問いかけ
   - 返信・体験共有を促す

### 避けるべき感情

- 押し付け感（「こうすべき」）
- 過度な不安喚起（炎上リスク）
- 企業宣伝感（商材を前面に出しすぎ）

### 感情キーワード

- 個人アカウントで使うと効果的な表現:
  - 「気づいたら」「最近思うんだけど」「現場でよくある」
  - 「どうしてる？」「教えてほしい」「自分はこうしてる」
  - 「びっくりした」「意外だった」「勉強になった」

### 感情の流れ（転用後）

```
[フック] 現場の小さな違和感や気づき
    ↓
[あるある] 同じ経験をした人がいることを示す
    ↓
[仮説] 個人の視点で考えを整理
    ↓
[軽い解決方向性] 実践的なヒント
    ↓
[CTA] 返信・議論・体験共有
```

### Risk Notes

- 個人の体験として語る際、架空の体験を断定的に述べない
- 「みんなこう」という一般化は避ける
- 感情を煽りすぎない（特に不安や怒り）
- 元投稿の構造は参考にしつつ、個人アカウントらしい謙虚さを保つ


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
