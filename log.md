# Log — AKU/TAKU Vault

Append-only operational history. Never edit past entries.

Format per entry:
```
## YYYY-MM-DD HH:MM — <event-type>
<one-line summary>
- <details, one bullet per fact>
```

Event types: `bootstrap` · `ingest` · `update` · `lint` · `capture` · `query` · `validate` · `deprecate` · `meta` · `reset`

---

## 2026-06-01 — bootstrap
Vault initialized from `_spec/AKU-System-Specification.md` and `_spec/TAKU-System-Specification.md`.
- Folder skeleton, templates, operating manual, slash commands.
- Branch `main`. `validated_by` identity: Joan Cepero.

## 2026-06-03 — reset
Cleaned test ingest (the 2.2-motores cluster of 11 AKUs + 1 TAKU + its PDF inside `raw/`) and established the permanent markdown-only flow.
- Removed: all 11 AKUs in `aku/`, the framework TAKU in `taku/frameworks/`, the `raw/2-2-motores-de-crecimiento/` folder (including the PDF that was inside it from the legacy flow).
- Reset: `index.md`, `log.md`, `_meta/pipeline-manifest.yml` to empty state.
- Added hard rules #9 (PDFs stay at origin, never in vault) and #10 (always quote paths with spaces/accents).
- Updated vault layout: `raw/<slug>/<slug>.md` + `raw/<slug>/images/` are the only contents of `raw/`. Source PDFs live at their origin path (G:\, OneDrive, etc.) and are read-only.
- Updated `/pipeline` § CONVERT description to emphasize originals-stay-put.
- Kept intact: `CLAUDE.md` operating rules (with the additions above), all templates, `scripts/pipeline.sh`, `.claude/commands/`, `.gitignore`, `_spec/`.

## 2026-06-03 — meta
Fixed two bugs in `scripts/pipeline.sh` surfaced on first external `/pipeline` run.
- mineru CLI not on git-bash PATH (user-install pip places `mineru.exe` under `$HOME/AppData/Roaming/Python/Python312/Scripts/`). Added `find_mineru()` probe + fallback to common user-install locations; `cmd_convert` now invokes `"$MINERU_BIN"`.
- `slugify` regex `s/\.[^.]+$//` was greedy and collapsed "2.1-Análisis..." to "2"; removed the redundant step (callers already strip extensions before calling slugify).
- Added `-b pipeline -l latin` flags to the MinerU invocation: forces CPU backend (default `hybrid-auto-engine` needs CUDA) and latin-alphabet OCR for Spanish/English content.

## 2026-06-03 — ingest
Source: `raw/2-1-an-alisis-de-un-modelo-de-negocio-innovacion-bmc/2-1-an-alisis-de-un-modelo-de-negocio-innovacion-bmc.md` (The Power MBA — Módulo 2.1, Business Model Canvas). Original PDF at `G:\Mi unidad\…\02-Innovación en los modelos de negocio\2.1-Análisis de un modelo de negocio- Innovacion - BMC.pdf` — untouched. First end-to-end pipeline run.
- MinerU pipeline backend (CPU, latin OCR): 9 pages → 106-line markdown + 17 image files. ~30s.
- Image classification: 7 referenced images, all decorative (fragments of one channels diagram: gear/person/hexagon icons + LinkedIn/WhatsApp brand logos). Consolidated 1 informational blockquote `> **Figura**:` summarizing the direct vs indirect channels diagram as a whole, since individual icons carry no transferable knowledge but the collective composition does. Lesson logged for future ingests: course slides often fragment one diagram into many icon files; classify at the group level.
- 14 AKUs created: 12 concept (BMC + 9 BMC blocks + canal directo + canal indirecto) + 2 claim (segmento-relevante, coste-prioridad-segun-estrategia). 0 method-AKUs (BMC has no formulas).
- 1 TAKU drafted: `taku-business-model-canvas` (framework, draft, llm-authored). 14 `justified_by` links, all llm-proposed.
- Bidirectional relations: 4 supports/supported_by pairs (recursos → costes, actividades → costes), 7 constrains/constrained_by pairs (segmentos → 4 right-side blocks; propuesta → 2 left-side blocks; 2 claims → 2 concepts), 12 related pairs (9 block ↔ BMC, 2 canal sub-types ↔ canales, 1 canal directo ↔ canal indirecto).
- Dedup: vacuous (empty graph post-reset).
- Lint preview: TAKU has 14 `justified_by` links (>7 threshold) — expected for a 9-block framework; will flag on next `/lint`. No other flags expected.
- Manifest: source entry added with `original: G:\Mi unidad\…\2.1-…pdf`, `raw_path: raw/2-1-an-alisis-de-un-modelo-de-negocio-innovacion-bmc/`, `ingested: 2026-06-03`.

## 2026-06-03 — ingest
Source: `raw/2-2-1-tiposmotorescrecimiento/2-2-1-tiposmotorescrecimiento.md` (The Power MBA — Módulo 2.2.1, Tipos de motores de crecimiento). MinerU: 2 pages → 86 lines, no images.
- 5 concept-AKUs: motor-crecimiento (meta), motor-pago, motor-viral, motor-sticky, coeficiente-viralidad.
- 1 claim-AKU: viral-bajo-cltv-compatible (counterintuitive claim about viral engines tolerating low CLTV).
- 1 TAKU drafted: `taku-tres-motores-crecimiento` (framework, 6 justified_by, llm-proposed).
- Relations: 6 `related` edges (motor-crecimiento ↔ pago/viral/sticky; pago/viral/sticky pairwise; viral ↔ coeficiente-viralidad); 1 supports edge (viral-bajo-cltv-claim → motor-viral). All inverses written.
- Dedup against existing BMC cluster (14 AKUs): no overlap detected. Motors mention CLTV/CAC/CAC payback/churn rate but the source 2.2.1 does NOT define them; those concepts will come from source 2.2 (next), at which point retroactive `related` links from the motor concepts will be wired.
- Lint preview: TAKU has 6 `justified_by` links (≤7 threshold, no inflation flag). No flags expected.

## 2026-06-03 — ingest
Source: `raw/2-2-motores-de-crecimiento-proncipales-m-etricas/2-2-motores-de-crecimiento-proncipales-m-etricas.md` (The Power MBA — Módulo 2.2, Motores de crecimiento — principales métricas). MinerU: 1 page → 31 lines, no images.
- 7 concept-AKUs: CLTV, CAC, ARPU, churn rate, CAC payback, CLTV/CAC ratio, CLTV−CAC.
- 2 method-AKUs: subscription formula, transactional formula (mutually `context_breaks_at`).
- 2 claim-AKUs: gross margin over revenue, CLTV-CAC dual optimization.
- 1 TAKU drafted: `taku-digital-growth-engine-metrics-map` (framework, 11 justified_by, llm-proposed).
- Dedup against 2.2.1 motor cluster: motors mention these metrics but don't define them — so all 11 AKUs net-new, with retroactive `related` links from motor concepts to the metrics they reference. Bidirectional wikilinks updated on both sides (5 edits to 2.2.1 AKUs).
- TAKU-to-TAKU: `taku-digital-growth-engine-metrics-map` complementary to `taku-tres-motores-crecimiento` (the metrics map answers "what to measure" while the engine taxonomy answers "what motor operates").
- Lint preview: TAKU has 11 `justified_by` links (>7 threshold) — expected for comprehensive metrics map, will flag.

## 2026-06-03 — ingest
Source: `raw/2-3-conceptos-clave-de-las-plataformas/2-3-conceptos-clave-de-las-plataformas.md` (The Power MBA — Módulo 2.3, Conceptos clave de las plataformas). MinerU: 2 pages → 33 lines + 2 informational figure blockquotes. 2 referenced images (círculo virtuoso + vicioso), both informational with consolidated descriptive blockquotes inserted.
- 12 concept-AKUs: modelo-lineal, modelo-plataforma, network-effect, masa-crítica, círculo-virtuoso, círculo-vicioso, huevo-gallina, marketplace, on-demand-platform, content-platform, modelo-free, modelo-freemium.
- 0 claim, 0 method.
- 1 TAKU drafted: `taku-modelos-negocio-plataforma` (framework, 12 justified_by, llm-proposed). TAKU has 12 `justified_by` (>7) — link inflation flag expected for comprehensive platform framework.
- Relations: 11 `related` edges centered on modelo-plataforma-concept; 2 `supports` edges (network-effect → ambos círculos). All inverses written.
- Dedup against existing cluster (31 AKUs): no overlap. Platform vocabulary distinct from BMC, growth engines, and metrics clusters.

## 2026-06-03 — ingest
Source: `raw/2-4-segmentaci-on-y-targeting-conceptos-clave-clientes-y-mercado-objetivo/...md` (The Power MBA — Módulo 2.4). MinerU: 5 pages → 295 lines. 2 informational images (TAM/SAM/SOM + top-down/bottom-up) with blockquote captions.
- 10 new AKUs: 8 concept (variables-segmentación, customer-persona, mass-market-strategy, segmentado-strategy, nicho-strategy, early-adopter, cliente-buscando-vs-no, TAM/SAM/SOM) + 2 claim (falacia-1-porciento, nicho-recomendado-lanzamiento).
- 2 TAKUs drafted: `taku-estrategias-targeting` (framework, 5 justified_by) + `taku-customer-persona` (technique, 3 justified_by). Neither triggers link inflation.
- Dedup: `aku-segmentos-de-clientes-concept` (from BMC 2.1) got 2.4 as second independent source; llm_confidence 0.50 → 0.60.
- Relations: 8 `related` edges among targeting concepts; 1 `supports` (nicho-claim → nicho-strategy); 1 `constrains` (TAM/SAM/SOM → falacia-claim).

## 2026-06-03 — ingest
Source: `raw/2-5-propuesta-de-valor-propuestas-de-valor-conceptos-clave-a/...md` (The Power MBA — Módulo 2.5). MinerU: 3 pages → 119 lines + figure blockquote.
- 10 new AKUs: 7 concept (Power-Value-modelo, beneficio-funcional, beneficio-emocional, problema-resuelto, coste-percibido-amplio, competencia-amplia, cosas-importantes) + 3 claim (ecuacion-valor, emocion-prevalece-razon, reducir-costes-no-precio).
- 1 TAKU drafted: `taku-power-value-modelo` (framework, 11 justified_by — will flag link inflation).
- Dedup: `aku-propuesta-de-valor-concept` (from BMC 2.1) got 2.5 as second independent source; llm_confidence 0.50 → 0.60.
- 3 images: 1 informational blockquote consolidado (estructura del canvas Power Value + ecuación de valor); 2 son variantes decorativas con quotes que el texto ya incluye.
- Relations: 8 `related` edges entre componentes del Power Value; 3 `supports` (ecuación-claim → propuesta-valor; emocion-claim → beneficio-emocional; reducir-costes-claim → coste-percibido-amplio).

## 2026-06-03 — ingest
Source: `raw/2-6-oceano-azul-.../...md` (Kim & Mauborgne resumido por The Power MBA — Módulo 2.6). MinerU: 2 pages → 121 lines, 5 imágenes (no blockquotes individuales — contenido cubierto por texto + body de TAKU).
- 9 new AKUs: 7 concept (factores-competitivos, curva-valor, matriz-rice, océano-rojo, océano-azul, innovación-valor, no-clientes) + 2 claim (empresas-borregos, más-valor-menos-coste-no-tradeoff).
- 1 TAKU drafted: `taku-estrategia-oceano-azul` (framework, 9 justified_by — flag link inflation).
- Cross-source `related` wires:
  - factores-competitivos ↔ competencia-amplia (2.5)
  - innovación-valor ↔ reducir-costes-no-precio (2.5)
  - no-clientes ↔ cliente-buscando-vs-no (2.4)
- TAKU-to-TAKU: `taku-estrategia-oceano-azul` complementary a `taku-power-value-modelo` (ambos atacan el diseño de propuesta de valor, con énfasis distinto).
- Lint preview: 4 TAKUs >7 justified_by acumulados (BMC=14, metrics-map=11, plataformas=12, power-value=11, océano-azul=9). Todos esperados.

## 2026-06-03 — meta
Módulo 02-Innovación en los modelos de negocio completo. Procesados 7 PDFs (2.1 BMC + 2.2.1 motores tipos + 2.2 motores métricas + 2.3 plataformas + 2.4 segmentación targeting + 2.5 propuesta de valor + 2.6 océano azul). Resultado:
- 72 AKUs (58 concept · 2 method · 12 claim).
- 8 TAKUs en draft (5 frameworks: BMC, tres motores, métricas-motor, plataformas, targeting, Power Value, océano azul; 1 technique: customer-persona; — wait, 7 frameworks + 1 technique = 8).
- 2 dedup updates (propuesta-de-valor y segmentos-de-clientes, ambos llm_confidence 0.50→0.60).
- 7 raws conservados en `raw/<slug>/` con sus imágenes (PDFs originales intactos en G:\).
- ~14 imágenes informacionales con blockquotes; ~14 decorativas dejadas sin caption.

## 2026-06-03 — lint
First lint pass over módulo 02 (72 AKUs + 8 TAKUs). Detected **15 bidirectional asymmetries**, fixed all 15 in the same pass. Final result: 0 errors, 5 warnings (TAKU link inflation, all expected), 3 informational.
- 14 `related` asymmetries + 1 `supports` asymmetry caused by later-module AKUs wiring cross-module relations without updating the earlier file's inverse.
- Most affected files: aku-propuesta-de-valor-concept (added 4 `related` + 1 `supported_by`) and aku-segmentos-de-clientes-concept (added 5 `related`).
- Verified post-fix: 212 directed edges, 0 asymmetric, 0 missing targets, 0 isolated nodes, all sources[] resolve, all TAKU body headers complete per type.
- Warnings: 5 TAKUs with >7 justified_by (BMC=14, growth-metrics=12, plataformas=12, Power Value=11, océano-azul=9). All expected for comprehensive frameworks.
- Report: outputs/lint/2026-06-03-modulo-02.md (gitignored).
- Lesson logged for future ingests: when wiring a cross-module `related` link, always update BOTH AKU files' frontmatter AND both body wikilink sections in the same Edit batch — failing to do so propagates asymmetry across the graph.
## 2026-06-03 — ingest
Source: `raw/3-0-1-lean-startup-lean-startup-recursos/...md` (Eric Ries via The Power MBA — Módulo 3.0.1). 4 pages → 117 lines + 2 figure blockquotes.
- 13 new AKUs: 10 concept + 3 claim (Lean Startup cluster).
- 2 TAKUs: `taku-lean-startup-method` (framework, 12 jb) + `taku-plantilla-experimentos-mvp` (tool, 5 jb).
- New `context_breaks_at` pair: métricas-vanidosas ↔ métricas-accionables.
- 7 retroactive cross-source `related` to módulo 02. 2 in-cluster fixes after lint check.

