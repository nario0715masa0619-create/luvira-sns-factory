# Data Schema

## buzz_post input schema

元バズ投稿の入力データ。

| 項目 | 型 | 説明 | 必須/任意 |
|------|-----|------|-----------|
| `id` | string | 入力データの識別子 | 必須 |
| `platform` | string | 出典プラットフォーム（X, Instagram, Threads 等） | 必須 |
| `original_text` | string | 元バズ投稿の全文 | 必須 |
| `industry` | string | 業種 | 必須 |
| `genre` | string | ジャンル | 必須 |
| `posted_at` | string (ISO8601) | 元投稿の投稿日時 | 任意 |
| `engagement` | object | いいね・リプ・保存・シェア数 | 任意 |
| `source_url` | string | 元投稿の URL | 任意 |

## client_context schema

クライアント情報。

| 項目 | 型 | 説明 | 必須/任意 |
|------|-----|------|-----------|
| `client_name` | string | クライアント名 | 必須 |
| `industry` | string | 業種 | 必須 |
| `product` | string | 商材・サービス名 | 必須 |
| `target` | string | ターゲット層 | 必須 |
| `purpose` | string | 投稿目的 | 必須 |
| `tone` | string | 口調・トーン | 必須 |
| `max_chars` | integer | 最大文字数 | 必須 |
| `ng_expressions` | array[string] | NG 表現リスト | 必須 |
| `hashtag_policy` | string | ハッシュタグ方針 | 任意 |
| `image_policy` | string | 画像方針 | 任意 |
| `notes` | string | その他注意事項 | 任意 |

## generated_post schema

生成された投稿候補。

| 項目 | 型 | 説明 | 必須/任意 |
|------|-----|------|-----------|
| `id` | string | 候補の識別子 | 必須 |
| `version` | integer | 生成バージョン | 必須 |
| `body` | string | 投稿本文 | 必須 |
| `hook` | string | 冒頭 1 行 | 必須 |
| `structure_id` | string | 使用した構造テンプレート ID | 必須 |
| `emotion_tags` | array[string] | 感情分類タグ | 必須 |
| `similarity_score` | float | 元投稿との類似度（0-1） | 必須 |
| `risk_level` | string | リスクレベル（low/medium/high） | 必須 |
| `risk_comment` | string | リスクコメント | 任意 |
| `estimated_impressions` | integer | 推定インプレッション数 | 任意 |
| `brand_fit_score` | integer (1-5) | ブランド適合度 | 必須 |

## review_result schema

人間レビューの結果。

| 項目 | 型 | 説明 | 必須/任意 |
|------|-----|------|-----------|
| `id` | string | レビュー識別子 | 必須 |
| `post_id` | string | レビュー対象の投稿 ID | 必須 |
| `reviewer` | string | レビュアー名 | 必須 |
| `status` | string | approved / revised / rejected | 必須 |
| `comment` | string | レビューコメント | 任意 |
| `reviewed_at` | string (ISO8601) | レビュー日時 | 必須 |
| `revision_time_minutes` | integer | 修正にかかった時間 | 任意 |

## experiment_result schema

実験結果。

| 項目 | 型 | 説明 | 必須/任意 |
|------|-----|------|-----------|
| `id` | string | 実験識別子 | 必須 |
| `team` | string | Team A または Team B | 必須 |
| `post_id` | string | 投稿 ID | 必須 |
| `posted_at` | string (ISO8601) | 投稿日時 | 必須 |
| `impressions_24h` | integer | 24 時間後インプレッション数 | 必須 |
| `likes` | integer | いいね数 | 任意 |
| `replies` | integer | リプ数 | 任意 |
| `reposts` | integer | リポスト数 | 任意 |
| `profile_visits` | integer | プロフィール遷移数 | 任意 |
| `saves` | integer | 保存数 | 任意 |
| `generation_cost` | float | 生成コスト | 任意 |
| `human_revision_time` | integer | 人間修正時間（分） | 任意 |
| `approved` | boolean | 承認済みか | 必須 |

## 補足

- 初期 MVP では Markdown 形式で運用する。
- 将来的に JSON / CSV 化する場合は、本スキーマをベースとする。
- 機密情報は本スキーマに含めない。
