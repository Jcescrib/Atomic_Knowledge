---
type: taku
taku_type: framework
id: taku-checklist-usabilidad-ux-5-guidelines
title: "Checklist de usabilidad UX (5 guidelines de Kolenda)"
origin: "Nick Kolenda — User Experience: A Guide for Marketers and Designers"
domain: [ux, usability, interface-design, marketing-psychology]

when_to_use: "Al diseñar o auditar la usabilidad de una interfaz (web, app, software): recorrer las cinco guidelines y sus tácticas como checklist de revisión."
when_not_to_use: "Para optimizar la persuasión/conversión (objetivo distinto de la usabilidad) o para decisiones de marca/contenido; este checklist cubre usabilidad, no persuasión."

aku_links:
  justified_by:
    - id: aku-ux-focus-guiar-la-atencion-concept
      link_validation: llm-proposed
      link_note: "Guideline 1."
    - id: aku-ux-understanding-comunicar-con-claridad-concept
      link_validation: llm-proposed
      link_note: "Guideline 2."
    - id: aku-ux-effort-minimizar-el-esfuerzo-concept
      link_validation: llm-proposed
      link_note: "Guideline 3."
    - id: aku-ux-errors-prevenir-y-recuperar-errores-concept
      link_validation: llm-proposed
      link_note: "Guideline 4."
    - id: aku-ux-compatibility-adaptarse-al-usuario-concept
      link_validation: llm-proposed
      link_note: "Guideline 5."
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

created: 2026-06-09
updated: 2026-06-09
status: draft
status_note: ""
---

## Summary

Checklist operativo de usabilidad organizado en cinco guidelines, cada una con sus tácticas principales (modeladas como AKUs) y sus sub-tips de implementación (recogidos aquí). Cubre el detalle imperativo de «qué hacer» en la interfaz; el «por qué» está en los AKUs enlazados.

## Core Components

Las cinco guidelines: **FOCUS** (atención), **UNDERSTANDING** (claridad), **EFFORT** (esfuerzo), **ERRORS** (errores), **COMPATIBILITY** (adaptación). Ver `aku_links.justified_by`.

## How to Apply

Recorrer cada guideline marcando sus tácticas y sub-tips:

**1. FOCUS**
- Crear un punto de entrada: enfatizar el elemento más importante · desaturar los elementos cercanos al punto de entrada.
- Guiar el flujo visual: oscurecer los detalles de fondo · solapar elementos entre secciones.
- Agrupar elementos similares: acercar titulares a sus secciones · mantener etiquetas junto a sus campos · agrupar por proximidad · trocear listas largas · distinguir funciones potentes para minimizar slips.
- Eliminar lo innecesario: omitir instrucciones obvias · maximizar el data-ink ratio · esconder detalles periféricos en expandibles.
- Comunicar secciones ocultas: indicar contenido bajo el fold · transmitir profundidad con fades/sombras.
- Mostrar cambios sin interrumpir: animar los cambios · prevenir que un cambio bloquee otras funciones · indicar qué cambió · avisar de funciones temporizadas.

**2. UNDERSTANDING**
- Indicar qué es interactivo: cambiar el cursor o medio · cambiar el elemento · indicar cuál recibirá la interacción.
- Dar feedback: si la interacción será exitosa · si fue exitosa.
- Comunicar en términos relativos: tiempo relativo al presente · comparar cifras con una baseline.
- Ayudar a ubicarse: mostrar pasos previos · indicar posición del cursor · comunicar la fase actual.
- Diseñar para el escaneo: info importante al principio · idea principal en titulares.
- Comunicar el resultado esperado: siguiente ítem de una secuencia · nº de ítems del grupo · preview del output · destino de los enlaces · acción que ocurrirá.
- Cumplir expectativas: consistencia enlace-destino · esencia primaria al cargar · layout consistente · colores semánticamente significativos.

**3. EFFORT**
- Ayudar a elegir: sugerir punto de partida · comparar por atributos · recomendar una opción · mostrar la respuesta típica.
- Minimizar la espera: colores fríos · mantener entretenido · alinear downtime máquina/usuario · placeholders al cargar.
- Minimizar cálculo y memoria: calcular ítems restantes · mantener info visible · dejar copiar · indicar ya visto · minimizar credenciales propias.
- Minimizar tareas redundantes: duplicar input previo · preservar input al cambiar · acelerar repeticiones.
- Acercar interacciones frecuentes (Fitts): opciones visibles en sets pequeños · prefijar respuestas comunes · comunes arriba en listas · sugerir input predicho · info pertinente junto a la interacción · frecuentes visibles · infrecuentes ocultas.
- Guiar hacia el objetivo: nudge hacia el valor · empezar el progreso por encima de cero.

**4. ERRORS**
- Prevenir restringiendo: deshabilitar botones tras pulsar · solo inputs aceptables · habilitar funciones solo si procede · estructurar campos al input · constraints en cambios irreversibles.
- Comunicar requisitos: describir input · describir parámetros · poblar unidades · ajustar tamaño de campo · indicar campos obligatorios.
- Monitorizar señales de error: wording que contradice la intención · envíos vacíos · inactividad · confirmar acciones repetidas.
- Deshacer/escapar: saltar confirmaciones reversibles · undo multinivel.
- Ayudar a resolver: identificar problema y solución · apuntar a soporte/documentación · evitar decir «tú».

**5. COMPATIBILITY**
- Extender áreas clicables: retardar hover unos ms · botón transparente en botones pequeños · hiperenlazar todo el fondo · menús que no colapsen en el recorrido.
- Acomodar habilidad/conocimiento: explicar idiomas no familiares · explicar términos no familiares · onboarding por expertise.
- Acomodar objetivo/workflow: controlar apariencia · controlar orden · posponer tareas · múltiples vías · ir directo a una ubicación.
- Maximizar accesibilidad: markup semántico · información en múltiples formatos · mensajes válidos en todos los escenarios.

## Underlying Claims

Cada táctica principal está respaldada por un claim-AKU propio (ver el cluster `kolenda, ux`); las guidelines son los cinco concept-AKUs enlazados en `justified_by`.

## Strengths

- Exhaustivo y accionable: convierte la usabilidad en una lista de verificación concreta.
- Separa el «qué hacer» (este checklist) del «por qué funciona» (los AKUs), sin perder ninguno.

## Limitations and Criticisms

- Es usabilidad, no persuasión ni conversión.
- Algunas tácticas son convenciones de diseño sin evidencia experimental fuerte.
- La priorización entre tácticas depende del contexto del producto.

## Variants and Extensions

- Combinar con los heurísticos de Nielsen para auditorías formales.
- Para e-commerce, complementar con el cluster `kolenda, ecommerce` (CRO).

## Relaciones

**justified_by** ← [[aku-ux-focus-guiar-la-atencion-concept]] · [[aku-ux-understanding-comunicar-con-claridad-concept]] · [[aku-ux-effort-minimizar-el-esfuerzo-concept]] · [[aku-ux-errors-prevenir-y-recuperar-errores-concept]] · [[aku-ux-compatibility-adaptarse-al-usuario-concept]]
