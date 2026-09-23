# Autonomous Hypothesis Cycle Pilot: OPS-009 Recommendation

## 1. Purpose & Scope

This is a **pilot artifact** for the Autonomous Hypothesis Engine proposed in `docs/roadmap.md`. It documents the first end-to-end cycle:

```text
Observation → Possible Explanation → Hypothesis → Experiment Design → Research Requirement → Expected Information Gain → Experiment Recommendation
```

- **Target product_slug**: `mens-fashion-gadget`
- **Runs analyzed**: OPS-002 through OPS-008
- **Status**: `pilot / draft` — not canonical knowledge
- **Human review required**: yes

## 2. Data Normalization Notes

Before analysis, two repository inconsistencies were corrected:

1. **OPS-007** was already posted by the human operator but the run folder still showed `status: pending_approval`. It has been updated to `posted` with `posted_at=2026-09-17T15:26:00+09:00` and a delayed observation of `39 impressions / 1 like / 1 reply / 0 reposts`.
2. **OPS-008** has been recorded as `posted` with a near-24h observation (`22/0/0/0` at ~24h42m). No strict 24h metrics exist.

All ratio comparisons to OPS-002 remain disabled because measurement windows differ.

## 3. Cross-Run Normalized Table

| OPS | run_id | hypothesis_id | content_angle | experiment_dimension | posted_at | measurement_window | impressions | likes | replies | reposts | result_label | comparable_to_OPS002 |
|-----|--------|---------------|---------------|----------------------|-----------|--------------------|-------------|-------|---------|---------|--------------|----------------------|
| OPS-002 | 20260906-2132 | H001 | バッグの中身 | content_angle | 2026-09-06 22:35 | late_measurement | 149 | 0 | 0 | 0 | no_signal | no |
| OPS-003 | 20260907-0751 | H001 | バッグの中身 | — | — | not_posted | — | — | — | — | pending | — |
| OPS-004 | 20260908-0801 | H002 | 靴の手入れ | content_angle | 2026-09-09 10:29 | late_24h_measurement | 9 | 0 | 0 | unknown | no_signal | no |
| OPS-005 | 20260910-1149 | H003 | 爪・髪・香り | content_angle | 2026-09-11 22:41 | delayed_observation | 29* | 1* | 1* | 0* | non_comparable | no |
| OPS-006 | 20260914-1426 | H009 | 営業/経営者の第一印象 | content_angle | 2026-09-14 22:08 | delayed_observation | 26* | 1* | 1* | 0* | non_comparable | no |
| OPS-007 | 20260917-1516 | H007 | 若作りしないジャケット | content_angle | 2026-09-17 15:26 | delayed_observation | 39* | 1* | 1* | 0* | non_comparable | no |
| OPS-008 | 20260920-1140 | H007 | 若作りしないジャケット | information_structure | 2026-09-21 00:22 | near_24h_observation | 22** | 0 | 0 | 0 | non_comparable | no |

\* Delayed observation; not strict 24h.  
\*\* Near-24h observation (~24h42m); not strict 24h.

### Key Facts

- Only **OPS-002** and **OPS-004** have any 24h-timed metrics, and both are `late` or `late_24h` rather than strict 24h.
- **OPS-005 through OPS-008** are all `non_comparable` due to missed 24h measurement.
- No run since OPS-002 has produced comparable distribution above the single-digit range.
- The strongest **descriptive** delayed number is OPS-007 (`39`), but it cannot be compared to OPS-002.

## 4. Experiment Coverage Map

| Dimension | Values Tested So Far | Gaps |
|-----------|----------------------|------|
| content_angle | H001 bag, H002 shoe care, H003 grooming, H009 first impression, H007 jacket fit | H006 gadgets, H008 NG fashion, H004/H005 small leather goods |
| information_structure | empathy/awareness (OPS-007), practical information (OPS-008) | comparison list, negative framing, story/narrative |
| CTA style | reply / discussion / experience_sharing only | poll/choice, bookmark-oriented, no explicit CTA |
| image | none | image present, before/after, carousel |
| URL | none | external link (not planned for organic reach tests) |
| hashtags | 2 tags: #40代ファッション + content tag | tag count, tag volume tests |
| account_type | personal | — |
| posting_time | varied, including 22:41 and 00:22 | controlled daytime vs. nighttime test |

