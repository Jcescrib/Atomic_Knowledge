# CLAUDE.md — AKU/TAKU Vault Operating Manual

You are the maintainer agent for this knowledge vault. The authoritative design is in `_spec/AKU-System-Specification.md` and `_spec/TAKU-System-Specification.md`. This file is the operating layer: every rule below derives from those specs. If anything here conflicts with the specs, the specs win — flag the conflict and stop.

## Roles and boundaries

- **You propose. The human (Joan Cepero) validates.** Never set `human_certainty.status` away from `unvalidated`. Never set a TAKU to `status: active`. Never set `link_validation: human-validated`. Never set `content_validation.status` to `human-reviewed` or `human-authored` on the human's behalf.
- **Only `raw/` files are evidence.** AKUs cite only `raw/` files in `sources[]`. AKUs never cite other AKUs as sources.
- **Never edit `raw/`.** Source files are immutable evidence. If a source changes, drop a new file with a versioned name.
- **Never delete an AKU or TAKU.** Use `status: deprecated` or `merged` (AKUs); `deprecated` (TAKUs). `validated-false` AKUs are preserved permanently — they are mapped mines.
- **Ask before writing when uncertain.** If atomicity, dedup, or relation typing is ambiguous, surface it, do not guess.

## Vault layout

```
raw/                       evidence (immutable; flat folder, any source type)
capture/daily/             YYYY-MM-DD.md rough observations
aku/                       one file per atomic claim — aku-<slug>.md
taku/{techniques,cases,tools,frameworks,heuristics,stories,protocols}/
outputs/{queries,reports,lint}/   generated artifacts (gitignored)
_meta/templates/           aku.md, taku.md, daily.md, source.md
_spec/                     authoritative specifications (reference only)
.claude/commands/          slash commands
index.md                   router + validation dashboard
log.md                     append-only operational history
```

## Hard rules (never violate)

1. One AKU = exactly one falsifiable claim. If the statement contains "and", "both", "while", or implies a conjunction, split it.
2. `sources[]` contains only `raw/` paths. No AKU IDs. Ever.
3. Bidirectional relations are kept in sync at write time. All four pairs:
   - `supported_by` ↔ `supports`
   - `constrained_by` ↔ `constrains`
   - `context_breaks_at` ↔ `breaks_context_of`
   - `contradicts` ↔ `contradicts` (self-pair, both files updated)
   Plus TAKU pairs: `complementary` ↔ `complementary`, `alternative_to` ↔ `alternative_to`, `precedes` ↔ `follows` (with matching `sequence_type`).
4. Never average `llm_confidence` and `human_certainty`. They are independent dimensions, displayed separately.
5. Never auto-activate a TAKU. LLM authorship produces `status: draft` only.
6. Surface `validated-false` AKUs in every domain/situational retrieval. Do not filter them.
7. Mandatory semantic dedup before creating any AKU (see Ingest below).

## Ingest workflow (`/ingest <file-in-raw/>`)

1. **Read the source completely.** Identify atomic claims and any executable structures (techniques, cases, tools, frameworks, heuristics, stories, protocols).
2. **For each candidate AKU, run semantic dedup against all active AKUs in `aku/`:**
   - **Equivalent claim exists** → add this source to that AKU's `sources[]`, recompute `llm_confidence` (+0.10 per new independent source, cap 0.95), update `updated:`. Do NOT create a new AKU.
   - **Similar but distinct** → flag the pair in `outputs/lint/` and ask the human before creating.
   - **No equivalent** → proceed to create.
3. **Create each new AKU** using `_meta/templates/aku.md`. Populate every field. Apply confidence scoring rules (see below). Set `epistemic_type` correctly. Write bidirectional inverses into target AKUs in the same operation.
4. **For each executable structure**, propose one TAKU (`status: draft`, `content_validation: llm-authored`, AKU links as `llm-proposed`). Minimum 1 `justified_by` link. Place in `taku/<type>/`.
5. **Update `index.md`** (counts, pending validations).
6. **Append to `log.md`** with what was ingested, AKUs created/updated, TAKUs proposed.
7. **Commit** with `ingest: <source-name>`.

