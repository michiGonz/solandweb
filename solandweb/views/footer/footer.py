import reflex as rx
import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import solandweb.theme as theme

load_dotenv()

class FooterState(rx.State):
    user_email: str = ""
    user_message: str = ""
    alert_message: str = ""
    alert_type: str = ""

    def set_user_email(self, value):
        self.user_email = value

    def set_user_message(self, value):
        self.user_message = value

    def send_message(self):
        try:
            company_email = os.getenv("RECEIVER_EMAIL")
            sender_email = os.getenv("SENDER_EMAIL")
            password = os.getenv("EMAIL_PASSWORD")

            if not company_email or not sender_email or not password:
                raise ValueError("Faltan variables de configuración en el archivo .env")

            msg = MIMEText(
                f"Mensaje de: {self.user_email}\n\n{self.user_message}"
            )
            msg["Subject"] = "Solicitud de servicios desde el sitio web"
            msg["From"] = sender_email
            msg["To"] = company_email

            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(sender_email, password)
                server.send_message(msg)

            self.alert_message = "¡Mensaje enviado exitosamente!"
            self.alert_type = "success"
            self.user_email = ""
            self.user_message = ""
        except Exception as e:
            self.alert_message = f"Error al enviar el mensaje: {e}"
            self.alert_type = "error"

def footer():
    return rx.box(
        rx.hstack(
            rx.box(
                rx.text(
                    "© 2025 SolandWeb. Todos los derechos reservados.",
                    style={
                        "color": rx.cond(theme.ThemeState.dark_mode, "#fff", "#222"),
                        "font_size": "1rem",
                        "margin_bottom": "0.5rem",
                    },
                ),
                rx.text(
                    "Dirección: Calle Ficticia 123, Ciudad, País",
                    style={
                        "color": rx.cond(theme.ThemeState.dark_mode, "#fff", "#222"),
                        "font_size": "0.9rem"
                    },
                ),
                rx.text(
                    "Teléfono: +123 456 7890",
                    style={
                        "color": rx.cond(theme.ThemeState.dark_mode, "#fff", "#222"),
                        "font_size": "0.9rem"
                    },
                ),
                rx.text(
                    "Email: contacto@solandweb.com",
                    style={
                        "color": rx.cond(theme.ThemeState.dark_mode, "#fff", "#222"),
                        "font_size": "0.9rem"
                    },
                ),
                style={
                    "width": "40%",
                    "padding": "1rem",
                },
            ),
            rx.box(
                rx.text(
                    "¿Deseas solicitar un servicio o tienes una consulta?",
                    style={
                        "color": rx.cond(theme.ThemeState.dark_mode, "#fff", "#222"),
                        "font_weight": "bold",
                        "margin_bottom": "0.5rem",
                        "font_size": "1.1rem",
                    },
                ),
                rx.text(
                    "Correo electrónico",
                    style={
                        "color": rx.cond(theme.ThemeState.dark_mode, "#fff", "#222"),
                        "font_weight": "bold",
                        "margin_bottom": "0.2rem",
                        "font_size": "1rem",
                        "margin_top": "0.7rem",
                    },
                ),
                rx.input(
                    placeholder="Tu correo electrónico",
                    value=FooterState.user_email,
                    on_change=FooterState.set_user_email,
                    style={
                        "width": "100%",
                        "padding": "0.5rem",
                        "margin_bottom": "0.5rem",
                        "border_radius": "5px",
                        "border": "none",
                        "background_color": "rgba(0,0,0,0)",
                        "color": rx.cond(theme.ThemeState.dark_mode, "#fff", "#222"),
                    },
                ),
                rx.text(
                    "Mensaje",
                    style={
                        "color": rx.cond(theme.ThemeState.dark_mode, "#fff", "#222"),
                        "font_weight": "bold",
                        "margin_bottom": "0.2rem",
                        "font_size": "1rem",
                        "margin_top": "0.7rem",
                    },
                ),
                rx.text_area(
                    placeholder="Escribe tu mensaje...",
                    value=FooterState.user_message,
                    on_change=FooterState.set_user_message,
                    style={
                        "width": "100%",
                        "padding": "0.5rem",
                        "margin_bottom": "0.5rem",
                        "border_radius": "5px",
                        "border": "none",
                        "min_height": "60px",
                        "resize": "vertical",
                        "background_color": "rgba(0,0,0,0)",
                        "color": rx.cond(theme.ThemeState.dark_mode, "#fff", "#222"),
                    },
                ),
                rx.button(
                    "Enviar mensaje",
                    on_click=FooterState.send_message,
                    style={
                        "background_color": rx.cond(theme.ThemeState.dark_mode, "#ffe066", "#222"),
                        "color": rx.cond(theme.ThemeState.dark_mode, "#222", "#fff"),
                        "padding": "0.5rem 1rem",
                        "border": "none",
                        "border_radius": "5px",
                        "cursor": "pointer",
                        "font_weight": "bold",
                    },
                ),
                rx.cond(
                    FooterState.alert_message != "",
                    rx.text(
                        FooterState.alert_message,
                        style={
                            "color": rx.cond(
                                FooterState.alert_type == "success",
                                rx.cond(theme.ThemeState.dark_mode, "#fff", "#222"),
                                "#ff3333"
                            ),
                            "margin_top": "0.5rem",
                            "font_weight": "bold",
                        },
                    ),
                ),
                style={
                    "width": "50%",
                    "padding": "1rem",
                },
            ),
            justify="between",
            align="start",
            style={"width": "100%"},
        ),
        style={
            "background": rx.cond(
                theme.ThemeState.dark_mode,
                "#000",
                "linear-gradient(90deg, #ffe066 60%, #222 100%)"
            ),
            "padding": "2rem 4rem 1rem 4rem",
            "border_top_left_radius": "20px",
            "border_top_right_radius": "20px",
            "box_shadow": "0px -2px 8px rgba(0,0,0,0.15)",
            "width": "100%",
            "margin_top": "3rem",
            "transition": "background 0.3s, color 0.3s"
        },
    )