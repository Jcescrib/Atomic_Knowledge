# Index — AKU/TAKU Vault

Router and validation dashboard. Updated by `/ingest`, `/lint`, and validation actions.

## Counts

| Layer | Active | Draft | Deprecated | Validated-false / failing |
|---|---|---|---|---|
| AKU | 11 | — | 0 | 0 |
| TAKU | 0 | 1 | 0 | 0 |

By AKU class: **7 concept**, **2 method**, **2 claim** · all `unvalidated` · all `epistemic_type: sourced` · all `llm_confidence: 0.50`.

_Last updated: 2026-06-02 (ingest: 2.2-motores-de-crecimiento)_

## Pending validation queue

Items awaiting human review. Surface order: oldest first.

### AKUs to validate (in practice)

All 11 AKUs from the first ingest are `unvalidated` — populate `human_certainty` after real-world testing:

- `aku-cltv-concept` (concept)
- `aku-cac-concept` (concept)
- `aku-arpu-concept` (concept)
- `aku-churn-rate-concept` (concept)
- `aku-cac-payback-concept` (concept)
- `aku-cltv-cac-ratio-concept` (concept)
- `aku-cltv-minus-cac-concept` (concept)
- `aku-cltv-subscription-formula` (method)
- `aku-cltv-transactional-formula` (method)
- `aku-cltv-gross-margin-over-revenue` (claim)
- `aku-cltv-cac-dual-optimization` (claim)

### TAKUs awaiting activation

- `taku-digital-growth-engine-metrics-map` (framework, draft, `content_validation: llm-authored`)

### AKU links awaiting validation

11 `llm-proposed` links on `taku-digital-growth-engine-metrics-map` (all `justified_by`). Promote each to `human-validated` after reviewing the link_note. Note: link count exceeds the lint threshold of 7 — this is expected for a comprehensive metrics-map framework, but `/lint` will flag it for review.

### Dedup candidates
_(none — first ingest, empty starting graph)_

## Lint flags (latest run)

_No lint runs yet. Run `/lint` to populate. Reports archived in `outputs/lint/`._

## Domain map

Tags currently in use (open taxonomy):

- `growth` (11)
- `unit-economics` (11)
- `metrics` (10)
- `business-model` (5)
- `subscription` (1) · `transactional` (1) · `retention` (1) · `monetization` (1) · `cash-flow` (1) · `roi` (1) · `profitability` (1) · `measurement` (1) · `strategy` (1)

## How to navigate

- Direct AKU lookup → `aku/aku-<slug>.md`
- Direct TAKU lookup → `taku/<type>/taku-<slug>.md`
- Situational query → `/query <description>`
- Daily capture → `/capture <text>`
- Process new source → drop file in `raw/`, then `/ingest raw/<file>`
- Health check → `/lint`

## File map (live)

- `CLAUDE.md` — operating manual
- `log.md` — append-only history
- `_meta/templates/` — schemas
- `_spec/` — authoritative specifications (reference only)
- `.claude/commands/` — slash command definitions
