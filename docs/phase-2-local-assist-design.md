# Phase 2-A Local Semi-Automation Design

## 1. Executive Summary

Phase 2-A は、Phase 1 で検証済みの 10 段階手動プロンプトチェーンを、**いきなり完全自動化せずにローカル支援ツールとして半自動化するための設計**を作成するフェーズである。

Phase 1 では、第1商材「AI エージェントセキュリティ診断」と第2商材「AI活用型短納期システム開発」の両方において、same-type / cross-type 全方向で手動チェーンが機能することを確認した。しかし、10 段階を人手だけで回すと、反復実験・ログ管理・承認記録が非効率になる。

Phase 2-A では、**ファイルベースの半自動化**を導入し、以下を実現する。

- 各 step の入出力をファイルとして保存する
- 途中結果を人間が確認できる
- 失敗時に途中から再開できる
- 人間承認パッケージを標準化する
- 24h impressions 記録の土台を作る
- 実投稿は人間が行う（自動投稿はしない）

**今回は設計のみである。** コード実装、スクリプト作成、API 連携、n8n 連携、自動投稿、実投稿は一切行わない。

---

## 2. Scope

### 2.1 In Scope

- ローカルファイルベースの半自動化設計
- test-case の標準化と input 生成
- 各 step の入出力管理
- result 生成支援の設計
- final package 生成支援の設計
- human approval package の設計
- 24h impressions 記録欄の設計
- 実験ログ管理の設計
- run metadata schema の設計
- エラー処理・リカバリ設計
- ガバナンス・安全基準の設計

### 2.2 Out of Scope

- 自動投稿の実施
- SNS API 連携
- n8n 連携
- 完全自動運用
- 実在第三者投稿本文の保存
- Claude 版 SNS システムとの統合
- LuviraMemory 連携
- prompt 本文の修正
- Phase 1 result / test-case の変更
- docs の大規模な書き換え

---

## 3. Proposed Local Workflow

Phase 2-A で提案するローカル半自動化ワークフローは以下の通り。

```
1. test-case 作成
   └── 人間が商材・account_type・source_account_type・CTA スタイル等を決定

2. run folder 作成
   └── runs/YYYYMMDD-HHMM-{slug}/ を生成

3. input.md 生成
   └── test-case から client_context と step-01 入力を生成

4. step-01 Pattern Miner 実行
   └── Kimi/OpenCode で prompt を実行し、step-01 output を保存

5. step-02 Emotion Mapper 実行
   └── step-01 output を参考に実行

6. step-03 Skeleton Builder 実行
   └── step-02 output を参考に実行

7. step-04 Adaptation Writer 実行
   └── step-03 output を参考に実行

8. step-05 Variation Generator 実行
   └── step-04 output を参考に実行（10 案生成）

9. step-06 Hook Specialist 実行
   └── step-05 output を参考に実行

10. step-07 Similarity Guard 実行
    └── 類似性判定を記録

11. step-08 Risk Filter 実行
    └── リスク判定を記録

12. step-09 Market Judge 実行
    └── 上位 5 本・最終おすすめ 1 本を選定

13. step-10 Final Packager 実行
    └── 人間承認用パッケージを生成

14. final-candidates.md 生成
    └── 最終候補 5 本・最終おすすめ 1 本を整理

15. approval.md 生成
    └── 人間承認チェック欄・修正指示欄・投稿後記録欄を生成

16. metrics.md 生成
    └── 24h impressions 記録欄を生成

17. run.json 生成 / 更新
    └── run metadata を記録

18. 人間承認
    └── approval.md を人間が確認し、採用/不採用/修正を決定

19. 投稿実行（人間）
    └── 人間が手動で SNS に投稿
    └── posted_at を metrics.md / run.json に記録

20. 24h impressions 記録（人間または後続工程）
    └── 24h 後に impressions, engagement 等を記録
```

### 3.1 人間が介入するポイント

- test-case 作成時
- 各 step 実行後の確認（特に step-05, 07, 08, 09）
- final package 承認時
- 投稿実行時
- 24h metrics 記録時

