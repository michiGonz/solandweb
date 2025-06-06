import reflex as rx
import solandweb.styles.styles as styles
from solandweb.styles.styles import Size as Size

import reflex as rx
import solandweb.styles.styles as styles
from solandweb.styles.styles import Size as Size
from solandweb.views.navbar.navbar import navbar  # Importa el navbar

def hero_section() -> rx.Component:
    """Hero section."""
    return rx.box(
        navbar(),  # Incluye el navbar en la parte superior
        rx.box(
            rx.vstack(
                rx.center(
                    rx.text(
                        "Servicios y Suministros Soland C.A",
                        class_name="title",
                        style={
                            "font_weight": "1000",
                            "font_size": "5rem",
                            "color": "black",
                            "text_align": "center",
                            "letter_spacing": "0.1em",
                            "padding": "0.5rem",
                            "display": "inline-block",
                            "text_shadow": (
                                "0 0 32px #fff,"
                                "0 0 64px #fff,"
                                "0 0 128px #fff,"
                                "0 0 256px #fff,"
                                "0 0 8px #ffe066,"
                                "0 0 16px #ffe066"
                            ),
                            "animation": "glow 2s ease-in-out infinite alternate",
                        },
                    ),
                    rx.html(
                        """
                        <style>
                        @keyframes glow {
                            0% {
                                text-shadow:
                                    0 0 32px #fff,
                                    0 0 64px #fff,
                                    0 0 128px #fff,
                                    0 0 256px #fff,
                                    0 0 8px #ffe066,
                                    0 0 16px #ffe066;
                            }
                            100% {
                                text-shadow:
                                    0 0 64px #fff,
                                    0 0 128px #fff,
                                    0 0 256px #fff,
                                    0 0 512px #fff,
                                    0 0 32px #ffe066,
                                    0 0 64px #ffe066;
                            }
                        }
                        </style>
                        """
                    ),
                ),
                # ...existing code...
                rx.text(
                    "Somos una empresa venezolana con más de 21 años de experiencia en el área de ingeniería.",
                    size="4",
                    style={
                        "font_weight": "900",
                        "background_color": "rgba(255,255,255,0.75)", 
                        "padding": "1.1rem 2rem",
                        "border_radius": "18px",
                        "color": "#222",
                        "text_align": "center",
                        "margin": "1.5rem 0 2rem 0",
                        "display": "inline-block",
                        "box_shadow": "0 4px 32px 0 #ffe066, 0 2px 8px rgba(0,0,0,0.08)",
                        "font_size": "1.45rem",
                        "letter_spacing": "0.03em",
                        "transition": "box-shadow 0.3s",
                    },
                ),
                rx.button(
                    "Contáctanos",
                    href="#contacto",
                    style={
                        "background": "linear-gradient(90deg, #ffe066 60%, #fffbe6 100%)",
                        "color": "#222",
                        "font_weight": "bold",
                        "padding": "1rem 2.2rem",
                        "border_radius": "12px",
                        "border": "none",
                        "box_shadow": "0 0 24px 4px #ffe066, 0 2px 8px rgba(0,0,0,0.10)",
                        "font_size": "1.25rem",
                        "cursor": "pointer",
                        "margin_top": "0.7rem",
                        "letter_spacing": "0.04em",
                        "transition": "background 0.3s, box-shadow 0.3s, transform 0.2s",
                    },
                    _hover={
                        "background": "linear-gradient(90deg, #fffbe6 0%, #ffe066 100%)",
                        "box_shadow": "0 0 48px 8px #ffe066, 0 4px 16px rgba(0,0,0,0.13)",
                        "transform": "scale(1.04)",
                    },
                ),
# ...existing code...
                spacing="2",
                align_items="center",
            ),
            style={
                **styles.HERO_STYLE,
                "margin": "0",  # Elimina márgenes externos
                "padding": "0",  # Elimina relleno interno
                "width": "100%",  # Asegura que ocupe todo el ancho
                "margin_top": "60px",  # Ajusta el header para que quede debajo del navbar (asumiendo que el navbar tiene 60px de altura)
            },
            id="inicio",  # Añadir ID para el enlace de navegación
        ),
    )

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


