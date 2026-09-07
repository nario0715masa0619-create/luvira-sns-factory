# Phase 3-A Cold Start PDCA Execution Design

## 1. Executive Summary

### Phase 2 MVPでできるようになったこと

Phase 2 では、Luvira SNS Factory の以下の MVP を完成させた。

- **Generate**: `scripts/new_run_folder.py` と 10-step chain による投稿候補生成
- **Approve**: `scripts/approval_package_generator.py` による `approval.md` / `final-candidates.md` 生成と人間承認フロー
- **Post**: 手動投稿（SNS API 連携なし）
- **Record**: `run.json` / `metrics.md` / `approval.md` への投稿記録
- **Manage**: `scripts/run_index_generator.py` による `runs/index.md` での run 管理

具体的には、OPS-002 が実投稿され、OPS-003 が生成済みである。

### なぜ「投稿生成MVP完成」だけでは不十分か

投稿を生成できることと、**バズ投稿を継続的に生成できる能力**は別である。

- 単発の良い投稿は偶然にもできる。
- しかし次回、別の切り口で再現できるかは別問題。
- 何が効いたのかを記録・分析・学習しなければ、同じ土台の上に積み上げられない。
- 結果を見ずに「これが勝ちパターンだ」と決めつけると、たまたまの反応に過学習する。

### バズ投稿生成能力は PDCA Learning Loop で育つ

継続的なバズ投稿生成能力は、以下のループで育つ。

```text
Plan    → Do    → Check    → Act
  ↑                       ↓
  ←←←←←←←←←←←←←←←←←←←←←←
```

- **Plan**: 次の content_genre / content_angle / hook / CTA / target_reader を決める
- **Do**: run を作成し、候補を生成し、承認し、手動投稿する
- **Check**: 24h metrics と定性評価から反応を分析する
- **Act**: 学習を次回 run の input に反映する

### 学習0の状態では Cold Start 探索が必要

現時点では以下の通り、学習データがほぼ0である。

- 実投稿済み: OPS-002（1本）
- 実 metrics: まだ取得できていない
- 勝ち/負けパターン: なし
- ジャンル別の反応地図: なし

この状態で「これが勝ちパターンだ」と決めるのは危険。
最初の目的は「勝ちパターン確定」ではなく、**反応の地図を作ること**。

### 最初の目的

> **「勝ちパターンを見つける」ではなく、「どの切り口にどんな反応があるかの地図を描く」こと。**

---

## 2. Current State

### 現在利用可能な仕組み

| 仕組み | ファイル | 用途 |
|--------|----------|------|
| run folder generator | `scripts/new_run_folder.py` | 新規 run folder の雛形作成 |
| step input composer | `scripts/step_input_composer.py` | 各 step への入力ファイル生成 |
| approval package generator | `scripts/approval_package_generator.py` | `final-candidates.md` / `approval.md` 生成 |
| run index generator | `scripts/run_index_generator.py` | `runs/index.md` 更新 |
| templates | `templates/input.md`, `run.json`, `approval.md`, `metrics.md`, `final-candidates.md` | run 作成時の雛形 |
| manual posting | 人間の手作業 | SNS API なしでの投稿 |
| run index | `runs/index.md` | run 全体の一覧・状態管理 |

### 現在の run 状態

| run_id | status | content_angle | 備考 |
|--------|--------|---------------|------|
| `20260906-2132-mens-fashion-gadget-corporate-to-personal` | posted | 40代男性のバッグの中身 | 24h metrics 取得待ち |
| `20260907-0751-mens-fashion-gadget-corporate-to-personal` | pending_approval | 40代のバッグの中身 | OPS-002 と重複のため投稿保留 |

### 現在できないこと

- 24h metrics の解釈と次回への反映
- 投稿結果からの学習抽出
- 次回 run への改善指示生成
- ジャンル別の勝ち/負けパターン蓄積
- Cold Start 時の仮説管理
- 投稿間の重複管理
- 同ジャンル内での比較評価

