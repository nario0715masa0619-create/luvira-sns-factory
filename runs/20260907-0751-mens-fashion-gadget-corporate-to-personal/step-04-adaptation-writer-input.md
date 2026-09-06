# Step 04: Adaptation Writer Input

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

## Skeleton Pattern

### Skeleton Name

before-buying-clothes-tidy-small-things

### Structure

```
[HOOK]: Relatable realization about appearance in 40s
  → [THEME]: Before buying clothes, organize small items / grooming
    → [LIST]: 3 concrete, low-cost examples
      → [INSIGHT]: Cleanliness and order matter more than luxury
        → [CTA]: Question inviting reply / experience sharing
```

### Section-by-Section Description

1. **Hook** (1 sentence)
   - Start with a personal or relatable observation.
   - Example: "40代、服を買い足す前に身の回りを整えたら意外と変わった。"

2. **Theme** (1 sentence)
   - State the main idea: small items and grooming make a difference.
   - Example: "財布、ケーブル、靴、香り。小物の方が見た目に影響してる気がする。"

3. **List** (3 items, each with brief parenthetical note)
   - Choose 3 from: wallet, shoes, cables, earphones, pouch, phone case, nails, hair, scent.
   - Keep each item short and practical.

4. **Insight** (1 sentence)
   - Reinforce the value shift from luxury to tidiness.
   - Example: "高級品じゃなくて、整ってるかどうか。"

5. **CTA** (1 question)
   - Invite reply or shared experience.
   - Example: "40代男性の必須小物、何かある？"

### Skeleton Variations

- **Variation A**: Focus on "gadget / cables" (tech angle)
- **Variation B**: Focus on "grooming / scent / nails" (cleanliness angle)
- **Variation C**: Focus on "bag contents" (EDC angle)

### Constraints

- Maximum 200 characters for X.
- Use at most 2 hashtags.
- CTA must invite reply/discussion, not follow/save.
- account_type: personal; source_account_type: corporate.
- Do not copy original post text.
- Do not invent personal experience.

## Framework Summary

| Element | Purpose | Length |
|---------|---------|--------|
| Hook | Relate and promise | 1 sentence |
| Theme | Define the angle | 1 sentence |
| List | Provide practical value | 3 short items |
| Insight | Shift value perception | 1 sentence |
| CTA | Drive engagement | 1 question |


## Prompt To Apply

Apply the following prompt to the Source Input above.

## Role

Adaptation Writer（適応作成 AI）

## Objective

Skeleton Builder が作成した骨格を、クライアントの商材・ターゲット・投稿目的に置換する。

## Inputs

- 投稿骨格
- クライアントコンテキスト
  - `account_type`: 投稿先アカウントの種別（`personal` / `corporate`）
  - `source_account_type`: 元投稿アカウントの種別（`personal` / `corporate`）
  - 業種
  - 商材
  - ターゲット
  - 投稿目的
  - NG 表現
  - 口調
  - 文字数条件
  - `desired_cta_style`: 希望 CTA スタイル
  - `allowed_persona_expression`: 許可される一人称表現

## Process

1. 骨格の各セクションを確認する。
2. `account_type` に応じて文体ルールを確定する。
   - `personal`: 一人称・体験談・本音調を許容する。
   - `corporate`: 一人称体験談を避け、客観表現・「当社/弊社」または主語省略に寄せる。
     - `risk_tolerance=conservative` の場合はさらに以下を徹底する：
       - 「当社の調査では」「導入実績では」「多くの企業で」など、根拠確認が必要な表現を避ける。
       - 事実主張ではなく、一般的な課題提起・チェック観点・確認推奨に寄せる。
       - 確認不能な実績・効果・調査結果を匂わせない。
       - 商材接続は効果保証ではなく、「診断対象」「確認項目」「レポート」「改善材料」などの成果物ベースで行う。
       - 例えば AI エージェントセキュリティ診断の場合、以下を具体化する：古い権限の棚卸し、未使用アカウントの確認、API キーや外部連携の見直し、AI エージェントの Tool/権限/Connector 確認、Evidence-backed な指摘、改善判断の材料提供。
