---
type: taku
taku_type: framework
id: taku-power-value-modelo
title: "Power Value — modelo para analizar y diseñar propuestas de valor"
origin: "The Power MBA — Módulo 2.5 «Conceptos clave: propuesta de valor»"
domain: [value-proposition, framework, marketing, business-model, power-mba]

when_to_use: >
  Cuando se necesita analizar la propuesta de valor de un negocio
  (propio o competidor), evolucionar una propuesta existente, o diseñar una
  propuesta nueva desde cero. Particularmente útil cuando los mensajes
  actuales no movilizan al cliente y hay sospecha de que se está
  comunicando funcionalidades en lugar de beneficios últimos.

when_not_to_use: >
  Como sustituto del análisis cuantitativo de unit economics (precio,
  margen, CAC, CLTV). Tampoco como única lente: la propuesta debe
  combinarse con análisis de segmentos (`taku-customer-persona`,
  `taku-estrategias-targeting`) y de competencia ampliada.

aku_links:
  justified_by:
    - id: aku-power-value-modelo-concept
      link_validation: llm-proposed
      link_note: "El canvas mismo."
    - id: aku-propuesta-de-valor-concept
      link_validation: llm-proposed
      link_note: "El concepto que el canvas operacionaliza."
    - id: aku-beneficio-funcional-concept
      link_validation: llm-proposed
      link_note: "Una de las tres dimensiones de beneficio."
    - id: aku-beneficio-emocional-concept
      link_validation: llm-proposed
      link_note: "Segunda dimensión de beneficio — crítica por la primacía de la emoción."
    - id: aku-problema-resuelto-concept
      link_validation: llm-proposed
      link_note: "Tercera dimensión — beneficio formulado en negativo."
    - id: aku-coste-percibido-amplio-concept
      link_validation: llm-proposed
      link_note: "La columna de costes en sus siete dimensiones."
    - id: aku-cosas-importantes-concept
      link_validation: llm-proposed
      link_note: "Los motores últimos a los que apuntar."
    - id: aku-competencia-amplia-concept
      link_validation: llm-proposed
      link_note: "La dimensión Diferenciación se mide contra esta visión ampliada."
    - id: aku-ecuacion-valor-claim
      link_validation: llm-proposed
      link_note: "El criterio de éxito del marco: Beneficios > Costes."
    - id: aku-emocion-prevalece-razon-claim
      link_validation: llm-proposed
      link_note: "Claim de fondo que prioriza la columna emocional de beneficios."
    - id: aku-reducir-costes-no-precio-claim
      link_validation: llm-proposed
      link_note: "Claim que prioriza operar sobre costes no-precio para preservar margen."
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
  complementary:
    - taku-estrategia-oceano-azul
    - taku-plan-de-marca
  alternative_to: []
  precedes: []
  follows: []

created: 2026-06-03
updated: 2026-06-03
status: draft
status_note: ""
---

## Summary

Canvas 2×3 que descompone una propuesta de valor en columnas (qué ofreces / beneficios / costes) cruzadas con filas (tu propuesta / diferenciación frente a competidores). Fuerza una mirada estructural a los componentes del valor y, sobre todo, hace explícita la columna de beneficios emocionales y la dimensión ampliada del coste (mucho más allá del precio) que las propuestas de valor débiles típicamente ignoran.

## Core Components

| | **QUÉ OFRECES** | **BENEFICIOS / PARA QUÉ** | **COSTES Y ESFUERZOS** |
|---|---|---|---|
| **Tu propuesta** | Funcionalidades y componentes separados | Racionales · Emocionales · Problemas resueltos | Económicos · Esfuerzos · Riesgos físicos · Riesgos sociales · Tiempo · Funcional · Costes de oportunidad |
| **Diferenciación** | Vs. competidores (ampliados: cualquier alternativa) | Beneficios diferenciales últimos | Costes diferenciales vs. competidores |

