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