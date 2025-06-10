import reflex as rx
import solandweb.theme as theme


SERVICIOS = [
    {
        "titulo": "Ingeniería y Proyectos",
        "desc": "Desarrollamos soluciones innovadoras y eficientes para tu empresa.",
        "img": "/1.jpg",
    },
    {
        "titulo": "Suministro de Equipos",
        "desc": "Proveemos equipos industriales de alta calidad y tecnología de punta.",
        "img": "/2.webp",
    },
    {
        "titulo": "Automatización Industrial",
        "desc": "Optimizamos procesos con sistemas inteligentes y automatizados.",
        "img": "/3.jpg",
    },
    {
        "titulo": "Mantenimiento Preventivo",
        "desc": "Cuidamos tus activos para que tu negocio nunca se detenga.",
        "img": "/4.jpg",
    },
    {
        "titulo": "Optimizacion de procesos",
        "desc": "Mejoramos la eficiencia y productividad de tus operaciones.",
        "img": "/5.webp",
    },
    {
        "titulo": "Ingenieria",
        "desc": "Soluciones de ingeniería adaptadas a tus necesidades.",
        "img": "/6.jpg",
    },
]


def servicios_section() -> rx.Component:
    return rx.box(
        rx.heading(
            "Nuestros Servicios",
            size="7",  # Más grande
            style={
                "text_align": "center",
                "margin_bottom": "2.5rem",
                "font_weight": "900",
                "font_size": "3.5rem",  # Tamaño manual extra grande
                "color": rx.cond(theme.ThemeState.dark_mode, "#ffffff", "#ffffff"),
                "letter_spacing": "0.08em",
                "text_shadow": rx.cond(
                    theme.ThemeState.dark_mode,
                    "0 4px 32px #222, 0 2px 16px #ffe066",
                    "0 4px 32px #ffe066, 0 2px 16px #b8860b"
                ),
                "text_transform": "uppercase",
                "animation": "glow 2.5s infinite alternate",
            },
        ),
        rx.html(
            """
            <style>
            @keyframes glow {
                0% {
                    text-shadow: 0 0 12px #ffe066, 0 0 24px #ffe06644;
                }
                100% {
                    text-shadow: 0 0 32px #ffe066, 0 0 48px #ffe06699;
                }
            }
            .servicio-card {
                transition: transform 0.5s cubic-bezier(.4,2,.6,1), box-shadow 0.4s;
                box-shadow: 0 4px 32px #ffe06644, 0 2px 8px rgba(0,0,0,0.08);
                border-radius: 18px;
                overflow: hidden;
                background: {{background_color}}; /* Se reemplaza dinámicamente abajo */
                cursor: pointer;
            }
            .servicio-card:hover {
                transform: scale(1.07) rotate(-2deg);
                box-shadow: 0 8px 48px #ffe06699, 0 4px 16px #b8860b33;
            }
            .servicio-img {
                width: 100%;
                height: 220px;
                object-fit: cover;
                transition: transform 1.5s cubic-bezier(.4,2,.6,1);
            }
            </style>
            """
        ),
          rx.hstack(
            *[
                rx.box(
                    rx.image(
                        src=servicio["img"],
                        alt=servicio["titulo"],
                        class_name="servicio-img",
                    ),
                    rx.box(
                        rx.text(
                            servicio["titulo"],
                            style={
                                "font_weight": "bold",
                                "font_size": "1.3rem",
                                "color": rx.cond(theme.ThemeState.dark_mode, "#ffe066", "#b8860b"),
                                "margin_top": "1rem",
                                "margin_bottom": "0.5rem",
                                "text_align": "center",
                                "letter_spacing": "0.03em",
                            },
                        ),
                        rx.text(
                            servicio["desc"],
                            style={
                                "color": rx.cond(theme.ThemeState.dark_mode, "#fff", "#222"),
                                "font_size": "1.05rem",
                                "text_align": "center",
                                "margin_bottom": "1.2rem",
                                "padding": "0 1rem",
                            },
                        ),
                        style={
                            "padding": "0.5rem 0.5rem 1.2rem 0.5rem",
                        },
                    ),
                    class_name="servicio-card",
                    style={
                        "width": "300px",
                        "margin": "2.5rem 2.5rem 2.5rem 2.5rem",  # Más separación entre tarjetas
                        "background": rx.cond(theme.ThemeState.dark_mode, "rgba(34,34,34,0.80)", "rgba(255,251,230,0.85)"),  # Más traslúcido
                        "display": "flex",
                        "flex_direction": "column",
                        "align_items": "center",
                        "justify_content": "flex-start",
                        "box_shadow": rx.cond(
                            theme.ThemeState.dark_mode,
                            "0 4px 32px #222, 0 2px 8px #ffe06644",
                            "0 4px 32px #ffe06644, 0 2px 8px rgba(0,0,0,0.08)"
                        ),
                        "padding": "1.5rem 1rem",  # Más espacio interno
                        "border_radius": "22px",
                    },
                )
                for servicio in SERVICIOS
            ],
            justify_content="center",
            align_items="stretch",
            spacing="4",  # Más espacio entre columnas
            style={
                "margin": "0 auto",
                "max_width": "1400px",
                "flex_wrap": "wrap",
                "row_gap": "3.5rem",  # Más espacio entre filas
                "column_gap": "3.5rem",
            },
        ),
        style={
            "padding": "6rem 0 7rem 0",  # Más espacio arriba y abajo
            "background": rx.cond(
                theme.ThemeState.dark_mode,
                "linear-gradient(120deg, #181818 60%, #222 100%)",
                "linear-gradient(120deg, #fffbe6 60%, #ffe066 100%)"
            ),
            "background_image": "url('/R.jpg')",
            "background_size": "cover",
            "background_position": "center",
            "width": "100%",
            "transition": "background 0.3s",
        },
        id="servicios",
        
    )