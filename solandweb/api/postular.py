import reflex as rx
import smtplib
from email.message import EmailMessage

@rx.endpoint("/api/postular")
async def postular(data, files):
    nombre = data.get("nombre")
    apellido = data.get("apellido")
    cv = files.get("cv")
    if not nombre or not apellido or not cv:
        return {"ok": False, "error": "Faltan datos o archivo."}

    # Configura estos datos con los de tu empresa
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    SMTP_USER = "rrhh.soland@gmail.com"
    SMTP_PASS = "uxqngmchpyylwuga"
    TO_EMAIL = "rrhh.soland@gmail.com"

    try:
        msg = EmailMessage()
        msg["Subject"] = "Nueva postulación"
        msg["From"] = SMTP_USER
        msg["To"] = TO_EMAIL
        msg.set_content(
            f"Nombre: {nombre}\nApellido: {apellido}\n\nAdjunto el CV del postulante."
        )
        msg.add_attachment(
            cv,
            maintype="application",
            subtype="octet-stream",
            filename=f"{nombre}_{apellido}_CV.pdf"
        )
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.send_message(msg)
        return {"ok": True}
    except Exception as e:
        return {"ok": False, "error": f"Error al enviar correo: {e}"}