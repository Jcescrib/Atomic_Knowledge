# -*- coding: utf-8 -*-
"""AKUs de «User Experience» (Nick Kolenda). source-tag: kolenda. Modo maximo-exhaustivo.
Los 28 principios-tactica = claim AKUs + 5 guideline-concepts + CORE + 4 sub-claims con mecanismo propio.
Los ~90 sub-tips imperativos puros van en el framework TAKU (checklist), no se omiten."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _audit_wire import wire
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/kolenda/user-experience2/user-experience2.md"
CORE = "aku-ux-cinco-guidelines-de-usabilidad-concept"
CORE_STMT = ("La usabilidad de una interfaz se rige por cinco guidelines: (1) FOCUS —guiar la atencion hacia lo que "
 "importa—; (2) UNDERSTANDING —comunicar con claridad que pasa y que pasara—; (3) EFFORT —minimizar el esfuerzo "
 "cognitivo y fisico—; (4) ERRORS —prevenir errores y facilitar la recuperacion—; y (5) COMPATIBILITY —adaptarse a la "
 "habilidad, el objetivo y la situacion del usuario—. Implica que una interfaz buena no es la mas bonita sino la que "
 "reduce la carga del usuario en estas cinco dimensiones.")
TPL = """---
type: aku
aku_class: {cls}
id: {slug}
statement: >
{stmt}
origin: "Nick Kolenda — User Experience"
domain: [{dom}]

llm_confidence: 0.50

human_certainty:
  status: unvalidated
  iterations: 0
  context_boundary: ""
  validated_by: ""
  validation_date: ""
  method: ""

epistemic_type: sourced

relations:
  supported_by: []
  supports: []
  constrained_by: []
  constrains: []
  context_breaks_at: []
  breaks_context_of: []
  contradicts: []
  related: []

sources:
  - {src}

created: 2026-06-09
updated: 2026-06-09
status: active
status_note: ""
---

