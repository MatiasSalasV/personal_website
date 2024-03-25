import reflex as rx
import personal_website.styles.styles as styles
import personal_website.constants as const
from personal_website.styles.fonts import Font, FontWeight
from personal_website.styles.colors import Color, TextColor
from personal_website.components.heading import heading
from personal_website.components.icon_link_button import icon_link_button
from personal_website.components.icon_skill import icon_skill


def header() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.text(
                "BIENVENIDO", 
                color=TextColor.TEXT.value
            ),
            heading("Soy Matias Salas Vergara"),
            heading("tu aliado en la era digital"),
            #  Transformo la complejidad tecnológica en ventaja competitiva para tu negocio, 
            #         a través de la automatización y digitalización. 
            # Te ayudo a sacar provecho de la tecnologia a través de la automatización y la digitalización de tu negocio
            #         para estar un paso por delante de la competencia.
                   
            #         En una era donde la innovación tecnológica redefine constantemente las reglas 
            #         del juego, los más innovadores y proactivos tienen la ventaja de expandir su 
            #         influencia y capturar nuevas oportunidades.      
            # En una era donde la innovación tecnológica redefine constantemente las reglas del juego, aquellos que 
            #     dan pasos audaces tienen la ventaja de capturar nuevas oportunidades.  
            rx.text(
                """
                Te ayudo a digitalizar y automatizar tu negocio para estar un paso por delante de la competencia.
                Dado que la tecnologia afecta a todas las industrias, aquellos que dan pasos audaces tienen la ventaja 
                de capturar nuevas oportunidades.
                
                
                
            
                """, 
                padding_y=styles.Size.SMALL.value ,
                color=TextColor.TEXT.value,
                max_width= "70ch",
            ),
            rx.flex(
                rx.vstack(
                    rx.text(
                        "CONECTA",
                        font_weight=FontWeight.MEDIUM.value,
                        padding_y=styles.EMSize.SMALL.value,
                        color=TextColor.TEXT.value
                    ),     
                    rx.hstack(
                        icon_link_button(
                            "linkedin", 
                            const.LINKEDIN_URL,
                            "LinkedIn"
                        ),
                        icon_link_button(
                            "youtube",
                            const.YOUTUBE_URL,
                            "YouTube"
                        ),
                        icon_link_button(
                            "twitter", 
                            const.TWITTER_URL,
                            "Twitter"
                        ), 
                        padding_bottom=styles.EMSize.LARGE.value
                    ),
                    align_items="start",
                    width="100%",
                ),
                rx.vstack(
                    rx.text(
                        "HABILIDADES",
                        font_weight=FontWeight.MEDIUM.value,
                        padding_y=styles.EMSize.SMALL.value,
                        color=TextColor.TEXT.value
                    ),     
                    rx.hstack(
                        # icon_skill(
                        #     "icons/openai.svg",
                        #     "OpenAI"
                        # ),
                        # icon_skill(
                        #     "icons/python.svg",
                        #     "Python"
                        # ),
                        # icon_skill(
                        #     "icons/camera.svg",
                        #     "Video"
                        # ), 
                        
                        icon_skill(
                            "icons/python.svg",
                            "Python"
                        ),
                        icon_skill(
                            "icons/openai.svg",
                            "OpenAI"
                        ),
                        icon_skill(
                            "icons/video.svg",
                            "Video"
                        ), 
                    ),
                    align_items="start",
                    width="100%",
                ),
                width="100%",
                padding_top=styles.EMSize.BIGGER.value,
                padding_bottom=styles.EMSize.BIG.value,
                flex_direction=["column","row"],
            ),
            
            align_items="start",
            padding_y=styles.EMSize.DEFAULT.value,
        ),

        rx.vstack(
            rx.box(
                width="500px",
                height="400px",
                color="red",
                bg=Color.SECONDARY.value,
                
            ),
            display=["none", "none", "none", "flex", "flex"],
            padding= styles.EMSize.DEFAULT.value,
            justify="center",
            align="center"
        ),

        # rx.avatar(
        #     src="https://liamottley.com/wp-content/uploads/2023/03/Liam-01.png", 
        #     fallback="RU", 
        #     size="9",
        #     display=["none", "none", "none", "flex", "flex"],
        # ),

        # height="70vh",
        width="100%",
        border_bottom = styles.border_bottom_color,
        align="center",
        justify="between",
        padding_y = styles.EMSize.BIGGER.value,
        id="inicio"
        
    )



