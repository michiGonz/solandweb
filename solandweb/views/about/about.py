import reflex as rx
import solandweb.theme as theme

def about():
    return rx.box(
        rx.box(
            rx.text(
                "Sobre nosotros",
                style={
                    "font_size": "3rem",
                    "font_weight": "900",
                    "margin_bottom": "1.2rem",
                    "color": rx.cond(theme.ThemeState.dark_mode, "#ffe066", "#b8860b"),
                    "text_align": "center",
                    "letter_spacing": "0.08em",
                    "text_shadow": rx.cond(
                        theme.ThemeState.dark_mode,
                        "0 4px 32px #222, 0 2px 16px #ffe066",
                        "0 4px 32px #ffe066, 0 2px 16px #b8860b"
                    ),
                    "text_transform": "uppercase",
                },
            ),
            rx.hstack(
                rx.box(
                    rx.text(
                        "V I S I O N",
                        style={
                            "font_size": "1.7rem",
                            "font_weight": "bold",
                            "letter_spacing": "0.5rem",
                            "color": rx.cond(theme.ThemeState.dark_mode, "#ffe066", "#b8860b"),
                            "text_align": "center",
                            "margin_bottom": "0.9rem",
                            "text_shadow": "0 2px 12px #ffe066cc",
                        },
                    ),
                    rx.image(
                        src="/imagen2.jpg",
                        alt="Nuestra Visión",
                        class_name="about-img-anim",
                        style={
                            "width": "320px",
                            "height": "320px",
                            "object_fit": "cover",
                            "border_radius": "28px",
                            "margin": "0 auto 1.5rem auto",
                            "box_shadow": "0 8px 48px #ffe06655, 0 2px 8px #b8860b33",
                            "background": "rgba(255,255,255,0.18)",
                            "opacity": "0.97",
                            "transition": "transform 1.2s cubic-bezier(.4,2,.6,1)",
                        }
                    ),
                    rx.text(
                        """Ser una empresa líder sustentable de clase mundial en el sector industrial, energético, reconocida por su excelencia para generar valor y ofrecer soluciones innovadoras de calidad, a nuestros clientes y grupos de interés, siempre actuando con seguridad, responsabilidad y respeto del medio ambiente y calidad de vida.""",
                        style={
                            "color": rx.cond(theme.ThemeState.dark_mode, "#ffe066", "#333"),
                            "margin_bottom": "2rem",
                            "text_align": "justify",
                            "margin_top": "1.5rem",
                            "padding": "1.1rem",
                            "border_radius": "14px",
                            "font_size": "1.08rem",
                            "box_shadow": "0 2px 16px #ffe06633",
                        },
                    ),
                    style={
                        "text_align": "center",
                        "padding": "2.2rem 1.5rem 1.7rem 1.5rem",
                        "box_shadow": rx.cond(
                            theme.ThemeState.dark_mode,
                            "0 0 48px 12px #222",
                            "0 0 48px 12px #ffe06655"
                        ),
                        "border": "2px solid #ffe066",
                        "border_radius": "28px",
                        "width": "40%",
                        "background": rx.cond(
                            theme.ThemeState.dark_mode,
                            "rgba(34,34,34,0.72)",
                            "rgba(255,255,255,0.72)"
                        ),
                        "backdrop_filter": "blur(4px)",
                        "transition": "box-shadow 0.3s, background 0.3s",
                    },
                ),
                rx.box(
                    rx.text(
                        "M I S I O N",
                        style={
                            "font_size": "1.7rem",
                            "font_weight": "bold",
                            "letter_spacing": "0.5rem",
                            "color": rx.cond(theme.ThemeState.dark_mode, "#ffe066", "#b8860b"),
                            "text_align": "center",
                            "margin_bottom": "0.9rem",
                            "text_shadow": "0 2px 12px #ffe066cc",
                        },
                    ),
                    rx.image(
                        src="/imagen2.jpg",
                        alt="Nuestra Misión",
                        class_name="about-img-anim",
                        style={
                            "width": "320px",
                            "height": "320px",
                            "object_fit": "cover",
                            "border_radius": "28px",
                            "margin": "0 auto 1.5rem auto",
                            "box_shadow": "0 8px 48px #ffe06655, 0 2px 8px #b8860b33",
                            "background": "rgba(255,255,255,0.18)",
                            "opacity": "0.97",
                            "transition": "transform 1.2s cubic-bezier(.4,2,.6,1)",
                        }
                    ),
                    rx.text(
                        """Satisfacer las necesidades de nuestros clientes, compañías, concesionarios, distribuidores, accionistas, trabajadores y suplidores, a través de nuestros productos y de la gestión de nuestros negocios, garantizando los más altos estándares de calidad, seguridad, excelente calidad de vida, protección ambiental, eficiencia y competitividad, con la mejor relación precio/valor, alta rentabilidad y crecimiento sostenido.""",
                        style={
                            "color": rx.cond(theme.ThemeState.dark_mode, "#ffe066", "#333"),
                            "margin_bottom": "2rem",
                            "text_align": "justify",
                            "margin_top": "1.5rem",
                            "padding": "1.1rem",
                            "border_radius": "14px",
                            "font_size": "1.08rem",
                            "box_shadow": "0 2px 16px #ffe06633",
                            
                        },
                    ),
                    style={
                        "text_align": "center",
                        "padding": "2.2rem 1.5rem 1.7rem 1.5rem",
                        "box_shadow": rx.cond(
                            theme.ThemeState.dark_mode,
                            "0 0 48px 12px #222",
                            "0 0 48px 12px #ffe06655"
                        ),
                        "border": "2px solid #ffe066",
                        "border_radius": "28px",
                        "width": "40%",
                        "background": rx.cond(
                            theme.ThemeState.dark_mode,
                            "rgba(34,34,34,0.72)",
                            "rgba(255,255,255,0.72)"
                        ),
                        "backdrop_filter": "blur(4px)",
                        "transition": "box-shadow 0.3s, background 0.3s",
                    },
                ),
                justify="center",
                spacing="6",
            ),
            style={
                "padding": "2.5rem 1rem 2.5rem 1rem",
                "background": "linear-gradient(120deg, #ffe066 0%, #ffd700 50%, #b8860b 100%)",
                "background_repeat": "no-repeat",
                "background_size": "cover",
                "background_position": "center",
                "background_color": rx.cond(theme.ThemeState.dark_mode, "#181818", "#fff"),
                "border_radius": "18px 18px 0 0",
                "box_shadow": rx.cond(
                    theme.ThemeState.dark_mode,
                    "0px 4px 12px #222",
                    "0px 4px 6px rgba(0, 0, 0, 0.1)"
                ),
                "width": "100%",
                "transition": "background 0.3s, box-shadow 0.3s"
            },
        ),
        rx.html(
            """
            <div style="width:100%;overflow:hidden;line-height:0;">
              <svg viewBox="0 0 1200 100" width="100%" height="100" preserveAspectRatio="none" style="display:block;">
                <defs>
                  <linearGradient id="aboutToServicios" x1="0" y1="0" x2="1" y2="1">
                    <stop offset="0%" stop-color="#ffe066" />
                    <stop offset="60%" stop-color="#ffd700" />
                    <stop offset="100%" stop-color="#b8860b" />
                  </linearGradient>
                </defs>
                <path d="M0,80 Q600,0 1200,80 L1200,100 L0,100 Z" fill="url(#aboutToServicios)"/>
              </svg>
            </div>
            <style>
            .about-img-anim {
                transition: transform 1.5s cubic-bezier(.4,2,.6,1);
            }
            .about-img-anim:hover {
                transform: scale(1.12) rotate(-2deg);
                box-shadow: 0 12px 64px #ffe066cc, 0 4px 16px #b8860b33;
            }
            </style>
            """
        ),
    )