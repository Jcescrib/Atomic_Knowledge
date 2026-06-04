# Index — AKU/TAKU Vault

Router and validation dashboard. Updated by `/ingest`, `/pipeline`, `/lint`, and validation actions.

## Counts

| Layer | Active | Draft | Deprecated | Validated-false / failing |
|---|---|---|---|---|
| AKU | 181 | — | 0 | 0 |
| TAKU | 0 | 28 | 0 | 0 |

By AKU class: **145 concept**, **4 method**, **32 claim** · all `unvalidated` · 174 `epistemic_type: sourced` at `llm_confidence: 0.50`, 5 `sourced` at `0.60` (post-dedup: segmentos, propuesta-valor, product-market-fit, nicho-strategy, lead-magnet), 1 `sourced` at `0.20` (mas-valor-menos-coste, −0.30 por contradicción con atrapado-medio/Porter), 1 `tacit` at `null` (Joan's free-bootstrap-plataforma claim).

Graph: **1 connected component**, 0 bidirectional errors (AKU 181/181 simétrico, 0 body-drift; TAKU 28/28 simétrico — verificado por script).

_Last updated: 2026-06-04 (cleanup: eliminados los 15 AKUs Kolenda de tesis-nuclear; 16 PDFs de 5.6-nickkolenda marcados pending-reingestion para desglose capítulo a capítulo tras completar Power MBA. raw/ conservados. Antes: pipeline módulos 04 + 05 completos — +106 AKUs/+17 TAKUs; tras cleanup quedan 181 AKUs / 28 TAKUs)._

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

**2026-06-03 (post-módulo 02)**: 0 errors · 5 warnings · 3 informational. Graph healthy after autonomous repair of 15 bidirectional asymmetries detected during the lint pass (all `related` and 1 `supports` cross-module edge inverses).
- 72 AKUs / 8 TAKUs / 212 directed edges all symmetric.
- W1-5 — 5 TAKUs > 7 `justified_by` (BMC=14, growth-metrics=12, plataformas=12, Power Value=11, océano-azul=9). Expected for comprehensive frameworks.
- I1 — No axiom candidates yet (top AKU has 3 incoming `supports`, threshold 10).
- I2 — 2 AKUs at `llm_confidence: 0.60` after dedup (segmentos-de-clientes, propuesta-de-valor).

Full report: `outputs/lint/2026-06-03-modulo-02.md` (gitignored).

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
