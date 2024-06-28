import reflex as rx
from rxconfig import config
from pages.login import register_page
from pages.login import login

class State(rx.State):
    """The app state."""
    ...
def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        #! Aqui empieza el vstack
        rx.vstack(  
            
        ),
    )
app = rx.App()
app.add_page(index)
# Configuración de la aplicación y rutas
app.add_page(login, "/")
app.add_page(register_page, "/register")