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
            heading("Soy Matias Salas Vergara", True),
            heading("un emprendedor digital"),
            rx.text("""
                I help my clients build powerful AI solutions to keep them one step ahead of the competition. 
                With AI affecting every industry at a rapid pace, those who make bold strides have a chance to increase 
                their market share. Sharing my knowledge with other entrepreneurs for free on YouTube.""", 
                padding_y=styles.Size.SMALL.value  ,
                color=TextColor.TEXT.value
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
                        icon_link_button("linkedin", const.LINKEDIN_URL),
                        icon_link_button("youtube",const.YOUTUBE_URL),
                        icon_link_button("twitter", const.TWITTER_URL), 
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
                width="400px",
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
        padding_y = styles.EMSize.BIGGER.value
        
    )



