import reflex as rx
from typing import List, Dict

class CarouselState(rx.State):
    index: int = 0

    puestos: List[Dict[str, str]] = [
        {
            "title": "Desarrollador Web",
            "description": "Desarrolla y mantiene aplicaciones web modernas y escalables.",
            "image": "/imagen1.jpg",
        },
        {
            "title": "Diseñador Gráfico",
            "description": "Crea diseños visuales atractivos para proyectos digitales.",
            "image": "/imagen1.jpg",
        },
        {
            "title": "Project Manager",
            "description": "Lidera equipos y asegura la entrega exitosa de proyectos.",
            "image": "/imagen1.jpg",
        },
    ]

    def siguiente(self):
        self.index = (self.index + 1) % len(self.puestos)

    def anterior(self):
        self.index = (self.index - 1) % len(self.puestos)

def carousel():
    puesto = CarouselState.puestos[CarouselState.index]
    return rx.center(
        rx.box(
            rx.image(
                src=puesto["image"],
                alt=puesto["title"],
                style={
                    "width": "350px",
                    "height": "200px",
                    "object_fit": "cover",
                    "border_radius": "12px",
                    "box_shadow": "0 4px 16px rgba(0,0,0,0.08)",
                },
            ),
            rx.text(
                puesto["title"],
                style={
                    "font_size": "1.3rem",
                    "font_weight": "bold",
                    "margin_top": "1rem",
                    "color": "#222",
                },
            ),
            rx.text(
                puesto["description"],
                style={
                    "font_size": "1rem",
                    "margin": "0.5rem 0 1rem 0",
                    "color": "#444",
                },
            ),
            rx.hstack(
                rx.button("Anterior", on_click=CarouselState.anterior),
                rx.button("Siguiente", on_click=CarouselState.siguiente),
                spacing="2",
                justify="center",
            ),
            style={
                "background": "white",
                "border_radius": "18px",
                "box_shadow": "0 8px 32px rgba(0,0,0,0.10)",
                "padding": "2rem",
                "min_width": "350px",
                "max_width": "400px",
                "text_align": "center",
            },
        ),
        style={"width": "100%", "margin": "40px 0"},
    )