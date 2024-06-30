import reflex as rx
from .editor import editor_example
from .sidebar import sidebar_bottom_profile
from .navbar import navbar_searchbar
from .tabs import tab_component

def pagina_principal() -> rx.Component:
    return rx.box(
        navbar_searchbar(),
        rx.color_mode.button(position="top-right"),
        rx.box(
            sidebar_bottom_profile(),
            tab_component(),
            editor_example(),
            padding_top="4em",
            padding_left=["0", "20em"],
            height="100vh",
            width="100%",
            bg=rx.color("gray", 1),
            align="start",
        ),
    )
