# -*- coding: utf-8 -*-
"""The 48 Laws of Power (Robert Greene) — Leyes 1-12 + framework TAKU.
Ingesta como claims DESCRIPTIVOS de las tacticas de poder que Greene afirma (no
recomendaciones del vault). 1 concept-AKU por ley."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/robert-greene/48-laws-of-power/48-laws-of-power.md"
ORIGIN = "Robert Greene — The 48 Laws of Power (1998)"
D = "2026-06-05"
RG = "robert-greene"

def law(n, slug, st, theme):
    nn = "%02d" % n
    return {"id": f"aku-48laws-{nn}-{slug}-concept", "class": "concept",
            "statement": st, "origin": ORIGIN,
            "domain": ["poder", RG, "48-laws", f"ley-{nn}", theme],
            "sources": [SRC], "created": D, "updated": D, "rel": {}}

akus = [
    law(1, "never-outshine-the-master",
        "La Ley 1 de Greene, «nunca eclipses al maestro», sostiene como táctica de poder que "
        "siempre debes hacer que quienes están por encima de ti se sientan cómodamente "
        "superiores: exhibir demasiado tus talentos inspira miedo e inseguridad en ellos y "
        "provoca tu caída (Fouquet ante Luis XIV), así que conviene hacerlos parecer más "
        "brillantes de lo que son (Galileo y los Medici); se invierte si tu superior es una "
        "estrella en declive, en cuyo caso eclipsarlo acelera su caída.", "jerarquia"),
    law(2, "never-trust-friends-use-enemies",
        "La Ley 2 de Greene, «nunca confíes demasiado en los amigos, aprende a usar a los "
        "enemigos», afirma que los amigos te traicionan antes porque se envidian con facilidad "
        "y se malcrían, mientras que un antiguo enemigo contratado es más leal porque tiene más "
        "que demostrar; implica que se debe temer más a los amigos que a los enemigos y, si no "
        "tienes enemigos, fabricarlos.", "lealtad"),
    law(3, "conceal-your-intentions",
        "La Ley 3 de Greene, «oculta tus intenciones», sostiene que mantengas a la gente "
        "desequilibrada y a oscuras sin revelar nunca el propósito de tus actos —si no saben "
        "qué tramas no pueden defenderse—, usando red herrings y cortinas de humo; se invierte "
        "cuando ya tienes fama de embustero, pues entonces ningún engaño oculta tus "
        "intenciones.", "engano"),
    law(4, "always-say-less-than-necessary",
        "La Ley 4 de Greene, «di siempre menos de lo necesario», afirma que cuanto más hablas "
        "más común y menos en control pareces, y más probable es que digas una tontería; los "
        "poderosos impresionan e intimidan diciendo poco y siendo vagos y enigmáticos "
        "(sphinxlike), de modo que el silencio incomoda al otro y le hace revelarse.", "silencio"),
    law(5, "guard-your-reputation",
        "La Ley 5 de Greene, «tanto depende de la reputación, guárdala con tu vida», sostiene "
        "que la reputación es la piedra angular del poder: solo con ella intimidas y ganas, "
        "pero al resquebrajarse quedas vulnerable; hay que hacerla inexpugnable y, a la vez, "
        "destruir a los enemigos abriendo agujeros en la suya y dejar que la opinión pública "
        "los hunda.", "reputacion"),
    law(6, "court-attention-at-all-cost",
        "La Ley 6 de Greene, «corteja la atención a toda costa», afirma que todo se juzga por "
        "su apariencia y lo que no se ve no cuenta, así que nunca debes perderte en la multitud "
        "sino destacar y ser conspicuo, volviéndote un imán de atención (más grande, colorido y "
        "misterioso); se invierte a medida que asciendes, cuando conviene no agotar al público "
        "con la misma táctica.", "atencion"),
    law(7, "get-others-to-do-the-work-take-credit",
        "La Ley 7 de Greene, «haz que otros hagan el trabajo, pero llévate siempre el "
        "crédito», sostiene usar la sabiduría, el conocimiento y el esfuerzo ajenos para tu "
        "causa, lo que ahorra tiempo y te da un aura divina de eficiencia; al final los "
        "ayudantes se olvidan y a ti se te recuerda: nunca hagas tú lo que otros pueden hacer "
        "por ti.", "delegacion"),
    law(8, "make-others-come-to-you",
        "La Ley 8 de Greene, «haz que la gente venga a ti, usa cebo si hace falta», afirma que "
        "quien fuerza al otro a actuar es quien controla: conviene hacer que el adversario "
        "venga a ti abandonando sus planes, atrayéndolo con ganancias fabulosas para luego "
        "atacar, manteniendo tú las cartas.", "iniciativa"),
    law(9, "win-through-actions-not-argument",
        "La Ley 9 de Greene, «vence con tus actos, nunca con la discusión», sostiene que "
        "cualquier triunfo logrado discutiendo es una victoria pírrica —el resentimiento que "
        "generas dura más que el cambio de opinión—, y que es mucho más poderoso lograr que "
        "otros estén de acuerdo mediante tus acciones, sin decir palabra: demuestra, no "
        "expliques.", "persuasion"),
    law(10, "avoid-the-unhappy-and-unlucky",
        "La Ley 10 de Greene, «infección: evita a los infelices y desafortunados», afirma que "
        "los estados emocionales son tan contagiosos como las enfermedades y que ayudar al que "
        "se ahoga solo precipita tu propio desastre, pues los desafortunados atraen la "
        "desgracia sobre sí y sobre ti; implica asociarse en cambio con los felices y "
        "afortunados.", "contagio-emocional"),
    law(11, "keep-people-dependent-on-you",
        "La Ley 11 de Greene, «aprende a mantener a la gente dependiente de ti», sostiene que "
        "para conservar tu independencia debes ser siempre necesario y deseado: cuanto más "
        "dependen de ti para su felicidad y prosperidad, más libertad y seguridad tienes, por "
        "lo que nunca les enseñes lo suficiente como para que puedan prescindir de ti.", "dependencia"),
    law(12, "selective-honesty-to-disarm",
        "La Ley 12 de Greene, «usa la honestidad y generosidad selectivas para desarmar a tu "
        "víctima», afirma que un solo gesto sincero cubre docenas de actos deshonestos y baja "
        "la guardia incluso del más suspicaz; una vez que tu honestidad selectiva abre un hueco "
        "en su armadura puedes manipularlo a voluntad, y un regalo oportuno funciona como un "
        "caballo de Troya.", "honestidad-selectiva"),
]

takus = [
    {"id": "taku-las-48-leyes-del-poder", "taku_type": "framework", "subdir": "frameworks",
     "title": "Las 48 Leyes del Poder (Robert Greene)",
     "origin": ORIGIN, "domain": [RG, "poder", "estrategia"],
     "when_to_use": "Para reconocer, anticipar y defenderte de las dinámicas de poder y manipulación en entornos competitivos (cortes, política, negocios); también para entender tácticas históricas.",
     "when_not_to_use": "Como manual moral de conducta: muchas leyes son amorales o manipuladoras; el propio Greene las presenta de forma descriptiva/histórica, no como receta ética. Úsalas sobre todo para detectarlas en otros.",
     "aku_links": {"justified_by": [
         "aku-48laws-01-never-outshine-the-master-concept",
         "aku-48laws-05-guard-your-reputation-concept",
         "aku-48laws-03-conceal-your-intentions-concept",
         "aku-48laws-02-never-trust-friends-use-enemies-concept"]},
     "created": D, "updated": D,
     "body": (
        "## Summary\n\n"
        "Catálogo de 48 leyes (tácticas de poder) destiladas por Robert Greene de la historia, "
        "la diplomacia y la estrategia (cortesanos, generales, estafadores, monarcas). Cada ley "
        "se presenta con su principio (Judgment), historias de transgresión/observancia, claves "
        "del poder y un Reversal (cuándo se invierte). Es descriptivo y amoral: su valor "
        "principal es reconocer estas dinámicas, no necesariamente practicarlas.\n\n"
        "## Core Components\n\n"
        "Las 48 leyes cubren ejes como: jerarquía y deferencia (1), lealtad y enemigos (2), "
        "ocultación e información (3, 14), comunicación e imagen (4, 6, 25, 37), reputación (5), "
        "apalancarse en otros (7, 8, 11, 13), control psicológico (9, 27, 33, 43), prudencia "
        "(10, 18, 19, 38, 47), audacia y timing (28, 35), formlessness y adaptación (48).\n\n"
        "## How to Apply\n\n"
        "1. Identifica qué ley está operando en una situación de poder (propia o ajena).\n"
        "2. Anticipa la jugada y diseña defensa o respuesta.\n"
        "3. Considera el Reversal: ninguna ley es absoluta; cada una tiene condiciones donde se "
        "invierte.\n"
        "4. Prioriza el uso defensivo (detectar manipulación) sobre el ofensivo.\n\n"
        "## Underlying Claims\n\n"
        "Cada ley es un AKU concept propio (`aku-48laws-NN-...`) que describe la táctica y, "
        "cuando aplica, su inversión. Ver el cluster completo.\n\n"
        "## Strengths\n\n"
        "Amplísimo repertorio histórico; útil para leer dinámicas de corte/política/negocios; "
        "cada ley con su contraindicación (Reversal).\n\n"
        "## Limitations and Criticisms\n\n"
        "Amoral y a menudo manipulador; selección histórica sesgada hacia confirmar las leyes; "
        "aplicado ingenuamente daña la confianza y las relaciones a largo plazo (choca con "
        "principios de integridad y juegos de suma positiva de otros corpus del vault).\n\n"
        "## Variants and Extensions\n\n"
        "Se complementa y a menudo tensiona con corpus de liderazgo basados en integridad "
        "(Jocko) y creación de valor de suma positiva (Naval): contrastar es parte del valor."),
    },
]

written, cross = akugen.generate(akus, takus, ROOT)
print("WRITTEN:", len(written))
for w in written: print("  ", os.path.relpath(w, ROOT))
print("CROSS:", len(cross))
