import reflex as rx
import personal_website.styles.styles as styles
from personal_website.styles.colors import Color, TextColor
from personal_website.components.heading import heading

def tab_content(title:str, subtitle:str, price:str, description:str) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.vstack(
                heading(title),
                rx.text(f"{subtitle}"),
            ), 
            rx.link(
                f"{price}",
                style=styles.agenda_button, #ESTE SE DEBERIA MODIFICAR PARA QUE NO SE LEVANTE
            ),
            justify="between",
            width="100%"
        ),
        rx.text(
            f"{description}",
            padding_y=styles.EMSize.DEFAULT.value
        ),
        rx.chakra.responsive_grid(
            rx.vstack( 
                rx.text(
                    rx.icon(
                        "check",
                        color=Color.PRIMARY.value,
                        style={"display": "inline"},
                        margin_right=styles.EMSize.SMALL.value
                    ),
                    "texto"
                ),
                rx.text(
                    rx.icon(
                        "check",
                        color=Color.PRIMARY.value,
                        style={"display": "inline"},
                        margin_right=styles.EMSize.SMALL.value
                    ),
                    "texto"
                ),
                align_items="start",
                margin_bottom=styles.EMSize.SMALL.value
            ),
            rx.vstack(
                rx.text(
                    rx.icon(
                        "check",
                        color=Color.PRIMARY.value,
                        style={"display": "inline"},
                        margin_right=styles.EMSize.SMALL.value
                    ),
                    "texto"
                ),
                rx.text(
                    rx.icon(
                        "check",
                        color=Color.PRIMARY.value,
                        style={"display": "inline"},
                        margin_right=styles.EMSize.SMALL.value
                    ),
                    "texto"
                ),
                align_items="start",
                margin_bottom=styles.EMSize.SMALL.value
            ),
            width="100%",
            columns=[1,1,1,2,2],
        ),
        rx.vstack(
            rx.link(
                "AGENDA AHORA ",
                rx.icon(
                    "arrow-right",
                    color=Color.PRIMARY.value,
                    style={"display": "inline"},
                ),
                style=styles.agenda_button, #ESTE SE DEBERIA MODIFICAR PARA QUE NO SE LEVANTE
            ),
            rx.chakra.responsive_grid(
                rx.vstack( 
                    rx.text(
                        rx.icon(
                            "clock",
                            style={"display": "inline"},
                            margin_right=styles.EMSize.SMALL.value,
                            width="15px",
                            height="15px"
                        ),
                        "Agenda en tu calendario",
                        size="1",
                        color=Color.OPACO.value,
                    ),
                    align_items="center",
                ),
                rx.vstack(
                    rx.text(
                        rx.icon(
                            "shield",
                            style={"display": "inline"},
                            margin_right=styles.EMSize.SMALL.value,
                            width="15px",
                            height="15px"
                        ),
                        "Garantia de devolución del 100%",
                        size="1",
                        color=Color.OPACO.value,
                    ),
                    align_items="center",
                ),
                columns=[1,1,1,2,2],
                padding_top=styles.EMSize.MEDIUM.value
            ),
            justify="center",
            align="center",
            width="100%",
            padding_y=styles.EMSize.LARGE.value
        ),
        padding_top=styles.EMSize.DEFAULT.value
    )



