# -*- coding: utf-8 -*-
"""AKUs de «Naming a Product» (Nick Kolenda). source-tag: kolenda. Modo maximo-exhaustivo."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _audit_wire import wire
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/kolenda/naming-a-product-by-nick-kolenda/naming-a-product-by-nick-kolenda.md"
CORE = "aku-naming-metodologia-cinco-pasos-concept"
CORE_STMT = ("Nombrar un producto sigue una metodologia de cinco pasos: (1) elegir el tipo de nombre en la matriz "
 "wording x relevance (descriptivo, asociativo, deviant, neologistico); (2) elegir sonidos y letras con significado "
 "(sound symbolism); (3) construir nombres potenciales con los metodos por tipo; (4) filtrar el mejor nombre (longitud, "
 "pronunciacion, escritura, abreviatura, traduccion, disponibilidad); y (5) anadir version o numero. Implica que un "
 "nombre comunica significado por como suena y se articula, no solo por lo que describe.")
TPL = """---
type: aku
aku_class: {cls}
id: {slug}
statement: >
{stmt}
origin: "Nick Kolenda — Naming a Product"
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
        fh.write(TPL.format(cls=cls,slug=slug,stmt=wrap(stmt),dom="kolenda, naming, "+dom,src=SRC))

A = [
 # ===== STEP 1: types =====
 ("aku-matriz-de-nombres-wording-x-relevance-concept","concept","step1,types",
  "La matriz de nombres clasifica todo nombre en dos ejes —wording (palabra real vs nonword) y relevance (relevante vs irrelevante al producto)—, generando cuatro tipos: descriptivo, asociativo, deviant y neologistico. Ambos ejes son espectros, no categorias discretas, y la categorizacion es subjetiva (depende del mercado/idioma)."),
 ("aku-nombre-descriptivo-concept","concept","step1,types",
  "Un nombre descriptivo es una palabra real que describe el producto (General Motors, Electronic Arts). Maximiza la relevancia pero es el tipo menos memorable, menos distintivo y menos protegible; conviene evitarlo salvo cuando la relevancia es critica (productos informativos)."),
 ("aku-nombre-asociativo-concept","concept","step1,types",
  "Un nombre asociativo es un nonword que evoca o describe el producto de forma indirecta (Facebook, YouTube, LinkedIn). Combina algo de relevancia con la flexibilidad de un termino inventado."),
 ("aku-nombre-deviant-concept","concept","step1,types",
  "Un nombre deviant es una palabra real sin relevancia con el producto (Apple, Amazon, Dove). Es el tipo mas emocional —empaqueta mucho contenido emocional en pocas letras— y el segundo mas protegible (marca arbitraria)."),
 ("aku-nombre-neologistico-concept","concept","step1,types",
  "Un nombre neologistico es un nonword sin relevancia con el producto (Kodak, Spotify, Exxon). Es el tipo mas escalable (lienzo en blanco, sin percepciones previas) y el mas protegible (marca fanciful), ideal con presupuesto grande."),
 ("aku-los-nombres-persuasivos-son-ligeramente-irrelevantes-u-shaped-claim","claim","step1,persuasion",
  "Los nombres mas persuasivos son ligeramente irrelevantes: existe una relacion en U entre persuasion y congruencia nombre-producto (Meyers-Levy et al. 1994). Un nombre algo incongruente empuja al cliente a buscar significado, y el «aha» al resolver el puzzle se misatribuye al producto; evita los extremos (totalmente congruente o totalmente incongruente)."),
 ("aku-los-nombres-memorables-tienen-congruencia-moderada-claim","claim","step1,memory",
  "Los nombres mas memorables tienen congruencia moderada con el producto (Robertson 1989): el cerebro procesa las marcas como nombres propios, asi que un descriptivo largo («Simple Skin Care») se codifica peor que uno moderadamente deviant («Wright's Traditional Soap»); evita tanto el descriptivo extremo como el deviant/neologistico extremo."),
 ("aku-los-nombres-descriptivos-son-los-menos-distintivos-claim","claim","step1,distinctiveness",
  "Los nombres descriptivos son los menos distintivos: los nombres unicos e inesperados se quedan y enmarcan las expectativas de la marca, mientras que un descriptivo se mezcla con la competencia (The Naming Group 2016)."),
 ("aku-los-nombres-descriptivos-maximizan-relevancia-claim","claim","step1,relevance",
  "Los nombres descriptivos tienen una ventaja: la relevancia, util para productos informativos (libros de no-ficcion). Pero en la mayoria de contextos la irrelevancia rinde mejor."),
 ("aku-los-nombres-deviant-son-los-mas-emocionales-claim","claim","step1,emotion",
  "Los nombres deviant son los mas emocionales porque empaquetan mucho contenido emocional en poco espacio: «Dove» comunica delicado, bello, inocente y puro en cuatro letras, algo que un nombre descriptivo no puede transmitir de forma concisa."),
 ("aku-los-nombres-neologisticos-son-los-mas-escalables-claim","claim","step1,scalability",
  "Los nombres neologisticos son los mas escalables porque empiezan con un lienzo en blanco (Exxon) sin percepciones previas que interfieran, lo que facilita pintar la imagen deseada y traducir/expandir a otros paises. Caveat: con presupuesto pequeno, un nombre relevante rinde mas (construye sobre percepciones existentes)."),
 ("aku-los-nombres-neologisticos-son-los-mas-protegibles-trademark-claim","claim","step1,trademark",
  "La fuerza de marca registrada ordena los tipos de mas a menos protegible: neologistico (fanciful, Kodak) > deviant (arbitrary, Apple) > asociativo (suggestive) > descriptivo (descriptive, el mas debil; Petty 2008)."),
 ("aku-los-nonwords-son-mejores-para-seo-claim","claim","step1,seo",
  "Los nonwords (neologisticos) y los deviant son mejores para SEO: sin conexiones semanticas, los buscadores identifican facilmente la marca, mientras que un descriptivo se confunde con el topico generico. Como minimo, fusiona un nombre unico con terminos descriptivos en los servicios."),
 # ===== STEP 2: sound symbolism =====
 ("aku-sound-symbolism-los-sonidos-tienen-significado-concept","concept","step2,sound-symbolism",
  "El sound symbolism es el fenomeno por el que los sonidos portan significado de forma no arbitraria (efecto bouba-kiki: el 95% asigna «kiki» a la forma angular y «bouba» a la redonda). Es transcultural, presente en bebes y en idiomas ajenos; incluye que al subvocalizar un nombre activas el significado de sus sonidos."),
 ("aku-el-lenguaje-necesita-simbolismo-y-arbitrariedad-claim","claim","step2,sound-symbolism",
  "El lenguaje necesita a la vez sound symbolism (hace la comunicacion vivida al reforzar el significado) y arbitrariedad (la hace eficiente y evita confundir palabras parecidas como «feb» y «peb»). Un nombre eficaz equilibra ambos."),
 ("aku-frequency-code-tono-agudo-parece-pequeno-concept","concept","step2,mechanism",
  "El frequency code (Ohala 1984) es el mecanismo por el que los sonidos agudos/de alta frecuencia parecen pequenos y los graves grandes: evolutivamente el bramido grave intimidaba y el grito agudo pedia ayuda; por eso subimos la entonacion al preguntar (supplicacion) y los animales grunen (agresion) o gimen (sumision)."),
 ("aku-perceptual-fluency-la-forma-visual-de-la-letra-significa-concept","concept","step2,mechanism",
  "La perceptual fluency es el mecanismo por el que los rasgos visuales de las letras portan significado: la «b» parece mas redonda que la «k» en parte porque la letra b es visualmente mas redonda (Lockwood & Dingemanse 2015)."),
 ("aku-kinesthetic-fluency-la-articulacion-bucal-significa-concept","concept","step2,mechanism",
  "La kinesthetic fluency es el mecanismo por el que los sonidos significan por como los articula la boca: «kiki» se siente afilado porque la lengua hace inflexiones bruscas, y «bouba» redondo por el redondeo de labios y cavidad oral (Yardy 2010)."),
 ("aku-facial-feedback-los-fonemas-que-fuerzan-sonrisa-generan-afecto-concept","concept","step2,mechanism",
  "La facial feedback hypothesis aplicada al sonido: ciertos fonemas fuerzan una distorsion facial que induce la emocion correspondiente. La gente ayudo mas a personas cuyo nombre terminaba en «e» dura porque ese fonema fuerza una sonrisa (Kniffin & Shimizu 2014)."),
 ("aku-blending-los-sonidos-adquieren-significado-por-mezcla-concept","concept","step2,mechanism",
  "El blending es el mecanismo mas potente: el lenguaje crea palabras combinando otras e inserta los mismos sonidos en palabras similares (p.ej. «-ash» en palabras de golpe), de modo que por efecto bola de nieve un grupo de fonemas acaba asociado al significado de esas palabras."),
 ("aku-vocales-anteriores-vs-posteriores-concept","concept","step2,phonemes",
  "Las vocales se clasifican por la posicion de la lengua: anteriores (front: e, i, e) con la lengua adelante y posteriores (back: o, a, u) con la lengua atras. Es un espectro; las vocales de los extremos portan significado mas fuerte (Klink 2000)."),
 ("aku-consonantes-sonoras-vs-sordas-concept","concept","step2,phonemes",
  "Las consonantes se clasifican por vibracion de las cuerdas vocales: sonoras/voiced (vibran: b, d, g) y sordas/voiceless (no vibran: p, t, f)."),
 ("aku-consonantes-fricativas-vs-oclusivas-concept","concept","step2,phonemes",
  "Las consonantes se clasifican por el flujo de aire: fricativas (el aire escapa: s, f, z) y oclusivas/stops (el aire se detiene en la boca: p, k, b)."),
 ("aku-grupo-1-vs-grupo-2-de-fonemas-concept","concept","step2,phonemes",
  "Los fonemas se agrupan en dos polos de significado: Grupo 1 (vocales anteriores, consonantes sordas y fricativas) evoca pequeno, angular, rapido, brillante, sofisticado, corto-plazo y femenino; Grupo 2 (vocales posteriores, consonantes sonoras y oclusivas) evoca grande, redondo, lento, oscuro, rugoso, largo-plazo y masculino. Para nombrar, elige el grupo cuyo lado «encaje» con los adjetivos del producto."),
 ("aku-los-fonemas-del-grupo-1-parecen-pequenos-claim","claim","step2,meaning",
  "Los fonemas del Grupo 1 (vocales anteriores, sordas, fricativas) hacen que un nombre parezca fisicamente mas pequeno, y los del Grupo 2 mas grande: «mil» es la mesa pequena y «mal» la grande (Sapir 1929); los farmacos de cancer usan sordas (p, t, f) para sugerir un tratamiento pequeno (Abel & Glinert 2008)."),
 ("aku-los-fonemas-del-grupo-1-parecen-angulares-claim","claim","step2,meaning",
  "Los fonemas del Grupo 1 hacen un nombre mas angular y los del Grupo 2 mas redondo: «Brimley» encajaba mejor con un cuchillo y «Bromley» con un martillo (Lowrey & Shrum 2007); para helado se prefirio «Frosh» (redondo, cremoso) sobre «Frish» (Yorkston & Menon 2004)."),
 ("aku-los-fonemas-del-grupo-1-parecen-rapidos-claim","claim","step2,meaning",
  "Los fonemas del Grupo 1 hacen un nombre mas rapido y los del Grupo 2 mas lento (Robertson 1989; Klink 2000)."),
 ("aku-los-fonemas-del-grupo-1-parecen-brillantes-claim","claim","step2,meaning",
  "Los fonemas del Grupo 1 hacen un nombre mas brillante/claro y los del Grupo 2 mas oscuro (Klink 2003; Hirata, Ukita & Kita 2011)."),
 ("aku-los-fonemas-del-grupo-1-parecen-sofisticados-claim","claim","step2,meaning",
  "Los fonemas del Grupo 1 hacen un nombre mas sofisticado y los del Grupo 2 mas rugoso/robusto (evidencia con vocales; Klink & Athaide 2012)."),
 ("aku-los-fonemas-del-grupo-1-evocan-corto-plazo-claim","claim","step2,meaning",
  "Los fonemas del Grupo 1 evocan beneficios a corto plazo y los del Grupo 2 a largo plazo (via construal level): «Dari» fue mejor para tratamientos cortos y «Daru» para largos (Maglio et al. 2014)."),
 ("aku-los-fonemas-anteriores-evocan-lo-femenino-claim","claim","step2,meaning,gender",
  "Los fonemas del Grupo 1 (vocales anteriores) evocan lo femenino y los del Grupo 2 (posteriores, sonoras) lo masculino (Wu, Klink & Guo 2013; Guevremont & Grohmann 2015)."),
 ("aku-fonestemas-grupos-de-sonido-con-significado-concept","concept","step2,phonaesthemes",
  "Los fonestemas son grupos de sonido (no prefijos ni sufijos) que portan significado por blending: «gl-» evoca luz (glimmer, glow, glint), «sn-» la boca/nariz (snore, snout, sniff). Sirven para insertar significado relevante al inicio de un nombre."),
 # ===== STEP 3: build methods + claims =====
 ("aku-construir-nombres-neologisticos-method","method","step3,method",
  "Para construir un nombre neologistico: (A1) empieza con un prefijo significativo (fonestema, prefijo latino o consonante plosiva); (A2) ordena las consonantes de delante hacia atras de la boca (inward); (A3) termina con un fonema de genero relevante; (A4) elige el acento adecuado (sustantivo = primera silaba)."),
 ("aku-construir-nombres-asociativos-method","method","step3,method",
  "Para construir un nombre asociativo: (B1) crea un mapa semantico del producto con topicos concretos cercanos; (B2) genera sinonimos del beneficio principal con un tesauro; (B3) aplica una tecnica generativa de nombres para morfear esa relevancia en un nonword que «suene bien»."),
 ("aku-construir-nombres-descriptivos-method","method","step3,method",
  "Para construir un nombre descriptivo (solo si la relevancia es muy importante): (C1) identifica el termino descriptivo del producto; (C2) genera sinonimos de los beneficios; (C3) aplica una tecnica relevante (aliteracion, rima, fundador, geografia)."),
 ("aku-construir-nombres-deviant-method","method","step3,method",
  "Para construir un nombre deviant: (D1) identifica las emociones primarias del producto; (D2) transforma cada emocion en una etiqueta visual tangible; (D3) crea mapas semanticos alrededor de esas etiquetas; (D4) quedate solo con sustantivos concretos que despierten tu interes."),
 ("aku-empezar-el-nombre-con-plosiva-mejora-el-recall-claim","claim","step3,sounds",
  "Empezar un nombre con consonante plosiva (b, c, d, g, k, p, t) mejora significativamente el recall y el reconocimiento de la marca por su sonido explosivo (Robertson 1989). Ademas el inicio del nombre tine toda la percepcion, porque el cerebro codifica antes de terminar de leer (como en los charm prices)."),
 ("aku-ordenar-las-consonantes-de-delante-hacia-atras-inward-claim","claim","step3,sounds",
  "Ordenar las consonantes de delante hacia atras de la boca (nombres «inward», B-F-M-P...K-G) genera mayor agrado y willingness-to-pay que el orden inverso (Topolinski et al. 2014): el movimiento hacia dentro imita la deglucion (aproximacion) y el inverso la expectoracion (evitacion), ademas de mayor fluidez de pronunciacion."),
 ("aku-terminar-el-nombre-con-fonema-de-genero-claim","claim","step3,sounds,gender",
  "Termina el nombre con un fonema de genero relevante: los nombres masculinos tienden a terminar en consonante (Bob, Ted) y los femeninos en vocal (Sue, Katie); Chris->Christie feminiza por adicion de vocal (Cassidy et al. 1999). Para hombres termina en consonante, para mujeres en vocal."),
 ("aku-el-acento-silabico-determina-sustantivo-vs-verbo-claim","claim","step3,sounds",
  "El acento silabico determina si un nonword se percibe como sustantivo o verbo: acentuar la primera silaba lo hace sonar a sustantivo y acentuar las posteriores a verbo (record/record, permit/permit; Kelly 1988)."),
 ("aku-los-nombres-deben-contener-un-beneficio-positivo-claim","claim","step3,sounds",
  "La gente evalua mejor los nombres que contienen un atributo o beneficio positivo (Kohli, Harich & Leuthesser 2005); por eso conviene incorporar al nombre un beneficio clave del producto."),
 ("aku-los-sustantivos-concretos-hacen-el-nombre-mas-memorable-claim","claim","step3,sounds,memory",
  "Los sustantivos concretos con referente visual tangible (Dove, Mustang, Rabbit, Apple) hacen el nombre mas memorable y recuperable que los abstractos (Pledge, Tempo, Bold), y pueden activarse al ver el objeto real (Robertson 1989; Fitzsimons et al. 2008)."),
 # ===== STEP 4: filter =====
 ("aku-nombres-cortos-para-productos-pequenos-largos-para-grandes-claim","claim","step4,length",
  "Los nombres cortos son mejores para productos «pequenos»/simples y los largos para «grandes»/complejos: la longitud de la palabra implica tamano y complejidad fisica (como estirar «huuuge»; Topolinski et al. 2014; Coulter & Coulter 2005). Por defecto los nombres cortos suelen ser buenos."),
 ("aku-los-nombres-faciles-de-pronunciar-parecen-familiares-claim","claim","step4,pronunciation",
  "Los nombres faciles de pronunciar se sienten familiares (fluency), lo que suele ser bueno; pero la familiaridad reduce la intensidad/emocion percibida (montanas rusas «Chunta» parecen menos intensas; Song & Schwarz 2009)."),
 ("aku-los-nombres-disfluentes-parecen-mas-avanzados-o-arriesgados-claim","claim","step4,pronunciation",
  "Los nombres dificiles de pronunciar (disfluentes) parecen mas intensos, avanzados o arriesgados, lo que puede beneficiar a productos tecnologicamente avanzados o de alta sensacion (montanas rusas «Tsiischili»; farmacos avanzados; Cho 2014), invirtiendo el efecto fluency tipico."),
 ("aku-la-repeticion-fonetica-aliteracion-rima-agrada-claim","claim","step4,pronunciation",
  "La repeticion fonetica —aliteracion (Best Buy) o rima (FitBit)— resulta agradable al oido y hace el nombre mas tentador (Robertson 1989; Argo, Popa & Smith 2010)."),
 ("aku-elegir-nombres-con-pocas-variantes-de-escritura-claim","claim","step4,spelling",
  "Elige nombres con pocas variantes de escritura para que el cliente sepa escribirlos al oirlos (Purex solo se escribe de una forma); si no, prima la grafia correcta colocando cerca una palabra que se escriba parecido (Luna, Carnevale & Lerman 2013)."),
 ("aku-el-nombre-debe-seguir-siendo-brandable-al-abreviarse-claim","claim","step4,abbreviation",
  "La gente abreviara tu nombre quieras o no, asi que elige uno que siga siendo brandable abreviado (cuidado con «Amazing New Ultimate Store»). Las abreviaturas faciles de pronunciar rinden mejor: los tickers pronunciables (COF) superan a los dificiles (XRI; Alter & Oppenheimer 2006)."),
 ("aku-verificar-el-significado-del-nombre-en-otros-idiomas-claim","claim","step4,translation",
  "Verifica siempre el significado del nombre en otros idiomas antes de lanzarlo: Honda Fitta, Mitsubishi Pajero o Clairol Mist Stick fracasaron por significados obscenos o negativos en otras lenguas."),
 ("aku-verificar-la-disponibilidad-del-nombre-claim","claim","step4,availability",
  "Verifica la disponibilidad del nombre antes de elegirlo: busqueda en Google, dominio (.com u otros) y handles en plataformas sociales, que pueden condicionar tu estrategia de marketing."),
 # ===== STEP 5: alphanumeric =====
 ("aku-los-nombres-alfanumericos-funcionan-en-productos-tecnicos-y-formulados-claim","claim","step5,alphanumeric",
  "Los nombres alfanumericos (nombre + numero/version) funcionan mejor en dos tipos de producto: tecnicos (electronica, calculadoras) y quimicamente formulados (farmacos, combustibles, vitaminas)."),
 ("aku-los-numeros-en-el-nombre-implican-atributos-del-producto-claim","claim","step5,alphanumeric",
  "Los numeros en el nombre implican atributos del producto (Pavia & Costa 1993): el 41% creyo que «767» se referia al numero de asientos del avion (Yan & Duclos 2013)."),
 ("aku-un-numero-mayor-sugiere-un-producto-mas-avanzado-claim","claim","step5,alphanumeric,anchoring",
  "Un numero mayor en el nombre sugiere un producto mas avanzado (heuristica «higher is better»: se prefiere X-200 sobre X-100; Gunasti & Ross 2010) y dispara anclaje: un MP3 de 500$ parecio mejor valor llamandose M-600 que M-500 (Yan & Duclos 2013). Conviene superar los numeros de la competencia."),
 ("aku-mantener-el-numero-del-nombre-simple-claim","claim","step5,alphanumeric",
  "Manten el numero del nombre simple: si elegiste un nombre corto por simplicidad, «Titan BH-X25GHL» lo arruina; usa un numero sencillo (Titan 200)."),
 ("aku-los-numeros-aliterados-en-el-nombre-funcionan-mejor-claim","claim","step5,alphanumeric",
  "Los numeros aliterados con el nombre funcionan mejor: «10 Teven for $10» (totalmente aliterado) resulto mas atractivo, mas llamativo y con mayor intencion de compra (Davis, Bagchi & Block 2012); de ahi «Titan 200»."),
 ("aku-los-numeros-redondos-en-el-nombre-se-prefieren-claim","claim","step5,alphanumeric",
  "Se prefieren los numeros redondos en el nombre por su simplicidad: la gente prefiere productos de 25 y 10 (50%, 125) y los evalua como mas atractivos (Janiszewski & King 2010)."),
 ("aku-usar-numeros-compuestos-no-primos-en-el-nombre-claim","claim","step5,alphanumeric",
  "Si no usas un numero redondo, usa al menos un numero compuesto (no primo): Volvo S12 supero a S29, Axe 16 a Axe 17. Mostrar divisores cerca (un 62 en la matricula para S12: 6x2=12) aumenta la fluidez y mejora la evaluacion (Janiszewski & King 2011)."),
]

