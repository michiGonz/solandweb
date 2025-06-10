import reflex as rx
from .state import State  # Ajusta la ruta según tu estructura

def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(rx.text(question), text_align="right"),
        rx.box(rx.text(answer), text_align="left"),
        margin_y="1em",
    )

def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )

def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=State.question,
            placeholder="Escribe tu pregunta...",
            on_change=State.set_question,
        ),
        rx.button(
            "Enviar",
            on_click=State.answer,
        ),
    )

def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            chat(),
            action_bar(),
            align="center",
        )
    )

app = rx.App()
app.add_page(index)