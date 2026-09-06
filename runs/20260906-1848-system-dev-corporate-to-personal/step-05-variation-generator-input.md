# Step 05: Variation Generator Input

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

## 置換ドラフト

### 前提

- source_account_type: corporate
- account_type: personal
- 商材: AI活用型短納期システム開発
- ターゲット: 中小企業経営者 / 事業責任者 / システム開発を検討している担当者
- 目標文字数: 200文字以内
- CTA: reply / discussion / experience_sharing

### 骨格の置換

```
[フック]: 要件整理で「これだけは決めとかないと後で痛い目を見る」ポイント
[セクション 1]: スコープがどんどん膨らんで、MVPと本開発の区別が曖昧になるあるある
[セクション 2]: AIにコードを書かせても、要件が曖昧だと期待したものが帰ってこない気づき
[セクション 3]: 人間が要件を整理してAIが下書き、人間が承認するという分担のヒント
[CTA]: 返信・議論を促す問いかけ
```

### 置換後の投稿案（案 A）

```
要件定義で「後で痛い目を見たくない」ポイントを1つ。

AI活用の短納期開発を頼む時、スコープが勝手に膨らんで「MVP」のはずが本開発化するの、よくある。

自分も経験あるけど、要件が曖昧だとAIも迷子になって、想定外のものが返ってくる。

人間が要件を整理 → AIが下書き → 人間が承認、っていう分担が意外と大事。

要件整理で気をつけてるポイント、あれば教えてほしい。
```

### 置換後の投稿案（案 B）

```
「AIに任せれば早くなる」は半分ウソだと思う。

実際、要件が整理できてないと、AIはとても速く「違うもの」を作ってくれる。

自分が見た失敗パターンは3つ：
① MVPと本開発の区切りが曖昧
② 承認ゲートがない
③ 仕様変更のルールが決まってない

これを事前に決めとくだけで、後々のムダが激減する気がする。

みんなの現場ではどうしてる？
```

### 置換ポイント

| 元（corporate） | 転用後（personal） |
|-----------------|-------------------|
| 業界全体の課題提示 | 自分の現場で気づいたこと |
| 「貴社も」 | 「自分も」 |
| チェックリスト | 気づき・仮説 |
| 資料請求CTA | 返信・議論CTA |
| 専門用語の羅列 | 現場のあるある |
| 自社サービス紹介 | 実践的なヒント |

### 感情チェック

- 不安: 2（過度に不安を煽らない）
- 共感: 4（現場のあるあるを共有）
- 発見: 4（新しい視点を提供）
- 信頼: 3（謙虚な専門性）
- 参加欲: 4（問いかけでリプ誘発）

### Risk Notes

- 「AIに任せれば早くなるはウソ」は比喩表現。効果保証ではないことを明確に。
- 「自分が見た失敗パターン」は個人の観察として語る。
- 具体的な企業名や案件は出さない。
- 200字を超える案は文字数調整が必要。


## Prompt To Apply

Apply the following prompt to the Source Input above.

## Role

Variation Generator（バリエーション生成 AI）

## Objective

同じ骨格から、構造は保ちつつ角度を変えた 20〜50 案の投稿案を生成する。

## Inputs

- 適応済み骨格
- `account_type`: 投稿先アカウントの種別（`personal` / `corporate`）
- `source_account_type`: 元投稿アカウントの種別（`personal` / `corporate`）
- `desired_cta_style`: 希望 CTA スタイル
- `allowed_persona_expression`: 許可される一人称表現
- `risk_tolerance`: リスク許容度
- フックパターン候補（あれば）
- 文字数条件
- 口調
- NG 表現

## Process

1. `account_type` が未指定の場合は生成を行わず、人間に確認を求める。
2. 骨格の構造を確認する。
3. `account_type` に応じた生成ルールを適用する。
   - `personal` の場合:
     - 一人称表現「僕」「私」「自分」を許容する。
     - 実体験風、本音、失敗談、問いかけ、やや尖った言い切りを許容する。
     - CTA はリプ、共感、経験募集、問いかけを優先する。
     - ただし虚偽体験、確認不能な成果、過剰な不安煽りは禁止する。
    - `corporate` の場合:
      - 一人称体験談「僕も」「私も」は原則禁止する。
      - 客観表現、課題提起、ノウハウ、チェックリスト、信頼形成を優先する。
      - CTA は無料相談、資料請求、チェックリスト、問い合わせ導線を優先する。
      - 保証表現、誇大表現、過度な煽りを避ける。
       - `risk_tolerance=conservative` の場合はさらに以下を徹底する：
         - 啓発だけで終わらせず、実務チェック項目を 1〜3 個入れる。
         - 商材接続は効果ではなく「何を見える化するか」で表現する。
         - 成果物ベースで語る：診断対象、確認項目、レポート、改善材料、判断材料。
        - 断定より「確認できます」「整理できます」「見直しの材料になります」などの控えめな表現を優先する。
        - 20 案を一度に無理に出さず、10 案×2 バッチを標準にする。
