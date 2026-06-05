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
raw/<curso-o-libro>/<slug>/<slug>.md   converted markdown of each source (canonical
raw/<curso-o-libro>/<slug>/images/     text the vault works with) + paired figures.
                           Sources are organised by origin:
                             raw/cursos/power-mba/<slug>/   — Power MBA course modules
                             raw/libros/<autor>/<slug>/      — external books (e.g. libros/kolenda/)
                           A bare raw/<slug>/ (root) is the generic fallback for
                           sources of unknown origin.
                           PDFs and other source binaries NEVER live here.
                           Original PDFs stay at their source location (G:\, OneDrive, etc.)
                           and are read-only — see hard rule #9.
capture/daily/             YYYY-MM-DD.md rough observations
aku/                       one file per atomic claim — aku-<slug>.md
taku/{techniques,cases,tools,frameworks,heuristics,stories,protocols,reference}/
outputs/{queries,reports,lint}/   generated artifacts (gitignored)
_meta/templates/           aku.md, taku.md, daily.md, source.md
_spec/                     authoritative specifications (reference only)
.claude/commands/          slash commands
scripts/                   shell scripts called by slash commands (pipeline.sh)
_meta/pipeline-manifest.yml  per-source state for /pipeline resumability
.claude/commands/audit-graph.md  /audit-graph — global graph integration audit + origin paths
index.md                   router + validation dashboard
log.md                     append-only operational history
```

## Hard rules (never violate)

1. One AKU = exactly one falsifiable proposition (claim, method, or concept — see § AKU classes). If the statement chains two independent propositions via "and"/"both"/"while", split it. A concept statement with includes/excludes/implies clauses is NOT a conjunction — it is a single proposition with structured content.
2. `sources[]` contains only converted-markdown paths inside the vault — under the origin-organised tree, i.e. `raw/cursos/power-mba/<slug>/<slug>.md`, `raw/libros/<autor>/<slug>/<slug>.md`, or a bare `raw/<slug>/<slug>.md` fallback. Never PDFs, never other binaries, never another AKU's ID. The original PDF's location is recorded only in `_meta/pipeline-manifest.yml` (the `original:` field), not in `sources[]`.
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
8. Body `## Relaciones` section is mandatory and must mirror non-empty frontmatter relations exactly. Three layers stay in sync on every edit: frontmatter inverse on the other file + body wikilinks on this file + body wikilinks on the other file.
9. **Source binaries (PDF, EPUB) are read-only at their origin path.** Never copied, moved, modified, or stored in the vault. The vault works exclusively with the markdown produced by the converter (MinerU for PDF in `raw/<slug>/<slug>.md`, `scripts/epub_to_md.py` for EPUB) plus paired images. The original PDFs/EPUBs live wherever they came from (G:\ Drive mounts, OneDrive, local folders, ...) and remain untouched. Re-conversion always reads from the origin path.
10. **Always quote paths with spaces or accents** when passing them to MinerU, shell commands, or any external tool. Use double quotes: `mineru -p "G:\Mi unidad\Formación\foo bar.pdf" -o "$tmp"`. This rule prevents silent argument splitting on Windows + git-bash + UTF-8 paths.

## Pipeline (`/pipeline <folder>`)

End-to-end ingestion of an external folder of PDFs and/or pre-converted markdowns, with resumability. Use `/pipeline` for batches and book-length sources; use `/ingest` for a single source already in `raw/`. Run `/pipeline` only against EXTERNAL folders, never the vault itself.

**Phases**:

