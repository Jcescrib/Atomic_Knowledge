---
description: Process a source file from raw/ into AKUs and proposed TAKUs
argument-hint: <path-in-raw/> (optional — if omitted, prompt for which raw/ file)
---

You are running the `/ingest` workflow defined in `CLAUDE.md`. Source: `$ARGUMENTS`.

If no argument was provided, list the contents of `raw/`, ask the user which file to ingest, then proceed.

Execute the ingest workflow exactly as specified in `CLAUDE.md` § Ingest workflow:

1. **Read the source file completely.** Note its `origin` (author + work).
2. **Extract candidate atomic claims.** Each must pass the atomicity test: independently falsifiable, present tense, one claim only.
3. **For each candidate, run semantic deduplication against ALL active AKUs in `aku/`.** Read the existing AKU statements — not just filenames. Three outcomes per candidate:
   - **Equivalent exists** → append source to that AKU's `sources[]`, recompute `llm_confidence` (+0.10 per new independent source, cap 0.95), bump `updated`. Do NOT create a new file.
   - **Similar but distinct** → STOP. Present the pair to the human with a comparison and ask: merge, keep distinct, or refine.
   - **No equivalent** → proceed to create.
4. **Create each new AKU** from `_meta/templates/aku.md`. Populate every field. Apply the deterministic `llm_confidence` rule. Choose `epistemic_type` correctly (sourced for written, hybrid only if you have evidence of prior personal validation, tacit if no source — should not arise from `/ingest`).
5. **Wire bidirectional relations in the same pass.** For every `supported_by`, `constrained_by`, `context_breaks_at`, or `contradicts` you add, edit the target AKU file to add the inverse. All four pairs.
6. **Identify executable structures** in the source (techniques, cases, tools, frameworks, heuristics, stories, protocols). For each, draft ONE TAKU:
   - Use the type-specific body headers from `_meta/templates/taku.md`.
   - Place in `taku/<type>/`.
   - `status: draft`, `content_validation.status: llm-authored`, every AKU link `link_validation: llm-proposed`.
   - Minimum 1 `justified_by` link. Aim for 2–5.
   - Do NOT activate. Do NOT set human_certainty status.
7. **Update `index.md`**: counts table, pending validation queue (new AKUs are unvalidated; new TAKUs are draft).
8. **Append to `log.md`** with: source name, candidates considered, AKUs created (list IDs), AKUs updated via dedup (list IDs), TAKUs proposed (list IDs + types), any dedup pairs flagged for human review.
9. **Commit** with message `ingest: <source-name>` covering all changes from this ingest.

Hard rules to enforce mid-flight:
- Only `raw/` paths in `sources[]`. Never another AKU.
- Never `human_certainty.status` other than `unvalidated` for newly created AKUs.
- Never set TAKU `status: active`.
- Never set any `link_validation: human-validated` — the human does that.
- If atomicity is ambiguous (statement contains "and"/"both"/"while"/conjunction), stop and ask how to split.

Final output to the user: a summary of what was created, what dedup decisions you made, what is pending human review.
