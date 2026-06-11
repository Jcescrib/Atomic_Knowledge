---
type: taku
taku_type: framework
id: taku-business-model-canvas
title: "Business Model Canvas (BMC)"
origin: "The Power MBA — Módulo 2.1 «Análisis de un modelo de negocio: Innovación BMC»"
domain: [business-model, strategy, framework, bmc, power-mba]

when_to_use: >
  Cuando se necesita describir, analizar o diseñar un modelo de negocio
  como sistema completo en un único cuadro: tanto para auditar un modelo
  existente (¿qué bloques son débiles? ¿qué dependencias no están
  resueltas?) como para diseñar uno nuevo (¿qué orden seguir para definir
  los 9 bloques de forma coherente?). Útil también como base común para
  comparar varios modelos de negocio del mismo sector o para detectar
  innovaciones de modelo.

when_not_to_use: >
  Cuando lo que se necesita es analizar la dinámica temporal del modelo
  (cómo evoluciona, en qué fase del ciclo está) o el contexto competitivo
  (sector, regulación, competidores), porque el BMC los excluye
  estructuralmente. Tampoco es la herramienta para diseñar productos
  individuales —su unidad de análisis es el modelo de negocio completo—
  ni para planes operativos a corto plazo.

aku_links:
  justified_by:
    - id: aku-bmc-concept
      link_validation: llm-proposed
      link_note: "El framework mismo — define los 9 bloques y su interdependencia."
    - id: aku-segmentos-de-clientes-concept
      link_validation: llm-proposed
      link_note: "Bloque cliente; punto de partida lógico para rellenar el canvas."
    - id: aku-propuesta-de-valor-concept
      link_validation: llm-proposed
      link_note: "Bloque oferta; bisagra entre el lado cliente y el lado infraestructura."
    - id: aku-canales-de-distribucion-concept
      link_validation: llm-proposed
      link_note: "Bloque cliente — medio de entrega de valor."
    - id: aku-canal-directo-concept
      link_validation: llm-proposed
      link_note: "Sub-concepto del bloque canales; trade-off margen/control vs alcance."
    - id: aku-canal-indirecto-concept
      link_validation: llm-proposed
      link_note: "Sub-concepto del bloque canales; trade-off complementario al directo."
    - id: aku-relaciones-con-clientes-concept
      link_validation: llm-proposed
      link_note: "Bloque cliente — tipo de relación sostenida post-captación."
    - id: aku-flujos-de-ingresos-concept
      link_validation: llm-proposed
      link_note: "Bloque financiero — cómo el modelo cobra a cada segmento."
    - id: aku-recursos-clave-concept
      link_validation: llm-proposed
      link_note: "Bloque infraestructura — activos necesarios para entregar la propuesta."
    - id: aku-actividades-clave-concept
      link_validation: llm-proposed
      link_note: "Bloque infraestructura — procesos operativos."
    - id: aku-ecosistema-alianzas-concept
      link_validation: llm-proposed
      link_note: "Bloque infraestructura — socios externos que extienden el modelo."
    - id: aku-estructura-de-costes-concept
      link_validation: llm-proposed
      link_note: "Bloque financiero — deriva de recursos clave y actividades clave."
    - id: aku-segmento-relevante-claim
      link_validation: llm-proposed
      link_note: "Regla metodológica para aplicar el bloque segmentos sin sobre-fragmentar."
    - id: aku-coste-prioridad-segun-estrategia-claim
      link_validation: llm-proposed
      link_note: "Claim estratégico que prioriza (o no) la gestión del bloque costes."
    - id: aku-value-equation-concept
      link_validation: llm-proposed
      link_note: "deducible: corrobora aku-propuesta-de-valor-concept desde [hormozi] (cross-source)"
    - id: aku-ltgp-concept
      link_validation: llm-proposed
      link_note: "deducible: corrobora aku-flujos-de-ingresos-concept desde [hormozi] (cross-source)"
    - id: aku-bonos-terceros-revenue-streams-claim
      link_validation: llm-proposed
      link_note: "deducible: corrobora aku-flujos-de-ingresos-concept desde [hormozi] (cross-source)"
    - id: aku-bonos-de-terceros-claim
      link_validation: llm-proposed
      link_note: "deducible: corrobora aku-ecosistema-alianzas-concept desde [hormozi] (cross-source)"
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

Cuadro visual de 9 bloques que describe un modelo de negocio completo en una sola página. Originado por Alexander Osterwalder y popularizado por su libro «Business Model Generation», el BMC se ha convertido en el estándar de facto para diagnosticar, comparar y diseñar modelos de negocio. Su valor está en forzar una mirada sistémica: cada bloque solo tiene sentido en relación con los otros 8.

## Core Components

Los 9 bloques agrupados en cuatro áreas:

| Área | Bloque | AKU | Pregunta clave |
|---|---|---|---|
| **Cliente** | Segmentos de clientes | `aku-segmentos-de-clientes-concept` | ¿A quién creamos valor? |
| **Cliente** | Canales de distribución | `aku-canales-de-distribucion-concept` | ¿Cómo entregamos valor? |
| **Cliente** | Relaciones con los clientes | `aku-relaciones-con-clientes-concept` | ¿Qué relación mantenemos? |
| **Oferta** | Propuesta de valor | `aku-propuesta-de-valor-concept` | ¿Qué ofrecemos? |
| **Infraestructura** | Actividades clave | `aku-actividades-clave-concept` | ¿Qué hacemos para entregar valor? |
| **Infraestructura** | Recursos clave | `aku-recursos-clave-concept` | ¿Qué necesitamos tener? |
| **Infraestructura** | Ecosistema de alianzas | `aku-ecosistema-alianzas-concept` | ¿En quién nos apoyamos? |
| **Financiero** | Flujos de ingresos | `aku-flujos-de-ingresos-concept` | ¿Cómo monetizamos? |
| **Financiero** | Estructura de costes | `aku-estructura-de-costes-concept` | ¿Cuánto cuesta operar? |

