# -*- coding: utf-8 -*-
"""AKUs de «Negotiation Tactics» (Nick Kolenda). source-tag: kolenda. Modo maximo-exhaustivo: 1 AKU por tactica."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _audit_wire import wire
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/kolenda/negotiation-tactics-by-nick-kolenda/negotiation-tactics-by-nick-kolenda.md"
CORE = "aku-negotiation-tactics-influencia-psicologica-por-fase-concept"
CORE_STMT = ("La negociacion se gana modulando la psicologia del rival en tres fases: antes (aumenta tu poder, controla "
 "la logistica, fomenta la cooperacion), durante (construye rapport, demuestra poder, aborda los terminos, ancla tu "
 "oferta, contraoferta) y despues (cierra el trato). Cada tactica explota un sesgo concreto (anclaje, reciprocidad, "
 "reactancia, BATNA, fixed-pie, simulacion); incluye que el valor percibido y la satisfaccion del rival importan tanto "
 "como el valor economico del acuerdo.")
TPL = """---
type: aku
aku_class: {cls}
id: {slug}
statement: >
{stmt}
origin: "Nick Kolenda — Negotiation Tactics"
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
        fh.write(TPL.format(cls=cls,slug=slug,stmt=wrap(stmt),dom="kolenda, negotiation, "+dom,src=SRC))