---

## 3. Problem Definition

### A. 投稿生成だけではバズ投稿生成能力は育たない

生成能力はあるが、生成したものが現場でどう機能したかのフィードバックがない。

### B. metrics を記録するだけでは次回投稿に活きない

metrics.md に数字を書いても、それをどう解釈し、次の input にどう落とすかの設計がない。

### C. 学習0の状態で「勝ち/負け」を早く決めすぎると過学習する

1本の結果だけで「これは勝ち」「これは負け」と決めると、たまたまの要因を法則と誤認する。

### D. 同じテーマを連投すると、検証が偏る

OPS-002 と OPS-003 はどちらも「バッグの中身」であり、連投すると同じ反応層にしかアプローチできない。

### E. 最初の10投稿は探索期間にすべき

最初の10投稿は、多様な仮説を試し、反応の分布を知る期間。
勝ちパターン確定はその後。

### F. 反応が低い投稿にも兆候がある

インプレッションが低くても、保存率・返信率・プロフィールクリック率が高い場合、小さな signal がある。

### G. インプだけで判断すると切り口を捨てる

インプレッションは表示回数でしかない。
エンゲージメントの質（返信、保存、フォロー）を見ないと、本来育てるべき切り口を見落とす。

---

## 4. Cold Start PDCA Philosophy

### 通常の PDCA

```text
Plan → Do → Check → Act
```

### Cold Start PDCA

学習0の状態では、Plan の精度が低い。そのため以下の拡張フローを使う。

```text
Hypothesize → Diversify → Post → Measure → Compare → Learn → Iterate
```

### 思想

1. **最初は過去データがないため、Plan の精度は低い**
   - だから仮説を複数立て、ばらして試す。

2. **1投稿だけで勝敗を決めない**
   - 1回の結果はノイズの可能性が高い。

3. **最初の10投稿は「反応の地図」を作る期間**
   - どの切り口が反応しやすいか、分布を知る。

4. **winning pattern は再現性が出るまで確定しない**
   - 最低2〜3回、同系統で良い結果が出るまで「仮勝ち」とする。

5. **win / lose より signal_detected / weak_signal / no_signal を使う**
   - 少数データでは強い言葉を使わない。

6. **バズ保証はしない**
   - 継続的に反応の確率を高めることが目的。

7. **ブランド軸を壊してまでインプを取りにいかない**
   - 過激なフックや誇大表現は避ける。

---

## 5. PDCA Loop Definition

### Plan

- content_genre
- content_angle
- target_reader
- desired_reaction
- post_format
- hook_style
- cta_style
- learning_inputs（前回の learning-brief）
- avoid_overlap_with_recent_posts

### Do

- `new_run_folder.py` で run 作成
- `input.md` 作成
- Step 01〜10 実行
- `final-candidates.md` 生成
- `approval.md` 生成
- 人間承認
- 手動投稿
- `posted_at` / `post_url` 記録

### Check

- 24h metrics 記録
- quantitative review
- qualitative review
- target fit review
- hook performance review
- CTA performance review
- timing / media review
- overlap review

### Act

- `post-analysis.md` 作成
- `learning-brief.md` 作成
- `next-run-recommendation.md` 作成
- knowledge store 更新（Phase 3-B以降）
- 次回 run の `input.md` へ反映

---

## 6. Cold Start Experiment Design

### 対象ジャンル

- content_genre: 40代ファッション×ガジェット
- product_slug: `mens-fashion-gadget`

### 目的

40代男性向けに、どの切り口が反応を取りやすいかを探索する。

### First 10 Hypothesis Plan

