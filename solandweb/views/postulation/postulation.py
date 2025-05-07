import reflex as rx
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
import os

# Cargar las variables del archivo .env
load_dotenv()

class PostulationState(rx.State):
    is_modal_open: bool = False
    email: str = ""
    selected_job: str = ""
    file_path: str = ""  # Estado para almacenar la ruta del archivo cargado
    alert_message: str = ""  # Mensaje de alerta
    alert_type: str = ""  # Tipo de alerta: "success" o "error"

    def toggle_modal(self, job_title=""):
        """Abre o cierra el modal y asigna el título del trabajo."""
        if isinstance(job_title, str):  # Verifica que job_title sea una cadena
            self.selected_job = job_title
        else:
            self.selected_job = ""  # Asigna un valor por defecto si no es una cadena
        self.is_modal_open = not self.is_modal_open

    def set_email(self, value):
        self.email = value

    def set_file_path(self, value):
        self.file_path = value  # Actualiza la ruta del archivo cargado

    def send_email(self):
        """Envía el correo con el archivo adjunto."""
        try:
            # Cargar las credenciales desde el archivo .env
            sender_email = os.getenv("SENDER_EMAIL")
            receiver_email = os.getenv("RECEIVER_EMAIL")
            password = os.getenv("EMAIL_PASSWORD")

            print(f"Sender Email: {sender_email}")
            print(f"Receiver Email: {receiver_email}")
            print(f"Password Loaded: {'Yes' if password else 'No'}")


            if not sender_email or not receiver_email or not password:
                raise ValueError("Faltan variables de configuración en el archivo .env")

            # Crear el mensaje
            msg = MIMEMultipart()
            msg["From"] = sender_email
            msg["To"] = receiver_email
            msg["Subject"] = f"Postulación para {self.selected_job}"

            # Cuerpo del correo
            body = (
                f"Correo del postulante: {self.email}\n"
                f"Puesto seleccionado: {self.selected_job}\n"
                f"Se adjunta el archivo de postulación."
            )
            msg.attach(MIMEText(body, "plain"))

            # Adjuntar el archivo
            if self.file_path:
                attachment = MIMEBase("application", "octet-stream")
                with open(self.file_path, "rb") as file:
                    attachment.set_payload(file.read())
                encoders.encode_base64(attachment)
                attachment.add_header(
                    "Content-Disposition",
                    f"attachment; filename={self.file_path.split('/')[-1]}",
                )
                msg.attach(attachment)

            # Enviar el correo
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(sender_email, password)
                server.send_message(msg)

            # Mostrar alerta de éxito
            self.alert_message = "¡Correo enviado exitosamente!"
            self.alert_type = "success"
            self.toggle_modal()  # Cierra el modal después de enviar el correo
        except Exception as e:
            # Mostrar alerta de error
            self.alert_message = f"Error al enviar el correo: {e}"
            self.alert_type = "error"

def postulation():
    """Sección de postulación."""
    return rx.box(
        rx.text(
            "Puestos Disponibles",
            style={
                "font_size": "2.5rem",
                "font_weight": "bold",
                "margin_bottom": "2rem",
                "text_align": "center",
                "color": "#333",
            },
        ),
        rx.vstack(
            *[
                rx.box(
                    rx.text(
                        job["title"],
                        style={
                            "font_size": "1.8rem",
                            "font_weight": "bold",
                            "margin_bottom": "0.5rem",
                            "color": "#333",
                        },
                    ),
                    rx.text(
                        job["description"],
                        style={
                            "font_size": "1rem",
                            "margin_bottom": "1rem",
                            "color": "#666",
                        },
                    ),
                    rx.button(
                        "Postularse",
                        on_click=lambda job=job["title"]: PostulationState.toggle_modal(job),
                        style={
                            "background_color": "#FFD700",
                            "color": "black",
                            "padding": "0.5rem 1rem",
                            "border": "none",
                            "border_radius": "5px",
                            "cursor": "pointer",
                            "font_weight": "bold",
                        },
                    ),
                    style={
                        "padding": "1.5rem",
                        "border": "1px solid #ddd",
                        "border_radius": "10px",
                        "box_shadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",
                        "margin_bottom": "2rem",
                        "background_color": "#fff",
                    },
                )
                for job in [
                    {
                        "title": "Desarrollador Web",
                        "description": "Responsable del desarrollo y mantenimiento de sitios web modernos y escalables.",
                    },
                    {
                        "title": "Diseñador Gráfico",
                        "description": "Encargado de crear diseños visuales atractivos para proyectos digitales y físicos.",
                    },
                    {
                        "title": "Gerente de Marketing",
                        "description": "Planificación y ejecución de estrategias de marketing para aumentar la visibilidad de la empresa.",
                    },
                ]
            ],
            style={"width": "100%", "max_width": "800px", "margin": "0 auto"},
        ),
        # Mostrar alerta si hay un mensaje
        rx.cond(
            PostulationState.alert_message,
            rx.box(
                rx.text(
                    PostulationState.alert_message,
                    style={
                        "color": rx.cond(
                            PostulationState.alert_type == "success",
                            "green",  # Si es éxito
                            "red",    # Si es error
                        ),
                        "font_weight": "bold",
                        "margin_top": "1rem",
                    },
                ),
                style={
                    "padding": "1rem",
                    "border": "1px solid #ddd",
                    "border_radius": "5px",
                    "background_color": "#f9f9f9",
                    "margin_top": "1rem",
                },
            ),
        ),
        # MODAL USANDO rx.dialog
        rx.dialog.root(
            rx.dialog.trigger(
                rx.box(),  # Placeholder, no visible
            ),
            rx.dialog.content(
                rx.dialog.title(
                    f"Postulación para {PostulationState.selected_job}",
                ),
                rx.dialog.description(
                    "Ingresa tu correo y sube tu CV para postularte.",
                ),
                rx.input(
                    placeholder="Tu correo",
                    value=PostulationState.email,
                    on_change=PostulationState.set_email,
                    style={
                        "margin_bottom": "1rem",
                        "padding": "0.5rem",
                        "border": "1px solid #ddd",
                        "border_radius": "5px",
                        "width": "100%",
                    },
                ),
                rx.input(
                    type="file",
                    on_change=PostulationState.set_file_path,
                    style={
                        "margin_bottom": "1rem",
                        "padding": "0.5rem",
                        "border": "1px solid #ddd",
                        "border_radius": "5px",
                        "width": "100%",
                    },
                ),
                rx.flex(
                    rx.dialog.close(
                        rx.button(
                            "Cancelar",
                            variant="soft",
                            color_scheme="gray",
                        ),
                    ),
                    rx.button(
                        "Enviar",
                        on_click=PostulationState.send_email,
                        style={
                            "background_color": "#FFD700",
                            "color": "black",
                            "padding": "0.5rem 1rem",
                            "border": "none",
                            "border_radius": "5px",
                            "cursor": "pointer",
                            "font_weight": "bold",
                        },
                    ),
                    spacing="3",
                    justify="end",
                ),
                max_width="450px",
            ),
            open=PostulationState.is_modal_open,
            on_open_change=PostulationState.toggle_modal,
        ),
        style={
            "padding": "2rem",
            "background_color": "#f9f9f9",
            "border_radius": "10px",
            "box_shadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",
            "width": "100%",
        },
    )