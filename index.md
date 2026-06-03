# Index — AKU/TAKU Vault

Router and validation dashboard. Updated by `/ingest`, `/pipeline`, `/lint`, and validation actions.

## Counts

| Layer | Active | Draft | Deprecated | Validated-false / failing |
|---|---|---|---|---|
| AKU | 43 | — | 0 | 0 |
| TAKU | 0 | 4 | 0 | 0 |

By AKU class: **36 concept**, **2 method**, **5 claim** · all `unvalidated` · all `epistemic_type: sourced` · all `llm_confidence: 0.50`.

_Last updated: 2026-06-03 (pipeline ingest #4: 2.3-conceptos plataformas)_

## Pending validation queue

Items awaiting human review. Surface order: oldest first.

### AKUs to validate (in practice)

All 14 AKUs from the 2.1-BMC ingest are `unvalidated` — populate `human_certainty` after real-world testing:

**Concept-AKUs (12)**
- `aku-bmc-concept`
- `aku-segmentos-de-clientes-concept`
- `aku-propuesta-de-valor-concept`
- `aku-canales-de-distribucion-concept`
- `aku-canal-directo-concept`
- `aku-canal-indirecto-concept`
- `aku-relaciones-con-clientes-concept`
- `aku-flujos-de-ingresos-concept`
- `aku-recursos-clave-concept`
- `aku-actividades-clave-concept`
- `aku-ecosistema-alianzas-concept`
- `aku-estructura-de-costes-concept`

**Claim-AKUs (2)**
- `aku-segmento-relevante-claim`
- `aku-coste-prioridad-segun-estrategia-claim`

### TAKUs awaiting activation

- `taku-business-model-canvas` (framework, draft, `content_validation: llm-authored`)

### AKU links awaiting validation

14 `llm-proposed` links on `taku-business-model-canvas` (all `justified_by`). Promote each to `human-validated` after reviewing its `link_note`. Note: link count exceeds the lint threshold of 7 — expected for a comprehensive framework that covers an entire 9-block canvas.

### Dedup candidates
_(none — fresh post-reset graph; the 2.1-BMC ingest was vacuous against the empty starting state)_

## Lint flags (latest run)

_No lint runs since reset. Run `/lint` to populate. Reports archived in `outputs/lint/` (gitignored)._

## Domain map

Tags currently in use (open taxonomy):

- `business-model` (14) · `bmc` (14)
- `strategy` (3) · `customer` (4) · `framework` (2)
- `distribution` (3) · `channel` (2)
- `segmentation` (2) · `methodology` (1)
- `value-proposition` (1)
- `relationship` (1) · `revenue` (1) · `monetization` (1)
- `resources` (1) · `operations` (2) · `activities` (1)
- `partnerships` (1) · `ecosystem` (1)
- `cost` (1) · `finance` (1) · `cost-management` (1)

## How to navigate

- Process a folder of PDFs from outside the vault → `/pipeline "<absolute-folder-path>"` (PDFs stay at source; markdown lands in `raw/<slug>/`)
- Process one source already in `raw/` → `/ingest raw/<slug>/<slug>.md`
- Direct AKU lookup → `aku/aku-<slug>.md`
- Direct TAKU lookup → `taku/<type>/taku-<slug>.md`
- Situational query → `/query <description>`
- Daily capture → `/capture <text>`
- Health check → `/lint`

## File map (live)

- `CLAUDE.md` — operating manual
- `log.md` — append-only history
- `_meta/templates/` — schemas
- `_meta/pipeline-manifest.yml` — per-source state + origin paths
- `_spec/` — authoritative specifications (reference only)
- `.claude/commands/` — slash command definitions
- `scripts/pipeline.sh` — deterministic pipeline phases
