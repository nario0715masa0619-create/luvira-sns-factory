# Step 09: Market Judge Input

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

## Risk Filter Review

### Candidate 01: Weekend Routine Focus

```text
40代になって、高い靴より手入れしてる靴が大事だと気づいた。

自分がやってるのは3つ：
① 週1回ブラシでホコリを落とす
② 月1回クリームを塗る
③ 雨の日は翌日に乾拭きする

高い靴じゃなくても、手入れが行き届いてるだけで全然違う。

靴磨き、ちゃんとやってる人どれくらいいる？
```

| Risk Category | Level | Notes |
|---------------|-------|-------|
| Fabricated experience | low | 個人の習慣として語っており、架空の購入経験を断定的に述べていない。 |
| Unsubstantiated claims | low | 「大事だと気づいた」「変わる」は個人の体感。絶対的な主張ではない。 |
| Effect guarantee | low | 効果保証をしていない。 |
| Fear-mongering | low | 中立的。 |
| Account type mismatch | low | personalアカウント向けのトーン・一人称・CTA。 |
| CTA mismatch | low | 返信・共感を促すCTA。desired_cta_styleと一致。 |
| Product pushiness | low | 特定ブランドを推奨していない。 |
| Controversy risk | low | 中立的なライフスタイルテーマ。 |

**Overall: low risk. Pass.**

### Candidate 02: Before Meeting Focus

```text
40代、大事な会議の前に必ずやるようになったこと。

靴の手入れ。

① 出かける前にブラシ
② 週末にクリーム
③ 雨の日は乾拭き

高級靴じゃなくても、きれいな靴は信頼感が違う。

みんなは会議前、靴を確認する？
```

| Risk Category | Level | Notes |
|---------------|-------|-------|
| Fabricated experience | low | 個人のルーティンとして語っている。 |
| Unsubstantiated claims | low | 個人の体感。 |
| Effect guarantee | low | 効果保証なし。 |
| Fear-mongering | low | 中立的。 |
| Account type mismatch | low | personalアカウント向け。 |
| CTA mismatch | low | 返信・議論CTA。 |
| Product pushiness | low | 特定製品を推奨していない。 |
| Controversy risk | low | 一般的なビジネステーマ。 |

**Overall: low risk. Pass.**

### Candidate 03: Rain Day Focus

```text
40代になって気づいた。

雨で濡れた靴を放置してると、見た目がだいぶくたびれて見える。

やってるのは3つ：
① 帰宅したらすぐ乾拭き
② 翌朝ブラシをかける
③ 週1回クリーム

高い靴じゃなくても、手入れしてる靴の方がきれいに見える。

雨の日の靴の手入れ、やってる？
```

| Risk Category | Level | Notes |
|---------------|-------|-------|
| Fabricated experience | low | 個人の習慣として語っている。 |
| Unsubstantiated claims | low | 個人の体感。 |
| Effect guarantee | low | 効果保証なし。 |
| Fear-mongering | low | 中立的。 |
| Account type mismatch | low | personalアカウント向け。 |
| CTA mismatch | low | 返信・議論CTA。 |
| Product pushiness | low | 特定製品を推奨していない。 |
| Controversy risk | low | 中立的。 |

**Overall: low risk. Pass.**

### Candidate 04: Personal Realization Focus

```text
40代、靴にこだわり始めたと思ったら、
実は「手入れ」にこだわるようになってた。

① ブラシでホコリを落とす
② クリームを塗る
③ 雨の日は乾拭き

高い靴を買うより、持ってる靴を大事にする方が変わる。

同じ人いる？
```

| Risk Category | Level | Notes |
|---------------|-------|-------|
| Fabricated experience | low | 個人の変化として語っている。 |
| Unsubstantiated claims | low | 個人の体感。 |
| Effect guarantee | low | 効果保証なし。 |
| Fear-mongering | low | 中立的。 |
| Account type mismatch | low | personalアカウント向け。 |
| CTA mismatch | low | 返信・議論CTA。 |
| Product pushiness | low | 特定製品を推奨していない。 |
| Controversy risk | low | 中立的。 |

**Overall: low risk. Pass.**

### Candidate 05: Minimal Habit Focus

```text
40代、見た目を整えるのに高い服を買う必要はなかった。

週1回の靴の手入れだけで十分。

① ブラシ
② クリーム
③ 乾拭き

これだけで、仕事の印象も変わる。

みんなは靴の手入れ、何から始めた？
```

