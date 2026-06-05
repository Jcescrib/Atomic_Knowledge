# -*- coding: utf-8 -*-
"""The 48 Laws of Power — Leyes 13-24."""
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
    law(13, "appeal-to-self-interest",
        "La Ley 13 de Greene, «cuando pidas ayuda, apela al interés propio del otro, nunca a "
        "su misericordia o gratitud», afirma que recordar a un aliado tus favores pasados hace "
        "que te ignore; en cambio, descubre y exagera lo que tu petición le aporta a él, porque "
        "responderá con entusiasmo cuando vea algo que ganar para sí mismo.", "interes-propio"),
    law(14, "pose-as-friend-work-as-spy",
        "La Ley 14 de Greene, «posa como amigo, trabaja como espía», sostiene que conocer a tu "
        "rival es crítico: usa espías para ir un paso por delante y, mejor aún, haz tú de espía "
        "sondeando en los encuentros sociales con preguntas indirectas que revelen las "
        "debilidades e intenciones del otro, pues toda ocasión es una oportunidad de espionaje "
        "sutil.", "informacion"),
    law(15, "crush-your-enemy-totally",
        "La Ley 15 de Greene, «aplasta a tu enemigo por completo», afirma que un enemigo "
        "temido debe ser aniquilado totalmente, porque si queda una sola brasa encendida el "
        "fuego acabará reavivándose; se pierde más deteniéndose a medias que con la "
        "aniquilación total; se invierte cuando aplastar provoca mártires o conviene la "
        "clemencia estratégica.", "enemigos"),
    law(16, "use-absence-to-increase-respect",
        "La Ley 16 de Greene, «usa la ausencia para aumentar el respeto y el honor», sostiene "
        "que el exceso de circulación baja el precio —cuanto más te ven, más común pareces—, "
        "así que, una vez establecido en un grupo, retirarte temporalmente hace que hablen más "
        "de ti y te admiren más; implica saber cuándo marcharte y crear valor por escasez.", "escasez"),
    law(17, "cultivate-unpredictability",
        "La Ley 17 de Greene, «mantén a los demás en terror suspendido: cultiva un aire de "
        "imprevisibilidad», afirma que los humanos son criaturas de hábito que necesitan ver "
        "familiaridad y predictibilidad para sentir control; ser deliberadamente impredecible "
        "invierte la mesa, desconcierta al adversario y lo obliga a la defensiva.", "imprevisibilidad"),
    law(18, "isolation-is-dangerous",
        "La Ley 18 de Greene, «no construyas fortalezas para protegerte: el aislamiento es "
        "peligroso», sostiene que aunque la fortaleza parezca lo más seguro, el aislamiento te "
        "expone a más peligros de los que evita —te corta de información valiosa y te vuelve "
        "conspicuo y blanco fácil—; implica mezclarse y circular en lugar de encerrarse.", "aislamiento"),
    law(19, "know-who-you-deal-with",
        "La Ley 19 de Greene, «conoce con quién tratas: no ofendas a la persona equivocada», "
        "afirma que las personas reaccionan de modos muy distintos y que engañar u ofender a "
        "ciertos individuos (lobos con piel de cordero) los lleva a buscar venganza de por "
        "vida; implica calibrar siempre a la contraparte antes de actuar contra ella.", "evaluar-personas"),
    law(20, "do-not-commit-to-anyone",
        "La Ley 20 de Greene, «no te comprometas con nadie», sostiene que solo el necio corre "
        "a tomar partido: no comprometerte con ningún bando ni causa salvo contigo mismo "
        "preserva tu independencia y te vuelve dueño de los demás, jugándolos unos contra "
        "otros y haciendo que te cortejen (dar esperanza pero nunca satisfacción).", "independencia"),
    law(21, "play-a-sucker-to-catch-a-sucker",
        "La Ley 21 de Greene, «hazte el tonto para cazar a un tonto: parece más torpe que tu "
        "objetivo», afirma que a nadie le gusta sentirse más estúpido que el otro, así que el "
        "truco es hacer que tus víctimas se sientan listas —y más listas que tú—, pues "
        "convencidas de ello nunca sospecharán que tienes motivos ocultos.", "engano"),
    law(22, "use-the-surrender-tactic",
        "La Ley 22 de Greene, «usa la táctica de la rendición: transforma la debilidad en "
        "poder», sostiene que cuando eres más débil nunca pelees por honor sino que te rindas: "
        "rendirte te da tiempo para recuperarte, atormentar al vencedor y esperar a que su "
        "poder mengüe, negándole la satisfacción de derrotarte en combate.", "debilidad"),
    law(23, "concentrate-your-forces",
        "La Ley 23 de Greene, «concentra tus fuerzas», afirma que debes conservar tus energías "
        "manteniéndolas concentradas en su punto más fuerte: se gana más hallando una mina "
        "rica y cavándola hondo que saltando de una mina superficial a otra, porque la "
        "intensidad vence a la extensidad cada vez.", "foco"),
    law(24, "play-the-perfect-courtier",
        "La Ley 24 de Greene, «sé el cortesano perfecto», sostiene que en un mundo que gira en "
        "torno al poder y la destreza política, el cortesano perfecto domina el arte de la "
        "indirección: halaga, cede ante los superiores y ejerce poder sobre los demás del modo "
        "más oblicuo y elegante, aprendiendo las leyes de la corte para ascender sin límite.", "cortesania"),
]

written, cross = akugen.generate(akus, [], ROOT)
print("WRITTEN:", len(written))
for w in written: print("  ", os.path.relpath(w, ROOT))
