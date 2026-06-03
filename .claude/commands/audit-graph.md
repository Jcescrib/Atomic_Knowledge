---
description: Audita el grafo completo — detecta componentes aislados, huérfanos, sub-conectados, y propone puentes clasificados por los 3 niveles de rigor (CLAUDE.md § Integración del grafo)
---

Ejecuta la auditoría global descrita en `CLAUDE.md` § Integración del grafo. Operación periódica lanzada por el usuario.

## Pasos

1. **Construir grafo** completo desde `aku/`. Parse YAML frontmatter de cada AKU. Para verificación programática usa Python con la lógica del audit script (mira `outputs/lint/` para ejemplos).

2. **Detectar topología**:
   - Calcular componentes conectados (undirected, sobre TODAS las relaciones). **Debe ser 1**.
   - Listar AKUs huérfanos (degree 0) — **error**.
   - Listar AKUs sub-conectados (degree 1-2) — candidatos a wire-up.
   - Identificar clusters temáticos aislados (>3 AKUs sin enlaces a otros clusters).

3. **Para cada candidato a wire-up**, buscar conexiones potenciales con dos métodos:
   - **Scan textual**: grep el `statement` de cada otro AKU buscando mención literal del concepto central del candidato (acrónimo, nombre canónico, frase identificativa).
   - **Adyacencia conceptual**: sub-tipo/super-tipo (mismo dominio + uno engloba al otro), siblings (mismo dominio + paralelos), composición (uno usa al otro como input/output).

4. **Clasificar cada candidato** en uno de los 3 niveles de rigor:
   - **(a)** Mención literal del concepto en el statement del otro → **aplicar directamente**.
   - **(b)** Conexión conceptual sin mención literal → **proponer al usuario**.
   - **(c)** Requiere conocimiento práctico del usuario → **el usuario aporta o no; el agente nunca lo crea unilateralmente**.

5. **Aplicar tier (a)** automáticamente con script Python (`add_related` con bidir + body wikilinks). Verificar simetría tras cada batch.

6. **Presentar tier (b)** al usuario con razonamiento por cada propuesta. Esperar aprobación selectiva (todas / todas-menos-N / lista específica).

7. **Tras aprobación**, escribir las (b) aprobadas. Re-verificar simetría.

8. **Documentar el audit**:
   - Guardar reporte en `outputs/lint/audit-YYYY-MM-DD.md` con: estado inicial, propuestas tier (a) aplicadas, tier (b) presentadas, tier (b) aprobadas, estado final.
   - Actualizar `index.md` § Lint flags con el resumen.
   - Append a `log.md` con un entry tipo `## YYYY-MM-DD — audit-graph`.

9. **Commit** como:
   `audit: graph-audit YYYY-MM-DD — N tier-(a) applied + M tier-(b) approved`

## Output al usuario

- Componentes antes/después.
- Aristas antes/después.
- AKUs huérfanos (debería ser 0).
- AKUs todavía sub-conectados con razón documentada (por qué no se conectaron — descartes por rigor, no por descuido).
- Lista de tier (a) aplicadas (resumen, 1 línea por wire).
- Lista de tier (b) propuestas (con razonamiento de cada una).
- Lista de tier (c) potenciales si las hay (claim-AKUs candidates desde conocimiento del usuario).

## Hard rules durante el audit

- Aplicar tier (a) **solo** si la mención literal es clara. Si dudas → tier (b).
- **NUNCA** crear un AKU nuevo durante el audit. Solo wirea conexiones entre AKUs existentes.
- **NUNCA** marcar nada como `validated-*` o `human-validated`.
- **NUNCA** wire una conexión empírica (válida para «cualquier negocio»). Skip.
- Si una conexión propuesta no encaja en ninguno de los 8 tipos de relación (supports, supported_by, constrains, constrained_by, context_breaks_at, breaks_context_of, contradicts, related), no fuerces — skip y documenta el caso para revisión de la taxonomía de relaciones.

## Frecuencia recomendada

Lanzar tras procesar un módulo completo, o cada ~25 AKUs nuevos, o cuando el usuario sospeche fragmentación.
