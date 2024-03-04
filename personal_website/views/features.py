import reflex as rx
import personal_website.styles.styles as styles
from personal_website.styles.colors import Color, TextColor
from personal_website.components.card_feature import card_feature
from personal_website.components.heading import heading

def features() -> rx.Component:
    return rx.vstack(
        rx.text(
            "CARACTERISTICAS",
            color=Color.PRIMARY.value,
            trim="both"
        ),
        heading("Lo que hago"),

        rx.chakra.responsive_grid(
            card_feature("bot","Desarrollo de Bots", "Texto para el primer card de pucartexto para el primer card de pucartexto para el primer card de pucar"),
            card_feature("cpu","Desarrollo Web", "Texto para el primer card de pucartexto para el primer card de pucartexto para el primer card de pucar"),
            card_feature("film","Creación de Contenido", "Texto para el primer card de pucartexto para el primer card de pucartexto para el primer card de pucar"),
            spacing="5",
            padding_top=styles.EMSize.LARGE.value,
            columns=[1,1,2, 3],
        ),
        
        align="center",
        width="100%",
        border_bottom = styles.border_bottom_color,
        padding_y = styles.EMSize.BIGGER.value
    )