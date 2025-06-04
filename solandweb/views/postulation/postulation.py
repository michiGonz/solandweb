import reflex as rx
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from dotenv import load_dotenv
from solandweb.views.navbar.navbar import navbar

# Cargar las variables del archivo .env
load_dotenv()

class PostulationState(rx.State):
    is_modal_open: bool = False
    email: str = ""
    selected_job: str = ""
    file_path: str = ""
    alert_message: str = ""
    alert_type: str = ""

    def toggle_modal(self, job_title=""):
        self.selected_job = job_title if isinstance(job_title, str) else ""
        self.is_modal_open = not self.is_modal_open

    def set_email(self, value):
        self.email = value

    def set_file_path(self, value):
        try:
            if not isinstance(value, dict) or "file" not in value:
                raise ValueError("El archivo cargado no es válido.")
            file = value["file"]
            upload_dir = "uploads"
            os.makedirs(upload_dir, exist_ok=True)
            file_path = os.path.join(upload_dir, file.filename)
            with open(file_path, "wb") as f:
                f.write(file.file.read())
            self.file_path = file_path
            print(f"Archivo guardado en: {self.file_path}")
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")
            self.alert_message = f"Error al guardar el archivo: {e}"
            self.alert_type = "error"

    def send_email(self):
        try:
            sender_email = os.getenv("SENDER_EMAIL")
            receiver_email = os.getenv("RECEIVER_EMAIL")
            password = os.getenv("EMAIL_PASSWORD")
            if not sender_email or not receiver_email or not password:
                raise ValueError("Faltan variables de configuración en el archivo .env")
            msg = MIMEMultipart()
            msg["From"] = sender_email
            msg["To"] = receiver_email
            msg["Subject"] = f"Postulación para {self.selected_job}"
            body = (
                f"Correo del postulante: {self.email}\n"
                f"Puesto seleccionado: {self.selected_job}\n"
                f"Se adjunta el archivo de postulación."
            )
            msg.attach(MIMEText(body, "plain"))
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
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(sender_email, password)
                server.send_message(msg)
            self.alert_message = "¡Correo enviado exitosamente!"
            self.alert_type = "success"
            self.toggle_modal()
        except Exception as e:
            print(f"Error al enviar el correo: {e}")
            self.alert_message = f"Error al enviar el correo: {e}"
            self.alert_type = "error"

def postulation_modal():
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
                    "color": "#000",  # Letras negras
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
                    "color": "#000",  # Letras negras
                },
            ),
            rx.form(
                rx.input(
                    type="file",
                    name="file",
                    style={
                        "margin_bottom": "1rem",
                        "color": "#000",  # Letras negras
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
                # Sombra eliminada
                "z_index": "1000",
                "width": "400px",
            },
        ),
    )

def postulation():
    """Sección de postulación."""
    return rx.box(
        navbar(),
        rx.box(
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
                        
                    ]
                ],
                style={"width": "100%", "max_width": "800px", "margin": "0 auto"},
            ),
            postulation_modal(),
            style={
                "padding": "2rem",
                "background_image": "url('header.jpg')",  # Usa el mismo fondo que la página principal
                "background_size": "cover",
                "background_position": "center",
                "border_radius": "10px",
                "box_shadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",
                "width": "100%",
                "max_width": "900px",
                "margin": "3rem auto 2rem auto",
            },
        ),
        style={
            "width": "100%",
            "background_image": "url('fondo.jpg')",  # Fondo general igual que principal
            "background_size": "cover",
            "background_position": "center",
            "min_height": "100vh",
        },
    )