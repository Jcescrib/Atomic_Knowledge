# Log — AKU/TAKU Vault

Append-only operational history. Never edit past entries.

Format per entry:
```
## YYYY-MM-DD HH:MM — <event-type>
<one-line summary>
- <details, one bullet per fact>
```

Event types: `bootstrap` · `ingest` · `update` · `lint` · `capture` · `query` · `validate` · `deprecate` · `meta`

---

## 2026-06-01 — bootstrap
Vault initialized from `_spec/AKU-System-Specification.md` and `_spec/TAKU-System-Specification.md`.
- Folder skeleton created: `raw/` (flat), `capture/daily/`, `aku/`, `taku/{7 types}/`, `outputs/{queries,reports,lint}/`, `_meta/templates/`, `.claude/commands/`.
- Templates written: `aku.md`, `taku.md`, `daily.md`, `source.md`.
- Operating manual `CLAUDE.md` encoded (198 lines).
- Slash commands installed: `/ingest`, `/lint`, `/query`, `/capture`.
- `.gitignore` configured for Obsidian + outputs/.
- Branch renamed `master` → `main`. Initial commit `meta: bootstrap AKU/TAKU vault`.
- `validated_by` identity: Joan Cepero.
- Local semantic search (qmd) deferred — not wired in this bootstrap.

## 2026-06-02 — meta
CLAUDE.md amended: three-class AKU typology (concept · method · claim) encoded permanently.
- Added required frontmatter field `aku_class` (template updated).
- Amended hard rule #1 to admit concept and method AKUs alongside claim AKUs.
- Amended ingest workflow step 1 to extract all three classes; "do not discard content-bearing definitions or formulas as merely definitional."
- Added language convention: Spanish prose + canonical English technical terms (CLTV, CAC, ARPU, churn rate, payback, ROI, ...). Field names, IDs, and class labels remain English.
- Added lint flag for unclassified AKUs.
- Reason: initial extraction during 2.2-motores-de-crecimiento ingest applied strict Popperian filter and discarded definitions/formulas. Joan corrected — definitions are falsifiable by adequacy, implications, and boundary. Three-class rule encoded in feedback memory.

## 2026-06-02 — ingest
Source: `raw/2.2-Motores de crecimiento - proncipales métricas.pdf` (The Power MBA — Módulo 2.2).
- 11 AKUs created (7 concept, 2 method, 2 claim), all `unvalidated`, all `llm_confidence: 0.50` (single source, no contradictions).
  - concepts: `aku-cltv-concept`, `aku-cac-concept`, `aku-arpu-concept`, `aku-churn-rate-concept`, `aku-cac-payback-concept`, `aku-cltv-cac-ratio-concept`, `aku-cltv-minus-cac-concept`.
  - methods: `aku-cltv-subscription-formula`, `aku-cltv-transactional-formula` (mutually `context_breaks_at` / `breaks_context_of`).
  - claims: `aku-cltv-gross-margin-over-revenue` (constrains `aku-cltv-concept`), `aku-cltv-cac-dual-optimization` (supported by both core concepts and by `aku-cltv-minus-cac-concept`).
- Bidirectional relations verified: `supports`/`supported_by`, `constrains`/`constrained_by`, `context_breaks_at`/`breaks_context_of`, `related` — all pairs in sync.
- 1 TAKU drafted: `taku-digital-growth-engine-metrics-map` (type: framework, status: draft, content_validation: llm-authored, 11 `justified_by` links all `llm-proposed`).
- Dedup check: empty graph, all candidates net-new.
- Lint flag preview: TAKU has 11 `justified_by` links (>7 threshold) — will flag on next `/lint` for link-inflation review. Expected given the framework's comprehensive scope.

## 2026-06-03 — meta
Pipeline workflow + body-wikilinks rule encoded permanently. CLAUDE.md grew to 280 lines (over 250 soft target — accepted given the new section).
- New `/pipeline <folder>` command: discover → convert (MinerU) → adopt (pre-converted) → image classification (informational vs decorative, vision-analyzed with Spanish blockquote captions) → section-based ingest with resumability.
- New `scripts/pipeline.sh` (discover, convert, adopt, slug) — deterministic file ops; LLM phases stay in the slash command.
- New `_meta/pipeline-manifest.yml` — per-source state for resumability; legacy 2.2-motores entry pre-populated.
- Body wikilinks rule: every AKU/TAKU body must include `## Relaciones` mirroring frontmatter relations as `[[wikilink]]`. Three-layer sync (frontmatter inverse + body wikilink on both files). Templates updated.
- New hard rule #8: body Relaciones mandatory. Three new lint flags.
- Vault layout updated to document `scripts/` and `_meta/pipeline-manifest.yml`.
- Reason: Obsidian's graph view only renders edges from `[[wikilink]]` syntax, not from YAML frontmatter. Without the Relaciones body section, all AKUs appeared as disconnected nodes despite a fully-typed graph in the frontmatter.

## 2026-06-03 — update
Retrofit: appended `## Relaciones` body sections to all 11 AKUs + 1 TAKU from the 2.2-motores ingest, mirroring their current frontmatter relations as `[[wikilink]]`.
- Pure mechanical projection: no relation graph changes, only body additions.
- All 12 files now show their typed relations both in YAML (canonical) and in body wikilinks (Obsidian-graph-visible).
- `updated` field bumped to 2026-06-03 on all 12 files.
- Expected effect in Obsidian: the previously disconnected cluster now renders as a single connected graph centered on `aku-cltv-concept`.

## 2026-06-03 — meta
Normalized legacy 2.2-motores source into the `raw/<slug>/<slug>.pdf` layout used by `/pipeline`.
- `git mv "raw/2.2-Motores de crecimiento - proncipales métricas.pdf" "raw/2-2-motores-de-crecimiento/2-2-motores-de-crecimiento.pdf"` (preserves file history).
- Updated `sources[]` in all 11 AKU files to point at the new path.
- Updated the manifest entry: `raw_path: raw/2-2-motores-de-crecimiento/`, notes record the original flat path.
- No relation graph changes. No content changes. Pure layout normalization for consistency with future pipeline runs.