| # | Hypothesis | content_angle | 理由 |
|---|------------|---------------|------|
| 01 | バッグの中身 | 40代男性のバッグの中身を整える | 実証済み（OPS-002） |
| 02 | 靴の手入れ | 40代男性の靴の手入れ習慣 | 清潔感の象徴、アイテム訴求しやすい |
| 03 | 爪・髪・香り | 40代男性の身だしなみケア | 比較的プライベートで共感しやすい |
| 04 | 薄型財布・キーケース | ポケットの膨らみを解消する小物 | ガジェット×ファッションの接点 |
| 05 | ガジェットポーチ・ケーブル整理 | ビジネスバッグ内の整理 | 実用性があり、会話を誘発 |
| 06 | ワイヤレスイヤホン | 通勤・移動の印象を変える小物 | 身近で購入検討しやすい |
| 07 | 若作りしないジャケット | 40代に似合うジャケット選び | ファッション特化の切り口 |
| 08 | 40代のNGファッション | やってしまいがちな失敗例 | 保存率が高い可能性 |
| 09 | 営業/経営者の第一印象 | 仕事場での見た目の重要性 | ターゲット層の業種訴求 |
| 10 | 買ってよかった小物3選 | 具体的な購入体験シェア | 真似したい反応を狙う |

### 既存状態の反映

- **OPS-002**: 「バッグの中身系」で実投稿済み。24h metrics 取得待ち。
- **OPS-003**: 「バッグの中身系」で生成済みだが、OPS-002 と重複のため投稿保留。

### 次に試すべき方向

OPS-004 は以下のどちらかを推奨する。

- **靴の手入れ**（清潔感・手入れの切り口）
- **爪・髪・香り**（身だしなみケアの切り口）

理由:
- OPS-002 とテーマが被らない
- 40代男性の「清潔感」という軸に沿っている
- ガジェット要素も自然に入れられる

---

## 7. Hypothesis Pool Design

### ファイル

```text
knowledge/mens-fashion-gadget/hypothesis-pool.md
```

※ 今回は設計のみ。Phase 3-B で雛形を作成する。

### スキーマ

| 項目 | 説明 |
|------|------|
| hypothesis_id | H001, H002, ... |
| content_angle | 切り口の一言 |
| target_reader | 想定読者 |
| desired_reaction | 期待する反応 |
| expected_signal | どの指標で signal を見るか |
| risk | リスク |
| priority | 優先度（high / medium / low） |
| status | untested / testing / signal_detected / weak_signal / no_signal / paused / retired |
| related_runs | 関連 run_id リスト |
| notes | 備考 |

### status 定義

- `untested`: 未検証
- `testing`: 検証中
- `signal_detected`: 強い兆候あり
- `weak_signal`: 弱い兆候あり、再検証価値あり
- `no_signal`: 反応なし、優先度低下
- `paused`: 一時保留
- `retired`: 退役

### 初期仮説例

| hypothesis_id | content_angle | status | priority |
|---------------|---------------|--------|----------|
| H001 | バッグの中身 | testing | high |
| H002 | 靴の手入れ | untested | high |
| H003 | 爪・髪・香り | untested | high |
| H004 | 薄型財布・キーケース | untested | medium |
| H005 | ガジェットポーチ・ケーブル整理 | untested | medium |
| H006 | ワイヤレスイヤホン | untested | medium |
| H007 | 若作りしないジャケット | untested | low |
| H008 | 40代NGファッション | untested | low |
| H009 | 営業/経営者の第一印象 | untested | medium |
| H010 | 買ってよかった小物3選 | untested | medium |

---

## 8. Experiment Queue Design

### ファイル

```text
knowledge/mens-fashion-gadget/experiment-queue.md
```

※ 今回は設計のみ。Phase 3-B で雛形を作成する。

### 目的

次にどの仮説を投稿するかを管理する。

### スキーマ

| 項目 | 説明 |
|------|------|
| queue_order | 実行順 |
| hypothesis_id | H001 など |
| planned_run_id | 例: 20260908-1000-mens-fashion-gadget-corporate-to-personal |
| content_angle | 切り口 |
| reason | 選定理由 |
| avoid_overlap | 重複回避理由 |
| planned_platform | X |
| planned_status | planned / generated / posted / waiting_metrics / analyzed / skipped |
| notes | 備考 |

