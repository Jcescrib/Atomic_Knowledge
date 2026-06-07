# Auditoría del `CLAUDE.md` — modelo de grafo, reglas de enlazado y evaluación crítica

**Fecha:** 2026-06-07
**Alcance:** revisión de solo lectura del manual operativo `CLAUDE.md` (capa operativa sobre `_spec/AKU-System-Specification.md` y `_spec/TAKU-System-Specification.md`), de los comandos `/lint` y `/audit-graph`, y del verificador `scripts/verify_graph.py`.
**Estado del grafo en el momento de la auditoría:** 1840 AKUs · 137 TAKUs (todos `draft`) · 1 componente conectado · 0 errores de `verify_graph`.

---

## 1. Modelo de grafo

### 1.1 Tipos de nodo

**AKU (Atomic Knowledge Unit)** — una proposición falsable por fichero (`aku/aku-<slug>.md`). Hard rule #1: *"One AKU = exactly one falsifiable proposition"*. Tres clases de primera categoría (campo obligatorio `aku_class` justo tras `id`):

| Clase | Patrón de statement | Falsable por |
|---|---|---|
| `concept` | *"W es [definición]; incluye [X]; excluye [Y]; implica [Z]."* | adecuación, implicaciones, frontera |
| `method` | *"En [condiciones], Z se computa como [fórmula]."* | aplicación (fórmula errónea → número erróneo) y domain mismatch |
| `claim` | *"X produce mejor resultado que Y bajo [condiciones]."* | sentido popperiano clásico |

Las tres son recuperables; *"None is filtered out as 'merely definitional.'"* Solo se excluye el **hollow nominal vocabulary** (términos sin implicaciones, fórmula ni condiciones de frontera).