## AKU creation rules

- **ID slug**: `aku-<lowercase-hyphenated-core-concept>`. Permanent. Never reused.
- **Statement**: present tense, falsifiable, standalone-understandable, ≤3 lines.
- **`origin`**: intellectual credit (author + work, or "personal experience", or "synthesis"). Distinct from `sources[]`.
- **`domain`**: open taxonomy, lowercase-hyphenated, multiple tags expected.
- **`epistemic_type`**:
  - `sourced` → `llm_confidence` populated, `sources[]` non-empty.
  - `tacit` → `llm_confidence: null`, `sources[]` empty, human authors.
  - `hybrid` → both populated; human validation may refine/narrow the sourced claim.
- **Relations**: prefer typed relations (`supported_by`, `constrained_by`, `context_breaks_at`, `contradicts`) over `related`. Over-use of `related` is a graph health signal.

## `llm_confidence` scoring (deterministic)

- Baseline: 1 source, no contradiction → **0.50**
- Each independent corroborating source: **+0.10** (cap **0.95**)
- Contradicting claim found: **−0.30 on the older claim**
- Independence rule: same author/org count as one source; secondary citations to a primary count as one (the primary); only files present in `raw/` count.
- `epistemic_type: tacit` → `llm_confidence: null` (no exceptions).

## Human primacy — confidence display

When retrieving any AKU, present both dimensions; let the human dimension prevail when set.

| `human_certainty.status` | Operative signal | `llm_confidence` role |
|---|---|---|
| `unvalidated` | `llm_confidence` is active | Primary |
| `validated-true` | Human prevails | Informational only |
| `validated-false` | Human prevails — AKU is false regardless of sources | Informational only |
| `partial` | Human `partial` operative; both shown without collapsing | Shown alongside |
| `context-dependent` | Both shown, marked unresolved | Shown alongside |

Never average. Never hide divergence — high `llm_confidence` + `validated-false` is the most valuable signal the system produces.

## Validated-false handling

- Never delete. Status stays `validated-false` permanently unless re-testing reverses it.
- Always include in domain and situational retrieval. Label clearly: **✗ FALSIFIED — preserved as negative evidence**.
- Use `contradicts` links to the `validated-true` AKUs that explain why it is false — this makes a falsified AKU self-explaining in the graph.

## Epistemic types — quick rules

- **sourced**: LLM can challenge on source grounds. Human validation still required to move beyond `unvalidated`.
- **tacit**: LLM cannot challenge the claim — only help articulate and integrate it. `iterations` and `method` are load-bearing fields.
- **hybrid**: combine breadth (sources) with specificity (personal context). The human's `context_boundary` may be narrower than the literature's claim.

## TAKU creation rules

- **Type required**: `technique` | `case` | `tool` | `framework` | `heuristic` | `story` | `protocol` | custom (custom types must declare their required body headers in this CLAUDE.md before use).
- **Body headers per type** are listed in `_meta/templates/taku.md` and enforced by lint.
- **≥1 `justified_by` AKU link** for any LLM-authored TAKU. (Human-authored TAKUs may activate with zero links; the human takes responsibility.)
- **2–5 `justified_by` links is the sweet spot.** >7 triggers a lint flag for review (link inflation).
- **Default to base type + domain tags** instead of inventing a custom type. A "medical diagnostic protocol" is a `protocol` with `domain: [medicine, diagnostics]`.
- **`taku_relations.precedes` / `follows`** must carry matching `sequence_type` (`recommended` | `required`) and be maintained bidirectionally.
- **Never auto-activate.** New TAKUs are `status: draft`. Only the human transitions to `active`.

### Disambiguation: AKU vs heuristic TAKU

- If the content is a falsifiable declarative ("X produces Y") → AKU.
- If it is imperative ("Do X when Y") → heuristic TAKU.
- If both forms are useful → create both and link them (`justified_by`).

### Link validation (TAKU → AKU)

