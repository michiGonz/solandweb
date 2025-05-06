import reflex as rx
from rxconfig import config
import solandweb.styles.styles as styles
from solandweb.styles.styles import Size as Size

class State(rx.State):
    """The app state."""
    search_query: str = ""  # Estado para almacenar el término de búsqueda

    @rx.var
    def filtered_results(self) -> str:  # Agregada la anotación de tipo
        # Aquí puedes implementar la lógica para filtrar resultados según el término de búsqueda
        return f"Resultados para: {self.search_query}" if self.search_query else "Sin resultados"

    def set_search_query(self, query: str):
        """Actualiza el término de búsqueda."""
        self.search_query = query

    def handle_search(self):
        """Maneja el evento de búsqueda."""
        print(f"Buscando: {self.search_query}")  # Puedes reemplazar esto con lógica adicional


def navbar():
    return rx.vstack(  # Apila los elementos verticalmente
      rx.hstack(
            rx.text("📞 1-800-405-377", class_name="contact_item"),
            rx.text("✉ info@company.com", class_name="contact_item"),
            rx.text("📍 Collins Street 8007, USA", class_name="contact_item"),
            rx.text("📅 Mon - Sat: 8.00 - 19:00", class_name="contact_item"),
            justify="between",  # Distribuye los elementos con espacio entre ellos
            width="100%",  # Ocupa todo el ancho del contenedor
            style={
                "background_color": "#f8f8f8",  # Fondo gris claro
                "padding": "0.5rem 1rem",  # Espaciado interno
                "font_size": "0.9em",  # Tamaño de fuente más pequeño
                "color": "#555",  # Color de texto gris oscuro
                "width": "100%",  # Ocupa todo el ancho de la página
            },
            class_name="contact_info",
        ),
        rx.hstack(  # Contenedor para el menú y la barra de búsqueda
            rx.text("Home", class_name="menu_item"),
            rx.text("Pages", class_name="menu_item"),
            rx.text("Portfolio", class_name="menu_item"),
            rx.text("Blog", class_name="menu_item"),
            rx.text("Elements", class_name="menu_item"),
            rx.hstack(  # Contenedor para la barra de búsqueda
                rx.input(
                    placeholder="Buscar...",
                    on_change=State.set_search_query,  # Actualiza el estado al escribir
                    class_name="search_input",
                ),
                rx.button(
                    "🔍",
                    on_click=State.handle_search,  # Llama a la función de búsqueda
                    class_name="search_button",
                ),
                spacing="1",
            ),
            justify="between",  # Distribuye los elementos a lo largo del ancho
            width="100%",  # Ocupa todo el ancho de la página
            style={"background_color": "#f0f0f0", "padding": "1rem"},  # Contenedor gris
        ),
        class_name="navbar",
    )
    
def hero_section() -> rx.Component:
    """Hero section."""
    return rx.box(
        rx.vstack(
            rx.heading("Bienvenido a Soland CA", size="6"),
            rx.text("Tu solución moderna para páginas web profesionales.", size="4"),
            rx.button("Contáctanos", href="#contacto", color_scheme="teal"),
            spacing="2",
            align_items="center",
        ),
        style=styles.HERO_STYLE,
        id="inicio",  # Añadir ID para el enlace de navegación
    ),


