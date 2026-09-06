# Step 09: Market Judge Input

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

## Risk Filter Review

### Candidate 01: Gadget Focus

```text
40代、服を買う前にガジェット周りを整えたら印象変わった。

① ケーブルはポーチに1つにまとめる
② 財布は薄型にしてポケットの膨らみを消す
③ スマホケースは汚れを落とす

高級品じゃなくても、身の回りが整ってるだけで清潔に見える。

みんなの必須ガジェット小物、何かある？
```

| Risk Category | Level | Notes |
|---------------|-------|-------|
| Fabricated experience | low | 個人の体感として語っており、架空の購入経験を断定的に述べていない。 |
| Unsubstantiated claims | low | 「印象変わった」「清潔に見える」は個人の体感。 |
| Effect guarantee | low | 効果保証をしていない。 |
| Fear-mongering | low | 中立的。 |
| Account type mismatch | low | personalアカウント向けのトーン・CTA。 |
| CTA mismatch | low | 返信・議論を促すCTA。 |
| Product pushiness | low | 特定ブランドを推奨していない。 |
| Controversy risk | low | 中立的なライフスタイルテーマ。 |

**Overall: low risk. Pass.**

### Candidate 02: Grooming Focus

```text
40代、服より先に手入れを整えた方が変わると気づいた。

① 靴は週1回手入れ
② 爪は短く整える
③ 香りはボディソープと整髪料で統一

お金かけなくても、清潔感があれば十分。

40代男性の身だしなみ、何から整えた？
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
| Controversy risk | low | 一般的な身だしなみテーマ。 |

**Overall: low risk. Pass.**

### Candidate 03: Wallet / Bag Focus

```text
40代、バッグの中身を整えたら自信が出てきた。

① 長財布から薄型財布へ
② 鍵はキーケースで静かに
③ ガジェットポーチでケーブルごちゃごちゃを防ぐ

中身が整うと、外見も整って見える。

バッグの中身、何をこだわってる？
```

| Risk Category | Level | Notes |
|---------------|-------|-------|
| Fabricated experience | low | 個人の体感として語っている。 |
| Unsubstantiated claims | low | 「外見も整って見える」は個人の体感。 |
| Effect guarantee | low | 効果保証なし。 |
| Fear-mongering | low | 中立的。 |
| Account type mismatch | low | personalアカウント向け。 |
| CTA mismatch | low | 返信・議論CTA。 |
| Product pushiness | low | 特定ブランドを推奨していない。 |
| Controversy risk | low | 中立的。 |

**Overall: low risk. Pass.**

### Candidate 04: Combined Small Habits

```text
40代、小物と清潔感を整えるだけで若作りじゃなく見えるようになった。

① イヤホンはワイヤレスに
② 財布は薄く
③ 靴は手入れ

高級品じゃなくても、整ってるかどうか。

40代で整えてよかった小物、何？
```

| Risk Category | Level | Notes |
|---------------|-------|-------|
| Fabricated experience | low | 個人の変化として語っている。 |
| Unsubstantiated claims | low | 個人の体感。 |
| Effect guarantee | low | 効果保証なし。 |
| Fear-mongering | low | 若作りへの不安に寄り添いすぎない。 |
| Account type mismatch | low | personalアカウント向け。 |
| CTA mismatch | low | 返信・議論CTA。 |
| Product pushiness | low | 特定製品を推奨していない。 |
| Controversy risk | low | 中立的。 |

**Overall: low risk. Pass.**

### Candidate 05: Before / After Realization

```text
40代、服を買い足す前にやるべきこと。

身の回りの小物と清潔感を整えるだけで、鏡を見るのが嫌じゃなくなった。

特に効いたのは：
① ガジェットポーチ
② 薄型財布
③ 靴の手入れ

まずは買わずに整えてみる。

みんなはどこから始めた？
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

### Summary

All 5 candidates pass risk filter.
- Lowest risk: all candidates
- Recommended for final selection: Candidate 03（バッグの中身フォーカス） due to emotional hook, clear items, and strong personal account fit.


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
