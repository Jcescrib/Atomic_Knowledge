# Auditoría hiper-rigurosa del grafo + creación de puentes cross-corpus

**Fecha:** 2026-06-07
**Motor:** `verify_graph.py` (integridad estructural) + tooling de auditoría (`scripts/_audit_analyze.py`, `_audit_wire.py`) siguiendo `/lint` y `/audit-graph`.
**Autorización:** el usuario autorizó crear enlaces por lotes sin aprobación uno-a-uno. Los pares ambiguos NO se forzaron — se listan abajo para revisión humana.

---

## 1. Estado inicial vs final

| Métrica | Inicial | Final |
|---|---|---|
| AKUs | 1840 | 1840 |
| Errores `verify_graph` | 0 | **0** |
| Componentes conectados | **4** | **1** |
| Componente mayor | 1831 | 1840 |
| Huérfanos (degree 0) | 0 | 0 |
| Sub-conectados (degree 1-2) | 1126 | 1080 |
| Aristas nuevas | — | **95** (8 islas + 87 cross-corpus) |

Distribución por corpus: power-mba 663 · jocko 429 · hormozi 380 · naval 235 · james-clear 84 · robert-greene 48 · (unknown) 1.

**TAKUs:** los 137 siguen en `status: draft` (Tarea B confirmada — ninguno activado por error).

---

## 2. Batch 0 — reparación de fragmentación (3 islas → componente único)

El grafo tenía 4 componentes. Las 3 islas se puentearon al componente principal con relaciones tipadas (8 aristas):

- **Isla Atomic Habits** (autocontrol / cues / contexto / entorno) → `habit-loop`, `cuatro-leyes-del-cambio-de-conducta`, `diseña-tu-entorno`.
- **Isla Naval salud/prioridades** → jerarquía `riqueza-salud-felicidad-se-persiguen-en-ese-orden`, `formula-de-la-felicidad`.
- **Isla Naval retiro** → `wealth-activos-que-ganan-mientras-duermes`, `equity`.

Resultado: **componentes 4 → 1**. Cumple la regla de `CLAUDE.md` (debe ser 1 solo componente).

---

## 3. Batches 1-6 — puentes cross-corpus (87 aristas)

Método: agrupación por tema/dominio, comparación de los statements reales corpus-vs-corpus (vía sub-auditoría paralela), revisión estricta (cita textual de ambos statements), descarte de coincidencias empíricas y same-corpus, y cableado bidireccional con sync de 3 capas. Cada lote: `verify_graph` 0 errores + commit + push.

| Batch | Tema | Corpus | Aristas |
|---|---|---|---|
| 1 | Liderazgo | jocko · power-mba · hormozi | 11 |
| 2 | Disciplina / hábitos / ego | jocko · james-clear · naval | 20 |
| 3 | Poder / influencia | robert-greene · jocko · power-mba · hormozi | 14 |
| 4 | Riqueza / unit-economics | naval · power-mba · hormozi | 9 |
| 5 | Oferta / valor / copy | hormozi · power-mba | 17 |
| 6 | Felicidad / mente / salud | naval · james-clear · jocko · power-mba | 16 |

### 3.1 Caso testigo verificado — Leadership Jocko ↔ Power MBA

Confirmado y cableado explícitamente (Batch 1). Los dos corpus tratan el mismo objeto «liderazgo» desde ángulos distintos y estaban desconectados:

- `mind-control-controla-tu-propia-mente` + `self-discipline-viene-de-dentro` (Jocko) **supports** → `autoliderazgo-prerequisito` + `tres-capas-liderazgo` (Power MBA): el control de la propia mente es el mecanismo del autoliderazgo que Power MBA postula como prerequisito.
- `liderazgo-situacional` (Power MBA) **related** ↔ `everyone-same-everyone-different` + `liderazgo-indirecto-supera-al-directo` (Jocko): mismo principio de adaptar el estilo a la persona/situación.
- `estilos-autoritario-delegativo` (Power MBA) **related** ↔ `dar-ordenes-solo-commanders-intent` (Jocko): el polo delegativo ES el mando por Commander's Intent.
- `no-obligar-sino-liderar` (Jocko) **supports** → `liderazgo` (def. Power MBA: motivar/inspirar, no forzar).
- `lideres-nacen-y-se-hacen` (Jocko) **supports** → `aprende-nuevas-habilidades-liderazgo` (Power MBA): el liderazgo se desarrolla.

