# -*- coding: utf-8 -*-
"""Batch 00 — puentea las 3 islas (componentes pequeños) al componente principal."""
import sys
from _audit_wire import wire

EDGES = [
    # --- Isla 1: Atomic Habits (autocontrol / cues / contexto / entorno) ---
    # El contexto-es-el-cue (concept) sustenta el metodo de disenar el entorno.
    ("aku-el-contexto-es-el-cue-un-espacio-un-uso-concept", "supports",
     "aku-disena-tu-entorno-se-su-arquitecto-no-su-victima-method"),
    # context=cue y el habit-loop definen el mismo objeto (cue) desde angulos distintos.
    ("aku-el-contexto-es-el-cue-un-espacio-un-uso-concept", "related",
     "aku-habit-loop-cue-craving-response-reward-concept"),
    # "autocontrol corto plazo / hazlo invisible" es la inversion de la 1a Ley del framework.
    ("aku-el-autocontrol-es-de-corto-plazo-haz-invisibles-los-cues-de-los-malos-habitos-claim", "supports",
     "aku-cuatro-leyes-del-cambio-de-conducta-concept"),

    # --- Isla 2: Naval salud / prioridades ---
    ("aku-tu-salud-es-la-prioridad-numero-uno-por-encima-de-todo-claim", "related",
     "aku-riqueza-salud-felicidad-se-persiguen-en-ese-orden-pero-importan-al-reves-claim"),
    ("aku-salud-amor-y-mision-en-ese-orden-nada-mas-importa-claim", "related",
     "aku-riqueza-salud-felicidad-se-persiguen-en-ese-orden-pero-importan-al-reves-claim"),
    ("aku-tu-salud-es-la-prioridad-numero-uno-por-encima-de-todo-claim", "supports",
     "aku-formula-de-la-felicidad-de-naval-salud-riqueza-relaciones-method"),

    # --- Isla 3: Naval retiro / libertad financiera ---
    ("aku-tres-caminos-al-retiro-concept", "related",
     "aku-wealth-activos-que-ganan-mientras-duermes-concept"),
    ("aku-no-te-haces-rico-alquilando-tu-tiempo-debes-poseer-equity-claim", "supports",
     "aku-tres-caminos-al-retiro-concept"),
]

if __name__ == "__main__":
    wire(EDGES, dry="--dry" in sys.argv)
