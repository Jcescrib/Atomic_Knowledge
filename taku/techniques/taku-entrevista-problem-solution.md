---
type: taku
taku_type: technique
id: taku-entrevista-problem-solution
title: "Entrevista Problem-Solution (validación cualitativa con potenciales clientes)"
origin: "The Power MBA — Módulo 3.0.2 «Probando modelos de negocio»"
domain: [lean-startup, customer-development, interviews, validation]

when_to_use: >
  Cuando se necesita validar en fase Problem-Solution Fit que un grupo
  identificable de clientes tiene un problema real, lo expresa, lo
  considera importante, y que la solución propuesta encaja a sus ojos.
  Especialmente útil al lanzar un producto/servicio nuevo o al pivotar
  uno existente. Es el MVP de menor coste y mayor velocidad para los
  primeros aprendizajes.

when_not_to_use: >
  Cuando ya se ha alcanzado PSF y el reto es validar canales, precio o
  unit economics (allí se usan otros MVPs: landing page, publicidad
  dirigida, A/B test). Tampoco con clientes que ya compran tu producto
  —para esos, las herramientas son retention interviews, NPS, churn
  surveys—. No sustituye experimentos cuantitativos sobre comportamiento
  agregado.

aku_links:
  justified_by:
    - id: aku-entrevista-problem-solution-concept
      link_validation: llm-proposed
      link_note: "Concepto que la técnica operacionaliza."
    - id: aku-problem-solution-fit-concept
      link_validation: llm-proposed
      link_note: "Estado objetivo que la técnica valida."
    - id: aku-customer-persona-concept
      link_validation: llm-proposed
      link_note: "El entrevistado debe encajar con la persona objetivo."
    - id: aku-mvp-concept
      link_validation: llm-proposed
      link_note: "La entrevista es un tipo de MVP."
    - id: aku-falso-positivo-validation-concept
      link_validation: llm-proposed
      link_note: "El riesgo central que la técnica debe gestionar."
  constrained_by:
    - id: aku-falso-positivo-validation-concept
      link_validation: llm-proposed
      link_note: "El falso positivo es la restricción epistémica más importante."
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
    - taku-plantilla-experimentos-mvp
  alternative_to: []
  precedes: []
  follows: []

created: 2026-06-03
updated: 2026-06-03
status: draft
status_note: ""
---

## Summary

Procedimiento estructurado para entrevistar a potenciales clientes con el objetivo de validar cuatro bloques en orden: entender quiénes son, validar el problema, validar la solución, validar el precio. La técnica está diseñada para extraer signos reales de compra (no opiniones de cortesía) y para evitar el falso positivo característico de las entrevistas mal hechas.

## When to Use

Idealmente al inicio de un proyecto nuevo o de un pivot, antes de invertir en construir nada. Útil también en cualquier momento en el que el equipo se da cuenta de que está dando por hecho cosas sobre el cliente que no ha verificado con un cliente real recientemente.

## Prerequisites

- Una hipótesis crítica clara de PSF a testar (`[[aku-hipotesis-concept]]`).
- Un perfil aproximado del entrevistado-objetivo (mejor si se tiene `[[aku-customer-persona-concept]]` ya esbozado).
- Una propuesta de valor articulada lo suficiente para describirla en una conversación.
- Disposición a escuchar respuestas que falsifiquen la hipótesis (sin la disposición, la entrevista se sesga).

## Steps

### 1. Entender al cliente

1.1 **Recopilar demográficos**: sexo, edad, educación, nivel de ingresos, ocupación. Variables que ayuden a identificar si encaja con tus segmentos.

1.2 **Preguntas adicionales de segmentación**: uso actual de productos sustitutos, visión sobre la categoría, opiniones que reflejen actitudes.

### 2. Validar el problema

2.1 **Describir el problema**: contar una historia que describa el problema (o problemas) sin meter aún tu solución.

2.2 **Validar el problema**: averiguar (a) si son conscientes del problema, (b) si les importa de verdad, (c) cómo lo expresan con sus palabras. Para cada problema por separado: «¿Qué opinas de esto?» «¿Estás de acuerdo?»

2.3 **Explorar cómo lo resuelven hoy**: averiguar si están buscando soluciones activamente, qué alternativas conocen, qué opinan de cada una. Pregunta clave: «¿Cómo abordas este problema hoy?»

### 3. Validar la solución

3.1 **Explicar o demostrar la solución**: aplicando el criterio MVP (simplemente explicarlo, folleto, landing page, mock-up). Si la presentación es rica, la solución es prematura.

3.2 **Validar los mensajes**: «¿Qué has entendido de lo que te he contado?» Si la reformulación no encaja con lo que esperabas, los mensajes están mal calibrados.

