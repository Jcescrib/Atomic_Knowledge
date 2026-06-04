# Index — AKU/TAKU Vault

Router and validation dashboard. Updated by `/ingest`, `/pipeline`, `/lint`, and validation actions.

## Counts

| Layer | Active | Draft | Deprecated | Validated-false / failing |
|---|---|---|---|---|
| AKU | 531 | — | 1 | 1 |
| TAKU | 0 | 83 | 0 | 0 |

By AKU class: **392 concept**, **30 method**, **110 claim** · all `unvalidated` · `sourced` mayoría at `llm_confidence: 0.50`, ~14 `sourced` at `0.60` (post-dedup), 1 at `0.70` (lead-magnet, 3 fuentes), 1 `sourced` at `0.20` (mas-valor-menos-coste, −0.30 por contradicción con atrapado-medio/Porter), 1 `tacit` at `null` (Joan's free-bootstrap-plataforma claim).

Graph: **1 connected component** (615 nodos: 532 AKU + 83 TAKU), 0 bidirectional errors (532/532 simétrico, 0 body-drift, 0 wikilinks rotos, 0 huérfanos — verificado por `scripts/verify_graph.py`). **130 AKUs llevan el source-tag `hormozi`** (121 nuevos + 9 dedup-merges cross-corpus). Tras la ingesta Hormozi se reconectaron 1 huérfano (convergent-vs-divergent) y 1 isla (create-flow/sales-fulfillment) con puentes nivel (a)/(b).

_Last updated: 2026-06-04 (TRILOGÍA HORMOZI COMPLETA — 3 libros book-mode: +121 AKUs / +25 TAKUs. **100M Offers** (51 AKU, 9 TAKU: grand-slam-offer, value-equation, escasez/urgencia/bonos/garantías, MAGIC naming), **100M Leads** (53 AKU, 11 TAKU: Core Four —warm/cold outreach, content, paid ads—, lead getters —referidos/empleados/agencias/afiliados—, LTGP:CAC, client-financed-acquisition, more-better-new, open-to-goal), **100M Money Models** (17 AKU, 5 TAKU: money model 3 etapas, attraction/upsell/downsell/continuity offers). Dedups cross-corpus Power-MBA↔Hormozi: commodity, ecuacion-valor, cialdini-escasez, lead-concept, lead-magnet, cta, cltv-cac-ratio, cltv-gross-margin, marketing-afiliados, cac/cac-payback. Previo: pipeline módulo 07 «Leadership» → 233 AKUs / 32 TAKUs)._

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

**2026-06-04 (post-módulos 04+05 + cleanup Kolenda)**: **0 errors · 6 warnings · informational**. 181 AKUs / 28 TAKUs · 1 connected component · 0 isolated · 0 bidirectional asymmetries (AKU 181/181, TAKU 28/28) · 0 body-drift · 0 broken wikilinks · 0 `sources[]` violations.
- W1-6 — 6 TAKUs > 7 `justified_by` (BMC=14, lean-startup=12, plataformas=12, growth-metrics=11, Power Value=11, océano-azul=9). Expected for comprehensive frameworks; ningún TAKU de los módulos 04/05 supera el umbral (máx. cinco-fuerzas=6).
- Decay/freshness: **ninguna** (todo `created` 2026-06-03, ≤1 día). I2 (related-only, 80 AKUs) disparará >14d (~2026-06-17); contradicción Porter↔océano-azul disparará >30d (~2026-07-03).
- I3 — Sin axiom candidates (hub máximo: cinco-fuerzas-porter con 5 incoming `supports`, umbral 10).
- I4 — Clusters de vocabulario `domain` ES/EN propuestos para normalización (estrategia/strategy, crecimiento/growth, metricas/metrics…) — propuesta, sin auto-merge.
- 16 PDFs `5.6-nickkolenda` en `pending-reingestion`.

Full report: `outputs/lint/2026-06-04.md` (gitignored).

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
