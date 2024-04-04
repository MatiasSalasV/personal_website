import reflex as rx
import personal_website.styles.styles as styles
from personal_website.styles.colors import Color, TextColor
from personal_website.components.heading import heading
from personal_website.components.card_video import card_video


def youtube() -> rx.Component:
    return rx.vstack(
        rx.text(
            "CREACIÓN DE CONTENIDO",
            color=Color.PRIMARY.value,
            trim="both"
        ),
        heading("YouTube"),

        rx.chakra.responsive_grid(
            card_video(
                "https://i.blogs.es/9b19ad/youtube/450_1000.webp",
                "Titulo de muestra para previsualizar sección" ,
                "Este seria un texto correspondiente a la descripción del video que se visualizaria en la card para que el usuario tenga un breve contexto de lo que se trata el video que seleccionó para ver en la pagina web para que redirija al contenido de youtube",   
                "https://www.youtube.com/embed/xcJtL7QggTI" 
            ),
            card_video(
                "https://i.blogs.es/9b19ad/youtube/450_1000.webp",
                "Titulo de muestra para previsualizar secció" ,
                "Este seria un texto correspondiente a la descripción del video que se visualizaria en la card para que el usuario tenga un breve contexto de lo que se trata el video que seleccionó para ver en la pagina web para que redirija al contenido de youtube",   
                "https://www.youtube.com/embed/xcJtL7QggTI" 
            ),
            card_video(
                "https://i.blogs.es/9b19ad/youtube/450_1000.webp",
                "Titulo de muestra para previsualizar secció" ,
                "Este seria un texto correspondiente a la descripción del video que se visualizaria en la card para que el usuario tenga un breve contexto de lo que se trata el video que seleccionó para ver en la pagina web para que redirija al contenido de youtube",   
                "https://www.youtube.com/embed/xcJtL7QggTI" 
            ),
            spacing="5",
            padding_top=styles.EMSize.LARGE.value,
            columns=[1,1,2, 3],
        ),

        
        
        align="center",
        width="100%",
        border_bottom = styles.border_bottom_color,
        padding_y = styles.EMSize.BIGGER.value,
        id="youtube"
    )