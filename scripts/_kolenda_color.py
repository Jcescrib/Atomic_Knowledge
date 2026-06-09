# -*- coding: utf-8 -*-
"""AKUs de «Color Psychology» (Nick Kolenda). source-tag: kolenda."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _audit_wire import wire
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/kolenda/color-psychology2/color-psychology2.md"
CORE = "aku-color-psychology-el-significado-del-color-depende-del-contexto-y-la-experiencia-concept"
CORE_STMT = ("El significado de un color no es intrinseco: depende de la experiencia pasada y solo es universal si "
 "todos lo ven en el mismo contexto (rojo/naranja son «calidos» porque todos sienten calor con el fuego o el sol). "
 "El color tiene tres componentes —hue (categoria), saturacion (vividez) y value (brillo)—, y las preferencias "
 "surgen de la evolucion y de la teoria de valencia ecologica (se prefiere el color asociado a experiencias "
 "positivas). Esos componentes generan significados universales (peso, tamano, proximidad, lujo, accion).")
TPL = """---
type: aku
aku_class: {cls}
id: {slug}
statement: >
{stmt}
origin: "Nick Kolenda — Color Psychology"
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
        fh.write(TPL.format(cls=cls,slug=slug,stmt=wrap(stmt),dom="kolenda, color, "+dom,src=SRC))
A = [
 ("aku-las-preferencias-de-color-vienen-de-la-evolucion-y-la-valencia-ecologica-claim","claim","preferences",
  "Las preferencias de color vienen de la evolucion (las mujeres prefieren rojizos por su rol ancestral recolector) y de la teoria de valencia ecologica: cuanto mas disfrute positivo asocias a objetos de un color, mas te gusta ese color (de ahi las diferencias de genero por refuerzo: azul a ninos, rosa a ninas; Palmer & Schloss 2010)."),
 ("aku-los-colores-oscuros-parecen-pesados-claim","claim","weight",
  "Los colores oscuros parecen pesados, y esa pesadez retrata otras ideas: durabilidad (productos oscuros mas duraderos), densidad (chocolate oscuro = rico y lleno; blanco = ligero/sano) e importancia (lo pesado «carga mas peso»). Pon los precios sobre fondo blanco para que pesen poco (Hagtvedt 2020; Ackerman et al. 2010)."),
 ("aku-los-colores-saturados-parecen-mas-grandes-claim","claim","size",
  "Los colores saturados parecen mas grandes: captan tu atencion, y como los objetos grandes captan mas atencion que los pequenos, el cerebro malatribuye esa atencion al tamano y asume que el objeto saturado es mayor (Hagtvedt & Brasel 2017)."),
 ("aku-los-colores-saturados-parecen-mas-cercanos-claim","claim","proximity",
  "Los colores saturados parecen mas cercanos (en espacio y en tiempo): la saturacion capta atencion y, como prestas mas atencion a lo cercano, se malatribuye a la proximidad. Una fecha limite saturada se percibe mas proxima; lo desaturado/grayscale se siente lejano en el tiempo (Lee et al. 2017)."),
 ("aku-los-colores-desaturados-grayscale-transmiten-lujo-claim","claim","luxury",
  "Los colores desaturados y el grayscale transmiten lujo: las marcas de lujo son aspiracionales porque se sienten distantes (como inalcanzables), y la distancia las hace mas deseadas. Reducir la saturacion de tus disenos refuerza la percepcion de marca premium (Chu, Chang & Lee 2021)."),
 ("aku-los-colores-saturados-orientan-al-detalle-claim","claim","details",
  "Los colores saturados, al sentirse cercanos, orientan el foco hacia los detalles del objeto (anuncios rojos funcionaron para describir detalles de una camara; azules para una vision general; Mehta & Zhu 2009). Cautela: con mucho texto, reduce la saturacion para que el diseno no abrume."),
 ("aku-el-blanco-facilita-la-accion-y-el-oscuro-retiene-claim","claim","actionability",
  "El blanco, al estar vacio, facilita el movimiento y la accion (registrarse, comprar); las interfaces oscuras retienen al visitante porque, al sentirse el movimiento mas dificil, salir tambien cuesta mas. Usa interfaces blancas en checkouts (Amazon, Kickstarter) y oscuras para retener (Netflix, Spotify)."),
 ("aku-el-blanco-promueve-visibilidad-y-el-oscuro-la-oculta-claim","claim","visibility",
  "El blanco promueve visibilidad (como el dia) y el oscuro la oculta (como la noche): cuando tu conducta se siente visible haces «buenas» acciones (donas mas cerca de una imagen de ojos), y la oscuridad aumenta las «malas» (equipos de uniforme negro reciben mas faltas). Fondo blanco para donaciones; oscuro para ocultar errores de novato o contenido sensible."),
 ("aku-el-rojo-refuerza-la-atraccion-social-claim","claim","sociality",
  "El rojo refuerza la atraccion: confundimos el calor fisico (rojo) con el calor social, que comparten circuito cerebral (forjado de bebes al ser sostenidos en brazos). Por eso la gente de rojo parece mas atractiva y el rojo va bien en contextos sociales (app de citas, eventos; Elliot & Niesta 2008)."),
 ("aku-los-colores-calidos-y-saturados-estimulan-el-azul-relaja-claim","claim","stimulating",
  "Los colores calidos y saturados estimulan e impulsan a actuar ya (la activacion inhibe el cortex y se racionaliza menos); el azul relaja y gusta. El azul va mejor en pantallas de carga (el usuario se relaja); el rojo saturado estimula y hace notar cada segundo de espera. Para accion usa rojo; para liking, azul (Crowley 1993)."),
 ("aku-el-rojo-aumenta-la-agresividad-y-el-dominio-claim","claim","aggression",
  "El rojo aumenta la agresividad y la percepcion de dominio: en competiciones, los de uniforme rojo ganan mas (se comportan mas agresivos y los rivales los ven mas dominantes), y las subastas de eBay con fondo rojo reciben pujas mas altas (Bagchi & Cheema 2013). Lleva azul a tu negociacion salarial."),
 ("aku-esquemas-de-combinacion-de-color-monocromatico-a-tetradico-method","method","schemes",
  "Esquemas para combinar colores: monocromatico (un hue, coherente/unido), analogo (hues adyacentes, unido con mas variedad), complementario (opuestos en la rueda, maximo contraste para empujar la atencion a un CTA), split-complementario (suaviza ese contraste extremo), triadico (tres a 120 grados, compromiso) y tetradico (rectangulo, variedad/complejidad)."),
]
def main():
    write(CORE,"concept","color, perception, branding, marketing-psychology",CORE_STMT)
    for slug,cls,dom,stmt in A: write(slug,cls,dom,stmt)
    print(f"Escritos {len(A)+1} AKUs.")
    edges = [(slug,"supports",CORE) for slug,*_ in A]
    edges += [
     ("aku-los-colores-oscuros-parecen-pesados-claim","related","aku-elegir-colores-claros-y-naturales-para-productos-sanos-claim"),  # cross-libro Packaging (claro/oscuro = peso)
     ("aku-el-rojo-aumenta-la-agresividad-y-el-dominio-claim","related","aku-mostrar-precios-en-rojo-a-los-hombres-claim"),  # cross-libro Pricing (rojo)
     (CORE,"related","aku-identidad-de-marca-concept"),
     (CORE,"related","aku-font-psychology-las-fuentes-significan-por-congruencia-de-rasgos-concept"),
    ]
    wire(edges)
if __name__=="__main__": main()
