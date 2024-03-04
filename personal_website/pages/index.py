import reflex as rx
import personal_website.styles.styles as styles
from personal_website.components.navbar import navbar
from personal_website.views.header import header
from personal_website.views.features import features
from personal_website.views.resumen import resumen
from personal_website.views.youtube import youtube
from personal_website.views.agenda import agenda
from personal_website.views.footer import footer
from personal_website.components.copy_right import copy_right
import personal_website.utils as utils
# from personal_website.styles.colors import Color



@rx.page(
    # route="/",
    title=utils.index_title,
    description=utils.index_description,
    # image=utils.preview,
    meta=utils.index_meta,
)
def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                features(),
                youtube(),
                # resumen(),
                agenda(),
                footer(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                # margin_y=styles.Size.BIG.value,
                padding=styles.EMSize.DEFAULT.value
            ),  
        ),
        copy_right(),

        # bg=Color.BACKGROUND.value
    )

