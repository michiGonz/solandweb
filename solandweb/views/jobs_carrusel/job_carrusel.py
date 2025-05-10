import reflex as rx

class CarruselState(rx.State):
    current_index: int = 0
    current_job_title: str = ""
    current_job_description: str = ""
    current_job_image: str = ""

    jobs = [
        {
            "title": "Desarrollador Web",
            "description": "Responsable del desarrollo y mantenimiento de sitios web modernos y escalables.",
            "image": "/imagen2.jpg",
        },
        {
            "title": "Diseñador Gráfico",
            "description": "Encargado de crear diseños visuales atractivos para proyectos digitales y físicos.",
            "image": "/imagen2.jpg",
        },
        {
            "title": "Gerente de Marketing",
            "description": "Planificación y ejecución de estrategias de marketing para aumentar la visibilidad de la empresa.",
            "image": "/imagen2.jpg",
        },
    ]

    @rx.event
    def set_job(self):
        """Actualiza el trabajo actual basado en el índice."""
        self.current_job_title = self.jobs[self.current_index]["title"]
        self.current_job_description = self.jobs[self.current_index]["description"]
        self.current_job_image = self.jobs[self.current_index]["image"]

    @rx.event
    def next_slide(self):
        """Muestra el siguiente trabajo automáticamente."""
        self.current_index = (self.current_index + 1) % len(self.jobs)
        self.set_job()

    @rx.event
    async def start_auto_slide(self):
        """Configura el desplazamiento automático del carrusel."""
        while True:
            await rx.sleep(2)  # Espera 2 segundos
            self.next_slide()

    @rx.event
    def on_load(self):
        """Inicializa el carrusel al cargar la página y configura el desplazamiento automático."""
        self.set_job()
        self.start_auto_slide()

def job_carrusel():
    """Carrusel de vacantes disponibles."""
    return rx.box(
        rx.text(
            "Puestos Disponibles",  # Título del carrusel
            style={
                "font_size": "2rem",
                "font_weight": "bold",
                "text_align": "center",
                "margin_bottom": "1rem",
                "color": "#333",
            },
        ),
        rx.box(
            rx.image(
                CarruselState.current_job_image,
                style={
                    "width": "300px",  # Ajusta el ancho de la imagen
                    "height": "200px",  # Ajusta la altura de la imagen
                    "border_radius": "10px",
                    "margin": "0 auto",  # Centra la imagen horizontalmente
                    "display": "block",  # Asegura que la imagen sea un bloque centrado
                },
            ),
            rx.text(
                CarruselState.current_job_title,
                style={
                    "font_size": "1.5rem",
                    "font_weight": "bold",
                    "margin_bottom": "0.5rem",
                    "color": "#333",
                    "text_align": "center",  # Centra el texto
                },
            ),
            rx.text(
                CarruselState.current_job_description,
                style={
                    "font_size": "1rem",
                    "margin_bottom": "1rem",
                    "color": "#666",
                    "text_align": "center",  # Centra el texto
                },
            ),
            rx.button(
                "Ir a Postulación",
                on_click=lambda: rx.redirect("/postulation"),
                style={
                    "background_color": "#FFD700",
                    "color": "black",
                    "padding": "0.5rem 1rem",
                    "border": "none",
                    "border_radius": "5px",
                    "cursor": "pointer",
                    "font_weight": "bold",
                    "margin": "0 auto",  # Centra el botón horizontalmente
                    "display": "block",  # Asegura que el botón sea un bloque centrado
                },
            ),
            style={
                "padding": "1.5rem",
                "border": "1px solid #ddd",
                "border_radius": "10px",
                "box_shadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",
                "margin": "1rem",
                "background_color": "#fff",
                "text_align": "center",
            },
        ),
        style={
            "width": "100%",
            "max_width": "800px",
            "margin": "0 auto",
            "overflow": "hidden",
        },
    )