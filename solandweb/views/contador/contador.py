import reflex as rx

def contador():
    return rx.box(
        rx.hstack(
            # Contador 1: Proyectos hechos
            rx.box(
                rx.text("📁", style={"font_size": "3rem", "color": "#FFD700"}),  # Ícono amarillo
                rx.text("120", style={"font_size": "2.5rem", "font_weight": "bold", "color": "#FFD700"}),  # Número
                rx.text("Proyectos hechos", style={"font_size": "1rem", "color": "#FFF"}),  # Descripción
                style={"text_align": "center", "padding": "1rem"},
            ),
            # Contador 2: Descargas de aplicaciones
            rx.box(
                rx.text("📈", style={"font_size": "3rem", "color": "#FFD700"}),  # Ícono amarillo
                rx.text("1,000,000", style={"font_size": "2.5rem", "font_weight": "bold", "color": "#FFD700"}),  # Número
                rx.text("Descargas de aplicaciones", style={"font_size": "1rem", "color": "#FFF"}),  # Descripción
                style={"text_align": "center", "padding": "1rem"},
            ),
            # Contador 3: Países número 1
            rx.box(
                rx.text("🏆", style={"font_size": "3rem", "color": "#FFD700"}),  # Ícono amarillo
                rx.text("34", style={"font_size": "2.5rem", "font_weight": "bold", "color": "#FFD700"}),  # Número
                rx.text("Países número 1", style={"font_size": "1rem", "color": "#FFF"}),  # Descripción
                style={"text_align": "center", "padding": "1rem"},
            ),
            # Contador 4: Tazas de café
            rx.box(
                rx.text("☕", style={"font_size": "3rem", "color": "#FFD700"}),  # Ícono amarillo
                rx.text("7,304", style={"font_size": "2.5rem", "font_weight": "bold", "color": "#FFD700"}),  # Número
                rx.text("Tazas de café", style={"font_size": "1rem", "color": "#FFF"}),  # Descripción
                style={"text_align": "center", "padding": "1rem"},
            ),
            justify="center",  # Espaciado uniforme entre los contadores
            style={"width": "100%"},
        ),
        style={
            "background_color": "#333",  # Fondo oscuro
            "padding": "2rem",
            "border_radius": "10px",
            "box_shadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",  # Sombra para un efecto sofisticado
            "width": "100%",
        },
    )