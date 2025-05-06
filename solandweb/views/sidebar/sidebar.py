import reflex as rx
import solandweb.styles.styles as styles
from solandweb.styles.styles import Size as Size


class SidebarState(rx.State):
    """Estado para controlar la visibilidad del sidebar."""
    is_open: bool = True  # El sidebar está abierto por defecto

    def toggle_sidebar(self):
        """Alterna entre abierto y cerrado."""
        self.is_open = not self.is_open


def sidebar():
    return rx.box(
        rx.vstack(
            # Encabezado con el logo de Soland
            rx.hstack(
                rx.image(
                    src="logo.jpeg",  # Ruta del logo de Soland
                    alt="Solan Logo",
                    style={
                        "width": "150px",  # Tamaño del logo
                        "height": "auto",
                        "margin": "0 auto",  # Centrar el logo
                    },
                ),
                style={"padding": "1rem", "align_items": "center"},
            ),
            rx.divider(style={"margin": "1rem 0"}),  # Línea divisoria

            # Elementos del menú
            rx.vstack(
                rx.hstack(
                    rx.text("🏠", style={"margin_right": "1rem"}),  # Ícono
                    rx.cond(SidebarState.is_open, rx.text("Home", style={"font_size": "1rem"})),
                    style={"padding": "0.8rem 1rem", "cursor": "pointer"},
                ),
                rx.hstack(
                    rx.text("📝", style={"margin_right": "1rem"}),  # Ícono
                    rx.cond(SidebarState.is_open, rx.text("My Post", style={"font_size": "1rem"})),
                    style={"padding": "0.8rem 1rem", "cursor": "pointer"},
                ),
                rx.hstack(
                    rx.text("💬", style={"margin_right": "1rem"}),  # Ícono
                    rx.cond(SidebarState.is_open, rx.text("Chat", style={"font_size": "1rem"})),
                    style={"padding": "0.8rem 1rem", "cursor": "pointer"},
                ),
                rx.hstack(
                    rx.text("👥", style={"margin_right": "1rem"}),  # Ícono
                    rx.cond(SidebarState.is_open, rx.text("Invite Friends", style={"font_size": "1rem"})),
                    style={"padding": "0.8rem 1rem", "cursor": "pointer"},
                ),
                rx.hstack(
                    rx.text("🔔", style={"margin_right": "1rem"}),  # Ícono
                    rx.cond(SidebarState.is_open, rx.text("Notification", style={"font_size": "1rem"})),
                    style={"padding": "0.8rem 1rem", "cursor": "pointer"},
                ),
                rx.hstack(
                    rx.text("ℹ️", style={"margin_right": "1rem"}),  # Ícono
                    rx.cond(SidebarState.is_open, rx.text("About us", style={"font_size": "1rem"})),
                    style={"padding": "0.8rem 1rem", "cursor": "pointer"},
                ),
                rx.hstack(
                    rx.text("🛠️", style={"margin_right": "1rem"}),  # Ícono
                    rx.cond(SidebarState.is_open, rx.text("Support", style={"font_size": "1rem"})),
                    style={"padding": "0.8rem 1rem", "cursor": "pointer"},
                ),
                rx.hstack(
                    rx.text("❓", style={"margin_right": "1rem"}),  # Ícono
                    rx.cond(SidebarState.is_open, rx.text("FAQ", style={"font_size": "1rem"})),
                    style={"padding": "0.8rem 1rem", "cursor": "pointer"},
                ),
                rx.hstack(
                    rx.text("🚪", style={"margin_right": "1rem"}),  # Ícono
                    rx.cond(SidebarState.is_open, rx.text("Logout", style={"font_size": "1rem", "color": "red"})),
                    style={"padding": "0.8rem 1rem", "cursor": "pointer"},
                ),
                style={"margin_top": "1rem"},
            ),

            # Botón inferior para cerrar el sidebar
            rx.button(
                rx.cond(SidebarState.is_open, "Close", "Open"),
                on_click=SidebarState.toggle_sidebar,  # Alterna el estado del sidebar
                style={
                    "background_color": "#FFD700",  # Amarillo
                    "color": "black",
                    "padding": "0.8rem 1rem",
                    "border": "none",
                    "border_radius": "5px",
                    "cursor": "pointer",
                    "font_weight": "bold",
                    "margin_top": "2rem",
                },
            ),
            style={"align_items": "center"},
        ),
        style={
            "background_color": "#FFF",  # Fondo blanco
            "width": rx.cond(SidebarState.is_open, "250px", "60px"),  # Ancho dinámico
            "height": "100vh",  # Altura completa
            "position": "fixed",  # Fijo en la pantalla
            "top": "0",
            "left": "0",
            "box_shadow": "2px 0 5px rgba(0, 0, 0, 0.1)",  # Sombra para un efecto sofisticado
            "padding": "1rem",
            "overflow_y": "auto",  # Scroll si el contenido es largo
            "transition": "width 0.3s ease",  # Animación suave al abrir/cerrar
        },
    )