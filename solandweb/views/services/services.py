import reflex as rx
import solandweb.styles.styles as styles

def services_section() -> rx.Component:
    """Services section."""
    return rx.box(
        rx.text(
            "Gallery",
            style={
                "font_size": "2.5rem",
                "font_weight": "bold",
                "margin_bottom": "1rem",
                "color": "#333",
                "text_align": "center",
            },
        ),
        rx.text(
            "Lorem ipsum dolor sit amet consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam quis nostrud exercitation ullamco laboris.",
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
                rx.image(src="/path/to/image1.jpg", alt="Service 1", style={"width": "100%", "border_radius": "8px"}),
                rx.text("Lorem sito ameto consectetuer.", style={"font_weight": "bold", "margin_top": "0.5rem"}),
                rx.text("Lorem ipsum dolor sit amet consectetuer.", style={"color": "#666", "margin_bottom": "1rem"}),
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
                rx.image(src="/path/to/image2.jpg", alt="Service 2", style={"width": "100%", "border_radius": "8px"}),
                rx.text("Lorem sito ameto consectetuer.", style={"font_weight": "bold", "margin_top": "0.5rem"}),
                rx.text("Lorem ipsum dolor sit amet consectetuer.", style={"color": "#666", "margin_bottom": "1rem"}),
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
                rx.image(src="/path/to/image3.jpg", alt="Service 3", style={"width": "100%", "border_radius": "8px"}),
                rx.text("Lorem sito ameto consectetuer.", style={"font_weight": "bold", "margin_top": "0.5rem"}),
                rx.text("Lorem ipsum dolor sit amet consectetuer.", style={"color": "#666", "margin_bottom": "1rem"}),
                style={
                    "text_align": "center",
                    "padding": "1rem",
                    "border": "1px solid #ddd",
                    "border_radius": "8px",
                    "box_shadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",
                    "width": "30%",
                },
            ),
            justify="between",
            spacing="2",  # Cambiado de "2rem" a 2
            style={"width": "100%"},
        ),
        rx.hstack(
            rx.button(
                "View details",
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
            rx.button(
                "Contacts",
                style={
                    "background_color": "transparent",
                    "color": "#ffcc00",
                    "padding": "0.5rem 1rem",
                    "border": "2px solid #ffcc00",
                    "border_radius": "5px",
                    "cursor": "pointer",
                    "font_weight": "bold",
                },
            ),
            justify="center",
            spacing="1",  # Cambiado de "1rem" a 1
            style={"margin_top": "2rem"},
        ),
        style={
            "padding": "2rem", 
            "border_radius": "10px",
            "box_shadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",
            "width": "100%",
        },
    )