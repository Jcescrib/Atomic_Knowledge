# -*- coding: utf-8 -*-
"""AKUs de «Advertising Psychology» (Nick Kolenda) — modo máximo-exhaustivo. source-tag: kolenda."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _audit_wire import wire
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/kolenda/ad-psychology2/ad-psychology2.md"
CORE = "aku-advertising-psychology-captar-atencion-facilitar-simulacion-y-ser-recordado-concept"
CORE_STMT = ("La publicidad eficaz combina tres objetivos psicologicos —captar la atencion, facilitar la simulacion "
 "mental de comprar/usar el producto, y ser recordada despues— modulando contenido, color, palabras, personas, "
 "framing, medios y timing. Incluye apoyarse en la neuroanatomia, la fluidez y la activacion de dominios "
 "semanticos; excluye depender solo de la repeticion bruta; implica que detalles de diseno y de eleccion de "
 "medio/momento mueven la respuesta tanto como el mensaje.")
TPL = """---
type: aku
aku_class: {cls}
id: {slug}
statement: >
{stmt}
origin: "Nick Kolenda — Advertising Psychology"
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
def write(slug, dom, stmt):
    with open(os.path.join(ROOT,"aku",slug+".md"),"w",encoding="utf-8",newline="\n") as fh:
        fh.write(TPL.format(cls="claim",slug=slug,stmt=wrap(stmt),dom="kolenda, advertising, "+dom,src=SRC))
