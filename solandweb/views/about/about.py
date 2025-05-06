import reflex as rx

def about():
    return rx.box(
        rx.vstack(
            rx.center(
                rx.text(
                    "Solutions",
                    class_name="title",
                    style={
                        "font_weight": "bold",  # Negrita
                        "font_size": "3rem",  # Tamaño más grande
                        "color": "white",  # Color blanco
                        "text_align": "center",  # Centrar el texto
                        "text_transform": "uppercase",  # Texto en mayúsculas
                        "letter_spacing": "0.1em",  # Espaciado entre letras
                        "margin": "0.5rem 0",  # Margen superior e inferior
                        "padding": "0.5rem",  # Relleno interno
                    },
                ),
            ),
            rx.vstack(
                # Primera fila: Una columna a la izquierda y otra a la derecha
                rx.hstack(
                    rx.box(
                        rx.image(src='/imagen1.jpg', alt="Meet Us", width="100%", height="150px", border_radius="8px"),  # Imagen
                        rx.text("Meet Us", class_name="box-title"),
                        rx.text("Get to know our team and what drives us.", class_name="box-text"),
                        rx.center(  # Centrar el botón
                            rx.button("Read more", class_name="button"),
                        ),
                        class_name="about_box",
                        style={
                            "margin": "1rem",  # Margen interno pequeño
                            "width": "35%",  # Ocupa el 45% del ancho
                            "height": "300px",  # Altura fija para uniformidad
                            "text_align": "center",  # Centrar el contenido horizontalmente
                            "background_color": "white",  # Fondo blanco
                            "padding": "1rem",  # Relleno interno
                            "border_radius": "8px",  # Bordes redondeados
                            "box_shadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",  # Sombra ligera
                        },
                    ),
                    rx.box(
                        rx.image(src='/imagen1.jpg', alt="Contact Us", width="100%", height="150px", border_radius="8px"),  # Imagen
                        rx.text("Contact Us", class_name="box-title"),
                        rx.text("Get in touch with us for inquiries and collaborations.", class_name="box-text"),
                        rx.center(  # Centrar el botón
                            rx.button("Read more", class_name="button"),
                        ),
                        class_name="about_box",
                        style={
                            "margin": "1rem",  # Margen interno pequeño
                            "width": "35%",  # Ocupa el 45% del ancho
                            "height": "300px",  # Altura fija para uniformidad
                            "text_align": "center",  # Centrar el contenido horizontalmente
                            "background_color": "white",  # Fondo blanco
                            "padding": "1rem",  # Relleno interno
                            "border_radius": "8px",  # Bordes redondeados
                            "box_shadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",  # Sombra ligera
                        },
                    ),
                    justify="between",  # Separar las columnas
                    spacing="4",  # Espaciado entre las columnas
                    class_name="about_row",
                ),
                  # Primera fila: Una columna a la izquierda y otra a la derecha
                rx.hstack(
                    rx.box(
                        rx.image(src='/imagen1.jpg', alt="Meet Us", width="100%", height="150px", border_radius="8px"),  # Imagen
                        rx.text("Meet Us", class_name="box-title"),
                        rx.text("Get to know our team and what drives us.", class_name="box-text"),
                        rx.center(  # Centrar el botón
                            rx.button("Read more", class_name="button"),
                        ),
                        class_name="about_box",
                        style={
                            "margin": "1rem",  # Margen interno pequeño
                            "width": "35%",  # Ocupa el 45% del ancho
                            "height": "300px",  # Altura fija para uniformidad
                            "text_align": "center",  # Centrar el contenido horizontalmente
                            "background_color": "white",  # Fondo blanco
                            "padding": "1rem",  # Relleno interno
                            "border_radius": "8px",  # Bordes redondeados
                            "box_shadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",  # Sombra ligera
                        },
                    ),
                    rx.box(
                        rx.image(src='/imagen1.jpg', alt="Contact Us", width="100%", height="150px", border_radius="8px"),  # Imagen
                        rx.text("Contact Us", class_name="box-title"),
                        rx.text("Get in touch with us for inquiries and collaborations.", class_name="box-text"),
                        rx.center(  # Centrar el botón
                            rx.button("Read more", class_name="button"),
                        ),
                        class_name="about_box",
                        style={
                            "margin": "1rem",  # Margen interno pequeño
                            "width": "35%",  # Ocupa el 45% del ancho
                            "height": "300px",  # Altura fija para uniformidad
                            "text_align": "center",  # Centrar el contenido horizontalmente
                            "background_color": "white",  # Fondo blanco
                            "padding": "1rem",  # Relleno interno
                            "border_radius": "8px",  # Bordes redondeados
                            "box_shadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",  # Sombra ligera
                        },
                    ),
                    justify="between",  # Separar las columnas
                    spacing="4",  # Espaciado entre las columnas
                    class_name="about_row",
                ),
                
            ),
            id="sobre_mi",
            spacing="0",  # Eliminar el espacio entre el título y los contenedores,
            style={
                "background_image": "url('/about.jpg')",  # Imagen de fondo
                "padding": "2rem",  # Relleno interno del contenedor principal
                "width": "100%",  # Ocupa todo el ancho
            },
        )
    )