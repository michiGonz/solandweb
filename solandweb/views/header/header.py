import reflex as rx
import solandweb.styles.styles as styles
from solandweb.styles.styles import Size as Size
import solandweb.theme as theme
from solandweb.views.navbar.navbar import navbar  # Importa el navbar

def hero_section() -> rx.Component:
    """Hero section."""
    return rx.box(
        navbar(),
        rx.box(
            rx.vstack(
                rx.center(
                    rx.text(
                        "Servicios y Suministros Soland C.A",
                        class_name="title",
                        style={
                            "font_weight": "1000",
                            "font_size": "5rem",
                            "color": rx.cond(
                                theme.ThemeState.dark_mode,
                                "#ffe066",  # Mostaza en oscuro
                                "black"
                            ),
                            "text_align": "center",
                            "letter_spacing": "0.1em",
                            "padding": "0.5rem",
                            "display": "inline-block",
                            "text_shadow": (
                                "0 0 32px #fff,"
                                "0 0 64px #fff,"
                                "0 0 128px #fff,"
                                "0 0 256px #fff,"
                                "0 0 8px #ffe066,"
                                "0 0 16px #ffe066"
                            ),
                            "animation": "glow 2s ease-in-out infinite alternate",
                        },
                    ),
                    rx.html(
                        """
                        <style>
                        @keyframes glow {
                            0% {
                                text-shadow:
                                    0 0 32px #fff,
                                    0 0 64px #fff,
                                    0 0 128px #fff,
                                    0 0 256px #fff,
                                    0 0 8px #ffe066,
                                    0 0 16px #ffe066;
                            }
                            100% {
                                text-shadow:
                                    0 0 64px #fff,
                                    0 0 128px #fff,
                                    0 0 256px #fff,
                                    0 0 512px #fff,
                                    0 0 32px #ffe066,
                                    0 0 64px #ffe066;
                            }
                        }
                        </style>
                        """
                    ),
                ),
                rx.text(
                    "Somos una empresa venezolana con más de 21 años de experiencia en el área de ingeniería.",
                    size="4",
                    style={
                        "font_weight": "900",
                        "background_color": rx.cond(
                            theme.ThemeState.dark_mode,
                            "rgba(34,34,34,0.85)",  # Fondo oscuro translúcido
                            "rgba(255,255,255,0.75)"
                        ),
                        "padding": "1.1rem 2rem",
                        "border_radius": "18px",
                        "color": rx.cond(
                            theme.ThemeState.dark_mode,
                            "#ffe066",
                            "#222"
                        ),
                        "text_align": "center",
                        "margin": "1.5rem 0 2rem 0",
                        "display": "inline-block",
                        "box_shadow": rx.cond(
                            theme.ThemeState.dark_mode,
                            "0 4px 32px 0 #222, 0 2px 8px rgba(255,255,255,0.08)",
                            "0 4px 32px 0 #ffe066, 0 2px 8px rgba(0,0,0,0.08)"
                        ),
                        "font_size": "1.45rem",
                        "letter_spacing": "0.03em",
                        "transition": "box-shadow 0.3s",
                    },
                ),
                rx.button(
                    "Contáctanos",
                    href="#contacto",
                    style={
                        "background": rx.cond(
                            theme.ThemeState.dark_mode,
                            "linear-gradient(90deg, #222 60%, #333 100%)",
                            "linear-gradient(90deg, #ffe066 60%, #fffbe6 100%)"
                        ),
                        "color": rx.cond(
                            theme.ThemeState.dark_mode,
                            "#ffe066",
                            "#222"
                        ),
                        "font_weight": "bold",
                        "padding": "1rem 2.2rem",
                        "border_radius": "12px",
                        "border": "none",
                        "box_shadow": rx.cond(
                            theme.ThemeState.dark_mode,
                            "0 0 24px 4px #222, 0 2px 8px rgba(255,255,255,0.10)",
                            "0 0 24px 4px #ffe066, 0 2px 8px rgba(0,0,0,0.10)"
                        ),
                        "font_size": "1.25rem",
                        "cursor": "pointer",
                        "margin_top": "0.7rem",
                        "letter_spacing": "0.04em",
                        "transition": "background 0.3s, box-shadow 0.3s, transform 0.2s",
                    },
                    _hover={
                        "background": rx.cond(
                            theme.ThemeState.dark_mode,
                            "linear-gradient(90deg, #333 0%, #222 100%)",
                            "linear-gradient(90deg, #fffbe6 0%, #ffe066 100%)"
                        ),
                        "box_shadow": rx.cond(
                            theme.ThemeState.dark_mode,
                            "0 0 48px 8px #ffe066, 0 4px 16px #222",
                            "0 0 48px 8px #ffe066, 0 4px 16px rgba(0,0,0,0.13)"
                        ),
                        "transform": "scale(1.04)",
                    },
                ),
                spacing="2",
                align_items="center",
            ),
            style={
                **styles.HERO_STYLE,
                "margin": "0",
                "padding": "0",
                "width": "100%",
                "margin_top": "60px",
                "background_color": rx.cond(
                    theme.ThemeState.dark_mode,
                    "#181818",
                    "#fff"
                ),
                "transition": "background-color 0.3s",
            },
            id="inicio",
        ),
    )

