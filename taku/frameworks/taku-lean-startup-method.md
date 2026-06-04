---
type: taku
taku_type: framework
id: taku-lean-startup-method
title: "Método Lean Startup (Eric Ries)"
origin: "Eric Ries 2011 «The Lean Startup»; resumido en The Power MBA — Módulo 3.0.1"
domain: [lean-startup, methodology, startup, innovation, power-mba]

when_to_use: >
  Cuando se afronta cualquier proyecto con grado de innovación o
  incertidumbre y se quiere minimizar el riesgo de fracasar invirtiendo lo
  mínimo posible hasta validar las hipótesis críticas. Aplicable desde
  decisiones pequeñas (probar una nueva línea de producto) hasta crear una
  empresa desde cero. Especialmente útil antes de haber alcanzado
  product-market fit.

when_not_to_use: >
  En contextos de baja incertidumbre donde el mercado, los clientes y la
  propuesta están establecidos (`aku-innovar-vs-competir-concept` lado
  «competir»). Allí la gestión tradicional —plan de negocio, estudio de
  mercado, ventaja competitiva, segmentación— es la herramienta correcta.
  Tampoco aplica una vez alcanzado el PMF; en fase de escalado la lógica
  cambia hacia eficiencia operativa y crecimiento.

aku_links:
  justified_by:
    - id: aku-lean-startup-method-concept
      link_validation: llm-proposed
      link_note: "El concepto meta que el framework operacionaliza."
    - id: aku-innovar-vs-competir-concept
      link_validation: llm-proposed
      link_note: "Define cuándo aplica el marco vs cuándo no."
    - id: aku-build-measure-learn-concept
      link_validation: llm-proposed
      link_note: "El ciclo iterativo central."
    - id: aku-hipotesis-concept
      link_validation: llm-proposed
      link_note: "Paso explícito antes del MVP."
    - id: aku-mvp-concept
      link_validation: llm-proposed
      link_note: "Vehículo del experimento."
    - id: aku-aprendizaje-validado-concept
      link_validation: llm-proposed
      link_note: "Output del ciclo y única medida real de progreso."
    - id: aku-product-market-fit-concept
      link_validation: llm-proposed
      link_note: "Objetivo de la fase de innovación."
    - id: aku-metricas-accionables-concept
      link_validation: llm-proposed
      link_note: "Las métricas que importan en esta fase."
    - id: aku-metricas-vanidosas-concept
      link_validation: llm-proposed
      link_note: "Las que NO importan en esta fase — contraste explícito."
    - id: aku-asumir-equivocarse-claim
      link_validation: llm-proposed
      link_note: "Disposición epistémica central."
    - id: aku-aprender-clientes-reales-claim
      link_validation: llm-proposed
      link_note: "Restricción epistémica sobre la fuente del aprendizaje."
    - id: aku-no-dar-supuesto-hipotesis-claim
      link_validation: llm-proposed
      link_note: "Anti-patrón estructural que el marco previene."
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
  precedes:
    - id: taku-blitzscaling
      sequence_type: recommended
  follows: []

created: 2026-06-03
updated: 2026-06-03
status: draft
status_note: ""
---

## Summary

Metodología sistemática para afrontar proyectos de innovación con alta incertidumbre. Reemplaza el plan-de-negocio detallado por ciclos cortos de hipótesis→MVP→aprendizaje validado. El objetivo no es ejecutar un plan sino descubrir el modelo de negocio que funciona —el plan emerge del aprendizaje, no al revés—.

## Core Components

| Componente | AKU |
|---|---|
| Cuándo aplica (diagnóstico de contexto) | `aku-innovar-vs-competir-concept` |
| Ciclo central | `aku-build-measure-learn-concept` |
| Punto de partida de cada vuelta | `aku-hipotesis-concept` |
| Vehículo del experimento | `aku-mvp-concept` (+ `aku-mago-de-oz-mvp-concept` como caso especial) |
| Output del ciclo | `aku-aprendizaje-validado-concept` |
| Objetivo | `aku-product-market-fit-concept` |
| Métricas correctas en esta fase | `aku-metricas-accionables-concept` |
| Anti-métricas | `aku-metricas-vanidosas-concept` |

Tres claims estructurales:
- `aku-asumir-equivocarse-claim` — disposición epistémica.
- `aku-aprender-clientes-reales-claim` — única fuente válida de aprendizaje.
- `aku-no-dar-supuesto-hipotesis-claim` — anti-patrón a evitar.

