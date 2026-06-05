# -*- coding: utf-8 -*-
"""Almanack of Naval — ch11 Be Patient + Building Judgment (Judgment, How to Think
Clearly, Shed Your Identity). Solo items NUEVOS."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/naval/almanack-of-naval-ravikant/almanack-of-naval-ravikant.md"
ORIGIN = "Naval Ravikant — The Almanack of Naval Ravikant (ed. Eric Jorgenson, 2020)"
D = "2026-06-05"
N = "naval"

def c(idn, cls, st, dom, rel=None):
    return {"id": idn, "class": cls, "statement": st, "origin": ORIGIN,
            "domain": dom, "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    # ── ch11 Be Patient ──
    c("aku-grandes-personas-tienen-grandes-resultados-si-eres-paciente-claim", "claim",
      "Las grandes personas tienen grandes resultados si eres paciente: casi sin excepción, "
      "quienes son muy capaces, listos y dedicados acaban teniendo mucho éxito, pero nunca en "
      "el plazo que tú o ellos querríais; hay que darles (y darte) una escala temporal "
      "suficientemente larga.",
      [N, "paciencia", "largo-plazo"]),
    c("aku-aplica-y-se-paciente-pero-no-lleves-la-cuenta-claim", "claim",
      "Aplica specific knowledge con leverage y acabarás recibiendo lo que mereces, pero el "
      "mundo es eficiente y lo inmediato no funciona: hay que poner las horas y disfrutarlo "
      "sin llevar la cuenta, porque si cuentas, te quedarás sin paciencia antes de que llegue "
      "el éxito.",
      [N, "paciencia", "constancia"],
      {"related": ["aku-armate-con-specific-knowledge-accountability-y-leverage-claim"]}),
    c("aku-no-esperes-por-ser-joven-solo-se-aprende-haciendo-claim", "claim",
      "El consejo «eres demasiado joven» suele ser malo: gran parte de la historia la "
      "construyeron jóvenes que solo recibieron el crédito de mayores; escucha la guía, pero no "
      "esperes, porque la única forma de aprender de verdad algo es haciéndolo.",
      [N, "accion", "juventud"]),
    c("aku-tu-curriculum-real-es-tu-catalogo-de-sufrimiento-claim", "claim",
      "Tu currículum real es el catálogo de todo tu sufrimiento: lo interesante que recordarás "
      "desde tu lecho de muerte serán los sacrificios y las cosas difíciles que hiciste; como "
      "lo que te viene dado no aporta sentido, tienes que hacer cosas difíciles para crear tu "
      "propio significado en la vida.",
      [N, "sentido", "esfuerzo"]),
    c("aku-el-dinero-resuelve-problemas-de-dinero-no-te-hace-feliz-claim", "claim",
      "El dinero compra libertad en el mundo material y elimina un conjunto de cosas que "
      "estorban a la felicidad, pero no te hará feliz ni sano ni en forma ni en calma: solo "
      "resuelve tus problemas de dinero; hay muchos ricos infelices.",
      [N, "dinero", "felicidad"],
      {"related": ["aku-la-libertad-es-el-valor-supremo-claim"]}),
    c("aku-la-persona-en-que-te-vuelves-para-ganar-dinero-es-ansiosa-y-no-se-apaga-claim", "claim",
      "La persona en que sueles tener que convertirte para ganar dinero es ansiosa, "
      "estresada, trabajadora y competitiva; tras décadas entrenándote así, al hacer dinero no "
      "puedes apagarlo, y entonces tienes que aprender por separado a ser feliz.",
      [N, "dinero", "felicidad"]),
    # ── Building Judgment / Judgment ──
    c("aku-te-haces-rico-ahorrando-tiempo-para-ganar-dinero-no-gastando-tiempo-para-ahorrar-claim", "claim",
      "No te haces rico gastando tu tiempo para ahorrar dinero, sino ahorrando tu tiempo para "
      "ganar dinero: el trabajo duro está sobrevalorado en la economía moderna y cuánto te "
      "esfuerzas importa mucho menos que en qué diriges ese esfuerzo.",
      [N, "tiempo", "juicio"]),
    c("aku-el-juicio-esta-infravalorado-claim", "claim",
      "El juicio está infravalorado y el trabajo duro sobrevalorado: en una era de leverage, "
      "una sola decisión correcta puede ganarlo todo, así que desarrollar buen juicio rinde "
      "más que aplicar más fuerza.",
      [N, "juicio", "leverage"],
      {"related": ["aku-judgment-naval-concept"]}),
    c("aku-sabiduria-es-conocer-consecuencias-a-largo-plazo-juicio-es-aplicarla-concept", "concept",
      "La sabiduría es conocer las consecuencias a largo plazo de tus acciones, y el juicio es "
      "la sabiduría aplicada a problemas externos —saber esas consecuencias y tomar la decisión "
      "correcta para capitalizarlas—; incluye estar muy ligados entre sí; implica que decidir "
      "bien depende de anticipar el largo plazo, no de la velocidad.",
      [N, "sabiduria", "juicio"],
      {"related": ["aku-judgment-naval-concept"]}),
    c("aku-la-direccion-importa-mas-que-la-velocidad-sobre-todo-con-leverage-claim", "claim",
      "La dirección en la que te mueves importa mucho más que la velocidad a la que lo haces, "
      "sobre todo con leverage: elegir bien la dirección de cada decisión pesa muchísimo más "
      "que la fuerza que aplicas; basta con elegir la dirección correcta y empezar a caminar.",
      [N, "juicio", "estrategia"]),
    # ── How to Think Clearly ──
    c("aku-pensador-claro-mejor-que-listo-explica-a-un-nino-desde-los-fundamentos-claim", "claim",
      "Ser «pensador claro» es mejor elogio que «listo»: el conocimiento real es intrínseco y "
      "se construye desde abajo, así que los más inteligentes pueden explicar cualquier cosa a "
      "un niño; si no puedes explicarlo a un niño o rederivarlo desde lo básico cuando lo "
      "necesitas, no lo sabes, solo lo memorizas.",
      [N, "pensamiento", "fundamentos"]),
    c("aku-domina-lo-basico-los-conceptos-avanzados-solo-senalan-pertenencia-claim", "claim",
      "Conviene clavar lo básico antes que profundizar: los conceptos avanzados de un campo "
      "están menos probados y los usamos para señalar conocimiento de iniciado, cuando "
      "estaríamos mejor dominando los fundamentos; quien usa muchas palabras y conceptos "
      "rimbombantes probablemente no sabe de qué habla.",
      [N, "pensamiento", "fundamentos"]),
    c("aku-el-deseo-y-el-ego-nublan-la-realidad-claim", "claim",
      "Lo que deseamos que sea verdad nubla nuestra percepción de lo que es verdad: la «monkey "
      "mind» y las nociones preconcebidas de cómo deberían ser las cosas impiden ver la "
      "realidad; lo que sientes no te dice nada sobre los hechos, solo sobre tu estimación de "
      "ellos, así que cuanto más pequeño hagas tu ego y tus deseos sobre el resultado, más "
      "fácil será ver la realidad.",
      [N, "realidad", "ego"],
      {"related": ["aku-el-ego-mas-dificil-es-el-propio-claim"]}),
    c("aku-el-sufrimiento-es-el-momento-de-ver-la-realidad-como-es-concept", "concept",
      "Un momento de sufrimiento es el momento en que ves las cosas exactamente como son, tras "
      "haber estado negando la realidad; incluye ser un momento de verdad que te fuerza a "
      "abrazar la realidad; excluye ser solo dolor inútil; implica que solo puedes progresar "
      "partiendo de la verdad, por lo que el sufrimiento habilita el cambio significativo.",
      [N, "sufrimiento", "realidad"]),
    c("aku-necesitas-espacio-vacio-para-pensar-las-ideas-llegan-tras-el-aburrimiento-claim", "claim",
      "Necesitas espacio vacío para pensar: si no reservas uno o dos días a la semana sin "
      "reuniones ni ajetreo, no tendrás buenas ideas ni buen juicio para tu negocio; las "
      "grandes ideas llegan tras el aburrimiento, nunca cuando estás estresado, ocupado o con "
      "prisa.",
      [N, "creatividad", "tiempo"]),
    c("aku-el-contrario-optimista-razona-desde-cero-y-es-la-especie-mas-rara-concept", "concept",
      "Un verdadero contrario (contrarian) no es quien siempre objeta —eso es otro conformismo— "
      "sino quien razona de forma independiente desde los cimientos y resiste la presión por "
      "conformarse; incluye que el cinismo y la mímica son fáciles; implica que el contrario "
      "optimista es la especie más rara y valiosa.",
      [N, "pensamiento-independiente", "contrarian"]),
    # ── Shed Your Identity to See Reality ──
    c("aku-el-ego-se-construye-en-las-primeras-dos-decadas-concept", "concept",
      "El ego se construye en las primeras dos décadas de vida a partir del entorno, los "
      "padres y la sociedad, y luego pasamos el resto de la vida intentando hacerlo feliz, "
      "interpretando todo lo nuevo a través de él («¿cómo cambio el mundo externo para que sea "
      "más como yo quiero?»); implica que el ego es una construcción revisable, no tu esencia.",
      [N, "ego", "identidad"]),
    c("aku-descondicionate-revisa-si-tus-habitos-aun-te-sirven-claim", "claim",
      "Necesitas hábitos para funcionar, pero conviene descondicionarse: desmontar cada hábito "
      "y preguntar si aún te sirve, te hace más feliz o sano, o te ayuda a lograr lo que te "
      "propones, porque muchos los adquiriste de niño y los incrustaste en tu identidad; haz "
      "tus hábitos deliberados en vez de accidentes de la historia.",
      [N, "habitos", "identidad"]),
    c("aku-las-creencias-tomadas-en-paquete-son-sospechosas-reevalua-desde-principios-claim", "claim",
      "Cualquier creencia que tomaste en paquete (demócrata, católico, americano, libertario) "
      "es sospechosa y debe reevaluarse desde principios base: si todas tus creencias encajan "
      "en paquetes ordenados, deberías desconfiar mucho, porque acabas defendiendo posiciones "
      "que no has pensado por ti mismo.",
      [N, "creencias", "pensamiento-independiente"]),
    c("aku-para-ser-honesto-habla-sin-identidad-las-etiquetas-te-atan-claim", "claim",
      "Para ser honesto, habla sin identidad: crear identidades y etiquetas te encierra y te "
      "impide ver la verdad, así que conviene no autoidentificarse en casi ningún nivel para no "
      "acumular creencias «estables» que defiendes por pertenencia y no por razón.",
      [N, "identidad", "honestidad"]),
    c("aku-todos-tenemos-una-creencia-contraria-que-la-tribu-rechaza-claim", "claim",
      "Cada uno tiene una creencia contraria que la sociedad rechaza, y cuanto más la rechazan "
      "tu propia identidad y tu tribu local, más probable es que sea cierta: el rechazo del "
      "entorno es una señal de que la creencia toca algo real.",
      [N, "pensamiento-independiente", "contrarian"]),
]

written, cross = akugen.generate(akus, [], ROOT)
print("WRITTEN:", len(written))
for w in written: print("  ", os.path.relpath(w, ROOT))
ops_by_id = {}
for new_id, field, inv, tgt in cross:
    ops_by_id.setdefault(tgt, {"id": tgt, "add_rel": []})["add_rel"].append((inv, new_id))
akupatch.apply(ROOT, list(ops_by_id.values()))
print("\nPATCHED:", list(ops_by_id.keys()))
print("CROSS count:", len(cross))