def about_section() -> rx.Component:
    """About section."""
    return rx.box(
        rx.text(
            "What we have to offer for your next business and career success",
            class_name="about-title",
            style={
                "color": rx.cond(
                    theme.ThemeState.dark_mode,
                    "#ffe066",
                    "#222"
                )
            }
        ),
        rx.text(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis aute irure dolor in reprehenderit.",
            class_name="about-subtitle",
            style={
                "color": rx.cond(
                    theme.ThemeState.dark_mode,
                    "#fff",
                    "#444"
                )
            }
        ),
        rx.grid(
            # Primera fila
            rx.box(
                rx.image(src="/imagen1.jpg", class_name="about-image"),
                rx.text("Green building", class_name="about-box-title", style={
                    "color": rx.cond(theme.ThemeState.dark_mode, "#ffe066", "#222"),
                    "font_weight": "bold"
                }),
                rx.text(
                    "Interdum iusto pulvinar consequuntur augue optio, repellat fuga! Purus expedita fusce temporibus eso.",
                    class_name="about_box_text",
                    style={"color": rx.cond(theme.ThemeState.dark_mode, "#fff", "#222")}
                ),
                rx.button(
                    "Take a look",
                    class_name="about-button",
                    style={
                        "background_color": rx.cond(theme.ThemeState.dark_mode, "#222", "#ffe066"),
                        "color": rx.cond(theme.ThemeState.dark_mode, "#ffe066", "#222"),
                        "font_weight": "bold",
                        "border_radius": "8px",
                        "box_shadow": rx.cond(theme.ThemeState.dark_mode, "0 2px 8px #ffe066", "0 2px 8px #ffe066"),
                        "transition": "background 0.3s, color 0.3s"
                    }
                ),
                class_name="about-box",
                style={
                    "background_color": rx.cond(theme.ThemeState.dark_mode, "#232323", "#fff"),
                    "box_shadow": rx.cond(theme.ThemeState.dark_mode, "0 2px 16px #222", "0 2px 16px #ffe066"),
                    "border_radius": "16px",
                    "padding": "1.5rem",
                    "transition": "background 0.3s, box-shadow 0.3s"
                }
            ),
            # Puedes repetir el mismo patrón para las demás cajas...
            # Segunda caja
            rx.box(
                rx.image(src="/imagen1.jpg", class_name="about-image"),
                rx.text("Interior design", class_name="about-box-title", style={
                    "color": rx.cond(theme.ThemeState.dark_mode, "#ffe066", "#222"),
                    "font_weight": "bold"
                }),
                rx.text(
                    "Interdum iusto pulvinar consequuntur augue optio, repellat fuga! Purus expedita fusce temporibus eso.",
                    class_name="about-box-text",
                    style={"color": rx.cond(theme.ThemeState.dark_mode, "#fff", "#222")}
                ),
                rx.button(
                    "Take a look",
                    class_name="about-button",
                    style={
                        "background_color": rx.cond(theme.ThemeState.dark_mode, "#222", "#ffe066"),
                        "color": rx.cond(theme.ThemeState.dark_mode, "#ffe066", "#222"),
                        "font_weight": "bold",
                        "border_radius": "8px",
                        "box_shadow": rx.cond(theme.ThemeState.dark_mode, "0 2px 8px #ffe066", "0 2px 8px #ffe066"),
                        "transition": "background 0.3s, color 0.3s"
                    }
                ),
                class_name="about-box",
                style={
                    "background_color": rx.cond(theme.ThemeState.dark_mode, "#232323", "#fff"),
                    "box_shadow": rx.cond(theme.ThemeState.dark_mode, "0 2px 16px #222", "0 2px 16px #ffe066"),
                    "border_radius": "16px",
                    "padding": "1.5rem",
                    "transition": "background 0.3s, box-shadow 0.3s"
                }
            ),
            # Tercera caja
            rx.box(
                rx.image(src="/imagen1.jpg", class_name="about-image"),
                rx.text("Expert team", class_name="about-box-title", style={
                    "color": rx.cond(theme.ThemeState.dark_mode, "#ffe066", "#222"),
                    "font_weight": "bold"
                }),
                rx.text(
                    "Interdum iusto pulvinar consequuntur augue optio, repellat fuga! Purus expedita fusce temporibus eso.",
                    class_name="about-box-text",
                    style={"color": rx.cond(theme.ThemeState.dark_mode, "#fff", "#222")}
                ),
                rx.button(
                    "Take a look",
                    class_name="about-button",
                    style={
                        "background_color": rx.cond(theme.ThemeState.dark_mode, "#222", "#ffe066"),
                        "color": rx.cond(theme.ThemeState.dark_mode, "#ffe066", "#222"),
                        "font_weight": "bold",
                        "border_radius": "8px",
                        "box_shadow": rx.cond(theme.ThemeState.dark_mode, "0 2px 8px #ffe066", "0 2px 8px #ffe066"),
                        "transition": "background 0.3s, color 0.3s"
                    }
                ),
                class_name="about-box",
                style={
                    "background_color": rx.cond(theme.ThemeState.dark_mode, "#232323", "#fff"),
                    "box_shadow": rx.cond(theme.ThemeState.dark_mode, "0 2px 16px #222", "0 2px 16px #ffe066"),
                    "border_radius": "16px",
                    "padding": "1.5rem",
                    "transition": "background 0.3s, box-shadow 0.3s"
                }
            ),
            # Cuarta caja
            rx.box(
                rx.image(src="/imagen1.jpg", class_name="about-image"),
                rx.text("Family plans", class_name="about-box-title", style={
                    "color": rx.cond(theme.ThemeState.dark_mode, "#ffe066", "#222"),
                    "font_weight": "bold"
                }),
                rx.text(
                    "Interdum iusto pulvinar consequuntur augue optio, repellat fuga! Purus expedita fusce temporibus eso.",
                    class_name="about-box-text",
                    style={"color": rx.cond(theme.ThemeState.dark_mode, "#fff", "#222")}
                ),
                rx.button(
                    "Take a look",
                    class_name="about-button",
                    style={
                        "background_color": rx.cond(theme.ThemeState.dark_mode, "#222", "#ffe066"),
                        "color": rx.cond(theme.ThemeState.dark_mode, "#ffe066", "#222"),
                        "font_weight": "bold",
                        "border_radius": "8px",
                        "box_shadow": rx.cond(theme.ThemeState.dark_mode, "0 2px 8px #ffe066", "0 2px 8px #ffe066"),
                        "transition": "background 0.3s, color 0.3s"
                    }
                ),
                class_name="about-box",
                style={
                    "background_color": rx.cond(theme.ThemeState.dark_mode, "#232323", "#fff"),
                    "box_shadow": rx.cond(theme.ThemeState.dark_mode, "0 2px 16px #222", "0 2px 16px #ffe066"),
                    "border_radius": "16px",
                    "padding": "1.5rem",
                    "transition": "background 0.3s, box-shadow 0.3s"
                }
            ),
            template_columns="repeat(2, 1fr)",
            gap="2rem",
            class_name="about-grid",
            style={
                "background_color": rx.cond(theme.ThemeState.dark_mode, "#181818", "#fff"),
                "padding": "2rem",
                "border_radius": "20px",
                "transition": "background 0.3s"
            }
        ),
        id="about",
        class_name="about-section",
        style={
            "background_color": rx.cond(theme.ThemeState.dark_mode, "#181818", "#fff"),
            "transition": "background 0.3s"
        }
    )

