import reflex as rx
import solandweb.styles.styles as styles
from solandweb.views.navbar.navbar import navbar  # Importa el navbar
from solandweb.views.header.header import hero_section
from solandweb.views.about.about import about
from solandweb.views.contador.contador import contador
from solandweb.views.postulation.postulation import postulation
from solandweb.views.jobs_carrusel.job_carrusel import job_carrusel, CarruselState  # Importa el carrusel y su estado
from solandweb.views.footer.footer import footer
from solandweb.views.services.servicios import servicios_section  # Importa la sección de servicios
from solandweb.views.ws.ws import whatsapp_button  # Importa el botón de WhatsApp


class State(rx.State):
    pass

def index() -> rx.Component:
    """Página de inicio."""
    return rx.fragment(
        navbar(),  # Navbar ocupa todo el ancho
        hero_section(),  # Sección principal
        about(),  # Sección "Acerca de"
        servicios_section(),
        whatsapp_button(),  # Botón de WhatsApp
        #sidebar(),
        footer()
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

