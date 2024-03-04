import reflex as rx
import personal_website.styles.styles as styles
import personal_website.utils as utils
from personal_website.components.navbar import navbar
from personal_website.pages import index


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    head_components=[
#         rx.script(
#             src=f"https://www.googletagmanager.com/gtag/js?id={const.G_TAG}"),
#         rx.script(
#             f"""
# window.dataLayer = window.dataLayer || [];
# function gtag(){{dataLayer.push(arguments);}}
# gtag('js', new Date());
# gtag('config', '{const.G_TAG}');
# """
#         ),
    ],
)

