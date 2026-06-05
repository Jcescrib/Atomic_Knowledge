# -*- coding: utf-8 -*-
"""The 48 Laws of Power — Leyes 37-48 (completa las 48)."""
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
    law(37, "create-compelling-spectacles",
        "La Ley 37 de Greene, «crea espectáculos cautivadores», sostiene que la imaginería "
        "impactante y los grandes gestos simbólicos crean el aura del poder porque todos "
        "responden a ellos; monta espectáculos llenos de visuales arrestadores y símbolos "
        "radiantes que realcen tu presencia, de modo que, deslumbrados por las apariencias, "
        "nadie note lo que de verdad haces.", "simbolos"),
    law(38, "think-as-you-like-behave-like-others",
        "La Ley 38 de Greene, «piensa como quieras pero compórtate como los demás», afirma que "
        "si haces alarde de ir contra tu tiempo, exhibiendo ideas heterodoxas, la gente creerá "
        "que solo buscas atención y que los desprecias, y hallará el modo de castigarte por "
        "hacerla sentir inferior; es más seguro guardarte tu disidencia y mezclarte en la "
        "conducta.", "conformidad"),
    law(39, "stir-up-waters-to-catch-fish",
        "La Ley 39 de Greene, «agita las aguas para pescar», sostiene que la ira y la emoción "
        "son estratégicamente contraproducentes y que debes mantenerte siempre calmado y "
        "objetivo; pero si logras enfurecer a tus enemigos mientras tú permaneces tranquilo, "
        "obtienes una ventaja decisiva al desequilibrarlos atacando la grieta de su vanidad.", "provocacion"),
    law(40, "despise-the-free-lunch",
        "La Ley 40 de Greene, «desprecia el almuerzo gratis», afirma que lo que se ofrece "
        "gratis es peligroso porque suele esconder una trampa o una obligación oculta, y que lo "
        "que vale la pena vale pagarlo; pagar tu parte te mantiene libre de gratitud, culpa y "
        "engaño, y a menudo es sabio pagar el precio completo.", "dinero"),
    law(41, "avoid-a-great-mans-shoes",
        "La Ley 41 de Greene, «evita meterte en los zapatos de un gran hombre», sostiene que lo "
        "que ocurre primero siempre parece mejor y más original que lo que viene después, así "
        "que suceder a un gran hombre o tener un padre famoso te obliga a lograr el doble para "
        "eclipsarlos; no te pierdas en su sombra ni te quedes atrapado en un pasado ajeno.", "sucesion"),
    law(42, "strike-the-shepherd",
        "La Ley 42 de Greene, «golpea al pastor y las ovejas se dispersarán», afirma que el "
        "problema suele rastrearse hasta un único individuo fuerte —el agitador, el subordinado "
        "arrogante, el envenenador de la buena voluntad—, y que si le das margen los demás "
        "sucumben a su influencia; no esperes a que sus problemas se multipliquen.", "agitadores"),
    law(43, "work-on-hearts-and-minds",
        "La Ley 43 de Greene, «trabaja sobre los corazones y las mentes de los demás», sostiene "
        "que la coerción genera una reacción que acaba volviéndose en tu contra, así que debes "
        "seducir a otros para que quieran moverse en tu dirección; una persona seducida se "
        "vuelve tu peón leal, y se seduce operando sobre su psicología y debilidades "
        "individuales.", "seduccion"),
    law(44, "mirror-effect",
        "La Ley 44 de Greene, «desarma y enfurece con el efecto espejo», afirma que el espejo "
        "refleja la realidad pero es también la herramienta perfecta del engaño: al reflejar a "
        "tus enemigos haciendo exactamente lo que ellos hacen, no logran descifrar tu "
        "estrategia, y el efecto espejo los burla y humilla, haciéndolos sobrerreaccionar.", "espejo"),
    law(45, "preach-change-but-reform-slowly",
        "La Ley 45 de Greene, «predica la necesidad de cambio, pero nunca reformes demasiado de "
        "golpe», sostiene que todos entienden el cambio en abstracto pero en el día a día son "
        "criaturas de hábito; demasiada innovación es traumática y provoca revuelta, así que si "
        "eres nuevo en el poder o un outsider, invoca el cambio pero implántalo gradualmente.", "cambio"),
    law(46, "never-appear-too-perfect",
        "La Ley 46 de Greene, «nunca parezcas demasiado perfecto», afirma que parecer mejor que "
        "los demás es peligroso, pero lo más peligroso de todo es parecer no tener defectos ni "
        "debilidades, porque la envidia crea enemigos silenciosos; es inteligente exhibir de "
        "vez en cuando defectos y admitir vicios inofensivos para desviar la envidia.", "envidia"),
    law(47, "learn-when-to-stop",
        "La Ley 47 de Greene, «no vayas más allá de la meta que apuntaste: en la victoria, "
        "aprende cuándo parar», sostiene que el momento de la victoria es a menudo el de mayor "
        "peligro, porque en su calor la arrogancia y el exceso de confianza te empujan más allá "
        "del objetivo y, al ir demasiado lejos, creas más enemigos de los que derrotas; no "
        "dejes que el éxito se te suba a la cabeza.", "moderacion"),
    law(48, "assume-formlessness",
        "La Ley 48 de Greene, «asume la falta de forma (formlessness)», sostiene que al tomar "
        "una forma o tener un plan visible te abres al ataque; en vez de ofrecer una forma que "
        "el enemigo pueda agarrar, mantente adaptable y en movimiento, aceptando que nada es "
        "cierto y ninguna ley es fija —la mejor protección es ser tan fluido y formless como "
        "el agua—.", "adaptabilidad"),
]

written, cross = akugen.generate(akus, [], ROOT)
print("WRITTEN:", len(written))
for w in written: print("  ", os.path.relpath(w, ROOT))