### 3.2 AI が支援するポイント

- prompt 入力の自動生成
- step 出力のファイル保存支援
- 最終候補・承認パッケージの雛形生成
- 判定結果の整形・記録支援

---

## 4. Directory Structure

Phase 2 用の推奨ディレクトリ構成は以下の通り。

```
D:\OpenCode\luvira-sns-factory/
├── docs/
│   ├── phase-2-local-assist-design.md   # 本設計書
│   └── ...
├── prompts/
│   ├── 01-pattern-miner.md
│   ├── 02-emotion-mapper.md
│   ├── ...
│   └── 10-final-packager.md
├── experiments/
│   └── phase-1/
│       └── ...（Phase 1 資産。変更しない）
└── runs/
    ├── index.md
    └── 20260905-1430-system-dev-corporate-to-personal/
        ├── input.md
        ├── step-01-pattern-miner.md
        ├── step-02-emotion-mapper.md
        ├── step-03-skeleton-builder.md
        ├── step-04-adaptation-writer.md
        ├── step-05-variation-generator.md
        ├── step-06-hook-specialist.md
        ├── step-07-similarity-guard.md
        ├── step-08-risk-filter.md
        ├── step-09-market-judge.md
        ├── step-10-final-packager.md
        ├── final-candidates.md
        ├── approval.md
        ├── metrics.md
        └── run.json
```

### 4.1 ディレクトリ命名規則

```
runs/YYYYMMDD-HHMM-{product-slug}-{source}-{target}/
```

例:
- `runs/20260905-1430-security-diagnosis-personal-to-corporate/`
- `runs/20260905-1500-system-dev-corporate-to-personal/`

### 4.2 ファイル説明

| ファイル | 目的 |
|----------|------|
| `input.md` | test-case から生成した client_context と step-01 入力 |
| `step-01-pattern-miner.md` | Pattern Miner の出力 |
| `step-02-emotion-mapper.md` | Emotion Mapper の出力 |
| `step-03-skeleton-builder.md` | Skeleton Builder の出力 |
| `step-04-adaptation-writer.md` | Adaptation Writer の出力 |
| `step-05-variation-generator.md` | Variation Generator の出力（10 案） |
| `step-06-hook-specialist.md` | Hook Specialist の出力 |
| `step-07-similarity-guard.md` | Similarity Guard の判定結果 |
| `step-08-risk-filter.md` | Risk Filter の判定結果 |
| `step-09-market-judge.md` | Market Judge の採点・上位 5 本 |
| `step-10-final-packager.md` | Final Packager の出力 |
| `final-candidates.md` | 最終候補 5 本・最終おすすめ 1 本の整理 |
| `approval.md` | 人間承認パッケージ |
| `metrics.md` | 24h impressions 等の指標記録欄 |
| `run.json` | run metadata |

### 4.3 注意

- 今回はディレクトリやファイルを作成しない。
- 本設計書では構成案のみを示す。

---

## 5. Run Metadata Schema

`run.json` の設計案を以下に示す。

```json
{
  "run_id": "20260905-1430-system-dev-corporate-to-personal",
  "created_at": "2026-09-05T14:30:00+09:00",
  "updated_at": "2026-09-05T15:45:00+09:00",
  "product_service": "AI活用型短納期システム開発",
  "client_context": {
    "industry": "IT / システム開発",
    "target_audience": "中小企業の経営層・IT責任者・開発責任者",
    "posting_purpose": "AI活用型短納期システム開発サービスの認知獲得と問い合わせ導線獲得",
    "tone": "客観的・信頼的な法人トーン",
    "character_limit": 200,
    "hashtag_policy": ["#システム開発", "#AI活用"]
  },
  "source_account_type": "corporate",
  "account_type": "personal",
  "desired_cta_style": "reply / discussion / experience_sharing",
  "allowed_persona_expression": "僕 / 私 / 自分 / 主語省略",
  "risk_tolerance": "balanced",
  "source_post_reference_type": "fictional_sample",
  "source_post_storage_policy": "do_not_save_third_party_text",
  "prompt_version": "phase-1-final",
  "model": "kimi-k2.7-code",
  "status": "pending_approval",
  "final_verdict": "low",
  "selected_candidate_id": "01",
  "selected_candidate_text": "AIでコードが書けるようになったのはいいけど...",
  "human_approved": false,
  "approved_by": null,
  "approved_at": null,
  "posted_at": null,
  "post_url": null,
  "metrics_due_at": null,
  "impressions_24h": null,
  "engagement_24h": null,
  "clicks_24h": null,
  "replies_24h": null,
  "notes": "第2商材 corporate→personal cross 変換実験"
}
```