A = [
 # --- BEFORE: increase power ---
 ("aku-reunir-datos-de-referencia-antes-de-negociar-claim","claim","preparation",
  "Antes de negociar reune datos de referencia (benchmark data): conoce el rango de mercado y el trato concreto que esperas conseguir. Sin un objetivo claro no puedes evaluar si una oferta es buena ni decidir cuando aceptar o contraofertar."),
 ("aku-mejorar-tus-batnas-antes-de-negociar-claim","claim","power,batna",
  "Antes de negociar mejora tus BATNAs (best alternative to a negotiated agreement): cuantas mas y mejores alternativas tengas, mayor es tu poder, mas atractivo eres como socio negociador, mas facil llegas a un acuerdo y mayor porcentaje del valor capturas (Malhotra & Bazerman 2008)."),
 # --- BEFORE: control logistics ---
 ("aku-elegir-un-dia-con-buen-tiempo-para-negociar-claim","claim","logistics",
  "Elige un dia con buen tiempo para negociar: el clima agradable mejora el estado de animo del rival y su disposicion cooperativa, lo que facilita las concesiones."),
 ("aku-elegir-una-hora-temprana-para-negociar-claim","claim","logistics",
  "Programa la negociacion a primera hora: el rival esta menos fatigado (menos decision fatigue) y mas fresco, lo que reduce la rigidez y favorece tu posicion; ademas una reunion temprana puede grabarse mejor en su memoria."),
 ("aku-elegir-el-medio-de-comunicacion-adecuado-claim","claim","logistics",
  "Elige el medio de comunicacion segun tu objetivo: los canales con mas riqueza social (presencial, video, voz) generan mas rapport y cooperacion, mientras que el texto (email) despersonaliza y endurece la negociacion. Elige el canal que favorezca tu estrategia."),
 # --- BEFORE: encourage cooperation ---
 ("aku-evitar-la-terminologia-de-negociacion-claim","claim","cooperation,language",
  "Evita la terminologia de negociacion (palabras como «negociar», «oferta» o «trato»): activan un marco competitivo de suma cero. Usa lenguaje cooperativo («trabajar juntos», «encontrar una solucion») para predisponer a la cooperacion."),
 ("aku-programar-una-interaccion-futura-claim","claim","cooperation",
  "Programa una interaccion futura con el rival: anticipar una relacion continuada (la sombra del futuro) activa la reputacion y la reciprocidad, reduce el comportamiento competitivo y fomenta la cooperacion."),
 ("aku-emparejar-los-nombres-en-la-invitacion-de-calendario-claim","claim","cooperation",
  "Empareja vuestros nombres en la invitacion de calendario: presentaros como una unidad crea una sensacion de equipo compartido y predispone a la cooperacion en lugar de a la confrontacion."),
 # --- DURING: build rapport ---
 ("aku-charlar-sobre-detalles-personales-antes-de-negociar-claim","claim","rapport",
  "Charla sobre detalles personales antes de entrar en materia: compartir informacion personal (schmoozing) genera rapport y confianza, y produce acuerdos mejores y mas rapidos para ambas partes."),
 ("aku-llevar-cafe-y-pasteles-a-la-negociacion-claim","claim","rapport,reciprocity",
  "Lleva cafe y pasteles a la negociacion: este favor no solicitado activa la reciprocidad (Cialdini 2006), eleva la glucosa —que reduce la agresividad (Denson et al. 2010)— y el calor fisico de la bebida aumenta la calidez interpersonal y la conducta cooperativa (Williams & Bargh 2008)."),
 ("aku-enmarcar-la-info-de-venta-como-info-de-formacion-claim","claim","rapport,reactance",
  "Enmarca cualquier informacion de venta como informacion de formacion: si el rival percibe un intento de persuadirlo aparece la reactancia psicologica y resiste (Brehm 1966). Presentar tus diapositivas como «material para nuevos empleados» evita ese marco y baja sus defensas (DeCarlo 2005)."),
 # --- DURING: demonstrate power ---
 ("aku-dar-al-rival-una-silla-baja-y-blanda-claim","claim","power,embodiment",
  "Da al rival una silla baja y blanda: el angulo ascendente al mirarte hacia arriba aumenta tu poder percibido, la postura encogida reduce el suyo (Carney et al. 2010) y la blandura ablanda su conducta —las sillas rigidas producen contraofertas mas rigidas (Ackerman et al. 2010)—."),
 ("aku-mencionar-tus-batnas-claim","claim","power,batna",
  "Menciona honestamente tus BATNAs durante la negociacion: revelar que tienes buenas alternativas te hace mas atractivo, evita que negocien agresivamente contigo y, por reciprocidad de auto-revelacion, hace que el rival tambien sea honesto sobre sus necesidades (DeRue et al. 2009; Collins & Miller 1994)."),
 ("aku-evitar-disclaimers-y-lenguaje-debil-claim","claim","power,language",
  "Elimina disclaimers y lenguaje debil («se que es mucho, pero…», «¿podrias considerar…?»): proyectan sumision y hacen que el rival negocie mas agresivamente dandote un peor trato (Van Kleef et al. 2006). Consigues mejores acuerdos siendo firme y seguro (Tiedens & Fragale 2003)."),
 ("aku-mostrar-enfado-y-decepcion-para-lograr-concesiones-claim","claim","power,emotion",
  "En fases avanzadas muestra enfado y decepcion (razonables) para lograr mayores concesiones (Van Kleef et al. 2004); ademas tu decepcion sube la performance percibida del rival, que predice su satisfaccion mejor que el valor economico (Curhan et al. 2009). Dirige el enfado a la oferta nunca a la persona, y usalo solo en relaciones de corto plazo (Kopelman et al. 2006)."),
 # --- DURING: address the terms ---
 ("aku-abordar-todos-los-terminos-relevantes-claim","claim","terms",
  "Aborda todos los terminos relevantes, no solo uno (salario): fijarse en una unica metrica activa la mentalidad de pastel fijo y obliga a ceder; listar todos los terminos (beneficios, teletrabajo, vacaciones, comisiones) hace la negociacion flexible y permite acuerdos mejores para ambas partes."),
 ("aku-ordenar-los-terminos-por-importancia-claim","claim","terms",
  "Ordena los terminos por importancia y resuelvelos todos a la vez, nunca de forma secuencial: conocer prioridades (no posiciones) revela los trade-offs integrativos (Weingart & Olekalns 2004), y agrupar todo mantiene tu poder de negociacion —cedes en lo menos importante para ganar en lo mas importante—."),
 ("aku-separar-cada-ganancia-en-componentes-individuales-claim","claim","terms,prospect-theory",
  "Separa cada ganancia en componentes individuales: por prospect theory dos ganancias separadas se sienten mejor que una sola equivalente (Kahneman & Tversky 1979). «Bajo presupuesto y a tiempo» se percibe como mas valor partido en tres beneficios distintos (Malhotra & Bazerman 2008)."),
 ("aku-mostrar-un-balance-visual-de-equidad-claim","claim","terms,fairness",
  "Muestra un balance visual de equidad: la gente valora el pago relativo (rechaza 8$ si otro recibe 10$ pero acepta 7$ a solas; Blount & Bazerman 1996). Tu lista de beneficios nunca debe parecer visualmente mas larga que la del rival."),
 # --- DURING: anchor your offer ---
 ("aku-hacer-la-primera-oferta-anclaje-claim","claim","anchoring",
  "Haz siempre la primera oferta: cada dolar mas en la primera oferta se traduce en ~50 centavos en el acuerdo final (Grant 2013). Orienta la atencion del rival hacia las mejores cualidades de tu oferta (Galinsky 2004) y dispara un anclaje que lo arrastra al extremo alto de su rango (Epley & Gilovich 2006)."),
 ("aku-pedir-un-rango-alto-y-preciso-claim","claim","anchoring",
  "Pide un rango alto y preciso: un «bolstering range» (con tu objetivo en el extremo inferior, p.ej. 80-90k para querer 80k) produce el mayor resultado (Ames & Mason 2015), y un rango preciso (81-84k) activa una regla mental fina donde cualquier movimiento se siente mas grande, por lo que el rival se aleja menos de el (Janiszewski & Uy 2008)."),
 ("aku-anadir-una-contingencia-simple-a-tu-oferta-claim","claim","anchoring,reciprocity",
  "Anade una contingencia simple a tu oferta («lo hago por 95k si hay buen paquete de beneficios»): la peticion enmarca tu oferta como un sacrificio, activa la reciprocidad y distrae al rival del compromiso instintivo a medio camino (favor request effect; Blanchard et al. 2016)."),
 ("aku-primar-la-capacidad-del-rival-de-ejecutar-el-trato-claim","claim","anchoring,simulation",
  "Prima la capacidad del rival de ejecutar el trato: las decisiones se toman por simulacion, asi que orienta su foco hacia una version mayor del recurso («¿cuanto es la facturacion anual?» en vez de mensual) para que imagine restar tu peticion de un numero grande, lo que se siente mas facil y menos doloroso."),
 # --- DURING: counter their offer ---
 ("aku-pausar-tras-su-oferta-claim","claim","countering",
  "Pausa unos segundos tras una oferta generosa antes de aceptar: tu silencio incomoda al rival y puede empujarlo a mejorar la oferta preventivamente; ademas las concesiones inmediatas se interpretan como senal de un objeto defectuoso o sobrevalorado (Kwon & Weingart 2005)."),
 ("aku-siempre-contraofertar-su-primera-oferta-claim","claim","countering",
  "Contraoferta siempre su primera oferta (sin ser codicioso): aceptarla de inmediato deja al rival arrepentido, como si hubiera cerrado un mal trato; contraofertar lo hace mas feliz con el acuerdo final (Galinsky et al. 2002). Pero nunca contraofertes por contraofertar: compara con tus benchmark data y, si la oferta iguala tu objetivo, acepta."),
 ("aku-diagnosticar-las-razones-detras-de-sus-respuestas-claim","claim","countering",
  "Diagnostica siempre las razones detras de un «no» o de sus respuestas: ¿es presupuesto, timing o performance? Identificar la causa real convierte un rechazo cerrado en un problema resoluble y te permite buscar la solucion concreta (cuando se abrira el presupuesto, que hara falta para el aumento)."),
 # --- AFTER: finalize the deal ---
 ("aku-cerrar-con-un-email-de-resumen-claim","claim","closing",
  "Cierra con un email de resumen lo antes posible: agradece la oportunidad de hablar y resume los terminos acordados para obtener prueba escrita antes de redactar el acuerdo formal."),
 ("aku-ser-el-primero-en-redactar-el-contrato-claim","claim","closing",
  "Se el primero en redactar el contrato: ademas de cerrar mas rapido, controlas los terminos —los defaults pre-escritos (duracion, penalizaciones, clausulas de terminacion) son «pegajosos» y dificiles de mover (Malhotra & Bazerman 2008)—. Hazlo siempre con transparencia."),
 # --- concepts transversales ---
 ("aku-batna-mejor-alternativa-a-un-acuerdo-negociado-concept","concept","batna",
  "El BATNA (best alternative to a negotiated agreement) es tu mejor alternativa si la negociacion fracasa; define tu poder real y tu precio de reserva. Incluye que cuantas mas y mejores alternativas tengas mas valor capturas; implica que negociar sin conocer tu BATNA es negociar a ciegas."),
 ("aku-mentalidad-de-pastel-fijo-fixed-pie-concept","concept","fixed-pie",
  "La mentalidad de pastel fijo (fixed-pie) es la creencia erronea de que el valor en una negociacion es fijo y suma cero, de modo que lo que uno gana el otro lo pierde; implica fijarse en una unica metrica y forzar concesiones mutuas. Su antidoto es ampliar el pastel abordando multiples terminos con prioridades distintas."),
]

