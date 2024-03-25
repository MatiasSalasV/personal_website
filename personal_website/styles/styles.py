from enum import Enum
import reflex as rx
from .fonts import Font, FontWeight
from .colors import Color, TextColor

MAX_WIDTH = "1350px"

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap",
    # "/css/styles.css"
]


class EMSize(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    BIGGER = "4em"


class Size(Enum):
    ZERO = "0"
    SMALL = "2"
    MEDIUM="3"
    DEFAULT = "4"
    LARGE = "6"
    BIG = "7"
    BIGGER = "8"
    VERY_BIG = "9"


BASE_STYLE = {
    "background_color": Color.BACKGROUND.value,
    "font_family": Font.DEFAULT.value,
    "font_weight":FontWeight.LIGHT.value,

    # rx.text: {
    #     "color":TextColor.TEXT.value
    # },

    rx.link: {
        # "padding":Size.DEFAULT.value,
        "color":TextColor.TITLE.value,
        "text_decoration": "none",
        "_hover": {
            "color":Color.PRIMARY.value,
            "transition": "color 0.4s ease, transform 0.4s ease",
        },
        "transition":"color 0.4s ease, transform 0.4s ease",
    }
    
}

border_bottom_color = "1px solid #dce1e4"
divider_bottom_color = "#dce1e4"

menu_icon_style= dict(
    color=Color.PRIMARY.value,
    padding=EMSize.DEFAULT.value,
    margin="0",
    box_shadow=" 5px 5px 15px #D1D9E6, -5px -5px 15px #ffffff",
    bg="linear-gradient(145deg, #e2e8ec, #ffffff)",
    _hover= {
        "transform": "scale(1.1)", 
        "cursor": "pointer",
    },
    transition="transform 0.4s ease", 
)

agenda_button = dict(
    color = Color.PRIMARY.value,
    font_family = Font.DEFAULT.value,
    font_weight = FontWeight.MEDIUM.value,
    padding= EMSize.SMALL.value,
    border_radius="25px",
    box_shadow=" 5px 5px 15px #D1D9E6, -5px -5px 15px #ffffff",
    bg="linear-gradient(145deg, #e2e8ec, #ffffff)",
    _hover= {
        "color": "white",
        "transition": "color 0.4s ease, transform 0.4s ease",  # Transición suave para el cambio de color, fondo y transformación
        # "transform": "translateY(-3px)", 
        "box_shadow": "none",
        "bg": Color.PRIMARY.value,
    },
    transition="color 0.4s ease, background_color 0.4s ease, transform 0.4s ease", 
)

text_presentation_mobile = dict(
    padding_y=EMSize.BIG.value,
    border_bottom=border_bottom_color,
    color= TextColor.TEXT.value
)

navbar_title_style = dict(
    font_family=Font.TITLE.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size=EMSize.LARGE.value
)