4. `source_account_type` と `account_type` が異なる場合は、以下の変換制約を生成前に適用する。
   - personal → corporate の場合:
     - 個人の失敗談・本音を法人の実体験風に置き換えない。
     - 「当社も」「当社でも」「弊社も」「弊社でも」は個人構造の残存として排除する。
     - 「皆さんはどうですか？」系のリプ募集CTAを残さない。
     - personal由来の煽り・感情表現をそのまま残さない。
      - corporate→corporate の結果とほぼ同じ案だけに収束させない。
      - personal由来の熱量は、実務チェック項目・保存性・説明責任に変換する。
      - 元投稿の冒頭フックを近い形で再利用しない。
      - 元投稿の「失敗」「痛い目」「本番で気づいた」「あとでやる」などの personal 由来フックを、そのまま corporate 向けに使わない。
      - すべての案をリスク棚卸し型に寄せない。
      - 「3 つの観点」だけに依存しない。
      - 最終的な方向性を最低 3 種類に分ける：
        1. チェックリスト型
        2. リスク棚卸し型
        3. 説明責任・レポート型
      - 各方向性を最低 2 案ずつ生成する。
      - 10 案生成する場合は、残り 4 案で別切り口を試す：
        - 導入前確認型
        - 権限管理型
        - 外部連携確認型
        - AI エージェント利用ルール型
      - `corporate` + `conservative` でも、フックには具体的な名詞を入れる：権限、API キー、外部連携、Tool 権限、Connector、未使用アカウント、説明責任。ただし、効果保証・根拠不明実績・過度な煽りは禁止。
    - corporate → personal の場合:
      - 法人の実務フック・啓発構造・チェックリストを、個人の気づき・問いかけ・仮説・議論誘発・リプ CTA に変換する。
      - ただし虚偽体験・捏造実績・確認不能な伝聞を禁止する。
      - 法人の「3 つ」「3 点」「チェック項目」型リスト構造を、そのまま personal 投稿に残さない。10 案中「3 つの〜」型は 2 案までに抑える。
      - 個人投稿として自然な入口から入り、以下の方向性に最低 1 案ずつ配分する：
        1. 気づき型
        2. 問いかけ型
        3. 仮説提示型
        4. 実務あるある型
        5. 論点整理型
      - 断定ではなく「〜かもしれない」「〜な気がする」「〜って意外と大事そう」などの仮説表現を優先する。
      - 「個人的な話だけど」「知り合いの会社で」「友達の現場で」「前に見た現場で」「ある会社で」「以前相談を受けた」「実際にあった」など、本人経験・他社経験・伝聞を匂わせる表現は使わない。
      - personal 向けだからといって商材接続を完全に消さない。以下のように軽く接続する：
        - セキュリティ診断って、脆弱性探しというより説明できない設定を減らす作業に近い
        - AI エージェント診断は、権限や外部連携を整理するきっかけになりそう
        - 診断レポートがあると、見直す順番を決めやすくなりそう
5. フック、具体例、結論、CTA の各要素でバリエーションを作る。
6. 同じ構造を維持しつつ、異なる切り口・感情・角度を試す。
7. 各案に通し番号を振る。
8. 生成段階で `account_type` に明らかに不適合な案（例：personal → corporate で個人構造を残す案）を自分で除外する。
9. 文字数条件と口調を守る。
10. 20〜50 案を一度に生成すると品質が落ちる場合は、10 案単位などにバッチ分割して生成してもよい。特に `corporate` + `conservative` の場合は、10 案×2 バッチを標準とする。

## Output Format

