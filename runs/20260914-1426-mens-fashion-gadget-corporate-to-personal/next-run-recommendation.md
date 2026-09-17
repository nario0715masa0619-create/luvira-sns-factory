# Next Run Recommendation

## Origin

- previous_run_id: `20260914-1426-mens-fashion-gadget-corporate-to-personal`
- previous_ops_id: `OPS-006`
- previous_hypothesis_id: `H009`
- recommendation_date: `2026-09-17`
- status: `pending_human_review`

## OPS-006 Summary

- content_angle: `営業/経営者の第一印象`
- posted_at: `2026-09-14T22:08:00+09:00`
- measurement_status: `24h_missed_delayed_observation_recorded`
- delayed observation: `impressions=26, likes=1, replies=1, reposts=0（約65時間後）`
- result_label: `non_comparable`
- reason: `strict 24h measurement missing`

## OPS-007 Recommendation

### Recommended Hypothesis

- **hypothesis_id**: `H007`
- **content_angle**: `若作りしないジャケット`
- **why_next**:
  - Experiment Queue の次に計画されていた候補。
  - H003（爪・髪・香り）と H009（営業/経営者の第一印象）とは異なるファッション選択軸であり、直近2投稿との重複が少ない。
  - H007 は high priority / untested であり、ジャケットという具体的なアイテムを扱うことで、40代男性の「服選びを見直したい」ニーズにアプローチできる。
  - OPS-005 / OPS-006 ともに measurement missed で winning pattern も losing pattern も得られていないため、次は queue 通りの新しい content_angle で角度分散を進めるのが最も合理的。

### Candidate Alternatives Considered

| hypothesis_id | content_angle | status | reason for not selecting now |
|---------------|---------------|--------|------------------------------|
| H003 | 爪・髪・香り | untested / 再検証候補 | 直近 OPS-005 と同じ content_angle。連投は避ける。後回し。 |
| H006 | ワイヤレスイヤホン | untested | ガジェット軸。H007 との優先度は同等だが、ファッション軸の H007 を先に検証して角度分散を保つ。 |
| H008 | 40代NGファッション | untested | ネガティブ訴求のリスクが高い。優先度は H007 より低い。 |
| H010 | 買ってよかった小物3選 | untested | 実体験ベースが望ましく、即座に生成しにくい。後回し。 |

### Experiment Control

**Fixed（Canonical Control）:**

| Control | Value | Reason |
|---------|-------|--------|
| account_type | `personal` | canonical |
| transformation | `corporate-to-personal` | canonical |
| platform | `X` | canonical |
| Target Tag | `#40代ファッション` | canonical |
| hashtag_count | `2` | canonical |
| image | `none` | canonical（OPS-007 では image 変数は検証しない） |
| URL | `none` | canonical |
| CTA style | `reply / discussion / experience_sharing` | canonical CTA style |
| posting time | `existing canonical control` | 現時点で固定 |

**Changed Variable:**

| Variable | From | To |
|----------|------|----|
| content_angle | H009 営業/経営者の第一印象 | H007 若作りしないジャケット |
| Content Angle Tag | `#第一印象` | `#ジャケット`（仮） |

> 1-variable experiment の原則により、content_angle 以外は一切変更しない。

### Expected Signal

- primary_signal: `bookmarks / replies`
- desired_reaction: `40代男性が「若作りに見えないジャケットの選び方」を保存・コメントしたい`
- risk: `ファッション助言が偉そうに見える可能性。個人の観察・失敗談を交えて謙虚なトーンを維持する。`

### Draft Direction（Not Final）

> これは推奨方向であり、最終投稿文ではありません。

- hook: `40代になって、若作りに見えないジャケットの選び方って結構むずかしい。`
- angle: `色・素材・丈感のポイントを個人の観察として共有。`
- CTA: `みんなが気をつけてる、若作りに見えないジャケットのポイントは何？`
- tone: 個人アカウントの実感・観察。強い断定や助言的表現を避ける。

## Stop Conditions for OPS-007

- 24h 計測を忘れないこと。metrics_due_at を投稿直後に記録しアラームを設定する。
- 1-variable 原則を守り、content_angle 以外は変更しない。
- 投稿後は厳密な 24h 後に metrics を取得する。

## Human Review Required

- [ ] H007 若作りしないジャケット を OPS-007 に採用する
- [ ] 1-variable experiment（content_angle のみ変更）を了承する
- [ ] 上記 Draft Direction から最終投稿文を生成・承認する
- [ ] OPS-007 の投稿日時を決定する

## Do Not Proceed Until Approved

OPS-007 の run folder 作成、候補生成、投稿、metrics 記録は、本 recommendation が human review 承認されるまで行わない。
