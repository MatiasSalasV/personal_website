import reflex as rx
import personal_website.styles.styles as styles

def copy_right() -> rx.Component:
    return rx.center(
        rx.text(
            "© 2024 Matías Salas Vergara. Todos los derechos reservados.",
            align="center"
        ),
        padding_bottom=styles.EMSize.DEFAULT.value,
        width="100%",
    )