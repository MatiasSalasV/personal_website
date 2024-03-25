import reflex as rx
from personal_website.styles.styles import Size
from personal_website.styles.fonts import Font

def heading(text: str, h1=False) -> rx.Component:
    return rx.heading(
        text,
        as_="h1" if h1 else "h2",
        size=Size.BIG.value if h1 else Size.LARGE.value,
        font_family=Font.DEFAULT.value,
        
    )