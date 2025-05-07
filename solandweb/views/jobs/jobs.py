import reflex as rx

def jobs():
    """Sección de especificaciones de los puestos de trabajo."""
    job_list = [
        {
            "title": "Desarrollador Web",
            "description": "Responsable del desarrollo y mantenimiento de sitios web modernos y escalables.",
            "requirements": [
                "Experiencia en HTML, CSS, JavaScript y frameworks como React o Angular.",
                "Conocimiento en bases de datos relacionales y no relacionales.",
                "Capacidad para trabajar en equipo y cumplir plazos.",
            ],
        },
        {
            "title": "Diseñador Gráfico",
            "description": "Encargado de crear diseños visuales atractivos para proyectos digitales y físicos.",
            "requirements": [
                "Dominio de herramientas como Photoshop, Illustrator y Figma.",
                "Creatividad y atención al detalle.",
                "Experiencia en diseño de interfaces de usuario (UI).",
            ],
        },
        {
            "title": "Gerente de Marketing",
            "description": "Planificación y ejecución de estrategias de marketing para aumentar la visibilidad de la empresa.",
            "requirements": [
                "Experiencia en marketing digital y redes sociales.",
                "Habilidades de comunicación y liderazgo.",
                "Capacidad para analizar métricas y optimizar campañas.",
            ],
        },
    ]

    return rx.box(
        rx.text(
            "Puestos de Trabajo Disponibles",
            style={
                "font_size": "2.5rem",
                "font_weight": "bold",
                "margin_bottom": "2rem",
                "text_align": "center",
                "color": "#333",
            },
        ),
        rx.vstack(
            *[
                rx.box(
                    rx.text(
                        job["title"],
                        style={
                            "font_size": "1.8rem",
                            "font_weight": "bold",
                            "margin_bottom": "0.5rem",
                            "color": "#333",
                        },
                    ),
                    rx.text(
                        job["description"],
                        style={
                            "font_size": "1rem",
                            "margin_bottom": "1rem",
                            "color": "#666",
                        },
                    ),
                    rx.text(
                        "Requisitos:",
                        style={
                            "font_size": "1.2rem",
                            "font_weight": "bold",
                            "margin_bottom": "0.5rem",
                            "color": "#333",
                        },
                    ),
                    rx.ul(
                        *[rx.li(req, style={"color": "#666", "margin_bottom": "0.5rem"}) for req in job["requirements"]],
                        style={"margin_bottom": "1rem"},
                    ),
                    rx.button(
                        "Postularse",
                        href="/postulation",
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
                    style={
                        "padding": "1.5rem",
                        "border": "1px solid #ddd",
                        "border_radius": "10px",
                        "box_shadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",
                        "margin_bottom": "2rem",
                        "background_color": "#fff",
                    },
                )
                for job in job_list
            ],
            style={"width": "100%", "max_width": "800px", "margin": "0 auto"},
        ),
        style={
            "padding": "2rem",
            "background_color": "#f9f9f9",
            "border_radius": "10px",
            "box_shadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",
            "width": "100%",
        },
    )