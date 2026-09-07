# Phase 3-B: PDCA Templates and Genre Learning Store

## Executive Summary

Phase 3-B では、Phase 3-A で設計した Cold Start PDCA を実際に運用できるように、以下を整備する。

- **Run-level PDCA templates**
  - `templates/post-analysis.md`
  - `templates/learning-brief.md`
  - `templates/next-run-recommendation.md`

- **Genre learning store scaffold**
  - `knowledge/mens-fashion-gadget/experiment-log.md`
  - `knowledge/mens-fashion-gadget/hypothesis-pool.md`
  - `knowledge/mens-fashion-gadget/experiment-queue.md`
  - `knowledge/mens-fashion-gadget/audience-insights.md`
  - `knowledge/mens-fashion-gadget/winning-patterns.md`
  - `knowledge/mens-fashion-gadget/losing-patterns.md`
  - `knowledge/mens-fashion-gadget/hook-patterns.md`
  - `knowledge/mens-fashion-gadget/cta-patterns.md`
  - `knowledge/mens-fashion-gadget/content-angle-map.md`

今回は雛形作成のみ。
新規 helper 実装、prompt 自動実行、API 連携、自動投稿は行わない。

---

## Scope

### In Scope

- run-level PDCA 用テンプレートの作成
- 40代ファッション×ガジェット用 learning store の雛形作成
- OPS-002 / OPS-003 の初期状態記録
- Phase 3-C への移行準備

### Out of Scope

- helper 実装
- prompt 自動実行
- SNS API 連携
- 自動投稿
- AI API 自動実行
- n8n 連携
- prompts/templates（既存）/scripts/runs/Phase 1 資産の変更
- 実際の metrics 入力や分析

---

## Created Files

### Run-level PDCA Templates

| ファイル | 目的 |
|----------|------|
| `templates/post-analysis.md` | 投稿後の数値と定性評価から「なぜ伸びた/伸びなかったか」を分析する |
| `templates/learning-brief.md` | 次回 run の `input.md` へ貼れる学習メモを作成する |
| `templates/next-run-recommendation.md` | 次にどの仮説・角度で run を作るかを決める |

### Genre Learning Store

| ファイル | 目的 |
|----------|------|
| `knowledge/mens-fashion-gadget/experiment-log.md` | 実験履歴と結果を一覧管理 |
| `knowledge/mens-fashion-gadget/hypothesis-pool.md` | 仮説プールと状態管理 |
| `knowledge/mens-fashion-gadget/experiment-queue.md` | 次に試す仮説のキュー管理 |
| `knowledge/mens-fashion-gadget/audience-insights.md` | 読者層の仮説・確認済みインサイト |
| `knowledge/mens-fashion-gadget/winning-patterns.md` | 再現性確認済みの勝ちパターン |
| `knowledge/mens-fashion-gadget/losing-patterns.md` | 再利用価値の低いパターン |
| `knowledge/mens-fashion-gadget/hook-patterns.md` | hook の効き/効かなしの傾向 |
| `knowledge/mens-fashion-gadget/cta-patterns.md` | CTA の効き/効かなしの傾向 |
| `knowledge/mens-fashion-gadget/content-angle-map.md` | content_angle のカテゴリマップと反応分布 |

---

## Run-level PDCA Templates

### post-analysis.md

- metrics.md とは役割を分離。
- metrics.md = 事実記録。
- post-analysis.md = 数値と内容の解釈。
- 1投稿だけで winning pattern と断定しない。
- `0` と `unknown` を区別する。

### learning-brief.md

- 次回 run の `input.md` へそのまま貼れる短さにする。
- Cold Start 期間は仮説として扱う。
- 「勝ちパターン」と言い切らない。

### next-run-recommendation.md

- `repeat / iterate / pivot / pause` の4つの判断を使う。
- 直近2投稿と同じ切り口を避ける。
- OPS-002 metrics 確認前は OPS-003 を投稿保留。

---

## Genre Learning Store

### experiment-log.md

実験の履歴テーブル。以下を含む。

- run_id
- hypothesis_id
- content_angle
- status
- posted_at / post_url
- 24h metrics
- result_label
- strongest_signal / weakest_signal
- next_action

初期状態で OPS-002 / OPS-003 を登録済み。

### hypothesis-pool.md

仮説プール。初期10仮説を登録。

- H001: バッグの中身
- H002: 靴の手入れ
- H003: 爪・髪・香り
- H004: 薄型財布・キーケース
- H005: ガジェットポーチ・ケーブル整理
- H006: ワイヤレスイヤホン
- H007: 若作りしないジャケット
- H008: 40代NGファッション
- H009: 営業/経営者の第一印象
- H010: 買ってよかった小物3選

H004 / H005 は H001 と近いため `paused`。
H002 / H003 は OPS-004 候補として `untested / high priority`。

