import reflex as rx
import solandweb.styles.styles as styles
from solandweb.views.navbar.navbar import navbar  # Importa el navbar
from solandweb.views.header.header import hero_section
from solandweb.views.about.about import about
from solandweb.views.contador.contador import contador
from solandweb.views.postulation.postulation import postulation
from solandweb.views.jobs_carrusel.job_carrusel import job_carrusel, CarruselState  # Importa el carrusel y su estado

class State(rx.State):
    pass

def index() -> rx.Component:
    """Página de inicio."""
    return rx.fragment(
        navbar(),  # Navbar ocupa todo el ancho
        hero_section(),  # Sección principal
        about(),  # Sección "Acerca de"
        #sidebar(),
        job_carrusel(),  # Carrusel de vacantes disponibles
        contador(),  # Contador de estadísticas
        rx.box(
            rx.link(
                "Ver puestos disponibles",
                href="/postulation",  # Ruta de la página de postulación
                target="_blank",  # Abrir en una nueva pestaña
                style={
                    "display": "block",
                    "margin": "71px auto",  # Centra el enlace
                    "text_align": "center",
                    "font_size": "1.2rem",
                    "color": "#FFD700",
                    "text_decoration": "none",
                    "font_weight": "bold",
                },
            ),
            style={
                "width": "100%",  # Asegura que ocupe todo el ancho
                "text_align": "center",
                "padding": "1rem",
            },
        ),
    )

# Configuración de la aplicación
app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
)


app.add_page(
    index,
    title="Soland | Inicio",
    image="logo.png",
    on_load=CarruselState.on_load, 

)

app.add_page(
    postulation,  # Página de postulación
    route="/postulation",  # Ruta de la página
    title="Puestos Disponibles | Soland",
    image="logo.png",
)