**Conclusion from coverage map:** The project is still in early Cold Start. The only dimension with any internal comparison is `information_structure` (OPS-007 vs OPS-008), but the comparison is invalid due to measurement-window mismatch.

## 5. Possible Explanations for Observed Patterns

| # | Explanation | Evidence For | Evidence Against | Testability |
|---|-------------|--------------|------------------|-------------|
| E1 | **Measurement miss spiral.** Most recent runs lack strict 24h data, so real effects are hidden. | 4 of last 5 runs are non-comparable. | — | Fix process and re-test. |
| E2 | **H007 angle fatigue.** Running H007 twice in a row reduced reach for OPS-008. | OPS-008 < OPS-007 descriptively; same angle repeated. | Measurement windows differ; OPS-008 was also night-posted. | Test H007 again only after several other angles. |
| E3 | **Night posting suppresses early distribution.** OPS-008 posted at 00:22 JST. | Low near-24h impressions. | Single data point; no controlled timing test. | Run a daytime variant of any angle with strict 24h measurement. |
| E4 | **Practical-information structure reduces surface appeal.** Lists/facts may not stop the scroll as well as empathy hooks. | OPS-008 0 engagement. | No comparable empathy baseline; near-24h only. | Re-run H007 empathy with strict 24h (not now; later). |
| E5 | **Small personal-account follower base limits organic distribution.** | All runs have modest impressions except OPS-002. | OPS-002 reached 149, so some distribution is possible. | Not directly testable without growth/channel mix. |
| E6 | **Delayed observations show a low but consistent engagement floor.** 1 like + 1 reply appears in OPS-005〜007. | 3 delayed runs show identical engagement. | Delayed windows accumulate more exposure than 24h; not comparable. | Need strict 24h runs to see if the floor persists. |
| E7 | **Hashtag #ジャケット has lower reach than #40代ファッション expects.** | Jacket posts are lower than bag post. | Only one H001 data point; measurement issues. | Test another angle with same hashtags or test hashtag variants. |
| E8 | **CTA is too open-ended.** Asking "what do you check first?" requires specific experience. | OPS-008 0 replies. | H007 empathy version got 1 delayed reply. | Test a simpler binary/poll CTA. |
| E9 | **Post length / visual density.** Practical-info post was longer than empathy version. | Long posts may reduce completion. | No A/B data. | Test shorter formats. |
| E10 | **Seasonal / external noise.** Mid-September fashion content may compete with other events. | Hard to verify. | No external data. | Low priority; not testable in short term. |

## 6. External Research Requirements

| Candidate Area | Research Needed | Source / Method | Estimated Effort |
|----------------|-----------------|-----------------|------------------|
| H006 wireless earphones | Verify that "fit / battery / noise canceling" can be framed as personal preference without product claims. | Self-check against approval rules; no external facts needed. | low |
| H003 grooming | Confirm terms are everyday, not medical/dermatological; avoid efficacy claims. | Self-check; optionally review one general grooming article. | low |
| H002 shoe care + image | Source or create a non-copyrighted before/after image; verify image policy on X. | Asset creation / license check. | medium |
| H008 NG fashion | Check that negative examples do not target specific brands or people; keep it general. | Self-check against controversy-risk rules. | low |
| H009 first impression (re-run) | No new research; already business-context safe. | — | low |

## 7. OPS-009 Experiment Candidates

All candidates below keep canonical controls constant **unless** the changed dimension is explicitly noted:

- account_type = `personal`
- image = `none`
- URL = `none`
- hashtags = `#40代ファッション` + content-angle tag (2 tags)
- CTA = `reply / discussion / experience_sharing`
- platform = `X`

