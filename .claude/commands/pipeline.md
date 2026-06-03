---
description: End-to-end ingestion of a folder of PDFs/markdowns via MinerU + vision + section-based AKU/TAKU extraction with resumability
argument-hint: <absolute-path-to-source-folder>
---

Run the full ingestion pipeline as defined in `CLAUDE.md` § Pipeline. Source folder: `$ARGUMENTS`.

If no argument was provided, ask the user for the folder path. The folder may contain PDFs (to be converted via MinerU) and/or pre-converted markdowns (adopted directly).

**Important**: do NOT run discover on the vault root. The script will return the vault's own infrastructure files if you do. Only run discover on EXTERNAL folders.

Execute the five phases below in order. At every phase, surface progress to the user as concise updates.

## Phase 1 — DISCOVER

1. Run `scripts/pipeline.sh discover "$FOLDER"` via Bash. Parse the output: two sections (`## PDFs`, `## Pre-converted markdowns`).
2. Read `_meta/pipeline-manifest.yml` (create it from `sources: []` if it does not exist).
3. For each discovered item, look up its likely slug (use `scripts/pipeline.sh slug "<basename>"`) in the manifest. Skip any item whose entry has `ingested: <date>` set.
4. Produce a discovery summary to the user:
   - N PDFs found, M to convert (others skipped: list IDs)
   - K markdowns found, J to adopt (others skipped: list IDs)
   - Total work units: M + J
5. If total work is 0, stop and inform the user.
6. If total work is >3 sources, **ask the user for confirmation before proceeding** (a book can take significant time).

## Phase 2 — CONVERT / ADOPT

