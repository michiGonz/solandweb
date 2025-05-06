import reflex as rx
from solandweb.views.navbar.navbar import navbar

def job_postings():
    """Sección de puestos disponibles."""
    # Lista de puestos disponibles
    jobs = [
        {"title": "Desarrollador Web", "description": "Responsable del desarrollo y mantenimiento de sitios web."},
        {"title": "Diseñador Gráfico", "description": "Encargado de crear diseños visuales atractivos para proyectos digitales."},
        {"title": "Gerente de Marketing", "description": "Planificación y ejecución de estrategias de marketing."},
        {"title": "Analista de Datos", "description": "Análisis de datos para la toma de decisiones estratégicas."},
    ]

    return rx.fragment(  # Usa fragment para combinar múltiples elementos
        navbar(),  # Navbar fuera del box principal
        rx.box(
            rx.box(
                rx.text(
                    "Bienvenido a la sección de postulación",
                    style={
                        "font_size": "2.5rem",
                        "font_weight": "bold",
                        "margin_bottom": "1rem",
                        "color": "#333",
                        "text_align": "center",
                    },
                ),
                rx.text(
                    "Aquí puedes postularte para los puestos disponibles en nuestra empresa. Selecciona el puesto que te interesa y sube tu CV.",
                    style={
                        "font_size": "1.2rem",
                        "color": "#666",
                        "text_align": "center",
                        "margin_bottom": "2rem",
                    },
                ),
                rx.hstack(
                    rx.text(
                        "¿Tienes alguna pregunta?",
                        style={
                            "font_size": "1.2rem",
                            "color": "#333",
                            "text_align": "center",
                            "margin_bottom": "1rem",
                        },
                    ),
                    rx.button(
                        "Contáctanos",
                        style={
                            "background_color": "#FFD700",
                            "color": "black",
                            "padding": "0.5rem 1rem",
                            "border": "none",
                            "border_radius": "5px",
                            "cursor": "pointer",
                            "font_weight": "bold",
                        },
                        on_click=lambda: rx.redirect("/contact"),  # Redirige a la sección de contacto
                    ),
                    spacing="1",
                    style={
                        "justify_content": "center",
                        "align_items": "center",
                        "margin_top": "1rem",
                        "margin_bottom": "2rem",
                    },
                ),
                style={
                    "background_color": "#f9f9f9",
                    "padding": "2rem",
                    "border_radius": "10px",
                    "box_shadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",
                    "width": "100%",
                    "display": "flex",
                    "flex_direction": "column",
                    "align_items": "center",
                    "justify_content": "center",
                },
            ),
            rx.text(
                "Puestos Disponibles",
                style={
                    "font_size": "2.5rem",
                    "font_weight": "bold",
                    "margin_bottom": "1rem",
                    "color": "#333",
                    "text_align": "center",
                },
            ),
            rx.vstack(
                *[
                    rx.box(
                        rx.text(job["title"], style={"font_size": "1.5rem", "font_weight": "bold", "color": "#333"}),
                        rx.text(job["description"], style={"font_size": "1rem", "color": "#666", "margin_bottom": "1rem"}),
                        rx.hstack(
                            rx.input(
                                type="file",
                                accept=".pdf,.doc,.docx",
                                style={
                                    "padding": "0.1rem",
                                    "border": "1px solid #ddd",
                                    "border_radius": "5px",
                                    "width": "70%",
                                },
                            ),
                            rx.button(
                                "Subir CV",
                                style={
                                    "background_color": "#FFD700",
                                    "color": "black",
                                    "padding": "0.5rem 1rem",
                                    "border": "none",
                                    "border_radius": "5px",
                                    "cursor": "pointer",
                                    "font_weight": "bold",
                                },
                            ),
                            spacing="1",
                        ),
                        style={
                            "padding": "1rem",
                            "border": "1px solid #ddd",
                            "border_radius": "8px",
                            "box_shadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",
                            "margin_bottom": "1rem",
                            "background_color": "#f9f9f9",
                            "width": "100%",
                            "min_height": "200px",
                            "display": "flex",
                            "flex_direction": "column",
                            "justify_content": "space-between",
                        },
                    )
                    for job in jobs
                ],
                spacing="1",
            ),
            style={
                "padding": "2rem",
                "max_width": "800px",
                "margin": "0 auto",
                "background_color": "#fff",
                "border_radius": "10px",
                "box_shadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",
            },
        ),
    )