# Autonomous Hypothesis Cycle Pilot — Human Review Follow-up (Revision 01)

## 1. Experiment Debt Assessment

### Current State (mens-fashion-gadget, OPS-002〜008)

| Metric | Count |
|--------|-------|
| total experiments attempted | `7` (OPS-002〜008) |
| posted | `6` (OPS-002, OPS-004, OPS-005, OPS-006, OPS-007, OPS-008) |
| not posted | `1` (OPS-003, held due to H001 overlap) |
| comparable experiments (strict 24h) | `0` |
| non-comparable experiments | `6` |
| hypotheses attempted | `5` (H001, H002, H003, H009, H007) |
| hypotheses validated | `0` |
| hypotheses rejected | `0` |
| hypotheses inconclusive | `5` |

### Diagnosis

The bottleneck is **not** a lack of explored content angles. The bottleneck is a lack of **comparable evidence**.

- 4 consecutive runs (OPS-005〜008) are non-comparable.
- Even OPS-002 and OPS-004 use `late_measurement` / `late_24h_measurement`, so they are not strict-24h comparable either.
- As a result, **no hypothesis can be validated, rejected, or promoted** to canonical knowledge.

**Conclusion**: SNS Factory is currently in **Experiment Debt** — experiment count has increased, but evidence quality has not.

---

## 2. Exploration vs Measurement Recovery / Replication

### Strategy A: Exploration

- **Action**: Run a new content_angle such as H006 ワイヤレスイヤホン.
- **Coverage value**: high — fills a gap in the content-angle map.
- **Evidence value**: low unless strict 24h measurement is obtained. If measurement is missed again, it adds another non-comparable run and increases debt.
- **Debt impact**: increases debt risk.

### Strategy B: Measurement Recovery / Replication

- **Action**: Re-run a previously attempted hypothesis under a strict measurement contract.
- **Coverage value**: low — no new angle.
- **Evidence value**: high — produces the first comparable data point for an existing hypothesis.
- **Debt impact**: reduces debt by converting an inconclusive hypothesis into an evaluable one.

### Strategic Judgment

Given 0 comparable experiments out of 7 attempts, **Strategy B must take priority for OPS-009**. The immediate goal is to acquire comparable evidence, not to expand coverage.

Once at least 1–2 comparable runs exist, Strategy A can resume under a stricter measurement contract.

---

## 3. OPS-009 Candidates Re-evaluated

All candidates keep canonical controls constant **except** the explicitly noted changed dimension. Image, URL, hashtag count, CTA style, and account_type remain unchanged.

| ID | hypothesis_id | content_angle | strategy | changed_dimension | Expected Information Gain | Comparable Evidence Value | Experiment Debt Reduction | Performance Potential | Confounding Risk | Cost | Future Decision Value |
|----|---------------|---------------|----------|-------------------|--------------------------:|--------------------------:|--------------------------:|----------------------:|-----------------:|-----:|----------------------:|
| A | H006 | ワイヤレスイヤホン | Exploration | content_angle (new) | 3 | 1 | −2 | unknown | medium (posting_time uncontrolled) | normal | medium |
| B | H003 | 爪・髪・香り | Replication | content_angle (re-test) | 4 | 5 | +4 | medium (delayed observation showed engagement) | low–medium | normal | high |
| C | H001 | バッグの中身 | Baseline / Replication | content_angle (re-test) | 3 | 4 | +3 | medium–high (historical 149 late impressions) | medium (stale angle; OPS-003 overlap) | normal | medium |
| D | H007 | 若作りしないジャケット (empathy/awareness) | Replication / Structure comparison | information_structure baseline | 4 | 4 | +3 | medium (delayed observation showed engagement) | high (H007 would be 3rd consecutive run) | normal | high for structure only |

### Candidate Notes

- **Candidate A (H006)**: High coverage value, but running a new angle now risks adding another non-comparable run. Deferred until measurement reliability is proven.
- **Candidate B (H003)**: Best balance. It re-tests a high-priority hypothesis, diversifies away from H007, and has a prior delayed-engagement signal. Strict 24h measurement would finally make H003 evaluable.
- **Candidate C (H001)**: Useful as a baseline, but the angle is older and overlaps with the pending OPS-003. Less urgent than clearing H003.
- **Candidate D (H007 empathy)**: Would enable a future information_structure comparison with OPS-008, but it requires a third consecutive H007 post. This violates angle diversification and should be deferred.

---

## 4. Expected Information Gain — Re-evaluated

Information gain is redefined as:

> The value of an experiment is proportional to the **evaluable evidence** it produces, not just the novelty of the angle.

| Candidate | Raw Novelty | Evidence Quality | Net Information Gain |
|-----------|------------:|-----------------:|---------------------:|
| A H006 | 5 | 1 | 3 |
| B H003 | 3 | 5 | 4 |
| C H001 | 2 | 4 | 3 |
| D H007 empathy | 2 | 4 | 4 (but high repetition cost) |

**Candidate B has the highest net information gain** when evidence quality and debt reduction are weighted.

---

## 5. Posting Time Conflict — Confirmation

### Issue

The initial pilot recommendation included:

> "posting_time: weekday daytime (e.g., 08:00–10:00 JST)"

while claiming that only `content_angle` would change. This is a contradiction.

### Resolution

- There is **no canonical posting_time** defined in the repository.
- For OPS-009, posting_time will **not** be intentionally optimized.
- If Candidate B (H003 replication) is selected, the posting_time will be recorded and, where feasible, matched to the prior H003 run (OPS-005, 22:41 JST) to reduce confounding.
- Posting_time will be treated as an **observed variable**, not an experiment dimension, unless a separate timing experiment is explicitly approved.