def contact_section() -> rx.Component:
    """Contact section."""
    return rx.box(
        rx.vstack(
            rx.heading("Contáctanos", size="4", style={
                "color": rx.cond(theme.ThemeState.dark_mode, "#ffe066", "#222")
            }),
            rx.form(
                rx.input(
                    placeholder="Tu nombre",
                    name="nombre",
                    required=True,
                    style={
                        "background_color": rx.cond(theme.ThemeState.dark_mode, "#232323", "#fff"),
                        "color": rx.cond(theme.ThemeState.dark_mode, "#ffe066", "#222"),
                        "border": rx.cond(theme.ThemeState.dark_mode, "1px solid #ffe066", "1px solid #ccc"),
                        "margin_bottom": "1rem",
                        "padding": "0.7rem",
                        "border_radius": "8px"
                    }
                ),
                rx.input(
                    placeholder="Tu correo",
                    type="email",
                    name="email",
                    required=True,
                    style={
                        "background_color": rx.cond(theme.ThemeState.dark_mode, "#232323", "#fff"),
                        "color": rx.cond(theme.ThemeState.dark_mode, "#ffe066", "#222"),
                        "border": rx.cond(theme.ThemeState.dark_mode, "1px solid #ffe066", "1px solid #ccc"),
                        "margin_bottom": "1rem",
                        "padding": "0.7rem",
                        "border_radius": "8px"
                    }
                ),
                rx.text_area(
                    placeholder="Tu mensaje",
                    name="mensaje",
                    required=True,
                    style={
                        "background_color": rx.cond(theme.ThemeState.dark_mode, "#232323", "#fff"),
                        "color": rx.cond(theme.ThemeState.dark_mode, "#ffe066", "#222"),
                        "border": rx.cond(theme.ThemeState.dark_mode, "1px solid #ffe066", "1px solid #ccc"),
                        "margin_bottom": "1rem",
                        "padding": "0.7rem",
                        "border_radius": "8px"
                    }
                ),
                rx.button(
                    "Enviar",
                    type="submit",
                    style={
                        "background_color": rx.cond(theme.ThemeState.dark_mode, "#ffe066", "#222"),
                        "color": rx.cond(theme.ThemeState.dark_mode, "#222", "#ffe066"),
                        "font_weight": "bold",
                        "border_radius": "8px",
                        "padding": "0.7rem 1.5rem",
                        "border": "none",
                        "cursor": "pointer",
                        "transition": "background 0.3s, color 0.3s"
                    },
                    _hover={
                        "background_color": rx.cond(theme.ThemeState.dark_mode, "#fffbe6", "#ffe066"),
                        "color": rx.cond(theme.ThemeState.dark_mode, "#222", "#222"),
                    }
                ),
                spacing="1",
            ),
            spacing="2",
        ),
        style={
            **styles.CONTACT_STYLE,
            "background_color": rx.cond(theme.ThemeState.dark_mode, "#181818", "#fff"),
            "border_radius": "20px",
            "transition": "background 0.3s"
        }
    )

def map_section() -> rx.Component:
    """Map section."""
    return rx.box(
        rx.html(
            '<iframe src="https://www.google.com/maps/embed?..." width="100%" height="400" style="border:0;" allowfullscreen="" loading="lazy"></iframe>'
        ),
        style={
            "margin": "2rem 0",
            "background_color": rx.cond(theme.ThemeState.dark_mode, "#181818", "#fff"),
            "border_radius": "20px",
            "transition": "background 0.3s"
        },
    )

def footer() -> rx.Component:
    """Footer section."""
    return rx.box(
        rx.text(
            "© 2025 MiWeb. Todos los derechos reservados.",
            text_align="center",
            style={
                "color": rx.cond(theme.ThemeState.dark_mode, "#ffe066", "#222")
            }
        ),
        style={
            **styles.FOOTER_STYLE,
            "background_color": rx.cond(theme.ThemeState.dark_mode, "#181818", "#fff"),
            "transition": "background 0.3s"
        }
    )