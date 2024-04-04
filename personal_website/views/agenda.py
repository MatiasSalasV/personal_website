import reflex as rx
import personal_website.styles.styles as styles
from personal_website.styles.colors import Color, TextColor
from personal_website.components.tab_content import tab_content
from personal_website.components.heading import heading

servicio1 = "simple"
servicio2 = "completo"

def agenda() -> rx.Component:
    return rx.hstack(
        rx.chakra.responsive_grid(
            rx.vstack(
                rx.text(
                    "AGENDA AHORA",
                    color=Color.PRIMARY.value,
                    trim="both"
                ),
                heading("Solicita tu servicio"),
                padding_bottom=styles.EMSize.LARGE.value,
            ),

            rx.vstack(
                rx.tabs.root(
                    rx.tabs.list(
                        rx.tabs.trigger(
                            "Simple", 
                            value=servicio1,
                            width="50%",
                            bg=Color.BACKGROUND_GRADIENT.value,
                            border_radius="5px",
                            _before={
                                "background_color":Color.PRIMARY.value,
                            }
                        ),
                        rx.tabs.trigger(
                            "Completo", 
                            value=servicio2,
                            width="50%",
                            bg=Color.BACKGROUND_GRADIENT.value,
                            border_radius="5px",
                            _before={
                                "background_color":Color.PRIMARY.value,
                            }
                        ),
                    ),
                    rx.tabs.content(
                        tab_content(
                            "Asesoría en Digitalización",
                            "45 minutos via Google Meet",
                            "$25.000",
                            """
                                Una sesión para abordar tus desafíos y oportunidades en la era digital. 
                                Juntos analizaremos tus metas, tus recursos y desarrollaremos una estrategia efectiva 
                                para adaptar tu negocio.
                            """
                        ),                      
                        border_radius="5px",
                        value="simple",
                        bg=Color.BACKGROUND_GRADIENT.value,
                        padding=styles.EMSize.DEFAULT.value,
                    ),
                    rx.tabs.content(
                        tab_content(
                            "Pack de Transformación Digital",
                            "45 minutos via Google Meet",
                            "$100.000",
                            """
                                Además de la asesoría, se abarca el desarrollo de una página web estática 
                                y la implementación de un chatbot personalizado, adaptados específicamente a las necesidades 
                                de tu negocio.
                                
                            """
                        ),
                        border_radius="5px",
                        value="completo",
                        bg=Color.BACKGROUND_GRADIENT.value,
                        padding=styles.EMSize.DEFAULT.value,
                    ),
                    default_value=servicio1,
                    border_radius="5px",
                    box_shadow="2px 2px 10px rgba(0, 0, 0, 0.1)",
                    max_width="600px",
                    width="100%"
                ),
                justify="center",
                align="center",
                width="100%"
            ),
            columns=[1,1,1,2,2],
            width="100%",
        ),
        width="100%",
        border_bottom = styles.border_bottom_color,
        padding_y = styles.EMSize.BIGGER.value,
        align="center",
        id="agenda"
    )
