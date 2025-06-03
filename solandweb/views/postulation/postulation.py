import reflex as rx
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from dotenv import load_dotenv

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
        self.selected_job = job_title if isinstance(job_title, str) else ""
        self.is_modal_open = not self.is_modal_open

    def set_email(self, value):
        """Establece el correo del postulante."""
        self.email = value

    def set_file_path(self, value):
        """Establece la ruta del archivo cargado."""
        try:
            # Verifica que el valor sea un diccionario con la clave 'file'
            if not isinstance(value, dict) or "file" not in value:
                raise ValueError("El archivo cargado no es válido.")

            file = value["file"]

            # Directorio donde se guardarán los archivos
            upload_dir = "uploads"
            os.makedirs(upload_dir, exist_ok=True)  # Crea el directorio si no existe

            # Ruta completa del archivo
            file_path = os.path.join(upload_dir, file.filename)
            with open(file_path, "wb") as f:
                f.write(file.file.read())  # Guarda el contenido del archivo

            self.file_path = file_path  # Actualiza la ruta del archivo cargado
            print(f"Archivo guardado en: {self.file_path}")
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")
            self.alert_message = f"Error al guardar el archivo: {e}"
            self.alert_type = "error"

    def send_email(self):
        """Envía el correo con el archivo adjunto."""
        try:
            # Cargar las credenciales desde el archivo .env
            sender_email = os.getenv("SENDER_EMAIL")
            receiver_email = os.getenv("RECEIVER_EMAIL")
            password = os.getenv("EMAIL_PASSWORD")

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
            if self.file_path and os.path.exists(self.file_path):
                attachment = MIMEBase("application", "octet-stream")
                with open(self.file_path, "rb") as file:
                    attachment.set_payload(file.read())
                encoders.encode_base64(attachment)
                attachment.add_header(
                    "Content-Disposition",
                    f"attachment; filename={os.path.basename(self.file_path)}",
                )
                msg.attach(attachment)
            else:
                raise FileNotFoundError("El archivo no se encontró en el servidor.")

            # Enviar el correo
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(sender_email, password)
                server.send_message(msg)

            self.alert_message = "¡Correo enviado exitosamente!"
            self.alert_type = "success"
            self.toggle_modal()  # Cierra el modal después de enviar el correo
        except Exception as e:
            print(f"Error al enviar el correo: {e}")
            self.alert_message = f"Error al enviar el correo: {e}"
            self.alert_type = "error"

def postulation_modal():
    """Componente del modal para la postulación."""
    return rx.cond(
        PostulationState.is_modal_open,
        rx.box(
            rx.text(
                f"Postulación para {PostulationState.selected_job}",
                style={
                    "font_size": "1.5rem",
                    "font_weight": "bold",
                    "margin_bottom": "1rem",
                    "text_align": "center",
                },
            ),
            rx.input(
                placeholder="Ingresa tu correo",
                on_change=PostulationState.set_email,
                style={
                    "width": "100%",
                    "padding": "0.5rem",
                    "margin_bottom": "1rem",
                    "border": "1px solid #ddd",
                    "border_radius": "5px",
                },
            ),
            rx.form(
                rx.input(
                    type="file",
                    name="file",
                    style={
                        "margin_bottom": "1rem",
                    },
                ),
                rx.button(
                    "Subir archivo",
                    type="submit",
                    style={
                        "background_color": "#4CAF50",
                        "color": "white",
                        "padding": "0.5rem 1rem",
                        "border": "none",
                        "border_radius": "5px",
                        "cursor": "pointer",
                        "font_weight": "bold",
                    },
                ),
                on_submit=PostulationState.set_file_path,
                style={
                    "margin_bottom": "1rem",
                },
            ),
            rx.hstack(
                rx.button(
                    "Enviar",
                    on_click=PostulationState.send_email,
                    style={
                        "background_color": "#4CAF50",
                        "color": "white",
                        "padding": "0.5rem 1rem",
                        "border": "none",
                        "border_radius": "5px",
                        "cursor": "pointer",
                        "font_weight": "bold",
                    },
                ),
                rx.button(
                    "Cancelar",
                    on_click=PostulationState.toggle_modal,
                    style={
                        "background_color": "#f44336",
                        "color": "white",
                        "padding": "0.5rem 1rem",
                        "border": "none",
                        "border_radius": "5px",
                        "cursor": "pointer",
                        "font_weight": "bold",
                    },
                ),
                justify="between",
            ),
            style={
                "position": "fixed",
                "top": "50%",
                "left": "50%",
                "transform": "translate(-50%, -50%)",
                "background_color": "white",
                "padding": "2rem",
                "border_radius": "10px",
                "box_shadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",
                "z_index": "1000",
                "width": "400px",
            },
        ),
    )

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
        postulation_modal(),  # Agrega el modal aquí
        style={
            "padding": "2rem",
            "background_color": "#f9f9f9",
            "border_radius": "10px",
            "box_shadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",
            "width": "100%",
        },
    )