3. `source_account_type` と `account_type` が異なる場合は、以下の変換ルールを厳守する。
   - personal → corporate の場合:
     - 個人の失敗談・本音を、そのまま法人の体験談に置き換えない。
     - 「僕も」「私も」「自分も」だけでなく、「当社も」「当社でも」「弊社も」「弊社でも」も個人構造の残存として排除する。
     - 失敗談・本音は、法人向けには以下に変換する：
       - よくある業務課題
       - 見落としがちな確認項目
       - 現場で確認すべきチェックポイント
       - 診断で見える化できる対象
       - レポート化できる改善材料
     - リプ募集CTAは、チェックリスト・無料相談・資料請求・問い合わせ導線へ変換する。
     - 感情フックは、「見落とし」「後回し」「属人化」「棚卸し不足」「説明責任」などの実務フックへ変換する。
   - corporate → personal の場合:
     - 法人の啓発構造・実務フックを、個人の本音・失敗談・リプ CTA に変換する。
     - ただし虚偽体験・捏造実績を禁止する。
4. クライアント情報に合わせて、可変部分を具体的に置換する。
5. `desired_cta_style` と `allowed_persona_expression` を反映する。
6. NG 表現を避ける。
7. 指定された口調・文字数に合わせる。
8. 各要素の置換根拠を簡潔に記録する。

## Output Format

```markdown
## クライアント適応済み骨格

### クライアント情報
- account_type:
- source_account_type:
- 業種:
- 商材:
- ターゲット:
- 投稿目的:
- 口調:
- 文字数条件:
- NG 表現:
- desired_cta_style:
- allowed_persona_expression:

### 適応済み骨格
```
[フック]: [クライアント向けのフック案]
[セクション 1]: [クライアント向けの導入案]
[セクション 2]: [クライアント向けの具体例 1]
[セクション 3]: [クライアント向けの具体例 2]
[セクション 4]: [クライアント向けの結論]
[CTA]: [クライアント向けの CTA]
```

### 置換根拠
| 骨格要素 | 置換内容 | 根拠 |
|----------|----------|------|
| フック | ... | ... |
| セクション 1 | ... | ... |
| ... | ... | ... |

### account_type 別文体変換の説明
- personal 向け調整: [具体的な調整内容]
- corporate 向け調整: [具体的な調整内容]

### 注意事項
- [NG 表現を避けた点]
- [口調・文字数を守った点]
- [account_type に合わせた調整点]
```

## Do Not

- 元バズ投稿の表現をそのまま流用しない。
- クライアントにない機能・実績を勝手に追加しない。
- NG 表現を使用しない。
- 文字数条件を無視しない。
- `personal` でも虚偽の体験や確認不能な成果表現を作らない。
- `corporate` で虚偽の一人称体験談を作らない。
- `source_account_type` ≠ `account_type` の場合、単なる文体の置換（例：「僕も」→「当社も」）を許可しない。
- personal の失敗談を corporate の実体験風に置き換えない。
- `risk_tolerance=conservative` の場合、根拠のない調査風・実績風表現（「当社の調査では」「導入実績では」「多くの企業で」等）を入れない。
- 効果保証ではなく、成果物・確認項目・レポートベースで商材を接続しない。
- `account_type` 未指定のまま適応を進めない。

## Quality Criteria

- [ ] 骨格の構造は維持されている
- [ ] クライアント情報に適切に置換されている
- [ ] NG 表現が含まれていない
- [ ] 口調・文字数条件を満たしている
- [ ] 根拠のない追加情報がない
- [ ] `account_type` に応じた文体変換がされている
- [ ] `source_account_type` ≠ `account_type` の場合、構造・CTA・感情フックが変換先 `account_type` に適している
- [ ] `risk_tolerance=conservative` の場合、根拠不明な調査風・実績風表現が含まれていない
- [ ] 商材接続が成果物ベース（診断対象・確認項目・レポート・改善材料）になっている


## Execution Instruction

1. Copy the entire content of this file (`step-04-adaptation-writer-input.md`).
2. Paste it into Kimi/OpenCode as a new request.
3. Save the AI response to `step-04-adaptation-writer.md` in the same run folder.
4. Review the output before proceeding to the next step.

> **Important:** This is a manual step. The script does not execute prompts, call APIs, or post automatically.