### 3.2 Contradicts cross-corpus de alto valor (creados)

- `48laws-12-selective-honesty-to-disarm` (Greene: usar honestidad selectiva para engañar) **contradicts** `lideres-dicen-la-verdad` (Jocko): oposición normativa directa sobre la honestidad.
- `48laws-43-work-on-hearts-and-minds` (Greene: seducir para volver al otro tu peón) **contradicts** `liderazgo-vs-manipulacion` (Jocko: el líder busca el bien del equipo, el manipulador el propio): tensión amoral vs liderazgo de servicio.

Estos son exactamente la señal cross-corpus más valiosa: misma técnica, ética opuesta.

---

## 4. PARA REVISIÓN HUMANA — pares apartados (no cableados)

Apartados por rigor: o son coincidencia empírica/genérica, o un `contradicts` no es negación estricta (es diferencia de marco), o el solapamiento es tangencial. **Decisión del humano.**

> **RESOLUCIÓN (2026-06-08, decisión del usuario aplicada):**
> - **§4.1** → **SKIP** (no enlazar). Decisión firme «no enlazar».
> - **§4.2** (6 pares propuestos como contradicts) → cableados como **`related`** (Batch 07, 7 aristas — el par §4.2.5 tiene 2 destinos).
> - **§4.3** (17 entradas tangenciales) → cableadas como **`related`** (Batch 08, 19 aristas — §4.3.5 y §4.3.9 tienen 2 destinos cada una).
> - Total resolución: **26 aristas nuevas** (`related`, bidireccionales, sync 3-capas). `verify_graph`: 0 errores. Ningún `contradicts` creado.

### 4.1 Falso amigo (recomendación: SKIP) — **RESUELTO: SKIP (no enlazado)**
- `leverage-multiplicador-de-juicio` (Naval, palanca de productividad: capital/labor/código) ↔ `apalancamiento-financiero` (Power MBA, amplificación del ROE vía deuda). Misma palabra «apalancamiento», objeto distinto. Solo la sub-fuente «capital» de Naval solapa parcialmente. → **Decisión: NO ENLAZAR.**

### 4.2 `contradicts` propuestos pero NO negación estricta — **RESUELTO: cableados como `related`**
- `willpower-no-es-finita-disciplina-engendra-disciplina` (Jocko) vs `el-autocontrol-cuesta-porque-no-es-satisfactorio` (Clear): Jocko dice que la disciplina se fortalece con el uso; Clear que la fuerza de voluntad es poco fiable a largo plazo. Debate clásico (¿finitud vs fiabilidad?), pero no son la negación literal el uno del otro.
- `precio-alto-aumenta-valor-percibido` (Hormozi) vs `reducir-costes-no-precio` (Power MBA): subir precio vs no tocar precio y operar sobre costes no-monetarios. Compatibles, no estrictamente opuestos.
- `48laws-43-work-on-hearts-and-minds` (Greene) vs `no-obligar-sino-liderar` (Jocko): ambos rechazan la coerción; la oposición es de intención (uso propio vs servicio), no de la proposición.
- `48laws-07-get-others-to-do-work-take-credit` (Greene) vs `liderar-pares-no-busques-credito` (Jocko): llevarse el crédito vs no buscarlo — posible contradicts, pero el objeto difiere (táctica de poder vs cómo liderar pares).
- `las-personas-disciplinadas-estructuran-su-entorno` (Clear) vs `no-cuentes-con-motivacion-cuenta-disciplina` / `self-discipline-viene-de-dentro` (Jocko): disciplina por diseño-del-entorno vs disciplina como fuerza interna. Tensión interno/externo real; ¿related o contradicts matizado?
- `elige-el-campo-de-competicion-genes` (Clear) vs `eleccion-vence-naturaleza-y-crianza` (Jocko): peso de la predisposición genética (Clear) vs primacía de la elección (Jocko).

