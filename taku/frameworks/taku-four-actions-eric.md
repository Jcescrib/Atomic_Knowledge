---
type: taku
taku_type: framework
id: taku-four-actions-eric
title: "Four Actions Framework (ERIC: Eliminar · Reducir · Incrementar · Crear)"
origin: "The Power MBA — Módulo 2.6 «Océano azul» (Kim & Mauborgne)"
domain: [estrategia, oceano-azul, propuesta-valor, power-mba]

when_to_use: >
  Cuando hay que redibujar la curva de valor de una propuesta para crear un
  océano azul: tras dibujar la curva actual del sector, se aplica el Four
  Actions Framework para decidir qué factores competitivos eliminar, reducir,
  incrementar y crear, generando una propuesta de valor diferenciada que rompe
  el trade-off valor-coste.

when_not_to_use: >
  Antes de haber mapeado los factores competitivos y la curva de valor actual
  (no hay nada sobre lo que actuar). Tampoco como receta mecánica sin la lógica
  de innovación en valor detrás: mover factores sin buscar simultáneamente más
  valor y menos coste solo reproduce el océano rojo.

aku_links:
  justified_by:
    - id: aku-eric-eliminar-method
      link_validation: llm-proposed
      link_note: "Acción E: qué factores que la industria da por supuestos eliminar."
    - id: aku-eric-reducir-method
      link_validation: llm-proposed
      link_note: "Acción R: qué factores reducir muy por debajo del estándar del sector."
    - id: aku-eric-incrementar-method
      link_validation: llm-proposed
      link_note: "Acción I: qué factores incrementar muy por encima del estándar del sector."
    - id: aku-eric-crear-method
      link_validation: llm-proposed
      link_note: "Acción C: qué factores nuevos crear que la industria no ofrece."
    - id: aku-innovacion-valor-via-eric-claim
      link_validation: llm-proposed
      link_note: "Claim central: aplicar ERIC produce innovación en valor (más valor + menos coste)."
    - id: aku-ampliar-gap-valor-precio-claim
      link_validation: llm-proposed
      link_note: "deducible: corrobora aku-innovacion-valor-via-eric-claim desde [hormozi] (cross-source)"
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
  complementary: [taku-estrategia-oceano-azul]
  alternative_to: []
  precedes: []
  follows: []

created: 2026-06-04
updated: 2026-06-04
status: draft
status_note: ""
---

## Summary

El Four Actions Framework (Kim & Mauborgne) es la herramienta operativa para redibujar la curva de valor de una propuesta y crear un océano azul. Plantea cuatro preguntas sobre los factores competitivos del sector — **Eliminar**, **Reducir**, **Incrementar**, **Crear** (ERIC) — cuya respuesta combinada produce una nueva curva de valor que ofrece simultáneamente más valor y menos coste, rompiendo el trade-off tradicional (innovación en valor).

## Core Components

| Acción | Pregunta | AKU |
|---|---|---|
| **Eliminar** | ¿Qué factores que la industria da por supuestos deberían eliminarse? | `aku-eric-eliminar-method` |
| **Reducir** | ¿Qué factores deberían reducirse muy por debajo del estándar del sector? | `aku-eric-reducir-method` |
| **Incrementar** | ¿Qué factores deberían incrementarse muy por encima del estándar del sector? | `aku-eric-incrementar-method` |
| **Crear** | ¿Qué factores nuevos, que la industria nunca ha ofrecido, deberían crearse? | `aku-eric-crear-method` |
| Resultado | Aplicar las cuatro acciones produce innovación en valor | `aku-innovacion-valor-via-eric-claim` |

Las dos primeras acciones (Eliminar, Reducir) atacan la estructura de **coste**; las dos últimas (Incrementar, Crear) elevan el **valor** para el comprador. Aplicarlas a la vez es lo que rompe el trade-off.

## How to Apply

1. **Partir de la curva de valor actual** del sector y de los factores competitivos ya mapeados.
2. **Eliminar**: identificar factores que el sector da por sentados pero que los clientes no valoran realmente — quitarlos baja coste sin sacrificar valor percibido.
3. **Reducir**: detectar factores sobre-dimensionados respecto a lo que el cliente necesita — bajarlos muy por debajo del estándar.
4. **Incrementar**: localizar factores infra-servidos por el sector — elevarlos muy por encima del estándar.
5. **Crear**: inventar factores que la industria nunca ha ofrecido y que abren demanda nueva.
6. **Recomponer la nueva curva de valor** con el resultado de las cuatro acciones y verificar que cumple la condición de innovación en valor: más valor Y menos coste simultáneamente.

## Underlying Claims

- `aku-innovacion-valor-via-eric-claim` sostiene que la aplicación conjunta de las cuatro acciones es lo que genera innovación en valor (no acciones aisladas).
- Las acciones Eliminar/Reducir operan sobre el eje coste; Incrementar/Crear sobre el eje valor — la simultaneidad es la condición que rompe el trade-off valor-coste.

## Strengths

- Convierte la abstracción «innovación en valor» en cuatro preguntas concretas y accionables en una sesión de trabajo.
- Fuerza a mirar tanto la reducción de coste (Eliminar/Reducir) como la creación de valor (Incrementar/Crear), evitando el sesgo de optimizar solo una dimensión.
- Encaja directamente sobre la curva de valor, dando un flujo de diagnóstico-a-rediseño continuo.

## Limitations and Criticisms

- No dice **cuáles** son los factores a mover: la calidad del resultado depende del conocimiento del sector y del cliente que aporte el equipo.
- Riesgo de aplicarlo de forma mecánica (mover factores sin buscar de verdad innovación en valor), reproduciendo un océano rojo ligeramente distinto.
- No aborda la defensa del océano azul una vez creado: los competidores pueden imitar la nueva curva.

## Variants and Extensions

- **ERRC grid / Matriz Eliminar-Reducir-Incrementar-Crear**: la misma herramienta presentada como rejilla de cuatro celdas (en este vault, las cuatro acciones se modelan como method-AKUs ERIC independientes y se relacionan con `aku-matriz-rice-concept`).
- **Buyer Utility Map** y **curva de valor**: herramientas complementarias del toolkit de océano azul que alimentan y validan el resultado del Four Actions.

## Relaciones

**justified_by** ← [[aku-eric-eliminar-method]] · [[aku-eric-reducir-method]] · [[aku-eric-incrementar-method]] · [[aku-eric-crear-method]] · [[aku-innovacion-valor-via-eric-claim]] · [[aku-ampliar-gap-valor-precio-claim]]
**complementary** ↔ [[taku-estrategia-oceano-azul]]