### 5.1 フィールド説明

| フィールド | 型 | 説明 |
|------------|-----|------|
| `run_id` | string | run folder 名と一致する一意ID |
| `created_at` | string (ISO8601) | run 作成日時 |
| `updated_at` | string (ISO8601) | 最終更新日時 |
| `product_service` | string | 商材名 |
| `client_context` | object | 業種・ターゲット・投稿目的・トーン等 |
| `source_account_type` | string | personal / corporate |
| `account_type` | string | personal / corporate |
| `desired_cta_style` | string | reply/discussion/experience_sharing または checklist/consultation/document_request |
| `allowed_persona_expression` | string | 許容される一人称表現 |
| `risk_tolerance` | string | balanced / conservative |
| `source_post_reference_type` | string | fictional_sample / client_original / etc. |
| `source_post_storage_policy` | string | 実在第三者投稿本文の保存禁止を明示 |
| `prompt_version` | string | 使用した prompt セットのバージョン |
| `model` | string | 使用モデル |
| `status` | string | pending / in_progress / pending_approval / approved / rejected / posted / metrics_recorded |
| `final_verdict` | string | low / medium / high |
| `selected_candidate_id` | string | 採用された候補のID |
| `selected_candidate_text` | string | 採用された候補の本文 |
| `human_approved` | boolean | 人間承認済みか |
| `approved_by` | string | 承認者名（任意） |
| `approved_at` | string (ISO8601) | 承認日時 |
| `posted_at` | string (ISO8601) | 投稿日時 |
| `post_url` | string | 投稿URL（任意） |
| `metrics_due_at` | string (ISO8601) | 24h metrics 計測予定時刻 |
| `impressions_24h` | number | 24h 後インプレッション数 |
| `engagement_24h` | number | 24h 後エンゲージメント数 |
| `clicks_24h` | number | 24h 後クリック数（任意） |
| `replies_24h` | number | 24h 後リプライ数（任意） |
| `notes` | string | 備考 |

---

## 6. Human Approval Package

`approval.md` の設計案を以下に示す。

```markdown
# Human Approval Package

## Run Information
- run_id: 20260905-1430-system-dev-corporate-to-personal
- product_service: AI活用型短納期システム開発
- source_account_type: corporate
- account_type: personal
- desired_cta_style: reply / discussion / experience_sharing
- risk_tolerance: balanced
- created_at: 2026-09-05T14:30:00+09:00

## Final Candidates

### Candidate 01
[最終候補1本目の本文]

### Candidate 02
[最終候補2本目の本文]

### Candidate 03
[最終候補3本目の本文]

### Candidate 04
[最終候補4本目の本文]

### Candidate 05
[最終候補5本目の本文]

## Recommended Candidate

### Candidate 01
[最終おすすめ1本の本文]

**Selection Reason:**
[選定理由]

## Risk Comments
- Similarity: low
- Exaggeration: low
- Controversy risk: low
- Account type fit: good
- CTA fit: good
- Product connection: natural

## Approval Decision

- [ ] Approve as-is
- [ ] Approve with edits
- [ ] Reject
- [ ] Request re-generation

## Edit Instructions
[承認者が修正指示を記入する欄]

## Pre-Posting Checklist
- [ ] Brand fit confirmed
- [ ] No factual errors
- [ ] Not a copy of original post
- [ ] No controversy risk
- [ ] Account type appropriate
- [ ] CTA appropriate
- [ ] Image prepared (if needed)
- [ ] Hashtags confirmed
- [ ] Posting time confirmed

## Posting Record
- posted_at: ___________
- post_url: ___________
- posted_by: ___________

## 24h Metrics Record
- metrics_due_at: ___________
- impressions_24h: ___________
- engagement_24h: ___________
- replies_24h: ___________
- clicks_24h: ___________
- notes: ___________
```

