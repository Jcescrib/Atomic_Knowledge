# -*- coding: utf-8 -*-
"""Ingesta — Discipline Equals Freedom, Batch 5 (Me Versus Me -> Laughter Wins, fin Parte 1)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import akugen, akupatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "raw/libros/jocko/discipline-equals-freedom/discipline-equals-freedom.md"
ORIGIN = "Jocko Willink, Discipline Equals Freedom: Field Manual (2017)"
ROOT_AKU = "aku-disciplina-raiz-de-toda-buena-cualidad-concept"
D = "2026-06-05"
DOM = ["liderazgo", "jocko", "disciplina"]

def aku(id, cls, statement, domain, rel=None):
    return {"id": id, "class": cls, "statement": statement, "origin": ORIGIN,
            "domain": domain, "llm_confidence": 0.50, "epistemic_type": "sourced",
            "sources": [SRC], "created": D, "updated": D, "rel": rel or {}}

akus = [
    aku("aku-me-versus-me-superarte-a-ti-mismo-claim", "claim",
        "Todos tenemos límites genéticos —«puedes ser lo que quieras si lo deseas con fuerza» es un cuento—, pero la competición que importa es uno mismo contra uno mismo: ser el mejor YO posible, mejor que ayer; esa victoria se gana a diario en solitario, en la oscuridad, y es una victoria de voluntad y disciplina que nadie te puede arrebatar.",
        DOM + ["superacion"],
        {"related": ["aku-eleccion-vence-naturaleza-y-crianza-claim", "aku-mantener-objetivo-largo-plazo-a-la-vista-claim"]}),
    aku("aku-derrota-por-mil-rendiciones-pequenas-claim", "claim",
        "Casi nadie es derrotado en una sola batalla decisiva, sino lentamente, por una pequeña e insignificante rendición cada vez (dormir un poco más, saltarse un entreno, comer lo que no debe), que va erosionando la voluntad y la disciplina hasta que un día te has vuelto débil sin darte cuenta; por eso hay que permanecer vigilante y mantener la línea en las cosas pequeñas que parecen no importar pero importan.",
        DOM + ["vigilancia"],
        {"related": [ROOT_AKU, "aku-camino-de-menor-resistencia-claim"]}),
    aku("aku-paso-agresivo-hacia-el-miedo-claim", "claim",
        "El miedo es normal; la única forma de afrontarlo es dar el paso, agresivamente, hacia el miedo —eso es entrar en la valentía—: tememos lo que no conocemos, y dejar de esperar, pensar, planificar y excusarse para tomar acción ahora (el primer paso es solo eso: dar el paso, ir) responde a la mayoría de las preguntas («¿cómo voy al gimnasio cada día? Step. Go.»).",
        DOM + ["miedo", "accion"],
        {"related": ["aku-default-agresivo-proactivo-dictar-situacion-claim", "aku-hesitacion-es-el-enemigo-claim", "aku-empezar-aqui-y-ahora-method"]}),
    aku("aku-la-oscuridad-solo-gana-si-la-dejas-claim", "claim",
        "Las tormentas y los tiempos oscuros llegarán y parecerán consumirlo todo, pero la oscuridad no puede extinguir tu luz —tu voluntad y tu determinación—: mientras sigas luchando, ganas; solo la rendición es derrota y solo abandonar es el final, porque la oscuridad solo gana si la dejas.",
        DOM + ["resiliencia"],
        {"related": ["aku-pelear-hasta-el-final-nada-que-perder-claim", "aku-destroyer-mode-emocion-y-logica-concept"]}),
    aku("aku-abrumado-pelear-mas-duro-priorizar-claim", "claim",
        "Cuando la vida te abruma lanzándote muchos problemas a la vez (ley de Murphy), no significa rendirse sino lo contrario: pelear más duro, evaluar los problemas, decidir cuál atacas primero y empezar; deja que esos retos te eleven y te hagan más fuerte en vez de hundirte.",
        DOM + ["adversidad", "priorizacion"],
        {"related": ["aku-prioritize-and-execute-concept", "aku-lider-abrumado-multiples-tareas-falla-claim", "aku-the-warpath-concept"]}),
    aku("aku-ignorar-y-superar-a-los-negativos-claim", "claim",
        "Ante la gente negativa que habla a tus espaldas: a veces hay que enfrentarla con profesionalidad (corregir una acusación seria o algo dañino para el equipo), pero el método preferido es «ignorar y superar» (ignore and outperform): mientras ellos cotillean, tú trabajas y llevas las cosas al siguiente nivel; supéralos en trabajo y resultados a todos.",
        DOM + ["entorno", "foco"],
        {"related": ["aku-mejores-lideres-mision-no-ego-claim", "aku-me-versus-me-superarte-a-ti-mismo-claim"]}),
    aku("aku-no-razonar-con-la-debilidad-solo-actuar-claim", "claim",
        "Todo empieza en la oscuridad cuando suena la alarma: hay que levantarse pese a la fatiga y el dolor, hacerlo rápido y sin pensar, porque no se puede razonar con la debilidad —solo se puede tomar acción—; levántate y ve.",
        DOM + ["accion", "autocontrol"],
        {"related": ["aku-mind-control-controla-tu-propia-mente-concept", "aku-empezar-aqui-y-ahora-method"]}),
    aku("aku-la-risa-gana-claim", "claim",
        "Pese a la oscuridad y el sufrimiento, conviene vivir con diversión y risa: la vida es dura pero se vuelve mucho más fácil cuando te ríes de ella (sobre todo de ti mismo); reírse a pesar de —y para fastidiar a— las dificultades las hace más llevaderas: «laughter wins».",
        DOM + ["actitud", "positividad"],
        {"related": ["aku-good-mindset-concept", "aku-actitud-lider-marca-el-tono-claim"]}),
]

written, cross = akugen.generate(akus, [], ROOT)
print(f"escritos: {len(written)} AKUs")
ops = {}
for src, field, inv, tgt in cross:
    ops.setdefault(tgt, []).append((inv, src))
patch_ops = [{"id": t, "add_rel": rels, "updated": D} for t, rels in ops.items()]
akupatch.apply(ROOT, patch_ops)
for t in ops: print("  ", t, [r[0] for r in ops[t]])
