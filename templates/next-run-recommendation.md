# Next Run Recommendation

## Source

- based_on_run_id: `RUN_ID`
- based_on_hypothesis_id: `HYPOTHESIS_ID`
- based_on_result_label: `RESULT_LABEL`
- generated_at: `YYYY-MM-DDTHH:MM:SS+09:00`

## Recommendation

- recommended_next_run_type: `repeat / iterate / pivot / pause`
- recommended_hypothesis_id: `HYPOTHESIS_ID`
- recommended_content_genre: `CONTENT_GENRE`
- recommended_content_angle: `CONTENT_ANGLE`
- recommended_target_reader: `TARGET_READER`
- desired_reaction: `DESIRED_REACTION`
- hook_direction: `HOOK_DIRECTION`
- cta_direction: `CTA_DIRECTION`
- post_format: `POST_FORMAT`
- media_recommendation: `MEDIA_RECOMMENDATION`

## Reason

- why_this_next: `WHY_THIS_NEXT`
- evidence: `EVIDENCE`
- uncertainty: `UNCERTAINTY`
- risk_notes: `RISK_NOTES`

## Overlap Avoidance

- recent_related_runs: `RECENT_RUNS`
- overlap_risk: `low / medium / high`
- avoid_topics: `AVOID_TOPICS`
- avoid_phrases: `AVOID_PHRASES`
- avoid_items: `AVOID_ITEMS`
- required_difference_from_recent_posts: `REQUIRED_DIFFERENCE`

## Draft Input Snippet

次回 run の `input.md` に貼れる形で書く。

```text
content_genre: CONTENT_GENRE
content_angle: CONTENT_ANGLE
target_reader: TARGET_READER
desired_reaction: DESIRED_REACTION
hook_direction: HOOK_DIRECTION
cta_direction: CTA_DIRECTION
avoid_overlap: AVOID_OVERLAP
previous_learning: PREVIOUS_LEARNING
```

## Human Approval

- approved_for_next_run: `yes / no`
- human_notes: `HUMAN_NOTES`

---

## Rules

- 直近2投稿と同じ切り口を避ける。
- バッグの中身系を連投しない。
- OPS-002 の metrics が出るまでは OPS-003 は投稿保留。
- `repeat` は再現性確認目的の場合のみ。
- `pivot` は `no_signal` の場合に使う。
- `iterate` は `weak_signal / promising` の場合に使う。
