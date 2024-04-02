import reflex as rx
import personal_website.styles.styles as styles
import personal_website.constants as const
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
            card_feature(
                "bot",
                "Desarrollo de Bots", 
                # Transforma la interacción con tus clientes con bots inteligentes. 
                # Desarrollo soluciones de chatbot personalizadas, integrando inteligencia artificial específica para tu negocio. 
                # Mejora la experiencia de usuario, aumenta la eficiencia y haz que tu servicio al cliente esté disponible 24/7.
                "Creo chatbots personalizados que integran inteligencia artificial y funciones específicas para tu negocio.",
                "#agenda",
                False
            ),
            card_feature(
                "cpu",
                "Desarrollo Web", 
                # Tu presencia online, rediseñada. Creo landing pages que no solo capturan la esencia de tu marca, sino que están optimizadas para convertir. 
                # Cada página es una obra de arte digital, diseñada desde cero para reflejar tu identidad única y conectar con tu audiencia.
                "Diseño y desarrollo páginas web a medida para establecer tu presencia en internet y potenciar tu marca.",
                "#agenda",
                False
            ),
            card_feature(
                "film",
                "Creación de Contenido", 
                # Comparto mis conocimientos con otros emprendedores a través de mi canal de YouTube. Descubre cómo implementar soluciones 
                # tecnológicas de forma sencilla para beneficiar tu vida y tu negocio, desde automatizaciones hasta las últimas tendencias en tecnología.
                "Comparto mis conocimientos con otros emprendedores a través de mi canal de YouTube.",
                const.YOUTUBE_URL,
                True
            ),
            spacing="5",
            padding_top=styles.EMSize.LARGE.value,
            columns=[1,1,2, 3],
        ),
        
        align="center",
        width="100%",
        border_bottom = styles.border_bottom_color,
        padding_y = styles.EMSize.BIGGER.value,
        id="features"
    )