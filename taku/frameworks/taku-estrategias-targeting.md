---
type: taku
taku_type: framework
id: taku-estrategias-targeting
title: "Estrategias de targeting — mass market, segmentado, nicho"
origin: "The Power MBA — Módulo 2.4 «Segmentación y targeting»"
domain: [strategy, targeting, segmentation, business-model]

when_to_use: >
  Cuando se necesita decidir a quién dirigir el modelo de negocio
  (especialmente al lanzarlo o pivotarlo), comparar la estrategia actual con
  alternativas viables, o diagnosticar por qué un modelo no consigue
  tracción (frecuentemente porque la estrategia de targeting no se eligió
  conscientemente).

when_not_to_use: >
  En modelos donde el targeting está forzado por restricciones externas
  (regulación, monopolio histórico) o donde la decisión de a quién dirigirse
  ya está validada por años de iteración. Tampoco como única lente: la
  elección de estrategia debe combinarse con análisis de propuesta de valor,
  unit economics y dinámicas competitivas.

aku_links:
  justified_by:
    - id: aku-mass-market-strategy-concept
      link_validation: llm-proposed
      link_note: "Primera estrategia — una oferta para todo el mercado."
    - id: aku-segmentado-strategy-concept
      link_validation: llm-proposed
      link_note: "Segunda estrategia — múltiples ofertas adaptadas por segmento."
    - id: aku-nicho-strategy-concept
      link_validation: llm-proposed
      link_note: "Tercera estrategia — foco extremo en un único segmento."
    - id: aku-nicho-recomendado-lanzamiento-claim
      link_validation: llm-proposed
      link_note: "Claim que prioriza nicho como estrategia recomendada en lanzamientos."
    - id: aku-segmentos-de-clientes-concept
      link_validation: llm-proposed
      link_note: "Concepto base sobre el que las tres estrategias operan."
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

Marco comparativo de las tres estrategias de targeting (mass market, segmentado, nicho) con sus implicaciones para conocer al cliente, crear propuesta de valor ganadora, llegar a ellos de forma rentable y construir posición competitiva. Hace explícito el trade-off entre alcance y profundidad de conocimiento del cliente, y recomienda nicho como estrategia por defecto en lanzamientos de modelos innovadores.

## Core Components

| Estrategia | Definición | Reto principal | Mejor para |
|---|---|---|---|
| **Mass market** | Una oferta para todo el mercado sin diferenciación | Es difícil ser competitivo sin segmentar | Negocios con grandes ventajas de coste o distribución |
| **Segmentado** | Varias propuestas adaptadas a segmentos distintos | Riesgo de apuntar a demasiados segmentos y no ser bueno en ninguno | Empresas con capacidad para ejecutar múltiples ofertas a la vez |
| **Nicho** | Foco extremo en un único segmento muy específico | Tamaño de mercado limitado | Lanzamientos innovadores, riesgo alto, recursos limitados |

Comparativa mass market vs nicho en 4 retos clave:

| Reto | Mass market | Nicho |
|---|---|---|
| Conocer y entender al cliente | Difícil (clientes heterogéneos) | Fácil (clientes homogéneos) |
| Crear propuesta ganadora | Difícil convencer a todos | Fácil convencer a un grupo homogéneo |
| Llegar de forma rentable | Canales masivos | Canales segmentados |
| Posición de mercado | Difícil ganar cuota | Más fácil construir monopolio + barreras |

## How to Apply

1. **Identificar la estrategia actual del modelo** (a menudo se opera con una estrategia por defecto sin haberla elegido).
2. **Diagnosticar si encaja con el momento del negocio**: ¿estás lanzando algo innovador con riesgo alto? Entonces nicho (`aku-nicho-recomendado-lanzamiento-claim`). ¿Tienes ventaja de coste/distribución? Mass market puede funcionar. ¿Tienes capacidad de ejecutar múltiples ofertas? Segmentado.
3. **Definir el(los) segmento(s) objetivo** usando variables relevantes del bloque `aku-variables-segmentacion-concept`.
4. **Para nicho**: identificar el customer persona específico (ver `taku-customer-persona`) y crear toda la propuesta y mensajes pensando en él.
5. **Revisar coherencia con el resto del modelo**: propuesta de valor, canales, relaciones, ingresos y costes deben alinearse con la estrategia de targeting elegida.
6. **Iterar si los resultados no llegan**: a menudo el problema no es el producto sino la estrategia de targeting. Cambiar de mass market a nicho (o viceversa) es una palanca estratégica de primer orden.

## Underlying Claims

- `aku-mass-market-strategy-concept`, `aku-segmentado-strategy-concept` y `aku-nicho-strategy-concept` definen las tres opciones estructurales del marco.
- `aku-nicho-recomendado-lanzamiento-claim` afirma que en lanzamientos innovadores, el nicho gana por reducción de riesgo y mejor product-market fit.
- `aku-segmentos-de-clientes-concept` (del BMC) es el concepto base sobre el que las tres estrategias operan.

## Strengths

- Tres categorías exhaustivas y comparables.
- Conecta directamente con las consecuencias operativas (canales, propuesta, conocimiento del cliente).
- Hace explícita la recomendación de nicho en lanzamientos, que contrarresta el sesgo natural a apuntar al mercado más grande posible.

## Limitations and Criticisms

- **Las tres no son siempre mutuamente exclusivas**: muchas empresas combinan mass market en un producto core con nichos en productos satélite.
- **El marco no incluye targeting B2B vs B2C**: las dinámicas son distintas (cuenta clave, ABM) y requieren extensiones específicas.
- **No cuantifica «cuándo dejar el nicho»**: tras alcanzar dominio en un nicho, la transición a segmentos adyacentes o mass market no está prescrita aquí.

## Variants and Extensions

- **Crossing the Chasm — Geoffrey Moore**: extiende la lógica de nicho/early adopters al ciclo de adopción de productos tecnológicos (innovators → early adopters → early majority → late majority → laggards).
- **Account-based marketing (ABM)**: variante de nicho radical en B2B —el «segmento» es una empresa concreta—.
- **Long-tail strategy — Chris Anderson**: variante donde el modelo agrega muchos nichos pequeños (e-commerce, plataformas de contenido).

## Relaciones

**justified_by** ← [[aku-mass-market-strategy-concept]] · [[aku-segmentado-strategy-concept]] · [[aku-nicho-strategy-concept]] · [[aku-nicho-recomendado-lanzamiento-claim]] · [[aku-segmentos-de-clientes-concept]]
