# Index — AKU/TAKU Vault

Router and validation dashboard. Updated by `/ingest`, `/pipeline`, `/lint`, and validation actions.

## Counts

| Layer | Active | Draft | Deprecated | Validated-false / failing |
|---|---|---|---|---|
| AKU | 0 | — | 0 | 0 |
| TAKU | 0 | 0 | 0 | 0 |

_Last updated: 2026-06-03 (post-reset — empty vault, ready for first real ingest)_

## Pending validation queue

Items awaiting human review. Surface order: oldest first.

### AKUs to validate (in practice)
_(none yet — AKUs created from sources start `unvalidated`; populate `human_certainty` after real-world testing)_

### TAKUs awaiting activation
_(LLM-authored TAKUs sit in `status: draft` until the human reviews content + AKU links and sets `active`)_

### AKU links awaiting validation
_(every `llm-proposed` link surfaces here until promoted to `human-validated` or removed)_

### Dedup candidates
_(pairs of similar AKUs flagged by `/ingest` for merge/distinct decision)_

## Lint flags (latest run)

_No lint runs since reset. Run `/lint` to populate. Reports archived in `outputs/lint/` (gitignored)._

## Domain map

_(open taxonomy — populated as AKUs accumulate)_

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
