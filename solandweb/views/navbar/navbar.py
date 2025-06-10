import reflex as rx
import solandweb.styles.styles as styles
from solandweb.styles.styles import Size as Size
import solandweb.theme as theme

def navbar():
    return rx.box(
        rx.hstack(
            rx.image(
                src="/logo.png",
                alt="Logo",
                style={
                    "width": "120px",
                    "height": "auto",
                    "margin_right": "2rem",
                },
            ),
            rx.html(
                """
                <style>
                .nav-link {
                    cursor: pointer;
                    font-weight: bold;
                    color: #222;
                    margin-right: 1.5rem;
                    font-size: 1.08rem;
                    letter-spacing: 0.04em;
                    text-decoration: none;
                    padding: 0.3rem 0.7rem;
                    border-radius: 8px;
                    transition: background 0.2s, color 0.2s;
                }
                .nav-link:hover {
                    background: #ffe06622;
                }
                 .navbar-dark .nav-link {
                    color: #fff !important;
                }
                </style>
                """
            ),
            rx.hstack(
                rx.link(
                    "Inicio",
                    href="/",
                    class_name="nav-link",
                    style={
                        "color": rx.cond(theme.ThemeState.dark_mode, "#ffe066", "#222"),
                    },
                ),
                rx.link(
                    "Servicios",
                    href="#servicios",
                    class_name="nav-link",
                    style={
                        "color": rx.cond(theme.ThemeState.dark_mode, "#ffe066", "#222"),
                    },
                    on_click=rx.call_script(
                        """
                        document.querySelector('#servicios').scrollIntoView({ behavior: 'smooth' });
                        """
                    ),
                ),
                rx.link(
                    "Portafolio",
                    href="#portafolio",
                    class_name="nav-link",
                    style={
                        "color": rx.cond(theme.ThemeState.dark_mode, "#ffe066", "#222"),
                    },
                ),
                rx.link(
                    "Blog",
                    href="#blog",
                    class_name="nav-link",
                    style={
                        "color": rx.cond(theme.ThemeState.dark_mode, "#ffe066", "#222"),
                    },
                ),
                rx.link(
                    "Puestos disponibles",
                    href="/postulation",
                    class_name="nav-link",
                    style={
                        "color": rx.cond(theme.ThemeState.dark_mode, "#ffe066", "#222"),
                        "margin_left": "1.5rem"
                    },
                ),
                spacing="1",
            ),
            rx.button(
                "Contáctanos",
                style={
                    "background_color": rx.cond(theme.ThemeState.dark_mode, "#ffe066", "black"),
                    "color": rx.cond(theme.ThemeState.dark_mode, "#222", "white"),
                    "padding": "0.5rem 1rem",
                    "border_radius": "5px",
                    "cursor": "pointer",
                    "font_weight": "bold",
                    "box_shadow": rx.cond(
                        theme.ThemeState.dark_mode,
                        "0 2px 8px #ffe066",
                        "0 2px 8px rgba(0,0,0,0.10)"
                    ),
                    "transition": "background 0.3s, color 0.3s"
                },
                on_click=lambda: rx.redirect("/contact"),
            ),
            rx.button(
                rx.cond(
                    theme.ThemeState.dark_mode,
                    "☀️ Modo Claro",
                    "🌙 Modo Oscuro"
                ),
                on_click=theme.ThemeState.toggle_dark_mode,
                style={
                    "margin_left": "2rem",
                    "background": rx.cond(theme.ThemeState.dark_mode, "#222", "#ffe066"),
                    "color": rx.cond(theme.ThemeState.dark_mode, "#ffe066", "#222"),
                    "font_weight": "bold",
                    "border_radius": "8px",
                    "padding": "0.5rem 1rem",
                    "border": "none",
                    "cursor": "pointer",
                    "box_shadow": rx.cond(
                        theme.ThemeState.dark_mode,
                        "0 2px 8px #ffe066",
                        "0 2px 8px rgba(0,0,0,0.10)"
                    ),
                    "transition": "background 0.3s, color 0.3s"
                }
            ),
            justify="between",
            align_items="center",
            width="100%",
            style={
                "padding": "1rem 2rem",
                "background_color": rx.cond(
                    theme.ThemeState.dark_mode,
                    "rgba(24,24,24,0.97)",
                    "rgba(255, 215, 0, 0.8)"
                ),
                "box_shadow": rx.cond(
                    theme.ThemeState.dark_mode,
                    "0px 4px 12px #222",
                    "0px 4px 6px rgba(0, 0, 0, 0.1)"
                ),
                "position": "fixed",
                "top": "0",
                "z_index": "1000",
                "backdrop_filter": "blur(4px)",
                "transition": "background-color 0.3s, box-shadow 0.3s"
            },
        ),
        style={
            "width": "100%"
        },
            class_name= rx.cond(
                theme.ThemeState.dark_mode,
                "navbar-dark",
                ""
            ),

    )