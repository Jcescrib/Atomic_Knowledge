# -*- coding: utf-8 -*-
"""The 48 Laws of Power — Leyes 25-36."""
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
    law(25, "re-create-yourself",
        "La Ley 25 de Greene, «recréate a ti mismo», sostiene que no aceptes los roles que la "
        "sociedad te impone, sino que forjes una identidad nueva que llame la atención y nunca "
        "aburra al público, siendo dueño de tu propia imagen en vez de dejar que otros la "
        "definan, e incorporando recursos dramáticos a tus gestos públicos.", "identidad"),
    law(26, "keep-your-hands-clean",
        "La Ley 26 de Greene, «mantén las manos limpias», afirma que debes parecer un dechado "
        "de civismo y eficiencia, con las manos nunca manchadas por errores ni actos sucios; "
        "para mantener esa apariencia impoluta, usa a otros como chivos expiatorios (scapegoats) "
        "y cat's-paws que disfracen tu implicación en lo desagradable.", "reputacion"),
    law(27, "play-on-need-to-believe",
        "La Ley 27 de Greene, «juega con la necesidad de creer de la gente para crear un "
        "séquito sectario», sostiene que las personas tienen un deseo abrumador de creer en "
        "algo; conviértete en el foco de ese deseo ofreciéndoles una causa o fe nueva, con "
        "palabras vagas pero llenas de promesa, enfatizando el entusiasmo sobre la racionalidad "
        "y el pensamiento claro.", "culto"),
    law(28, "enter-action-with-boldness",
        "La Ley 28 de Greene, «entra en acción con audacia», afirma que si dudas de un curso de "
        "acción no lo intentes, pues tus titubeos infectan la ejecución; la timidez es "
        "peligrosa y es mejor entrar con audacia, ya que cualquier error cometido por audacia "
        "se corrige con más audacia.", "audacia"),
    law(29, "plan-all-the-way-to-the-end",
        "La Ley 29 de Greene, «planifica hasta el final», sostiene que el final lo es todo: "
        "planifica hasta él teniendo en cuenta todas las consecuencias, obstáculos y giros de "
        "fortuna posibles que podrían revertir tu trabajo y dar la gloria a otros, para no "
        "verte abrumado por las circunstancias.", "planificacion"),
    law(30, "make-accomplishments-seem-effortless",
        "La Ley 30 de Greene, «haz que tus logros parezcan sin esfuerzo», afirma que tus "
        "acciones deben parecer naturales y ejecutadas con facilidad, ocultando todo el "
        "esfuerzo, la práctica y los trucos; actúa sin esfuerzo aparente, como si pudieras "
        "hacer mucho más, evitando la tentación de revelar lo duro que fue.", "apariencia"),
    law(31, "control-the-options",
        "La Ley 31 de Greene, «controla las opciones: haz que otros jueguen con las cartas que "
        "tú repartes», sostiene que los mejores engaños son los que parecen dar al otro una "
        "elección: tus víctimas se sienten en control pero son tus marionetas, porque les das "
        "opciones que te benefician elijan la que elijan.", "manipulacion"),
    law(32, "play-to-peoples-fantasies",
        "La Ley 32 de Greene, «juega con las fantasías de la gente», afirma que la verdad se "
        "evita por fea y desagradable, así que nunca apeles a la verdad y la realidad salvo "
        "que estés listo para la ira del desencanto; quien sabe fabricar romance y conjurar "
        "fantasías en una vida dura atrae poder y seguidores.", "fantasia"),
    law(33, "discover-each-mans-thumbscrew",
        "La Ley 33 de Greene, «descubre el punto débil (thumbscrew) de cada cual», sostiene que "
        "todos tienen una debilidad, una grieta en el muro del castillo —normalmente una "
        "inseguridad, una emoción incontrolable o un pequeño placer secreto—, y que una vez "
        "hallada es un tornillo que puedes apretar a tu favor.", "debilidades"),
    law(34, "be-royal-in-your-own-fashion",
        "La Ley 34 de Greene, «sé regio a tu manera: actúa como un rey para ser tratado como "
        "uno», afirma que el modo en que te portas determina cómo te tratan: parecer vulgar o "
        "común hace que te falten el respeto, mientras que actuar con porte regio y seguro de "
        "tu poder hace que los demás te respeten, porque un rey se respeta a sí mismo e inspira "
        "lo mismo.", "porte"),
    law(35, "master-the-art-of-timing",
        "La Ley 35 de Greene, «domina el arte del timing», sostiene que nunca parezcas tener "
        "prisa —la prisa delata falta de control sobre ti y sobre el tiempo—; muéstrate siempre "
        "paciente, como si supieras que todo llegará, y vuélvete un detective del momento "
        "oportuno, olfateando el espíritu y las tendencias de la época.", "timing"),
    law(36, "disdain-what-you-cannot-have",
        "La Ley 36 de Greene, «desdeña lo que no puedes tener: ignorarlo es la mejor "
        "venganza», afirma que al reconocer un problema menor le das existencia y credibilidad, "
        "y que cuanta más atención prestas a un enemigo más fuerte lo haces (un error pequeño "
        "empeora al intentar arreglarlo); a veces lo mejor es dejar las cosas en paz.", "indiferencia"),
]

written, cross = akugen.generate(akus, [], ROOT)
print("WRITTEN:", len(written))
for w in written: print("  ", os.path.relpath(w, ROOT))
