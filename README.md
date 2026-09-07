# Luvira SNS Factory

低コストモデルで再現性のあるSNS投稿を量産する、構造転用型生成システム。

## 目的

「luvira-sns-factory」は、OpenCode Go / Kimi K2.7 Code を中心に構築した、低コストSNS投稿生成チームの設計 Repository です。

本 Repository の目的は、AI に投稿を 0→1 で自由生成させるのではなく、実際に伸びたバズ投稿から「構造・感情導線・反応設計」を抽出し、クライアントの商材・ターゲット・投稿目的に置換して再現性のある投稿を生成することです。

## Claude 版とは完全に独立

本システムは、株式会社ルヴィラ（Luvira Inc.）の既存 Claude + Claude Code 版 SNS 生成システムとは**完全に独立した別チーム**として設計されています。

- 補助・レビュー用途ではありません。
- 別理論、別モデル、別コスト構造で運用します。
- 最終評価は両者を直接比較する 24 時間インプレッション数で判定します。

## 初期主力モデル：Kimi K2.7 Code

- 初期主力モデルは **Kimi K2.7 Code** とします。
- Kimi K3 は常用しません。
- K3 は、K2.7 で品質課題が出た場合の比較・検証用に限定します。
- まずは K2.7 単独で、どこまで再現性のある SNS 投稿生成ができるかを検証します。

## 核心理念

1. **0→1 生成をしない**
   AI に自由に投稿を書かせません。

2. **バズ投稿の構造を分析する**
   元投稿の文言を真似るのではなく、構造・感情導線・反応設計だけを抽出します。

3. **構造を置換する**
   抽出した構造をクライアント商材・ターゲット・投稿目的に置き換えます。

4. **低コストで大量横展開する**
   同じ構造から 20〜50 案を生成し、上位候補を選抜します。

5. **リスクをチェックする**
   パクリ感、誇大表現、炎上リスク、事実誤認を必ず確認します。

6. **人間承認後に投稿する**
   自動投稿はしません。必ず人間が承認してから投稿します。

7. **勝敗は数字で決める**
   最終評価は、投稿から **24 時間後のインプレッション数**で行います。

## Repository 構成

```
.
├── README.md
├── docs/
│   ├── product-definition.md
│   ├── team-roles.md
│   ├── workflow.md
│   ├── prompt-design.md
│   ├── evaluation-rule.md
│   ├── experiment-design.md
│   ├── safety-policy.md
│   ├── data-schema.md
│   └── phase-3-a-cold-start-pdca-execution-design.md
├── prompts/
│   ├── 01-pattern-miner.md
│   ├── 02-emotion-mapper.md
│   ├── 03-skeleton-builder.md
│   ├── 04-adaptation-writer.md
│   ├── 05-variation-generator.md
│   ├── 06-hook-specialist.md
│   ├── 07-similarity-guard.md
│   ├── 08-risk-filter.md
│   ├── 09-market-judge.md
│   └── 10-final-packager.md
├── examples/
│   ├── input-sample.md
│   └── output-sample.md
├── scripts/
│   └── new_run_folder.py
├── templates/
│   ├── input.md
│   ├── run.json
│   ├── approval.md
│   └── metrics.md
├── runs/
│   └── README.md
└── experiments/
    └── phase-1/
        ├── README.md
        ├── manual-chain-test-template.md
        ├── test-case-001.md
        └── result-template.md
```

## 使い方（初期段階）

1. `examples/input-sample.md` の形式で入力を用意する。
2. `prompts/01-pattern-miner.md` から `10-final-packager.md` まで順に AI にプロンプトを渡す。
3. 各段階の出力を確認し、必要に応じて人間が修正する。
4. `09-market-judge.md` で上位 5 本と最終おすすめ 1 本を選定する。
5. 人間が最終承認し、手動で投稿する。
6. 24 時間後のインプレッション数を記録し、次の改善に活かす。

## 重要な制約

- 元バズ投稿の文言コピーは禁止。
- 自動投稿は禁止。
- 人間承認は必須。
- 事実確認できない断定は禁止。
- 誇大広告、炎上誘発、法務リスクのある表現は採用しない。
- クライアント機密情報、API キー、`.env`、顧客データをプロンプトやログに投入しない。

## Phase 2 Local Helpers

Phase 2 introduces lightweight local helpers to reduce manual copy-paste while keeping the workflow human-in-the-loop.

- `scripts/new_run_folder.py` — Generate a new run folder from `templates/`.
- `scripts/approval_package_generator.py` — Generate `final-candidates.md` and update `approval.md` from step-09/10 outputs.
- `scripts/run_index_generator.py` — Scan `runs/` and generate `runs/index.md` from each `run.json`.
- `scripts/step_input_composer.py` — Compose input Markdown for the next step of the 10-step prompt chain.
- `docs/phase-2-e-run-folder-generator.md` — Run folder generator usage and design details.
- `docs/phase-2-f-approval-package-generator.md` — Approval package generator usage and design details.
- `docs/phase-2-g-run-index-generator.md` — Run index generator usage and design details.
- `docs/phase-2-h-step-input-composer.md` — Step input composer usage and design details.

These helpers do **not** execute prompts, integrate with APIs, or post automatically.

## License

Proprietary - Luvira Inc.