TACTICS = [s for s,*_ in A if s not in (
 "aku-batna-mejor-alternativa-a-un-acuerdo-negociado-concept",
 "aku-mentalidad-de-pastel-fijo-fixed-pie-concept")]

def main():
    write(CORE,"concept","negotiation, marketing-psychology",CORE_STMT)
    for slug,cls,dom,stmt in A: write(slug,cls,dom,stmt)
    print(f"Escritos {len(A)+1} AKUs.")
    edges = [(s,"supports",CORE) for s,*_ in A]
    edges += [
     # BATNA concept underlies the two BATNA tactics
     ("aku-batna-mejor-alternativa-a-un-acuerdo-negociado-concept","supports","aku-mejorar-tus-batnas-antes-de-negociar-claim"),
     ("aku-batna-mejor-alternativa-a-un-acuerdo-negociado-concept","supports","aku-mencionar-tus-batnas-claim"),
     # fixed-pie: addressing all terms refines when the concept (mis)applies
     ("aku-abordar-todos-los-terminos-relevantes-claim","constrains","aku-mentalidad-de-pastel-fijo-fixed-pie-concept"),
     ("aku-ordenar-los-terminos-por-importancia-claim","related","aku-mentalidad-de-pastel-fijo-fixed-pie-concept"),
     # --- cross-corpus bridges ---
     ("aku-hacer-la-primera-oferta-anclaje-claim","supported_by","aku-anchor-principle-concept"),                       # anclaje (Hormozi/pricing)
     ("aku-hacer-la-primera-oferta-anclaje-claim","related","aku-exponer-a-cualquier-numero-alto-eleva-el-precio-de-referencia-claim"),  # anclaje (Pricing)
     ("aku-pedir-un-rango-alto-y-preciso-claim","related","aku-ser-preciso-con-precios-grandes-claim"),                 # precision numerica (Pricing)
     ("aku-pedir-un-rango-alto-y-preciso-claim","related","aku-cuando-te-meten-un-numero-en-la-cabeza-moverte-de-el-se-siente-como-perdida-claim"),  # anclaje/movimiento (50 Cent)
     ("aku-llevar-cafe-y-pasteles-a-la-negociacion-claim","supported_by","aku-cialdini-reciprocidad-concept"),         # reciprocidad
     ("aku-anadir-una-contingencia-simple-a-tu-oferta-claim","supported_by","aku-cialdini-reciprocidad-concept"),      # reciprocidad (favor request)
     ("aku-anadir-una-contingencia-simple-a-tu-oferta-claim","related","aku-pedir-de-nuevo-con-bono-reciprocidad-claim"),  # reciprocidad (50 Cent)
     ("aku-enmarcar-la-info-de-venta-como-info-de-formacion-claim","related","aku-enfatizar-la-autonomia-de-decision-but-you-are-free-claim"),  # reactancia (Copywriting)
     ("aku-primar-la-capacidad-del-rival-de-ejecutar-el-trato-claim","supported_by","aku-simulation-fluency-simulamos-resultado-menos-proceso-concept"),  # simulacion (Choice)
     ("aku-elegir-una-hora-temprana-para-negociar-claim","related","aku-colocar-la-opcion-objetivo-primera-o-ultima-claim"),  # serial position/memoria (Choice)
     ("aku-siempre-contraofertar-su-primera-oferta-claim","related","aku-nunca-te-fijes-en-un-numero-en-una-negociacion-claim"),  # benchmark vs fijacion (50 Cent)
     ("aku-reunir-datos-de-referencia-antes-de-negociar-claim","related","aku-hustlar-exige-definir-con-claridad-que-quieres-claim"),  # claridad de objetivo (50 Cent)
    ]
    wire(edges)
if __name__=="__main__": main()