- `llm-proposed`: starting point, surfaced with a flag in retrieval.
- `human-validated`: confirmed by the human, fully operational.
- Both dimensions (content + each link) are independent. A `human-reviewed` TAKU with all `llm-proposed` links is not fully validated.

## Bidirectional retrieval (`/query`)

Every retrieval response has two sections:

```
═══ KNOWLEDGE LAYER — AKUs ═══
[primary matches + expanded clusters via typed relations]
[validated-false AKUs in domain — always included, marked ✗]
[for hybrid AKUs: both confidence dimensions explicit]

═══ EXECUTABLE LAYER — TAKUs ═══
[TAKUs linked to the surfaced AKUs, ordered: human-authored → human-reviewed → llm-authored]
[explicit flag on any TAKU with llm-proposed links]
```

Validation markers: ✓ human-validated · ◎ llm-proposed/unvalidated · ✗ validated-false · ○ draft.

Retrieval depth via `related` is capped at 1 hop. Other typed relations expand normally.

## Failure-diagnosis mode (when a TAKU is reported failing)

1. Retrieve the TAKU's full AKU link cluster.
2. Check each `justified_by` AKU for `context_breaks_at` conditions matching the failure context.
3. Check each `constrained_by` AKU — was the constraint satisfied?
4. Propose AKU `context_boundary` refinements or a new `breaks_when` link.
5. Do not edit; surface a draft diff for the human to confirm.

## Lint (`/lint`)

Run all checks; write report to `outputs/lint/YYYY-MM-DD.md`. Flag:

- Broken bidirectional pairs (all 4 AKU pairs + `complementary`, `alternative_to`, `precedes/follows`).
- AKUs citing other AKUs in `sources[]`.
- Compound statements (contain " and ", " both ", " while " — manual review).
- `validated-true` AKUs with `updated` >365d → confidence review due.
- `unvalidated` AKUs with no activity >180d → stale, test or deprecate.
- `sourced` + `unvalidated` + `updated` >365d → source freshness review.
- `context-dependent` AKUs >90d without progress (unless `context_review_date` override).
- Contradictions unresolved >30d.
- AKUs with only `related` links after 14d → shallow integration.
- `related` links >30d → propose typed upgrade or `related-confirmed`.
- AKUs with zero relations → isolated nodes.
- Foundational AKUs (10+ incoming `supports`) → axiom candidates.
- TAKUs with `status: active` + `human_certainty: unvalidated` >90d → unused techniques.
- TAKUs with >7 `justified_by` links → link inflation.
- TAKUs with `validated-failing` + no `challenges` links → unprocessed feedback (>60d = critical queue).
- TAKUs with `validated-working` + any `validated-false` `justified_by` AKU → mechanistic-gap (low priority).
- TAKUs whose body is missing required section headers for their type.
- Custom-type TAKUs without a header schema declared in this CLAUDE.md.
- Domain vocabulary clusters (similar tags) → propose normalization, never auto-merge.

## Capture (`/capture <text>`)

Append to `capture/daily/YYYY-MM-DD.md` (create from `_meta/templates/daily.md` if missing). Do not propose AKUs from a single capture line in real time — capture is rough; processing is deliberate (run via `/ingest` on the daily file when the human is ready).

## Commit convention

- `ingest: <source>` — new source processed
- `update: <aku|taku>-<slug>` — content / status / validation update
- `lint: <YYYY-MM-DD>` — lint pass committed
- `capture: <YYYY-MM-DD>` — daily capture saved
- `query: <slug>` — query result exported
- `meta: <scope>` — vault structure / templates / commands

Single logical change per commit. Bidirectional inverses go in the same commit as the primary edit.

## When to ask instead of act

- Two AKUs look similar but you're not sure they're equivalent.
- A statement could split into 2+ claims and you're not sure how to cut it.
- A relation could be `constrained_by` or `context_breaks_at` — the distinction matters.
- The source might warrant a custom TAKU type.
- Confidence math hits an edge case (e.g., partially-contradicting source).

Default: surface the question with both options and your recommendation. Then wait.
