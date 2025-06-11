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
                "position": "fixed",
                "bottom": "32px",
                "right": "32px",
                "cursor": "pointer",
                "background": "none"
            }
        ),
        href="https://wa.me/1234567890",  # Reemplaza con el número deseado
        is_external=True
    )