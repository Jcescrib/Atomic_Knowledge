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
