import reflex as rx

def cv():
    return rx.box(
        rx.text(
            "Submit Your CV",
            class_name="section-title",
            style={
                "font_size": "2rem",
                "font_weight": "bold",
                "text_align": "center",
                "margin": "1rem 0",
                "color": "#333",
            },
        ),
        rx.form(
            rx.vstack(
                rx.input(
                    type="file",
                    name="cv",
                    accept=".pdf,.doc,.docx",
                    class_name="file-input",
                    style={
                        "padding": "0.5rem",
                        "border": "1px solid #ccc",
                        "border_radius": "5px",
                        "margin_bottom": "1rem",
                        "width": "100%",
                    },
                ),
                rx.button(
                    "Submit",
                    type="submit",
                    class_name="submit-button",
                    style={
                        "background_color": "#007BFF",
                        "color": "white",
                        "padding": "0.5rem 1rem",
                        "border": "none",
                        "border_radius": "5px",
                        "cursor": "pointer",
                        "font_size": "1rem",
                    },
                ),
            ),
            action="/submit-cv",
            method="POST",
            enc_type="multipart/form-data",
            style={
                "display": "flex",
                "flex_direction": "column",
                "align_items": "center",
                "width": "100%",
            },
        ),
        style={
            "padding": "2rem",
            "background_color": "#f9f9f9",
            "border_radius": "10px",
            "box_shadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",
            "max_width": "500px",
            "margin": "2rem auto",
        },
    )