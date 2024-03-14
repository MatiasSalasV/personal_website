import reflex as rx
import personal_website.styles.styles as styles
import personal_website.constants as const
from personal_website.styles.fonts import Font, FontWeight
from personal_website.styles.colors import Color, TextColor
from personal_website.components.icon_link_button import icon_link_button


def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.box(
                rx.text("Matias", as_="span"),
                rx.text("SV", as_="span", color=Color.PRIMARY.value),
                style=styles.navbar_title_style
            ),
            href="/",
            is_external=True, #DESPUES CAMBIAR A FALSE Y PONER RUTA localhost:3000/
        ),

        rx.spacer(),

        rx.desktop_only(
            rx.link(
                "INICIO",
                padding=styles.EMSize.DEFAULT.value,
            ),
            rx.link(
                "LO QUE HAGO",
                padding=styles.EMSize.DEFAULT.value
            ),
            rx.link(
                "YOUTUBE",
                padding=styles.EMSize.DEFAULT.value
            ),
            rx.link(
                "RESUMEN",
                padding=styles.EMSize.DEFAULT.value
            ),
            rx.link(
                "CONTÁCTAME",
                style=styles.agenda_button
            ),      
            # rx.theme_panel(default_open=True)      
        ),

        rx.mobile_and_tablet(
            rx.drawer.root(
                rx.drawer.trigger(
                    rx.button(
                        rx.icon(tag="menu"),
                        variant="ghost",
                        radius="full",
                        style=styles.menu_icon_style
                    ),
                ),
                rx.drawer.overlay(),
                rx.drawer.portal(
                    rx.drawer.content(
                        rx.vstack(
                            rx.hstack(
                                rx.avatar(
                                    fallback="MSV",
                                    size=styles.Size.VERY_BIG.value
                                ),
                                rx.flex(
                                    rx.drawer.close(
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
                                width="100%"
                            ),
                            rx.text(
                                "I help my clients build powerful AI solutions to keep them one step ahead of the competition.",
                                style=styles.text_presentation_mobile,
                            ),
                            rx.vstack(
                                rx.link(
                                    "INICIO",
                                    padding_y=styles.EMSize.SMALL.value
                                ),
                                rx.link(
                                    "LO QUE HAGO",
                                    padding_y=styles.EMSize.SMALL.value
                                ),
                                rx.link(
                                    "YOUTUBE",
                                    padding_y=styles.EMSize.SMALL.value
                                ),
                                rx.link(
                                    "RESUMEN",
                                    padding_y=styles.EMSize.SMALL.value
                                ),
                                # agenda_button("RESERVA TU HORA", "https://x.com"),
                                align_items="start",
                                padding_y=styles.EMSize.BIG.value,
                            ),
                            rx.text(
                                "ENCUENTRAME EN",
                                font_weight=FontWeight.MEDIUM.value,
                                color=TextColor.TEXT.value
                            ),
                        
                            rx.hstack(
                                icon_link_button("linkedin", const.LINKEDIN_URL),
                                icon_link_button("youtube",const.YOUTUBE_URL),
                                icon_link_button("twitter", const.TWITTER_URL), 
                            ),
                        ),
                        
                        height="100%",
                        width="85%",
                        padding=styles.EMSize.LARGE.value,
                        background_color=Color.BACKGROUND.value
                    )
                ),
                direction="left",
            ),
        ),
        border_bottom = styles.border_bottom_color,
        padding_y=styles.EMSize.DEFAULT.value,
        padding_x=styles.EMSize.BIG.value,
        align="center",
        position="sticky",
        z_index="999",
        top="0",
        bg=Color.BACKGROUND.value,
        box_shadow= "0px 4px 6px rgba(0, 0, 0, 0.1)"
    )