## 2026-06-03 — ingest
Source: `raw/3-0-2-probando-modelos-de-negocio-testing-business-models-recursos/...md` (The Power MBA — Módulo 3.0.2). 3 pages → 14 lines (mostly tables) + tables flow through.
- 4 new AKUs: 4 concept (problem-solution-fit, etapas-startup, entrevista-problem-solution, falso-positivo-validation).
- 1 TAKU: `taku-entrevista-problem-solution` (technique, 5 jb, constrained_by falso-positivo). Complementary a `taku-plantilla-experimentos-mvp`.
- Dedup: `aku-product-market-fit-concept` (de 3.0.1) recibe 3.0.2 como segunda fuente; llm_confidence 0.50 → 0.60.
- 7 retroactive cross-source `related` wires post-lint check.

## 2026-06-03 — ingest
Source: `raw/3-01-01-experiments-template/...md` (The Power MBA — Módulo 3.01.01). 1 page → 5 lines, sin imágenes.
- **Sin AKUs/TAKUs nuevos**: el contenido es exactamente la plantilla Hipótesis/MVP/Aprendizaje, ya cubierta por `taku-plantilla-experimentos-mvp` creado durante el ingest 3.0.1.
- Dedup decision: NO añado 3.0.3 como segunda fuente a los AKUs hipotesis/mvp/aprendizaje-validado porque 3.0.3 los usa como labels del template (no los define conceptualmente con includes/excludes/implies). Sería inflación artificial de llm_confidence.
- Registrado en manifest como ingested con aku_count=0, taku_count=0. La plantilla TAKU ya está completa.

## 2026-06-03 — audit
Graph integration audit post-módulo 03. Detected 2 connected components (88 + 2 isolated TAM/SAM/SOM cluster). Applied 17 cross-cluster `related` wires in two tiers:
- **Tier (a)** — 8 text-anchored wires applied autonomously (ecosistema↔recursos/actividades/canales, cliente-buscando↔oceano-rojo, cosas-importantes↔propuesta-valor, emocion-claim↔propuesta-valor, mago-de-oz↔aprendizaje-validado, asumir-equivocarse↔no-dar-supuesto).
- **Tier (b)** — 9 conceptual wires user-approved (tam-sam-som↔segmentos+bmc rescate, modelo-lineal↔bmc, canal-directo↔modelo-lineal, nicho-recomendado↔innovar-vs-competir+early-adopter, cliente-buscando↔oceano-azul, ecuacion-valor↔coste-percibido, reducir-costes↔ecuacion-valor).

