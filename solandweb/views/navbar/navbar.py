import reflex as rx
import solandweb.styles.styles as styles
from solandweb.styles.styles import Size as Size
import solandweb.theme as theme

def navbar():
    return rx.box(
        rx.hstack(
            # Logo de la empresa
            rx.image(
                src="/logo.png",
                alt="Logo",
                style={
                    "width": "120px",
                    "height": "auto",
                    "margin_right": "2rem",
                },
            ),
            # Menú principal
            rx.hstack(
                rx.link(
                    "Inicio",
                    href="/",
                    style={
                        "cursor": "pointer",
                        "font_weight": "bold",
                        "color": rx.cond(theme.ThemeState.dark_mode, "#ffe066", "black"),
                        "margin_right": "1.5rem"
                    },
                ),
                rx.text(
                    "Servicios",
                    style={
                        "cursor": "pointer",
                        "font_weight": "bold",
                        "color": rx.cond(theme.ThemeState.dark_mode, "#ffe066", "black"),
                        "margin_right": "1.5rem"
                    }
                ),
                rx.text(
                    "Portafolio",
                    style={
                        "cursor": "pointer",
                        "font_weight": "bold",
                        "color": rx.cond(theme.ThemeState.dark_mode, "#ffe066", "black"),
                        "margin_right": "1.5rem"
                    }
                ),
                rx.text(
                    "Blog",
                    style={
                        "cursor": "pointer",
                        "font_weight": "bold",
                        "color": rx.cond(theme.ThemeState.dark_mode, "#ffe066", "black"),
                        "margin_right": "1.5rem"
                    }
                ),
                rx.link(
                    "Puestos disponibles",
                    href="/postulation",
                    style={
                        "cursor": "pointer",
                        "font_weight": "bold",
                        "color": rx.cond(theme.ThemeState.dark_mode, "#ffe066", "black"),
                        "margin_left": "1.5rem"
                    },
                ),
                spacing="1",
            ),
            # Botón de acción
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
            # Botón modo oscuro
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
        style={"width": "100%"},
    )