---
type: taku
taku_type: technique
id: taku-customer-persona
title: "Customer Persona — cómo crear y usar"
origin: "The Power MBA — Módulo 2.4 «Segmentación y targeting»"
domain: [segmentation, customer, marketing, methodology, power-mba]

when_to_use: >
  Cuando se necesita personificar un segmento de clientes para crear
  propuestas de valor, mensajes, anuncios, canales o productos pensados en
  alguien concreto en lugar de en una abstracción. Especialmente útil al
  lanzar un nuevo producto o servicio (apoyarse en personas conocidas baja
  el coste cognitivo y aumenta la precisión).

when_not_to_use: >
  Cuando los segmentos son tan heterogéneos que una persona no los
  representa (en ese caso crear varias personas o re-segmentar). Tampoco en
  productos B2B muy complejos donde la decisión depende de un comité; ahí
  hace falta complementar con perfiles de stakeholders.

aku_links:
  justified_by:
    - id: aku-customer-persona-concept
      link_validation: llm-proposed
      link_note: "El concepto que la técnica operacionaliza."
    - id: aku-variables-segmentacion-concept
      link_validation: llm-proposed
      link_note: "Las variables que se cruzan para definir la persona."
    - id: aku-segmentos-de-clientes-concept
      link_validation: llm-proposed
      link_note: "Concepto base sobre el que la técnica opera."
  constrained_by: []
  breaks_when: []
  illustrates: []
  challenges: []

content_validation:
  status: llm-authored
  reviewed_by: ""
  review_date: ""
  review_notes: ""

human_certainty:
  status: unvalidated
  iterations: 0
  context_boundary: ""
  validated_by: ""
  validation_date: ""
  method: ""

taku_relations:
  complementary: []
  alternative_to: []
  precedes: []
  follows: []

created: 2026-06-03
updated: 2026-06-03
status: draft
status_note: ""
---

## Summary

Técnica para crear customer personas útiles: personas ficticias pero representativas que sustituyen segmentos abstractos en las decisiones de marketing, producto y canales. La clave es construir una persona que se pueda **describir** (no solo medir), apoyándose en gente real cercana cuando es posible.

## When to Use

Idealmente al diseñar o iterar la propuesta de valor, mensajes de marketing, decisión de canales o road-map de producto. La técnica gana fuerza cuando la respuesta a «¿a quién le hablamos?» deja de ser «mujeres entre 30 y 45» y pasa a ser «a Marta, que se levanta a las 7, lleva a sus hijos al cole, trabaja como X y se siente Y…».

## Prerequisites

- Tener identificados al menos un par de segmentos candidatos (ver `[[aku-segmentos-de-clientes-concept]]`).
- Conocer las variables de segmentación relevantes (`[[aku-variables-segmentacion-concept]]`).
- Idealmente, acceso a clientes reales cercanos para basar la persona en alguien concreto.

## Steps

1. **Elegir el método de construcción**:
   - A. **Cruzando variables de segmentación**: cruzar solo las variables más importantes para acotar la persona.
   - B. **Partiendo de alguno de tus clientes reales** o de empresas reales (en B2B). Suele dar personas más vivas y útiles.
2. **Cubrir el bloque «conocerle mejor»**: datos demográficos (edad, salario, clase social, lugar), biografía (vida, trabajo, familia, historia), perfil/estilo de vida (personalidad, aficiones, un día tipo), actitudes (cómo ve el mundo, qué le importa), objetivos/problemas/retos (qué le preocupa, qué le duele, qué quiere cambiar).
3. **Cubrir el bloque «por qué nos compra»**: qué problema quiere resolver o qué beneficio busca, stoppers (qué le pararía), alternativas que considera, qué le atrae de tu oferta concretamente, esfuerzos y costes que percibe, cómo te ve respecto a la competencia, qué canales usa para llegar a ti, cómo toma la decisión (Customer Journey), influenciadores (importante en B2B), cuándo y cómo usa el producto, qué espera y qué obtiene, fidelidad, recomendación/viralidad.
4. **Capturar las palabras del cliente**: identificar todas las expresiones, palabras e ideas que ya están en su mente sobre todos los puntos anteriores. Vital para crear mensajes que conecten.
5. **Validar contra la realidad**: contrastar la persona contra clientes reales (entrevistas, observación, encuestas). Iterar.
6. **Usarla activamente**: cada decisión de marketing/producto/canal se evalúa con «¿esto encaja con Marta?». Si la persona no se usa, es solo una plantilla con colorcitos.

## Anti-patterns

- **Plantilla con colorcitos**: rellenar todos los campos sin usar luego la persona en decisiones reales. Anti-patrón #1 según la fuente.
- **Quedarse en demográfica + geográfica**: la persona se queda plana y no genera insights accionables. Hay que incluir actitudinal y motivacional.
- **Inventar la persona desde cero sin datos**: produce sesgos y caricaturas. Mejor partir de gente real.
- **Una persona para «todos los clientes»**: si los clientes son heterogéneos, una sola persona no captura nada. Crear varias.

## Expected Outcome

Tener una persona (o pequeño set) que cualquier persona del equipo pueda invocar al tomar decisiones: «¿le sirve esto a Marta?», «¿le hablaría así Marta?», «¿por qué canal llegaría Marta a esto?». Producir mensajes y propuestas que conecten mucho más que las genéricas.

## Failure Signals

- El equipo no usa el nombre de la persona en reuniones.
- Las decisiones de marketing siguen siendo igual de genéricas que antes.
- La persona no responde preguntas concretas cuando se intenta «consultar».
- Múltiples personas se contradicen sin haber tomado decisión sobre cuál priorizar.

## Underlying Logic

Funciona porque [[aku-customer-persona-concept]] postula que pensar en una persona concreta produce decisiones de marketing más precisas que pensar en una abstracción medible. La técnica fuerza a aterrizar el nivel de detalle (palabras concretas, día tipo, motivaciones específicas) que las decisiones de marketing necesitan, y que un segmento abstracto no proporciona.

## Notes and Variants

- **Persona por canal de adquisición**: misma persona vista por canal (búsqueda, redes, recomendación) — útil cuando el customer journey varía por canal.
- **Persona negativa**: caracterizar a quién NO queremos como cliente. Útil para excluir leads de baja calidad.
- **Persona de stakeholder en B2B**: en compras corporativas, varias personas componen el comité de decisión (sponsor, técnico, financiero, end-user). Crear una persona por rol.

## Relaciones

**justified_by** ← [[aku-customer-persona-concept]] · [[aku-variables-segmentacion-concept]] · [[aku-segmentos-de-clientes-concept]]