### planned_status 定義

- `planned`: 計画中
- `generated`: run 生成済み
- `posted`: 投稿済み
- `waiting_metrics`: metrics 取得待ち
- `analyzed`: 分析完了
- `skipped`: スキップ

### キュー運用ルール

1. 直近2投稿と同じ切り口は避ける
2. 「バッグの中身系」を連投しない
3. 同じアイテムを連続使用しない
4. 投稿時間帯を記録する
5. 画像あり/なしを可能なら記録する
6. 同系統の仮説を最低3本比較してから winning pattern と判断する

### 初期キュー例

| queue_order | hypothesis_id | content_angle | reason | avoid_overlap |
|-------------|---------------|---------------|--------|---------------|
| 1 | H001 | バッグの中身 | OPS-002 で実施済み | - |
| 2 | H002 | 靴の手入れ | OPS-002 と被らない清潔感軸 | バッグの中身系ではない |
| 3 | H003 | 爪・髪・香り | 身だしなみケア軸 | 靴/バッグと被らない |
| 4 | H005 | ガジェットポーチ・ケーブル整理 | 実用性×ガジェット | H001 から時間を空ける |
| 5 | H004 | 薄型財布・キーケース | ポケットの膨らみ解消 | H001 と被らない切り口 |

---

## 9. Run-level PDCA Artifacts

### 追加予定ファイル

`runs/{run_id}/` 配下に以下を追加する。

- `post-analysis.md`
- `learning-brief.md`
- `next-run-recommendation.md`

### post-analysis.md

| 項目 | 内容 |
|------|------|
| purpose | 数値と投稿内容を見て、なぜ伸びた/伸びなかったかを分析する |
| owner | 人間（Kimi/OpenCode は補助） |
| timing | 24h metrics 取得後 |
| inputs | metrics.md, final-candidates.md, approval.md |
| outputs | 仮説単位の解釈、strongest_signal, weakest_signal |
| update rules | 1回の投稿ごとに作成。断定しすぎない。 |
| do-not-write rules | 勝ちパターンを1回の結果で決めない。 |

### learning-brief.md

| 項目 | 内容 |
|------|------|
| purpose | 次回以降も使える学習を短く残す |
| owner | 人間（Kimi/OpenCode は補助） |
| timing | post-analysis.md 承認後 |
| inputs | post-analysis.md, metrics.md |
| outputs | 次回 run の input.md へ貼れる形の学習 |
| update rules | 簡潔に。1回の結果から法則化しない。 |
| do-not-write rules | 「これが勝ちパターン」と言い切らない。 |

### next-run-recommendation.md

| 項目 | 内容 |
|------|------|
| purpose | 次に試す仮説・角度・フック・CTAを提案する |
| owner | 人間（Kimi/OpenCode は補助） |
| timing | learning-brief.md 承認後 |
| inputs | learning-brief.md, hypothesis-pool.md, experiment-queue.md |
| outputs | repeat / iterate / pivot / pause の判断、次回 run の方針 |
| update rules | overlap 回避を含める。 |
| do-not-write rules | 自動投稿指示は書かない。 |

### 責務分離

| ファイル | 責務 |
|----------|------|
| metrics.md | 数値を記録する。事実のみ。解釈は控えめ。 |
| post-analysis.md | 数値と内容から「なぜ」を分析する。仮説単位で解釈。 |
| learning-brief.md | 次回以降に使える学習を短くまとめる。 |
| next-run-recommendation.md | 次の run の方針を提案する。 |

---

## 10. Metrics Design

### Basic Metrics

| Metric | 説明 |
|--------|------|
| impressions_24h | 24時間のインプレッション数 |
| likes_24h | いいね数 |
| replies_24h | 返信数 |
| reposts_24h | リポスト数 |
| bookmarks_24h | ブックマーク数 |
| profile_clicks_24h | プロフィールクリック数 |
| follows_24h | フォロー数 |

### Calculated Metrics

