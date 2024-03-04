import reflex as rx
import personal_website.styles.styles as styles
from personal_website.styles.colors import Color, TextColor


def icon_link_button(icon:str, url:str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.icon(tag=icon),
            box_shadow=" 5px 5px 15px #D1D9E6, -5px -5px 15px #ffffff",
            bg="linear-gradient(145deg, #e2e8ec, #ffffff)",
            color= TextColor.TEXT.value,
            _hover= {
                "color": "white",
                "transition": "color 0.4s ease, transform 0.4s ease",  # Transición suave para el cambio de color, fondo y transformación
                "transform": "translateY(-3px)", 
                "box_shadow": "none",
                "bg": Color.PRIMARY.value,
                "cursor": "pointer",
            },
            transition="color 0.4s ease, background_color 0.4s ease, transform 0.4s ease", 
            width="56px",
            height="56px",
            margin_right=styles.EMSize.SMALL.value,
        ),
        href=url,    
        is_external=True
    )