3.3 **Validar la compra**: «¿Esto es para ti?» En caso positivo, profundizar para evitar **falso positivo** (`[[aku-falso-positivo-validation-concept]]`): «¿Por qué?» «¿Para qué?» «¿Cómo te va a ayudar?» Clasificar el entusiasmo real en escala 0–10. Un 6 sin pasión es falso positivo; un 8–10 con razones concretas es signo real.

3.4 **Desglosar la propuesta de valor**: validar por separado cada componente o funcionalidad. «¿Qué es lo que más te gusta?» «Esta funcionalidad, ¿para qué te va a servir?» «¿Por qué deberíamos incluirla?» Si todas se valoran igual, el desglose no es real.

### 4. Validar precios

4.1 **Prueba de precio**: «Vamos a lanzar el producto a un precio de X, ¿qué te parece?» «¿Quieres comprarlo / hacer una reserva?» «¿Si te hacemos un 20% de descuento?» Estas tres preguntas revelan: tolerancia al precio, intención real de compra, y elasticidad al descuento. El compromiso de reserva (con o sin pago) es signo más fuerte que el «sí» verbal.

## Anti-patterns

- **Pitchear en lugar de escuchar**: la entrevista se convierte en venta. Cero aprendizaje.
- **Aceptar el «sí» genérico**: no pedir el porqué, el para qué, ni la escala de entusiasmo. Falso positivo garantizado.
- **Hacer preguntas que sugieren la respuesta**: «¿No te molesta que…?» (sí), «¿No te gustaría…?» (sí). Reformular para que la respuesta no esté insinuada.
- **Mezclar problema y solución desde el inicio**: el entrevistado adapta sus respuestas a la solución que ya conoce. Validar problema ANTES de mostrar solución.
- **Entrevistar a amigos o cualquiera**: solo cuenta entrevistar a quien encaja con el customer persona objetivo. Amigos sin perfil dan signal a cero.
- **Saltar el desglose de la propuesta**: hace que validar globalmente la solución oculte que algunas funcionalidades no aportan valor.

## Expected Outcome

Tras 5–15 entrevistas con perfiles consistentes:
- Decisión clara de si el problema es real para el segmento.
- Lista priorizada de los componentes de la propuesta de valor que más resuenan vs los que no.
- Sensación cualitativa robusta de si compradores potenciales pagarían el precio.
- Vocabulario del cliente para mensajes y copy.
- Lista de pivots candidatos si las hipótesis fallan.

## Failure Signals

- Todos los entrevistados dicen sí a todo y no muestran entusiasmo real. → Falso positivo masivo; revisar la técnica.
- Los entrevistados no reconocen el problema o lo trivializan. → El problema no existe en ese segmento (pivot o cambio de segmento).
- El precio anticipado es 5× menor que la disposición observada. → Replantear modelo económico antes de seguir.
- Las respuestas se contradicen entre entrevistas sin patrón. → El segmento no es homogéneo; re-segmentar.

## Underlying Logic

Funciona porque [[aku-aprender-clientes-reales-claim]] establece que el único aprendizaje válido en fase de innovación viene de clientes reales, y [[aku-no-dar-supuesto-hipotesis-claim]] que las hipótesis críticas deben validarse antes de construir. La entrevista es el MVP de menor coste (`[[aku-mvp-concept]]`) que cubre estas dos restricciones. La estructura en 4 bloques con desglose y validación de entusiasmo es la salvaguarda contra [[aku-falso-positivo-validation-concept]].

## Notes and Variants

- **The Mom Test (Rob Fitzpatrick)**: complemento que afina aún más la formulación de preguntas para evitar elogios de cortesía. Lectura recomendada antes de aplicar la técnica.
- **Validation Board (Lean Startup Machine)**: plantilla visual que organiza varias entrevistas en una matriz de hipótesis testadas.
- **Customer Discovery (Steve Blank)**: variante más exhaustiva con cuatro fases (customer discovery → validation → creation → company building).
- **Tipos de entrevistador**: para reducir el sesgo de complacencia, mejor que entreviste alguien que el entrevistado no asocie con el éxito del proyecto (no el fundador soñador con el producto).

## Relaciones

**justified_by** ← [[aku-entrevista-problem-solution-concept]] · [[aku-problem-solution-fit-concept]] · [[aku-customer-persona-concept]] · [[aku-mvp-concept]] · [[aku-falso-positivo-validation-concept]]

**constrained_by** ← [[aku-falso-positivo-validation-concept]]

**complementary** ↔ [[taku-plantilla-experimentos-mvp]]
