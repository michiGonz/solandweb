import reflex as rx
import solandweb.styles.styles as styles
from solandweb.styles.styles import Size as Size

def navbar():
    return rx.box(
        rx.hstack(
            # Logo de la empresa
            rx.image(
                src="logo.jpeg",  # Ruta del logo
                alt="Logo",
                style={
                    "width": "120px",
                    "height": "auto",
                    "margin_right": "2rem",
                },
            ),
            # Menú principal
            rx.hstack(
                rx.text("Inicio", style={"cursor": "pointer", "font_weight": "bold", "color": "black", "margin_right": "1.5rem"}),
                rx.text("Servicios", style={"cursor": "pointer", "font_weight": "bold", "color": "black", "margin_right": "1.5rem"}),
                rx.text("Portafolio", style={"cursor": "pointer", "font_weight": "bold", "color": "black", "margin_right": "1.5rem"}),
                rx.text("Blog", style={"cursor": "pointer", "font_weight": "bold", "color": "black", "margin_right": "1.5rem"}),
                rx.text("Contacto", style={"cursor": "pointer", "font_weight": "bold", "color": "black"}),
                spacing="1",
            ),
            # Botón de acción
            rx.button(
                "Contáctanos",
                style={
                    "background_color": "black",
                    "color": "white",
                    "padding": "0.5rem 1rem",
                    "border_radius": "5px",
                    "cursor": "pointer",
                    "font_weight": "bold",
                },
                on_click=lambda: rx.redirect("/contact"),
            ),
            justify="between",  # Espaciado entre los elementos
            align_items="center",
            width="100%",
            style={
                "padding": "1rem 2rem",
                "background_color": "#FFD700",  # Fondo amarillo
                "box_shadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",  # Sombra para un efecto sofisticado
                "position": "fixed",  # Navbar fijo en la parte superior
                "top": "0",
                "z_index": "1000",  # Asegura que esté encima de otros elementos
            },
        ),
        style={"width": "100%"},
    )