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
