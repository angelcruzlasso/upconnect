import reflex as rx
from rxconfig import config
from pages.forum import pagina_principal

class State(rx.State):
    """The app state."""
    pass

def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.text("klk mi loco bienvenido seas al lado oscuro del mundo"),
            rx.button("Pulse aqui pa irte pa allá xd", on_click=lambda: rx.redirect("/pagina_principal")),
        ),
    )

app = rx.App()
app.add_page(index, route="/")
app.add_page(pagina_principal, route="/pagina_principal")