import reflex as rx
from solandweb.views.navbar.navbar import navbar
from solandweb.views.footer.footer import footer

class PostulacionState(rx.State):
    show_modal: bool = False
    nombre: str = ""
    apellido: str = ""
    mensaje: str = ""
    mensaje_color: str = "#222"

    def abrir_modal(self):
        self.show_modal = True
        self.mensaje = ""
        self.nombre = ""
        self.apellido = ""

    def cerrar_modal(self):
        self.show_modal = False
        self.mensaje = ""

    def set_nombre(self, value):
        self.nombre = value

    def set_apellido(self, value):
        self.apellido = value

    def manejar_open(self, opened):
        if not opened:
            self.cerrar_modal()

    @rx.event
    async def enviar_postulacion(self, files: list[rx.UploadFile]):
        if not self.nombre or not self.apellido or not files:
            self.mensaje = "Por favor completa todos los campos y adjunta tu CV."
            self.mensaje_color = "#d32f2f"
            return
        try:
            cv_bytes = await files[0].read()
            # Aquí deberías manejar el envío (por ejemplo, guardar el archivo o enviar por email)
            # Simulación de éxito:
            self.mensaje = "¡Enviado correctamente!"
            self.mensaje_color = "#388e3c"
           
        except Exception:
            self.mensaje = "Ocurrió un error al enviar. Intenta de nuevo."
            self.mensaje_color = "#d32f2f"

def modal_postulacion():
    return rx.dialog.root(
        rx.dialog.trigger(rx.box()),  # Trigger vacío, controlado por show_modal
        rx.dialog.content(
            rx.dialog.title(
                "Postulación",
                style={"color": "#222", "font_weight": "bold", "font_size": "1.4rem"},
            ),
            rx.dialog.description(
                "Completa tus datos para postularte.",
                style={"color": "#222","font_weight": "bold"}
            ),
            rx.vstack(
                rx.text(
                    "Nombre",
                    style={
                        "color": "#222",
                        "font_weight": "bold",
                        "font_size": "0.95rem",
                        "margin_top": "1.2rem",
                        "margin_bottom": "0.3rem",
                    },
                ),
                rx.input(
                    placeholder="Nombre",
                    value=PostulacionState.nombre,
                    on_change=PostulacionState.set_nombre,
                    style={
                        "margin_bottom": "1rem",
                        "padding": "0.5em",
                        "border_radius": "4px",
                        "border": "1px solid #FFD700",
                        "background": "#fffffd",
                        "color": "#222",
                        "placeholder_color": "#222",
                    },
                ),
                rx.text(
                    "Apellido",
                    style={
                        "color": "#222",
                        "font_weight": "bold",
                        "font_size": "0.95rem",
                        "margin_top": "0.2rem",
                        "margin_bottom": "0.2rem",
                    },
                ),
                rx.input(
                    placeholder="Apellido",
                    value=PostulacionState.apellido,
                    on_change=PostulacionState.set_apellido,
                    style={
                        "margin_bottom": "1rem",
                        "padding": "0.5em",
                        "border_radius": "8px",
                        "border": "1px solid #FFD700",
                        "background": "#ffffff",
                        "color": "#222",
                        "placeholder_color": "#222",
                    },
                ),
                rx.upload(
                    rx.button(
                        "Adjuntar CV",
                        style={
                            "background_color": "#FFD700",
                            "color": "black",
                            "padding": "0.5rem 1.5rem",
                            "border": "none",
                            "border_radius": "5px",
                            "cursor": "pointer",
                            "font_weight": "bold",
                            "margin_bottom": "1rem",
                        },
                    ),
                    accept=".pdf,.doc,.docx",
                    max_files=1,
                    id="cv_upload",
                ),
                rx.cond(
                    PostulacionState.mensaje != "",
                    rx.text(
                        PostulacionState.mensaje,
                        style={
                            "color": PostulacionState.mensaje_color,
                            "font_weight": "bold",
                            "margin_top": "0.5rem",
                            "margin_bottom": "0.5rem",
                        },
                    ),
                ),
            ),
            rx.flex(
                rx.button(
                    "Enviar",
                    on_click=PostulacionState.enviar_postulacion(
                        rx.upload_files(upload_id="cv_upload")
                    ),
                    style={
                        "background_color": "#FFD700",
                        "color": "black",
                        "padding": "0.5rem 1.5rem",
                        "border": "none",
                        "border_radius": "5px",
                        "cursor": "pointer",
                        "font_weight": "bold",
                        "margin_right": "1rem",
                    },
                ),
                rx.dialog.close(
                    rx.button(
                        "Cancelar",
                        on_click=PostulacionState.cerrar_modal,
                        style={
                            "background_color": "#eee",
                            "color": "#222",
                            "padding": "0.5rem 1.5rem",
                            "border": "none",
                            "border_radius": "5px",
                            "cursor": "pointer",
                            "font_weight": "bold",
                        },
                    ),
                ),
                spacing="3",
                justify="end",
                margin_top="1rem",
            ),
            max_width="450px",
            style={
                "background": "white",
                "border_radius": "14px",
                "box_shadow": "0 8px 32px rgba(0,0,0,0.18)",
                "padding": "2rem",
                "min_width": "320px",
                "max_width": "95vw",
            },
        ),
        open=PostulacionState.show_modal,
        on_open_change=PostulacionState.manejar_open,
    )

