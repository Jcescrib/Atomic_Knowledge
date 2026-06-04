---
type: taku
taku_type: framework
id: taku-modelos-negocio-plataforma
title: "Modelos de negocio de plataforma — taxonomía y dinámicas"
origin: "The Power MBA — Módulo 2.3 «Conceptos clave de las plataformas»"
domain: [business-model, platform, network-effects, strategy, power-mba]

when_to_use: >
  Cuando se necesita decidir si un nuevo negocio debería ser una plataforma
  o un modelo lineal, diagnosticar el motor de valor de una plataforma
  existente, identificar dónde se atasca un lanzamiento de plataforma
  (problema huevo-y-gallina), o clasificar competencia y oportunidades en
  un sector dominado por plataformas.

when_not_to_use: >
  En modelos lineales puros donde el valor es independiente del número de
  clientes —en esos casos los conceptos de network effect, masa crítica y
  círculo virtuoso aplican débilmente o no aplican. Tampoco como única lente
  estratégica: la dinámica multi-side coexiste con consideraciones de unit
  economics (CLTV/CAC), propuesta de valor, segmentación, etc.

aku_links:
  justified_by:
    - id: aku-modelo-plataforma-concept
      link_validation: llm-proposed
      link_note: "El concepto central — sin él no hay marco."
    - id: aku-modelo-lineal-concept
      link_validation: llm-proposed
      link_note: "El contraste necesario para entender qué hace especial a una plataforma."
    - id: aku-network-effect-concept
      link_validation: llm-proposed
      link_note: "Mecanismo subyacente que explica las dinámicas virtuosa/viciosa."
    - id: aku-masa-critica-concept
      link_validation: llm-proposed
      link_note: "Umbral operativo clave del marco."
    - id: aku-circulo-virtuoso-concept
      link_validation: llm-proposed
      link_note: "Dinámica positiva tras superar masa crítica."
    - id: aku-circulo-vicioso-concept
      link_validation: llm-proposed
      link_note: "Estado por defecto pre-masa-crítica."
    - id: aku-huevo-gallina-concept
      link_validation: llm-proposed
      link_note: "El reto operativo concreto del lanzamiento."
    - id: aku-marketplace-concept
      link_validation: llm-proposed
      link_note: "Subtipo: oferta y demanda con libertad de fijación."
    - id: aku-on-demand-platform-concept
      link_validation: llm-proposed
      link_note: "Subtipo: oferta y demanda con condiciones centralizadas."
    - id: aku-content-platform-concept
      link_validation: llm-proposed
      link_note: "Subtipo: asimetría creadores/consumidores."
    - id: aku-modelo-free-concept
      link_validation: llm-proposed
      link_note: "Modelo de monetización común en plataformas con masa grande."
    - id: aku-modelo-freemium-concept
      link_validation: llm-proposed
      link_note: "Variante con capa pagada que monetiza un subconjunto de usuarios."
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

Marco que organiza los conceptos centrales del modelo de negocio de plataforma: el contraste con el modelo lineal, el network effect como motor, la masa crítica como umbral, el círculo virtuoso/vicioso como dinámicas, y el problema del huevo y la gallina como reto operativo del lanzamiento. Incluye además la taxonomía de subtipos (marketplace, on-demand, content platform) y los modelos de monetización asociados (free, freemium).

## Core Components

**Conceptos base:**
- Modelo lineal vs. modelo de plataforma (`aku-modelo-lineal-concept`, `aku-modelo-plataforma-concept`).
- Network effect (`aku-network-effect-concept`) — el valor escala con el número de usuarios.

**Dinámicas operativas:**
- Masa crítica (`aku-masa-critica-concept`) — umbral.
- Círculo virtuoso (`aku-circulo-virtuoso-concept`) — auto-refuerzo tras umbral.
- Círculo vicioso (`aku-circulo-vicioso-concept`) — estado pre-umbral.
- Huevo y gallina (`aku-huevo-gallina-concept`) — el reto de romper el círculo vicioso.