1. **DISCOVER** — `scripts/pipeline.sh discover <folder>` lists every `.pdf`, every `.epub` (recursive) and every `.md` candidate. Cross-reference `_meta/pipeline-manifest.yml`; items with `ingested: <date>` are skipped.
2. **CONVERT / ADOPT** — Supported source formats: `.pdf` (MinerU), `.epub` (ebooklib + BeautifulSoup), and pre-converted `.md` (adopted as-is). For each PDF: `scripts/pipeline.sh convert "<pdf>"` runs MinerU against the file at its **origin path** (G:\, OneDrive, etc. — the PDF is NEVER copied or moved into the vault), then moves only the produced `.md` + `images/` to the origin-organised destination (`scripts/pipeline.sh` routes by source path: `…\Apuntes Power MBA\…` → `raw/cursos/power-mba/<slug>/`, `…nickkolenda…` → `raw/libros/kolenda/<slug>/`, otherwise `raw/<slug>/`), rewrites image refs to flat `images/<filename>`, and discards all MinerU scaffolding (`*middle.json`, `*model.json`, `*content_list*.json`, `*_layout.pdf`, `*_span.pdf`, `*_origin.pdf`). For each EPUB: `scripts/pipeline.sh convert-epub "<epub>"` invokes `scripts/epub_to_md.py` (ebooklib reads spine order, BeautifulSoup converts each chapter's HTML to clean markdown), writing the `.md` + flat `images/<filename>` into the same origin-organised destination — the EPUB stays read-only at its origin path, exactly like a PDF. The original PDF/EPUB location is recorded in the manifest's `original:` field. For each pre-converted markdown: `scripts/pipeline.sh adopt "<md>"` copies the .md + any adjacent `images/` folder into the same origin-organised destination. **Always quote paths with spaces or accents.**
3. **PROCESS IMAGES AND TABLES** — Tables (inline `<table>` HTML from MinerU) are read directly during ingest. Images are classified per reference:
   - **Informational** (diagram, chart, framework figure, schema, data viz, structured screenshot) → vision-analyze, insert a `> **Figura**: <descripción precisa en español>` blockquote immediately after the image reference. Maximum fidelity — the figure's knowledge must be extractable from the description alone.
   - **Decorative** (cover, portrait, ornament, divider, brand mark) → leave the reference, extract nothing.
   - Idempotent: existing `> **Figura**:` captions are detected and skipped.
4. **INGEST** — Short markdowns (≤500 lines, no H1 chapter structure): one pass via § Ingest workflow, one commit. Long markdowns/books: parse H1 (fall back to H2) into chapters; per chapter, run the full ingest workflow with dedup against the growing graph (including AKUs from earlier chapters of the same book); write AKUs and TAKUs with frontmatter + body `## Relaciones` wikilinks (three-layer sync per § Body wikilinks); commit per chapter as `ingest: <book-slug> - <chapter-slug>`.
5. **REPORT** — Counts (discovered/converted/adopted/image-processed/ingested/skipped), AKU/TAKU breakdown by class, dedup decisions pending, lint preview, commits made.

**Manifest** — `_meta/pipeline-manifest.yml` tracks per-source state across phases. Re-running `/pipeline` resumes from the most recent incomplete phase. Each phase is idempotent.

**Hard rules during pipeline** — All ingest rules apply unchanged. The pipeline command does not relax any rule; it batches the work.

## Ingest workflow (`/ingest <file-in-raw/>`)

For batch processing of an external folder of PDFs/markdowns (including MinerU conversion and image vision-classification), use `/pipeline <folder>` above. The `/ingest` command below operates on one source already present in `raw/`.

> ### ⚠ Salvaguarda 1 — Paso de COBERTURA obligatorio (antes de crear ningún AKU, por capítulo)
>
> Antes de crear AKUs en cada capítulo, **enumera primero TODOS los items con identidad propia del capítulo** (concepts, methods, claims) con su **nombre y su clase**, y **muestra el recuento** (p. ej. "Capítulo X: 18 items — 9 concept, 3 method, 6 claim"). **Solo entonces** crea AKUs — **uno por cada item enumerado**, deduplicando cada uno contra el grafo. Sin enumeración previa **no hay garantía de cobertura**: extraer "sobre la marcha" produce omisiones sistemáticas (sub-tipos plegados, claims normativos descartados, fórmulas saltadas). La enumeración es el *denominador* contra el que se mide la creación. Verificar el grafo (simetría, body-drift, componentes) comprueba *consistencia*, **nunca cobertura** — son chequeos distintos y ambos son obligatorios.

> ### ⚠ Salvaguarda 2 — Granularidad MÁXIMA siempre (invariante, no negociable)
>
> La granularidad del vault es **máxima por defecto y en todo momento**. **Si existe identidad propia, existe AKU propio.**
> - **Nunca plegar sub-tipos en un paraguas** si tienen nombre propio, mecanismo diferenciado o condiciones de aplicación distintas (cada componente de un framework, cada tipo de garantía/oferta/escasez, cada método individual → su propio AKU, enlazado al paraguas con `supported_by`/`related`).
> - **Nunca omitir un claim normativo del autor** ("siempre haz X", "nunca hagas Y", "X produce mejor Y que Z") aunque parezca obvio → es un claim-AKU propio.
> - **Nunca omitir una fórmula o cálculo** → es un method-AKU propio.
> - **Mismo nombre, definición/matiz/condiciones distintas ≠ dedup** → AKU nuevo con `related` (no fusionar). Confundir adyacencia conceptual con equivalencia es un error de dedup.
>
> Esta regla **no se negocia ni se ajusta por eficiencia, longitud del informe ni volumen** — es invariante. Ante la duda, **crea**.

1. **Read the source completely.** Identify atomic propositions across all three AKU classes — claims, methods, and concepts (see § AKU classes) — and any executable structures (techniques, cases, tools, frameworks, heuristics, stories, protocols). Do not discard content-bearing definitions or formulas as "merely definitional." **Then run the COVERAGE step (Salvaguarda 1): enumerate every identity-bearing item per chapter with name + class and show the count, before creating anything.**
2. **For each candidate AKU, run semantic dedup against all active AKUs in `aku/`:**
   - **Equivalent claim exists** → add this source to that AKU's `sources[]`, recompute `llm_confidence` (+0.10 per new independent source, cap 0.95), update `updated:`. Do NOT create a new AKU.
   - **Similar but distinct** → flag the pair in `outputs/lint/` and ask the human before creating.
   - **No equivalent** → proceed to create.
3. **Create each new AKU** using `_meta/templates/aku.md`. Populate every field. Apply confidence scoring rules (see below). Set `epistemic_type` correctly. Write bidirectional inverses into target AKUs in the same operation.
4. **For each executable structure**, propose one TAKU (`status: draft`, `content_validation: llm-authored`, AKU links as `llm-proposed`). Minimum 1 `justified_by` link. Place in `taku/<type>/`.
5. **Update `index.md`** (counts, pending validations).
6. **Append to `log.md`** with what was ingested, AKUs created/updated, TAKUs proposed.
7. **Commit** with `ingest: <source-name>`.

## Integración del grafo

El grafo se integra activamente. Ningún concepto nuevo queda huérfano por defecto. Se aplica en dos momentos.

### En cada ingest — paso INTEGRATE (5.5) tras la deduplicación

Después de crear los AKUs nuevos con sus inversos bidireccionales (paso 5 del Ingest workflow), añadir el paso **5.5 INTEGRATE**: para cada AKU nuevo, evaluar con qué AKUs **existentes del grafo** debería conectarse — no solo deduplicar contra ellos. Para cada AKU existente, buscar:

- **Mención textual**: el `statement` del nuevo AKU menciona literalmente un término que es el concepto central del AKU existente, o viceversa.
- **Adyacencia conceptual directa**: ambos describen el mismo objeto desde ángulos distintos, o uno es composición/instancia del otro.

Wire las conexiones encontradas según la regla de los 3 niveles (abajo). Documentar las wires en el commit del ingest (no en una pasada posterior).

### Auditoría global (`/audit-graph`)

Operación periódica que escanea todo el grafo y propone puentes. Lanzada por el usuario explícitamente, no automática. Detecta:
- Componentes conectados (debe ser 1 solo).
- Nodos huérfanos (degree 0) — error.
- Nodos sub-conectados (degree 1-2) — candidatos a wire-up.
- Clusters temáticos aislados (>3 AKUs sin enlace externo).

Genera propuestas clasificadas por los 3 niveles de rigor.

### Regla de los 3 niveles de rigor

Toda conexión candidata se clasifica en uno de tres niveles, de más a menos peso epistémico:

**(a) Anclada en el texto de las fuentes** — el statement de un AKU menciona literalmente el concepto del otro (e.g., `canal-indirecto` dice «plataforma»; `ecosistema-alianzas` dice «recursos clave»). El agente **aplica directamente** sin pedir aprobación. Reportable, no preguntable.

**(b) Conexión conceptual directa** — sin mención literal, los dos AKUs describen el mismo objeto desde ángulos distintos o uno es composición/instancia del otro (e.g., `modelo-lineal ↔ bmc`: un modelo lineal ES un modelo de negocio). El agente **propone con razonamiento; el humano aprueba antes de escribir**.

**(c) Conocimiento práctico del humano** (siempre `epistemic_type: tacit` o `hybrid`, **nunca `sourced`**) — el humano aporta un claim o relación que viene de su experiencia, no del material de las fuentes. El agente **nunca lo crea unilateralmente**; solo lo soporta cuando el humano lo propone.

### Quién decide qué

- **Nivel (a)** → agente aplica. Lo lista en el reporte; no abre ronda de aprobación.
- **Niveles (b) y (c)** → agente propone; humano aprueba antes de escribir.
- **Rigor, no cantidad**: si dudas entre conectar o no, NO conectes y márcalo para revisión humana. Mejor un grafo parcialmente desconectado pero bien curado que sobre-conectado con puentes falsos.

### Distinción crítica — conexión conceptual real ≠ coincidencia empírica

Si la conexión aplica a «cualquier negocio» o «muchas empresas», es coincidencia empírica, no conceptual. Skip.

Ejemplo del módulo 2.3:
- ✓ `marketplace ↔ canal-indirecto`: definicional (canal-indirecto incluye «plataforma» como intermediario — anclado en texto).
- ✗ `marketplace ↔ CLTV-CAC`: empírico (marketplaces aplican unit economics, pero TODA empresa los aplica — conexión genérica que no aporta).

## AKU creation rules

- **ID slug**: `aku-<lowercase-hyphenated-core-concept>`. Permanent. Never reused.
- **Statement**: present tense, falsifiable, standalone-understandable, ≤3 lines.
- **`origin`**: intellectual credit (author + work, or "personal experience", or "synthesis"). Distinct from `sources[]`.
- **`domain`**: open taxonomy, lowercase-hyphenated, multiple tags expected.
- **`domain` source-tag (mandatory)**: every `sourced`/`hybrid` AKU carries **exactly one canonical source-tag** in `domain` identifying the origin corpus, derived from the `raw/` path of its source. The vocabulary is **closed** and mirrors `raw_subdir_for` in `scripts/pipeline.sh` — never invent a variant (`thepowermba`, `alex-hormozi`, `nick-kolenda` are all wrong):

  | `raw/` path prefix | canonical source-tag |
  |---|---|
  | `raw/cursos/power-mba/…` | `power-mba` |
  | `raw/libros/hormozi/…` | `hormozi` |
  | `raw/libros/jocko/…` | `jocko` |
  | `raw/libros/kolenda/…` | `kolenda` |
  | `raw/<slug>/…` (root fallback, unknown origin) | *(no source-tag — leave it off rather than guess)* |

  The source-tag is the only `domain` entry with a fixed vocabulary; all other domain tags remain free taxonomy. A `tacit` AKU (no `sources[]`) has no source-tag. When a new corpus is first ingested, fix its tag here **before** writing the first AKU, then add the matching `raw_subdir_for` case if missing.
- **`epistemic_type`**:
  - `sourced` → `llm_confidence` populated, `sources[]` non-empty.
  - `tacit` → `llm_confidence: null`, `sources[]` empty, human authors.
  - `hybrid` → both populated; human validation may refine/narrow the sourced claim.
- **Relations**: prefer typed relations (`supported_by`, `constrained_by`, `context_breaks_at`, `contradicts`) over `related`. Over-use of `related` is a graph health signal.
- **Nunca omitir un AKU por escasez de información en la fuente actual.** Si un concepto tiene identidad propia (nombre propio, rol diferenciado, mecanismo específico), se crea con lo disponible ahora. La riqueza llega con fuentes futuras — el sistema está diseñado para enriquecerse con nuevas fuentes, no para esperar a tener información completa. Omitir un AKU hoy es impedir que se enriquezca mañana.

## AKU classes — concept, method, claim

AKUs come in three first-class types. All are retrievable. None is filtered out as "merely definitional."

- **`concept` AKU** — definition of a contentful concept. Statement pattern: *"W es [definition]; incluye [X]; excluye [Y]; implica [Z]."* Falsifiable by **adequacy** (does the definition capture what matters?), **implications** (the entailed consequences can be wrong), and **boundary** (the line it draws can be wrong in a context).
- **`method` AKU** — procedural recipe. Statement pattern: *"En [conditions], Z se computa como [formula]."* Falsifiable by application (wrong formula yields wrong number) and by domain mismatch.
- **`claim` AKU** — empirical or normative proposition. Statement pattern: *"X produce mejor resultado que Y bajo [conditions]."* Falsifiable in the classic Popperian sense.

Exclude only **hollow nominal vocabulary** — terms with no implications, no formula, and no boundary conditions.

**Required frontmatter field**: `aku_class: concept | method | claim` (placed right after `id`). Lint flags any AKU without this field.

**Relation patterns by class** (bidirectional inverses still mandatory):
- concept ↔ method: `supports` / `supported_by` (the concept underlies the formula).
- claim → concept (when the claim refines the correct use of the concept): `constrains` / `constrained_by`.
- method ↔ method in mutually exclusive contexts: `context_breaks_at` / `breaks_context_of` on both sides (symmetric pair).
- concept ↔ concept (paired metrics, no causal/logical link): `related` (use sparingly — prefer a typed relation when one fits).

## Language conventions

- AKU statements and TAKU body prose are written in **Spanish**.
- **Technical terms stay in their canonical English form**: CLTV, CAC, ARPU, churn rate, payback, ROI, lifetime, unit economics, input/output, and any acronym or term-of-art that is widely used untranslated in business/tech Spanish. When in doubt, keep the English form.
- **Field names, IDs, slugs, and class labels stay in English**: `aku_class: concept`, `human_certainty.status: validated-true`, `id: aku-<english-slug>`, `taku_type: framework`, etc.
- Source citations and `origin` strings match the source's published language.
- This rule applies to all future ingests. Lint does not enforce it mechanically; it is a convention for retrieval and dedup consistency.

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

#### Custom type declarations

- **`reference`** — a curated pointer to external resources (bibliography, link list, resource index) that grounds future ingests rather than executing a procedure. Required body headers:
  - `## Descripción`
  - `## Recursos`
  - `## Cómo usar esta referencia`
  - `## Relaciones`

### Disambiguation: AKU vs heuristic TAKU

- If the content is a falsifiable declarative ("X produces Y") → AKU.
- If it is imperative ("Do X when Y") → heuristic TAKU.
- If both forms are useful → create both and link them (`justified_by`).
- If it is a curated pointer to external resources (e.g., a list of recommended books by domain) → `reference` TAKU, not a `concept` AKU.

### Link validation (TAKU → AKU)

- `llm-proposed`: starting point, surfaced with a flag in retrieval.
- `human-validated`: confirmed by the human, fully operational.
- Both dimensions (content + each link) are independent. A `human-reviewed` TAKU with all `llm-proposed` links is not fully validated.

## Body wikilinks — Obsidian graph visibility

Every AKU and TAKU body must include a `## Relaciones` section that mirrors all non-empty frontmatter relations as `[[wikilink]]` references. The frontmatter is the canonical, machine-readable source of truth; the body section is the Obsidian-graph-visible projection — Obsidian only renders graph edges from `[[wikilink]]` syntax, not from YAML.

**Format**:
- One line per non-empty relation field.
- `**<field>** <arrow> [[target-1]] · [[target-2]] · ...`
- Field names stay in English; arrows: `→` outgoing, `←` incoming, `↔` symmetric.
- Omit empty relations entirely — no placeholder lines.
- For AKUs: `## Relaciones` is the only mandatory body content.
- For TAKUs: `## Relaciones` is the **last** body section, after type-specific content.

**Arrow convention**:
- AKU outgoing (`supports`, `constrains`, `context_breaks_at`, `breaks_context_of`): `→`
- AKU incoming (`supported_by`, `constrained_by`): `←`
- AKU symmetric (`contradicts`, `related`): `↔`
- TAKU AKU-link incoming (`justified_by`, `constrained_by`): `←`
- TAKU AKU-link outgoing (`breaks_when`, `illustrates`, `challenges`): `→`
- TAKU sibling symmetric (`complementary`, `alternative_to`): `↔`
- TAKU sequence: `precedes` →, `follows` ←

**Three-layer sync** — every relation edit propagates to three places:
1. Frontmatter inverse on the OTHER file.
2. Body wikilink on THIS file.
3. Body wikilink on the OTHER file.

Lint verifies all three.

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
- AKUs missing the `aku_class` field → unclassified, fix at next pass.
- `sourced`/`hybrid` AKU whose `domain` lacks the canonical source-tag expected from its `sources[]` path (per § AKU creation rules table) → missing source-tag, fix at next pass. Also flag the inverse: a `tacit` AKU (or a source whose path matches no known prefix) carrying a known source-tag → spurious source-tag.
- Body `## Relaciones` section missing on any active AKU or TAKU → structural error.
- Body wikilinks don't match frontmatter relations (missing, extra, or mistyped slug) → structural error.
- Pipeline manifest references a source with no corresponding `raw/<slug>/` folder → broken manifest entry.
- Componentes conectados del grafo > 1 → fragmentación. Lanzar `/audit-graph` para detectar islas y proponer puentes.
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
