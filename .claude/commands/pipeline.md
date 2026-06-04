---
description: End-to-end ingestion of a folder of PDFs/markdowns via MinerU + vision + section-based AKU/TAKU extraction with resumability — autonomous by default
argument-hint: <absolute-path-to-source-folder>
---

Run the full ingestion pipeline as defined in `CLAUDE.md` § Pipeline. Source folder: `$ARGUMENTS`.

If no argument was provided, ask the user for the folder path. The folder may contain PDFs (converted via MinerU), EPUBs (converted via `scripts/epub_to_md.py` — ebooklib + BeautifulSoup), and/or pre-converted markdowns (adopted directly).

**Important**: do NOT run discover on the vault root. The script will return the vault's own infrastructure files if you do. Only run discover on EXTERNAL folders.

## DEFAULT MODE — AUTONOMOUS

The pipeline runs **autonomously**: discover → convert/adopt → image-classify → ingest → commit, **per PDF, in sequence, without asking for approval between PDFs**. Process the whole folder end-to-end and produce **ONE consolidated report at the end**.

**Aggressive dedup**: at every PDF's ingest step, compare each candidate AKU against the **full existing graph** (every active AKU in `aku/`, including those from earlier PDFs in this same run). When dedup matches:
- Add the new source path to the existing AKU's `sources[]` (idempotent).
- Recompute `llm_confidence` per CLAUDE.md (+0.10 per new independent source, cap 0.95).
- Bump `updated` to today.
- Where the new source adds new content (extra context, examples, refinements), enrich the statement on the existing AKU; do NOT create a duplicate.
- Wire any new `related` / `supports` / `constrains` cross-source links surfacing from the new material.

**Stop and ask the user ONLY when the work genuinely requires their decision**, namely:
- A semantic dedup candidate is too close to call (could merge, could stay separate).
- MinerU fails repeatedly on a specific PDF and pipeline cannot recover.
- A concept the source treats as definitional contradicts an existing `validated-true` AKU in the graph (would force `contradicts` or `breaks_context_of` against human-validated content).
- Custom TAKU type warranted but no schema declared in CLAUDE.md.
- An image is genuinely ambiguous between informational and decorative AND its content materially affects extractable AKUs.

Anything else — commit decisions, image classification of ordinary cases, claim vs concept-AKU choice within the 3-class rule, slug normalisation, etc. — is decided autonomously and reported (not pre-approved). The user reviews the consolidated report at the end and can redirect on the next turn.

Execute the five phases below in order. Surface progress at most as one-line updates between PDFs ("PDF 3/7 done: 8 AKUs, 1 TAKU drafted, 2 image blockquotes"); save the deep narrative for the final report.

## Phase 1 — DISCOVER

1. Run `scripts/pipeline.sh discover "$FOLDER"` via Bash. Parse the output: three sections (`## PDFs`, `## EPUBs`, `## Pre-converted markdowns (candidate sources)`).
2. Read `_meta/pipeline-manifest.yml` (create it from `sources: []` if it does not exist).
3. For each discovered item, look up its likely slug (use `scripts/pipeline.sh slug "<basename>"`) in the manifest. Skip any item whose entry has `ingested: <date>` set.
4. Produce a discovery summary in the consolidated final report (not as a separate user-facing turn):
   - N PDFs found, M to convert (others skipped: list IDs)
   - E EPUBs found, F to convert (others skipped: list IDs)
   - K markdowns found, J to adopt (others skipped: list IDs)
   - Total work units: M + F + J
5. If total work is 0, stop and inform the user.
6. If total work is non-zero, **proceed autonomously** through phases 2–4 for every source in sequence. Do NOT ask for batch confirmation — autonomous mode is the default per user preference.

## Phase 2 — CONVERT / ADOPT

**Hard rule reminder (from CLAUDE.md #9 and #10)**: source binaries (PDF and EPUB) stay at their origin path. They are NEVER copied, moved, or modified during this phase — the converter reads from the origin and only the produced markdown + images land in `raw/<slug>/`. Always quote paths with spaces or accents.

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

For each EPUB queued to convert:
- Run `scripts/pipeline.sh convert-epub "<absolute-epub-path>"` (quotes mandatory). The script invokes `scripts/epub_to_md.py` (ebooklib reads spine order, BeautifulSoup converts each chapter's HTML to clean markdown) and prints the destination `raw/<slug>/`. The EPUB stays read-only at its origin path, exactly like a PDF.
- Manifest entry: same shape, `converter: epub`. `original:` records the EPUB's origin path.

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

## When to ask the user (rare — autonomous mode is the default)

Only stop and ask if one of these is true; otherwise decide and report in the final consolidated report.

- A semantic dedup candidate is too close to call (could merge, could stay separate, real ambiguity).
- MinerU fails repeatedly on a specific PDF and the script's diagnostics cannot recover.
- A new source's content contradicts an existing `validated-true` (human-validated) AKU and would force a `contradicts` or `breaks_context_of` link against human-validated content.
- A custom TAKU type is genuinely warranted but no schema is declared in CLAUDE.md.
- An image is genuinely ambiguous AND its content materially affects extractable AKUs.

Image classification ordinary cases (icons, logos, book covers, slide template variants, fragmented diagram pieces), claim vs concept-AKU choice within the 3-class rule, slug normalisation, sequencing of related TAKUs, and standard dedup decisions are all autonomous — report in the final consolidated report rather than pausing per-PDF.
