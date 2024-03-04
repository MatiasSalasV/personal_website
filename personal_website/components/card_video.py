import reflex as rx
import personal_website.styles.styles as styles
from personal_website.styles.colors import Color, TextColor
from personal_website.components.heading import heading
from personal_website.styles.fonts import Font, FontWeight


def card_video(
        image:str,
        title:str, 
        description:str,
        url:str
    ) -> rx.Component:
    
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.box(
                rx.vstack(
                    rx.image(
                        src=image,
                        border_radius="10px",
                    ),
                    rx.text(
                        "VIDEO",
                        color=Color.PRIMARY.value,
                    ),
                    rx.text(
                        title,
                        rx.icon(
                            "arrow-up-right",
                            style={"display": "inline"},
                            margin_right=styles.EMSize.SMALL.value,
                            size=25
                        ),
                        size="5",
                        font_family=Font.TITLE.value,
                        font_weight=FontWeight.MEDIUM.value,
                    ),
                    
                    align_items="start",  # Alinea verticalmente los elementos
                    justify_content="center",  # Centra los elementos horizontalmente
                    height="100%",
                    width="100%",
                    _hover={
                        "color": Color.PRIMARY.value,
                        "transition": "color 0.4s ease, transform 0.4s ease",  # Transición suave para el cambio de color, fondo y transformación
                        "cursor": "pointer",
                    },
                    transition="color 0.4s ease, transform 0.4s ease",  # Aplica la misma transición al estado normal del elemento
                ),
                

                padding=styles.EMSize.DEFAULT.value,
                bg=Color.BACKGROUND_GRADIENT.value,
                margin_bottom=styles.EMSize.SMALL.value,
                border_radius="10px",
                box_shadow="5px 5px 15px #D1D9E6, -5px -5px 15px #ffffff",   
            )
        ),
        rx.dialog.content(
            # rx.html(
            #     '<iframe width="100%" height="315" src="https://www.youtube.com/embed/NXiM9vwEAfk?si=5KLMOYpz7RC0QCAJ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>',
            # ),
            rx.hstack(
                rx.spacer(),
                rx.flex(
                    rx.dialog.close(
                        rx.box(
                            rx.button(
                                rx.icon(tag="x"),
                                variant="ghost",
                                radius="full",
                                style=styles.menu_icon_style
                            )
                        )
                    ),
                    align_items="start",
                ),
                justify="between",
                width="100%",
            ),
            rx.vstack(
                rx.video(
                    url=url,
                    width="100%",
                    height="170px",
                    display=["flex", "none", "none", "none", "none"],
                    padding_bottom=styles.EMSize.DEFAULT.value
                ),
                rx.video(
                    url=url,
                    width="100%",
                    height="315px",
                    display=["none", "flex", "flex", "flex", "flex"],
                    padding_bottom=styles.EMSize.DEFAULT.value
                ),

                heading(title),

                rx.text(
                    description,
                    padding_y=styles.EMSize.DEFAULT.value
                ),



                padding=styles.EMSize.DEFAULT.value
            ),
            padding="0"
        ),
    )