**Subtipos por libertad / control de la interacción:**
- Marketplace (`aku-marketplace-concept`) — libertad para ambos lados.
- On-demand platform (`aku-on-demand-platform-concept`) — la plataforma centraliza condiciones.
- Content platform (`aku-content-platform-concept`) — pocos creadores, muchos consumidores.

**Modelos de monetización asociados:**
- Free (`aku-modelo-free-concept`) — monetización vía publicidad.
- Freemium (`aku-modelo-freemium-concept`) — capa básica gratuita + premium pagada.

## How to Apply

1. **Clasificar primero**: ¿el modelo de negocio es lineal o plataforma? Si lineal, el resto del marco no aplica con la misma fuerza.
2. **Identificar los lados**: en una plataforma, enumerar los segmentos/lados (consumidor, vendedor, anunciante, creador…). Cada lado tiene su propia masa crítica y su propio incentivo para unirse.
3. **Diagnosticar la fase actual**: ¿la plataforma está en círculo vicioso (pre-masa-crítica) o virtuoso (post)? La fase determina la prioridad operativa.
4. **Si pre-masa-crítica**: identificar el reto huevo-y-gallina concreto y elegir mecanismo de bootstrapping (subsidio de un lado, oferta sintética, comunidad inicial cerrada, marketing unilateral).
5. **Si post-masa-crítica**: el foco pasa a mantener el círculo virtuoso (no degradar la propuesta, defender ventaja competitiva, expandir verticalmente o multi-lateralmente).
6. **Elegir subtipo y modelo de monetización**: marketplace / on-demand / content + free / freemium / comisión / suscripción según naturaleza de la interacción y volumen esperado.

## Underlying Claims

- `aku-modelo-plataforma-concept` postula que un modelo multi-side estructura el negocio de forma fundamentalmente distinta a un modelo lineal.
- `aku-network-effect-concept` es el mecanismo causal que justifica las dinámicas virtuosa y viciosa.
- `aku-huevo-gallina-concept` es el reto operativo concreto que el marco hace explícito y resoluble.

## Strengths

- Vocabulario compartido para discutir plataformas y compararlas con modelos lineales.
- Hace explícito el reto del lanzamiento (huevo-y-gallina) en lugar de tratarlo como mala suerte.
- Conecta dinámica operativa (círculos) con elección estratégica (subtipo + monetización).
- Permite predecir comportamiento competitivo (winner-takes-most en plataformas con network effect fuerte).

## Limitations and Criticisms

- **No cuantifica masa crítica**: el marco la nombra pero no ofrece un método para estimarla; eso queda como ejercicio del practitioner.
- **Subtipos no son exclusivos**: muchas plataformas reales combinan marketplace + content + on-demand (Amazon, por ejemplo). El marco trata los subtipos como categorías limpias.
- **No incluye plataformas multi-lateralidad >2 lados**: la teoría avanzada de plataformas (Hagiu, Eisenmann) modela 3+ lados, identifica «pipelines», y considera homing/multi-homing.
- **Asume network effects positivos**: no aborda network effects negativos o congestion effects que aparecen a escala.

## Variants and Extensions

- **Eisenmann/Parker/Van Alstyne — Platform Revolution**: ampliación con conceptos como pipeline-vs-platform, modular vs integrated, openness vs control, multi-homing.
- **Hagiu — Strategic decisions for multi-sided platforms**: 4 decisiones estratégicas centrales (numero de lados, diseño, precio, política).
- **Reillier — Platform Strategy**: framework operativo con 5 fases de evolución de plataforma.

## Relaciones

**justified_by** ← [[aku-modelo-plataforma-concept]] · [[aku-modelo-lineal-concept]] · [[aku-network-effect-concept]] · [[aku-masa-critica-concept]] · [[aku-circulo-virtuoso-concept]] · [[aku-circulo-vicioso-concept]] · [[aku-huevo-gallina-concept]] · [[aku-marketplace-concept]] · [[aku-on-demand-platform-concept]] · [[aku-content-platform-concept]] · [[aku-modelo-free-concept]] · [[aku-modelo-freemium-concept]]