**No dual-variable change** (content_angle + posting_time) will be made in OPS-009.

---

## 6. Measurement Contract Proposal

A separate proposal file is created: `docs/measurement-contract-proposal.md`.

### Summary

| Element | Proposal |
|---------|----------|
| posted_at | recorded at actual posting time, ISO-8601 +09:00 |
| metrics_due_at | `posted_at + 24 hours` |
| pre_measurement_reminder | `metrics_due_at - 60 minutes` |
| measurement_reminder | at `metrics_due_at` |
| measurement_tolerance | `±15 minutes` from `metrics_due_at` |
| strict_24h_recorded | observation taken within `±15 minutes` |
| near_24h_observation | observation taken within `±60 minutes` but outside `±15 minutes` |
| delayed_observation | observation taken after `metrics_due_at + 60 minutes` |
| result_label rule | Only `strict_24h_recorded` may be used for ratio comparisons or hypothesis validation. Other windows default to `non_comparable`. |

This is a **proposal**, not a canonical rule. Human approval is required before it becomes standard.

---

## 7. Revised OPS-009 Recommendation

**Selected candidate: B — H003 爪・髪・香り (replication with strict 24h measurement)**

### Configuration

| Field | Value |
|-------|-------|
| ops_id | `OPS-009` |
| hypothesis_id | `H003` |
| content_angle | 爪・髪・香り |
| experiment_dimension | `content_angle` |
| information_structure | `empathy / awareness` (personal observation + question) |
| account_type | `personal` |
| image | `none` |
| URL | `none` |
| hashtags | `#40代ファッション #爪髪香り` |
| CTA | `reply / discussion / experience_sharing` |
| posting_time | recorded; matched to OPS-005 (22:41 JST) if feasible, otherwise documented as observed variable |
| measurement contract | `docs/measurement-contract-proposal.md` |

### Rationale

1. **Reduces Experiment Debt**: Re-tests an existing hypothesis instead of adding a new one.
2. **Produces Comparable Evidence**: If strict 24h measurement succeeds, H003 becomes the first evaluable hypothesis in this product.
3. **Angle Diversification**: Moves away from H007 after two consecutive runs.
4. **Prior Signal**: Delayed observation of OPS-005 showed engagement (1 like, 1 reply), suggesting the topic resonates.
5. **Single-Variable Experiment**: Only `content_angle` changes from the canonical control set; posting_time is not optimized.

### Account Distribution Evaluation

| Factor | Assessment |
|--------|------------|
| Audience fit | `#40代ファッション` followers are 40s men; grooming/cleanliness is broadly relevant. |
| Personal-account fit | Sharing personal grooming habits fits a personal account; no corporate pitch. |
| Differentiation | Distinct from recent H007 jacket posts. |
| Expected reach | Moderate; no guarantee. The primary success criterion is strict 24h measurement, not a specific impression count. |
| Risk | Medium: grooming advice can sound patronizing. Mitigation: frame as personal observation, not prescription. |

---

## 8. Autonomous Hypothesis Engine — Design Learning

### Key Learning from Human Review

The engine must balance more than coverage and novelty. It needs an **Experiment Selection Policy** that includes:

1. **Experiment Coverage** — which dimensions/angles have been tried.
2. **Evidence Quality** — how many runs are comparable.
3. **Experiment Debt** — experiments attempted minus evaluable evidence.
4. **Expected Information Gain** — evidence-weighted learning value.
5. **Measurement Reliability** — likelihood that the next run will produce comparable data.

### Policy Modes

| Mode | Trigger | Action |
|------|---------|--------|
| **Explore** | Low coverage AND high measurement reliability | Try a new content_angle/dimension. |
| **Replicate** | High debt, recent non-comparable runs | Re-test an existing hypothesis with strict measurement. |
| **Recover Measurement** | Measurement miss detected | Fix process/contract before next experiment. |
| **Exploit** | 2+ comparable runs show consistent signal | Scale or promote the pattern, still human-approved. |

### Current Mode

**Recover Measurement → Replicate**

OPS-009 should not explore a new angle. It should replicate H003 under a strict measurement contract to convert debt into evidence.

### Status

This design learning is recorded as a **draft pilot learning**. It is **not** promoted to a canonical algorithm.

---

## 9. Files Changed

- `docs/pilots/ops009-autonomous-hypothesis-cycle-follow-up.md` (this file, new)
- `docs/measurement-contract-proposal.md` (new)
- `docs/pilots/ops009-autonomous-hypothesis-cycle-pilot.md` (revision note added)
- `docs/roadmap.md` (design learning reflected)
- `knowledge/mens-fashion-gadget/experiment-queue.md` (OPS-009 recommendation updated to H003)
- `knowledge/mens-fashion-gadget/hypothesis-pool.md` (H003 status updated to planned/testing)

No OPS-009 run folder was created. No copy was generated. No post was made.

---

## 10. Atomic Commits

1. `docs: add measurement contract proposal and pilot follow-up`
2. `experiment: revise OPS-009 recommendation to H003 replication per human review`
3. `docs: update roadmap with autonomous engine design learning`

## 11. Push Result

Pushed to `main` on the remote repository.

## 12. Git Status

Working tree clean after push.

---

- artifact_type: `autonomous_hypothesis_cycle_follow_up`
- revision: `01`
- product_slug: `mens-fashion-gadget`
- revised_recommended_ops: `OPS-009`
- revised_recommended_hypothesis: `H003`
- human_review_required: `true`