def about_section() -> rx.Component:
    """About section."""
    return rx.box(
        rx.text("What we have to offer for your next business and career success", class_name="about-title"),
        rx.text(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis aute irure dolor in reprehenderit.",
            class_name="about-subtitle",
        ),
        rx.grid(
            # Primera fila
            rx.box(
                rx.image(src="/imagen1.jpg", class_name="about-image"),
                rx.text("Green building", class_name="about-box-title"),
                rx.text(
                    "Interdum iusto pulvinar consequuntur augue optio, repellat fuga! Purus expedita fusce temporibus eso.",
                    class_name="about_box_text",
                ),
                rx.button("Take a look", class_name="about-button"),
                class_name="about-box",
            ),
            rx.box(
                rx.image(src="/imagen1.jpg", class_name="about-image"),
                rx.text("Interior design", class_name="about-box-title"),
                rx.text(
                    "Interdum iusto pulvinar consequuntur augue optio, repellat fuga! Purus expedita fusce temporibus eso.",
                    class_name="about-box-text",
                ),
                rx.button("Take a look", class_name="about-button"),
                class_name="about-box",
            ),
            # Segunda fila
            rx.box(
                rx.image(src="/imagen1.jpg", class_name="about-image"),
                rx.text("Expert team", class_name="about-box-title"),
                rx.text(
                    "Interdum iusto pulvinar consequuntur augue optio, repellat fuga! Purus expedita fusce temporibus eso.",
                    class_name="about-box-text",
                ),
                rx.button("Take a look", class_name="about-button"),
                class_name="about-box",
            ),
            rx.box(
                rx.image(src="/imagen1.jpg", class_name="about-image"),
                rx.text("Family plans", class_name="about-box-title"),
                rx.text(
                    "Interdum iusto pulvinar consequuntur augue optio, repellat fuga! Purus expedita fusce temporibus eso.",
                    class_name="about-box-text",
                ),
                rx.button("Take a look", class_name="about-button"),
                class_name="about-box",
            ),
            template_columns="repeat(2, 1fr)",  # Dos columnas
            gap="2rem",  # Espaciado entre elementos
            class_name="about-grid",
        ),
        id="about",
        class_name="about-section",
    )
    
    
def services_section() -> rx.Component:
    """Services section."""
    return rx.box(
        rx.vstack(
            rx.heading("Nuestros Servicios", size="4"),
            rx.hstack(
                rx.box(
                    rx.icon("laptop", size=3),
                    rx.text("Desarrollo Web"),
                    rx.text("Diseñamos y desarrollamos sitios web personalizados."),
                    align_items="center",
                    text_align="center",
                ),
                rx.box(
                    rx.icon("phone", size=3),
                    rx.text("Diseño Responsivo"),
                    rx.text("Tu sitio web se verá genial en cualquier dispositivo."),
                    align_items="center",
                    text_align="center",
                ),
                rx.box(
                    rx.icon("search", size=3),
                    rx.text("SEO"),
                    rx.text("Optimización para motores de búsqueda."),
                    align_items="center",
                    text_align="center",
                ),
                spacing="2",
            ),
            spacing="2",
        ),
        style=styles.SERVICES_STYLE,
    )

def contact_section() -> rx.Component:
    """Contact section."""
    return rx.box(
        rx.vstack(
            rx.heading("Contáctanos", size="4"),
            rx.form(
                rx.input(placeholder="Tu nombre", name="nombre", required=True),
                rx.input(placeholder="Tu correo", type="email", name="email", required=True),
                rx.text_area(placeholder="Tu mensaje", name="mensaje", required=True),
                rx.button("Enviar", type="submit", color_scheme="teal"),
                spacing="1",
            ),
            spacing="2",
        ),
        style=styles.CONTACT_STYLE,
    )

def map_section() -> rx.Component:
    """Map section."""
    return rx.box(
        rx.html(
            '<iframe src="https://www.google.com/maps/embed?..." width="100%" height="400" style="border:0;" allowfullscreen="" loading="lazy"></iframe>'
        ),
        style={"margin": "2rem 0"},
    )
    
def footer() -> rx.Component:
    """Footer section."""
    return rx.box(
        rx.text("© 2025 MiWeb. Todos los derechos reservados.", text_align="center"),
        style=styles.FOOTER_STYLE,  # Aplicar estilos desde styles.py
    )


def index() -> rx.Component:
    """Main page."""
    return rx.container(
        navbar(),
        hero_section(),
        about_section(),
        services_section(),
        contact_section(),
        footer(),
        style=styles.GLOBAL_STYLE,  
    )


app = rx.App()
app.add_page(index)