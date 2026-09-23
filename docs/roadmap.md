# Roadmap

## Purpose

Luvira SNS Factory の将来機能候補を管理する。現時点では確定計画ではなく、改善・拡張のアイデア置き場。

---

## Backlog

### Autonomous Hypothesis Engine

**Status**: `pilot_completed`  
**Priority**: `medium`  
**Added**: `2026-09-20`  
**Pilot Completed**: `2026-09-23`

#### Motivation

OPS-005 → OPS-008 の間、Human Reviewer が行ってきた一連の意思決定

```text
Observation → Possible Explanation → Hypothesis → Experiment Design → Research → Fact Check → Experiment Selection
```

は、将来的に SNS Factory 自身が支援・半自動化できる能力である。

#### Proposed Responsibilities

| # | Capability | Description | Pilot Coverage |
|---|------------|-------------|----------------|
| 1 | Past OPS analysis | 過去の run 結果を集計し、pattern / anomaly を抽出する。 | OPS-002〜008 cross-run table |
| 2 | Failure explanation generation | 24h metrics missing などの失敗要因を構造化して記録する。 | measurement miss spiral, 10 explanations |
| 3 | Hypothesis generation | 観察から新しい仮説（content_angle / information_structure / CTA / timing 等）を生成する。 | 6 OPS-009 candidates |
| 4 | Experiment dimension selection | 次に検証すべき1変数を選び、Control を固定する提案を行う。 | 1 dimension changed per candidate |
| 5 | Expected information gain evaluation | 各候補仮説の情報利得を定性的・定量的に評価する。 | 1–5 scoring with rationale |
| 6 | Research requirement判定 | 仮説がファクトチェックを必要とするか判定する。 | low/medium per candidate |
| 7 | Experiment recommendation | 上記を統合して、Human Reviewer への推奨実験を提示する。 | C2 H006 selected |

#### Constraints / Non-Goals

- Human-in-the-loop の最終承認を残す。自動投稿は行わない。
- Canonical Knowledge の勝手な昇格は行わない。
- 既存の run folder / approval / experiment-log 構造を無理に変更しない。

#### Related Files

- `knowledge/mens-fashion-gadget/experiment-log.md`
- `knowledge/mens-fashion-gadget/experiment-queue.md`
- `knowledge/mens-fashion-gadget/hypothesis-pool.md`
- `docs/experiment-design.md`
- `docs/pilots/ops009-autonomous-hypothesis-cycle-pilot.md`

#### Notes

- 実装時は、まず小規模な "hypothesis suggestion" 機能から始め、複数 OPS で安定動作を確認してから責務を拡張する。
- OPS-008 では Human Reviewer が上記プロセスを手動で実行した。結果は `knowledge/mens-fashion-gadget/research/ops008-practical-jacket-fitting.md` に記録済み。
- OPS-009 推奨に向けた初回 Autonomous Hypothesis Cycle Pilot が完了。Human Reviewer の承認待ち。

#### Milestones

1. `2026-09-20` — Concept added to backlog.
2. `2026-09-23` — Pilot executed for OPS-009; artifact `docs/pilots/ops009-autonomous-hypothesis-cycle-pilot.md` created.
3. `2026-09-23` — Human Review Follow-up completed. Initial H006 recommendation revised to **H003 replication** after Experiment Debt analysis. Design learning added: engine must balance Explore / Replicate / Recover Measurement / Exploit modes. Follow-up artifact `docs/pilots/ops009-autonomous-hypothesis-cycle-follow-up.md` and measurement contract proposal `docs/measurement-contract-proposal.md` created.
4. Next — Validate the revised recommendation and measurement contract with OPS-009 strict 24h measurement, then iterate.