| Metric | 計算式 |
|--------|--------|
| engagement_rate_24h | (likes + replies + reposts + bookmarks) / impressions × 100 |
| reply_rate_24h | replies / impressions × 100 |
| bookmark_rate_24h | bookmarks / impressions × 100 |
| profile_click_rate_24h | profile_clicks / impressions × 100 |
| follow_conversion_rate_24h | follows / impressions × 100 |

### metrics の分類

#### Critical（必須）

- impressions_24h
- likes_24h
- replies_24h
- reposts_24h
- bookmarks_24h

#### Optional（あれば記録）

- profile_clicks_24h
- follows_24h

#### Unknown（取得できない/未記録）

- X の画面上で取得できない場合
- 手動記録漏れ
- 仕様上見えない指標

### ルール

- Critical metrics が欠けたら `result_label` は `invalid_missing_metrics` とする。
- Optional metrics が欠けても invalid にはしない。
- `0` と `unknown` は区別する。
  - `0`: 取得できたがゼロ
  - `unknown`: 取得できない/未記録

---

## 11. Result Labeling Design

### Cold Start 用ラベル

| ラベル | 意味 |
|--------|------|
| signal_detected | 強い兆候あり |
| weak_signal | 弱い兆候あり、再検証価値あり |
| no_signal | 反応なし、優先度を下げる |
| invalid_missing_metrics | critical metrics 不足で判断不能 |

### 本格 PDCA 用ラベル

| ラベル | 意味 |
|--------|------|
| win | 再現性確認済みの勝ちパターン |
| promising | 良い兆候あり、追加検証の価値あり |
| neutral | 大きな悪さはないが強い反応もない |
| weak | 反応が弱く、改善しないと再投稿価値が低い |
| reject | ブランド不一致、反応なし、再利用価値なし |

### 重要

Cold Start 期間では `win` を安易に使わない。
`win` は再現性確認後に使う。

### Cold Start 判定基準

#### signal_detected

- 同時期の投稿と比べて相対的に反応が良い
- または、インプは普通でも replies / bookmarks / profile_clicks に強い兆候がある

#### weak_signal

- 数字は弱いが、フック/テーマ/CTAの一部に改善余地がある
- もう1回だけ角度を変えて試す価値がある

#### no_signal

- インプも反応も弱い
- 保存/返信/プロフィール遷移などの兆候がない
- 優先度を下げる

#### invalid_missing_metrics

- critical metrics 不足
- 投稿 URL 不明
- 24h 計測条件が崩れた
- 記録ミスにより判断不能

### 本格 PDCA 判定基準

#### win

- 同系統の投稿を最低2〜3回試し、複数回良い兆候が出た
- 再現性がある

#### promising

- 1〜2回の投稿で良い兆候がある
- 追加検証の価値あり

#### neutral

- 大きな悪さはないが強い反応もない

#### weak

- 反応が弱く、改善しないと再投稿価値が低い

#### reject

- ブランド不一致、反応なし、再利用価値なし

---

## 12. Qualitative Analysis Design

### 分析項目

| # | 項目 |
|---|------|
| 1 | hook は強かったか |
| 2 | 読み始める理由があったか |
| 3 | 保存したくなる具体性があったか |
| 4 | コメントしたくなる余白があったか |
| 5 | 40代男性に刺さる悩みだったか |
| 6 | 若作りではなく清潔感という軸に合っていたか |
| 7 | ガジェット要素が自然に入っていたか |
| 8 | 投稿が説教臭くなっていないか |
| 9 | 自慢っぽくなっていないか |
| 10 | 実体験の捏造リスクがないか |
| 11 | 直近投稿とテーマが被っていないか |
| 12 | 投稿時間帯は妥当だったか |
| 13 | 画像の有無は影響しそうか |
| 14 | CTA は返信しやすかったか |

### 定性評価の使い方

- 各項目を `strong` / `ok` / `weak` / `unknown` で評価する。
- 数字と合わせて、「何が効いた/効かなかったか」を推測する。
- ただし、推測は推測として扱い、法則化しない。