| ID | hypothesis_id | content_angle | changed_dimension | predicted_signal | info_gain | risk | research_needed | notes |
|----|---------------|---------------|-------------------|------------------|-----------|------|-----------------|-------|
| C1 | H003 | 爪・髪・香り | content_angle (clean strict-24h test) | bookmarks / replies | 4 | medium | low | Delayed observation showed 1 like + 1 reply. Clean run needed. |
| C2 | H006 | ワイヤレスイヤホン | content_angle (new gadget angle) | replies / bookmarks | 5 | medium | low | Fills gadget coverage gap; no prior data. |
| C3 | H009 | 営業/経営者の第一印象 | content_angle (clean strict-24h test) | profile_clicks / replies | 3 | medium | low | Already tested once but non-comparable. Repeating immediately is lower priority than new angles. |
| C4 | H002 | 靴の手入れ | image (before/after photo) | bookmarks / likes | 4 | medium | medium | Tests media dimension; H002 text-only was weak. Breaks canonical image=none control. |
| C5 | H007 | 若作りしないジャケット | posting_time (daytime) + strict 24h | impressions | 3 | low | low | Same angle as last two runs; only use if timing hypothesis is urgent. |
| C6 | H008 | 40代NGファッション | content_angle + negative framing | impressions / replies | 3 | medium | low | Risk of sounding preachy; needs careful tone. |

### Expected Information Gain Scoring

- **5** = Tests an entirely untested content angle or dimension; highest learning value.
- **4** = Cleans up an existing angle or tests a major new dimension (image/timing).
- **3** = Repeats a recently tested angle or explores higher-risk framing.

## 8. Recommended OPS-009 Experiment

**Selected candidate: C2 — H006 ワイヤレスイヤホン**

### Why C2?

1. **Highest expected information gain (5/5).** H006 has never been tested, so any clean result is new learning.
2. **Angle diversification.** After OPS-007 and OPS-008 both used H007, the queue rule "avoid the same cut for the last two posts" strongly favors leaving H007.
3. **Gadget coverage gap.** The product_slug is `mens-fashion-gadget`; only H001 (bag contents) and H006 are gadget-oriented. Re-opening the gadget angle is strategically important.
4. **Moderate risk, low research.** Wireless earphones are a common personal-preference topic. No product-specific claims are required.
5. **Clean measurement opportunity.** Because it is a fresh angle, there is no temptation to compare it to OPS-002/007/008 directly; the success criterion can be simply "obtain strict 24h metrics".

### Proposed Run Configuration

| Field | Value |
|-------|-------|
| ops_id | `OPS-009` |
| hypothesis_id | `H006` |
| content_angle | ワイヤレスイヤホン |
| experiment_dimension | `content_angle` |
| information_structure | `empathy / awareness` (personal observation + question) |
| account_type | `personal` |
| image | `none` |
| URL | `none` |
| hashtags | `#40代ファッション #ワイヤレスイヤホン` |
| CTA | `reply / discussion / experience_sharing` |
| posting_time | weekday daytime (e.g., 08:00–10:00 JST) to reduce timing confounder |

### Sample Direction (not final copy)

> 40代になって、移動中のイヤホン選びって変わった。
> 音質だけじゃなくて、付け心地や通話のしやすさも気になる。
> 電車の中で長時間使うなら、ノイズの入り方も大事。
> みんなは通勤・移動のイヤホン、何を重視して選んでる？
> #40代ファッション #ワイヤレスイヤホン

This is a **direction only**. Final copy must go through the standard candidate generation, fact-check, market-judge, risk-review, and human-approval pipeline.

### Account Distribution Evaluation

| Factor | Assessment |
|--------|------------|
| Audience fit | `#40代ファッション` followers are 40s men; wireless earphones are relevant to commuting/mobility. |
| Personal-account fit | Sharing personal selection criteria fits a personal account; no corporate product pitch. |
| Differentiation | Less saturated than fashion-fit advice; gadget tag may reach a broader subset. |
| Expected reach | Moderate; no guarantee. The primary goal is clean measurement, not a viral hit. |
| Risk | Medium: gadget-only posts can feel off-brand if not tied to lifestyle context. Mitigation: frame around commuting/work mobility. |

## 9. What We Would NOT Do

