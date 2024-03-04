import reflex as rx
import personal_website.styles.styles as styles
from personal_website.styles.colors import Color, TextColor

def box_timeline(title:str,subtitle:str,place:str,text:str) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.box(
                    rx.heading(f"{title}"),
                    rx.text(f"{subtitle}")
                ),
                rx.link(
                    f"{place}",
                    style=styles.agenda_button, #ESTE SE DEBERIA MODIFICAR PARA QUE NO SE LEVANTE
                ),
                justify="between",
                width="100%"
            ),
            rx.divider(
                margin_y=styles.EMSize.LARGE.value
            ),
            rx.text(
                f"{text}"
            ),
            align_items="start",  # Alinea verticalmente los elementos
            padding_x=styles.EMSize.BIG.value,
            padding_y=styles.EMSize.BIGGER.value,
        ),
        _hover={
            "background": Color.SECONDARY.value,
            "box_shadow":"none",
            "color": "white",
        },  
        max_width="625px",
        bg=Color.BACKGROUND_GRADIENT.value,
        transition="background 0.4s, color 0.4s",
        margin_bottom=styles.EMSize.LARGE.value, #ESTE QUIZA SE MODIFIQUE PARA QUE NO SE PASE PARA ABAJO EL ULITMO (HACER MAS PEQUEÑO)
        border_radius="10px",
        box_shadow="2px 2px 10px rgba(0, 0, 0, 0.1)",

    )