CONCEPTS = {"concept","method"}
def main():
    write(CORE,"concept","naming, marketing-psychology",CORE_STMT)
    for slug,cls,dom,stmt in A: write(slug,cls,dom,stmt)
    print(f"Escritos {len(A)+1} AKUs.")
    edges = [(s,"supports",CORE) for s,*_ in A]
    edges += [
     # --- internal: methods supported by the sound/phoneme concepts ---
     ("aku-grupo-1-vs-grupo-2-de-fonemas-concept","supports","aku-construir-nombres-neologisticos-method"),
     ("aku-sound-symbolism-los-sonidos-tienen-significado-concept","supports","aku-grupo-1-vs-grupo-2-de-fonemas-concept"),
     ("aku-empezar-el-nombre-con-plosiva-mejora-el-recall-claim","supports","aku-construir-nombres-neologisticos-method"),
     ("aku-ordenar-las-consonantes-de-delante-hacia-atras-inward-claim","supports","aku-construir-nombres-neologisticos-method"),
     ("aku-terminar-el-nombre-con-fonema-de-genero-claim","supports","aku-construir-nombres-neologisticos-method"),
     ("aku-el-acento-silabico-determina-sustantivo-vs-verbo-claim","supports","aku-construir-nombres-neologisticos-method"),
     ("aku-los-sustantivos-concretos-hacen-el-nombre-mas-memorable-claim","supports","aku-construir-nombres-deviant-method"),
     ("aku-los-nombres-deben-contener-un-beneficio-positivo-claim","supports","aku-construir-nombres-asociativos-method"),
     ("aku-terminar-el-nombre-con-fonema-de-genero-claim","related","aku-los-fonemas-anteriores-evocan-lo-femenino-claim"),
     ("aku-fonestemas-grupos-de-sonido-con-significado-concept","supports","aku-blending-los-sonidos-adquieren-significado-por-mezcla-concept"),
     # --- cross-corpus bridges ---
     ("aku-sound-symbolism-los-sonidos-tienen-significado-concept","related","aku-font-psychology-las-fuentes-significan-por-congruencia-de-rasgos-concept"),  # forma->significado (Font)
     ("aku-perceptual-fluency-la-forma-visual-de-la-letra-significa-concept","related","aku-font-psychology-las-fuentes-significan-por-congruencia-de-rasgos-concept"),
     ("aku-los-fonemas-del-grupo-1-parecen-angulares-claim","related","aku-fuentes-angulares-transmiten-formalidad-y-masculinidad-claim"),  # angular/redondo (Font)
     ("aku-los-fonemas-anteriores-evocan-lo-femenino-claim","related","aku-texturas-rugosas-parecen-masculinas-claim"),  # genero (Packaging)
     ("aku-empezar-el-nombre-con-plosiva-mejora-el-recall-claim","related","aku-colocar-el-numero-mayor-a-la-izquierda-principio-de-sustraccion-claim"),  # left-digit encoding (Pricing)
     ("aku-un-numero-mayor-sugiere-un-producto-mas-avanzado-claim","related","aku-exponer-a-cualquier-numero-alto-eleva-el-precio-de-referencia-claim"),  # anclaje (Pricing)
     ("aku-los-numeros-redondos-en-el-nombre-se-prefieren-claim","related","aku-usar-precios-redondos-en-el-contexto-adecuado-claim"),  # numeros redondos (Pricing)
     ("aku-los-numeros-aliterados-en-el-nombre-funcionan-mejor-claim","related","aku-insertar-aliteracion-en-los-precios-claim"),  # aliteracion (Pricing)
    ]
    wire(edges)
if __name__=="__main__": main()
