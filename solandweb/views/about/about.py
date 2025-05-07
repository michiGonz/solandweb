import reflex as rx

def about():
    return rx.box(
        rx.text(
            "About Us",
            style={
                "font_size": "2.5rem",
                "font_weight": "bold",
                "margin_bottom": "1rem",
                "color": "#333",
                "text_align": "center",
            },
        ),
        rx.text(
            "Learn more about our team and what drives us to deliver the best solutions for you.",
            style={
                "font_size": "1rem",
                "color": "#666",
                "text_align": "center",
                "margin_bottom": "2rem",
                "line_height": "1.5",
            },
        ),
        rx.hstack(     
            rx.box(
                rx.image(src="/imagen2.jpg", alt="Our Mission", style={"width": "100%", "border_radius": "8px"}),
                rx.text("Our Mission", style={"font_weight": "bold", "margin_top": "0.5rem"}),
                rx.text("Discover our goals and how we aim to achieve them.", style={"color": "#666", "margin_bottom": "1rem"}),
                rx.button(
                    "Learn more",
                    style={
                        "background_color": "#ffcc00",
                        "color": "black",
                        "padding": "0.5rem 1rem",
                        "border": "none",
                        "border_radius": "5px",
                        "cursor": "pointer",
                        "font_weight": "bold",
                    },
                ),
                style={
                    "text_align": "center",
                    "padding": "1rem",
                    "border": "1px solid #ddd",
                    "border_radius": "8px",
                    "box_shadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",
                    "width": "30%",
                },
            ),
            rx.box(
                rx.image(src="/imagen2.jpg", alt="Our Mission", style={"width": "100%", "border_radius": "8px"}),
                rx.text("Our Mission", style={"font_weight": "bold", "margin_top": "0.5rem"}),
                rx.text("Discover our goals and how we aim to achieve them.", style={"color": "#666", "margin_bottom": "1rem"}),
                rx.button(
                    "Learn more",
                    style={
                        "background_color": "#ffcc00",
                        "color": "black",
                        "padding": "0.5rem 1rem",
                        "border": "none",
                        "border_radius": "5px",
                        "cursor": "pointer",
                        "font_weight": "bold",
                    },
                ),
                style={
                    "text_align": "center",
                    "padding": "1rem",
                    "border": "1px solid #ddd",
                    "border_radius": "8px",
                    "box_shadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",
                    "width": "30%",
                },
            ),
            justify="center",  # Centra los contenedores horizontalmente
            spacing="2",
        ),
        style={
            "padding": "2rem",
            "background_image": "url('/prueba.png)", 
            "border_radius": "10px",
            "box_shadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",
            "width": "100%",
        },
    )