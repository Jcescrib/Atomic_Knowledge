# Index — AKU/TAKU Vault

Router and validation dashboard. Updated by `/ingest`, `/pipeline`, `/lint`, and validation actions.

## Counts

| Layer | Active | Draft | Deprecated | Validated-false / failing |
|---|---|---|---|---|
| AKU | 2244 | — | 1 | 1 |
| TAKU | 0 | 140 | 0 | 0 |

By AKU class: **929 concept**, **175 method**, **1141 claim** · all `unvalidated` · `sourced` mayoría at `llm_confidence: 0.50`, ~21 `sourced` at `0.60` (post-dedup/merge), 3 at `0.70` (lead-magnet, cltv-cac-ratio, churn-rate — 3 fuentes c/u), 1 `sourced` at `0.20` (mas-valor-menos-coste), 1 `tacit` at `null` (Joan's free-bootstrap-plataforma claim).

Graph: **componentes conectados** (1976 nodos: 1840 AKU + 136 TAKU) — **TAREA 2 COMPLETA (3/3 libros)**: nuevo cluster **Robert Greene / 48 Laws of Power** (libro 3 COMPLETO: **48 concept-AKUs** —1 por ley— + 1 framework TAKU; INTEGRATE 5.5 con 0 huérfanos: 48 leyes encadenadas + 16 puentes cross-corpus, muchos **tensiones** valiosas con Jocko/Naval —ingestado como descripción amoral de las tácticas que afirma Greene, no como recomendación—). Clusters **Naval** (235 AKUs) y **James Clear / Atomic Habits** (TAREA 2 libro 2 COMPLETO: **84 AKUs** —23 concept, 18 method, 43 claim— + 1 framework TAKU, INTEGRATE 5.5 con 0 huérfanos; **muy integrado cross-corpus** vía `related`: identidad/hábitos/entorno/deseo/specific-knowledge/sistemas-diseña-entorno/cinco-chimpancés/run-uphill/felicidad-ausencia-de-deseo↔**Naval** (13+ puentes en conclusion+little-lessons), empezar-aquí-y-ahora/disciplina/good-mindset/caer-del-path/accountability↔**Jocko**, categoría-de-uno↔**Hormozi**, camino-de-menor-resistencia↔**32-principles**, sistemas-vs-metas↔Naval/Power-MBA). El cluster Naval también con puentes a Power-MBA (apalancamiento/equity/interés-compuesto) y Hormozi; candidatos a más puentes en `/audit-graph`. El corpus Jocko (incl. Libro 5 «The 32 Principles» y Libro 6 «The Code», integrado al cluster Jocko vía 8 puentes nivel (a) anclados-en-texto: detach, miedo-al-fracaso, camino-de-menor-resistencia, stress-cortisol, no-bad-teams, delegar, liderar-desde-frente, humildad) forma de momento una isla separada del grafo de negocio; **6 TAKUs Jocko nuevos** (draft, llm-authored): laws-of-combat, prioritize-and-execute, planning-checklist, post-operational-debrief, dichotomy-of-leadership, diagnostico-micromanagement-hands-off. los puentes al grafo Power-MBA/Hormozi son nivel (b) conceptual y esperan aprobación de Joan. 0 bidirectional errors (1055/1055 simétrico, 0 body-drift, 0 wikilinks rotos, 0 huérfanos — verificado por `scripts/verify_graph.py`). +22 conexiones conceptuales nivel (b) aplicadas entre AKUs (related bidireccional). **389 AKUs llevan el source-tag `hormozi`** (130 de la 1ª ingesta + 259 de la reingesta diferencial hiper-exhaustiva).

_Last updated: 2026-06-05 (**TAREA 2 COMPLETA (3/3 libros)** — libro 3 **«THE 48 LAWS OF POWER» (Robert Greene, 1998) COMPLETO**: book-mode en 4 lotes, commit+push por lote, **+48 concept-AKUs** (1792→1840; 1 por ley, `aku-48laws-NN-<slug>-concept`) + **1 framework TAKU** (las-48-leyes-del-poder). Cada ley = táctica de poder descrita por Greene (framing descriptivo «La Ley N de Greene sostiene...», NO recomendación del vault; contenido amoral/manipulación), con principio + mecanismo + reversal foldeado como cláusula donde aplica. Solo 4 imágenes decorativas → 0 blockquotes. 2º pase verify_graph 0 errores; INTEGRATE 5.5 → 0 huérfanos (48 leyes encadenadas related N↔N+1 + 16 puentes cross-corpus, sobre todo **tensiones** valiosas: L1↔humildad (Jocko), L5↔reputación-Naval, L9↔intenciones-no-importan, L23↔maestría-1-o-2-cosas, L43↔power-of-relationships [coerción vs seducción], L46↔celos, L47↔ego, L48↔no-soluciones-permanentes). El cluster 48-laws contrasta deliberadamente con los corpus de integridad (Jocko) y suma-positiva (Naval). **Con esto se completan los 3 libros de la TAREA 2: Naval (235), Atomic Habits (84), 48 Laws (48).** Previo: TAREA 2 libro 2 — **«ATOMIC HABITS» (James Clear, 2018) COMPLETO**: book-mode, commit+push por capítulo, **+84 AKUs** (1708→1792; 23 concept, 18 method, 43 claim) + **1 framework TAKU** (cuatro-leyes-del-cambio-de-conducta). THE FUNDAMENTALS (hábito-atómico, agregación-marginal, plateau-of-latent-potential, sistemas-vs-metas, 3-capas-identidad, habit-loop) + LAS 4 LEYES DEL CAMBIO DE CONDUCTA (1ª Make It Obvious: scorecard/implementation-intentions/habit-stacking/entorno; 2ª Make It Attractive: dopamina/supernormales/temptation-bundling/normas-sociales; 3ª Make It Easy: motion-vs-action/mínimo-esfuerzo/two-minute-rule/commitment-device; 4ª Make It Satisfying: recompensa-inmediata/habit-tracker/never-miss-twice/accountability) + ADVANCED TACTICS (talento/genes/big-five, goldilocks-rule, aburrimiento, maestría=hábitos+práctica-deliberada, reflexión-y-revisión) + Little Lessons (system-1/2, satisfacción=liking−wanting, identidad-pequeña-y-flexible). 15 figuras informacionales → blockquotes. 2º pase verify_graph 0 errores; INTEGRATE 5.5 → 0 huérfanos. **Integración cross-corpus muy rica**: 13+ puentes a Naval, varios a Jocko/Hormozi/32-principles (related, NO recreación — mismo concepto ≠ misma definición). Pendiente TAREA 2: Robert Greene «48 Laws of Power» (convertido). Previo: TAREA 2 libro 1 — **«THE ALMANACK OF NAVAL RAVIKANT» (ed. Eric Jorgenson, 2020) COMPLETO**: book-mode, commit+push por sección, **+235 AKUs** (1473→1708; 54 concept, 8 method, 173 claim) + **4 TAKUs** (framework como-hacerse-rico-sin-suerte, heuristic encontrar-tu-specific-knowledge, heuristic habitos-de-felicidad-naval, reference naval-recommended-reading). Part I Wealth (specific knowledge, leverage, accountability, judgment, productize-yourself, 4 tipos de suerte, juegos suma-positiva/cero) + Part II Happiness (felicidad=paz/ausencia-de-deseo, deseo=contrato-para-ser-infeliz, cambiar-aceptar-o-dejar, abrazar-la-muerte, rational-buddhism, el-presente-es-todo-lo-que-hay) + Saving Yourself (salud=prioridad-1, desajuste-evolutivo, dieta azúcar+grasa, meditación, choiceless-awareness) + Bonus (Life Formulas, Naval's Rules, Recommended Reading). Routing pipeline.sh + source-tag `naval` añadidos. Imágenes (31): QR codes + doodles Visualize Value → decorativo (0 blockquotes). 2º pase: verify_graph 0 errores, 235/235 con source-tag+aku_class; INTEGRATE 5.5 pass → 0 huérfanos (134 aislados enrutados a 14 anclas temáticas). Cross-corpus related a Power-MBA/Hormozi/Jocko, NO recreación (mismo término ≠ misma definición). Pendientes TAREA 2: JAMES CLEAR (Atomic Habits), Robert Greene (48 Laws). Previo: CORPUS JOCKO FASE 2 — **Libro 6 «THE CODE. THE EVALUATION. THE PROTOCOLS» (Willink/Berke/Armstrong, 2020) COMPLETO**: 3 secciones, commit+push por sección, **+20 AKUs** (1453→1473; 10 concept, 2 method, 8 claim) + **12 TAKUs** (1 heuristic el-codigo-10-compromisos, 1 framework la-evaluacion-eqh, 10 protocol). S1 The Code: the-code/the-path/eminently-qualified-human concepts + pequenas-elecciones-diarias claim. S2 The Evaluation: the-evaluation-concept + 6 pilares-concept (supports→the-evaluation) + scoring-0-5-method + 4 claims (eqh-camino-sin-fin, autoevaluacion-honesta-you-vs-you, mejorar-mas-dificil-al-crecer-capacidad, tiempo-recurso-mas-valioso). S3 The Protocols: caer-del-path-inevitable, paso-pequeno-reevaluar (method), buscar-ayuda-profesional-sin-ego, tras-el-exito-ir-mas-duro + 10 protocol TAKUs (ruptura, duelo, dinero, traicion, trabajo, disculpa, accidente, adiccion, trauma, lo-desconocido). Imágenes: 6 rúbricas de The Evaluation → 6 blockquotes `> **Figura**:` (commit 52c233e). Dedup (mismo autor Jocko, +source sin bump): empezar-aqui-y-ahora, disciplina-se-extiende, humildad-cualidad-mas-importante, ego-nubla-todo, no-sobrerreaccionar, power-of-relationships, ego-impide-evaluacion-honesta, good-mindset; protocolos justified_by reusan corpus Jocko (detach, prioritize-and-execute, the-warpath, extreme-ownership, incluso-en-la-muerte-hay-good, humildad-asumir-errores). 2º pase verify_graph 0 errores. **CORPUS JOCKO COMPLETO (libros 1-6).** Previo: **Libro 5 «THE 32 PRINCIPLES» (Gracie/Volponi) COMPLETO**: intro/foreword + 32 caps = **+94 AKUs** (1359→1453; 52 concept, 3 method, 39 claim) + **1 framework TAKU** (taku-32-principios-jiu-jitsu), commit por capítulo, verify_graph 0 errores tras fix de simetría (24 pares related principio↔sub-AKU). Granularidad máxima: cada principio = 1 concept-AKU núcleo + sub-conceptos/methods/claims con identidad propia. **Imágenes: las 41 NO son figuras de jiu-jitsu** — 33 QR (vídeos), 4 portada, 1 divisor, 3 back-matter; todas decorativas/referencia, 0 blockquotes (técnica en vídeos, no en figuras; texto autosuficiente). 8 puentes INTEGRATE nivel (a) al corpus liderazgo Jocko. 1 candidato `contradicts` flagged para Joan: miedo-al-fracaso-paraliza (Gracie) ↔ miedo-al-fracaso-es-bueno (Jocko) — modelado como `related` (reconciliable por intensidad), pendiente decisión humana. Previo: conversión 6 libros (PDF→MinerU / EPUB→epub_to_md) (PDF→MinerU / EPUB→epub_to_md) + routing/source-tag `jocko`. FASE 2 ingesta hiper-exhaustiva **Libro 1 «Extreme Ownership» COMPLETO**: intro + 12 caps = **+133 AKUs** (1044→1177; 80 claim, 41 concept, 12 method), commit+push por capítulo, verify_graph 0 errores en cada uno. 2º pase de verificación OK: 0 huérfanos, 1 componente interno, 133/133 con source-tag jocko + aku_class + source único. Arquitectura paraguas: extreme-ownership (axioma, 15 supports), laws-of-combat (4 leyes), dichotomy-of-leadership (14 dicotomías). El cluster Jocko es de momento 2º componente global; puentes (b) al grafo de negocio flagged para Joan. Candidatos TAKU flagged (no creados). Pendiente: libros 2-6 (dichotomy-of-leadership, discipline-equals-freedom, leadership-strategy-and-tactics, 32-principles, the-code). Previo: 2026-06-04 CIERRE DE GAPS PASO 3 — REFACTOR RETROACTIVO granularidad máxima: +234 AKUs (810→1044). Desplegados sub-items plegados en paraguas como AKUs propios `supported_by` el paraguas, en 8 módulos: 15 GA (+23: métricas/UTM/objetivos/plan), 14 influencers (+15: 10 cláusulas contrato + 4 KPI funnel + cesión), 06 vender (+39: 14 secciones pitch deck + 5 templates elevator + 7 dimensiones fit + 4 perfiles modelo + 5 claims financiación), 04 estrategia (+50: barreras + 4 ejes PEST + best-cost + niveles brand awareness + 8 posicionamiento + 9 principios blitzscaling + 4 factores crecimiento), 05 marketing digital (+59: 6 formatos display + 16 formatos contenido + 7 tips + 8 lead magnets + 4 cats CRO + flywheel + adblockers + branding raíz), 02 modelo negocio (+20: customer-persona dimensiones + 3 niveles no-clientes + 4 acciones ERIC + claims valor/segmentación), 03 lean (+9: fases optimizar-canales/escalar + 4 métodos validación entrevista), 07 liderazgo (+19: 4 estructuras org + 3 Deep Work + 4 zonas Ikigai + OKR objetivos-vs-KR). Dedup-merges: 5-2 (9 métricas), churn-rate, ab-testing, landing-page (re-source). verify_graph: 1044/1044 simétrico, 0 errores. Candidatos TAKU flagged (no creados): Customer Persona Canvas, ERIC/Four Actions, plantilla experimentos (framework); 9 reglas blitzscaling + 7 tips contenido (heuristic); apps meditación (reference). Previo: CIERRE DE GAPS PASO 2 — quick wins: +19 AKUs (791→810). 09-03 múltiplos de valoración (+4 method: EV/EBITDA, EV/Ventas, P/VC, P/FCF), 08-01 tríada fortalezas-debilidades-motivaciones (+1 concept), 18 hacks de copy desplegados (+7 claim), 20-2 fórmulas de títulos desplegadas (+7 method). Merge fuente 5-2 en 9 AKUs de métricas growth-engine (+0.10 confianza c/u). verify_graph: 810/810 simétrico, 0 errores. Previo: REINGESTA DIFERENCIAL HIPER-EXHAUSTIVA Hormozi: +259 AKUs (offers +51, leads +88, money +120), máxima granularidad — explota paraguas en sub-tipos individuales (4 upsells, 3 downsells, 3 continuity, 5 componentes MAGIC, tipos de garantía/escasez/urgencia), atomiza claims normativos y money-math methods, y 7 SPLIT cross-corpus (gross-profit, LTGP, price-to-value, lead-contactable, lead-magnet-hormozi, cta-hormozi, affiliate-hormozi). Total Hormozi: 389 AKUs. Previo: TRILOGÍA HORMOZI 1ª ingesta — 3 libros book-mode: +121 AKUs / +25 TAKUs. **100M Offers** (51 AKU, 9 TAKU: grand-slam-offer, value-equation, escasez/urgencia/bonos/garantías, MAGIC naming), **100M Leads** (53 AKU, 11 TAKU: Core Four —warm/cold outreach, content, paid ads—, lead getters —referidos/empleados/agencias/afiliados—, LTGP:CAC, client-financed-acquisition, more-better-new, open-to-goal), **100M Money Models** (17 AKU, 5 TAKU: money model 3 etapas, attraction/upsell/downsell/continuity offers). Dedups cross-corpus Power-MBA↔Hormozi: commodity, ecuacion-valor, cialdini-escasez, lead-concept, lead-magnet, cta, cltv-cac-ratio, cltv-gross-margin, marketing-afiliados, cac/cac-payback. Previo: pipeline módulo 07 «Leadership» → 233 AKUs / 32 TAKUs)._

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

**2026-06-07 (audit-graph cross-corpus)**: **0 errors** (`verify_graph` 1840/1840 simétrico, 0 body-drift, 0 wikilinks rotos). **Componentes conectados 4 → 1** (3 islas puenteadas). **+95 aristas** (8 islas + 87 cross-corpus en 6 lotes temáticos: liderazgo, disciplina/hábitos/ego, poder/influencia, riqueza/unit-economics, oferta/valor/copy, felicidad/mente/salud). Caso testigo Jocko↔Power MBA (liderazgo) verificado y cableado. Sub-conectados 1126 → 1080. Lista de **pares dudosos para revisión humana** + evaluación crítica del CLAUDE.md (GAP 1: relleno retroactivo cross-corpus) en `_meta/auditoria-grafo-2026-06-07.md` y `_meta/auditoria-claude-md.md`. TAKUs: 137/137 siguen `draft`.

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
