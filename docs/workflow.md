# Workflow

## 概要

入力（元バズ投稿 + クライアント情報）から、人間承認済みの投稿候補を出力するまでの流れ。

初期 MVP では、各ステップを手動でプロンプトを順に実行する。

```
[Input]
  ├─ account_type （personal / corporate） ← 必須
  ├─ source_account_type （personal / corporate）
  └─ その他クライアント情報
  ↓
[01 Pattern Miner]        構造抽出（account_type / source_account_type を考慮）
  ↓
[02 Emotion Mapper]       感情分類（account_type に適した反応設計を評価）
  ↓
[03 Skeleton Builder]     骨格作成
  ↓
[04 Adaptation Writer]    クライアント適応（personal/corporate 別文体変換）
  ↓
[05 Variation Generator]  20〜50案生成
  ↓
[06 Hook Specialist]      フック強化（account_type に合ったフック調整）
  ↓
[07 Similarity Guard]     類似性チェック
  ↓
[08 Risk Filter]          リスクチェック（account_type 別基準適用）
  ↓
[09 Market Judge]         上位5本 + 最終1本選定（account_type 適合性評価）
  ↓
[10 Final Packager]       人間承認用資料作成（account_type を明記）
  ↓
[Human Review]            人間が承認 or 修正
  ↓
[Manual Post]             人間が手動投稿
  ↓
[24h Later]               インプレッション数記録
```

## ステップ詳細

### Step 0: 入力準備

入力ファイルには以下を含める：

- `account_type`: 投稿先アカウントの種別（`personal` / `corporate`）
- `source_account_type`: 元バズ投稿アカウントの種別（`personal` / `corporate`）
- 元バズ投稿（原文）
- 出典プラットフォーム
- 業種
- 商材
- ターゲット
- 投稿目的
- NG 表現
- 口調
- 文字数条件
- 画像有無
- ハッシュタグ方針
- `desired_cta_style`: 希望 CTA スタイル
- `allowed_persona_expression`: 許可される一人称表現
- `risk_tolerance`: リスク許容度

`account_type` は必須項目である。未指定の場合は生成に進まず、人間に確認を求める。

`source_account_type` と `account_type` が異なる場合（例: 個人アカウントの投稿を企業アカウントに転用する場合）、文体・一人称・CTA・リスク観点を必ず調整する。

### Step 1: Pattern Miner

元バズ投稿の構造を抽出する。`account_type` と `source_account_type` を確認し、転用先アカウント種別に適した構造要素を重視して分析する。

出力例：

- 導入：問いかけから入り、共感を誘発
- 展開：自分の失敗話を 3 つ並べる
- 結論：読者に行動を促す
- 反応設計：リプで体験を募る

### Step 2: Emotion Mapper

何の感情で伸びたか分類する。

出力例：

- 保存：手順がまとまっている
- 共感：失敗談が身近
- 議論：意見が分かれるポイントがある

### Step 3: Skeleton Builder

構造をテンプレート化する。

出力例：

```
[フック] 共感できる問いかけ
[事例1] 身近な失敗
[事例2] 別角度の失敗
[事例3] 意外な失敗
[結論] 読者へのメッセージ
[CTA] リプや保存を促す一言
```

### Step 4: Adaptation Writer

骨格をクライアント情報に置換する。

### Step 5: Variation Generator

同じ骨格から 20〜50 案を生成する。

### Step 6: Hook Specialist

各案の冒頭 1 行を強化する。

### Step 7: Similarity Guard

元バズ投稿との類似度をチェックする。

### Step 8: Risk Filter

炎上・誇大広告・事実誤認・法務リスクをチェックする。

### Step 9: Market Judge

上位 5 本と最終おすすめ 1 本を選ぶ。

### Step 10: Final Packager

人間が確認しやすい形に整える。

## 人間承認の位置

Final Packager の出力を人間が確認し、以下を判断する：

- 採用する / 修正する / 棄却する
- 投稿日時
- 必要に応じて画像・ハッシュタグの調整

人間承認がない状態では、いかなる自動投稿も行わない。

## 実投稿後の 24 時間インプレッション記録

1. 投稿完了時刻を記録する。
2. 24 時間後に各種指標を記録する：
   - インプレッション数（Primary KPI）
   - いいね数
   - リプ数
   - リポスト数
   - プロフィール遷移数
   - 保存数
3. 結果を `docs/data-schema.md` の `experiment_result` スキーマに従って記録する。
4. 次回の構造分析やプロンプト改善に反映する。

## Claude 版との比較実験の流れ

詳細は `docs/experiment-design.md` を参照。

簡易フロー：

1. 同じアカウント・同じジャンル・近い時間帯で投稿する。
2. Team A（Claude 版）と Team B（Kimi K2.7 版）がそれぞれ 5 本ずつ投稿する。
3. 各投稿の 24 時間後インプレッション数を比較する。
4. 平均値・最大値・生成コスト・人間修正時間を総合判定する。
5. 勝者を決定し、次の改善に活かす。

## account_type に関する注意点

- `account_type` は Step 0 で確定させ、以降のすべてのステップで引き継ぐ。
- `personal` の場合は、個人発信者・起業家・エンジニア・専門家・現場経験者の投稿構造を優先し、一人称・本音・体験談を許容する。
- `corporate` の場合は、企業公式・BtoB SaaS・オウンドメディア系の投稿構造を優先し、客観性・信頼性・ブランド毀損防止を重視する。
- `source_account_type` と `account_type` が異なる場合は、Adaptation Writer で必ず文体・一人称・CTA を調整する。
- account_type 未指定時は、どのステップでも生成・選抜に進まない。

## 注意点

- 各ステップの出力は、次のステップの入力としてそのまま使える形式にする。
- 中間で品質が崩れた場合、前のステップに戻って修正する。
- すべての判断ログは人間が確認できる形で残す。