**Ecuación de valor**: una propuesta es válida cuando **Beneficios − Costes > 0** o equivalentemente **Beneficios / Costes > 1**.

## How to Apply

1. **Rellenar «Qué ofreces»** identificando todas las funcionalidades y componentes sin dar nada por supuesto.
2. **Rellenar la columna «Beneficios» en tres niveles**: racionales (qué obtienen), emocionales (cómo les hace sentir, ver `aku-emocion-prevalece-razon-claim`), problemas resueltos (qué dolor desaparece). **Vete a los beneficios últimos** (`aku-cosas-importantes-concept`): no te quedes en la primera capa.
3. **Rellenar la columna «Costes» en sus siete dimensiones** (no solo precio). Esto es donde la mayoría de empresas pierde ventaja sin darse cuenta.
4. **Verificar la ecuación de valor**: ¿Beneficios > Costes para el cliente objetivo?
5. **Rellenar la fila Diferenciación** comparando contra el conjunto **ampliado** de competidores (`aku-competencia-amplia-concept`): no solo el mismo producto, sino toda alternativa que cubre el mismo job.
6. **Identificar palancas de mejora**: ¿podemos aumentar beneficios emocionales? ¿reducir esfuerzo o tiempo (mejor que reducir precio, ver `aku-reducir-costes-no-precio-claim`)?
7. **Usar el canvas resultante** como input para mensajes, anuncios, web, propuesta comercial.

## Underlying Claims

- `aku-power-value-modelo-concept` postula la estructura del canvas como suficiente para descomponer cualquier propuesta de valor.
- `aku-ecuacion-valor-claim` define el criterio de éxito (B > C).
- `aku-emocion-prevalece-razon-claim` justifica el peso de la columna emocional.
- `aku-reducir-costes-no-precio-claim` da una prescripción operativa para optimizar.

## Strengths

- Estructura simple en un solo cuadro.
- Explicita la columna emocional (frente a marcos que se quedan en funcional).
- Explicita la dimensión amplia del coste (mucho más allá del precio).
- Conecta con la realidad neuropsicológica de la decisión (emoción > razón).
- Aplicable tanto al análisis competitivo (fila Diferenciación) como al diseño puro.

## Limitations and Criticisms

- **No es cuantitativo**: ofrece estructura, no medición. Cuantificar «beneficio emocional» requiere otras herramientas.
- **El marco asume cliente individual**: en B2B con comités de compra, los beneficios y costes son distintos para cada stakeholder; hay que aplicar el canvas por persona.
- **Mucho terreno**: con 2 filas × 3 columnas + sub-componentes, rellenarlo bien lleva tiempo; la tentación es hacerlo superficialmente.
- **No incluye contexto temporal**: la propuesta de valor evoluciona con el ciclo de vida del producto y el mercado; el canvas captura un momento.

## Variants and Extensions

- **Value Proposition Canvas (Osterwalder)**: variante con énfasis en pains/gains/jobs por segmento, complementaria al BMC.
- **Jobs To Be Done (Christensen)**: profundiza en el «para qué último» (la cosa importante) y reformula competencia ampliada en términos de jobs.
- **Blue Ocean (Kim & Mauborgne)**: ver `taku-...` del módulo 2.6 — la lógica de mover en el plano de costes y beneficios para crear espacios nuevos.

## Relaciones

**justified_by** ← [[aku-power-value-modelo-concept]] · [[aku-propuesta-de-valor-concept]] · [[aku-beneficio-funcional-concept]] · [[aku-beneficio-emocional-concept]] · [[aku-problema-resuelto-concept]] · [[aku-coste-percibido-amplio-concept]] · [[aku-cosas-importantes-concept]] · [[aku-competencia-amplia-concept]] · [[aku-ecuacion-valor-claim]] · [[aku-emocion-prevalece-razon-claim]] · [[aku-reducir-costes-no-precio-claim]]

**complementary** ↔ [[taku-estrategia-oceano-azul]] · [[taku-plan-de-marca]]