---

## 13. Knowledge Store Design

### 構造

```text
knowledge/
└── mens-fashion-gadget/
    ├── experiment-log.md
    ├── hypothesis-pool.md
    ├── experiment-queue.md
    ├── winning-patterns.md
    ├── losing-patterns.md
    ├── hook-patterns.md
    ├── cta-patterns.md
    ├── content-angle-map.md
    └── audience-insights.md
```

※ 今回は設計のみ。Phase 3-B で雛形を作成する。

### 各ファイルの定義

| ファイル | purpose | update timing |
|----------|---------|---------------|
| experiment-log.md | 実験の履歴と結果を一覧管理 | 各 run の metrics 取得後 |
| hypothesis-pool.md | 仮説のプールと状態管理 | 随時 |
| experiment-queue.md | 次に試す仮説のキュー | 各 run 分析後 |
| winning-patterns.md | 再現性が確認された勝ちパターン | signal_detected が2〜3回続いた後 |
| losing-patterns.md | 再利用価値が低いと判断されたパターン | no_signal が2〜3回続いた後 |
| hook-patterns.md | 効いた/効かなかった hook の傾向 | 複数 run の分析後 |
| cta-patterns.md | 効いた/効かなかった CTA の傾向 | 複数 run の分析後 |
| content-angle-map.md | 各 content_angle の反応分布 | 複数 run の分析後 |
| audience-insights.md | ターゲット層の反応傾向 | 複数 run の分析後 |

### 更新ルール

- `winning-patterns.md` は Cold Start 初期には安易に埋めない。
- `losing-patterns.md` も1回の失敗で断定しない。
- 最初は `experiment-log.md` / `hypothesis-pool.md` / `audience-insights.md` を中心に育てる。
- signal が再現したものだけ `winning-patterns.md` に昇格する。

---

## 14. Experiment Log Design

### ファイル

```text
knowledge/mens-fashion-gadget/experiment-log.md
```

### 記録項目

| 項目 | 説明 |
|------|------|
| run_id | run の ID |
| posted_at | 投稿日時 |
| content_angle | 切り口 |
| hypothesis_id | H001 など |
| post_url | 投稿 URL |
| status | posted / waiting_metrics / analyzed |
| impressions_24h | インプレッション |
| likes_24h | いいね |
| replies_24h | 返信 |
| reposts_24h | リポスト |
| bookmarks_24h | ブックマーク |
| profile_clicks_24h | プロフィールクリック |
| follows_24h | フォロー |
| result_label | signal_detected / weak_signal / no_signal / invalid_missing_metrics |
| strongest_signal | 最も強かった兆候 |
| weakest_signal | 最も弱かった点 |
| next_action | repeat / iterate / pivot / pause |

### 用途

- 初期10投稿の相対比較
- 重複チェック
- 次回投稿方針の判断
- winning pattern 候補の発見

---

## 15. Learning Brief Format

### 目的

次回 run の `input.md` へ貼れる形で学習をまとめる。

### 含める項目

| 項目 | 説明 |
|------|------|
| previous_run_id | 前回 run_id |
| hypothesis_id | 仮説ID |
| content_angle | 切り口 |
| result_label | 判定ラベル |
| strongest_signal | 最も強かった兆候 |
| weakest_signal | 最も弱かった点 |
| quantitative_summary | 数値の要約 |
| qualitative_summary | 定性評価の要約 |
| winning_elements | 効いた要素 |
| losing_elements | 効かなかった要素 |
| avoid_next_time | 次回避けるべきこと |
| try_next_time | 次回試す価値があること |
| recommended_content_genre | 推奨ジャンル |
| recommended_content_angle | 推奨切り口 |
| recommended_hook_style | 推奨フックスタイル |
| recommended_cta_style | 推奨CTAスタイル |
| recommended_target_reader | 推奨ターゲット読者 |
| avoid_overlap_with_recent_posts | 重複回避情報 |
| confidence | 確信度（low / medium / high） |
| human_notes | 人間の補足メモ |

