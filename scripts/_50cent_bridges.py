# -*- coding: utf-8 -*-
"""Cablea los puentes cross-corpus (b) y cross-chapter (a) del corpus 50-cent.
Aprobados por Joan (2026-06-08). Todos `related` bidireccionales (sync 3 capas)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _audit_wire import wire

R = "related"
EDGES = [
    # ── Ch1 ──
    ("aku-un-poco-de-miedo-y-paranoia-es-util-claim", R, "aku-miedo-al-fracaso-es-bueno-claim"),                 # Jocko
    ("aku-al-otro-lado-del-miedo-esta-la-libertad-claim", R, "aku-la-libertad-es-el-valor-supremo-claim"),       # Jocko
    # ── Ch2 ──
    ("aku-cambiar-un-habito-comprometiendote-30-dias-y-enfocando-semana-a-semana-method", R, "aku-never-miss-twice-claim"),                       # Atomic
    ("aku-dormir-lo-suficiente-es-parte-del-hustle-no-su-enemigo-claim", R, "aku-tu-salud-es-la-prioridad-numero-uno-por-encima-de-todo-claim"),   # Naval
    ("aku-un-estilo-de-vida-limpio-sostiene-la-capacidad-de-trabajo-claim", R, "aku-tu-salud-es-la-prioridad-numero-uno-por-encima-de-todo-claim"),# Naval
    ("aku-el-trabajo-duro-es-el-rasgo-comun-a-quienes-se-mantienen-arriba-claim", R, "aku-enamorate-del-aburrimiento-los-profesionales-aparecen-sin-importar-el-animo-claim"),  # Atomic
    ("aku-los-vision-boards-materializan-las-metas-y-elevan-su-probabilidad-claim", R, "aku-compartir-objetivos-compromiso-claim"),                # Power MBA
    # ── Ch3 ──
    ("aku-ser-juez-astuto-de-caracter-es-la-mayor-habilidad-del-emprendedor-concept", R, "aku-judgment-naval-concept"),                            # Naval
    ("aku-ser-juez-astuto-de-caracter-es-la-mayor-habilidad-del-emprendedor-concept", R, "aku-no-bad-teams-only-bad-leaders-concept"),             # Jocko
    ("aku-ser-juez-astuto-de-caracter-es-la-mayor-habilidad-del-emprendedor-concept", R, "aku-48laws-02-never-trust-friends-use-enemies-concept"), # Greene
    ("aku-instila-y-exige-disciplina-tolerancia-cero-al-conflicto-interno-claim", R, "aku-extreme-ownership-concept"),                             # Jocko
    ("aku-el-liderazgo-eficaz-adapta-la-tactica-a-cada-persona-claim", R, "aku-dichotomy-of-leadership-concept"),                                  # Jocko
    ("aku-el-liderazgo-eficaz-adapta-la-tactica-a-cada-persona-claim", R, "aku-liderazgo-situacional-concept"),                                    # Power MBA
    ("aku-cuando-te-meten-un-numero-en-la-cabeza-moverte-de-el-se-siente-como-perdida-claim", R, "aku-nunca-te-fijes-en-un-numero-en-una-negociacion-claim"),  # same-book Ch3<->Ch4 (anclaje)
    ("aku-el-exceso-de-confianza-antes-de-un-reto-te-hace-vulnerable-claim", R, "aku-la-confianza-sin-miedo-viene-de-la-preparacion-claim"),       # same-book Ch3<->Ch1
    # ── Ch4 ──
    ("aku-pedir-equity-es-apostar-por-ti-mismo-claim", R, "aku-no-te-haces-rico-alquilando-tu-tiempo-debes-poseer-equity-claim"),                  # Naval
    ("aku-due-diligence-de-equity-valoracion-vesting-y-abogado-method", R, "aku-equity-value-concept"),                                            # Power MBA
    ("aku-el-tiempo-es-el-gasto-mas-caro-e-irrecuperable-valoralo-sobre-el-cheque-claim", R, "aku-tiempo-recurso-mas-valioso-y-limitado-claim"),   # Jocko
    ("aku-just-do-shit-no-esperes-permiso-de-los-gatekeepers-concept", R, "aku-accountability-bajo-tu-nombre-concept"),                            # Naval
    ("aku-quien-te-emplea-siempre-intentara-pagarte-menos-de-lo-que-vales-claim", R, "aku-no-te-haces-rico-alquilando-tu-tiempo-debes-poseer-equity-claim"),  # Naval
    # ── Ch5 ──
    ("aku-la-meditacion-con-mantra-baja-el-volumen-de-los-pensamientos-method", R, "aku-choiceless-awareness-acepta-sin-juzgar-y-el-90-por-ciento-de-pensamientos-son-miedo-concept"),  # Naval
    ("aku-la-meditacion-con-mantra-baja-el-volumen-de-los-pensamientos-method", R, "aku-meditacion-es-apagar-a-la-sociedad-y-escucharte-y-adopta-muchas-formas-claim"),                 # Naval
    ("aku-evolucionar-o-morir-concept", R, "aku-debes-editar-y-expandir-tu-identidad-continuamente-claim"),                                        # Greene/Atomic identidad
    ("aku-expande-tu-mente-a-traves-de-un-circulo-diverso-y-mas-sabio-claim", R, "aku-juega-juegos-iterados-retornos-del-interes-compuesto-claim"),# Naval (con quien te rodeas)
    ("aku-cambiar-de-opinion-ante-una-perspectiva-nueva-es-evolucion-no-debilidad-claim", R, "aku-judgment-naval-concept"),                        # Naval
    # ── Ch6 ──
    ("aku-act-like-you-dont-need-it-la-neediness-repele-la-inalcanzabilidad-atrae-claim", R, "aku-cialdini-escasez-concept"),                      # Cialdini
    ("aku-crear-percepcion-de-demanda-y-exclusividad-enciende-la-demanda-real-claim", R, "aku-cialdini-escasez-concept"),                          # Cialdini
    ("aku-crear-percepcion-de-demanda-y-exclusividad-enciende-la-demanda-real-claim", R, "aku-tipos-y-tacticas-escasez-concept"),                  # Hormozi
    ("aku-ciertos-bienes-son-senales-que-dictan-si-te-toman-en-serio-claim", R, "aku-branding-concept"),                                           # Power MBA
    ("aku-subvierte-las-expectativas-da-la-energia-opuesta-para-desarmar-claim", R, "aku-48laws-46-never-appear-too-perfect-concept"),             # Greene
    ("aku-el-poder-de-la-percepcion-concept", R, "aku-identidad-de-marca-concept"),                                                                # Power MBA
    ("aku-el-toque-ligero-en-el-antebrazo-aumenta-el-acuerdo-method", R, "aku-cialdini-simpatia-concept"),                                          # Cialdini
    ("aku-fake-it-till-you-make-it-proyecta-exito-antes-de-tenerlo-claim", R, "aku-48laws-37-create-compelling-spectacles-concept"),               # Greene
    # ── Ch7 ──
    ("aku-la-competencia-como-estrategia-if-we-cant-be-friends-concept", R, "aku-48laws-15-crush-your-enemy-totally-concept"),                     # Greene
    ("aku-la-competencia-como-estrategia-if-we-cant-be-friends-concept", R, "aku-48laws-06-court-attention-at-all-cost-concept"),                  # Greene
    ("aku-lleva-un-book-scouting-report-de-tu-competencia-method", R, "aku-cinco-fuerzas-porter-concept"),                                         # Power MBA
    ("aku-enfrentar-a-tu-competencia-de-frente-y-out-trabajarla-da-confianza-duradera-claim", R, "aku-el-diferenciador-decisivo-es-estar-dispuesto-a-out-trabajar-a-todos-claim"),  # same-book Ch7<->Ch2
    ("aku-la-gente-siempre-responde-a-un-competidor-correr-hacia-la-pelea-atrae-miradas-claim", R, "aku-las-negociaciones-no-son-personales-muevete-por-estrategia-no-emocion-claim"),  # same-book Ch7<->Ch4 (sin emocion)
    # ── Ch8 ──
    ("aku-aprender-de-tus-Ls-el-fracaso-como-herramienta-concept", R, "aku-good-mindset-concept"),                                                 # Jocko
    ("aku-aprender-de-tus-Ls-el-fracaso-como-herramienta-concept", R, "aku-establece-un-sistema-de-reflexion-y-revision-de-tus-habitos-method"),   # Atomic
    ("aku-aprender-de-tus-Ls-el-fracaso-como-herramienta-concept", R, "aku-extreme-ownership-concept"),                                            # Jocko
    ("aku-admitir-que-te-equivocaste-es-el-primer-paso-para-aprender-del-error-claim", R, "aku-humildad-asumir-errores-claim"),                    # Jocko
    ("aku-admitir-que-te-equivocaste-es-el-primer-paso-para-aprender-del-error-claim", R, "aku-admitir-que-no-lo-sabes-todo-es-el-requisito-para-crecer-claim"),  # same-book Ch8<->Ch5
    ("aku-rodearte-de-yes-men-impide-aprender-de-tus-errores-claim", R, "aku-cambiar-de-opinion-ante-una-perspectiva-nueva-es-evolucion-no-debilidad-claim"),     # same-book Ch8<->Ch5
    # ── Ch9 ──
    ("aku-toma-responsabilidad-total-incluso-de-lo-que-no-fue-tu-culpa-claim", R, "aku-extreme-ownership-concept"),                                # Jocko
    ("aku-toma-responsabilidad-total-incluso-de-lo-que-no-fue-tu-culpa-claim", R, "aku-accountability-bajo-tu-nombre-concept"),                    # Naval
    ("aku-aceptar-que-todo-depende-de-ti-es-liberador-claim", R, "aku-accountability-bajo-tu-nombre-concept"),                                     # Naval
    ("aku-el-trabajo-duro-crea-felicidad-no-solo-exito-claim", R, "aku-felicidad-es-satisfaccion-el-exito-viene-de-la-insatisfaccion-claim"),      # Naval
    ("aku-pregunta-de-cada-persona-hace-depositos-o-solo-retiros-claim", R, "aku-juega-juegos-iterados-retornos-del-interes-compuesto-claim"),     # Naval
    ("aku-el-want-es-motivador-solo-si-lo-conviertes-en-trabajo-no-en-expectativa-claim", R, "aku-el-deseo-es-un-contrato-para-ser-infeliz-hasta-conseguirlo-concept"),  # Naval (tension)
]

if __name__ == "__main__":
    dry = "--dry" in sys.argv
    wire(EDGES, dry=dry)