Dimensiones epistémicas independientes en cada AKU:
- `epistemic_type`: `sourced` | `tacit` | `hybrid`.
- `llm_confidence`: determinista (baseline 0.50; +0.10 por fuente independiente, cap 0.95; −0.30 al claim más antiguo ante contradicción; `null` si `tacit`).
- `human_certainty.status`: `unvalidated` | `validated-true` | `validated-false` | `partial` | `context-dependent`.
- **Nunca se promedian** `llm_confidence` y `human_certainty` (hard rule #4); se muestran por separado y el humano prevalece cuando está fijado.

**TAKU (Tactical/Executable Knowledge Unit)** — estructura ejecutable (`taku/<tipo>/`). Ocho tipos: `technique` | `case` | `tool` | `framework` | `heuristic` | `story` | `protocol` + custom (los custom deben declarar sus headers de body en `CLAUDE.md` antes de usarse — actualmente solo `reference`). Cada TAKU LLM-authored exige ≥1 link `justified_by` a un AKU; 2–5 es el sweet spot, >7 dispara flag de link inflation.

**Frontera dura evidencia/derivado:** solo `raw/` es evidencia. Los AKUs citan en `sources[]` únicamente rutas markdown bajo `raw/` (nunca PDFs, nunca otro AKU). Los AKUs nunca se citan entre sí como fuente (hard rule #2).

### 1.2 Tipos de relación permitidos y su significado

**Relaciones AKU↔AKU** (8 campos = 4 pares + el self-pair + `related`):

| Campo (saliente / entrante) | Significado | Patrón de clase típico |
|---|---|---|
| `supports` → / `supported_by` ← | A sustenta/evidencia a B (el concepto subyace a la fórmula; la evidencia sostiene el concepto) | concept↔method; evidencia→concept |
| `constrains` → / `constrained_by` ← | A acota la aplicación correcta de B | claim→concept (cuando el claim refina el uso correcto) |
| `context_breaks_at` → / `breaks_context_of` → | A y B son métodos mutuamente excluyentes según contexto (par **simétrico**: ambos lados llevan el mismo apuntando al otro) | method↔method en contextos excluyentes |
| `contradicts` ↔ | A y B se contradicen (self-pair: se escribe en ambos ficheros) | cualquier clase |
| `related` ↔ | enlace más débil; métricas pareadas sin vínculo causal/lógico | concept↔concept (usar con moderación; profundidad de retrieval limitada a 1 hop) |

Preferencia explícita: *"prefer typed relations … over `related`. Over-use of `related` is a graph health signal."*

**Relaciones TAKU:** pares `complementary` ↔ `complementary`, `alternative_to` ↔ `alternative_to`, `precedes` ↔ `follows` (con `sequence_type` `recommended`|`required` coincidente). Links TAKU→AKU: `justified_by`, `constrained_by` (entrantes); `breaks_when`, `illustrates`, `challenges` (salientes). Validación de link independiente del contenido: `llm-proposed` → `human-validated`.

---

## 2. Reglas de enlazado

### 2.1 Simetría obligatoria — sync de 3 capas

Hard rule #3 + #8 + § Body wikilinks. **Toda edición de relación se propaga a tres sitios en el mismo commit:**
1. El **inverso en el frontmatter del OTRO fichero**.
2. El **wikilink en el body de ESTE** fichero (sección `## Relaciones`).
3. El **wikilink en el body del OTRO** fichero.

El frontmatter YAML es la fuente de verdad máquina-legible; el body `## Relaciones` es la proyección visible en el grafo de Obsidian (Obsidian solo dibuja aristas desde `[[wikilink]]`, no desde YAML). Flechas: `→` saliente, `←` entrante, `↔` simétrico. `verify_graph.py` comprueba las tres capas: targets existentes, simetría del inverso (`ASIMETRIA`), y coincidencia frontmatter↔body (`BODY-DRIFT`).

### 2.2 Cuándo crear un enlace — regla de los 3 niveles de rigor

Toda conexión candidata se clasifica de más a menos peso epistémico:

- **(a) Anclada en el texto** — el `statement` de un AKU menciona literalmente el concepto central del otro. → **El agente la aplica solo** (la reporta, no la pregunta).
- **(b) Conexión conceptual directa** — sin mención literal, pero ambos describen el mismo objeto desde ángulos distintos, o uno es composición/instancia del otro. → **El agente propone con razonamiento; el humano aprueba antes de escribir.**
- **(c) Conocimiento tácito del humano** — claim o relación que viene de su experiencia, no del material (`tacit`/`hybrid`, nunca `sourced`). → **El agente nunca lo crea solo.**

Distinción crítica: **conexión conceptual real ≠ coincidencia empírica.** Si la conexión aplica a «cualquier negocio» o «muchas empresas», es coincidencia empírica, no conceptual → skip. *"Rigor, no cantidad: ante la duda, NO conectar y marcar para revisión."*

### 2.3 Anti link-inflation

- AKU: preferir relaciones tipadas; el exceso de `related` es señal de salud del grafo. `related` >30d → proponer upgrade a tipada o marcar `related-confirmed`. AKUs con solo `related` tras 14d → integración superficial (flag).
- TAKU: 2–5 `justified_by` es el sweet spot; **>7 dispara flag de link inflation**.

### 2.4 Paso INTEGRATE 5.5 (en cada ingest)

Tras crear los AKUs nuevos con sus inversos (paso 5 del Ingest), el paso **5.5 INTEGRATE** evalúa, para cada AKU nuevo, con qué AKUs **existentes del grafo** debería conectarse (no solo deduplicar): busca **mención textual** y **adyacencia conceptual directa**, cablea según los 3 niveles, y documenta los wires en el commit del ingest. *"Ningún concepto nuevo queda huérfano por defecto."*

---

## 3. Qué definen `/lint` y `/audit-graph`

### 3.1 `/lint` — diagnóstico de solo lectura

*"Do not modify any AKU or TAKU file during this pass — lint is read-only diagnosis. Repairs are proposed, not applied."* **No crea enlaces.** Recorre todo `aku/` y `taku/` y reporta a `outputs/lint/YYYY-MM-DD.md`:

- **Integridad estructural:** roturas bidireccionales (4 pares AKU + pares TAKU), AKUs citando AKUs en `sources[]`, headers de body faltantes por tipo TAKU, custom-types sin schema, self-relations, integridad del **source-tag** de `domain` (vocabulario cerrado por corpus).
- **Atomicidad/calidad:** statements con ` and `/` both `/` while ` (posibles compuestos), nodos aislados (0 relaciones), AKUs con solo `related`.
- **Decay/freshness:** `validated-true` >365d, `unvalidated` >180d, `sourced`+`unvalidated` >365d, `context-dependent` >90d, TAKUs `validated-working` >365d.
- **Contradicciones:** `contradicts` sin resolver >30d, mechanistic-gap, feedback no procesado.
- **Salud TAKU:** active+unvalidated >90d, >7 `justified_by`, TAKUs sin links no activables.
- **Estructura emergente:** axiom candidates (10+ `supports` entrantes — informativo).
- **Vocabulario de dominio:** clusters de tags similares → propone normalización, **nunca auto-fusiona**.
- **Fragmentación:** componentes conectados > 1 → recomienda lanzar `/audit-graph`.

Commit `lint: YYYY-MM-DD`. **No commitea reparaciones** — esas son `update:` que autoriza el humano.

### 3.2 `/audit-graph` — auditoría topológica + propuesta de puentes

Operación periódica lanzada por el usuario. Construye el grafo completo, detecta topología (componentes — **debe ser 1**; huérfanos degree 0 — error; sub-conectados degree 1-2 — candidatos; clusters temáticos aislados >3), y para cada candidato busca conexiones por **scan textual** (grep del statement) y **adyacencia conceptual**.

**Sí crea enlaces, pero solo de tier (a):** *"Aplicar tier (a) automáticamente con script Python (`add_related` con bidir + body wikilinks)."* Los tier (b) los **presenta al usuario** y espera aprobación; tier (c) nunca los crea unilateralmente. Hard rules durante el audit: **nunca crea AKUs nuevos** (solo wirea entre existentes), nunca marca `validated-*`, nunca wirea coincidencia empírica, y si una conexión no encaja en ninguno de los 8 tipos no la fuerza (skip + documenta para revisión de taxonomía). Reporte a `outputs/lint/audit-YYYY-MM-DD.md`; commit `audit: graph-audit YYYY-MM-DD`.

**Diferencia operativa clave:** `/lint` **solo reporta**; `/audit-graph` **reporta y aplica tier (a)**, propone (b)/(c).

---

## 4. Ciclo de vida TAKU y validación humana

- **Autoría LLM → `status: draft` siempre.** Hard rule #5: *"Never auto-activate a TAKU."* Solo el humano transiciona `draft → active`.
- El agente **nunca** fija `human_certainty.status` fuera de `unvalidated`, nunca `link_validation: human-validated`, nunca `content_validation` a `human-reviewed`/`human-authored`. *"You propose. The human validates."*
- Validación de **contenido** y de **cada link** son dimensiones independientes: un TAKU `human-reviewed` con todos los links `llm-proposed` **no** está plenamente validado.
- TAKUs human-authored pueden activarse con 0 links (el humano asume la responsabilidad); los LLM-authored exigen ≥1 `justified_by`.
- Modo failure-diagnosis: ante un TAKU que falla, el agente recupera el cluster de AKUs, revisa `context_breaks_at`/`constrained_by`, y **propone un diff** sin editar.

---

## 5. Evaluación crítica

### 5.1 Lo que está bien definido

- **Separación evidencia/derivado** (`raw/` inmutable, AKUs no se citan entre sí) es nítida y verificable mecánicamente.
- **Sync de 3 capas + `verify_graph.py`** cierra el hueco clásico entre YAML y grafo Obsidian; la simetría es comprobable y está comprobada (0 errores).
- **Doble dimensión de confianza sin promediar** preserva la señal más valiosa (alto `llm_confidence` + `validated-false`).
- **Regla de los 3 niveles** da un criterio operativo claro de cuándo aplicar vs proponer vs nunca-crear, con la distinción conceptual≠empírica como guardia anti-ruido.
- **Granularidad máxima** (Salvaguarda 2) + **paso de cobertura** (Salvaguarda 1) son defensas explícitas contra la omisión sistemática.

### 5.2 Huecos detectados

**GAP 1 — Relleno retroactivo de puentes cross-corpus al entrar libros nuevos (el más importante).**
El manual define la integración del grafo en **dos momentos**: (i) el paso INTEGRATE 5.5 *dentro de cada ingest* y (ii) la auditoría global `/audit-graph` *lanzada manualmente*. Pero:
- El paso 5.5 integra **el AKU nuevo contra el grafo existente** — es *forward-only*. Cuando entra un corpus nuevo (p. ej. un libro), sus AKUs se conectan hacia atrás, pero **no hay ningún disparador que reevalúe los AKUs ANTIGUOS contra el corpus nuevo de forma sistemática**. Un concepto de liderazgo de Power MBA ya escrito hace meses no se "entera" de que ha llegado el liderazgo de Jocko salvo que el agente, al ingerir Jocko, recuerde mirar hacia Power MBA — lo cual el 5.5 sí cubre en teoría, pero **solo desde el lado nuevo y AKU a AKU**, sin una pasada temática cross-corpus dirigida.
- `/audit-graph` **sí** podría hacerlo, pero (a) es manual ("lanzada por el usuario explícitamente, no automática"), (b) su heurística primaria es **topológica** (componentes, degree, clusters aislados) y de **scan textual**, no una comparación semántica temática corpus-vs-corpus, y (c) por diseño **solo aplica tier (a)**; los puentes cross-corpus más valiosos suelen ser **tier (b)** (mismo concepto, distinto vocabulario entre autores) y por tanto quedan represados esperando aprobación manual uno a uno.
- **No existe** en el manual: (1) una obligación de lanzar una pasada de **bridging retroactivo cross-corpus** tras completar la ingesta de un corpus nuevo; (2) un criterio para **agrupar AKUs por tema/dominio across corpora** y comparar definiciones reales (no solo palabras); (3) un registro de qué pares cross-corpus ya se evaluaron, para no repetir trabajo ni dejar huecos.
- **Consecuencia medida:** la auditoría que acompaña a este informe encontró 4 componentes desconectados y >1000 AKUs sub-conectados (degree 1-2) en un grafo de 1840 nodos provenientes de 6 corpus — exactamente el patrón que produce un bridging forward-only sin pasada retroactiva.
- **Recomendación:** añadir a `CLAUDE.md` un tercer momento de integración — **"INTEGRATE retroactivo cross-corpus"** — disparado al cerrar un corpus nuevo: agrupar por dominio/tema, comparar statements reales corpus-vs-corpus, aplicar tier (a) y (b-fuerte) bajo autorización por lotes (como en esta sesión), y registrar los pares evaluados. Definir también el **tag-de-corpus** como eje explícito de agrupación para esta pasada.

**GAP 2 — Tipos de relación insuficientes para puentes cross-corpus.**
Los 8 campos son ricos para relaciones *intra-tema* (sustento, restricción, contradicción, ruptura de contexto), pero para conectar el **mismo concepto visto por dos autores** el único campo disponible es `related` — justo el que el manual desaconseja por link-inflation. No hay un tipo `same_as`/`elaborates`/`corroborates` para "A y B son el mismo principio en corpus distintos". Resultado: o se fuerza `supported_by` (semántica algo torcida) o se acumula `related`. **Recomendación:** o bien declarar explícitamente que la corroboración cross-corpus se modela con `supported_by` (el segundo corpus *sostiene* el principio del primero) — y eximir esos `related`/`supported_by` del flag de inflation —, o bien introducir un tipo de relación de corroboración.

**GAP 3 — Ambigüedad `constrained_by` vs `context_breaks_at` no resuelta con ejemplos.**
El propio manual lista esta distinción en § "When to ask instead of act" como caso a consultar, pero no da una regla de decisión accionable ni ejemplos contrastados. Para una pasada autónoma a gran escala esto obliga a `related` por defecto (degradando la tipificación). **Recomendación:** añadir 2-3 ejemplos canónicos contrastados.

**GAP 4 — Vocabulario de dominio bilingüe sin política de resolución.**
Coexisten `liderazgo` (310) y `leadership` (56), `estrategia`/`strategy`, `marketing`/`marketing-digital`/`content-marketing`. El § Language conventions fija que los *términos técnicos* quedan en inglés y los *statements* en español, pero **no fija el idioma de los tags de `domain`** (salvo el source-tag, que sí es vocabulario cerrado). `/lint` detecta los clusters pero "nunca auto-fusiona" y no hay decisor. **Recomendación:** fijar el idioma canónico de los domain-tags temáticos (recomendado: español, coherente con los statements) y una tabla de normalización, o declarar que el bilingüismo es intencional.

**GAP 5 — `/audit-graph` no escala a bridging semántico masivo.**
Su método 3 ("scan textual" por grep + "adyacencia conceptual") funciona para huérfanos y sub-conectados puntuales, pero no para comparar 663×429 AKUs cross-corpus. No define un flujo de **agrupación por tema → comparación de definiciones → cableado por lotes**. La pasada de esta sesión tuvo que construir tooling ad-hoc (`_audit_analyze.py`, `_audit_wire.py`). **Recomendación:** absorber ese flujo (agrupar por dominio, dump de statements por tema, wire driver con dry-run) en el comando `/audit-graph` como modo "deep/cross-corpus".

### 5.3 Veredicto

El `CLAUDE.md` está **bien definido para la operación intra-corpus y para la integridad estructural** (las hard rules y el sync de 3 capas son sólidos y mecánicamente verificables). El hueco real y de impacto está en la **integración cross-corpus retroactiva**: el sistema integra hacia delante en cada ingest y ofrece una auditoría global manual, pero **no especifica cómo rellenar retroactivamente los puentes cross-corpus cuando entran libros nuevos**, ni con qué tipo de relación, ni con qué registro de cobertura. **GAP 1 queda marcado como el gap principal**, con GAP 2 y GAP 5 como sus habilitadores técnicos.