### 注意

- 断定しすぎない。
- 学習0〜初期10投稿では仮説として扱う。
- 「勝ちパターン」と言い切らない。
- Kimi/OpenCode にそのまま貼れる短さにする。

---

## 16. Next Run Recommendation Format

### ファイル

```text
runs/{run_id}/next-run-recommendation.md
```

### 含める項目

| 項目 | 説明 |
|------|------|
| recommended_next_run_type | repeat / iterate / pivot / pause |
| recommended_hypothesis_id | 推奨仮説ID |
| recommended_angle | 推奨切り口 |
| reason | 選定理由 |
| avoid_overlap_with_previous_posts | 過去投稿との重複回避 |
| target_reader | 推奨ターゲット読者 |
| desired_reaction | 期待する反応 |
| hook_direction | フックの方向性 |
| cta_direction | CTAの方向性 |
| draft_input_snippet | 次回 input.md への貼り付け用スニペット |
| risk_notes | リスクメモ |
| confidence | 確信度（low / medium / high） |

### ルール

- OPS-002 の結果を見るまでは、バッグの中身系の連投は避ける。
- OPS-004 は靴の手入れ or 爪・髪・香りを優先。
- 次回 run の `input.md` へ貼れる形で出す。

---

## 17. OPS-002 Application Plan

### 対象

- run_id: `20260906-2132-mens-fashion-gadget-corporate-to-personal`
- content_angle: 40代男性のバッグの中身
- status: posted
- metrics_due_at: `2026-09-07T22:35:48+09:00`

### metrics.md に記録する項目

- impressions_24h
- likes_24h
- replies_24h
- reposts_24h
- bookmarks_24h
- profile_clicks_24h（取得できれば）
- follows_24h（取得できれば）
- 各 calculated metrics
- result_label

### post-analysis.md で見るべき観点

- インプレッションは予想以上か以下か
- 保存率は高いか
- 返信率は高いか
- プロフィール遷移はあるか
- どの部分が反応を引いたか
- 投稿時間帯の影響
- 画像の有無の影響

### learning-brief.md に変換する内容

- OPS-002 の result_label
- strongest_signal / weakest_signal
- winning_elements / losing_elements
- avoid_next_time / try_next_time
- 次回推奨 content_angle

### next-run-recommendation.md で判断する内容

#### 分岐例 A: impressions 高い + bookmarks 高い

- バッグの中身系は `signal_detected`
- OPS-003 は被りが強いので数日後に回す
- 次は靴/清潔感に広げる

#### 分岐例 B: impressions 低い + replies あり

- フックは弱いが会話余地あり
- CTA 改善して再テスト

#### 分岐例 C: impressions 低い + engagement なし

- バッグの中身系は一旦弱い
- 靴/香り/髪など別角度へ pivot

#### 分岐例 D: metrics 不足

- `invalid_missing_metrics`
- 判断保留

---

## 18. OPS-003 Handling Rule

### 対象

- run_id: `20260907-0751-mens-fashion-gadget-corporate-to-personal`
- status: pending_approval
- selected_candidate_id: candidate-03
- content_angle: バッグの中身

### 判断

- OPS-002 とテーマが強く重複
- すぐ投稿しない
- OPS-002 の 24h metrics を見てから判断
- 投稿する場合は数日〜1週間空ける
- もしくは別 angle へ再生成する

### 推奨アクション

1. OPS-002 metrics 取得後、post-analysis を実施
2. バッグの中身系が `signal_detected` なら、1週間以上空けて OPS-003 を投稿
3. `weak_signal` / `no_signal` なら、OPS-003 は `paused` または `retired` とし、別 angle へ pivot

---

## 19. Human Review Gate

PDCA でも人間判断を必須にする。

### 必須ゲート

