# Index — AKU/TAKU Vault

Router and validation dashboard. Updated by `/ingest`, `/pipeline`, `/lint`, and validation actions.

## Counts

| Layer | Active | Draft | Deprecated | Validated-false / failing |
|---|---|---|---|---|
| AKU | 1043 | — | 1 | 1 |
| TAKU | 0 | 86 | 0 | 0 |

By AKU class: **639 concept**, **84 method**, **321 claim** · all `unvalidated` · `sourced` mayoría at `llm_confidence: 0.50`, ~21 `sourced` at `0.60` (post-dedup/merge), 3 at `0.70` (lead-magnet, cltv-cac-ratio, churn-rate — 3 fuentes c/u), 1 `sourced` at `0.20` (mas-valor-menos-coste), 1 `tacit` at `null` (Joan's free-bootstrap-plataforma claim).

Graph: **1 connected component** (1130 nodos: 1044 AKU + 86 TAKU), 0 bidirectional errors (1044/1044 simétrico, 0 body-drift, 0 wikilinks rotos, 0 huérfanos — verificado por `scripts/verify_graph.py`). +22 conexiones conceptuales nivel (b) aplicadas entre AKUs (related bidireccional). **389 AKUs llevan el source-tag `hormozi`** (130 de la 1ª ingesta + 259 de la reingesta diferencial hiper-exhaustiva).

_Last updated: 2026-06-04 (CIERRE DE GAPS PASO 3 — REFACTOR RETROACTIVO granularidad máxima: +234 AKUs (810→1044). Desplegados sub-items plegados en paraguas como AKUs propios `supported_by` el paraguas, en 8 módulos: 15 GA (+23: métricas/UTM/objetivos/plan), 14 influencers (+15: 10 cláusulas contrato + 4 KPI funnel + cesión), 06 vender (+39: 14 secciones pitch deck + 5 templates elevator + 7 dimensiones fit + 4 perfiles modelo + 5 claims financiación), 04 estrategia (+50: barreras + 4 ejes PEST + best-cost + niveles brand awareness + 8 posicionamiento + 9 principios blitzscaling + 4 factores crecimiento), 05 marketing digital (+59: 6 formatos display + 16 formatos contenido + 7 tips + 8 lead magnets + 4 cats CRO + flywheel + adblockers + branding raíz), 02 modelo negocio (+20: customer-persona dimensiones + 3 niveles no-clientes + 4 acciones ERIC + claims valor/segmentación), 03 lean (+9: fases optimizar-canales/escalar + 4 métodos validación entrevista), 07 liderazgo (+19: 4 estructuras org + 3 Deep Work + 4 zonas Ikigai + OKR objetivos-vs-KR). Dedup-merges: 5-2 (9 métricas), churn-rate, ab-testing, landing-page (re-source). verify_graph: 1044/1044 simétrico, 0 errores. Candidatos TAKU flagged (no creados): Customer Persona Canvas, ERIC/Four Actions, plantilla experimentos (framework); 9 reglas blitzscaling + 7 tips contenido (heuristic); apps meditación (reference). Previo: CIERRE DE GAPS PASO 2 — quick wins: +19 AKUs (791→810). 09-03 múltiplos de valoración (+4 method: EV/EBITDA, EV/Ventas, P/VC, P/FCF), 08-01 tríada fortalezas-debilidades-motivaciones (+1 concept), 18 hacks de copy desplegados (+7 claim), 20-2 fórmulas de títulos desplegadas (+7 method). Merge fuente 5-2 en 9 AKUs de métricas growth-engine (+0.10 confianza c/u). verify_graph: 810/810 simétrico, 0 errores. Previo: REINGESTA DIFERENCIAL HIPER-EXHAUSTIVA Hormozi: +259 AKUs (offers +51, leads +88, money +120), máxima granularidad — explota paraguas en sub-tipos individuales (4 upsells, 3 downsells, 3 continuity, 5 componentes MAGIC, tipos de garantía/escasez/urgencia), atomiza claims normativos y money-math methods, y 7 SPLIT cross-corpus (gross-profit, LTGP, price-to-value, lead-contactable, lead-magnet-hormozi, cta-hormozi, affiliate-hormozi). Total Hormozi: 389 AKUs. Previo: TRILOGÍA HORMOZI 1ª ingesta — 3 libros book-mode: +121 AKUs / +25 TAKUs. **100M Offers** (51 AKU, 9 TAKU: grand-slam-offer, value-equation, escasez/urgencia/bonos/garantías, MAGIC naming), **100M Leads** (53 AKU, 11 TAKU: Core Four —warm/cold outreach, content, paid ads—, lead getters —referidos/empleados/agencias/afiliados—, LTGP:CAC, client-financed-acquisition, more-better-new, open-to-goal), **100M Money Models** (17 AKU, 5 TAKU: money model 3 etapas, attraction/upsell/downsell/continuity offers). Dedups cross-corpus Power-MBA↔Hormozi: commodity, ecuacion-valor, cialdini-escasez, lead-concept, lead-magnet, cta, cltv-cac-ratio, cltv-gross-margin, marketing-afiliados, cac/cac-payback. Previo: pipeline módulo 07 «Leadership» → 233 AKUs / 32 TAKUs)._

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
