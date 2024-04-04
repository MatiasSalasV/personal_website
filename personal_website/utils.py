import reflex as rx

# Común

def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")



_meta = [
    {"name": "og:type", "content": "website"},
    {"name": "twitter:card", "content": "summary_large_image"},
    {"name": "twitter:site", "content": "@MatiasSalasV"}
]

# Index

index_title = "Matias Salas Vergara | Desarrollo Web, Automatización con IA"
index_description = "Hola, soy Matias Salas Vergara. Digitalizo y automatizo tu negocio con IA, brindándote la ventaja de liderar tu sector. En esta era tecnológica, considero que quien se adapta, gana. Además, comparto mis conocimientos con otros emprendedores a través de YouTube."

index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
]
index_meta.extend(_meta)

# # Cursos

# courses_title = "MoureDev | Cursos gratis de programación"
# courses_description = "Este es un listado con algunos cursos gratis para aprender programación y desarrollo de software. Python, SQL, Git..."

# courses_meta = [
#     {"name": "og:title", "content": courses_title},
#     {"name": "og:description", "content": courses_description},
# ]
# courses_meta.extend(_meta)