
import reflex as rx
import solandweb.styles.styles as styles
from solandweb.styles.styles import Size as Size
from solandweb.views.header.header import navbar
from solandweb.views.header.header import hero_section
from solandweb.views.about.about import about
from solandweb.views.header.header import services_section
from solandweb.views.header.header import contact_section
from solandweb.views.header.header import footer
from solandweb.views.header.header import map_section


    
class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.container(
        navbar(),
        hero_section(),
        about(),
        width="100%",
        style=styles.GLOBAL_STYLE,
    )

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
)

app.add_page(
    index,
    title="Soland | WEB",
    image="logo.png"
)