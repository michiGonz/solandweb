# Estilos globales
import reflex as rx
from enum import Enum
from solandweb.styles.fonts import Font
from solandweb.styles.colors import Color as Color

# Base style
STYLESHEETS = []

#constants
MAX_WIDTH="600px"

#sizes
class Size(Enum):
    SMALL = "1"
    MEDIUM = "2"
    DEFAULT = "3"
    LARGE = "4"
    BIG = "5"

STYLESHEETS =[
    "https://fontsgoogleapiscom/css?family=Roboto:wght@300&display=swap"
]

BASE_STYLE =  {
    "font_family": Font.DEFAULT.value, #fuente general
    "background_color": Color.BACKGROUND.value, #color de fondo general
    "scroll_behavior": "smooth",  # Habilita el desplazamiento suave
}

GLOBAL_STYLE =  {
    "margin": "0",  # Eliminar margen externo
    "padding": "0",  # Eliminar relleno externo
}

# Estilos generales

navbar = {
    "display": "flex",
    "justify_content": "space_between",
    "align_items": "center",
    "padding": "1rem",
    "background": "linear_gradient(to right, yellow, black)",
    "color": "white",
    "width": "100%",
}

logo = {
    "font_size": "18em",
    "font_weight": "bold",
    "color": "yellow",
}

contact_info = {
    "display": "flex",
    "gap": "15px",
    "font_size": "09em",
    "color": "#aaa",
}

menu = {
    "display": "flex",
    "gap": "20px",
}

menu_item = {
    "font_size": "1em",
    "cursor": "pointer",
    "transition": "0.3s",
}

social_media = {
    "display": "flex",
    "gap": "10px",
}
social_icon = {
    "font_size": "12em",
    "cursor": "pointer",
}
language_selector = {
    "font_size": "1em",
    "background_color": "#444",
    "padding": "5px 10px",
    "border_radius": "5px",
}
search_icon = {
    "font_size": "15em",
    "cursor": "pointer",
}


HERO_STYLE =  {
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

SERVICES_STYLE =  {
    "padding": "4rem",
    "display": "flex",
    "justify_content": "space_around",
    "background_color": "#f9f9f9",
}

CONTACT_STYLE =  {
    "padding": "4rem",
    "background_color": "#f1f1f1",
    "text_align": "center",
}

FOOTER_STYLE =  {
    "padding": "2rem",
    "background_color": "#333",
    "color": "white",
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
    "grid_template_columns": "repeat(2, 1fr)",
    "gap": "2rem",
}

about_section = {
    "padding": "2rem",
    "background_color": "#ffeb3b",  # Fondo amarillo
}

about_image = {
    "width": "20%",  # Reduce el tamaño de las imágenes
    "border_radius": "8px",
    "margin_bottom": "1rem",
}

about_box = {
    "text_align": "center",
    "padding": "1rem",
    "border": "1px solid #ddd",
    "border_radius": "8px",
    "box_shadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
    "background_color": "#fff",  # Fondo blanco para las cajas
}

about_box_title = {
    "font_size": "1.5rem",
    "font_weight": "bold",
    "margin_bottom": "0.5rem",
}

about_box_text = {
    "font_size": "1rem",
    "color": "#666",
    "margin_bottom": "1rem",
}

about_button = {
    "background_color": "#ffc107",
    "color": "#fff",
    "padding": "0.5rem 1rem",
    "border": "none",
    "border_radius": "4px",
    "cursor": "pointer",
    "transition": "background-color 0.3s",
}

about_button_hover = {
    "background_color": "#e0a800",
}

sobre_mi =  {
    "padding": "4rem",
    "background_image":" url('/imagen2jpg')",
    "background_size":"cover",
    "background_position": "center",
    "background_repeat": "no_repeat",
    "color": "white",
    "display": "flex",
    "flex_direction": "column",
    "align_items": "center",
    "text_align": "center",
}


sobre_mih1 =  {
    "font_size": "25em",
    "font_weight": "bold",
    "color": "#fff",
    "margin_bottom": "10px",
}


subtitle =  {
    "font_size":"12em",
    "color": "#ddd",
    "margin_bottom": "30px",
}


about_container =  {
    "display": "flex",
    "justify_content": "space_between",
    "gap": "20px",
    "width": "80%",
}


about_box =  {
    "background_color": "white",
    "padding": "20px",
    "width": "30%",
    "border_radius": "10px",
    "box_shadow": "2px 2px 10px rgba(0, 0, 0, 01)",
    "text_align": "left",
    "color": "#333",
}


about_box =  {
    "font_size": "15em",
    "font_weight": "bold",
    "color": "#222",
    "margin_bottom": "10px",
}


about_boxp =  {
    "font_size": "1em",
    "color": "#666",
}


button =  {
    "display": "inline_block",
    "background_color": "#007bff",
    "color": "white",
    "padding": "10px 15px",
    "margin_top": "15px",
    "text_decoration": "none",
    "border_radius": "5px",
    "transition": "03s",
}

menu = {
    "display": "flex",
    "gap": "20px",
    "justify_content": "center",
}

menu_item = {
    "font_size": "1em",
    "cursor": "pointer",
    "transition": "0.3s",
}

navbar_top = {
    "display": "flex",
    "justify_content": "space-between",
    "align_items": "center",
    "padding": "1rem",
}

navbar = {
    "width": "100%",
    "background_color": "#fff",
}

contact_info = {
    "display": "flex",
    "justify_content": "space-between",
    "align_items": "center",
    "background_color": "#f8f8f8",
    "padding": "0.5rem 1rem",
    "font_size": "0.9em",
    "color": "#555",
    "width": "100%",  # Ocupa todo el ancho de la página
    "margin": "0",  # Elimina el margen exterior
}

contact_item = {
    "margin_right": "1rem",  # Espaciado entre los elementos
    "display": "flex",
    "align_items": "center",
}





