# -*- coding: utf-8 -*-
"""AKUs de «eCommerce Psychology» (Nick Kolenda). source-tag: kolenda."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _audit_wire import wire
import akupatch
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/kolenda/ecommerce-psychology-by-nick-kolenda/ecommerce-psychology-by-nick-kolenda.md"
CORE = "aku-ecommerce-psychology-optimizar-el-funnel-via-simulacion-de-compra-concept"
CORE_STMT = ("El cliente evalua cada compra simulando el resultado (consumir el producto) y el proceso (completar la "
 "transaccion), asi que optimizar un eCommerce es facilitar esas dos simulaciones en cada etapa del funnel "
 "(pre-purchase, evaluacion de producto, resenas, botones y checkout). Incluye reducir friccion y reforzar la "
 "imageneria de compra; excluye elementos que disparen simulaciones competidoras; implica que detalles "
 "aparentemente triviales (borde, boton, barra de progreso) mueven la conversion.")
TPL = """---
type: aku
aku_class: {cls}
id: {slug}
statement: >
{stmt}
origin: "Nick Kolenda — eCommerce Psychology"
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
        fh.write(TPL.format(cls=cls,slug=slug,stmt=wrap(stmt),dom="kolenda, ecommerce, "+dom,src=SRC))
A = [
 ("aku-oscurecer-el-borde-superior-de-la-interfaz-claim","claim","pre-purchase",
  "Oscurece el borde superior de la interfaz: por gestalt de similitud, un sitio de fondo blanco se agrupa con las pestanas blancas/grises del navegador, y el visitante puede clicar una pestana y salir. Una barra oscura arriba se vuelve una barra conceptual que fija la atencion en el sitio (al reves si las pestanas son oscuras)."),
 ("aku-usar-visuales-en-las-etapas-tempranas-de-eleccion-claim","claim","pre-purchase",
  "Usa opciones visuales en las etapas tempranas de la eleccion (home con thumbnails) para facilitar el browsing, y una interfaz mas textual en el momento de la consideracion de compra para que el cliente frene y revise cada opcion con cuidado (Townsend & Kahn 2014)."),
 ("aku-disponer-los-productos-horizontalmente-para-explorar-claim","claim","pre-purchase",
  "Dispon los productos en horizontal para el browsing: los ojos, alineados horizontalmente, escanean mas rapido los surtidos horizontales y eso aumenta la variedad percibida (Deng et al. 2016). Pero usa listas verticales cuando el cliente busca una opcion concreta, para situarla arriba, en su linea de mirada."),
 ("aku-recomendar-una-opcion-genera-momentum-claim","claim","pre-purchase",
  "Recomienda una opcion: la gente quiere elecciones faciles, y aunque no escoja la recomendada, contemplarla genera momentum (empieza a comparar otras y avanza en la decision). Idealmente personaliza la recomendacion segun su historial; como minimo destaca la opcion «mas popular»."),
 ("aku-mostrar-el-unboxing-del-producto-claim","claim","evaluation",
  "Muestra el unboxing del producto (imagen o video de alguien abriendo la caja): el cliente se sumerge en quien abre la caja —siente que es el quien la abre—, lo que activa la imagen mental de comprar y emociones positivas (sensacion de regalo), y malinterpreta esa vividez como deseo de compra."),
 ("aku-ayudar-al-usuario-a-imaginar-tocar-el-producto-claim","claim","evaluation",
  "Ayuda al usuario a imaginar tocar el producto: se prefieren los productos interactuables (las tazas con el asa hacia la mano dominante, porque se imagina agarrarla; Elder & Krishna 2012). Orienta el producto en las imagenes para facilitar esa simulacion motora."),
 ("aku-insertar-la-foto-del-usuario-en-la-interfaz-claim","claim","evaluation",
  "Inserta la foto del usuario en la interfaz (con un enfoque no creepy: pidela al crear la cuenta y mantenla en el menu): esa senal tangible de la realidad transforma un evento vago en una compra mas realista en todas las paginas."),
 ("aku-restringir-la-cantidad-de-productos-de-estatus-escasez-claim","claim","evaluation,scarcity",
  "La escasez tiene dos tipos: de cantidad («solo 3 en stock») y de duracion («caduca manana»). La escasez de cantidad funciona mejor con productos conspicuos/de estatus (ropa), porque el comprador compite con otros y el producto se vuelve simbolo de estatus; la de duracion sirve en cualquier caso (Jang et al. 2015)."),
 ("aku-mostrar-resenas-imperfectas-claim","claim","reviews",
  "Las resenas perfectas estan sobrevaloradas: persuaden mas las de valoracion moderadamente alta (4 a 4,5 estrellas) y las que mencionan pros y contras (un dato negativo menor tras lo positivo mejora la evaluacion global y la credibilidad del resenador; Maslowska et al. 2017)."),
 ("aku-insertar-contenido-persuasivo-en-las-resenas-claim","claim","reviews",
  "Insertar contenido persuasivo en las resenas: corrige erratas (las erratas restan persuasion), censura tacos (las resenas enfadadas ayudan menos), premia a quien anade fotos/video, muestra nombres reales (Joe S. > jschmo), prueba de consumo («compra verificada») y pide valorar multiples dimensiones (precio, calidad, estetica)."),
 ("aku-responder-a-las-resenas-negativas-claim","claim","reviews",
  "Responder a las resenas negativas ayuda: reservas de hotel +60%, valoraciones +20%, volumen de resenas +17%. Como menos del 4% de los negocios responde a las negativas, hacerlo te diferencia (Ye et al. 2008; Xie et al. 2016)."),
 ("aku-traer-los-botones-al-primer-plano-claim","claim","buttons",
  "Trae los botones al primer plano: el boton es la segunda simulacion (completar la transaccion), y se compra mas si el cliente imagina clicarlo. Ponlo cerca de los dedos (abajo, como Apple) o dale profundidad (sombra, fondo detras) para que parezca fisicamente mas cercano y clicable."),
 ("aku-describir-el-siguiente-paso-concreto-en-el-boton-claim","claim","buttons",
  "Que el texto del boton describa el siguiente paso concreto y vivido: «View on Amazon» (no «Buy on Amazon», porque comprar no es el paso siguiente: aun hay que leer la descripcion) se simula con menos esfuerzo. Cautela: un boton de «mayor inversion» (Buy) baja el click-through pero puede subir conversiones despues, porque genera la imagen mental de la compra."),
 ("aku-evitar-texto-cursi-y-exclamaciones-en-los-botones-claim","claim","buttons",
  "Evita texto cursi («Count Me In») o exclamativo («Buy Now!») en los botones: por el habla interior, ese texto se lee con disfluencia, algo «se siente mal» y el cliente atribuye esa sensacion a la compra. Elige texto que suene natural, como se diria en la vida real."),
 ("aku-mostrar-opciones-de-rechazo-feas-claim","claim","buttons",
  "Muestra las opciones de rechazo feas: si el boton de compra es bonito (y sus rasgos positivos se atribuyen a la compra), haz lo reciproco con la opcion de rechazo (fuentes raras, posicion desequilibrada, espaciado ancho) para que el cliente le atribuya rasgos negativos y prefiera la opcion de compra."),
 ("aku-mostrar-una-afirmacion-positiva-cerca-del-boton-claim","claim","buttons",
  "Muestra una afirmacion positiva cerca del boton principal («Instant Access», «100% Secure», «30-Day Guarantee»): el boton dispara la simulacion de compra, y cualquier frase cercana se infiltra en esa imagen mental, asi que conviene que sea positiva."),
 ("aku-mencionar-las-palabras-click-o-tap-cerca-del-boton-claim","claim","buttons",
  "Menciona las palabras «click» o «tap» cerca del boton: al leer verbos se simula la accion motora descrita (resonancia motora; Zwaan & Taylor 2006), asi que esos verbos activan los musculos del gesto y el boton parece mas clicable."),
 ("aku-facilitar-el-movimiento-simbolico-del-progreso-en-el-checkout-claim","claim","checkout",
  "Facilita el movimiento simbolico del progreso en el checkout: muestra los pasos restantes, idealmente con movimiento descendente (por la gravedad, el momentum percibido es mayor hacia abajo; Hubbard 2005), para que el usuario imagine alcanzar antes la entrega. Si va en horizontal, usa un gradiente o acerca la barra al paso final."),
 ("aku-ocultar-los-enlaces-de-salida-en-el-checkout-claim","claim","checkout",
  "Oculta los enlaces de salida en el checkout: los enlaces de menu diluyen la compra porque el cliente imagina visitarlos (simulaciones competidoras), y aunque se quede, esas simulaciones debilitan la de la compra. Quita todo estimulo que dispare simulaciones rivales."),
 ("aku-restar-saliencia-al-campo-de-cupon-claim","claim","checkout",
  "Resta saliencia al campo de cupon: el cliente compara su precio con lo que pagaron otros, y un campo de descuento vacio le hace inferir que otros pagan menos (doloroso, percepcion de injusticia). No lo elimines; sustituye el campo vacio por un enlace de texto («Tienes un codigo de descuento?»)."),
 ("aku-reducir-la-saliencia-de-las-opciones-competidoras-tras-comprar-claim","claim","checkout",
  "Tras completar el checkout, reduce la saliencia de las opciones competidoras (choice closure): el chocolate supo mejor al cerrar la tapa tras elegir, y el te al cerrar el menu (Gu, Botti & Faro 2013). Puedes hacer upsell/cross-sell, pero que no compita con lo elegido para que el cliente no dude."),
]
def main():
    write(CORE,"concept","ecommerce, conversion, marketing-psychology",CORE_STMT)
    for slug,cls,dom,stmt in A: write(slug,cls,dom,stmt)
    print(f"Escritos {len(A)+1} AKUs.")
    # dedup-merge cross-libro: which-to-choose ya existe (Choice). +fuente eCommerce, 0.50->0.60
    akupatch.apply(ROOT, [{"id":"aku-activar-una-mentalidad-de-cual-elegir-which-to-choose-claim",
                           "add_source":SRC, "confidence":0.60, "updated":"2026-06-09"}])
    print("Dedup-merge: +fuente eCommerce en which-to-choose (0.60).")
    edges = [(slug,"supports",CORE) for slug,*_ in A]
    edges += [
     (CORE,"related","aku-activar-una-mentalidad-de-cual-elegir-which-to-choose-claim"),  # which-to-choose (Choice)
     ("aku-evitar-texto-cursi-y-exclamaciones-en-los-botones-claim","related","aku-eliminar-los-signos-de-exclamacion-claim"),  # cross-libro Copywriting
     ("aku-mostrar-resenas-imperfectas-claim","related","aku-mencionar-inconvenientes-argumento-bilateral-claim"),  # two-sided (cross-libro Copywriting)
     ("aku-restringir-la-cantidad-de-productos-de-estatus-escasez-claim","related","aku-cialdini-escasez-concept"),  # escasez (Power MBA)
     ("aku-restar-saliencia-al-campo-de-cupon-claim","related","aku-describir-los-costes-del-producto-aumenta-la-percepcion-de-justicia-claim"),  # justicia de precio (cross-libro Pricing)
    ]
    wire(edges)
if __name__=="__main__": main()