Cada bloque del lado izquierdo (infraestructura) deriva su prioridad del lado derecho (cliente + propuesta de valor): no se eligen actividades, recursos, alianzas o costes en abstracto, sino en función de qué exige entregar la propuesta de valor a los segmentos elegidos. Esa direccionalidad es estructural al framework.

## How to Apply

Orden recomendado para rellenar el canvas (puede iterarse varias veces):

1. **Segmentos de clientes** primero. Sin claridad de a quién se sirve, los demás bloques son aire. Aplicar la regla del `aku-segmento-relevante-claim`: no inventar segmentos sin diferencia operativa.
2. **Propuesta de valor** por cada segmento. Articularla en una de las dos formas válidas: oferta concreta de productos/servicios, o descripción de los valores/beneficios entregados.
3. **Canales** y **relaciones con los clientes** por cada segmento — cómo se llega y cómo se mantiene la relación.
4. **Flujos de ingresos** por cada segmento — cómo paga, con qué cadencia, qué estructura (fija/variable, estable/estacional).
5. **Actividades clave** y **recursos clave** derivados de lo necesario para entregar la propuesta de valor.
6. **Ecosistema de alianzas** para identificar qué se externaliza y por qué.
7. **Estructura de costes** como derivada de los recursos y actividades clave. Aplicar el `aku-coste-prioridad-segun-estrategia-claim` para definir prioridad.
8. Iterar revisando coherencia entre bloques (cada cambio desplaza al menos otros dos).

## Underlying Claims

El framework descansa en:

- **El claim sistémico** (`aku-bmc-concept` implícito en su definición): un modelo de negocio se puede analizar exhaustivamente con 9 bloques interdependientes.
- **Direccionalidad cliente → infraestructura**: el lado derecho del canvas (cliente, propuesta de valor, financiero) condiciona el lado izquierdo (operaciones, recursos, alianzas, costes).
- `aku-segmento-relevante-claim` — regla metodológica que evita el error más común al rellenar el bloque segmentos.
- `aku-coste-prioridad-segun-estrategia-claim` — claim estratégico que prioriza la gestión del bloque costes según la estrategia genérica elegida.

## Strengths

- Una página, vista completa: facilita comparación, conversación y revisión rápidas.
- Forzar coherencia sistémica: no se puede definir un bloque en aislamiento.
- Lenguaje compartido: el vocabulario BMC es estándar entre emprendedores, inversores y consultores.
- Adaptable a innovar: cambiar un bloque (e.g., flujos de ingresos de venta a suscripción) ilumina qué otros bloques exige re-pensar.

## Limitations and Criticisms

- **Estático**: el BMC no captura cómo el modelo evoluciona en el tiempo, en qué fase del ciclo está, ni cómo responder a cambios del entorno.
- **No incluye competencia ni regulación**: el contexto competitivo y regulatorio queda fuera; requiere complementarse con frameworks como las Cinco Fuerzas o análisis PESTLE.
- **Sin métricas**: el BMC describe pero no mide; tampoco prioriza qué bloque atender primero más allá de la heurística estratégica del `aku-coste-prioridad-segun-estrategia-claim`.
- **Riesgo de plantilla**: rellenar los 9 bloques puede caer en cosmética si no se cuestiona la coherencia entre ellos.
- **Granularidad cliente** insuficiente: para entender al cliente en profundidad suele necesitarse complementar con Value Proposition Canvas (Osterwalder posterior).

## Variants and Extensions

- **Lean Canvas** (Ash Maurya): adaptación del BMC para startups en fase de descubrimiento; reemplaza algunos bloques (alianzas → problema; relaciones → solución) y prioriza incertidumbre vs corporativo establecido.
- **Value Proposition Canvas**: zoom-in al bloque propuesta de valor + bloque segmentos, con jobs-to-be-done, pains y gains.
- **Business Model Navigator** (Gassmann): 55 patrones de modelos de negocio como cartas de innovación.
- **Versiones por canal de adquisición / por producto / multi-sided**: aplicar BMC distintos para cada lado de una plataforma o cada combinación producto-segmento.

## Relaciones

**justified_by** ← [[aku-bmc-concept]] · [[aku-segmentos-de-clientes-concept]] · [[aku-propuesta-de-valor-concept]] · [[aku-canales-de-distribucion-concept]] · [[aku-canal-directo-concept]] · [[aku-canal-indirecto-concept]] · [[aku-relaciones-con-clientes-concept]] · [[aku-flujos-de-ingresos-concept]] · [[aku-recursos-clave-concept]] · [[aku-actividades-clave-concept]] · [[aku-ecosistema-alianzas-concept]] · [[aku-estructura-de-costes-concept]] · [[aku-segmento-relevante-claim]] · [[aku-coste-prioridad-segun-estrategia-claim]] · [[aku-value-equation-concept]] · [[aku-ltgp-concept]] · [[aku-bonos-terceros-revenue-streams-claim]] · [[aku-bonos-de-terceros-claim]]
