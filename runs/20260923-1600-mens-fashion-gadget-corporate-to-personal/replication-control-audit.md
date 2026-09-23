# Replication Control Audit: OPS-005 → OPS-009

## Replication Source

- ops_id: `OPS-005`
- run_id: `20260910-1149-mens-fashion-gadget-corporate-to-personal`
- post_url: `https://x.com/ritsu_opt/status/2098406679058797046?s=20`
- posted_at: `2026-09-11T22:41:00+09:00`

## Actual Controls Extracted from OPS-005

| Control | OPS-005 Actual Value | OPS-009 Plan | Match Classification |
|---------|----------------------|--------------|----------------------|
| account_type | `personal` | `personal` | **EXACT MATCH** |
| transformation | `corporate-to-personal` | `corporate-to-personal` | **EXACT MATCH** |
| platform | `X` | `X` | **EXACT MATCH** |
| hypothesis_id | `H003` | `H003` | **EXACT MATCH** |
| content_angle | `爪・髪・香り` | `爪・髪・香り` | **EXACT MATCH** |
| Target Tag | `#40代ファッション` | `#40代ファッション` | **EXACT MATCH** |
| Content Angle Tag | `#身だしなみ` | `#身だしなみ` | **EXACT MATCH** |
| hashtag_count | `2` | `2` | **EXACT MATCH** |
| image | `none` | `none` | **EXACT MATCH** |
| URL | `none` | `none` | **EXACT MATCH** |
| CTA style | `reply / discussion / experience_sharing` | `reply / discussion / experience_sharing` | **EXACT MATCH** |
| information_structure | `empathy / awareness` | `empathy / awareness` | **EXACT MATCH** |
| post length | ~130 characters (body) | ~130 characters (body, identical text) | **EXACT MATCH** |
| posting_time | `22:41 JST` | `22:40–22:45 JST` | **NEAR MATCH** |
| tone | 観察・気づきの個人口調 | 観察・気づきの個人口調 (identical text) | **EXACT MATCH** |
| hook structure | 穏やかな対比フック（服 vs 身だしなみ） | 穏やかな対比フック（服 vs 身だしなみ, identical text) | **EXACT MATCH** |

## Notes

- No control is classified as **INTENTIONAL DIFFERENCE**.
- No control is classified as **UNKNOWN**.
- Posting time band is a near match because the exact minute cannot be guaranteed before actual posting, but the band is intentionally matched to OPS-005.
- Post length, tone, and hook structure are exact matches because the final selected text is identical to OPS-005 `selected_candidate_text` in run.json representation.

## Replication Fidelity Summary

- EXACT MATCH: 15 items
- NEAR MATCH: 1 item
- INTENTIONAL DIFFERENCE: 0 items
- UNKNOWN: 0 items

## Prohibited Differences

The following were explicitly avoided in OPS-009 candidate generation:

- Strong viral hooks
- Practical checklists
- Numerical claims
- New structure formats
- New CTA styles
- Different hashtags (e.g., `#爪髪香り`)
- Daytime posting optimization
- Image attachments
- URL inclusion

---

- audit_date: `2026-09-23`
- audited_by: `kimi-k2.7-code`
- human_review_required: `true`
