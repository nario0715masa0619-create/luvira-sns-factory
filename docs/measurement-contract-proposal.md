# Measurement Contract Proposal

## Status

`proposal` — awaiting human review and approval. Not canonical until explicitly adopted.

## Purpose

Define the minimum operational rules for 24h metrics so that SNS Factory experiments produce comparable evidence.

## Scope

Applies to all organic X posts used for Distribution Learning / hypothesis evaluation in Luvira SNS Factory.

## Definitions

| Term | Definition |
|------|------------|
| `posted_at` | The actual timestamp when the post was published. Recorded in ISO-8601 with timezone (`+09:00` for JST). |
| `metrics_due_at` | `posted_at + 24 hours`. The target time for the strict 24h observation. |
| `pre_measurement_reminder` | `metrics_due_at - 60 minutes`. A reminder to prepare for observation. |
| `measurement_reminder` | `metrics_due_at`. The primary reminder to take the screenshot / record metrics. |
| `measurement_tolerance` | The allowed window around `metrics_due_at` for a strict 24h observation. Proposed: `±15 minutes`. |

## Measurement Window Classification

| Window | Elapsed Time from `metrics_due_at` | Usable for Ratio Comparison? | Default Result Label |
|--------|------------------------------------|------------------------------|----------------------|
| `strict_24h_recorded` | within `±15 minutes` | yes | depends on metrics |
| `near_24h_observation` | `>15 min` and `≤60 min` | no | `non_comparable` |
| `delayed_observation` | `>60 minutes` | no | `non_comparable` |
| `late_measurement` | historical term for observations taken hours/days later | no | `non_comparable` |
| `not_recorded` | no observation taken | no | `invalid_missing_metrics` |

## Success Criteria for a Comparable Run

A run may be used for hypothesis evaluation or ratio comparison only if:

1. `posted_at` is recorded.
2. `metrics_due_at` is recorded.
3. Observation is taken within `measurement_tolerance` of `metrics_due_at`.
4. `measurement_status` is set to `strict_24h_recorded`.
5. No other canonical control was changed during the experiment.

## Reminder Protocol

1. At post time, the agent records `posted_at` and `metrics_due_at` in `run.json` and `approval.md`.
2. A `reminder.md` is created in the run folder with the due time and tolerance window.
3. At `pre_measurement_reminder`, the agent adds a visible note to the run folder or log.
4. At `measurement_reminder`, the agent expects the human operator to record metrics.
5. If metrics are missed, the agent records `non_comparable` and does not compute ratios.

## Tolerance Justification

- `±15 minutes` is narrow enough to keep the observation within the same platform traffic cycle for most posts.
- It is wide enough to accommodate normal human response delay.
- It matches the precision needed for low-impression accounts where small time windows can matter.

## Open Questions

1. Should the tolerance differ for accounts with very high posting frequency?
2. Should weekends/holidays affect the due time or tolerance?
3. Should platform-native analytics (e.g., X Analytics) be the sole source, or are third-party tools allowed?

## Adoption

This contract becomes canonical only after:

- Human reviewer approval.
- Update to `docs/evaluation-rule.md` or `docs/data-schema.md`.
- A reference added in `knowledge/mens-fashion-gadget/experiment-log.md` rules section.

---

- proposal_date: `2026-09-23`
- proposed_by: `kimi-k2.7-code`
- human_approval_required: `true`
