# -*- coding: utf-8 -*-
"""Genera los AKUs de «Copywriting Psychology» (Nick Kolenda). source-tag: kolenda."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _audit_wire import wire

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/kolenda/copywriting-psychology-by-nick-kolenda/copywriting-psychology-by-nick-kolenda.md"
CORE = "aku-copywriting-psychology-frases-persuasivas-via-simulacion-mental-concept"
CORE_STMT = ("La persuasion de una frase depende de la simulacion mental que dispara en el lector, que "
 "imagina usar el producto para calibrar su deseo. Incluye palabras concretas y vividas (faciles de "
 "imaginar), continuidad fluida entre frases, rasgos linguisticos que reflejan el significado y un framing "
 "que evita la reactancia y las reciprocidades daninas; excluye lo vago, lo ambiguo y lo negativo; implica "
 "que la forma de la frase moldea su persuasion tanto como su contenido.")

TPL = """---
type: aku
aku_class: {cls}
id: {slug}
statement: >
{stmt}
origin: "Nick Kolenda — Copywriting Psychology"
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
    with open(os.path.join(ROOT, "aku", slug + ".md"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(TPL.format(cls=cls, slug=slug, stmt=wrap(stmt), dom="kolenda, "+dom, src=SRC))

A = [
 ("aku-elegir-palabras-faciles-de-imaginar-claim","claim","vividness",
  "Escribe palabras concretas y faciles de imaginar: el cliente decide imaginando la experiencia de usar el producto, y si no la imagina no imagina el valor. Describe galletas en «bolsas» o «piezas» (no «gramos»), y da instrucciones concretas («crea usuario y contrasena» mejor que «registrate»; Monnier & Thomas 2022)."),
 ("aku-reemplazar-beneficios-vagos-por-ejemplos-concretos-claim","claim","vividness",
  "Reemplaza beneficios vagos (quality, powerful, fast, easy, durable) por ejemplos concretos de una sola idea: «durable» admite mil interpretaciones (material, impacto, peso, vida util). Explica por que tu software es «facil»: pocas funciones, interfaz bella, onboarding rapido, automatizacion."),
 ("aku-adaptar-las-palabras-al-escenario-claim","claim","vividness",
  "Adapta las palabras al escenario concreto del cliente: las respuestas personalizadas persuaden mas (Packard & Berger 2021). «No puedo anadir esos vaqueros a tu pedido» supera a «no puedo anadir un producto»; cada ejemplo mas especifico instala una imagen mas concreta («esa camiseta verde te queda genial»)."),
 ("aku-ofrecer-aplicaciones-relevantes-del-producto-claim","claim","vividness",
  "La versatilidad puede salir mal: un seguro de «muerte por terrorismo» se prefirio a uno de «muerte por cualquier causa» (economicamente mejor) porque se imagina el escenario (Johnson et al. 1993). No obligues al cliente a pensar aplicaciones: sustituye «comida» por sopas, salsas, carnes; «emails» por lanzamientos, onboarding, newsletters."),
 ("aku-sumergir-al-lector-en-la-conducta-hipotetica-if-then-claim","claim","vividness,if-then",
  "Sumerge al lector en la conducta deseada con frases SI-ENTONCES: evaluar un condicional eleva la creencia en su antecedente mas que en su consecuente (Over et al. 2007). «Si ganaras el premio, que harias?» hace la victoria sentirse mas probable; «Si haces este curso...», «Si creas una cuenta...»."),
 ("aku-usar-marcos-positivos-no-negativos-claim","claim","vividness,framing",
  "Usa marcos positivos, no negativos: un marco negativo retrata el evento negativo («no gotea» evoca algo goteando, como «no pienses en un elefante rosa»; Jacoby et al. 1982). Escribe «suave con tu piel» en vez de «no dana tu piel»; si debes negar, conviertelo en positivo: «leak-proof», «BPA-free», «scratch-free»."),
 ("aku-distribuir-palabras-semanticamente-relacionadas-claim","claim","vividness,priming",
  "Distribuye palabras semanticamente relacionadas: activar un concepto activa los conectados («spreading activation»). «Si preparas (brew) cafe» supera a «si haces cafe» porque «brew» evoca «cafe» antes de leerlo; el texto se lee mas facil, gusta mas y se percibe mas veraz (Topolinski & Strack 2008)."),
 ("aku-usar-voz-activa-claim","claim","continuity",
  "Usa voz activa: vemos las causas antes que los efectos, asi que «Tim hugged Greg» se despliega sin fricciones mientras la pasiva obliga al cerebro a sostener un placeholder. Empieza las frases con algo concreto y evita aperturas vagas («there are», «this is») que oscurecen el sujeto."),
 ("aku-unir-frases-con-conectores-coherence-markers-claim","claim","continuity",
  "Une las frases con conectores («coherence markers»: and/or, then/next, but/though, because/so) para mantener un flujo de imagineria continuo; los lectores prefirieron la version conectada de un anuncio de Dove (Kamalski 2007). Los causales (because, so) persuaden especialmente porque senalan justificacion, que el modo automatico busca (Langer 1978)."),
 ("aku-terminar-las-frases-con-una-imagen-concreta-claim","claim","continuity",
  "Termina las frases con una palabra concreta, no con preposiciones colgando («what are you waiting for?»), que resultan chocantes porque el lector espera algo despues. «Why are you waiting?» empieza y acaba con palabras concretas."),
 ("aku-empezar-cada-frase-con-el-objeto-previo-claim","claim","continuity",
  "Empieza cada frase con el objeto de la anterior para que una sola narrativa se despliegue: el lector integra cada frase entrante en un unico modelo mental (Ehrlich & Johnson-Laird 1982). Encadenar el final de una frase con el principio de la siguiente facilita la lectura."),
 ("aku-restringir-a-una-sola-interpretacion-claim","claim","continuity",
  "Ordena las palabras para que solo sea posible una interpretacion: si la frase es ambigua, el lector debe descifrar el significado, lo que ralentiza la lectura y oscurece el mensaje."),
 ("aku-que-los-rasgos-linguisticos-reflejen-el-mensaje-claim","claim","linguistics",
  "Haz que los rasgos linguisticos reflejen el mensaje: como una fuente grande agranda el precio percibido, una frase larga y compleja agranda la tarea percibida. Para retratar un proceso simple, escribe una frase corta y simple; para variedad, usa palabras variadas; para consistencia, repite una frase; para diversion, usa palabras divertidas de decir."),
 ("aku-ajustar-la-distancia-entre-palabras-claim","claim","linguistics",
  "Ajusta la distancia entre palabras: el lector traduce clusters de palabras a una imagen, no palabras sueltas, asi que las cercanas se fusionan. «Customers find the chair comfortable» hace la silla mas comoda que «...that the chair is comfortable», donde «chair» y «comfortable» se separan (Coulter & Coulter 2005)."),
 ("aku-secuenciar-palabras-en-orden-alfabetico-claim","claim","linguistics,phonetics",
  "Secuenciar las palabras en orden alfabetico se siente agradable y el lector malatribuye esa sensacion al producto («Bufferil eases pain»; King & Auschaitrakul 2020)."),
 ("aku-retratar-acciones-con-verbos-imperfectos-claim","claim","linguistics",
  "Retrata las acciones con verbos imperfectos (was painting) en vez de perfectos (painted): «was painting» hace creer que pinto mas casas y dedico mas tiempo porque retrata el trabajo en curso (Matlock 2011). Un fiscal que dice «el acusado estaba apuntando el arma» logra mas condenas que «apunto el arma»."),
 ("aku-diversificar-palabras-sintaxis-y-emociones-claim","claim","linguistics",
  "Diversifica palabras, longitudes de frase y emociones: el cerebro se aburre con rasgos linguisticos repetidos (como con la misma comida; saciedad sensorial-especifica). El contenido que cambia de emocion de forma impredecible tiene mas exito (analisis de 4.000 peliculas y 30.000 articulos; Berger, Kim & Meyer 2021)."),
 ("aku-cuidar-el-flujo-fonetico-de-las-palabras-claim","claim","linguistics,phonetics",
  "Cuida el flujo fonetico: al leer hay habla interior, asi que lo dificil de decir es dificil de leer. Evita palabras con principios similares (sparrow snatched spider swiftly), finales similares (sling seating), adjuntos que comparten sonido (chairs sling) y cadenas de muchas palabras cortas (McCutchen et al. 1991)."),
 ("aku-eliminar-los-signos-de-exclamacion-claim","claim","linguistics",
  "Elimina los signos de exclamacion: el habla interior se vuelve enfatica al leerlos, lo que resulta raro en contextos mundanos («Buy Now!»), y el lector malatribuye esa emocion negativa al producto. Si necesitas un signo de exclamacion para generar emocion, tu texto no es lo bastante fuerte."),
 ("aku-segmentar-la-copy-por-necesidades-distintas-claim","claim","framing,segmentation",
  "Si distintos clientes compran por razones distintas (funcionalidad vs estetica), no diluyas la copy: empuja a cada segmento hacia una version distinta del texto (p.ej. una pagina por segmento: profesores, gerentes, estudiantes) para que cada uno llegue a una copy laser-enfocada en sus necesidades exactas."),
 ("aku-enfatizar-la-autonomia-de-decision-but-you-are-free-claim","claim","framing,reactance",
  "Enfatiza la libertad de elegir del cliente para esquivar la reactancia: la gente cumple menos si cree que la intentas persuadir (Brehm 1966), pero dono 4 veces mas tras oir «pero eres libre de aceptar o rechazar» (Guéguen & Pascual 2000)."),
 ("aku-describir-los-beneficios-indirectamente-claim","claim","framing,inference",
  "Describe los beneficios indirectamente para esquivar las reciprocidades daninas: «nuestro producto es seguro» invita al cliente caute a considerar «es inseguro». Si en cambio infiere el beneficio (certificaciones, lenguaje indirecto: «la frescura del exterior, ahora liquida»), el cliente se vuelve la fuente y confia mas en si mismo que en el marketer."),
 ("aku-mencionar-inconvenientes-argumento-bilateral-claim","claim","framing,two-sided",
  "Menciona tambien los inconvenientes: los argumentos bilaterales (pros y contras) se prefieren y generan mas confianza (Rucker, Petty & Brinol 2008); por eso Amazon muestra resenas positivas y negativas. La decision se siente mas cauta e informada y el cliente compra mas tranquilo."),
 ("aku-usar-preguntas-retoricas-claim","claim","framing,engagement",
  "Usa preguntas retoricas: invitan a una respuesta implicita que aumenta el compromiso y la certeza de la actitud, y el lector evalua tu mensaje con mas cuidado (Petty, Cacioppo & Heesacker 1981)."),
 ("aku-demostrar-el-impacto-en-otras-personas-claim","claim","framing,social",
  "Demuestra el impacto en otras personas, no solo en el cliente: por el sesgo optimista, nadie espera que el evento negativo le ocurra, asi que tu producto parece innecesario. El personal sanitario se lavo mas las manos con «previene que los pacientes enfermen» que con «que tu enfermes» (Grant & Hofmann 2011): «protege a tu familia»."),
]

def main():
    write(CORE, "concept", "copywriting, persuasion, marketing-psychology", CORE_STMT)
    for slug, cls, dom, stmt in A:
        write(slug, cls, "copywriting,"+dom, stmt)
    print(f"Escritos {len(A)+1} AKUs (nucleo + {len(A)} tacticas).")
    edges = [(slug, "supports", CORE) for slug, *_ in A]
    edges += [
     ("aku-que-los-rasgos-linguisticos-reflejen-el-mensaje-claim","related","aku-mostrar-precios-en-fuente-pequena-claim"),       # cross-libro Coulter (tamano-fuente)
     ("aku-ajustar-la-distancia-entre-palabras-claim","related","aku-agrupar-palabras-de-tamano-pequeno-junto-al-precio-claim"),    # cross-libro Coulter (distancia)
     ("aku-secuenciar-palabras-en-orden-alfabetico-claim","related","aku-insertar-aliteracion-en-los-precios-claim"),               # cross-libro fluidez fonetica
     ("aku-elegir-palabras-faciles-de-imaginar-claim","related","aku-reemplazar-beneficios-vagos-por-ejemplos-concretos-claim"),    # intra
    ]
    wire(edges)

if __name__ == "__main__":
    main()
