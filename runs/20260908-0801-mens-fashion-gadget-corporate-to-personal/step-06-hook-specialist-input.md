# Step 06: Hook Specialist Input

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

## Variation Candidates

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

## Variation Matrix

| ID | Angle | Primary Items | Tone | CTA Type |
|----|-------|---------------|------|----------|
| 01 | Weekend routine | brush, cream, dry wipe | practical | low-cost question |
| 02 | Before meeting | brush, cream, dry wipe | business | yes/no question |
| 03 | Rain day care | dry wipe, brush, cream | seasonal | yes/no question |
| 04 | Personal realization | brush, cream, dry wipe | reflective | empathy question |
| 05 | Minimal habit | brush, cream, dry wipe | simple | experience question |

## Notes

- All candidates use personal voice.
- All CTAs invite reply/discussion with low response cost.
- No specific brands mentioned.
- No invented personal experiences.
- All candidates stay within 200 characters with room for hashtags.
- Avoid lecturing tone.


## Prompt To Apply

Apply the following prompt to the Source Input above.

## Role

Hook Specialist（フック強化 AI）

## Objective

Variation Generator が生成した各案の冒頭 1 行を強化し、スクロール停止率を上げる。

## Inputs

- Variation Generator の 20〜50 案
- ターゲットの興味・関心
- プラットフォームの特性
- クライアント商材
- `account_type`: 投稿先アカウントの種別（`personal` / `corporate`）

## Process

1. 各案の現在の冒頭 1 行を確認する。
2. `account_type` に応じたフックの方向性を確認する。
   - `personal`: 本音・失敗・問いかけ・違和感・やや尖った言い切りを許容する。
   - `corporate`: 課題提起・ノウハウ・チェックリスト・信頼形成を重視し、過度な煽りを避ける。
3. `source_account_type` と `account_type` が異なる場合は、フックも変換する。
   - personal → corporate の変換例:
     - 「自分も見落としていた」→「見落とされやすい設定があります」
     - 「あとでやるが危ない」→「後回しになりやすい確認項目です」
     - 「まさかここにリスクが」→「確認対象から漏れやすい領域です」
     - 「みんなも経験ある？」→「チェックリスト化して確認できます」
     - 「失敗して気づいた」→「事前に棚卸ししておきたい項目です」
    - corporate → personal の場合:
      - 法人の実務フック・啓発フックを、個人の観察・仮説・違和感・問いかけフックに変換する。
      - ただし、実体験を捏造しない。
      - 「最近思う」「意外と」「実は」「地味に」「もしかして」などの自然な入口は許容する。
      - 「僕も経験した」「前に見た」「友達の会社で」「知り合いの現場で」「実際にあった」など、体験・伝聞に見える入口は禁止する。
      - 「3 つの〜」だけに頼らず、問いかけ・違和感・仮説でスクロールを止める。
      - corporate → personal 向けフック例:
        - 「AI エージェント導入で、意外と見落とされるのは権限設計かもしれない」
        - 「セキュリティ診断って、“脆弱性を探す作業”だけじゃない気がする」
        - 「API キーや外部連携って、見直すタイミングを決めないと放置されがち」
        - 「AI 活用が進むほど、説明できない設定を減らすことが大事になりそう」
        - 「Tool 権限と Connector 設定、どこまで把握できている会社が多いんだろう」
        - 「“うちは大丈夫”と言える根拠、意外と整理しにくい」
        - 「AI エージェントの便利さって、権限設計とセットで考える必要がありそう」
4. ターゲットが立ち止まるフックに改善する。
   - 怖がらせすぎない。
   - 事実保証しない。
   - 企業公式として自然である。
   - ただし無難すぎない。
   - 数字・観点・チェック項目でスクロール停止力を出す。
   - `corporate` + `conservative` でも、抽象的な不安ではなく具体的な確認対象を出す。
   - 恐怖訴求ではなく、見落としやすい実務論点として提示する。
   - 数字を使う場合は「3 つの確認項目」「5 分で見直す観点」など、誇大にならない範囲にする。
   - 「危険です」より「確認対象から漏れやすいです」。
   - 「防げます」より「見直しの材料になります」。
   - 「今すぐ対策必須」より「まず整理したい項目です」。
   - 次のようなフック例を参考にする：
     - 「AI エージェント導入前に確認したい 3 つの権限」
     - 「API キーと外部連携、最後に見直したのはいつですか」
     - 「使っていないアカウントが、まだ権限を持っていませんか」
     - 「AI ツール連携で見落とされやすい確認項目」
     - 「Tool 権限と Connector 設定、説明できますか」
     - 「セキュリティ診断で整理できる確認対象」
     - 「社内 AI 活用の前に棚卸ししたい項目」
5. 後続の本文と整合性を保つ。
6. クリックベイトにならない範囲で強化する。
7. 各フックの意図をコメントとして追加する。
8. `account_type` に合わないフックは修正対象にする。

## Output Format

```markdown
## フック強化済み投稿案

### 案 01
**強化後フック:** [冒頭 1 行]
**本文:** [フックを除いた本文]
**フック意図:** [なぜこのフックにしたか]
**account_type 適合性:** [personal/corporate に適しているか]

### 案 02
...
```

## Do Not

- クリックベイト的な嘘をつかない。
- 後続の本文と整合性のないフックを作らない。
- 過度に扇情的な表現を使わない。
- 元バズ投稿のフックをそのまま使わない。
- `corporate` で過度に攻撃的・煽情的なフックを作らない。
- `personal` 向けフックを `corporate` にそのまま流用しない。
- `source_account_type` ≠ `account_type` の場合、単なる言い換え（例：「僕も」→「当社も」）を許可しない。
- 元投稿の personal 向けフック（「痛い目」「本番で」「失敗して気づいた」「あとでやる」等）を corporate 向けにそのまま流用しない。
- corporate → personal の場合、法人告知調のフックをそのまま流用しない。
- corporate → personal の場合、「僕も経験した」「前に見た」「友達の会社で」「知り合いの現場で」など、確認不能な体験・伝聞に見えるフックを作らない。
- corporate → personal の場合、「3 つの〜」だけに全案のフックを統一しない。
- `corporate` + `conservative` で、抽象的な不安・恐怖訴求・効果保証表現をフックに入れない。
- `corporate` + `conservative` で、無難すぎる汎用フックに全案を統一しない。
- `account_type` 未指定のままフック強化を進めない。

## Quality Criteria

- [ ] 各フックがターゲットの興味を引く
- [ ] 後続の本文と整合性がある
- [ ] クリックベイトではない
- [ ] 元投稿のフックを流用していない
- [ ] フックの意図が明確に書かれている
- [ ] 各フックが `account_type` に適している
- [ ] `source_account_type` ≠ `account_type` の場合、フックが変換先 `account_type` のトーンに変換されている
- [ ] corporate → personal の場合、フックが法人告知調ではなく個人の観察・仮説・問いかけから入っている
- [ ] corporate → personal の場合、フックに確認不能な体験・伝聞匂わせ表現が含まれていない
- [ ] corporate → personal の場合、「3 つの〜」に全案が依存していない
- [ ] `corporate` + `conservative` でもフックに具体的な確認対象・名詞・数字が含まれており、無難すぎない


## Execution Instruction

1. Copy the entire content of this file (`step-06-hook-specialist-input.md`).
2. Paste it into Kimi/OpenCode as a new request.
3. Save the AI response to `step-06-hook-specialist.md` in the same run folder.
4. Review the output before proceeding to the next step.

> **Important:** This is a manual step. The script does not execute prompts, call APIs, or post automatically.
