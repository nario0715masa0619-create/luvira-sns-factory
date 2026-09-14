# Next Run Recommendation

## Source

- based_on_run_id: `20260910-1149-mens-fashion-gadget-corporate-to-personal`
- based_on_ops_id: `OPS-005`
- based_on_hypothesis_id: `H003`
- based_on_result_label: `non_comparable`
- generated_at: `2026-09-14T15:00:00+09:00`

## Recommendation

- recommended_next_run_type: `pivot`
- recommended_hypothesis_id: `H009`
- recommended_content_genre: `40代ファッション×ガジェット`
- recommended_content_angle: `H009 営業/経営者の第一印象`
- recommended_target_reader: `40代男性 / 経営者 / 営業職 / 見た目と仕事道具を整えたい人`
- desired_reaction: `共感リプライ・経験共有。ビジネス文脈での共感を狙う。`
- hook_direction: `「40代になって気づいた」型を維持。content_angle のみを H009 に変更。`
- cta_direction: `reply / discussion / experience_sharing（OPS-004 までの canonical CTA 形式を維持。 exact 文言は content_angle に合わせて調整してもよいが、style は固定）`
- post_format: `text-only`
- media_recommendation: `none（OPS-006 では変更変数を content_angle のみに限定するため画像なしを維持）`

## Experiment Control

OPS-006 で変更する変数は **content_angle のみ**。

| Condition | OPS-006 Value | Change? |
|-----------|---------------|---------|
| account_type | personal | no |
| transformation | corporate-to-personal | no |
| Target Tag | #40代ファッション | no |
| hashtag count | 2 | no |
| Content Angle Tag | #第一印象 等、H009 に応じたタグ | yes（content_angle と連動） |
| image | none | no |
| URL | none | no |
| CTA style | reply / discussion / experience_sharing（canonical） | no |
| posting_time | 既存Controlに準ずる | no |
| content_angle | H009 営業/経営者の第一印象 | **yes** |

## Reason

- why_this_next: `OPS-005 は 24h metrics missed のため、H003 の勝敗は未確定。次回は既存Control条件を維持したまま content_angle のみを変更し、H009 営業/経営者の第一印象を検証する。`
- evidence: `OPS-005 delayed observation: impressions=29, likes=1, replies=1, reposts=0。24h 計測なしのため正式比較不可。`
- uncertainty: `高い。delayed observation 値だけでは、H003 の構造・CTA・画像・時間帯の効果を分離できない。`
- risk_notes: `H009 はビジネス色が強くなりすぎないよう注意。個人アカウント口調を維持し、「上から目線」にならないようにする。`

## Overlap Avoidance

- recent_related_runs: `OPS-002（バッグの中身、metrics_recorded）、OPS-003（バッグの中身、held）、OPS-004（靴の手入れ、metrics_recorded）、OPS-005（爪・髪・香り、non_comparable）`
- overlap_risk: `low`（H009 は H003/H002/H001 とは異なる切り口）
- avoid_topics: `バッグの中身、靴の手入れ、爪・髪・香り（即座の再検証を避ける）`
- avoid_phrases: `「みんなのバッグの中身、何が必須？」、「みんなの靴の手入れ、何が必須？」`
- avoid_items: `財布、ガジェットポーチ、ワイヤレスイヤホン、靴磨きセットの同じ組み合わせ`
- required_difference_from_recent_posts: `content_angle を H009 営業/経営者の第一印象 に変更。Target Tag は固定（#40代ファッション）し、Content Angle Tag を #第一印象 等に切り替える。image / URL / CTA style / posting time は既存Controlを維持。`

## Draft Input Snippet

次回 run の `input.md` に貼れる形で書く。

```text
content_genre: 40代ファッション×ガジェット
content_angle: H009 営業/経営者の第一印象
target_reader: 40代男性 / 経営者 / 営業職 / 見た目と仕事道具を整えたい人
desired_reaction: 共感リプライ・経験共有。ビジネス文脈での共感を狙う。
hook_direction: 「40代になって気づいた」型を維持。content_angle のみ変更。
cta_direction: reply/discussion/experience_sharing（canonical CTA style を維持。exact 文言は H009 に合わせる）
media: none（OPS-006 では変更変数を content_angle のみに限定）
url: none
hashtags: #40代ファッション + Content Angle Tag（#第一印象 等）
avoid_overlap: バッグの中身、靴の手入れ、爪・髪・香り（即座再検証は避ける）
previous_learning: OPS-005 H003 爪・髪・香りは 24h metrics missed、delayed observation で impressions=29, likes=1, replies=1。正式比較不可。H003 を retired にしない。OPS-006 は既存Control維持の上で content_angle のみ H009 へ変更。
```

## Human Approval

- approved_for_next_run: `pending`
- human_notes: `OPS-006 仮説確定は人間承認後。推奨は H009 営業/経営者の第一印象。image / CTA style / posting time は既存Controlを維持。`

---

## Rules

- 直近2投稿と同じ切り口を避ける。
- バッグの中身系・靴の手入れ系を連投しない。
- OPS-003 は OPS-002 metrics 確認後に判断。
- `repeat` は再現性確認目的の場合のみ。
- `pivot` は `no_signal / non_comparable` の場合に使う。
- `iterate` は `weak_signal / promising` の場合に使う。
- 24h 計測を徹底する。
