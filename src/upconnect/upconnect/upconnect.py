import reflex as rx
from rxconfig import config

class State(rx.State):
    """The app state."""
    ...
def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        #! Aqui empieza el vstack
        rx.vstack(
            rx.container(
                rx.text("Hello World"),
            ),
        ),
    )
app = rx.App()
app.add_page(index)