| # | ゲート | 内容 |
|---|--------|------|
| 1 | metrics 入力 | 人間が X から数字を確認し入力する |
| 2 | result_label 確定 | 人間が label を決定する |
| 3 | post-analysis 確認 | 人間が分析内容を確認する |
| 4 | learning-brief 承認 | 人間が学習内容を承認する |
| 5 | knowledge store 反映 | 人間が知見の更新を承認する |
| 6 | next run 方針承認 | 人間が次回方針を承認する |
| 7 | 実投稿承認 | 人間が最終承認してから手動投稿する |

### 理由

- 数字の過剰解釈を防ぐ
- ブランド毀損を防ぐ
- バズ狙いで過激化するのを防ぐ
- 実体験の捏造を防ぐ
- 投稿ジャンルの一貫性を守る

---

## 20. Anti-Overfitting Rules

少数データへの過剰適応を防ぐルール。

1. 1投稿だけでジャンル勝敗を決めない
2. 3本以上同系統で比較する
3. 初期10投稿は探索期間とする
4. 投稿時間・画像有無・フォロワー状態を考慮する
5. インプが低くても保存率や返信率が高ければ `signal_detected` または `weak_signal` にできる
6. インプが高くてもフォロー/保存/返信が弱ければ過大評価しない
7. バズ狙いでブランド軸を壊さない
8. 同じテーマを連投しない
9. 勝ちパターン化は再現性確認後にする
10. 体験談風投稿では実体験の捏造を避ける

---

## 21. Phase 3-B以降の推奨

### 選択肢

#### A. PDCA templates and genre learning store scaffold

- `post-analysis.md` template
- `learning-brief.md` template
- `next-run-recommendation.md` template
- `knowledge/mens-fashion-gadget/` 初期ファイル群

#### B. OPS-002 24h metrics check + first post-analysis

- 実 metrics を使って初回 PDCA を回す

#### C. metrics_recorder.py

- `metrics.md` / `run.json` への手動入力補助

#### D. learning_brief_generator.py

- `post-analysis.md` と `metrics.md` から learning brief 生成補助

### 推奨順序

| フェーズ | 内容 |
|----------|------|
| Phase 3-B | PDCA templates and genre learning store scaffold |
| Phase 3-C | OPS-002 24h metrics check + first post-analysis |
| Phase 3-D | metrics recorder helper |
| Phase 3-E | learning brief generator |

### 理由

- 先にテンプレートと learning store の器を作る
- その後、OPS-002 の実 metrics を入れて初回 PDCA を回す
- helper 実装は運用が固まってからでよい

---

## 22. Out of Scope

以下は明確に対象外。

- 自動投稿
- SNS API からの自動取得
- AI API 自動実行
- n8n 連携
- 実投稿の自動判断
- 人間承認の省略
- バズ保証
- 投稿結果の過剰解釈
- 既存 run の修正
- scripts 実装
- prompts 改修
- templates 改修

---

## 23. Acceptance Criteria

- [x] `docs/phase-3-a-cold-start-pdca-execution-design.md` が作成されている
- [x] Cold Start 前提が明確になっている
- [x] 初期10投稿は探索期間として定義されている
- [x] hypothesis-pool / experiment-queue の設計がある
- [x] run-level artifacts の責務が明確
- [x] metrics 設計がある
- [x] result labeling 設計がある
- [x] knowledge store 設計がある
- [x] OPS-002 への適用方針がある
- [x] OPS-003 の保留判断ルールがある
- [x] anti-overfitting rules がある
- [x] Phase 3-B 以降の推奨がある
- [x] 実装・投稿・API 連携に進んでいない
- [x] git status を確認している

---

## 24. Generated Metadata

- document: `docs/phase-3-a-cold-start-pdca-execution-design.md`
- phase: 3-A
- purpose: Cold Start PDCA Execution Design
- created_at: 2026-09-07
- model: kimi-k2.7-code
- execution_mode: file_based_semi_automation
- new_helpers: none
- api_integration: none
- auto_posting: none