### 4.3 Solapamiento conceptual dudoso o tangencial — **RESUELTO: cableados como `related`**
- `enfocar-una-iniciativa-a-la-vez` (Jocko, foco organizativo / Prioritize and Execute) ↔ `single-tasking-foco-una-tarea` (Power MBA, foco cognitivo individual).
- `liderazgo-factor-mas-importante` (Jocko, postula importancia) ↔ `liderazgo` (Power MBA, define el objeto).
- `medida-significativa-liderazgo` (Jocko) ↔ `liderar-vs-gestionar` (Power MBA).
- `mejores-lideres-mision-no-ego` (Jocko, «misión» = objetivo operativo) ↔ `proposito-mision` (Power MBA, «misión» = razón de ser). Colisión de palabra, no de concepto.
- `evolucion-rol-fundador` (Power MBA) ↔ `delegar-todo-para-liderar` (Jocko) y ↔ `negocio-sin-ti-es-activo` (Hormozi): el fundador que deja de ejecutar.
- `48laws-13-appeal-to-self-interest` (Greene) ↔ `cialdini-reciprocidad` (Power MBA): mecanismos distintos (interés propio vs obligación de devolver).
- `48laws-32-play-to-peoples-fantasies` (Greene) ↔ `cialdini-simpatia` (Power MBA): fantasía ≠ simpatía/likability.
- `48laws-31-control-the-options` (Greene) ↔ `manejar-jefe-micromanager-indeciso` (Jocko): controlar las opciones del otro.
- `reversion-riesgo-numero-uno` / `urgencia` (Hormozi) ↔ `palabras-frases-persuasivas` (Kolenda/Power MBA): principio de oferta vs léxico de copy.
- `emocion-prevalece-razon` (Power MBA) ↔ `dream-outcome` (Hormozi): el deseo emocional como motor.
- `azucar-es-adictivo-como-droga` (Jocko) ↔ `estimulos-supernormales` (Clear): mecanismos distintos (neuroquímico vs etológico).
- `regla-100-no-80-20` (Jocko, abstinencia total) ↔ `el-autocontrol-cuesta` (Clear, soltar el deseo).
- `la-esperanza-declina-con-la-experiencia` (Clear) ↔ `no-hay-esquemas-para-hacerse-rico-rapido` (Naval): enlace solo por la frase «hacerse rico rápido».
- `felicidad-es-paz` (Naval) ↔ `the-warpath` (Jocko): enlace solo por la palabra «paz».
- `toda-actividad-de-pantalla-resta-felicidad` (Naval) ↔ `el-entorno-es-la-mano-invisible` (Clear): la pantalla como factor ambiental (tangencial).
- `wealth-activos-que-ganan-mientras-duermes` (Naval) ↔ `cltv-minus-cac` (Power MBA): riesgo de coincidencia empírica (todo negocio rentable es un activo).
- `lead-magnet-reduce-cac` (Power MBA) ↔ `cac` (def.): roza lo genérico (toda táctica «reduce CAC»).

---

## 5. Nota de método y vínculo con el GAP 1 del CLAUDE.md

Esta pasada es precisamente el **«INTEGRATE retroactivo cross-corpus»** que `_meta/auditoria-claude-md.md` (Tarea A, GAP 1) identifica como ausente en el manual: agrupar por tema, comparar definiciones reales corpus-vs-corpus, aplicar puentes por lotes con autorización agregada, y registrar lo evaluado. El tooling (`_audit_analyze.py`, `_audit_wire.py`) y estos lotes quedan como plantilla reutilizable para futuras reingestas de libros nuevos.

**Pendiente recomendado:** ~~que el humano revise la lista §4~~ → **HECHO (2026-06-08)**: el usuario resolvió toda la §4 (4.1 skip; 4.2 y 4.3 como `related`, +26 aristas). Queda como único pendiente, si procede, normalizar el vocabulario bilingüe de `domain` (`liderazgo`/`leadership`, `estrategia`/`strategy`).

---

## 6. Estado final tras resolución §4 (2026-06-08)

- Aristas de la resolución §4: **+26** (`related`): §4.2 → 7 (Batch 07), §4.3 → 19 (Batch 08); §4.1 → 0 (skip).
- Total acumulado de la auditoría: **95 (pasada inicial) + 26 (resolución §4) = 121 aristas nuevas**.
- Grafo: **1840 AKUs · 1 componente conectado · 0 huérfanos · 0 errores** `verify_graph`.
- TAKUs: 137/137 `draft`.
