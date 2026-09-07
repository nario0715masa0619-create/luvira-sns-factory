# Post Analysis

## Run Metadata

- run_id: `RUN_ID`
- hypothesis_id: `HYPOTHESIS_ID`
- content_genre: `CONTENT_GENRE`
- content_angle: `CONTENT_ANGLE`
- account_type: `ACCOUNT_TYPE`
- source_account_type: `SOURCE_ACCOUNT_TYPE`
- platform: `PLATFORM`
- posted_at: `YYYY-MM-DDTHH:MM:SS+09:00`
- post_url: `https://...`
- analyzed_at: `YYYY-MM-DDTHH:MM:SS+09:00`

## Posted Content

- final_post_text: `POSTED_TEXT`
- image_attached: `yes / no`
- image_type: `IMAGE_TYPE_OR_UNKNOWN`
- hashtags: `HASHTAGS`
- cta: `CTA_TEXT`

## 24h Metrics

- impressions_24h: ``
- likes_24h: ``
- replies_24h: ``
- reposts_24h: ``
- bookmarks_24h: ``
- profile_clicks_24h: ``
- follows_24h: ``

## Calculated Metrics

- engagement_rate_24h: ``
- reply_rate_24h: ``
- bookmark_rate_24h: ``
- profile_click_rate_24h: ``
- follow_conversion_rate_24h: ``

## Quantitative Review

| Signal | Level | Notes |
|--------|-------|-------|
| reach_signal | `strong / ok / weak / unknown` | |
| engagement_signal | `strong / ok / weak / unknown` | |
| conversation_signal | `strong / ok / weak / unknown` | |
| save_signal | `strong / ok / weak / unknown` | |
| conversion_signal | `strong / ok / weak / unknown` | |

## Qualitative Review

| Aspect | Level | Notes |
|--------|-------|-------|
| hook_strength | `strong / ok / weak / unknown` | |
| readability | `strong / ok / weak / unknown` | |
| specificity | `strong / ok / weak / unknown` | |
| commentability | `strong / ok / weak / unknown` | |
| saveability | `strong / ok / weak / unknown` | |
| target_fit | `strong / ok / weak / unknown` | |
| brand_fit | `strong / ok / weak / unknown` | |
| originality | `strong / ok / weak / unknown` | |
| overlap_with_recent_posts | `none / low / medium / high` | |

## Diagnosis

- strongest_signal: `STRONGEST_SIGNAL`
- weakest_signal: `WEAKEST_SIGNAL`
- likely_reason_for_result: `REASON`
- what_worked: `WHAT_WORKED`
- what_did_not_work: `WHAT_DID_NOT_WORK`
- uncertainty: `UNCERTAINTY`
- external_factors: `EXTERNAL_FACTORS`

## Result Label

- cold_start_label: `signal_detected / weak_signal / no_signal / invalid_missing_metrics`
- pdca_label: `win / promising / neutral / weak / reject / not_applicable`
- label_reason: `REASON_FOR_LABEL`
- confidence: `low / medium / high`

## Human Review

- reviewed_by: `NAME`
- human_notes: `HUMAN_NOTES`
- approved_for_learning: `yes / no`

---

## Rules

- `metrics.md` は事実記録、`post-analysis.md` は解釈に限定する。
- 1投稿だけで winning pattern と断定しない。
- 不明な値は `unknown` と書く。
- `0` と `unknown` を区別する。
- 実 metrics がない状態で断定しない。