### 6.1 approval.md に含める必須項目

- 最終候補 5 本
- 最終おすすめ 1 本
- 採用 / 不採用 / 修正承認 / 再生成要求の選択肢
- 修正指示欄
- 類似性コメント
- リスクコメント
- account_type 適合性
- CTA 適合性
- 投稿前チェックリスト
- 投稿後記録欄（posted_at, post_url, posted_by）
- 24h impressions 記録欄

---

## 7. Step Execution Model

半自動化の実行モデルを以下で比較する。

### A. Fully Manual
- 人間が各 step を手動で実行。
- メリット: 柔軟性が高い。
- デメリット: 反復実験が非効率、ログ管理が煩雑。

### B. Prompt Copy Assisted
- 人間が prompt をコピーし、手動で変数を埋めて実行。
- メリット: Phase 1 資産をそのまま活用できる。
- デメリット: 依然として手作業が多い、ミスが起きやすい。

### C. File-Based Semi-Automation
- 各 step の入出力をファイルで管理し、人間が確認しながら進める。
- メリット:
  - Phase 1 資産を活かせる
  - Kimi K2.7 / OpenCode Go で低コストに回せる
  - 人間承認を残せる
  - 途中結果を確認できる
  - 失敗時に途中から再開できる
  - 自動投稿まで行かないため安全
- デメリット:
  - 完全自動化ほど速くない
  - ファイル管理のルールが必要

### D. Full Automation
- API 連携・n8n・自動投稿まで含む完全自動化。
- メリット: 最も効率的。
- デメリット:
  - 法務・倫理リスクが高い
  - 人間承認が薄れる
  - 実装コストが高い
  - Phase 2-A のスコープ外

### 推奨: C. File-Based Semi-Automation

本設計では **C. File-Based Semi-Automation** を推奨する。

理由:
- Phase 1 の prompts/docs/result をそのまま活用できる。
- 人間承認を維持しつつ、機械的なファイル管理を効率化できる。
- 自動投稿や API 連携を導入せず、安全に運用できる。
- Kimi K2.7 / OpenCode Go で追加コストなく実行可能。
- 途中結果を人間が確認できるため、品質を担保しやすい。

---

## 8. Error Handling / Recovery

各種エラー・異常時の対応を設計する。

### 8.1 Step 失敗時
- 該当 step の input/output を確認する。
- 必要に応じて prompt 入力を修正し、同じ step を再実行する。
- 再実行後、output ファイルを上書き保存する。
- `run.json` の `status` を `in_progress` に維持。

### 8.2 出力形式崩れ
- step output が Markdown 構造を崩した場合、人間が目視で修正する。
- 崩れた step 以前のファイルはそのまま再利用可能。

### 8.3 account_type 不一致
- step output で `account_type` または `source_account_type` が指定と異なる場合、
  その step を再実行する。
- `Adaptation Writer` または `Variation Generator` の入力を見直す。

### 8.4 CTA 不一致
- 生成された候補の CTA が `desired_cta_style` と異なる場合、
  `Variation Generator` または `Adaptation Writer` の指示を強化して再実行。

### 8.5 Similarity Guard medium/high
- medium/high の候補は修正または除外する。
- `Similarity Guard` の判定理由を参考に、`Variation Generator` / `Hook Specialist` を再実行。

### 8.6 Risk Filter medium/high
- medium/high の候補は修正または除外する。
- `Risk Filter` の判定理由を参考に、NG 表現を除去して再生成。

### 8.7 Market Judge で採用不可
- 全候補のスコアが低い場合、step-05 まで遡って方向性を変更する。
- または test-case の条件を見直す。