Plus 1 new tacit claim earlier in session: `aku-free-bootstrap-plataforma-claim` (Joan's tier-c knowledge, epistemic_type: tacit).

Result: graph passes from 2 components → **1 connected component**, 372→388 directed edges, 0 bidirectional errors.

Permanent rules established in CLAUDE.md § Integración del grafo: INTEGRATE step (5.5) in every ingest, `/audit-graph` slash command for periodic global audits, three-tier rigor classification (a applied / b proposed / c user-led), distinction conceptual real vs empirical coincidence, lint flag «componentes > 1 = fragmentación». Memoria `feedback_graph_integration.md` guardada.

## 2026-06-03 — pipeline (módulo 04, PDF 1/6)
Source: `raw/4-1-an-alisis-de-un-sector/...md` (The Power MBA — Módulo 4.1 «Análisis de un sector»). PDF convertido con MinerU (pipeline backend, latin OCR), 10 páginas → 215 líneas. 2 H1 (5 Fuerzas+barreras / Ciclo de vida) tratadas en una pasada (fuente corta).
- **3 imágenes informational** con blockquote `> **Figura**:`: diagrama 5 Fuerzas de Porter, curva del ciclo de vida del producto, flecha de escala de concentración.
- **15 AKUs nuevos** (13 concept + 2 claim):
  - Cluster 5 Fuerzas: `cinco-fuerzas-porter` (umbrella), `amenaza-sustitutivos`, `barreras-de-entrada`, `poder-proveedores`, `poder-compradores`, `rivalidad-competitiva`; soporte: `costes-de-cambio`, `commodity`, `barreras-de-salida`.
  - `ciclo-vida-producto`, `concentracion-sector`, `diferenciacion-sector`, `analisis-pest`.
  - Claims: `barreras-entrada-aumentan-rentabilidad`, `rivalidad-reduce-rentabilidad`.
- **3 framework TAKUs** (draft, llm-authored, links llm-proposed): `taku-cinco-fuerzas-porter` (6 jb), `taku-ciclo-vida-producto` (2 jb), `taku-analisis-pest` (1 jb). Triángulo `complementary` entre los tres + `cinco-fuerzas` ↔ `oceano-azul`.
- **INTEGRATE (5.5) — wires nivel (a) text-anchored aplicados** a clusters existentes:
  - `barreras-de-entrada` ↔ `network-effect`, `masa-critica` («economías de red», «masa crítica»).
  - `rivalidad-competitiva` ↔ `oceano-rojo`; `ciclo-vida-producto` ↔ `oceano-rojo` («Entra aquí el océano rojo»), `early-adopter`.
  - `amenaza-sustitutivos` ↔ `competencia-amplia`.
  - `commodity` ↔ `empresas-borregos`; `rivalidad-reduce-rentabilidad` ↔ `oceano-rojo`, `empresas-borregos`.
- Sin dedup-merges: módulo 04 (estrategia competitiva) no solapa con clusters 02/03.
- Sin pausas: ninguna ambigüedad de atomicidad/dedup. Pendiente OK del usuario antes de seguir con 4.2–4.5.

## 2026-06-03 — pipeline (módulo 04, PDF 2/6: 4.2.1)
Source: `raw/4-2-1-intro-estrategias-competitivas/...md` (The Power MBA — 4.2.1, intro). 38 líneas, 2 imágenes decorativas (portada vídeo + retrato cita Jack Welch).
- **2 concept-AKUs nuevos** (introductorios): `aku-ventaja-competitiva-concept`, `aku-estrategias-genericas-porter-concept` (umbrella de las 3/4 estrategias genéricas). Se enriquecerán y recibirán 4.2.2 como 2ª fuente en el siguiente PDF.
- Sin dedup-merges. Sin TAKUs (la intro no aporta estructura ejecutable; el framework va en 4.2.2).

## 2026-06-03 — pipeline (módulo 04, PDF 3/6: 4.2.2)
Source: `raw/4-2-2-estrategias-competitivas/...md` (The Power MBA — 4.2.2). 119 líneas, 1 imagen informational (matriz 2×2 estrategias genéricas) con blockquote.
- **6 AKUs nuevos** (3 concept + 3 claim): `liderazgo-en-coste`, `estrategia-diferenciacion`, `factores-internos-recursos-capacidades`; claims `atrapado-medio`, `diferenciacion-mayores-margenes`, `liderazgo-coste-imitable`.
- **1 framework TAKU**: `taku-estrategias-genericas-porter` (5 jb + 1 constrained_by). `complementary` ↔ cinco-fuerzas-porter; `alternative_to` ↔ estrategia-oceano-azul.
- **CONTRADICCIÓN modelada**: `atrapado-medio-claim` (Porter «stuck in the middle») ↔ `contradicts` ↔ `mas-valor-menos-coste-no-tradeoff-claim` (océano azul). Anclado en texto en ambos lados (el claim de océano azul cita literalmente «la estrategia competitiva tradicional»). Penalización determinista −0.30 a la claim más antigua: `mas-valor-menos-coste` 0.50 → 0.20. Ambos AKUs preservados; divergencia = señal epistémica.
- **Dedup/enriquecimiento**: `nicho-strategy` recibe 4.2.2 como 2ª fuente (lección distinta a 2.4 → corroboración → 0.50→0.60), statement enriquecido con framing Porter (3 dimensiones + sub-especialización). `ventaja-competitiva` y `estrategias-genericas-porter` reciben 4.2.2 como fuente SIN bump (misma lección que 4.2.1, regla de independencia: mismo autor/lección = una fuente).
- INTEGRATE: inverse `related` a barreras-de-entrada, mass-market, commodity, diferenciacion-sector, recursos-clave, actividades-clave; supported_by chains a estrategias-genericas y ventaja-competitiva.

## 2026-06-03 — pipeline (módulo 04, PDF 4/6: 4.3)
Source: `raw/4-3-estrategias-de-crecimiento/...md` (The Power MBA — 4.3). 110 líneas, 2 imágenes informational (eje y matriz completa de Ansoff) con blockquote.
- **9 AKUs nuevos** (7 concept + 2 claim): `matriz-ansoff` (umbrella) + 4 cuadrantes (`penetracion-mercado`, `desarrollo-productos`, `desarrollo-mercados`, `diversificacion`) + `crecimiento-organico-inorganico` + `integracion-vertical-adelante`; claims `riesgo-ansoff`, `crecimiento-inorganico-rapido`.
- **1 framework TAKU**: `taku-matriz-ansoff` (5 jb + 1 constrained_by), `complementary` ↔ estrategias-genericas-porter.
- INTEGRATE nivel (a): `penetracion` ↔ motor-crecimiento; `desarrollo-mercados` ↔ segmentos-de-clientes; `crecimiento-organico-inorganico` ↔ ecosistema-alianzas; `integracion-vertical` ↔ canal-directo/canal-indirecto/barreras-de-entrada/ventaja-competitiva.
- Sin dedup-merges (Ansoff/crecimiento no solapan con AKUs previos).

## 2026-06-03 — pipeline (módulo 04, PDF 5/6: 4.4)
Source: `raw/4-4-branding/...md` (The Power MBA — 4.4). 267 líneas, 5 imágenes (4 informational con blockquote: brand equity, pirámide brand awareness, círculo dorado, plan de marca; 1 decorativa: gota de agua).
- **13 AKUs nuevos** (10 concept + 3 claim): `marca`, `identidad-de-marca`, `brand-equity`, `brand-awareness`, `circulo-dorado`, `proposito-mision`, `valores-marca`, `atributos-marca`, `posicionamiento`, `plan-de-marca`; claims `marca-potente-beneficios`, `esencia-mas-que-logo`, `gota-en-oceano`.
- **2 framework TAKUs**: `taku-plan-de-marca` (5 jb + 1 constrained_by) y `taku-circulo-dorado` (2 jb), complementary entre sí; plan-de-marca complementary a power-value-modelo.
- INTEGRATE nivel (a): marca-potente/circulo-dorado ↔ ventaja-competitiva, barreras-de-entrada; posicionamiento ↔ estrategia-diferenciacion, diferenciacion-sector, customer-persona; plan-de-marca ↔ propuesta-de-valor, canales-de-distribucion.
- Sin dedup-merges (branding es cluster nuevo).

## 2026-06-03 — pipeline (módulo 04, PDF 6/6: 4.5)
Source: `raw/4-5-blitzscaling/...md` (The Power MBA — 4.5). 197 líneas, 2 imágenes decorativas (iconos de bullet rojo/verde). Tablas inline (tipos de crecimiento, etapas) leídas directamente.
- **6 AKUs nuevos** (5 concept + 1 claim): `blitzscaling`, `factores-crecimiento-blitzscaling`, `limitadores-crecimiento-blitzscaling`, `tipos-estrategias-crecimiento`, `etapas-organizacion`; claim `blitzscaling-cuando-oportunidad-enorme`.
- **2 TAKUs**: `taku-blitzscaling` (framework, 4 jb + 1 constrained_by) y `taku-principios-blitzscaling` (heuristic, 9 reglas contradictorias, 2 jb). `taku-lean-startup-method` precedes `taku-blitzscaling` (sequence recommended). complementary blitzscaling ↔ matriz-ansoff y ↔ principios.
- Los «9 principios» se modelan como TAKU heuristic (forma imperativa) en vez de AKU, por la regla de desambiguación AKU vs heuristic.
- INTEGRATE nivel (a): factores ↔ network-effect/masa-critica/motor-crecimiento; limitadores ↔ product-market-fit; tipos ↔ lean-startup-method/innovar-vs-competir/PMF; blitzscaling ↔ ventaja-competitiva/motor-crecimiento/innovar-vs-competir.
- Sin dedup-merges.

### Módulo 04 COMPLETO (6/6 PDFs)
49 AKUs nuevos + 11 TAKUs nuevos en el módulo 04. 1 contradicción modelada (atrapado-medio ↔ océano-azul). 0 PDFs fallidos.

## 2026-06-03 — pipeline (módulo 05, 5.1)
Source: `raw/5-1-clave-powerselling/...md` (The Power MBA — 5.1 «Power Selling»). 334 líneas, 5 imágenes (2 informational: StoryBrand SB7 + BrandScript; 3 decorativas: metáfora mente, ejemplos de anuncio/lead magnet).
- **6 concept-AKUs**: `leyes-persuasion-cialdini` (7 leyes), `vender-una-accion`, `conversacion-mente-cliente`, `estilo-editorial`, `lead-magnet`, `brandscript-storybrand`.
- **2 TAKUs**: `taku-leyes-persuasion-cialdini` (framework) + `taku-decalogo-power-selling` (heuristic, 10 reglas). Complementary entre sí.
- INTEGRATE: conversacion-mente-cliente ↔ customer-persona/cosas-importantes; lead-magnet ↔ cliente-buscando-vs-no; cialdini/estilo-editorial ↔ emocion-prevalece-razon; brandscript ↔ propuesta-de-valor.
- Sin dedup-merges.

## 2026-06-03 — pipeline (módulo 05, 5.2)
Source: `raw/5-2-m-etricas-clave-en-motores-de-crecimiento/...md` (The Power MBA — 5.2). Tabla-resumen de métricas (ARPU, Lifetime, Churn, CLTV, CAC, CLTV-CAC, CLTV/CAC, CAC payback, coef. viralidad).
- **0 AKUs nuevos**: recap exacto del cluster de métricas ya cubierto en módulo 2.2 (arpu, cltv, cac, churn-rate, cltv-minus-cac, cltv-cac-ratio, cac-payback, coeficiente-viralidad). Decisión conservadora: no se añade como 2ª fuente ni se sube confianza (misma org, tabla-resumen que usa las métricas como labels, no las redefine; mismo criterio que 3.01.01). Lifetime=1/Churn no se aísla como AKU (cubierto en fórmulas CLTV). Registrado como ingested para que /pipeline lo salte.

## 2026-06-03 — pipeline (módulo 05, 5.3)
Source: `raw/5-3-visi-on-estrat-egica/...md` (The Power MBA — 5.3 «Visión estratégica»). 158 líneas, 2 imágenes decorativas (embudos sin labels).
- **6 AKUs nuevos** (5 concept + 1 claim): `power-funnel` (incluye 5.3.1 como 2ª fuente), `funnel-corto-vs-largo`, `objetivos-negocio`, `palancas-marketing-digital`, `atribucion`; claim `conversion-olvidada`.
- **1 framework TAKU**: `taku-power-funnel` (4 jb + 1 constrained_by), complementary a `digital-growth-engine-metrics-map`.
- INTEGRATE fuerte con cluster métricas: palancas ↔ cltv/cac/cltv-minus-cac; conversion-olvidada ↔ cltv-cac-dual-optimization/cac; power-funnel ↔ motor-crecimiento/lead-magnet; atribucion ↔ cac/canales-de-distribucion.
- Sin dedup-merges.

## 2026-06-03 — pipeline (módulo 05, 5.3.1)
Source: `raw/5-3-1-tabla-power-funnel/...md` (tabla Power Funnel: etapas × estrategias/herramientas/métricas/responsables).
- **0 AKUs nuevos**: la tabla es la plantilla de etapas del Power Funnel, ya incorporada al statement de `aku-power-funnel-concept`, que cita 5.3.1 como 2ª fuente. Registrado como ingested.

## 2026-06-03 — pipeline (módulo 05, 5.3.2)
Source: `raw/5-3-2-objetivos-formula-que-lo-relaciona-todo/...md` (28 líneas, 1 imagen decorativa).
- **1 method-AKU**: `formula-objetivos-marketing-method` (Ventas/MB/ROI en función de las 4 palancas: tráfico × conversión × CLTV / CLTV-CAC). Related a objetivos-negocio, palancas-marketing-digital, cltv-minus-cac.
- Cierra el cluster estratégico de módulo 05 (5.3+5.3.1+5.3.2).

## 2026-06-03 — pipeline (módulo 05, 5.4.1)
Source: `raw/5-4-1-atracci-on-y-branding/...md` (180 líneas, sin imágenes). Lección de atracción/canales.
- **8 concept-AKUs**: `calidad-vs-cantidad-trafico`, `performance-marketing`, `inbound-marketing`, `outbound-marketing`, `canales-marketing-digital` (taxonomía de canales), `publicidad-nativa`, `marketing-influencers`, `roi-vs-roas`.
- **1 framework TAKU**: `taku-mix-canales-atraccion` (4 jb + 1 constrained_by), complementary a power-funnel.
- Dedup: «branding» de 5.4.1 = brand-awareness/marca (4.4) → no se duplica; se relaciona. Email/SEO/SEM/display/programática se pliegan en canales-marketing-digital.
- INTEGRATE: canales ↔ canales-de-distribucion/atribucion; calidad-cantidad ↔ palancas/power-funnel; publicidad-nativa ↔ estilo-editorial; influencers ↔ cialdini; roi-vs-roas ↔ objetivos-negocio/formula; inbound ↔ lead-magnet; performance ↔ brand-awareness.

## 2026-06-03 — pipeline (módulo 05, 5.4.2–5.4.11 directorios de referencia)
10 PDFs de referencia (herramientas, agencias, plataformas, ejemplos, formatos, tips), 0 AKUs nuevos cada uno. Su contenido conceptual ya está cubierto por las AKUs de 5.4.1 (canales-marketing-digital, inbound-marketing, publicidad-nativa, marketing-influencers) y de 5.1 (lead-magnet). Decisión conservadora (mismo criterio que 3.01.01): no se crean AKUs de listados/herramientas; se registran como ingested. Imágenes = capturas/logos de referencia (decorativas), no diagramas de conocimiento. Commit agrupado por eficiencia; cada PDF tiene su entrada en el manifest.
- 5.4.2 herramientas tráfico · 5.4.3 formatos anuncios display · 5.4.4 bloqueadores de publicidad · 5.4.5 ejemplos publicidad nativa · 5.4.6 herramientas email marketing · 5.4.7 agencias influencers · 5.4.8 plataformas influencers · 5.4.9 formatos content marketing · 5.4.10 tips generación de contenidos · 5.4.11 listado plataformas afiliados.

## 2026-06-03 — pipeline (módulo 05, 5.5.1)
Source: `raw/5-5-1-...captacion-y-nurturing-de-leads...md` (100 líneas; imágenes = ejemplos de lead magnet + diagramas de estados/workflow descritos en texto → decorativas).
- **6 AKUs nuevos** (5 concept + 1 claim): `lead`, `estados-lead-funnel`, `lead-nurturing`, `lead-scoring`, `marketing-automation`; claim `nurturing-segun-complejidad`.
- **Dedup/enriquecimiento**: `lead-magnet` recibe 5.5.1 como 2ª fuente (lección distinta de 5.1 → corroboración → 0.50→0.60), statement ampliado a «cualquier forma de captar datos de un lead».
- **1 framework TAKU**: `taku-lead-nurturing` (4 jb + 1 constrained_by), complementary a power-funnel.
- INTEGRATE: lead/estados ↔ power-funnel; nurturing/claim ↔ funnel-corto-vs-largo; lead-magnet ↔ lead.

## 2026-06-03 — pipeline (módulo 05, 5.5.2–5.5.4 directorios de referencia)
3 PDFs de referencia (ejemplos de lead magnets, herramientas de formularios, herramientas de marketing automation), 0 AKUs nuevos. Contenido cubierto por lead-magnet y marketing-automation. Commit agrupado; entrada por PDF en el manifest.

## 2026-06-03 — pipeline (módulo 05, 5.6.1 + 5.6.3; 5.6.2/5.6.4 referencia)
- **5.6.1 «Conversión»** (96 líneas; pirámide de conversión captionada, A/B img decorativa): 6 AKUs (`cro`, `cuello-botella-funnel`, `piramide-conversion`, `proceso-cro` [method], `ab-testing`, `landing-page`) + framework TAKU `taku-cro`. INTEGRATE: cro ↔ conversion-olvidada/palancas/power-funnel; proceso-cro ↔ lean-startup; ab-testing ↔ mvp.
- **5.6.3 «Consejos para CTA»** (85 líneas, ejemplos decorativos): 1 AKU `cta` + heuristic TAKU `taku-optimizar-cta`. cta ↔ vender-una-accion, cro, landing-page.
- **5.6.2 tabla herramientas** y **5.6.4 herramientas CRO**: directorios de referencia, 0 AKUs.

## 2026-06-04 — pipeline (módulo 05, 5.6 Kolenda — 16 libros de psicología de marketing)
Bundle `5.6-nickkolenda-Marketing full PDF` (16 PDFs book-length). Decisión documentada: por ser obras de referencia book-length y supletorias, se ingieren a **granularidad de tesis nuclear** — 1 concept-AKU por libro capturando su framework central (no capítulo-a-capítulo, que serían cientos de AKUs y desproporcionado). Conversión: 15 OK al primer intento + 1 fallo recuperado en reintento (Pricing Psychology, 70 págs).
- **15 concept-AKUs** (todos sourced, 0.50): ad-psychology, copywriting, color, font, ecommerce, visual-attention, ux, choice, pricing, packaging, naming, negotiation (12) + methods-persuasion, mental-imagery (imagine-reading), viral-marketing (3 companions).
- **0 AKUs**: `bonus-pdf` («The Tangled Mind», psicología evolutiva general, fuera del scope de marketing) → registrado como referencia.
- Cluster Kolenda conectado internamente + **6 puentes** al grafo principal (copywriting↔estilo-editorial, pricing↔ecuacion-valor, ecommerce↔cro, visual-attention/ux↔piramide-conversion, ad-psychology/methods/negotiation↔leyes-cialdini, naming↔marca, viral-marketing↔coeficiente-viralidad/motor-crecimiento-viral). Garantiza 1 componente.
- **PDF FALLIDO recuperado**: Pricing Psychology falló en la pasada batch (timeout/recurso) y convirtió OK en reintento individual.

## 2026-06-03 — pipeline (módulo 05, 5.7.1 + 5.8.1 + 5.8.2)
- **5.7.1 «Fidelización y retención»**: 2 AKUs (`fidelizacion-vs-retencion` concept, `retencion-no-es-mala` claim). El funnel no acaba en la venta; fidelización (voluntad) vs retención (lock-in/costes-de-cambio/network-effect/prepago). INTEGRATE: ↔ churn-rate, costes-de-cambio, power-funnel.
- **5.8.1 «Recomendación y viralización»**: 3 AKUs (`recomendacion-vs-viralizacion` concept, `boca-a-boca-supera-campana` + `recomendacion-depende-producto` claims). Reducen CAC ~0. INTEGRATE: ↔ coeficiente-viralidad, cac, viral-marketing-kolenda, leyes-cialdini, product-market-fit.
- **5.8.2 «Flywheel Funnel»**: 1 AKU (`flywheel-funnel`) + framework TAKU `taku-flywheel-funnel` (`alternative_to` power-funnel). Rueda marketing-ventas-servicio; velocidad/fricción. ↔ fidelizacion, inbound, power-funnel.
- Imágenes decorativas/descritas en texto.

### Módulo 05 COMPLETO (42 PDFs)
Resumen módulo 05: 42 PDFs procesados (incl. 16 libros Kolenda). +55 AKUs (48 concept + 2 method + 5 claim), +8 TAKUs. 1 conversión fallida y recuperada (Pricing Psychology). Lecciones nativas a granularidad completa; libros Kolenda a granularidad de tesis nuclear; directorios de herramientas/plataformas/ejemplos a 0 AKUs (referencia).

## 2026-06-04 — lint/integridad final (módulos 04 + 05)
Verificación por script tras módulo 05: **196 AKUs / 28 TAKUs**, **1 componente conectado** (~812 aristas, 0 huérfanos), **0 asimetrías bidireccionales** (AKU y TAKU), **0 body-drift** (frontmatter↔cuerpo), 0 wikilinks rotos, 0 AKUs sin aku_class. Reparadas 18 asimetrías intra-sesión (faltaban inversos en targets) + 1 type-mismatch (palancas-marketing-digital: conversion-olvidada movido de related→supports). index.md actualizado.

## 2026-06-04 — cleanup (eliminación AKUs Kolenda tesis-nuclear)
Borrados los 15 AKUs `*-kolenda-*` creados a granularidad de tesis nuclear (decisión del usuario: granularidad insuficiente; pendiente desglose capítulo a capítulo tras completar Power MBA). Reversible vía git; `raw/` de Kolenda conservados para el re-ingest real.
- **15 AKUs eliminados**: ad-psychology, choice, color, copywriting, ecommerce, font, mental-imagery, methods-persuasion, naming, negotiation, packaging, pricing, ux, viral-marketing, visual-attention (todos `-kolenda-`).
- **11 AKUs del grafo principal**: eliminada la referencia puente a AKUs Kolenda (frontmatter + body) dejando el resto intacto: atributos-marca, coeficiente-viralidad, cro, ecuacion-valor, emocion-prevalece-razon, estilo-editorial, leyes-persuasion-cialdini, marca, motor-crecimiento-viral, piramide-conversion, recomendacion-vs-viralizacion.
- **Manifest**: los 16 PDFs de `5.6-nickkolenda` marcados `ingested: null # pending-reingestion`, `aku_count: 0`, nota "borrado por granularidad insuficiente — pendiente desglose capítulo a capítulo tras completar Power MBA". `converted`/`raw_path` intactos.
- **Verificado**: 181 AKUs / 28 TAKUs, 0 referencias kolenda residuales, 0 wikilinks rotos, 0 asimetrías, 0 body-drift, 1 componente conectado, 0 huérfanos.
- Nota: CLAUDE.md prohíbe borrar AKUs (usar deprecated); ejecutado bajo override explícito del propietario, reversible por git.

## 2026-06-04 — lint  0 errors / 6 warnings / info

## 2026-06-04 — pipeline (módulo 06, 6.1.01)
Source: `raw/6-1-01-fit-entre-tu-proyecto-y-tu/...md` (Power MBA — 6.1 «Fit entre tu proyecto y tú»). 1 imagen (diagrama MATCH «TÚ ♥ MODELO DE NEGOCIO») captionada como informacional; tablas (implicaciones, anexo startup/tradicional/marketplace/ecommerce) ya extraídas por MinerU como HTML.
- **2 concept-AKUs**: `fit-proyecto-emprendedor`, `implicaciones-modelo-negocio` (7 dimensiones).
- **1 framework TAKU**: `taku-eleccion-proyecto-fit`.
- INTEGRATE: ↔ innovar-vs-competir (riesgo/incertidumbre), ventaja-competitiva.

## 2026-06-04 — pipeline (módulo 06, 6.3.01)
Source: `raw/6-3-01-fuentes-financiacion-quien-ok/...md`. La tabla del «quién/cuándo» ya fue extraída por MinerU como HTML; añadido además su render en **markdown estructurado** en el raw (honrando la instrucción de la tabla). Sin imágenes.
- **6 concept-AKUs + 1 claim**: `fuentes-financiacion` (umbrella), `fases-financiacion`, `bootstrapping`, `incubadora-aceleradora`, `venture-capital`, `venture-builder`; claim `vc-busca-x10`.
- **1 framework TAKU**: `taku-mapa-fuentes-financiacion` (5 jb + constrained_by vc-busca-x10), complementary a eleccion-proyecto-fit.
- INTEGRATE: fases-financiacion ↔ problem-solution-fit / product-market-fit / motor-crecimiento (mapa fase desarrollo); bootstrapping ↔ free-bootstrap-plataforma; venture-capital ↔ blitzscaling / etapas-startup; fuentes ↔ implicaciones-modelo-negocio (puente diferido de 6.1.01).

## 2026-06-04 — pipeline (módulo 06, 6.3.1)
Source: `raw/6-3-1-vender-tu-proyecto/...md` (intro al curso de relación con inversores). Sin imágenes.
- **1 concept + 1 claim**: `criterios-inversion`, `levantar-financiacion-como-ventas`. Sin TAKU (es introducción; el framework va en 6.3.3/6.3.4).
- INTEGRATE: criterios-inversion ↔ venture-capital; levantar-financiacion ↔ vender-una-accion, leyes-cialdini.

## 2026-06-04 — pipeline (módulo 06, 6.3.3)
Source: `raw/6-3-3-estructura-del-pitch-deck/...md`. Estructura del Pitch Deck (tabla de secciones ya en HTML por MinerU).
- **1 concept-AKU**: `pitch-deck` (estructura de ~11 secciones + opcionales).
- **1 framework TAKU**: `taku-pitch-deck` (3 jb: pitch-deck + criterios-inversion + levantar-financiacion-como-ventas).
- INTEGRATE: pitch-deck ↔ criterios-inversion, problem-solution-fit, tam-sam-som, bmc (las secciones del deck mapean a estos conceptos).

## 2026-06-04 — pipeline (módulo 06, 6.3.4)
Source: `raw/6-3-4-templates-elevator-pitch/...md`. Plantillas de elevator pitch. Sin imágenes.
- **1 concept-AKU**: `elevator-pitch`.
- **1 technique TAKU**: `taku-elevator-pitch` (2 jb), complementary a `taku-pitch-deck`.
- INTEGRATE: elevator-pitch ↔ pitch-deck, propuesta-de-valor, vender-una-accion, brandscript-storybrand.

### Módulo 06 COMPLETO (5 PDFs)
13 AKUs nuevos (11 concept + 2 claim) + 4 TAKUs (eleccion-proyecto-fit, mapa-fuentes-financiacion, pitch-deck [framework], elevator-pitch [technique]). 0 PDFs fallidos. La «tabla en imagen» resultó ya extraída por MinerU como texto/HTML; añadido render markdown de la tabla de financiación; única imagen real (diagrama MATCH) captionada.

Verificación final módulo 06: 194 AKUs / 32 TAKUs, 1 componente conectado, 0 asimetrías (AKU+TAKU), 0 body-drift, 0 wikilinks rotos. Reparada 1 asimetría intra-06 (propuesta-de-valor ← elevator-pitch).

## 2026-06-04 — reingesta diferencial (módulo 02)
Re-escaneo de los raw del módulo 02 aplicando la regla «nunca omitir AKU por escasez de info». 3 conceptos nuevos con identidad propia creados:
- `aku-lifetime-concept` (2.2) — métrica de permanencia (lifetime = 1/churn); ↔ churn-rate, cltv, arpu, cltv-subscription-formula.
- `aku-clasificados-concept` (2.3) — subtipo de plataforma (Wallapop/Vibbo, monetización publicitaria, modelo Free); ↔ modelo-plataforma, marketplace, modelo-free, on-demand.
- `aku-estimacion-tamano-mercado-concept` (2.4) — top-down vs bottom-up; ↔ tam-sam-som, falacia-1%.
Sin ambigüedades (ninguno era dedup de un AKU existente). Verificado: 197 AKUs, 0 asimetrías, 0 body-drift.

## 2026-06-04 — reingesta diferencial (módulo 03)
Re-escaneo de los raw del módulo 03 (Lean Startup). 3 conceptos nuevos con identidad propia (tipos de MVP que estaban listados pero no eran AKU propio):
- `aku-test-de-humo-concept` (3.0.1) — smoke test (landing/forms/CTA sin producto); ↔ mvp(supported_by), landing-page, cta, aprendizaje-validado.
- `aku-crowdfunding-validacion-concept` (3.0.1) — Kickstarter/Indiegogo como validación + financiación; ↔ mvp, aprendizaje-validado, fuentes-financiacion.
- `aku-lista-de-espera-concept` (3.0.1) — waitlist; ↔ mvp, aprendizaje-validado, lead-magnet.
AMBIGÜEDAD pendiente de consulta (no creado): `publicidad dirigida` como MVP — solapa con performance-marketing/outbound-marketing (5.4.1) y con test-de-humo. A decisión del humano: crear como AKU propio, o tratar como faceta de los existentes.
Verificado: 200 AKUs, 0 asimetrías, 0 body-drift.

## 2026-06-04 — reingesta diferencial (módulo 04)
Re-escaneo de los raw del módulo 04. 10 conceptos nuevos con identidad propia (nombre + mecanismo distinto), antes plegados en umbrellas:
- `economias-de-escala` (4.1/4.2.2) → supports liderazgo-en-coste + barreras-de-entrada.
- `monopolio`, `oligopolio` (4.1) → support concentracion-sector.
- `fusion`, `adquisicion`, `joint-venture`, `alianza-estrategica` (4.3) → support crecimiento-organico-inorganico; alianza ↔ ecosistema-alianzas.
- `fastscaling`, `crecimiento-clasico-startup`, `crecimiento-clasico-scaleup` (4.5) → support tipos-estrategias-crecimiento (junto a blitzscaling); startup ↔ lean-startup/PMF.
PLEGADOS deliberadamente (degradaciones de una escala / contenido estructurado, no entidades con mecanismo propio), marcados como candidatos: niveles de brand-awareness (top-of-mind/recall/recognition/unaware), etapas de organización (familia→nación), atomización, conglomerado.
Verificado: 210 AKUs, 0 asimetrías, 0 body-drift.

## 2026-06-04 — reingesta diferencial (módulo 05; Kolenda EXCLUIDO)
Re-escaneo de los raw nativos del módulo 05 (5.1–5.8). El sub-bundle 5.6-nickkolenda se OMITE deliberadamente (preferencia de usuario: pendiente de reingesta capítulo a capítulo). 15 conceptos nuevos con identidad propia, antes plegados en umbrellas:
- 7 leyes de Cialdini (5.1): `cialdini-reciprocidad`, `cialdini-compromiso-consistencia`, `cialdini-prueba-social`, `cialdini-simpatia`, `cialdini-autoridad`, `cialdini-escasez`, `cialdini-pertenencia` → support leyes-persuasion-cialdini.
- 8 canales (5.4.1): `seo-aso`, `sem-paid-search`, `paid-social`, `red-display`, `programatica`, `email-marketing`, `marketing-afiliados`, `publicidad-offline` → support canales-marketing-digital.
AMBIGÜEDAD pendiente (no creado): `content-marketing` — solapa fuertemente con `inbound-marketing` (¿AKU propio o faceta?). PLEGADOS (degradación/overlap): niveles de brand-awareness, PR, redes-sociales-orgánicas.
Verificado: 0 asimetrías, 0 body-drift.

## 2026-06-04 — reingesta diferencial (módulo 06)
6 conceptos nuevos: fuentes de financiación con nombre propio antes plegadas en el umbrella:
- `business-angel`, `fff`, `media-4-equity`, `socio-industrial`, `equity-crowdfunding`, `organismos-publicos` → support fuentes-financiacion.
Puentes: business-angel ↔ venture-capital/fases; fff ↔ bootstrapping; socio-industrial ↔ adquisicion/diversificacion; equity-crowdfunding ↔ crowdfunding-validacion (primo «reward» del módulo 03); media-4-equity ↔ publicidad-offline.

## 2026-06-04 — reingesta diferencial 02–06 COMPLETA
Total: +37 AKUs (02:+3, 03:+3, 04:+10, 05:+15, 06:+6). Grafo: 231 AKUs / 32 TAKUs, 1 componente conectado, 0 asimetrías, 0 body-drift, 0 wikilinks rotos, 0 sin aku_class. Kolenda excluido (preferencia usuario). 2 ambigüedades pendientes de consulta: `content-marketing` (¿AKU propio o faceta de inbound-marketing?) y `publicidad-dirigida` como MVP (¿propio o faceta de performance/test-de-humo?).

## 2026-06-04 — reingesta diferencial: resolución de ambigüedades
Las 2 ambigüedades pendientes resueltas como AKU propio (decisión del humano):
- `aku-content-marketing-concept` (canal/táctica distinta de inbound) → related ↔ inbound-marketing, canales-marketing-digital.
- `aku-publicidad-dirigida-mvp-concept` (instancia del paraguas test-de-humo: lanzar publicidad real, no el producto, para medir demanda) → related ↔ test-de-humo, performance-marketing, outbound-marketing.
Grafo final reingesta diferencial: 233 AKUs / 32 TAKUs, 1 componente, 0 asimetrías, 0 body-drift, 0 wikilinks rotos.

## 2026-06-04 — pipeline módulo 07 (Leadership) — 7.1.x «Liderarse a uno mismo»
Convertidos 3 PDFs del módulo 07 vía MinerU. Ingesta de 7.1.1 + 7.1.2 (plantilla):
**+15 AKUs** (11 concept + 4 claim) + **5 TAKUs** (1 tool, 3 technique, 1 framework).
- Concepts: liderazgo, tres-capas-liderazgo (self→teams→orgs), autoevaluacion-cuerpo-mente-alma,
  mente-de-mono, mindfulness, tests-personalidad, mbti, objetivos-personales, deep-work,
  minimalismo-digital, ikigai.
- Claims: autoliderazgo-prerequisito (constrains tres-capas), test-personalidad-solo-preferencias
  (constrains tests-personalidad), compartir-objetivos-compromiso, proposito-personal-sostenibilidad
  (constrains ikigai).
- TAKUs: taku-autoevaluacion-liderazgo-personal (tool), taku-practica-mindfulness (technique,
  complementary deep-work), taku-deep-work (technique), taku-objetivos-personales (technique,
  complementary ikigai), taku-ikigai (framework).
- 7.1.2 es la plantilla descargable de la autoevaluación cuerpo-mente-alma: 0 AKUs nuevos; añadida
  como 2ª fuente de aku-autoevaluacion-cuerpo-mente-alma-concept SIN bump de confianza (misma lección
  7.1, no fuente independiente — regla de independencia). Sus imágenes son iconos decorativos dentro
  de la tabla HTML (image_processing n/a).
- Imágenes 7.1.1: 4 informational captionadas (3-capas diana, ciclo mindfulness, 4 dimensiones MBTI,
  Venn Ikigai); 3 decorativas (mente-de-mono, portadas Deep Work / Digital Minimalism de Newport).
- Bridge pendiente: aku-tres-capas-liderazgo supports → aku-liderar-vs-gestionar-concept (se cablea
  en la ingesta de 7.2.1, donde nace ese AKU).
Verificación post-7.1.x: sin asimetrías ni body-drift dentro del lote.

## 2026-06-04 — pipeline módulo 07 (Leadership) — 7.2.1 «Liderar a otros»
**+15 AKUs** (10 concept + 5 claim) + **6 framework TAKUs**.
- Concepts: liderar-vs-gestionar, liderazgo-situacional, estilos-autoritario-delegativo, vision-empresa,
  cascada-estrategica-ejecucion (misión→visión→valores→objetivos→iniciativas→ejecución),
  cultura-corporativa, arquetipos-cultura (Clan/Adhocracia/Jerarquía/Mercado, modelo Cameron & Quinn),
  estructuras-organizacionales (funcional/divisional/matriz/proyectos), okr, ajuste-objetivos-tradicional.
- Claims: mix-liderazgo-gestion-segun-trabajo (constrains liderar-vs-gestionar),
  complementar-habilidades-equipo, estructura-cultura-siguen-estrategia (constrains cultura + estructuras),
  cultura-saludable-ventaja, revision-anual-falla-incertidumbre (constrains ajuste-tradicional).
- TAKUs: taku-liderar-vs-gestionar, taku-estilos-liderazgo-situacional, taku-mision-vision-valores,
  taku-arquetipos-cultura, taku-estructuras-organizacionales, taku-okr (todos framework, draft).
  Complementarios: liderar-vs-gestionar↔estilos-situacional, mision-vision-valores↔okr,
  mision-vision-valores↔circulo-dorado (Sinek, anclado en texto), arquetipos-cultura↔estructuras.
- DEDUP (enriquecimiento, sin AKU nuevo):
  - misión organizacional → aku-proposito-mision-concept: +raw/7-2-1 (2ª fuente, 0.50→0.60), statement
    enriquecido con framing organizacional/ejecución (Tesla, estrella polar, círculo dorado).
  - valores organizacionales → aku-valores-marca-concept: +raw/7-2-1 (2ª fuente, 0.50→0.60), statement
    enriquecido con cultura/ejecución.
- INTEGRATE (paso 5.5) — el módulo 07 creó 6 componentes; reunificado a 1 con 5 puentes nivel (a)
  anclados literalmente en el texto de las fuentes (agente aplica, reporta):
  1. ikigai ↔ proposito-mision (related) — 7.2.1: «Podemos compararlo con el propósito de nuestra vida personal».
  2. tres-capas → liderazgo-situacional (supports) — capa «liderar equipos» que el liderazgo situacional desarrolla.
  3. cultura-corporativa ↔ cascada-estrategica (related) — la cultura «depende de la misión/visión/valores».
  4. liderazgo ↔ tests-personalidad (related) — el liderazgo debe «alinearse con tu personalidad».
  5. autoevaluacion ↔ minimalismo-digital (related) — el área Mente evalúa «desconectar de distracciones digitales».
  + bridge tres-capas → liderar-vs-gestionar (capa equipos/organizaciones).
Verificación final módulo 07: 263 AKUs / 43 TAKUs, 1 componente conectado, 0 nodos aislados,
0 asimetrías bidireccionales, 0 body-drift, 0 wikilinks rotos (script format-aware AKU+TAKU).

---

## 2026-06-04 — pipeline módulo 08 «Desarrollo personal» PDF 1/2: 08.01.01 Diagnóstico estratégico personal

+3 AKUs (1 concept + 2 claim):
- aku-diagnostico-estrategico-personal-concept — aplicar aparato estratégico de empresa (visión/objetivos/planes/KPIs) a la persona.
- aku-claridad-objetivos-fortalezas-exito-claim — sin claridad de objetivos/fortalezas/motivaciones, el éxito es más difícil.
- aku-alineacion-laboral-motivaciones-felicidad-claim — (Carlos Puig) trabajo alineado con motivaciones/fortalezas ↑ felicidad.
Relations: related ↔ objetivos-personales-concept, autoevaluacion-cuerpo-mente-alma-concept (3 capas sync).
Imágenes: 2 decorativas (portada Power MBA + retrato Carlos Puig). 0 TAKUs.
Posible dedup leve anotado para revisión: claridad-objetivos-exito vs autoliderazgo-prerequisito (conservados separados — distinto objeto).

## 2026-06-04 — pipeline módulo 08 «Desarrollo personal» PDF 2/2: 08.01.02 Herramientas de desarrollo personal

+2 AKUs concept:
- aku-descubrir-fortalezas-feedback-externo-concept — terceros revelan fortalezas/puntos ciegos que la introspección no capta.
- aku-motivaciones-desde-experiencias-pasadas-concept — analizar experiencias pasadas revela motivaciones intrínsecas.
+4 TAKUs technique (secuencia): test-del-aeropuerto → viaje-al-pasado → email-descubre-tus-poderes → analisis-situacion-laboral.
DEDUP: dimensiones de personalidad (E/I, S/N, T/F, J/P) → enriquecen aku-mbti-concept (+2ª fuente, mismo org → sin bump); puntos ciegos → +2ª fuente a aku-tests-personalidad-concept (sin bump).
Imágenes: 2 redundantes (tablas Test del aeropuerto + Viaje al pasado, ya en HTML del markdown).
Módulo 08 COMPLETO: 2 PDFs, +5 AKUs (3 concept + 2 claim) + 4 TAKUs.

## 2026-06-04 — pipeline módulo 09 «Contabilidad y finanzas» (HYPERDETALLE) PDF 1/4: 09.01.01 Balance de situación

+21 AKUs concept (hyperdetalle, una por concepto contable con identidad propia):
Estructura: balance-situacion, activo, activo-corriente, activo-no-corriente, pasivo, pasivo-corriente, pasivo-no-corriente, patrimonio-neto.
Partidas: caja-bancos, clientes-partida, existencias, inmovilizado-{intangible,material,financiero}, proveedores-partida, deudas-corto-plazo-entidades-financieras, otros-acreedores, deudas-largo-plazo-entidades-credito, obligaciones-y-bonos, capital-social, reservas-beneficios-no-distribuidos.
Cada partida con su rango de cuentas del PGC español. Árbol related interno simétrico (categoría↔partida).
Cluster contable aislado temporalmente del grafo principal — reconexión en INTEGRATE al cierre del módulo.
0 imágenes, 0 TAKUs (contenido puramente definicional).

## 2026-06-04 — pipeline módulo 09 (HYPERDETALLE) PDF 2/4: 09.01.02 Estado de resultados

+9 AKUs concept: estado-resultados, ingresos-contables, ventas, gastos-contables, coste-mercancias-vendidas (COGS), amortizacion, provisiones, gastos-financieros, partidas-extraordinarias.
INTEGRATE (a) anclado: estado-resultados↔balance-situacion, ingresos-contables↔patrimonio-neto, amortizacion↔activo-no-corriente, coste-mercancias↔existencias, gastos-financieros↔pasivo.
INTEGRATE (b) bajo autonomía (anotado para revisión): ingresos-contables↔flujos-de-ingresos (BMC), gastos-contables↔estructura-de-costes (BMC) → reconectan el cluster contable completo al grafo principal.
0 imágenes, 0 TAKUs.

## 2026-06-04 — pipeline módulo 09 (HYPERDETALLE) PDF 3/4: 09.02.01 Ratios de análisis financiero

+25 AKUs: 9 concept (solvencia, liquidez, ebitda, ebit, margen-bruto, beneficio-neto, NOF, fondo-de-maniobra, periodo-medio-maduracion) + 15 method (4 endeudamiento/solvencia, 3 liquidez, 4 márgenes, 2 rotación, formula-nof, ciclo-working-capital-dias) + 1 claim (margen-volumen-patron-sectorial).
Backbone concept→method (supports/supported_by) totalmente tipado; ventas/activo/existencias/coste-mercancias (de PDFs 1-2) actualizados con sus supports.
INTEGRATE (a) anclado: margen-volumen-patron-sectorial ↔ liderazgo-en-coste + diferenciacion-mayores-margenes.
1 imagen informational captionada (ciclo working capital PMM).
Verificación: 323 AKUs, 0 asimetrías bidireccionales, 0 body-drift.

## 2026-06-04 — pipeline módulo 09 (HYPERDETALLE) PDF 4/4: 09.03.01 Conceptos clave Finanzas (valoración)

+31 AKUs: 16 concept (valor-actual-presente, valor-futuro, tasa-de-descuento, prima-de-riesgo, van, tir, enterprise-value, equity-value, valoracion-empresa-enfoques, multiplo, estructura-de-capital, escudo-fiscal, free-cash-flow, cash-flow-accionistas, coste-fondos-propios-ke, coste-deuda-kd) + 11 method (descontar-actualizar, capitalizar-interes-simple/-compuesto, van-formula, tir-formula, valoracion-por-activos, valoracion-por-multiplos, per, ratio-de-apalancamiento, dcf, wacc) + 4 claim (van-tir-equivalencia, apalancamiento-aumenta-roe/-riesgo, apalancamiento-valoracion-optimo).
INTEGRATE (a) anclado a PDF3: multiplo ↔ ebitda/ventas/beneficio-neto; per supported_by beneficio-neto; escudo-fiscal ↔ gastos-financieros.
1 imagen informational (U invertida valor-empresa vs apalancamiento).
Verificación: 354 AKUs, 0 asimetrías, 0 body-drift, 0 sin aku_class.
Módulo 09 ingesta base: 4 PDFs, +86 AKUs (21+9+25+31). Pendiente 2º pase de verificación (relectura raw/).

## 2026-06-04 — módulo 09 SEGUNDO PASE DE VERIFICACIÓN (regla especial módulo 09)

Relectura de los 4 raw/ del módulo. Conceptos/fórmulas que habían quedado sin AKU → creados (+14 concept):
- PDF2 (estado resultados): ingresos-financieros, subvenciones, ingresos-por-arrendamientos, ingresos-prestaciones-servicios, gastos-de-explotacion, sueldos-y-salarios.
- PDF3 (ratios): periodo-medio-cobro (PMC), periodo-medio-pago (PMP), dias-de-existencias (componentes del ciclo de working capital).
- PDF4 (finanzas): valor-residual, interes-sin-riesgo, roe, roa, apalancamiento-financiero.
Todos enlazados a sus conceptos padre (ingresos-contables, gastos-contables, periodo-medio-maduracion, estructura-de-capital, etc.) con sync bidireccional.
Verificación módulo 09 COMPLETO: 368 AKUs (288 concept · 30 method · 50 claim), 0 asimetrías, 0 body-drift, 0 sin aku_class.
Módulo 09 total: 4 PDFs + 2º pase = +100 AKUs (21+9+25+31+14), 0 TAKUs (contenido conceptual/fórmulas).

## 2026-06-04 — pipeline módulo 11 «Google Ads» PDF 1/2: Anuncios de texto

+8 AKUs (6 concept: anuncio-texto-google-ads, titulo, descripcion, url-visible, extensiones-anuncio-google, tipos-extensiones-google; 2 claim: extensiones-mejoran-rendimiento, relevancia-anuncio-landing-rendimiento).
+2 TAKUs: heuristic optimizar-anuncio-texto-google, technique ab-testing-anuncio-google.
INTEGRATE (a) anclado: anuncio-texto ↔ sem-paid-search; descripcion ↔ cta-concept; url-visible ↔ landing-page; relevancia-claim ↔ landing-page.
7 imágenes decorativas (capturas de anuncios reales ya descritas íntegramente en el texto). Verificación: 376 AKUs, 0 asimetrías, 0 body-drift, TAKU links OK.

## 2026-06-04 — pipeline módulo 11 «Google Ads» PDF 2/2: Concordancia de palabras clave

+7 AKUs (6 concept: concordancia-palabras-clave, concordancia-amplia, modificador-concordancia-amplia, concordancia-frase, concordancia-exacta, concordancia-negativa; 1 claim: concordancia-alcance-relevancia-tradeoff).
+1 TAKU technique: estrategia-concordancias-google (ejemplo Montblanc).
INTEGRATE (a): concordancia-palabras-clave ↔ sem-paid-search + anuncio-texto-google-ads.
0 imágenes. Verificación: 383 AKUs, 0 asimetrías, 0 body-drift.
Módulo 11 COMPLETO: 2 PDFs, +15 AKUs (12 concept + 3 claim) + 3 TAKUs.

## 2026-06-04 — pipeline módulo 12 «Social media» (3 PDFs)

PDF1 (creación contenido): +1 concept (herramientas-creacion-contenido-rrss). 6 img decorativas.
PDF2 (gestión RRSS): +3 concept (herramientas-gestion-rrss, community-manager, escucha-social). 3 img decorativas.
PDF3 (tabla comparativa): +9 AKUs (hub comparativa-redes-sociales + 7 platforms twitter/instagram/linkedin/facebook/tiktok/pinterest/youtube + claim eleccion-red-social-segun-negocio) + 1 framework TAKU seleccion-red-social. 10 logos decorativos; tablas HTML = fuente.
INTEGRATE (a): herramientas-creacion ↔ content-marketing; comparativa ↔ paid-social.
Módulo 12 COMPLETO: 3 PDFs, +13 AKUs (12 concept + 1 claim) + 1 TAKU. Verificación: 396 AKUs, 51 TAKUs, 0 asimetrías, 0 body-drift.

## 2026-06-04 — pipeline módulo 13 «Growth hacking» (1 PDF): Herramientas y recursos

+1 concept (herramientas-growth-hacking) que cataloga las categorías funcionales de herramientas (bases de datos, emails, scrapers, competidores, extensiones Chrome, product marketing, contenido, data enrichment, market research, LinkedIn automation, email outreach). Directorio de nombres de producto (hollow nominal) → 1 concept de categorías.
INTEGRATE nivel (b) bajo autonomía (ANOTADO para revisión humana): herramientas-growth-hacking ↔ motor-crecimiento-concept (conexión conceptual, no anclada textualmente). 0 imágenes, 0 TAKUs.
Verificación: 397 AKUs, 0 asimetrías, 0 body-drift.

## 2026-06-04 — pipeline módulo 14 «Marketing de Influencers» (5 PDFs)

+4 AKUs concept: herramientas-marketing-influencers (14.01), colaboraciones-influencers-pagadas-vs-gratuitas (14.02), clausulas-contrato-influencers (14.03+14.05), medicion-resultados-influencers (14.06).
+2 framework TAKUs: contrato-influencers, medicion-campana-influencers.
14.05 (modelo contrato C21BeBrave) = mismo caso que 14.03 → folded como 2ª fuente, 0 AKUs nuevos.
INTEGRATE (a): los 4 conceptos ↔ marketing-influencers-concept (parent); medicion-resultados ↔ power-funnel.
Imágenes: 14.02 y 14.06 redundantes (tablas en HTML), 14.05 decorativa (firma). Verificación: 401 AKUs, 53 TAKUs, 0 asimetrías, 0 body-drift.

## 2026-06-04 — pipeline módulo 15 «Analítica» (4 PDFs, Google Analytics)

+4 AKUs concept: plan-de-medicion (15.1, hub), metricas-google-analytics (15.2, 8 métricas), codigos-utm (15.3, 5 params), tipos-objetivos-google-analytics (15.4, 4 tipos).
+1 framework TAKU: plan-de-medicion.
INTEGRATE (a) anclado: plan-de-medicion ↔ objetivos-negocio + metricas-accionables; metricas-ga ↔ metricas-accionables; codigos-utm ↔ atribucion; tipos-objetivos ↔ piramide-conversion.
Imágenes: todas redundantes (tablas en HTML). Verificación: 405 AKUs, 54 TAKUs, 0 asimetrías, 0 body-drift.

## 2026-06-04 — pipeline módulo 18 «Facebook & Instagram Ads» (1 PDF + 1 DOCX)

PDF (herramientas crear anuncios): +1 concept (herramientas-creacion-anuncios-facebook) + 1 claim (regla-20-texto-facebook-ads, con status_note sobre vigencia). 13 imgs decorativas (planes de precios).
DOCX (info.docx «Hacks copy», convertido con python-docx): +1 concept (hacks-copywriting: 7 principios) + 1 heuristic TAKU (hacks-copywriting).
INTEGRATE (a): herramientas-anuncios-fb ↔ herramientas-creacion-contenido-rrss + facebook; regla-20-texto ↔ facebook; hacks-copywriting ↔ cta.
Verificación: 408 AKUs, 55 TAKUs, 0 asimetrías, 0 body-drift.

## 2026-06-04 — pipeline módulo 20 «Copywriting» (3 PDFs) + AUDIT reunificación grafo

PDF1 (power words): +1 concept (palabras-frases-persuasivas) + heuristic TAKU power-words-copywriting.
PDF2 (fórmulas titulares): +1 concept (formulas-titulos-potentes, 7 plantillas) + framework TAKU formulas-titulos-potentes.
PDF3 (libros): +1 concept (libros-copywriting-recomendados, bibliografía). 21 portadas decorativas.
INTEGRATE (a): cluster copy ↔ hacks-copywriting (M18), cta, cialdini, titulo-anuncio-google.

AUDIT FINAL DE GRAFO: detectado 2º componente (isla de 17 nodos: solvencia/liquidez/working-capital del módulo 09 ratios). Reunificado con 6 puentes INTEGRATE nivel (a) anclados en texto: solvencia↔pasivo, liquidez↔activo-corriente, fondo-de-maniobra↔activo-corriente/pasivo-corriente, NOF↔existencias/clientes-partida/proveedores-partida.
Resultado: 1 componente conectado (468 nodos), 411 AKUs (326 concept · 30 method · 55 claim) + 57 TAKUs, 0 asimetrías, 0 body-drift, 0 sin aku_class, TAKU justified_by 100% válidos.

## 2026-06-04 — revisión humana (Joan): aprobaciones + nota de obsolescencia

- DEDUPS aprobados como SEPARADOS (3): claridad-objetivos-exito vs autoliderazgo-prerequisito; ingresos-prestaciones-servicios vs ventas; enriquecimientos mbti/tests-personalidad sin bump.
- PUENTES nivel (b) APROBADOS (3): ingresos-contables↔flujos-de-ingresos, gastos-contables↔estructura-de-costes, herramientas-growth-hacking↔motor-crecimiento.
- aku-regla-20-texto-facebook-ads-claim: status_note actualizado → Facebook eliminó la regla del 20% en 2020; el AKU queda DESACTUALIZADO; el humano lo marcará human_certainty: validated-false en próxima revisión (se conserva como evidencia negativa). human_certainty SIN cambios (sigue unvalidated, no lo toca el agente).

## 2026-06-04 — validación humana (Joan): aku-regla-20-texto-facebook-ads-claim → VALIDATED-FALSE

human_certainty.status: unvalidated → validated-false (validated_by: Joan Cepero, validation_date: 2026-06-04).
Motivo: Facebook eliminó la regla del 20% de texto en imágenes en 2020; el AKU registra el contenido del curso pero está desactualizado y ya no aplica.
contradicts: no añadido — no existe un AKU claim de buenas prácticas de Facebook Ads vigente y validated-true al que enlazar (los relacionados son definiciones: facebook-concept, paid-social-concept, herramientas-creacion-anuncios-facebook-concept). Se revisará si en futuras ingestas aparece un claim contradictorio.
Se conserva como evidencia negativa (✗ FALSIFIED). llm_confidence se mantiene 0.50 (informativo; señal: high-confidence-sourced + validated-false).
index dashboard: validated-false 0 → 1.
TAKUs: NO tocados (los activa el humano manualmente).

## 2026-06-04 — meta: custom type `reference` + migración bibliografía copywriting

- CLAUDE.md § TAKU creation rules: declarado el custom type `reference` con headers obligatorios (## Descripción · ## Recursos · ## Cómo usar esta referencia · ## Relaciones).
- DEPRECADO aku-libros-copywriting-recomendados-concept (status: active → deprecated; status_note: "Sustituido por taku-bibliografia-copywriting (reference)."). Se conserva; los related entrantes (aku-hacks-copywriting-concept, aku-leyes-persuasion-cialdini-concept) se mantienen.
- CREADO taku/reference/taku-bibliografia-copywriting.md (status: draft, content_validation: llm-authored). justified_by ← aku-hacks-copywriting-concept · aku-leyes-persuasion-cialdini-concept (aku-corpus-copywriting-concept no existe, omitido). Carpeta taku/reference/ creada.

## 2026-06-04 — ingest: TRILOGÍA HORMOZI completa (3 libros book-mode)

Ingesta capítulo a capítulo de los 3 libros de Alex Hormozi (`raw/libros/hormozi/`), autónoma, con dedup contra el grafo Power MBA creciente. source-tag: `hormozi`. Herramientas nuevas: `scripts/akugen.py` (generador con espejado bidireccional + cuerpo `## Relaciones`), `scripts/akupatch.py` (parcheo de ficheros existentes con sync 3-capas), `scripts/verify_graph.py` (simetría + body-drift + targets + componentes).

**Totales**: +121 AKUs nuevos, +25 TAKUs (51→... ver index). 10 dedup-merges cross-corpus Power-MBA↔Hormozi. verify_graph final: **532 AKUs, 0 errores, 1 componente conectado, 0 huérfanos**.

- **100M Offers** (51 AKU, 9 TAKU) — 11 caps: grand-slam-offer/categoría-de-uno, starving-crowd/4-indicadores-mercado/riches-in-niches, premium-pricing/virtuous-cycle, **value-equation** (dream-outcome/perceived-likelihood/time-delay/effort-sacrifice), crear-la-oferta (problemas→soluciones/trim-and-stack/delivery-cube), oferta-demanda/escasez, urgencia, bonos, garantías (4 tipos), MAGIC naming. Dedups: commodity, cltv-gross-margin, ecuacion-valor, cialdini-escasez.
- **100M Leads** (53 AKU, 11 TAKU) — 11 caps: lead/engaged-lead/lead-magnet, **Core Four** (warm-outreach/ACA, post-free-content/content-unit/give-ask, cold-outreach/big-fast-value, paid-ads/call-out-value-cta/what-who-when/LTGP:CAC/**client-financed-acquisition**), more-better-new/rule-of-100, **lead getters** (referidos/goodwill, empleados/3D-training, agencias, afiliados/whisper-tease-shout), open-to-goal/roadmap-7-niveles. Dedups: lead-concept (restaurado tras colisión), lead-magnet (0.70), cta, cltv-cac-ratio, marketing-afiliados.
- **100M Money Models** (17 AKU, 5 TAKU) — 6 caps: money-model (3 etapas), 4 tipos de oferta — attraction (win-your-money-back/giveaway/decoy/buy-x-get-y/pay-less-now), upsell (classic/menu/anchor/rollover), downsell (payment-plan/trial-penalty/feature), continuity (bonus/discount/waived-fee) — + capstone construir-money-model. Puente clave libro2↔libro3: money-model↔client-financed-acquisition.

**INTEGRATE**: aplicados solo puentes nivel (a) anclados en texto + algún (b) anotado (effort-sacrifice↔coste-percibido-amplio, constraint↔cuello-botella-funnel, money-model↔CFA, continuity↔churn/cltv-subscription, etc.). Manifest: entradas `100m-offers`/`100m-leads`/`100m-money-models` con `ingested: 2026-06-04` y `chapters_ingested` por capítulo (resumible). Commit por capítulo (`ingest: <libro> - <cap>`).

**Pendiente humano**: los 121 AKUs nuevos son `unvalidated`; los 25 TAKUs son `draft` con links `llm-proposed` (a validar por Joan). Kolenda (16 libros) sigue bloqueado por instrucción global.

## 2026-06-04 — reingest: DIFERENCIAL HIPER-EXHAUSTIVO trilogía Hormozi (+259 AKUs)

Segunda pasada sobre los 3 libros Hormozi a petición del usuario: máxima granularidad, atomizando cada concepto/claim/fórmula con identidad propia y separando los merges cross-corpus incorrectos. Método: 3 subagentes (uno por libro) enumeran exhaustivamente todo item con identidad (cruzado contra `outputs/aku-index-full.txt`), marcando SKIP/SPLIT/NEW; motor `scripts/_reingest.py` parsea las enumeraciones, ancla cada item por keyword a un concepto existente (relación o `supported_by` para sub-tipos de paraguas) y genera vía akugen + akupatch (inversos). verify_graph final: **791 AKUs, 0 errores, 1 componente, 0 huérfanos**.

- **+51 offers**: sub-conceptos M-A-G-I-C (Magnet/Avatar/Goal/Interval/Container), tipos de garantía (unconditional/conditional/anti), tipos+caps de escasez, métodos de urgencia, methods de proceso (GSO 5 pasos, listar-problemas, problema→solución, trim&stack, orden-variación), claims normativos (grow-or-die, tres-formas-crecer, honest-scarcity, extreme-scarcity, reversión-riesgo-nº1, stacking-guarantees, ofertas-fatigan…). **3 SPLIT**: gross-profit↔margen-bruto, LTGP↔cltv, price-to-value↔ampliar-gap.
- **+88 leads**: 5 categorías de topics, 7 componentes de headline, callouts verbales/no-verbales, 8 elementos del What, internal-core-four, 6 pasos affiliate-army, cualificación cliente/experto, 7 formas de pedir referidos, 6 pasos mejora-producto; money-math (benchmarks warm/cold, money-math warm, presupuesto-2x, coste-por-lead-payroll, diagnóstico-CAC-3x, affiliate-LTGP:CAC). **4 SPLIT**: lead-contactable↔lead-concept, lead-magnet-hormozi↔lead-magnet, cta-hormozi↔cta, affiliate-hormozi↔marketing-afiliados.
- **+120 money**: explota los paraguas en sub-ofertas individuales — upsells (classic/menu/anchor/rollover + unselling/prescription/A-B/card-on-file/BAMFAM/say-no-to-say-yes/hyper-buying), downsells (payment-plan/trial-with-penalty/feature + seesaw), continuity (bonus/discount/waived-fee) — y money-math (giveaway 6 pasos / 10-30% margen, payment-plan 7 pasos, standalone-ratio, billing-4-semanas/8,3%, processing-fee-3%, rollover-4×, anchor-5-10×) y ~80 claims normativos (store-credit, hard-selling-producto-débil, dar-refund-siempre, nunca-negociar-precio, no-arrancar-money-model-completo…).

Atomicidad: bajo el criterio del usuario «si dudas, crea». Cada nuevo AKU es `sourced`/`hormozi`/`unvalidated`/0.50, anclado al grafo por ≥1 relación. Pendiente humano: validar (`human_certainty`) los 259 nuevos. Herramientas nuevas: `scripts/_reingest.py` (motor de reingesta por enums).

## 2026-06-04 — gaps PASO 2 (quick wins): 09, 08, 18, 20 + merge 5-2 (+19 AKUs)

Cierre de gaps de alto valor / bajo coste detectados en el test de cobertura Power MBA. Granularidad máxima, bidireccionalidad three-layer, INTEGRATE nivel (a) anclado en texto. verify_graph tras cada commit: 0 errores. 791→810 AKUs.

- **09-03 múltiplos de valoración (+4 method)**: `ev-ebitda`, `ev-ventas`, `precio-valor-contable`, `precio-flujo-caja`. Todos `supported_by aku-multiplo-concept` + sus magnitudes componentes (EV, EBITDA, Ventas, Equity Value, FCF). `precio-valor-contable related valoracion-por-activos` (su input es el valor contable). Completa la familia de múltiplos que solo tenía PER. Commit standalone.
- **08-01 tríada autoconocimiento (+1 concept)**: `fortalezas-debilidades-motivaciones`. `supported_by` ← descubrir-fortalezas-feedback-externo / motivaciones-desde-experiencias-pasadas; `constrained_by` ← diagnostico-estrategico-personal; `related` ↔ ikigai / objetivos-personales. Cierra el triángulo diagnóstico→técnica→output. "Test 4 colores" NO creado (hollow nominal, sin contenido en fuente).
- **18 hacks de copy desplegados (+7 claim)**: investiga-antes / objetivo-definido / incluir-titular / promesas-concretas / aportar-pruebas / sin-florituras / incluir-cta. `supported_by aku-hacks-copywriting-concept`. INTEGRATE (a): titular↔formulas-titulos, cta↔cta-concept, pruebas↔leyes-persuasion-cialdini.
- **20-2 fórmulas de títulos desplegadas (+7 method)**: resultado-tiempo-objecion / numero-sustantivo-adjetivo / como-lograr-objecion / numero-errores-deseo / caso-exito / numero-trucos-resultado-objecion / porque-resultado. `supported_by aku-formulas-titulos-potentes-concept`. TAKU `taku-formulas-titulos-potentes`: justified_by ampliado a 7 (cap anti-inflación; 2 fórmulas cubiertas vía paraguas).
- **Merge fuente 5-2 (9 AKUs, sin creación)**: añadida la fuente 5-2 (misma tabla que 2-2) a sources[] de ARPU, Lifetime, Churn, CLTV, CAC, CLTV−CAC, CLTV/CAC, CAC Payback, Coef-viralidad. +0.10 confianza c/u (cltv-cac-ratio 0.60→0.70; resto 0.50→0.60).

**Pendiente humano**: los 19 nuevos son `unvalidated`; flags nivel (b) anotados para revisión (p.ej. tríada↔claridad-objetivos-exito, copy-sin-florituras↔palabras-persuasivas). Sin push de módulos 11/13: ya estaban ingeridos (2026-06-04, granularidad máxima) — re-pipeline era no-op.

## 2026-06-04 — gaps PASO 3 (refactor retroactivo, granularidad máxima): 15,14,06,04,05,02,03,07 (+234 AKUs)

Refactor retroactivo aprobado por el usuario: desplegar TODOS los sub-items plegados en paraguas como AKUs propios `supported_by` el paraguas (three-layer sync). 810→1044 AKUs. Ejecutado con subagentes de ingesta secuenciales (uno por módulo/submódulo para evitar carreras de escritura sobre ficheros-destino compartidos), patrón verificado del módulo 09. verify_graph: 0 errores tras cada commit. 44 commits.

- **15 Google Analytics (+23)**: plan de medición (5 bloques), métricas GA (8), códigos UTM (5 params + construcción URL), tipos de objetivo GA (4). Cada uno `supported_by` su paraguas.
- **14 influencers (+15)**: 10 cláusulas de contrato (briefing, exclusividad, remuneración, aprobación previa, cesión…), 4 etapas KPI del funnel de medición (notoriedad/engagement/visita/acción) como methods, cesión de uso del contenido. 14-02 ya cubierto (omitido).
- **06 vender el proyecto (+39)**: 14 secciones del pitch deck, 5 templates de elevator pitch, 7 dimensiones del fit modelo-emprendedor, 4 perfiles de modelo (marketplace/e-commerce/startup/tradicional, dedup vs definiciones existentes), 5 claims de financiación (VC/pública/venture-builder), 2 de vender.
- **04 estrategia (+50)**: 4 barreras de entrada + 4 ejes PEST (incl. político que faltaba), best-cost + claims competitivos, integración vertical/conglomerados/sinergias, brand-love + 4 niveles brand awareness + 8 opciones de posicionamiento + errores de marca, blitzscaling (4 factores crecimiento, 9 principios contradictorios, evolución rol fundador, winner-takes-all).
- **05 marketing digital (+59)**: branding (nodo raíz, faltaba) + tráfico, 6 formatos display + clasificación, adblockers + anuncios aceptables, publicidad nativa, 16 formatos de contenido + paraguas, 7 tips de contenido, 8 lead magnets nuevos + 4 reconectados desde formatos, herramientas formularios, 4 categorías de herramientas CRO + stack, fidelización-eleva-CLTV, viralización coste~0, velocidad/fricción del flywheel. Dedup-merges: churn-rate (+0.10), ab-testing (+0.10).
- **02 modelo de negocio (+20)**: costes fijos/variables, BMC interdependencia, customer-persona dimensiones de análisis, segmentos-vs-personas, foco early-adopters, dirigirse a no-buscadores, mass-market-vs-nicho, claims de propuesta de valor, 3 niveles de no-clientes (3 AKUs), 4 acciones ERIC (4 method-AKUs), innovación-valor-vía-ERIC.
- **03 lean startup (+9)**: beneficios Lean, velocidad de iteración, fases optimizar-canales/escalar, 4 métodos de validación en entrevista. Re-source de landing-page (3-0-1/3-0-2, confianza sin cambio: misma org). Dedup: identificar-hipótesis ya cubierto.
- **07 liderazgo (+19)**: 4 estructuras organizacionales, 3 estrategias Deep Work, 4 zonas del Ikigai, objetivos-vs-resultados-clave + beneficios OKR, autoconciencia del líder, aprende-nuevas-habilidades (dedup vs complementar-habilidades).

**Candidatos TAKU flagged (NO creados, pendiente de Joan)**: Customer Persona Canvas + ERIC/Four Actions + plantilla de experimentos (framework); 9 reglas de blitzscaling + 7 tips de contenido (heuristic); apps de meditación (reference).

**Pendiente humano**: los 234 nuevos son `unvalidated`. Flags nivel (b) acumulados para revisión / `/audit-graph` (p.ej. utm-content↔ab-testing, anuncios-aceptables↔publicidad-nativa, estructura-proyectos↔adhocracia, prueba-precio↔falso-positivo, posicionamiento-barato↔liderazgo-coste). Nota menor: ~14 AKUs nuevos llevan `llm_confidence: 0.5` (en vez de `0.50`) — cosmético, no afecta verify.

## 2026-06-04 — capa ejecutable + integración (b): 3 TAKUs nuevos + 22 conexiones (b) + normalización

Tras el refactor PASO 3, conexión de la capa ejecutable y aplicación de las conexiones conceptuales nivel (b) aprobadas por Joan.

- **3 TAKUs creados** (draft, llm-authored, links llm-proposed): `taku-four-actions-eric` (framework, justified_by 4 acciones ERIC + innovacion-valor-via-eric; complementary ↔ taku-estrategia-oceano-azul), `taku-tips-generacion-contenidos` (heuristic, justified_by 7 tips 5-4-10), `taku-apps-meditacion` (reference, justified_by mindfulness + descansos-un-minuto; complementary ↔ taku-practica-mindfulness). 83→86 TAKUs.
- **3 candidatos NO duplicados** (dedup): Customer Persona Canvas → ya existe `taku-customer-persona` (technique, enriquecido +1 justified_by customer-persona-dimensiones-analisis); plantilla experimentos → ya existe `taku-plantilla-experimentos-mvp` (tool, intacto); 9 reglas blitzscaling → ya existe `taku-principios-blitzscaling` (heuristic, enriquecido +1 justified_by paraguas nueve-principios).
- **22 conexiones nivel (b)** aplicadas como `related` bidireccional (three-layer), aprobadas por Joan (par #12 ya existía).
- **Normalización**: 14 AKUs `llm_confidence: 0.5` → `0.50`.

verify_graph: 1044 AKUs, 0 errores.

## 2026-06-05 — FASE 1 corpus Jocko: conversión 6 libros + routing/source-tag

Convertidos los 6 libros de `G:\Mi unidad\JOCKO` a markdown en `raw/libros/jocko/`: **extreme-ownership** y **dichotomy-of-leadership** (PDF → MinerU `-b pipeline -l latin`, 289 y 345 págs), **discipline-equals-freedom**, **leadership-strategy-and-tactics**, **32-principles**, **the-code** (EPUB → `epub_to_md.py`). Routing `*JOCKO*` → `raw/libros/jocko` en `raw_subdir_for`; source-tag `jocko` añadido a la tabla de CLAUDE.md; 6 entradas nuevas en `pipeline-manifest.yml` (`ingested: null`). Nota técnica: los nombres de Anna's Archive llevan apóstrofo tipográfico (U+2019) que git-bash corrompe al pasar argv a Python → conversiones lanzadas desde PowerShell con `PYTHONUTF8=1` (argv Unicode nativo), pasando slug limpio como destino. Commit `52a2b26`.

## 2026-06-05 — FASE 2 Jocko · Libro 1 Extreme Ownership — Introducción (cap 0)

Ingesta hiper-exhaustiva, granularidad máxima. **COBERTURA**: 11 items (4 concept, 1 method, 6 claim) → **11 AKUs nuevos** (1044→1055), 0 dedups (corpus nuevo). Núcleo: `extreme-ownership` (concept fundacional) `supported_by` humildad-asumir-errores + mejores-lideres-mision-no-ego; `laws-of-combat` (paraguas 4 leyes) `supported_by` extreme-ownership; `medida-significativa-liderazgo` `constrains` lider-efectivo-vs-inefectivo; + liderazgo-factor-mas-importante, liderazgo-en-todos-los-niveles, principios-combate-aplican-a-negocio, simple-but-not-easy, relax-look-around-make-a-call (method decisión bajo presión). Todos `sourced`/`jocko`/`unvalidated`/0.50.

**INTEGRATE 5.5**: sin puentes (a) text-anchored al grafo existente (corpus de liderazgo, no de negocio) → el cluster Jocko es de momento componente separado (2 componentes). **Flags (b) pendientes de Joan**: extreme-ownership ↔ aku-autoliderazgo-prerequisito-claim; mejores-lideres-mision-no-ego ↔ aku-autoconciencia-lider-carencias-claim / aku-autoevaluacion-cuerpo-mente-alma-concept; liderazgo-en-todos-los-niveles ↔ aku-estilos-autoritario-delegativo-concept; relax-look-around-make-a-call ↔ aku-asumir-equivocarse-claim. verify_graph: 1055 AKUs, 0 errores.

### Cap 1 «Extreme Ownership» (+11 AKUs)

**COBERTURA**: 11 items (todos claim; el concept `extreme-ownership` ya existía del intro → dedup, enriquecido con +11 `supported_by`). 1055→1066. Claims: lider-mirar-al-espejo, lider-responsable-mision-tactica-recursos, entrenar-mentorizar-underperformer ↔ lealtad-mision-sobre-individuo (par train→cut), atribucion-sesgada-exito-fracaso, owner-no-toma-credito-da-honor, extreme-ownership-cultura-equipo ↔ culpar-se-contagia (espejo +/−), ver-problemas-lente-objetiva, actitud-lider-determina-exito (claim empírico central del cap), no-obligar-sino-liderar. Los 11 `support` el concepto fundacional (ahora axioma con 13 incoming supports). Cross-related (a) a intro: atribucion↔humildad-asumir-errores, owner-no-credito + ver-problemas-objetiva↔mejores-lideres-mision-no-ego. Todos `sourced`/`jocko`/0.50. verify_graph: 1066 AKUs, 0 errores.

### Cap 2 «No Bad Teams, Only Bad Leaders» (+12 AKUs)

**COBERTURA**: 12 items (2 concept, 2 method, 8 claim). 1066→1078. Concepts: `no-bad-teams-only-bad-leaders` (`supported_by` extreme-ownership; related liderazgo-factor-mas-importante) y `tortured-genius` (anti-patrón, **contradicts** extreme-ownership; related atribucion-sesgada). Methods: repetir-tarea-hasta-estandar (`supports` no-es-lo-que-toleras), metas-intermedias-visibles. Claims: actitud-lider-marca-el-tono, no-es-lo-que-predicas-sino-lo-que-toleras (principio clave), gente-quiere-ganar-necesita-forcing-function, cultura-ownership-resiste-perdida-lider (resiliencia ↔ cultura/niveles), lideres-nunca-satisfechos-mejora-continua, si-no-ganas-no-tomas-buenas-decisiones (↔ medida-significativa), liderar-desde-posicion-mas-dificil, lealtad-mal-entendida-proteger-underperformers (↔ lealtad-mision/entrenar). 6 claims/methods `support` el concepto del cap. **Flag (b)**: metas-intermedias-visibles ↔ OKR/objetivos-clave (Power MBA) — coincidencia de dominio, no conectado. verify_graph: 1078 AKUs, 0 errores.

### Cap 3 «Believe» (+13 AKUs)

**COBERTURA**: 13 items (3 concept, 1 method, 9 claim). 1078→1091. Concepts: `believe-in-the-mission` (`supported_by` extreme-ownership), `detach-tactico-estrategico` (`supports` preguntar-por-que), `liderazgo-es-grupo-no-individuo` (related liderazgo-en-todos-los-niveles). Method: `preguntar-por-que` (paso atrás → deconstruir → analizar estratégico → preguntar arriba). Claims: creer-para-asumir-riesgos-y-convencer, parte-de-algo-mas-grande, creencia-del-lider-se-transmite, senior-debe-explicar-el-porque, objetivos-alineados-organizacion, feedback-hacia-arriba-cadena, subordinado-responsable-de-entender-porque (`supports` EO), preguntar-requiere-coraje, jefe-subestima-peso-de-su-posicion. Pendiente wire futuro: believe ↔ decentralized-command (cap 8). **Flag (b)**: objetivos-alineados ↔ OKR (Power MBA). verify_graph: 1091 AKUs, 0 errores.

### Cap 4 «Check the Ego» (+9 AKUs) — cierra PARTE I (Winning the War Within)

**COBERTURA**: 9 items (2 concept, 1 method, 6 claim). 1091→1100. Concepts: `check-the-ego` (`supports` extreme-ownership; related humildad/mejores-lideres-mision-no-ego) y `confident-but-not-cocky` (ref cap 12). Method: `check-ego-asumiendo-culpa-primero` (desactivar choque de egos asumiendo la culpa; related lider-mirar-al-espejo). Claims: ego-nubla-todo, ego-bueno-vs-destructivo (doble naturaleza del ego), el-ego-mas-dificil-es-el-propio, ego-impide-evaluacion-honesta (↔ lente-objetiva/mejora-continua), nunca-complacencia-subestimar-enemigo (`supports` confident-but-not-cocky), culpar-subordinado-natural-pero-contraproducente (↔ culpar-se-contagia). «It's about the mission not you» → dedup a mejores-lideres-mision-no-ego. **PARTE I completa** (intro + caps 1-4): 56 AKUs. verify_graph: 1100 AKUs, 0 errores.

## 2026-06-05 — FASE 2 Jocko · Libro 1 Extreme Ownership — PARTE II (Laws of Combat)

### Cap 5 «Cover and Move» — Law of Combat #1 (+8 AKUs)

**COBERTURA**: 8 items (2 concept, 1 method, 5 claim). 1100→1108. `cover-and-move` (1ª ley = trabajo en equipo) `supports` laws-of-combat (paraguas, ahora con su 1er hijo). `main-effort-supporting-efforts` (concept, se relacionará con prioritize-execute cap 7). Method: cover-and-move-construir-relacion. Claims: romper-silos-interdependencia, subteams-compiten-pierden-perspectiva, lider-mantiene-perspectiva-estrategica (↔ detach/parte-de-algo-mas-grande), equipo-gana-o-falla-en-conjunto, competidor-es-externo-no-interno (reframe «el enemigo está fuera»). verify_graph: 1108 AKUs, 0 errores.

### Cap 6 «Simple» — Law of Combat #2 (+9 AKUs)

**COBERTURA**: 9 items (2 concept, 1 method, 6 claim). 1108→1117. `simple-law-of-combat` `supports` laws-of-combat (related simple-but-not-easy, distinto: éste = mantén los planes simples). `el-enemigo-tiene-voto` (concept: la realidad perturba el plan → exige simplicidad). Method: incentivos-simples-pocas-metricas (2-4 áreas, visibles). Claims: complejidad-se-agrava-cuando-falla, briefear-al-minimo-comun-denominador (accountability del líder sobre la comprensión), facilitar-preguntas-clarificacion (↔ preguntar-por-que), simplicidad-permite-ajuste-rapido, conexion-accion-consecuencia-conducta (operant conditioning → fundamenta incentivos), camino-de-menor-resistencia. verify_graph: 1117 AKUs, 0 errores.

### Cap 7 «Prioritize and Execute» — Law of Combat #3 (+9 AKUs)

**COBERTURA**: 9 items (3 concept, 2 method, 4 claim). 1117→1126. `prioritize-and-execute` `supports` laws-of-combat y `supported_by` relax-look-around-make-a-call (¡wire pendiente del intro resuelto! El method del intro ahora `supports` su concept hogar); related main-effort-supporting-efforts. Concepts: `target-fixation` (anti-patrón), `decisively-engaged`. Methods: contingency-planning-anticipar (habilita decentralized command), prioritize-and-execute-pasos (7 pasos explícitos). Claims: lider-abrumado-multiples-tareas-falla, pull-off-the-firing-line (↔ detach), prioridades-cambian-comunicar, enfocar-una-iniciativa-a-la-vez (↔ decisively-engaged). verify_graph: 1126 AKUs, 0 errores.

### Cap 8 «Decentralized Command» — Law of Combat #4 (+11 AKUs) — cierra PARTE II

**COBERTURA**: 11 items (4 concept, 7 claim). 1126→1137. `decentralized-command` `supports` laws-of-combat (related believe + contingency-planning + simple — anclados en texto). **laws-of-combat ya tiene sus 4 hijos** (cover-and-move, simple, prioritize-and-execute, decentralized-command). Concepts: `commanders-intent` (related believe/senior-explica-porque), `battlefield-aloofness` (anti-patrón), `span-of-control`. Claims: limite-cognitivo-6-10-personas (`supports` DC y span-of-control), decentralized-limites-de-autoridad (left/right limits), lideres-junior-proactivos-no-reactivos, decentralized-requiere-confianza-bidireccional (↔ feedback-hacia-arriba), micromanagement-disuelve-en-caos (extremo opuesto a aloofness), posicionamiento-del-lider-flexible (kill house), confianza-se-construye-no-se-da. **PARTE II completa** (caps 5-8, Laws of Combat). Acumulado libro 1: 93 AKUs (8/12 caps + intro). verify_graph: 1137 AKUs, 0 errores.

## 2026-06-05 — FASE 2 Jocko · Libro 1 Extreme Ownership — PARTE III (Sustaining Victory)

### Cap 9 «Plan» (+9 AKUs)

**COBERTURA**: 9 items (1 concept, 2 method, 6 claim). 1137→1146. `planning-process-estandarizado` (related simple/commanders-intent). Methods: leaders-checklist-planning (11 pasos explícitos), post-operational-debrief (3 preguntas: qué salió bien/mal/cómo adaptar). Claims: stand-back-be-the-tactical-genius (↔ detach/pull-off-firing-line), brief-orientado-a-frontline (↔ briefear-minimo-comun/facilitar-preguntas), calcular-y-mitigar-riesgo ↔ los-que-no-arriesgan-no-ganan (John Paul Jones), analisis-constante-medir-efectividad (↔ debrief/mejora-continua), decentralizar-proceso-planificacion (↔ decentralized-command). Buena densidad de cross-links intra-Jocko (no sub-isla). verify_graph: 1146 AKUs, 0 errores.

### Cap 10 «Leading Up and Down the Chain of Command» (+8 AKUs)

**COBERTURA**: 8 items (2 concept, 6 claim). 1146→1154. `leading-down-the-chain` (related decentralized-command/commanders-intent/senior-explica-porque) y `leading-up-the-chain` (`supported_by` extreme-ownership — liderar hacia arriba es EO aplicado al jefe; related leading-down). Claims: conexion-rol-big-picture-no-intuitiva, boss-no-da-soporte-culpate-primero (↔ mirar-al-espejo), leading-up-requiere-influencia-no-autoridad, humildad-aceptar-prioridades-superiores, presentar-frente-unido (desacuerdo público socava la cadena), ejecutar-decision-como-propia (disagree & commit; ↔ believe). «Mirar al espejo» y «dile qué harás» dedup a cap 1/cap 8. verify_graph: 1154 AKUs, 0 errores.

### Cap 11 «Decisiveness amid Uncertainty» (+8 AKUs)

**COBERTURA**: 8 items (2 concept, 1 method, 5 claim). 1154→1162. `decisiveness-amid-uncertainty` (related relax-look-around/prioritize-execute/contingency-planning) y `battlefield-promotion` (ascender talento de primera línea). Method: conjetura-educada. Claims: no-hay-solucion-100-correcta (↔ el-enemigo-tiene-voto), esperar-certeza-causa-paralisis (analysis paralysis), default-agresivo-proactivo-dictar-situacion (↔ proactivos-no-reactivos), lider-percibido-como-decisivo, cortar-cancers-del-equipo-rapido (↔ tortured-genius/lealtad-mision). verify_graph: 1162 AKUs, 0 errores.

### Cap 12 «Discipline Equals Freedom — The Dichotomy of Leadership» (+15 AKUs) — CIERRA LIBRO 1

**COBERTURA**: 15 items (14 concept, 1 claim). 1162→1177. Catálogo de dicotomías (puente al Libro 2). Umbrella `dichotomy-of-leadership` `supported_by` cada dicotomía específica (axioma con 14 supports, incluido `confident-but-not-cocky` del cap 4 wirado como instancia). `discipline-equals-freedom` (título; enriquecerá con Libro 3). 11 dicotomías concept: lider-y-seguidor, agresivo-no-prepotente, calmado-no-robotico, valiente-no-temerario, competitivo-buen-perdedor, atento-detalle-no-obsesionado, fuerte-con-resistencia, humilde-no-pasivo, callado-no-silencioso, cercano-pero-no-demasiado, balance-ownership-decentralized-command (related EO+DC). Claim meta: lider-se-desvia-por-inclinarse-demasiado. Granularidad máxima: cada dicotomía con nombre propio = AKU (se enriquecerán cuando se ingiera el Libro 2, que dedica capítulos a varias). verify_graph: 1177 AKUs, 0 errores.

**★ LIBRO 1 «EXTREME OWNERSHIP» COMPLETO**: intro + 12 caps = **133 AKUs nuevos** (1044→1177). Manifest `ingested: 2026-06-05`.

### ✅ 2º PASE DE VERIFICACIÓN + INFORME CONSOLIDADO — Libro 1 Extreme Ownership

**Verificación de integridad (133 AKUs del libro)**:
- `verify_graph`: 1177 AKUs, **0 errores** (simetría bidireccional, body-sync, targets válidos) — verificado tras cada uno de los 13 commits.
- 133/133 con source-tag `jocko` en `domain`; 133/133 con `aku_class`; 133/133 con `sources: [extreme-ownership.md]` (único). 0 desviaciones.
- **0 huérfanos** (degree 0). **1 solo componente conexo interno**: el cluster Extreme Ownership está completamente integrado consigo mismo (no hay sub-islas por capítulo).
- Clases: **80 claim, 41 concept, 12 method**. Nodos axioma (incoming supports): extreme-ownership (15), dichotomy-of-leadership (15), decentralized-command (8), no-bad-teams (7), planning-process-estandarizado (7), believe-in-the-mission, laws-of-combat (4 leyes).

**Cobertura por capítulo** (todos con paso COBERTURA previo): intro 11 · cap1 11 · cap2 12 · cap3 13 · cap4 9 · cap5 8 · cap6 9 · cap7 9 · cap8 11 · cap9 9 · cap10 8 · cap11 8 · cap12 15 = 133. Foco de extracción: secciones PRINCIPLE + APPLICATION TO BUSINESS (donde Willink/Babin destilan el conocimiento transferible). Conceptos célebres atomizados: the enemy gets a vote, commander's intent, span of control, tortured genius, battlefield aloofness, decisively engaged, battlefield promotion, stand back and be the tactical genius. Los 4 Laws of Combat y las ~12 dicotomías cada uno como AKU propio bajo su paraguas.

**Estructura del grafo**: arquitectura paraguas→hijos consistente (extreme-ownership ← {humildad, ego, no-bad-teams, believe, check-the-ego, leading-up...}; laws-of-combat ← {cover-and-move, simple, prioritize-and-execute, decentralized-command}; dichotomy-of-leadership ← 14 dicotomías; planning-process ← checklist/debrief/risk).

**Pendiente humano (Joan)**:
- Los 133 AKUs son `unvalidated` (validar `human_certainty`).
- **Cluster Jocko = componente separado del grafo de negocio** (2 componentes globales). Puentes nivel (b) flagged, NO escritos (esperan tu aprobación): extreme-ownership↔autoliderazgo-prerequisito; mejores-lideres-mision-no-ego/check-the-ego↔autoconciencia-lider/autoevaluacion-cuerpo-mente-alma; liderazgo-en-todos-los-niveles/decentralized-command↔estilos-autoritario-delegativo; relax-look-around/decisiveness↔asumir-equivocarse; metas-intermedias-visibles/objetivos-alineados↔OKR; conexion-accion-consecuencia-conducta↔incentivos (ya hay relación dominio marketing).
- **Candidatos TAKU flagged (NO creados, decisión AKU-céntrica de la instrucción Jocko)**: `taku-laws-of-combat` (framework, justified_by las 4 leyes), `taku-prioritize-and-execute` (protocol, los 7 pasos), `taku-planning-checklist` (tool, leaders-checklist-planning), `taku-post-operational-debrief` (protocol, 3 preguntas), `taku-dichotomy-of-leadership` (framework, las dicotomías). Crear si Joan lo aprueba.

Próximo libro: **dichotomy-of-leadership** (PDF, 345 págs) — enriquecerá los AKUs de dicotomías ya creados (dedup + 2ª fuente).

## 2026-06-05 — FASE 2 Jocko · Libro 2 The Dichotomy of Leadership (Willink & Babin 2018)

### Introducción + Cap 1 «The Ultimate Dichotomy» (+7 AKUs, +1 enrich)

**COBERTURA**: intro (1 claim + enrich umbrella) + cap1 (2 concept, 4 claim). 1177→1184. **Puente cross-libro**: `dichotomy-of-leadership` enriquecido con 2ª fuente (dichotomy-of-leadership.md) → confianza 0.50→0.60; ahora cubre EO cap12 + este libro. Intro: `liderazgo-requiere-balance-no-extremos` (tesis del libro: EO es el fundamento pero el liderazgo exige equilibrio, no extremos). Cap1: `ultimate-dichotomy-cuidar-vs-mision` (la dicotomía más difícil; related cercano-pero-no-demasiado/lealtad-mision), `burden-of-command`, cuidar-demasiado-impide-decisiones-duras, demasiado-desapegado-dana-al-equipo (↔ battlefield-aloofness), a-veces-hay-que-herir-para-ayudar, proteger-a-pocos-arriesga-a-todos (↔ lealtad-mision/equipo-gana-o-falla). verify_graph: 1184 AKUs, 0 errores.

### Cap 2 «Own It All, but Empower Others» (+7 AKUs, +1 enrich)

**COBERTURA**: 7 items (4 method, 3 claim) + enrich `balance-ownership-decentralized-command` (2ª fuente, 0.50→0.60, ahora 5 supports). 1184→1191. Claims: micromanagement-mata-iniciativa (↔ micromanagement-disuelve-en-caos), hands-off-laissez-faire-descoordina (↔ decentralized-limites-de-autoridad), asignar-lead-claro-evita-planes-divergentes (↔ main-effort/decentralizar-planificacion). Methods diagnósticos/correctivos: sintomas-de-micromanagement (7 señales), sintomas-de-hands-off (6 señales), corregir-micromanagement, corregir-hands-off. verify_graph: 1191 AKUs, 0 errores.

### Cap 3 «Resolute, but Not Overbearing» (+3 AKUs)

**COBERTURA**: 3 items (2 concept, 1 claim). 1191→1194. `resolute-but-not-overbearing` (`supports` dichotomy-of-leadership; related agresivo-no-prepotente —polo distinto, no dedup— y no-es-lo-que-toleras), `leadership-capital` (poder finito del líder; related confianza-se-construye), enforzar-estandares-siempre-con-el-porque (nunca «porque lo digo yo»; ↔ senior-debe-explicar-el-porque). verify_graph: 1194 AKUs, 0 errores.

### Cap 4 «When to Mentor, When to Fire» (+4 AKUs)

**COBERTURA**: 4 items (1 concept, 3 claim). 1194→1198. `when-to-mentor-when-to-fire` (related entrenar-mentorizar/lealtad-mision/no-bad-teams), lider-responsable-del-output-maximizar-potencial (ubicar a cada uno donde sus fortalezas rinden), invertir-en-uno-puede-perjudicar-al-equipo (la mantra no-bad-teams puede volverse en contra; ↔ lealtad-mal-entendida), ni-muy-rapido-ni-muy-lento-para-despedir (timing; ↔ cortar-cancers). verify_graph: 1198 AKUs, 0 errores.

### Cap 5 «Train Hard, but Train Smart» (+4 AKUs) — abre PARTE II (Balancing the Mission)

**COBERTURA**: 4 items (1 concept, 1 method, 2 claim). 1198→1202. `train-hard-but-train-smart`, train-how-you-fight (no hay crecimiento en la zona de confort), entrenamiento-realismo-fundamentos-repeticion (3 pilares; ↔ repetir-hasta-estandar), entrenamiento-desde-abajo-no-desde-arriba (EO del entrenamiento; ↔ extreme-ownership/analisis-constante). verify_graph: 1202 AKUs, 0 errores.

### Cap 6 «Aggressive, Not Reckless» (+5 AKUs, +1 enrich)

**COBERTURA**: 5 nuevos (2 concept, 3 claim) + enrich `default-agresivo-proactivo-dictar-situacion` (2ª fuente, 0.50→0.60: «Default: Aggressive» = mismo principio que EO cap11 → dedup/enrich). 1202→1207. `aggressive-not-reckless` (related valiente-no-temerario/calcular-mitigar-riesgo/default-agresivo), `disease-of-victory` (exceso de confianza tras éxitos; ↔ nunca-complacencia/confident-not-cocky), agresivo-significa-proactivo-no-iracundo (↔ calmado-no-robotico), hesitar-a-veces-es-prudente, sopesar-riesgo-recompensa-coste-inaccion (↔ calcular-mitigar-riesgo/esperar-certeza). verify_graph: 1207 AKUs, 0 errores.

### Cap 7 «Disciplined, Not Rigid» (+3 AKUs, +1 enrich)

**COBERTURA**: 3 nuevos (1 concept, 2 claim) + enrich `discipline-equals-freedom` (2ª fuente, 0.50→0.60). 1207→1210. `disciplined-not-rigid` (related discipline-equals-freedom/simple), disciplina-da-libertad-de-maniobra (los SOPs son una línea de la que desviarse; ↔ planning-process), exceso-de-sops-ahoga-iniciativa (↔ micromanagement-mata-iniciativa). verify_graph: 1210 AKUs, 0 errores.

### Cap 8 «Hold People Accountable, but Don't Hold Their Hands» (+3 AKUs) — cierra PARTE II

**COBERTURA**: 3 items (1 concept, 2 claim). 1210→1213. `accountability-no-como-herramienta-principal` (related believe/decentralized-command), accountability-no-escala-y-ciega-al-lider (atrapa al líder mirando abajo/dentro; ↔ leading-up/micromanagement), accountability-temporal-luego-soltar (↔ no-es-lo-que-toleras/corregir-micromanagement). **PARTE II completa** (caps 5-8, Balancing the Mission). verify_graph: 1213 AKUs, 0 errores.

### Cap 9 «A Leader and a Follower» (+1 AKU, +1 enrich) — abre PARTE III (Balancing Yourself)

**COBERTURA**: gran parte dedup (seguir al jefe = ejecutar-decision-como-propia/presentar-frente-unido EO cap10; la dicotomía = lider-y-seguidor EO cap12 → enrich 2ª fuente 0.50→0.60). 1 NUEVO: `excepcion-resistir-ordenes-ilegales-inmorales` (único caso para plantarse: órdenes ilegales/inmorales/no éticas/de riesgo grave; related lider-y-seguidor/ejecutar-decision/frente-unido). 1213→1214. verify_graph: 1214 AKUs, 0 errores.

### Cap 10 «Plan, but Remain Flexible» (+2 AKUs)

**COBERTURA**: 2 items (1 concept, 1 method); complacencia/riesgo-recompensa dedup a disease-of-victory/sopesar-riesgo. 1214→1216. `plan-but-remain-flexible` (no se puede planificar cada contingencia; related planning-process/el-enemigo-tiene-voto/simplicidad-ajuste), priorizar-3-4-contingencias-mas-probables (+ peor caso por fase; ↔ contingency-planning/leaders-checklist). verify_graph: 1216 AKUs, 0 errores.

### Cap 11 «Humble, Not Passive» (+1 AKU, +1 enrich)

**COBERTURA**: dedup a humilde-no-pasivo (EO cap12 → enrich 2ª fuente 0.50→0.60); «no pasivo/push back» ya cubierto por callado-no-silencioso. 1 NUEVO: `humildad-es-la-cualidad-mas-importante` (a los líderes SEAL se les destituía casi siempre por falta de humildad, no por incompetencia; `supports` check-the-ego; related humilde-no-pasivo/el-ego-mas-dificil). 1216→1217. verify_graph: 1217 AKUs, 0 errores.

### Cap 12 «Focused, but Detached» (+1 AKU, +2 enrich) — CIERRA LIBRO 2

**COBERTURA**: dedup a atento-detalle-no-obsesionado (EO cap12) y detach-tactico-estrategico (EO cap3) → ambos enrich 2ª fuente 0.50→0.60. 1 NUEVO: `detachment-default-high-port` (el desapego como posición por defecto, metáfora «high port»; `supports` detach-tactico-estrategico; related atento-detalle/pull-off-firing-line). 1217→1218.

**★ LIBRO 2 «THE DICHOTOMY OF LEADERSHIP» COMPLETO**: intro + 12 caps = **41 AKUs nuevos** (1177→1218) + **8 enriquecimientos cross-libro** de AKUs de EO (dichotomy-of-leadership, balance-ownership-decentralized-command, discipline-equals-freedom, default-agresivo-proactivo, lider-y-seguidor, humilde-no-pasivo, atento-detalle-no-obsesionado, detach-tactico-estrategico → 0.60 c/u). Manifest `ingested: 2026-06-05`.

**2º pase verificación Libro 2**: verify_graph 1218 AKUs / 0 errores (simetría, body-sync, targets). El catálogo de dicotomías de EO cap12 se ha desarrollado aquí (varias dicotomías ahora con 2 fuentes y sub-contenido propio: micromanagement/hands-off con diagnósticos+correcciones, leadership-capital, disease-of-victory, accountability-no-principal, etc.). Cluster Jocko sigue siendo 2º componente global (sin puentes (b) al grafo de negocio). Pendiente Joan: validar; aprobar puentes (b). Candidatos TAKU adicionales: taku-dichotomy-of-leadership (framework con las dicotomías), taku-diagnostico-micromanagement-hands-off (protocol).

## 2026-06-05 — FASE 2 Jocko · Libro 3 Discipline Equals Freedom (Willink 2017, field manual)

### Batch 1 «The Way of Discipline → Mind Control» (+6 AKUs, +1 enrich)

**COBERTURA**: 6 nuevos (3 concept, 1 method, 2 claim) + enrich `discipline-equals-freedom` (3ª fuente, libro título → 0.60→0.70). 1218→1224. `disciplina-raiz-de-toda-buena-cualidad`, `self-discipline-viene-de-dentro` (la disciplina viene de dentro), `mind-control-controla-tu-propia-mente` («no tienen voto» la debilidad/pereza/etc.), method `empezar-aqui-y-ahora` (↔ default-agresivo), claims no-hay-atajo-ni-hack, solo-te-puedes-controlar-a-ti-mismo (↔ extreme-ownership). verify_graph: 1224 AKUs, 0 errores.

### TAKUs Jocko libros 1-2 (+6 TAKUs, draft/llm-authored)

Creados los 6 TAKUs ejecutables flaggeados (86→92 TAKUs draft, todos `content_validation: llm-authored`, links `llm-proposed`, `status: draft` — pendientes de activación por Joan): `taku-laws-of-combat` (framework, justified_by laws-of-combat + 4 leyes; complementary ↔ prioritize-and-execute), `taku-prioritize-and-execute` (protocol, 7 pasos; complementary ↔ laws-of-combat/planning-checklist), `taku-planning-checklist` (tool, checklist 11 pasos; precedes → post-operational-debrief), `taku-post-operational-debrief` (protocol, 3 preguntas; follows ← planning-checklist), `taku-dichotomy-of-leadership` (framework, catálogo de dicotomías; complementary ↔ diagnostico), `taku-diagnostico-micromanagement-hands-off` (protocol, síntomas + correcciones). Fix en `akugen._taku_body`: precedes/follows ahora extraen `id` del dict (antes serializaba el dict en el wikilink del cuerpo). Simetría TAKU verificada entre los 6.

### Batch 2 «Weakness → Default Aggressive» (+9 AKUs, +1 enrich, +1 TAKU)

**COBERTURA**: 9 nuevos (2 concept, 2 method, 5 claim) + enrich `default-agresivo-proactivo` (3ª fuente → 0.60→0.70) + TAKU `gestion-del-stress` (technique). 1224→1233. Concepts: `destroyer-mode-emocion-y-logica` (equilibrio emoción/lógica, dicotomía), `compromiso-externo-si-interno-no` (dicotomía). Methods: `gestionar-stress-detach-y-perspectiva` (perspectiva→detach→controlable?resuelve:abraza), `cuestionarlo-todo-y-a-uno-mismo` (↔ preguntar-por-que). Claims: fortaleza-puede-ser-debilidad-y-viceversa, no-relajarse-hasta-completar-la-mision (relentless; ↔ nunca-complacencia), disciplina-se-extiende-a-todo, conocimiento-es-el-arma-definitiva, pelear-hasta-el-final-nada-que-perder. verify_graph: 1233 AKUs, 0 errores.

### Batch 3 «Nature vs Nurture → Focus» (+8 AKUs, +1 TAKU)

**COBERTURA**: 8 nuevos (1 concept, 7 claim) + TAKU `ir-igualmente` (heuristic). 1233→1241. `the-warpath` (la senda de guerra contra las propias debilidades → libertad). Claims: eleccion-vence-naturaleza-y-crianza (↔ extreme-ownership), miedo-al-fracaso-es-bueno (↔ contingency-planning), comida-basura-es-veneno, instinto-de-rendirse-es-mentiroso (↔ destroyer-mode), not-feeling-it-go-anyway (↔ camino-menor-resistencia/empezar-aqui-ahora), regret-solo-vale-por-la-leccion (↔ humildad-asumir-errores/post-op-debrief), mantener-objetivo-largo-plazo-a-la-vista (↔ metas-intermedias/enfocar-una-iniciativa). verify_graph: 1241 AKUs, 0 errores.

### Batch 4 «Hesitation → Staying Motivated» (+7 AKUs, +1 TAKU)

**COBERTURA**: 7 nuevos (2 concept, 5 claim) + TAKU `good-mindset` (heuristic). 1241→1248. Concepts: `draw-fire` (el líder absorbe el impacto), `good-mindset` («GOOD» icónico). Claims: hesitacion-es-el-enemigo (tensión/related con hesitar-a-veces-es-prudente — dicotomía contextual), incluso-en-la-muerte-hay-good, es-un-trabajo-de-cada-dia, no-mas-excusas, no-cuentes-con-motivacion-cuenta-disciplina (motivación vs disciplina; ↔ no-hay-atajo). verify_graph: 1248 AKUs, 0 errores.
