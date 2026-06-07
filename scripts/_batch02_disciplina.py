# -*- coding: utf-8 -*-
"""Batch 02 — puentes cross-corpus DISCIPLINA/HABITOS/EGO (jocko/james-clear/naval)."""
import sys
from _audit_wire import wire
EDGES = [
 ("aku-discipline-equals-freedom-concept","related","aku-los-habitos-crean-libertad-no-la-restringen-claim"),
 ("aku-disciplina-da-libertad-de-maniobra-claim","related","aku-los-habitos-crean-libertad-no-la-restringen-claim"),
 ("aku-te-conviertes-en-tus-habitos-y-cambiarlos-es-un-viaje-de-anos-claim","related","aku-tu-identidad-emerge-de-tus-habitos-claim"),
 ("aku-descondicionate-revisa-si-tus-habitos-aun-te-sirven-claim","related","aku-debes-editar-y-expandir-tu-identidad-continuamente-claim"),
 ("aku-metodo-de-cambio-de-habitos-la-autodisciplina-es-un-puente-a-una-nueva-autoimagen-method","related","aku-proceso-de-dos-pasos-para-cambiar-tu-identidad-method"),
 ("aku-metodo-de-cambio-de-habitos-la-autodisciplina-es-un-puente-a-una-nueva-autoimagen-method","related","aku-implementation-intention-method"),
 ("aku-di-a-tus-amigos-que-eres-feliz-para-conformarte-a-ello-claim","related","aku-cada-accion-es-un-voto-por-el-tipo-de-persona-que-quieres-ser-claim"),
 ("aku-evolucionamos-para-la-escasez-pero-vivimos-en-abundancia-claim","related","aku-entorno-de-recompensa-inmediata-vs-diferida-concept"),
 ("aku-evolucionamos-para-la-escasez-pero-vivimos-en-abundancia-claim","related","aku-estimulos-supernormales-concept"),
 ("aku-la-lucha-moderna-individuos-vs-ejercitos-que-explotan-la-abundancia-concept","related","aku-estimulos-supernormales-concept"),
 ("aku-elecciones-faciles-vida-dificil-elecciones-dificiles-vida-facil-claim","related","aku-pequenas-elecciones-diarias-construyen-todo-claim"),
 ("aku-haz-algo-fisico-cada-dia-el-mejor-ejercicio-es-el-que-haras-cada-dia-claim","related","aku-los-habitos-se-forman-por-frecuencia-no-por-tiempo-claim"),
 ("aku-lee-lo-que-amas-hasta-que-ames-leer-claim","related","aku-construye-habitos-que-encajen-con-tu-personalidad-big-five-concept"),
 ("aku-comida-basura-es-veneno-claim","related","aku-estimulos-supernormales-concept"),
 ("aku-el-deseo-y-el-ego-nublan-la-realidad-claim","related","aku-ego-nubla-todo-claim"),
 ("aku-la-insignificancia-del-yo-ayuda-a-la-felicidad-claim","related","aku-el-ego-mas-dificil-es-el-propio-claim"),
 ("aku-no-te-tomes-tan-en-serio-eres-un-mono-con-un-plan-claim","related","aku-check-the-ego-concept"),
 ("aku-mejora-metodica-de-tu-baseline-de-felicidad-method","related","aku-redefinir-agotamiento-eleva-baseline-claim"),
 ("aku-no-cuentes-con-motivacion-cuenta-disciplina-claim","related","aku-enamorate-del-aburrimiento-los-profesionales-aparecen-sin-importar-el-animo-claim"),
 ("aku-compartir-objetivos-compromiso-claim","related","aku-habit-contract-y-accountability-partner-method"),
]
if __name__=="__main__": wire(EDGES, dry="--dry" in sys.argv)
