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
                "How to Build a Custom Knowledge ChatGPT Clone in 5 Minutes" ,
                "In this video I'll be showing you how to create ChatGPT style custom knowledge chatbots using LlamaIndex/GPTIndex. You can create useful chatbot agents for your business by loading in your own data, eg for customer service chatbots or a range of other uses that LlamaIndex/GPTIndex.",   
                "https://www.youtube.com/embed/ydjRYmM19DY" 
            ),
            card_video(
                "https://i.blogs.es/9b19ad/youtube/450_1000.webp",
                "How to Build a Custom Knowledge ChatGPT Clone in 5 Minutes" ,
                "In this video I'll be showing you how to create ChatGPT style custom knowledge chatbots using LlamaIndex/GPTIndex. You can create useful chatbot agents for your business by loading in your own data, eg for customer service chatbots or a range of other uses that LlamaIndex/GPTIndex.",   
                "https://www.youtube.com/embed/ydjRYmM19DY" 
            ),
            card_video(
                "https://i.blogs.es/9b19ad/youtube/450_1000.webp",
                "How to Build a Custom Knowledge ChatGPT Clone in 5 Minutes" ,
                "In this video I'll be showing you how to create ChatGPT style custom knowledge chatbots using LlamaIndex/GPTIndex. You can create useful chatbot agents for your business by loading in your own data, eg for customer service chatbots or a range of other uses that LlamaIndex/GPTIndex.",   
                "https://www.youtube.com/embed/ydjRYmM19DY" 
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