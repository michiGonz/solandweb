# Estilos globales
import reflex as rx
from enum import Enum
from solandweb.styles.fonts import Font
from solandweb.styles.colors import Color as Color

# Base style
STYLESHEETS = [
    "https://fonts.googleapis.com/css?family=Roboto:wght@300&display=swap"
]

# Constantes
MAX_WIDTH = "1200px"  # Ajustado para pantallas más grandes

# Tamaños
class Size(Enum):
    SMALL = "1"
    MEDIUM = "2"
    DEFAULT = "3"
    LARGE = "4"
    BIG = "5"

# Estilo base
BASE_STYLE = {
    "font_family": Font.DEFAULT.value,  # Fuente general
    "background_color": Color.BACKGROUND.value,  # Color de fondo general
    "scroll_behavior": "smooth",  # Habilita el desplazamiento suave
}

# Estilo global
GLOBAL_STYLE = {
    "margin": "0 !important",
    "padding": "0 !important",
    "width": "100vw !important",
    "box_sizing": "border-box !important",
}

# Navbar
navbar = {
    "display": "flex",
    "justify_content": "space-between",
    "align_items": "center",
    "padding": "1rem",
    "background": "linear-gradient(to right, yellow, black)",
    "color": "white",
    "width": "100%",
}

# Hero section
HERO_STYLE = {
    "height": "100vh",
    "display": "flex",
    "align_items": "center",
    "justify_content": "center",
    "background_image": "url('/header.jpg')",  # Imagen de fondo
    "background_size": "cover",
    "background_position": "center",
    "color": "black",
    "text_align": "center",
}

# About section
about_section = {
    "padding": "4rem",
    "background_color": "#ffeb3b",  # Fondo amarillo
    "text_align": "center",
}

about_title = {
    "font_size": "2rem",
    "font_weight": "bold",
    "margin_bottom": "1rem",
    "text_align": "center",
}

about_subtitle = {
    "font_size": "1.2rem",
    "color": "#666",
    "margin_bottom": "2rem",
    "text_align": "center",
}

about_grid = {
    "display": "grid",
    "grid_template_columns": "repeat(auto-fit, minmax(300px, 1fr))",  # Diseño responsivo
    "gap": "2rem",
}

about_box = {
    "background_color": "white",
    "padding": "20px",
    "border_radius": "10px",
    "box_shadow": "2px 2px 10px rgba(0, 0, 0, 0.1)",
    "text_align": "left",
    "color": "#333",
}

about_image = {
    "width": "100%",  # Asegura que las imágenes ocupen todo el ancho del contenedor
    "border_radius": "8px",
    "margin_bottom": "1rem",
}

# Servicios
SERVICES_STYLE = {
    "padding": "4rem",
    "display": "flex",
    "justify_content": "space-around",
    "background_color": "#f9f9f9",
}

# Contacto
CONTACT_STYLE = {
    "padding": "4rem",
    "background_color": "#f1f1f1",
    "text_align": "center",
}

# Footer
FOOTER_STYLE = {
    "padding": "2rem",
    "background_color": "#333",
    "color": "white",
    "text_align": "center",
}

# Botones
button = {
    "display": "inline-block",
    "background_color": "#007bff",
    "color": "white",
    "padding": "10px 15px",
    "margin_top": "15px",
    "text_decoration": "none",
    "border_radius": "5px",
    "transition": "0.3s",
}

button_hover = {
    "background_color": "#0056b3",
}