import reflex as rx
import personal_website.styles.styles as styles
import personal_website.constants as const
from personal_website.styles.colors import Color, TextColor
from personal_website.components.icon_link_button import icon_link_button


def footer() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.link(
                rx.box(
                    rx.text("Matias", as_="span"),
                    rx.text("SV", as_="span", color=Color.PRIMARY.value),
                    style=styles.navbar_title_style
                ),
                href="https://x.com",
                is_external=True, #DESPUES CAMBIAR A FALSE Y PONER RUTA localhost:3000/
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
            height="100%",
            spacing="3",
            width="100%",
            justify="end",
            margin_bottom=styles.EMSize.BIG.value
        ),
        rx.vstack(
            rx.text(
                "ENLACES RÁPIDOS",
                color=Color.PRIMARY.value,
            ),
            rx.link(
                "Lo Que Hago",
                padding_y=styles.EMSize.SMALL.value
            ),
            rx.link(
                "YouTube",
                padding_y=styles.EMSize.SMALL.value
            ),
            rx.link(
                "Resumen",
                padding_y=styles.EMSize.SMALL.value
            ),
            rx.link(
                "Reserva una Hora",
                padding_y=styles.EMSize.SMALL.value
            ),
            width="100%",
        ),

        width="100%",
        padding_y=styles.EMSize.BIGGER.value,
        padding_x=styles.EMSize.MEDIUM.value,
        border_bottom = styles.border_bottom_color,
        flex_direction=["column","row"],
    )