### 8.8 人間承認 NG
- `approval.md` に修正指示を記入し、該当 step まで遡って再実行。
- 承認 NG の理由を `run.json` の `notes` に記録。

### 8.9 posted_at 未記録
- 投稿後、人間が `metrics.md` と `run.json` に `posted_at` を記録する。
- 未記録でも投稿自体は有効だが、24h metrics の紐付けが困難になる。

### 8.10 24h metrics 未記録
- 24h 後に人間が手動で metrics を記録する。
- 未記録でも投稿自体は有効だが、勝敗測定に使えない。
- `run.json` の `status` は `posted` のまま `metrics_recorded` に遷移しない。

### 8.11 git 未 push 状態
- 実験結果はローカル `runs/` 内に保存されるため、git 未 push でも実験は可能。
- ただし、チーム共有やバックアップのために定期的な push を推奨。
- `runs/` 配下のファイルは `.gitignore` 扱いにするか、機密情報を含まない範囲で commit するかを運用で決める。

---

## 9. Governance / Safety Rules

Phase 2-A の半自動化において、以下のガバナンス・安全基準を遵守する。

1. **自動投稿禁止**
   - いかなる段階でも、SNS への自動投稿を行わない。
   - 投稿は人間が手動で行う。

2. **人間承認必須**
   - `approval.md` に記載された最終おすすめ案は、人間が承認して初めて投稿対象となる。
   - `human_approved` が `true` になるまで、投稿してはならない。

3. **実在第三者投稿の本文保存禁止**
   - バズ投稿の全文コピーは保存しない。
   - 構造・感情・反応設計のみを利用する。
   - `source_post_storage_policy` を `do_not_save_third_party_text` とする。

4. **構造・感情・反応設計のみ利用**
   - 元投稿の文言そのものを転用しない。
   - パターン・フレーム・感情導線を再利用する。

5. **虚偽体験禁止**
   - 架空の本人実体験・企業版一人称体験を生成・投稿しない。

6. **根拠不明実績禁止**
   - 「多くの企業で」「導入企業では」等の根拠不明な実績表現を使用しない。

7. **効果保証禁止**
   - 「必ず」「完全」「防げます」「解決します」等の効果保証表現を使用しない。

8. **account_type 確認必須**
   - 全 step で `account_type` と `source_account_type` を明示し、確認する。

9. **source_account_type 確認必須**
   - cross 変換時は、変換元・変換先の両方を常に認識する。

10. **final package なしで投稿禁止**
    - `approval.md` と `final-candidates.md` が生成されていない run は、投稿対象にしない。

11. **metrics 未記録でも投稿自体は可**
    - 24h impressions が未記録でも、承認済みの投稿は実行可能。
    - ただし、未記録の場合は勝敗測定に使えない。

---

## 10. Phase 2-A Deliverables

Phase 2-A で最終的に作成すべき成果物は以下の通り。

| 成果物 | 形式 | 状態 |
|--------|------|------|
| Local assist design document | `docs/phase-2-local-assist-design.md` | 本設計書で作成 |
| Run directory convention | 本設計書 4. で定義 | 設計済み |
| Run metadata schema | 本設計書 5. で定義 | 設計済み |
| Approval package template | 本設計書 6. で定義 | 設計済み |
| Metrics recording schema | 本設計書 5. / 6. で定義 | 設計済み |
| Implementation backlog | 本設計書 11. で定義 | 設計済み |

### 10.1 今回作成しないもの

- `runs/` ディレクトリ
- 実行スクリプト
- CLI ツール
- API 連携
- n8n ワークフロー

---

## 11. Implementation Backlog

Phase 2-B 以降で実装を検討する項目を、優先順位付きで整理する。

### P0: まず作るべき

1. **run folder generator**
   - test-case から `runs/YYYYMMDD-HHMM-{slug}/` を生成する。
   - `input.md` と `run.json` の雛形を同時に生成する。

2. **test-case to input.md generator**
   - `experiments/phase-1/test-case-XXX.md` から `input.md` と `run.json` を生成する。
   - client_context を自動抽出する。