### experiment-queue.md

初期キュー:

1. H002 靴の手入れ
2. H003 爪・髪・香り
3. H007 若作りしないジャケット
4. H009 営業/経営者の第一印象
5. H006 ワイヤレスイヤホン

### audience-insights.md

現時点では仮説が中心。
metrics 確認後に confirmed insights / rejected assumptions を更新。

### winning-patterns.md / losing-patterns.md

Cold Start 中はまだ空。
2〜3回の再現性確認後に昇格。

### hook-patterns.md / cta-patterns.md

Cold Start 中は candidate notes のみ。
複数 run の分析後に傾向を出す。

### content-angle-map.md

First 10 Hypothesis Plan をカテゴリマップ化。
反応マップは OPS-002 metrics 取得後に更新。

---

## Cold Start Operating Rules

1. 初期10投稿は探索期間。
2. 1投稿だけで勝ち負けを決めない。
3. 同じテーマを連投しない。
4. `0` と `unknown` を区別する。
5. インプだけで判断しない。
6. ブランド軸を壊してまでバズを狙わない。
7. 人間承認を必須とする。
8. winning pattern は再現性確認後に昇格。

---

## OPS-002 / OPS-003 Initial State

### OPS-002

- run_id: `20260906-2132-mens-fashion-gadget-corporate-to-personal`
- hypothesis_id: H001
- content_angle: バッグの中身
- status: `waiting_metrics`
- posted_at: `2026-09-06T22:35:48+09:00`
- post_url: `https://x.com/ritsu_opt/status/2096593132653572341?s=20`
- metrics_due_at: `2026-09-07T22:35:48+09:00`
- result_label: `pending`
- next_action: `wait_24h_metrics`

### OPS-003

- run_id: `20260907-0751-mens-fashion-gadget-corporate-to-personal`
- hypothesis_id: H001
- content_angle: バッグの中身
- status: `generated`
- posted_at: `-`
- post_url: `-`
- result_label: `pending`
- next_action: `hold_due_to_overlap_with_OPS-002`

---

## How to Use After 24h Metrics

1. OPS-002 の metrics を X から取得し、`metrics.md` に記録。
2. `templates/post-analysis.md` をコピーして `runs/OPS-002/post-analysis.md` を作成。
3. 人間が review し、`learning-brief.md` / `next-run-recommendation.md` を作成。
4. `experiment-log.md` / `hypothesis-pool.md` / `content-angle-map.md` を更新。
5. 次回 run の `input.md` に learning-brief を反映。

---

## Human Review Gates

- metrics 入力
- post-analysis 確認
- result_label 確定
- learning-brief 承認
- knowledge store 反映
- next run 方針承認
- 実投稿承認

---

## Anti-Overfitting Rules

1. 1投稿だけでジャンル勝敗を決めない。
2. 3本以上同系統で比較する。
3. 初期10投稿は探索期間とする。
4. 投稿時間・画像有無・フォロワー状態を考慮する。
5. インプが低くても保存率/返信率が高ければ signal を見る。
6. インプが高くてもフォロー/保存/返信が弱ければ過大評価しない。
7. バズ狙いでブランド軸を壊さない。
8. 同じテーマを連投しない。
9. 勝ちパターン化は再現性確認後にする。
10. 体験談風投稿では実体験の捏造を避ける。

---

## Known Limitations

- 現時点では metrics データがないため、learning store は仮説で満たされている。
- winning-patterns.md / losing-patterns.md は空。
- hook-patterns.md / cta-patterns.md は candidate notes のみ。
- これらは Phase 3-C 以降の実運用で更新される。

---

## Recommended Next Phase

### Phase 3-C: OPS-002 24h metrics check + first post-analysis

内容:

1. OPS-002 の 24h metrics を X から取得
2. `runs/20260906-2132-mens-fashion-gadget-corporate-to-personal/metrics.md` に記録
3. `templates/post-analysis.md` を使って `post-analysis.md` を作成
4. `templates/learning-brief.md` を使って `learning-brief.md` を作成
5. `templates/next-run-recommendation.md` を使って `next-run-recommendation.md` を作成
6. `knowledge/mens-fashion-gadget/experiment-log.md` を更新
7. `knowledge/mens-fashion-gadget/hypothesis-pool.md` の H001 status を更新
8. `knowledge/mens-fashion-gadget/content-angle-map.md` を更新

---

## Generated Metadata

- document: `docs/phase-3-b-pdca-templates-and-learning-store.md`
- phase: 3-B
- purpose: PDCA Templates and Genre Learning Store Scaffold
- created_at: 2026-09-07
- model: kimi-k2.7-code
- execution_mode: file_based_semi_automation
- new_helpers: none
- api_integration: none
- auto_posting: none
