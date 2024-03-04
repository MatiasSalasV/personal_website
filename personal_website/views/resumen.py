import reflex as rx
import personal_website.styles.styles as styles
from personal_website.styles.colors import Color, TextColor
from personal_website.components.box_timeline import box_timeline

def resumen() -> rx.Component:
    return rx.vstack(
        rx.text(
            "EDUCACIÓN Y EXPERIENCIA",
            color=Color.SECONDARY.value,
            trim="both"
        ),
        rx.heading(
            "Mi Resumen",
            color=TextColor.TITLE.value,
            size="7",
            padding_bottom=styles.EMSize.LARGE.value,
            trim="both"
        ),
        
        rx.tablet_and_desktop(
            rx.hstack(
                rx.chakra.responsive_grid(
                    rx.vstack(
                        rx.text(
                            "2019 - Actualidad",
                            color=Color.SECONDARY.value,
                            trim="both",
                            margin_top=styles.EMSize.DEFAULT.value,
                        ),
                        rx.heading(
                            "Experiencia",
                            color=TextColor.TITLE.value,
                            size="7",
                            padding_bottom=styles.EMSize.LARGE.value,
                            trim="both"
                        ),
                        
                        # Items de experiencia DESKTOP
                        rx.unordered_list(
                            rx.list_item(
                                rx.hstack(
                                    rx.icon(
                                        "circle-dot",
                                        color=Color.BACKGROUND.value,
                                        transform="translate(-14px,60px)",
                                        bg=Color.SECONDARY.value,
                                        border_radius="50%",
                                    ),
                                    box_timeline(
                                        "Fundador, CEO",
                                        "Adaptate.IA - (Junio 2023 - Actualidad)",
                                        "Online",
                                        "Fundador de una empresa digital que se encarga de digitalizar procesos mediante inteligencia artificial"
                                    ),
                                ),
                                border_left = "4px solid #dce1e4",
                            ),
                            rx.list_item(
                                rx.hstack(
                                    rx.icon(
                                        "circle-dot",
                                        color=Color.BACKGROUND.value,
                                        transform="translate(-14px,60px)",
                                        bg=Color.SECONDARY.value,
                                        border_radius="50%"
                                    ),
                                    box_timeline(
                                        "Analista de Datos",
                                        "PUC - (Agosto 2023 - Enero 2024)",
                                        "Santiago, Chile",
                                        "Encargado de automatizar procesos de extracción, limpieza y carga de datos para su posterior analisis y visualización."
                                    ),
                                ),
                                border_left = "4px solid #dce1e4",
                            ),
                            rx.list_item(
                                rx.hstack(
                                    rx.icon(
                                        "circle-dot",
                                        color=Color.BACKGROUND.value,
                                        transform="translate(-14px,60px)",
                                        bg=Color.SECONDARY.value,
                                        border_radius="50%"
                                    ),
                                    box_timeline(
                                        "Ingeniero de Procesos",
                                        "PUC - (Marzo 2023 - Julio 2023)",
                                        "Santiago, Chile",
                                        "Encargado de apoyar al proceso de mejora continua de la organización. Levantamiento, diagramación y optimización de procesos."
                                    ),
                                ),
                                border_left = "4px solid #dce1e4",
                            ),
                            list_style_type="none",
                        ),
                    ),
                    rx.vstack(
                        rx.text(
                            "2014 - 2023",
                            color=Color.SECONDARY.value,
                            trim="both",
                            margin_top=styles.EMSize.DEFAULT.value,
                        ),
                        rx.heading(
                            "Educación",
                            color=TextColor.TITLE.value,
                            size="7",
                            padding_bottom=styles.EMSize.LARGE.value,
                            trim="both"
                        ),
                        
                        # Items de educación DESKTOP
                        rx.unordered_list(
                            rx.list_item(
                                rx.hstack(
                                    rx.icon(
                                        "circle-dot",
                                        color=Color.BACKGROUND.value,
                                        transform="translate(-14px,60px)",
                                        bg=Color.SECONDARY.value,
                                        border_radius="50%"
                                    ),
                                    box_timeline(
                                        "Ingenieria en Informática",
                                        "Duoc UC (2019-2023)",
                                        "Tecnologia",
                                        "Estudios en los cuales obtuve conocimientos y habilidades en informatica como programacion, datos, proyectos"
                                    ),
                                ),
                                border_left = "4px solid #dce1e4",
                            ),
                            rx.list_item(
                                rx.hstack(
                                    rx.icon(
                                        "circle-dot",
                                        color=Color.BACKGROUND.value,
                                        transform="translate(-14px,60px)",
                                        bg=Color.SECONDARY.value,
                                        border_radius="50%"
                                    ),
                                    box_timeline(
                                        "Ingenieria en Informática",
                                        "Duoc UC (2019-2023)",
                                        "Tecnologia",
                                        "Estudios en los cuales obtuve conocimientos y habilidades en informatica como programacion, datos, proyectos"
                                    ),
                                ),
                                border_left = "4px solid #dce1e4",
                            ),
                            
                            list_style_type="none",
                        ),
                    ),
                    columns=[1,1,1,2]
                ),
            ),
        ),

                   # Items de educacion MOBILE
                  

        align="center",
        width="100%",
        border_bottom = styles.border_bottom_color,
        padding_y = styles.EMSize.BIGGER.value
    )