3. **approval.md template**
   - `approval.md` の雛形を生成する。
   - 最終候補 5 本・最終おすすめ 1 本のプレースホルダーを含む。

### P1: 次に作るべき

4. **prompt input composer**
   - 前 step の output を読み込み、次 step の入力 Markdown を生成する。
   - 人間がコピーして Kimi/OpenCode に貼り付けられる形にする。

5. **step output validator**
   - step output に `account_type` / `source_account_type` が含まれているか検証。
   - Markdown 構造が崩れていないか簡易チェック。

6. **final package generator**
   - `step-09-market-judge.md` / `step-10-final-packager.md` から
     `final-candidates.md` と `approval.md` を生成する。

7. **metrics.md generator**
   - `metrics.md` の雛形を生成する。

### P2: 余裕があれば

8. **run index generator**
   - `runs/index.md` を自動更新し、全 run の一覧・status を管理する。

9. **simple CLI or batch launcher**
   - PowerShell または Python で、step 間のファイルコピー・雛形生成を支援する。
   - ただし、Kimi/OpenCode 自体の実行は含めない。

10. **README update**
    - Phase 2 の運用方法を README.md に追記する。

---

## 12. Recommended Next Step

**Phase 2-B: run directory convention and metadata templates**

### 理由

- いきなり実行スクリプトを作るより、まずログと成果物の型を固める方が安全。
- `run.json` と `approval.md` の雛形があれば、人間が手動で運用しながら改善できる。
- 24h impressions 評価につながる構造を先に作っておく。
- 人間承認の導線を崩さない。

### Phase 2-B で作成するもの

1. `runs/` ディレクトリ（空）
2. `runs/.gitkeep` または `runs/README.md`
3. `templates/run.json` （雛形）
4. `templates/approval.md` （雛形）
5. `templates/metrics.md` （雛形）
6. `templates/input.md` （雛形）
7. `docs/phase-2-b-run-convention.md` （運用ガイド）

### Phase 2-B で行わないこと

- 自動実行スクリプトの作成
- API 連携
- 自動投稿
- prompt 修正
- 既存 result/test-case の変更

---

## 13. Non-Goals

以下は Phase 2-A / 2-B および本プロジェクト全体で**行わない**。

1. **自動投稿**
   - 人間が手動で投稿する。

2. **SNS API 連携**
   - X/Twitter API 等とは連携しない。

3. **n8n 連携**
   - ワークフロー自動化ツールは使用しない。

4. **Claude 版 SNS システムとの統合**
   - Luvira SNS Factory は独立したプロジェクトとして運用する。

5. **LuviraMemory 連携**
   - 本プロジェクトの対象外。

6. **AI スコアだけで最終判断**
   - Market Judge のスコアは参考。最終判断は人間が行う。

7. **実在投稿本文のコピー保存**
   - 構造・感情・反応設計のみを利用する。

8. **完全自動運用**
   - 人間承認を必須とする半自動化に留める。

---

## 14. Appendices

### A. 用語集

| 用語 | 説明 |
|------|------|
| run | 1 回の投稿候補生成実験単位 |
| client_context | 商材・業種・ターゲット・投稿目的等の文脈情報 |
| source_account_type | 元投稿のアカウント種別 |
| account_type | 転用先アカウント種別 |
| desired_cta_style | 希望する CTA スタイル |
| allowed_persona_expression | 許容される一人称表現 |
| risk_tolerance | リスク許容度 |

### B. 参考ファイル

- `experiments/phase-1/PHASE-1-CLOSURE-REVIEW.md`
- `experiments/phase-1/result-005-corporate-to-personal-system-dev.md`
- `experiments/phase-1/result-006-personal-to-corporate-system-dev.md`
- `experiments/phase-1/result-007-personal-to-personal-system-dev.md`
- `experiments/phase-1/result-008-corporate-to-corporate-system-dev.md`
- `docs/workflow.md`
- `docs/prompt-design.md`
- `docs/evaluation-rule.md`
- `docs/safety-policy.md`

### C. 更新履歴

- 2026-09-05: Phase 2-A 設計初版作成