A = [
 ("aku-posicionar-las-imagenes-a-la-izquierda-del-anuncio-claim","images","Posiciona las imagenes a la izquierda del anuncio: el hemisferio derecho (mejor para lo pictorico) procesa el campo visual izquierdo, asi que poner la imagen a la izquierda del texto mejora el procesamiento del mensaje (Grobelny & Michalski 2015)."),
 ("aku-insertar-un-bloqueo-a-la-derecha-del-anuncio-claim","images","Inserta un bloqueo a la derecha del anuncio: como leemos de izquierda a derecha, los ojos entran por la izquierda y se mueven a la derecha; una persona/objeto que mire hacia dentro o bloquee la salida por la derecha impide que la mirada escape y la dirige hacia el producto (Park et al. 2018, reinterpretado por Kolenda)."),
 ("aku-inmersar-al-espectador-en-perspectiva-de-primera-persona-claim","images","Inmersa al espectador en una perspectiva en primera persona (POV): facilita la simulacion mental de usar el producto (como hace Peloton con planos POV), y esa facilidad se malinterpreta como deseo de compra."),
 ("aku-asociar-el-producto-a-un-trigger-cotidiano-claim","images","Asocia el producto a una experiencia/trigger cotidiana para que el espectador lo recuerde despues: cuando vuelva a vivir esa experiencia (p.ej. la desgana matinal de levantarse a hacer ejercicio), se le activara el recuerdo del anuncio."),
 ("aku-anadir-elementos-de-la-atencion-top-down-del-espectador-claim","images","Atraviesa la atencion top-down insertando una clave que el espectador esta monitoreando activamente: quien ignora un anuncio mientras espera que vuelva su serie giro la cabeza al oir la voz de un actor de esa serie metida en el spot (Kolenda)."),
 ("aku-retratar-el-problema-en-escala-de-grises-contrast-fluency-claim","color","Retrata el «problema» en escala de grises y la «solucion» en color (los infomerciales): el contraste visual se confunde con un contraste semantico —«si se ven muy distintos, el producto marca una gran diferencia»— (contrast fluency)."),
 ("aku-reducir-el-color-en-anuncios-llenos-de-texto-claim","color","Reduce el color (p.ej. el brillo) en anuncios con mucho texto: cuando el espectador se siente abrumado y no puede escrutar el anuncio, el blanco y negro persuade mas (Meyers-Levy & Peracchio 1995)."),
 ("aku-reducir-el-color-para-eventos-distantes-en-el-tiempo-claim","color","Reduce el color para eventos distantes en el tiempo: visualizamos el futuro lejano en escala de grises, asi que los anuncios en grises rinden mas para compras a futuro y los de color para compras inminentes (Lee, Fujita, Deng & Unnava 2017)."),
 ("aku-agrandar-las-palabras-emocionales-claim","words","Agranda las palabras emocionales: las imagenes grandes son mas emocionales (los ancestros juzgaban la amenaza por el tamano/cercania), las palabras heredaron ese efecto, y ademas el texto grande capta mas atencion (Bayer, Sommer & Schacht 2012; Pieters & Wedel 2004)."),
 ("aku-rimar-el-eslogan-o-la-llamada-a-la-accion-claim","words","Rima tu eslogan o CTA (rhyme-as-reason): «what sobriety conceals, alcohol reveals» se percibio mas veraz que la version sin rima, porque la rima produce una sensacion agradable que se malatribuye a la veracidad del mensaje (McGlone & Tofighbakhsh 2000)."),
 ("aku-mover-el-logo-en-las-variaciones-del-anuncio-claim","people","Crea variaciones del anuncio y mueve el logo de sitio: las exposiciones posteriores fuerzan a recuperar el anuncio original de memoria (la recuperacion fortalece el recuerdo), y mover el logo capta mas atencion porque «algo se siente distinto» (Appleton-Knapp et al. 2005; Shapiro & Nielson 2013)."),
 ("aku-elegir-modelos-que-se-parezcan-a-cada-segmento-claim","people","Elige modelos que se parezcan a cada segmento: cuando el anuncio coincide con una dimension saliente del yo del espectador, este se auto-referencia, lo que genera pensamientos, actitudes e intencion de compra mas favorables (Lee, Fernandez & Martin 2002). En Facebook, cambia el modelo por segmento."),
 ("aku-usar-miradas-directas-a-camara-en-productos-virtuosos-claim","people","Usa miradas directas a camara en productos virtuosos (caridad): hacemos «buenas» conductas cuando nos observan (se dona mas junto a una imagen de ojos), asi que orientar la mirada del modelo hacia el espectador (un nino que saluda rompiendo la cuarta pared) presiona a comportarse bien y donar (Bateson et al. 2006)."),
 ("aku-usar-anuncios-negativos-para-captar-atencion-claim","strategy","Usa anuncios negativos para captar atencion y disparar accion inmediata: estamos hechos para evitar el dolor, asi que notamos mas los estimulos negativos (mas fijaciones oculares, mas compras impulsivas). Si el objetivo es accion inmediata (un clic), un marco negativo puede funcionar mejor (Ferreira et al. 2011; Shiv et al. 1997)."),
 ("aku-usar-anuncios-positivos-para-ser-recordado-claim","strategy","Usa anuncios positivos para ser recordado: los negativos captan atencion, pero los positivos se recuerdan mas, no por mas atencion sino por el nivel de activacion (arousal) durante la exposicion (Bolls, Lang & Potter 2001)."),
 ("aku-apelar-a-las-emociones-en-mercados-tradicionales-claim","strategy","Apela a las emociones en mercados maduros/tradicionales: el cliente familiarizado con un producto ignora los anuncios y procesa menos, asi que las apelaciones emocionales y los marcos positivos —que suben la implicacion personal— generan mas respuesta conductual (Chandy et al. 2001)."),
 ("aku-inyectar-algo-absurdo-o-sin-sentido-en-el-anuncio-claim","strategy","Inyecta algo absurdo o sin sentido: lo absurdo capta atencion al romper las expectativas (Arias-Bolzmann et al. 2000). Recursos: surrealismo (usar objetos de forma no convencional), antropomorfismo (rasgos humanos a objetos) y alegoria (describir algo en terminos de otra cosa)."),
 ("aku-terminar-los-anuncios-ilustrando-el-siguiente-paso-claim","strategy","Termina los anuncios ilustrando el siguiente paso en vez de pedir el CTA: muestra la accion realizandose (un cursor clicando «registrarse», una resena publicandose, tu URL tecleandose) para que el espectador la simule con facilidad y malatribuya esa facilidad a deseo y bajo esfuerzo."),
 ("aku-anunciar-en-modalidades-congruentes-claim","mediums","Anuncia en modalidades congruentes con el estado corporal del espectador: vende un curso online via video (YouTube), porque quien ya esta viendo video imagina mejor verlo; vende un libro via medios escritos (revistas, blogs), porque facilita simular la lectura."),
 ("aku-buscar-medios-con-emociones-congruentes-claim","mediums","Busca medios donde el espectador ya experimenta la emocion relevante: es mas facil exponer tu mensaje a alguien que ya siente una reaccion que generarla (Tums patrocina «Hot Ones», donde por neuronas espejo el espectador simula la comida picante y el valor del antiacido); o anuncia en el momento/lugar en que pueda simular el valor del producto."),
 ("aku-anunciar-en-el-mismo-dominio-tematico-claim","mediums","Anuncia en el mismo dominio semantico para que el espectador imagine usar tu producto: un anuncio de ketchup rindio mas tras uno de mayonesa, porque activo el dominio «condimentos» (Lee & Labroo 2004). Anuncia un curso de cocina en dominios de cocina."),
 ("aku-evitar-medios-que-muestren-un-emplazamiento-pagado-claim","mediums","Evita medios que etiqueten tu anuncio como «pagado»: la etiqueta «Paid Advertisement» redujo los clics un 25-27%, y el efecto aparece incluso con 6 (vs 3) segundos de divulgacion (Edelman & Gilchrist 2012)."),
 ("aku-anunciar-pronto-para-moldear-las-simulaciones-futuras-claim","timing","Anuncia pronto para moldear las simulaciones futuras: los spots de vuelta-al-cole o Navidad empiezan antes no para influir en el momento, sino para plantar una simulacion que dictara la conducta semanas despues (vas a comprar en Target porque plantaron la semilla antes que la competencia)."),
 ("aku-dispersar-los-anuncios-en-el-tiempo-claim","timing","Dispersa los anuncios en el tiempo (practica distribuida): igual que estudiar en incrementos supera al cramming, los anuncios espaciados rinden mas que los amontonados —se codifican mejor y con menos hartazgo— (Sahni 2011; Campbell & Keller 2003)."),
]
def main():
    write(CORE.replace("aku-",""), "concept", "advertising, marketing-psychology", CORE_STMT) if False else None
    with open(os.path.join(ROOT,"aku",CORE+".md"),"w",encoding="utf-8",newline="\n") as fh:
        fh.write(TPL.format(cls="concept",slug=CORE,stmt=wrap(CORE_STMT),dom="kolenda, advertising, marketing-psychology",src=SRC))
    for slug,dom,stmt in A: write(slug,dom,stmt)
    print(f"Escritos {len(A)+1} AKUs.")
    edges=[(slug,"supports",CORE) for slug,_,_ in A]
    edges += [
     ("aku-retratar-el-problema-en-escala-de-grises-contrast-fluency-claim","related","aku-hacer-que-el-precio-de-oferta-se-vea-distinto-contrast-fluency-claim"),  # contrast fluency (Pricing)
     ("aku-anadir-elementos-de-la-atencion-top-down-del-espectador-claim","related","aku-haz-tu-estimulo-similar-a-lo-que-el-objetivo-monitorea-goal-directed-claim"),  # top-down (Visual Attention)
     ("aku-posicionar-las-imagenes-a-la-izquierda-del-anuncio-claim","related","aku-posicionar-precios-arriba-o-a-la-izquierda-claim"),  # izquierda (Pricing)
     ("aku-reducir-el-color-para-eventos-distantes-en-el-tiempo-claim","related","aku-los-colores-desaturados-grayscale-transmiten-lujo-claim"),  # distancia temporal (Color)
     ("aku-rimar-el-eslogan-o-la-llamada-a-la-accion-claim","related","aku-insertar-aliteracion-en-los-precios-claim"),  # fluidez fonetica (Pricing)
     ("aku-inyectar-algo-absurdo-o-sin-sentido-en-el-anuncio-claim","related","aku-la-novedad-capta-la-atencion-claim"),  # novedad (Visual Attention)
     ("aku-anunciar-en-el-mismo-dominio-tematico-claim","related","aku-distribuir-palabras-semanticamente-relacionadas-claim"),  # spreading activation (Copywriting)
     ("aku-terminar-los-anuncios-ilustrando-el-siguiente-paso-claim","related","aku-mencionar-las-palabras-click-o-tap-cerca-del-boton-claim"),  # simulacion motora (eCommerce)
     ("aku-usar-miradas-directas-a-camara-en-productos-virtuosos-claim","related","aku-la-mirada-eye-gaze-capta-la-atencion-claim"),  # eye gaze (Visual Attention)
    ]
    wire(edges)
if __name__=="__main__": main()
