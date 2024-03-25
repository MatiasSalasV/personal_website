import reflex as rx
import personal_website.styles.styles as styles
from personal_website.styles.colors import Color, TextColor
from personal_website.components.heading import heading


def card_feature(icon:str,title:str, text:str, url:str, external:bool) -> rx.Component:
    return rx.link(
        rx.box(
            rx.vstack(
                rx.icon(
                    tag=f"{icon}", 
                    # color=Color.SECONDARY.value, 
                    # width=styles.EMSize.BIGGER.value,
                    # height=styles.EMSize.BIGGER.value,
                    size=70,
                    margin_bottom = styles.EMSize.DEFAULT.value,
                ),
                heading(title),
                rx.text(
                    f"{text}",
                    margin_y = styles.EMSize.SMALL.value,
                ),
                rx.icon(
                    tag="arrow-right", 
                    color=Color.BACKGROUND.value,
                    width=styles.EMSize.BIG.value,
                    height=styles.EMSize.BIG.value,
                ),
                align_items="start",  # Alinea verticalmente los elementos
                justify_content="center",  # Centra los elementos horizontalmente
                height="100%",
                width="100%",
                _hover={
                    "color": "white",
                    "transition": "color 0.4s ease, transform 0.4s ease",  # Transición suave para el cambio de color, fondo y transformación
                    "transform": "translateY(-20px)",  # Movemos el contenido hacia arriba al hacer hover
                },
                transition="color 0.2s ease, transform 0.2s ease",  # Aplica la misma transición al estado normal del elemento
            ),
            
            _hover={
                "background": Color.SECONDARY.value,
                "box_shadow":"none",
                "cursor": "pointer",
            },  
            
            bg=Color.BACKGROUND_GRADIENT.value,
            transition="background 0.4s",
            margin_bottom=styles.EMSize.SMALL.value,
            border_radius="10px",
            box_shadow="2px 2px 10px rgba(0, 0, 0, 0.1)",
            padding_x=styles.EMSize.BIG.value,
            padding_y=styles.EMSize.BIGGER.value,
        ),
        href=url,
        is_external=external,
    )