```markdown
## 投稿案バリエーション

### 生成条件
- account_type:
- source_account_type:
- desired_cta_style:
- allowed_persona_expression:
- risk_tolerance:
- 文字数条件:
- 口調:
- 骨格:

### 案 01
[投稿本文]

### 案 02
[投稿本文]

...（案 03 〜 案 50 まで同様）...
```

## Do Not

- 単に言い換えを繰り返さない。構造は同じで角度を変える。
- 誇大表現や断定的な言い回しを増やさない。
- NG 表現を使用しない。
- 元バズ投稿の固有名詞や独自表現を流用しない。
- `account_type` に合わない文体で生成しない。
- `personal` 向け表現を `corporate` 向けに流用しない。
- `corporate` 向けの無難な表現を `personal` 向けで弱く使いすぎない。
- 元バズ投稿の言い回しを直接流用しない。
- `source_account_type` ≠ `account_type` の場合、以下を特に避ける:
  - 「当社も」「当社でも」「弊社も」「弊社でも」
  - 個人の失敗談を法人の実体験のように置き換えること
  - 「皆さんはどうですか？」系のリプ募集CTAを残すこと
  - personal由来の本音・煽り・感情表現をそのまま残すこと
  - 元投稿の冒頭フックを近い形で再利用すること
  - 元投稿の「失敗」「痛い目」「本番で気づいた」「あとでやる」などの personal 由来フックをそのまま corporate 向けに使うこと
  - すべての案をリスク棚卸し型に寄せること
  - corporate→corporate結果とほぼ同じ投稿だけに収束すること
  - 「3 つの観点」だけに依存すること
  - corporate → personal の場合、さらに以下を避ける:
    - corporate 由来の「3 つ」「3 点」「チェック項目」型に全案を寄せること
    - 法人投稿のリスト構造をそのまま personal 投稿に残すこと
    - 「個人的な話だけど」「知り合いの会社で」「友達の現場で」「前に見た現場で」「ある会社で」「以前相談を受けた」「実際にあった」など、確認不能な体験・伝聞を匂わせる表現
    - 架空の実体験、伝聞、実績、具体事例を作ること
    - personal 向けだからといって商材接続を完全に消すこと
- `account_type` 未指定のまま生成を進めない。
- `corporate` + `conservative` の場合、以下の表現を避ける：
  - 「当社の調査では」「弊社の実績では」「導入企業では」「多くの企業で」
  - 「必ず」「完全に」「事故を防げます」「漏洩を防ぎます」
  - 「小さな対応の積み重ねが、大きな安心を作ります」系の定型表現
  - 元投稿の締め文・決め台詞を近い形で再利用すること

## Quality Criteria

- [ ] すべての案が同じ骨格構造を保っている
- [ ] 各案が異なる角度・切り口になっている
- [ ] 文字数条件を満たしている
- [ ] 口調が `account_type` に適して統一されている
- [ ] `allowed_persona_expression` を守っている
- [ ] `desired_cta_style` に沿っている
- [ ] 誇大表現や断定が含まれていない
- [ ] 元投稿の文言を流用していない
- [ ] `source_account_type` ≠ `account_type` の場合、変換先 `account_type` に不適合な案が生成段階で除外されている
- [ ] `source_account_type` ≠ `account_type` の場合、最低 3 方向性に分かれており、各方向性が 2 案以上含まれている
- [ ] `source_account_type` ≠ `account_type` の場合、元投稿フックの丸コピーや近しい表現が含まれていない
- [ ] corporate → personal の場合、法人の「3 つ」「3 点」「チェック項目」型リスト構造が過半数を占めていない
- [ ] corporate → personal の場合、「個人的な話だけど」「知り合いの会社で」「友達の現場で」などの体験・伝聞匂わせ表現が含まれていない
- [ ] corporate → personal の場合、断定ではなく「〜かもしれない」「〜な気がする」などの仮説表現が使われている
- [ ] corporate → personal の場合、商材接続が軽く・自然に含まれている
- [ ] `corporate` + `conservative` の場合、実務チェック項目が 1〜3 個含まれている
- [ ] `corporate` + `conservative` の場合、根拠不明な調査風・実績風表現が含まれていない


## Execution Instruction

1. Copy the entire content of this file (`step-05-variation-generator-input.md`).
2. Paste it into Kimi/OpenCode as a new request.
3. Save the AI response to `step-05-variation-generator.md` in the same run folder.
4. Review the output before proceeding to the next step.

> **Important:** This is a manual step. The script does not execute prompts, call APIs, or post automatically.