- Do **not** run another H007 post for OPS-009. The last two posts were H007; angle diversification takes priority.
- Do **not** compare OPS-009 results to OPS-002, OPS-007, or OPS-008 unless measurement windows match exactly.
- Do **not** promote any hypothesis to `winning-patterns.md` or canonical knowledge.
- Do **not** change multiple dimensions at once (e.g., content angle + image + CTA).

## 10. Measurement Process Improvements

Because 4 of the last 5 runs are non-comparable, measurement discipline is now the top operational risk.

| # | Improvement | Owner | Implementation Hint |
|---|-------------|-------|---------------------|
| M1 | **Hard gate:** No `result_label` other than `non_comparable` unless `measurement_status` is `strict_24h_recorded`. | Agent / Human | Enforce in post-analysis template. |
| M2 | **Auto-reminder:** Generate a `reminder.md` inside the run folder immediately after posting with `metrics_due_at` and a 15-min-before alarm. | Agent | Create file during posting record step. |
| M3 | **Pre-post checklist:** Approval.md must include "who will record metrics and how" before posting. | Human | Add to Pre-Post Checklist. |
| M4 | **Missed-metric protocol:** If 24h is missed, record `non_comparable` immediately and do not attempt ratio comparisons. | Agent | Enforce in post-analysis. |
| M5 | **Measurement window metadata:** Always record `measurement_window`, `measurement_status`, and elapsed time in `run.json` and `metrics.md`. | Agent | Already added for OPS-007/008; make standard. |

## 11. Knowledge Promotion Architecture

A hypothesis or pattern should only be promoted out of `pilot / draft` status when **all** of the following are true:

1. At least **2 comparable runs** (same measurement window, same controls) support the same direction.
2. All runs have `measurement_status=strict_24h_recorded`.
3. Human reviewer has approved the promotion.
4. The pattern is written into `knowledge/mens-fashion-gadget/winning-patterns.md` or the relevant canonical file, with explicit controls and limitations.
5. The promotion is committed separately from run data and clearly labeled.

**Current status:** No hypothesis meets these criteria.

## 12. Pilot Validation Checklist

- [x] Past OPS analysis: OPS-002〜008 summarized.
- [x] Failure explanation generation: measurement miss spiral documented.
- [x] Hypothesis generation: 6 OPS-009 candidates listed.
- [x] Experiment dimension selection: 1 changed dimension per candidate.
- [x] Expected information gain evaluation: scored 1–5 with rationale.
- [x] Research requirement判定: low/medium assigned per candidate.
- [x] Experiment recommendation: C2 H006 selected with rationale.
- [x] Human-in-the-loop preserved: final copy not generated; approval required.
- [x] Canonical knowledge not promoted: no winning-pattern updates.

## 13. Revision Note

**2026-09-23 Human Review Follow-up**: The initial recommendation (C2 H006) was re-evaluated. The Human Reviewer identified that the project is in **Experiment Debt** — 0 comparable experiments out of 7 attempts — and that adding a new content angle would increase debt risk rather than reduce it. The revised recommendation is **Candidate B: H003 爪・髪・香り replication with strict 24h measurement**. See full follow-up in `docs/pilots/ops009-autonomous-hypothesis-cycle-follow-up.md` and the proposed measurement contract in `docs/measurement-contract-proposal.md`.

## 14. Next Steps

1. Human reviewer confirms or rejects the **revised** OPS-009 recommendation (H003 replication) and the measurement contract proposal.
2. If approved, create OPS-009 run folder with standard pipeline.
3. Generate candidates, perform fact-check / research, run market judge, risk review, and human approval.
4. After posting, enforce the strict 24h measurement contract.
5. Use OPS-009 result as the first comparable data point in the next Autonomous Hypothesis Cycle.

---

- artifact_type: `autonomous_hypothesis_cycle_pilot`
- product_slug: `mens-fashion-gadget`
- pilot_date: `2026-09-23`
- revised_follow_up_date: `2026-09-23`
- initial_recommended_ops: `OPS-009`
- initial_recommended_hypothesis: `H006`
- revised_recommended_hypothesis: `H003`
- human_review_required: `true`
