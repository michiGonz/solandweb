import reflex as rx
import solandweb.styles.styles as styles
from solandweb.styles.styles import Size as Size
from solandweb.views.navbar.navbar import navbar
from solandweb.views.header.header import hero_section
from solandweb.views.about.about import about
from solandweb.views.sidebar.sidebar import sidebar
from solandweb.views.contador.contador import contador
from solandweb.views.postulation.postulation import job_postings  # Importa la página de postulación

class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.container(
        sidebar(),
        hero_section(),
        about(),
        contador(),
        rx.link(
            "Ver puestos disponibles",
            href="/postulation",  # Ruta de la página de postulación
            target="_blank",  # Abrir en una nueva pestaña
            style={
                "display": "block",
                "margin": "2rem auto",
                "text_align": "center",
                "font_size": "1.2rem",
                "color": "#FFD700",
                "text_decoration": "none",
                "font_weight": "bold",
            },
        ),
        width="100%",
        style=styles.GLOBAL_STYLE, 
    )

# Agrega la página de postulación
app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
)

app.add_page(
    index,
    title="Soland | WEB",
    image="logo.png"
)

app.add_page(
    job_postings,  # Página de postulación
    route="/postulation",  # Ruta de la página
    title="Puestos Disponibles | Soland",
    image="logo.png",
)