| Risk Category | Level | Notes |
|---------------|-------|-------|
| Fabricated experience | low | 個人の体感として語っている。 |
| Unsubstantiated claims | low | 個人の体感。 |
| Effect guarantee | low | 効果保証なし。 |
| Fear-mongering | low | 中立的。 |
| Account type mismatch | low | personalアカウント向け。 |
| CTA mismatch | low | 返信・議論CTA。 |
| Product pushiness | low | 特定製品を推奨していない。 |
| Controversy risk | low | 中立的。 |

**Overall: low risk. Pass.**

### Summary

All 5 candidates pass risk filter.
- Lowest risk: Candidate 01, 03, 04
- Slightly more business-oriented but acceptable: Candidate 02
- Slightly broad hook but acceptable: Candidate 05

Recommended for final selection: Candidate 01（週末ルーティンフォーカス） due to strongest balance of low risk, clear personal voice, and low-cost CTA.


## Prompt To Apply

Apply the following prompt to the Source Input above.

## Role

Market Judge（市場判定 AI）

## Objective

Risk Filter 通過後の候補を採点し、上位 5 本と最終おすすめ 1 本を選ぶ。

## Inputs

- リスク通過後の候補群
- 元構造分析
- 感情分類
- クライアントコンテキスト
- `account_type`: 投稿先アカウントの種別（`personal` / `corporate`）
- `desired_cta_style`: 希望 CTA スタイル
- 評価基準（インプレッション予測、ブランド適合度、パクリ感、共感度、`account_type` 適合性等）

## Process

1. `account_type` が未指定の場合は採点を行わず、人間に確認を求める。
2. 各候補を以下の観点で採点する：
   - インプレッション予測（1-5）
   - ブランド適合度（1-5）
   - パクリ感の少なさ（1-5）
   - 共感度（1-5）
   - フック力（1-5）
   - `account_type` 適合性（1-5）
3. `account_type` に応じた重み付けを行う。
   - `personal`: 共感・本音・リプ誘発・体験共有を加点要素とする。
   - `corporate`: 保存・信頼・問い合わせ導線・ノウハウ性を加点要素とする。
4. `account_type` と明らかに不一致な案は上位候補から除外する。
5. 合計点で上位 5 本を選ぶ。
6. 上位 5 本の中から最終おすすめ 1 本を選ぶ。
7. 各案の採点理由を簡潔に述べる。

## Output Format

```markdown
## 市場判定結果

### account_type
- account_type: [personal / corporate]
- desired_cta_style: [reply / experience_sharing / discussion / consultation / document_request / checklist]

### 採点基準
| 項目 | 満点 |
|------|------|
| インプレッション予測 | 5 |
| ブランド適合度 | 5 |
| パクリ感の少なさ | 5 |
| 共感度 | 5 |
| フック力 | 5 |
| account_type 適合性 | 5 |

### 各候補の採点
| 案 No | インプ | ブランド | パクリ感 | 共感 | フック | account_type | 合計 | 備考 |
|-------|--------|----------|----------|------|--------|--------------|------|------|
| 01 | 4 | 5 | 5 | 4 | 4 | 5 | 27 | ... |
| 02 | ... | ... | ... | ... | ... | ... | ... | ... |

### 上位 5 本
1. 案 [No]: [本文]
2. 案 [No]: [本文]
3. 案 [No]: [本文]
4. 案 [No]: [本文]
5. 案 [No]: [本文]

### 最終おすすめ 1 本
**案 [No]**
[本文]

**選定理由:**
[理由を 3 行以内]
```

## Do Not

- 自分の好みだけで選ばない。
- 根拠なき高評価をしない。
- リスク medium 以上の案を選ばない。
- ブランド適合度が低い案を最終おすすめにしない。
- `account_type` に合わない案を最終おすすめにしない。
- `account_type` 未指定のまま採点を進めない。

## Quality Criteria

- [ ] 各案に数値スコアが付いている
- [ ] 上位 5 本が明確
- [ ] 最終おすすめに理由がある
- [ ] ブランド適合度を重視している
- [ ] リスク通過案のみを対象としている
- [ ] `account_type` 適合性が評価されている


## Execution Instruction

1. Copy the entire content of this file (`step-09-market-judge-input.md`).
2. Paste it into Kimi/OpenCode as a new request.
3. Save the AI response to `step-09-market-judge.md` in the same run folder.
4. Review the output before proceeding to the next step.

> **Important:** This is a manual step. The script does not execute prompts, call APIs, or post automatically.
