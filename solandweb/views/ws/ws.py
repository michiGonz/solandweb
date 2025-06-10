import reflex as rx

def whatsapp_button():
    return rx.link(
        rx.button(
            rx.image(
                src="/ws.png",
                width="48px",
                height="48px",
                style={"margin_right": "12px"}
            ),
            style={
                "display": "flex",
                "align_items": "center",
                "gap": "8px",
                "position": "fixed",
                "bottom": "32px",
                "right": "32px",
                "color": "white",
                "padding": "16px 24px",
                "font_weight": "bold",
                "font_size": "1.1em",
                "z_index": 9999,
                "cursor": "pointer",
                "box_shadow": "none",
                "background": "none"
            }
        ),
        href="https://wa.me/1234567890",  # Reemplaza con el número deseado
        is_external=True
    )