## Relaciones
"""
def wrap(s): return "\n".join("  " + l for l in s.strip().split("\n"))
def write(slug, cls, dom, stmt):
    with open(os.path.join(ROOT,"aku",slug+".md"),"w",encoding="utf-8",newline="\n") as fh:
        fh.write(TPL.format(cls=cls,slug=slug,stmt=wrap(stmt),dom="kolenda, ux, "+dom,src=SRC))

GUID = [
 ("aku-ux-focus-guiar-la-atencion-concept","concept","focus",
  "La guideline FOCUS consiste en guiar la atencion del usuario hacia los elementos que importan: crear un punto de entrada visual, dirigir el flujo de la mirada, agrupar lo similar, eliminar lo innecesario, comunicar las secciones ocultas y mostrar los cambios sin interrumpir."),
 ("aku-ux-understanding-comunicar-con-claridad-concept","concept","understanding",
  "La guideline UNDERSTANDING consiste en comunicar con claridad que pueden hacer y que ocurrira: indicar que es interactivo, dar feedback, comunicar en terminos relativos, ubicar al usuario, disenar para el escaneo, anticipar el resultado y cumplir las expectativas."),
 ("aku-ux-effort-minimizar-el-esfuerzo-concept","concept","effort",
  "La guideline EFFORT consiste en minimizar el esfuerzo cognitivo y fisico del usuario: simplificar la eleccion, reducir los perjuicios de la espera, evitar calculos y memoria, eliminar tareas redundantes, acercar las interacciones frecuentes y empujar hacia el objetivo."),
 ("aku-ux-errors-prevenir-y-recuperar-errores-concept","concept","errors",
  "La guideline ERRORS consiste en prevenir errores y facilitar la recuperacion: restringir las entradas invalidas, comunicar los requisitos, monitorizar senales tipicas de error, ofrecer formas faciles de deshacer/escapar y ayudar a resolver el problema."),
 ("aku-ux-compatibility-adaptarse-al-usuario-concept","concept","compatibility",
  "La guideline COMPATIBILITY consiste en adaptar la interfaz al usuario: extender las areas clicables, acomodar su habilidad/conocimiento, acomodar su objetivo/workflow y maximizar la accesibilidad para todos."),
]

A = [
 # ===== FOCUS =====
 ("aku-crear-un-punto-de-entrada-visual-claim","claim","focus",
  "Toda interfaz necesita un punto de entrada: un elemento que atraiga la mirada hacia el inicio del diseno. Se crea enfatizando el elemento mas importante y desaturando los elementos cercanos para que destaque por contraste."),
 ("aku-guiar-el-flujo-visual-de-la-mirada-claim","claim","focus",
  "Tras captar la atencion, hay que guiar el flujo visual por el diseno: oscurecer o difuminar los detalles de fondo y solapar elementos entre secciones para que la mirada fluya de una a otra en el orden deseado."),
 ("aku-agrupar-elementos-similares-por-proximidad-gestalt-claim","claim","focus,gestalt",
  "Los elementos similares deben agruparse por proximidad (principio gestalt): acercarlos, darles el mismo color o meterlos en un contenedor. Acercar los titulos a sus secciones, las etiquetas a sus campos y trocear las listas largas en secciones reduce la carga perceptiva."),
 ("aku-eliminar-elementos-innecesarios-data-ink-claim","claim","focus,data-ink",
  "Hay que eliminar los elementos innecesarios para mantener el foco en lo que importa (maximizar el data-ink ratio de Tufte): omitir instrucciones obvias, quitar adornos sin informacion y esconder los detalles perifericos en zonas expandibles."),
 ("aku-comunicar-las-secciones-ocultas-del-diseno-claim","claim","focus",
  "Hay que comunicar las secciones ocultas del diseno: indicar si existe contenido bajo el fold y transmitir profundidad con fades o sombras, para que el usuario sepa que la interfaz se extiende mas alla de lo visible."),
 ("aku-mostrar-los-cambios-sin-interrumpir-al-usuario-claim","claim","focus",
  "Hay que mostrar los cambios de la interfaz sin interrumpir al usuario: animar las transiciones para que las note, indicar que elementos han cambiado, evitar que un cambio bloquee otras funciones y avisar antes de una funcion temporizada."),
 # ===== UNDERSTANDING =====
 ("aku-indicar-que-elementos-son-interactivos-affordance-claim","claim","understanding,affordance",
  "El usuario debe saber si puede interactuar con un elemento (affordance): cambiar el cursor o el medio al pasar por encima, cambiar el propio elemento e indicar cual recibira la interaccion."),
 ("aku-dar-feedback-durante-y-tras-las-interacciones-claim","claim","understanding,feedback",
  "Hay que dar feedback durante y despues de las interacciones: indicar si una interaccion va a ser exitosa (mientras se realiza) y si ha sido exitosa (al terminar), para que el usuario sepa que ocurrio."),
 ("aku-comunicar-en-terminos-relativos-claim","claim","understanding",
  "Comunicar en terminos relativos es mas significativo que en absolutos: expresar el tiempo en relacion al presente («hace 3 min» mejor que una hora exacta) y comparar las cifras con una baseline con sentido."),
 ("aku-ayudar-al-usuario-a-ubicarse-en-la-interfaz-claim","claim","understanding",
  "Hay que ayudar al usuario a ubicarse dentro de la interfaz para que no se sienta perdido: mostrar sus pasos previos, indicar la posicion del cursor y comunicar la fase actual de una interaccion multipaso."),
 ("aku-disenar-para-el-escaneo-scannability-claim","claim","understanding,scanning",
  "Los usuarios escanean, no leen: hay que disenar para el escaneo en vez de resistirlo. Colocar la informacion importante hacia el principio e insertar la idea principal en los titulares (no esconderla en el cuerpo)."),
 ("aku-comunicar-el-resultado-esperado-de-las-interacciones-claim","claim","understanding",
  "El usuario debe saber que pasara antes de que pase: comunicar el resultado esperado de cada interaccion indicando el siguiente item de una secuencia, mostrando un preview del output, describiendo el destino de los enlaces y especificando la accion que ocurrira."),
 ("aku-cumplir-las-expectativas-del-usuario-consistencia-claim","claim","understanding,consistency",
  "Tras comunicar las expectativas correctas hay que cumplirlas: mantener consistencia entre enlaces y destinos, mostrar la esencia primaria al cargar, adherirse a un layout consistente y elegir colores semanticamente significativos (verde=ok, rojo=error)."),
 # ===== EFFORT =====
 ("aku-ayudar-al-usuario-a-elegir-opciones-choice-overload-claim","claim","effort,choice",
  "Mas opciones no son mejores (choice overload): hay que simplificar la eleccion. Sugerir un punto de partida, permitir comparar opciones por atributos, recomendar una opcion y mostrar la respuesta tipica reducen la paralisis de decision."),
 ("aku-minimizar-los-perjuicios-de-la-espera-claim","claim","effort,waiting",
  "Si el usuario debe esperar, hay que minimizar los perjuicios de la espera: reducir su arousal con colores frios, mantenerlo entretenido, alinear el downtime de la maquina con el del usuario y poblar la interfaz con placeholders mientras carga (para que la espera parezca mas corta)."),
 ("aku-minimizar-la-dependencia-de-calculo-y-memoria-claim","claim","effort,memory",
  "No hay que hacer que el usuario calcule o recuerde (reconocer es mas facil que recordar): calcular por el los items restantes, mantener visible la informacion pertinente, dejarle copiar datos, indicar que ya vio y minimizar las credenciales especificas de la interfaz."),
 ("aku-minimizar-las-tareas-redundantes-claim","claim","effort",
  "Hay que minimizar las tareas redundantes: dejar al usuario duplicar input previo («igual que la facturacion»), preservar su input al cambiar de pantalla y acelerar exponencialmente las repeticiones que detecte."),
 ("aku-acercar-las-interacciones-frecuentes-al-usuario-fitts-claim","claim","effort,fitts",
  "No todas las funciones son iguales: hay que acercar las interacciones frecuentes al usuario (ley de Fitts: cuanto mas cerca y grande el objetivo, menor el esfuerzo). Prefijar respuestas comunes, ponerlas arriba en las listas, sugerir input predicho, mantener visibles las frecuentes y esconder las infrecuentes."),
 ("aku-guiar-al-usuario-hacia-su-objetivo-claim","claim","effort",
  "Hay que empujar al usuario hacia su objetivo: nudge hacia el valor (resaltar la accion que le conviene) y arrancar el progreso por encima de cero para activar su motivacion de completarlo."),
 # ===== ERRORS =====
 ("aku-prevenir-errores-restringiendo-las-entradas-claim","claim","errors,prevention",
  "La mejor forma de gestionar errores es prevenirlos restringiendo las entradas: deshabilitar botones tras pulsarlos, ofrecer solo inputs aceptables, habilitar funciones solo cuando proceda, estructurar los campos para que encajen con el input y anadir constraints a los cambios irreversibles."),
 ("aku-comunicar-los-requisitos-de-una-interaccion-claim","claim","errors",
  "Hay que comunicar por adelantado los requisitos de una interaccion: describir el input y los parametros necesarios, poblar las unidades, ajustar el tamano de los campos al input esperado e indicar que elementos son obligatorios."),
 ("aku-monitorizar-senales-tipicas-de-error-poka-yoke-claim","claim","errors,poka-yoke",
  "Hay que monitorizar las senales tipicas de un error para cazarlo antes de que ocurra (poka-yoke): wording que contradice la intencion («adjunte» sin adjunto), envios vacios, inactividad y acciones repetidas que podrian ser no intencionadas (confirmar)."),
 ("aku-ofrecer-formas-faciles-de-deshacer-o-escapar-undo-claim","claim","errors,undo",
  "Hay que ofrecer formas faciles de revertir o escapar de un desliz: saltar confirmaciones en decisiones reversibles (un undo es mejor que un dialogo) y permitir deshacer multiples niveles de accion."),
 ("aku-ayudar-al-usuario-a-resolver-el-error-claim","claim","errors",
  "Cuando ocurre un error hay que ayudar a resolverlo: identificar el problema Y la solucion (no solo «error»), apuntar a soporte o documentacion y evitar decir «tu» en los mensajes para no culpar al usuario."),
 # ===== COMPATIBILITY =====
 ("aku-extender-las-areas-clicables-y-rutas-de-cursor-claim","claim","compatibility,fitts",
  "No hay que exigir precision: conviene extender las areas clicables y las rutas de cursor. Anadir un boton transparente alrededor de los botones pequenos, hiperenlazar todo el fondo de un item, retardar las animaciones de hover unos milisegundos y evitar que los menus colapsen durante el recorrido del cursor."),
 ("aku-adaptarse-a-la-habilidad-o-conocimiento-del-usuario-claim","claim","compatibility,onboarding",
  "Hay que adaptarse a la habilidad o conocimiento del usuario, ayudando al novato sin estorbar al experto: explicar idiomas y terminos no familiares y hacer onboarding segun la expertise (matriz de onboarding)."),
 ("aku-adaptarse-al-objetivo-o-workflow-del-usuario-claim","claim","compatibility",
  "Cada usuario trabaja distinto: hay que adaptarse a su objetivo o workflow dejandole controlar la apariencia y el orden de los elementos, posponer tareas innecesarias, ofrecer multiples vias para una misma tarea e ir directo a una ubicacion."),
 ("aku-maximizar-la-accesibilidad-de-la-interfaz-claim","claim","compatibility,accessibility",
  "Hay que maximizar la accesibilidad para que cualquier usuario pueda interactuar: categorizar los elementos con markup semantico, comunicar la informacion en multiples formatos (no solo color/sonido) y asegurar que los mensajes apliquen a todos los escenarios (formatos de fecha, plurales)."),
 # ===== promoted sub-claims (mecanismo psicologico propio) =====
 ("aku-empezar-el-progreso-por-encima-de-cero-endowed-progress-claim","claim","effort,motivation",
  "Arrancar una barra de progreso por encima de cero aumenta la probabilidad de completarla (endowed progress effect): el usuario percibe que ya ha avanzado y se siente impulsado a no perder ese progreso, mas que si empieza vacia."),
 ("aku-recomendar-una-opcion-por-defecto-claim","claim","effort,defaults",
  "Recomendar o preseleccionar una opcion por defecto reduce el esfuerzo y guia la eleccion: el usuario tiende a quedarse con el default o con la opcion marcada como «recomendada»/«mas popular» en lugar de evaluar todo el set."),
 ("aku-los-colores-frios-reducen-la-percepcion-de-espera-claim","claim","effort,color",
  "Los colores frios (azul) reducen el arousal del usuario durante una espera, haciendo que el tiempo percibido sea menor y la espera mas tolerable que con colores calidos."),
 ("aku-evitar-decir-tu-en-los-mensajes-de-error-claim","claim","errors,language",
  "Evitar la palabra «tu» en los mensajes de error reduce la sensacion de culpa del usuario: «Falta el codigo postal» se siente mejor que «Has olvidado el codigo postal», y mantiene al usuario dispuesto a corregir."),
]

def main():
    write(CORE,"concept","ux, usability, marketing-psychology",CORE_STMT)
    for slug,cls,dom,stmt in GUID: write(slug,cls,dom,stmt)
    for slug,cls,dom,stmt in A: write(slug,cls,dom,stmt)
    print(f"Escritos {len(GUID)+len(A)+1} AKUs.")
    edges = [(s,"supports",CORE) for s,*_ in GUID]
    # map each tactic to its guideline concept
    G = {
      "focus":"aku-ux-focus-guiar-la-atencion-concept",
      "understanding":"aku-ux-understanding-comunicar-con-claridad-concept",
      "effort":"aku-ux-effort-minimizar-el-esfuerzo-concept",
      "errors":"aku-ux-errors-prevenir-y-recuperar-errores-concept",
      "compatibility":"aku-ux-compatibility-adaptarse-al-usuario-concept",
    }
    for slug,cls,dom,stmt in A:
        key = dom.split(",")[0]
        edges.append((slug,"supports",G[key]))
    edges += [
     # promoted sub-claims also support their parent tactic
     ("aku-empezar-el-progreso-por-encima-de-cero-endowed-progress-claim","supports","aku-guiar-al-usuario-hacia-su-objetivo-claim"),
     ("aku-recomendar-una-opcion-por-defecto-claim","supports","aku-ayudar-al-usuario-a-elegir-opciones-choice-overload-claim"),
     ("aku-los-colores-frios-reducen-la-percepcion-de-espera-claim","supports","aku-minimizar-los-perjuicios-de-la-espera-claim"),
     ("aku-evitar-decir-tu-en-los-mensajes-de-error-claim","supports","aku-ayudar-al-usuario-a-resolver-el-error-claim"),
     # --- cross-corpus bridges ---
     ("aku-los-colores-frios-reducen-la-percepcion-de-espera-claim","related","aku-los-colores-calidos-y-saturados-estimulan-el-azul-relaja-claim"),  # color->arousal (Color)
     ("aku-cumplir-las-expectativas-del-usuario-consistencia-claim","related","aku-esquema-de-color-complementario-claim"),  # color semantico (Color)
     ("aku-ayudar-al-usuario-a-elegir-opciones-choice-overload-claim","related","aku-mostrar-el-surtido-completo-de-opciones-claim"),  # choice overload (Choice)
     ("aku-recomendar-una-opcion-por-defecto-claim","related","aku-colocar-la-opcion-objetivo-en-el-centro-claim"),  # steering choice (Choice)
     ("aku-disenar-para-el-escaneo-scannability-claim","related","aku-colocar-la-opcion-objetivo-primera-o-ultima-claim"),  # serial position (Choice)
     ("aku-crear-un-punto-de-entrada-visual-claim","related","aku-visual-attention-captamos-estimulos-de-amenaza-ancestral-concept"),  # saliencia/atencion (Visual Attention)
     ("aku-guiar-el-flujo-visual-de-la-mirada-claim","related","aku-anadir-senales-sensoriales-para-captar-atencion-claim"),  # captar atencion (Choice/Visual)
    ]
    wire(edges)
if __name__=="__main__": main()