## How to Apply

1. **Verificar el contexto**: ¿alta incertidumbre? Sí → aplicar Lean Startup. No → gestión tradicional.
2. **Identificar todas las hipótesis implícitas** en la idea: comportamiento del cliente, costes, ingresos, canales, retención, etc.
3. **Priorizar hipótesis críticas**: aquellas cuyo fracaso colapsaría el modelo entero. Testar primero las críticas.
4. **Diseñar el MVP** que mejor valide la hipótesis crítica del momento, optimizando coste/tiempo del experimento (no completitud del producto). Considerar formatos: entrevista problema-solución, landing page, test de humo, Mago de Oz, crowdfunding, lista de espera, publicidad dirigida.
5. **Construir el MVP** y exponerlo a clientes reales.
6. **Medir el comportamiento** con métricas accionables (conversión, retención, CAC, CLTV, NPS) — NO vanity metrics.
7. **Aprender**: ¿la hipótesis se confirma, se falsifica o se refina? Documentar el aprendizaje.
8. **Iterar**: si la hipótesis falla, pivotar (cambiar de hipótesis); si se confirma, abordar la siguiente hipótesis crítica. Repetir hasta PMF.
9. **Una vez en PMF**: la lógica cambia. Se sale del marco Lean Startup y se entra en escalado.

## Underlying Claims

- `aku-asumir-equivocarse-claim` — sin esta disposición, el método no se aplica de verdad.
- `aku-aprender-clientes-reales-claim` — sin esta restricción, el aprendizaje es ruido (consejo de expertos, opiniones).
- `aku-no-dar-supuesto-hipotesis-claim` — sin esta vigilancia, el método se reduce a teatro (rellenar plantillas sin validar nada).

## Strengths

- Universal: se adapta desde decisiones pequeñas hasta crear empresas.
- Compresión radical del coste de descubrimiento: validar una hipótesis crítica en semanas vs meses.
- Explicita el contexto donde aplica (alta incertidumbre) y donde no, evitando aplicarlo por defecto.
- Genera disciplina epistémica: distingue aprendizaje validado de opinión.
- Conecta con unit economics: las métricas accionables son las mismas que las métricas de unit economics (CLTV, CAC, churn).

## Limitations and Criticisms

- **Sesgo de supervivencia**: los casos célebres (Dropbox, Airbnb, Zappos) son éxitos retrospectivos; el marco no documenta los fracasos a pesar de aplicarlo.
- **Pivotitis**: la facilidad de pivotar puede convertirse en zigzag perpetuo sin convicción suficiente para profundizar.
- **No-aplicable a todo**: en hardware, biotech, infraestructura, regulado, los ciclos no se pueden comprimir a semanas; el marco requiere adaptación.
- **El aprendizaje validado se sobre-mistifica**: a veces el problema no es falta de aprendizaje sino falta de capacidad para ejecutar lo que el aprendizaje señala.
- **Cuesta romper con cultura plan-de-negocio**: en entornos corporativos o subvencionados se exige business plan a 5 años, lo que entra en tensión con el marco.

## Variants and Extensions

- **Customer Development (Steve Blank)**: complemento operativo enfocado en las primeras 4 fases del customer journey (customer discovery, validation, creation, company building).
- **Running Lean (Ash Maurya)**: aplicación práctica con Lean Canvas como plantilla central.
- **The Mom Test (Rob Fitzpatrick)**: técnica específica para las entrevistas problema-solución que evita el sesgo de complacencia.
- **Design Sprint (Knapp et al., Google Ventures)**: variante comprimida en 5 días para resolver una hipótesis crítica con prototipado rápido.

## Relaciones

**justified_by** ← [[aku-lean-startup-method-concept]] · [[aku-innovar-vs-competir-concept]] · [[aku-build-measure-learn-concept]] · [[aku-hipotesis-concept]] · [[aku-mvp-concept]] · [[aku-aprendizaje-validado-concept]] · [[aku-product-market-fit-concept]] · [[aku-metricas-accionables-concept]] · [[aku-metricas-vanidosas-concept]] · [[aku-asumir-equivocarse-claim]] · [[aku-aprender-clientes-reales-claim]] · [[aku-no-dar-supuesto-hipotesis-claim]]

**precedes** → [[taku-blitzscaling]]
