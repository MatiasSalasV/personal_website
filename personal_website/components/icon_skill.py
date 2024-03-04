import reflex as rx
import personal_website.styles.styles as styles
from personal_website.styles.colors import Color, TextColor

#ESTE PODRIA SER UN BADGE
def icon_skill(image:str, alt:str) -> rx.Component:
    return rx.button(
            # rx.icon(tag=icon),
            rx.image(
                src=image,
                width=styles.EMSize.BIG.value,
                height=styles.EMSize.BIG.value,
                alt=alt
            ),
            box_shadow=" 5px 5px 15px #D1D9E6, -5px -5px 15px #ffffff",
            bg="linear-gradient(145deg, #e2e8ec, #ffffff)",
            color= TextColor.TEXT.value,
            _hover= {
                "cursor": "default",
            },
            width="56px",
            height="56px",
            margin_right=styles.EMSize.SMALL.value,
        )