def puestos_disponibles():
    puestos = [
        {
            "title": "Desarrollador Web",
            "description": "Responsable del desarrollo y mantenimiento de sitios web modernos y escalables.",
            "skills": ["Python", "JavaScript", "React", "Bases de datos"],
            "location": "Remoto",
        },
        {
            "title": "Diseñador Gráfico",
            "description": "Crea diseños visuales atractivos para proyectos digitales y físicos.",
            "skills": ["Photoshop", "Illustrator", "Creatividad"],
            "location": "Presencial - Santiago",
        },
        {
            "title": "Project Manager",
            "description": "Lidera equipos y asegura la entrega exitosa de proyectos tecnológicos.",
            "skills": ["Gestión", "Comunicación", "Scrum"],
            "location": "Híbrido",
        },
    ]

    return rx.box(
        modal_postulacion(),
        rx.text(
            "Puestos Disponibles",
            style={
                "font_size": "2.5rem",
                "font_weight": "bold",
                "margin_bottom": "2rem",
                "text_align": "center",
                "color": "#222",
                "letter_spacing": "1px",
            },
        ),
        rx.grid(
            *[
                rx.box(
                    rx.text(
                        puesto["title"],
                        style={
                            "font_size": "1.5rem",
                            "font_weight": "bold",
                            "margin_bottom": "0.5rem",
                            "color": "#222",
                        },
                    ),
                    rx.text(
                        puesto["description"],
                        style={
                            "font_size": "1rem",
                            "margin_bottom": "1rem",
                            "color": "#444",
                        },
                    ),
                    rx.hstack(
                        *[
                            rx.badge(
                                skill,
                                color_scheme="yellow",
                                style={"color": "black"}
                            )
                            for skill in puesto["skills"]
                        ],
                        spacing="2",
                        style={"margin_bottom": "1rem"},
                    ),
                    rx.text(
                        f"Ubicación: {puesto['location']}",
                        style={
                            "font_size": "0.95rem",
                            "color": "#666",
                            "margin_bottom": "1rem",
                        },
                    ),
                    rx.button(
                        "Postularse",
                        on_click=PostulacionState.abrir_modal,
                        style={
                            "background_color": "#FFD700",
                            "color": "black",
                            "padding": "0.5rem 1.5rem",
                            "border": "none",
                            "border_radius": "5px",
                            "cursor": "pointer",
                            "font_weight": "bold",
                            "box_shadow": "0px 2px 4px rgba(0,0,0,0.07)",
                        },
                    ),
                    style={
                        "padding": "2rem",
                        "background_color": "rgba(255,255,255,0.95)",
                        "border_radius": "12px",
                        "box_shadow": "0 4px 16px rgba(0,0,0,0.08)",
                        "border": "1px solid #eee",
                        "margin": "0.5rem",
                        "min_width": "260px",
                        "max_width": "350px",
                        "display": "flex",
                        "flex_direction": "column",
                        "align_items": "flex-start",
                    },
                )
                for puesto in puestos
            ],
            columns="3",
            spacing="2",
            style={"width": "100%", "margin": "0 auto"},
        ),
        style={
            "width": "100%",
            "max_width": "1200px",
            "margin": "110px auto 0 auto",
            "padding": "2rem 1rem 4rem 1rem",
            "background": "rgba(255,255,255,0.85)",
            "border_radius": "18px",
            "box_shadow": "0 8px 32px rgba(0,0,0,0.10)",
        },
    )

def postulation():
    return rx.box(
        navbar(),
        rx.box(
            puestos_disponibles(),
            style={
                "width": "100%",
                "min_height": "100vh",
                "background_image": "url('/fondo.jpg')",
                "background_size": "cover",
                "background_position": "center",
                "padding": "0",
            },
        ),
        footer(),
    )