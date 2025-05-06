from flask import Flask, request, jsonify
import os
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

# Configuración para la carpeta donde se guardarán los archivos
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Configuración del correo electrónico
EMAIL_ADDRESS = 'tu_correo@example.com'  # Reemplaza con tu correo
EMAIL_PASSWORD = 'tu_contraseña'         # Reemplaza con tu contraseña o contraseña de aplicación

@app.route('/submit-cv', methods=['POST'])
def submit_cv():
    if 'cv' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['cv']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Guardar el archivo en la carpeta de uploads
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Enviar el archivo por correo electrónico
        send_email(file_path, file.filename)

        return jsonify({'message': 'File uploaded and sent via email successfully'}), 200

def send_email(file_path, file_name):
    msg = EmailMessage()
    msg['Subject'] = 'Nuevo CV recibido'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = 'rrhh.soland@gmail.com'  # Reemplaza con el correo del destinatario
    msg.set_content('Se ha recibido un nuevo CV. Consulta el archivo adjunto.')

    # Adjuntar el archivo
    with open(file_path, 'rb') as f:
        file_data = f.read()
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    # Enviar el correo
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

if __name__ == '__main__':
    app.run(debug=True)