**Hard rule reminder (from CLAUDE.md #9 and #10)**: source PDFs stay at their origin path. They are NEVER copied, moved, or modified during this phase — MinerU reads from the origin and only the produced markdown + images land in `raw/<slug>/`. Always quote paths with spaces or accents.

For each PDF queued to convert:
- Run `scripts/pipeline.sh convert "<absolute-pdf-path>"` (quotes mandatory for `G:\Mi unidad\...` style paths with spaces and accents). The script prints the destination `raw/<slug>/`.
- Append (or update) a manifest entry — critically, `original:` records the source PDF's origin path (NOT a path inside the vault):
  ```yaml
  - original: "G:\\Mi unidad\\...\\source.pdf"   # absolute origin path
    name_slug: <slug>
    raw_path: raw/<slug>/
    converter: mineru
    converted: <today>
    image_processing: null
    ingested: null
    chapters_ingested: []
    aku_count: 0
    taku_count: 0
    last_commit: ""
    notes: ""
  ```

For each markdown queued to adopt:
- Run `scripts/pipeline.sh adopt "<md-path>"`. The script prints the destination and reports whether an `images/` folder was located.
- Manifest entry: same shape, `converter: preexisting`.

The script:
- Discards MinerU scaffolding (`*middle.json`, `*model.json`, `*content_list*.json`, `*_layout.pdf`, `*_span.pdf`, `*_origin.pdf`).
- Keeps only `<slug>.md` + `images/` in `raw/<slug>/`.
- Rewrites image references inside the markdown to flat `images/<filename>` form so they resolve after the move.

## Phase 3 — PROCESS IMAGES AND TABLES

For every `raw/<slug>/<slug>.md` whose manifest entry has `image_processing: null`:

1. **Read the markdown.**
2. **Tables**: leave as-is. MinerU emits inline HTML (`<table>...`) which is knowledge-bearing text — the next phase reads them directly.
3. **Images**: find every `![](images/...)` reference. For each:
   - Check if the next non-empty line is already a `> **Figura**:` blockquote. If yes, SKIP (idempotent — already processed).
   - Use the Read tool with the image file path to view the image (Read renders images visually).
   - **Classify**:
     - **Informational** — diagram, chart, framework figure, schema, data visualization, screenshot of structured content, anything carrying transferable knowledge. Generate a precise Spanish-prose description and insert it as a blockquote IMMEDIATELY AFTER the image reference, on its own line(s):
       ```
       ![](images/<hash>.jpg)
       > **Figura**: <descripción precisa en español>. Enumerar elementos del
       > diagrama, leer datos clave del chart, transcribir labels y flechas.
       > Mantener términos técnicos en inglés canónico (CLTV, CAC, ROI, ...).
       ```
       Maximum fidelity. Do not summarize informational figures away — the AKU extractor in Phase 4 must be able to extract the figure's knowledge from this description alone.
     - **Decorative** — cover, author portrait, ornament, chapter divider, brand mark, page-edge graphic. Leave the image reference untouched, extract nothing.
4. Save the enriched markdown back to the same path with the Edit tool (multiple sequential Edits if needed; or one Write if a full rewrite is cleaner).
5. Stamp the manifest: `image_processing: <today>`.

## Phase 4 — INGEST

For each enriched markdown in `raw/<slug>/<slug>.md` whose manifest has `ingested: null`:

**Classify size/structure:**
- Count lines via `wc -l`.
- Grep for `^# ` (H1) and `^## ` (H2) headers.
- If line count ≤ 500 AND no H1 chapter structure: **short mode** (single pass).
- Otherwise: **book mode** (section-by-section).

### Short mode

Run the full ingest workflow from `CLAUDE.md` § Ingest workflow on the entire markdown. One commit: `ingest: <slug>`.

### Book mode

1. Parse H1 chapter boundaries. If no H1 exists but H2 does, fall back to H2.
2. For each chapter in order:
   a. Compute a chapter slug from its title (use `scripts/pipeline.sh slug "<chapter-title>"`).
   b. **Skip if** the chapter slug is already in `chapters_ingested: [...]` in the manifest.
   c. Extract the chapter's text content (from the chapter heading to the next same-level heading).
   d. Run the full ingest workflow on that chapter content alone. Dedup checks ALL existing AKUs in `aku/` (including those just created from earlier chapters of this same book — the graph grows as you proceed).
   e. Write AKUs and TAKUs with full frontmatter, bidirectional inverses, AND the `## Relaciones` body wikilinks per `CLAUDE.md` § Body wikilinks. **Three-layer sync**: frontmatter on this file + frontmatter inverse on the target file + body wikilinks on both.
   f. Update `index.md` (counts, validation queue, domain map).
   g. Append a single entry to `log.md` for this chapter.
   h. Commit: `ingest: <book-slug> - <chapter-slug>`.
   i. Stamp the manifest: append the chapter slug to `chapters_ingested`, increment `aku_count` and `taku_count`, record `last_commit: <sha>`.

3. After the last chapter completes: stamp the manifest `ingested: <today>`.

### Hard rules throughout (from CLAUDE.md — never violate)

- Only `raw/` paths in `sources[]`. Never another AKU.
- Three AKU classes (concept, method, claim). Do not discard content-bearing definitions or formulas.
- Spanish prose; canonical English technical terms (CLTV, CAC, ARPU, churn rate, payback, ROI, lifetime, unit economics, ...).
- Bidirectional relations (4 AKU pairs + TAKU pairs) AND body `## Relaciones` wikilinks (three-layer sync).
- TAKUs default to `status: draft`, `content_validation: llm-authored`, every `link_validation: llm-proposed`.
- Never set `human_certainty.status` away from `unvalidated`. Never set `link_validation: human-validated`. Never set TAKU `status: active`.
- `llm_confidence`: 0.50 baseline; +0.10 per independent corroborating source (cap 0.95); −0.30 on older claim when contradicted; null for tacit.
- Ask before writing when uncertain.

## Phase 5 — REPORT

Summarize to the user:
- Items discovered / converted / adopted / image-processed / ingested / skipped.
- AKU and TAKU counts per source (concept · method · claim breakdown).
- Any dedup pairs flagged for human decision (Phase 4 may have paused for one).
- Lint preview (will any of these trigger on next `/lint`?): isolated nodes, link inflation, missing `aku_class`, body-wikilink drift.
- Commits made (oneline).
- Manifest path: `_meta/pipeline-manifest.yml`.

## Resumability

If interrupted at any phase:
- Manifest holds the most recent progress markers per source.
- Re-running `/pipeline <same-folder>` re-runs discover, sees what's already done from the manifest + filesystem state, and resumes from the most-advanced incomplete phase.
- Each phase is idempotent: convert overwrites the temp/dest, adopt re-copies, image processing skips already-captioned images, ingest skips already-committed chapters.

## When to ask the user

- Before processing >3 sources (confirm scope).
- When a dedup candidate is similar but not clearly equivalent.
- When an image is genuinely ambiguous between informational and decorative.
- When MinerU output structure is unexpected and the script reports an error.
- When a chapter has no extractable atomic propositions (a pure-narrative chapter — confirm whether to skip or extract).
