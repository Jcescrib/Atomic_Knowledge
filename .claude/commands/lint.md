---
description: Run the full lint suite over the AKU/TAKU graph and write a report
---

Execute all lint checks defined in `CLAUDE.md` § Lint. Read every file in `aku/` and `taku/`. Do not modify any AKU or TAKU file during this pass — lint is read-only diagnosis. Repairs are proposed, not applied.

Today's date is in the conversation context (`currentDate`). Use it for the report filename.

Run these checks and collect findings:

**Structural integrity**
- Bidirectional pair breakage: scan all 4 AKU pairs (`supported_by`/`supports`, `constrained_by`/`constrains`, `context_breaks_at`/`breaks_context_of`, `contradicts` self-pair) and all TAKU pairs (`complementary`, `alternative_to`, `precedes`/`follows` with `sequence_type` match). Report each missing inverse with both file paths.
- AKUs citing AKU IDs in `sources[]` (must be raw/ paths only).
- TAKU bodies missing required section headers for their declared `taku_type`.
- Custom-type TAKUs without a schema declared in `CLAUDE.md`.
- AKUs with self-relations.

**Atomicity / claim quality**
- AKU statements containing ` and `, ` both `, ` while ` — flag as possible compound claims.
- AKUs with zero relations — isolated nodes.
- AKUs with only `related` links and no typed structural relations after 14 days of `created`.
- `related` links present on AKUs older than 30 days — propose upgrade to typed relation or mark `related-confirmed`.

**Decay / freshness**
- `human_certainty.status: validated-true` with `updated` >365 days → confidence review due.
- `human_certainty.status: unvalidated` with no activity >180 days → stale, test or deprecate.
- `epistemic_type: sourced` + `unvalidated` + `updated` >365 days → source freshness review.
- `human_certainty.status: context-dependent` >90 days without progress (respect `context_review_date` if set).
- TAKUs with `human_certainty.status: validated-working` + `validation_date` >365 days → re-confirmation due.

**Contradictions and tensions**
- AKUs in `contradicts` relationships unresolved >30 days.
- TAKUs with `validated-working` and one or more `justified_by` AKUs with `validated-false` → mechanistic-gap (low priority).
- TAKUs with `human_certainty.status: validated-failing` and no `challenges` AKU links → unprocessed feedback. >60 days = critical queue.

**TAKU health**
- Active TAKUs with `human_certainty.status: unvalidated` and `created` >90 days → unused techniques.
- TAKUs with more than 7 `justified_by` links → link inflation review.
- TAKUs with zero AKU links and `content_validation.status: llm-authored` → cannot be activated.

**Graph emergent structure**
- AKUs with 10+ incoming `supports` links → axiom candidates (informational, not an error).

**Domain vocabulary**
- Cluster all `domain` tags across the vault; surface similar-looking pairs (`sales`/`selling`, `decision-making`/`decisions`) and propose normalizations. Never auto-merge.

**Output**
Write the report to `outputs/lint/YYYY-MM-DD.md` (overwrite if same day). Structure:

```
# Lint report — YYYY-MM-DD

## Summary
- N AKUs scanned, N TAKUs scanned
- N findings: X errors, Y warnings, Z informational

## Errors (must fix)
[broken bidirectionals, sources[] violations, missing required body headers, custom-type schema gaps]

## Warnings (review)
[decay flags, contradictions, link inflation, mechanistic gaps, atomicity suspicions]

## Informational
[axiom candidates, domain vocabulary clusters, foundational AKUs]

## Validation queue
[pending dedup pairs, llm-proposed link counts, draft TAKUs awaiting activation]
```

Update the "Lint flags (latest run)" section of `index.md` with the top-line counts and a link to the report.

Append a single line to `log.md`: `## YYYY-MM-DD — lint  N errors / N warnings / N info`.

Commit with `lint: YYYY-MM-DD`. Do not commit any AKU/TAKU repairs — those are separate `update:` commits the human authorizes.
