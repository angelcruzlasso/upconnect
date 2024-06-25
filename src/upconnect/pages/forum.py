import reflex as rx
from rxconfig import config

class Estado(rx.State):
    """El estado de la aplicación."""
    ...

class EditorState(rx.State):
    content: str = "<p>Editor content</p>"

    def handle_change(self, content: str):
        """Handle the editor value change."""
        self.content = content

def editor_example():
    return rx.vstack(
        rx.editor(
            set_contents=EditorState.content,
            on_change=EditorState.handle_change,
            style={"font-size": "20px"},
        ),
        rx.box(
            rx.html(EditorState.content),
            border="1px dashed #ccc",
            border_radius="4px",
            width="100%",
            style={"font-size": "20px"},
        ),
    )

def sidebar_item(text: str, icon: str, href: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text(text, size="4"),
            width="100%",
            padding_x="0.5rem",
            padding_y="0.75rem",
            align="center",
            style={
                "_hover": {
                    "bg": rx.color("accent", 4),
                    "color": rx.color("accent", 11),
                    "box-shadow": "0px 0px 10px rgba(0, 0, 0, 0.1)"
                },
                "_active": {
                    "bg": rx.color("accent", 6),
                    "color": rx.color("accent", 10),
                },
                "border-radius": "0.5em",
                "border": "none",
                "box-shadow": "none",
                "background-color": "transparent"
            },
        ),
        href=href,
        underline="none",
        weight="medium",
        width="100%",
        style={
            "border": "none",
            "box-shadow": "none",
        }
    )

def sidebar_menu_item(text: str, icon: str, options: list) -> rx.Component:
    return rx.menu.root(
        rx.menu.trigger(
            rx.button(
                rx.hstack(
                    rx.icon(icon),
                    rx.text(text, size="4"),
                    width="100%",
                    padding_x="0.5rem",
                    padding_y="0.75rem",
                    align="center",
                    style={
                        "_hover": {
                            "bg": rx.color("accent", 4),
                            "color": rx.color("accent", 11),
                            "box-shadow": "0px 0px 10px rgba(0, 0, 0, 0.1)"
                        },
                        "_active": {
                            "bg": rx.color("accent", 6),
                            "color": rx.color("accent", 10),
                        },
                        "border": "none",
                        "box-shadow": "none",
                        "background-color": "transparent"
                    },
                ),
                variant="soft",
                width="100%",
                style={
                    "border": "none",
                    "box-shadow": "none",
                    "background-color": "transparent"
                }
            ),
        ),
        rx.menu.content(
            *[rx.menu.item(opt["text"], href=opt["href"]) for opt in options]
        ),
    )

def sidebar_items() -> rx.Component:
    ing_informatica_options = [
        {"text": "PROYECTOS DE INFORMÁTICA", "href": "/#PROYECTOS"},
        {"text": "MATERIAS DE SEMESTRE", "href": "/#SEMESTRES"},
        {"text": "CHISME/MEMES DE INFORMÁTICA", "href": "/#MEMES DE PROGRAMACIÓN"},
    ]
    ing_informatica_item = sidebar_menu_item("ING. EN INFORMÁTICA", "layout-dashboard", ing_informatica_options)

    ing_electronica_options = [
        {"text": "PROYECTOS DE ELECTRÓNICA", "href": "/#PROYECTOS"},
        {"text": "MATERIAS DE SEMESTRE", "href": "/#SEMESTRES"},
        {"text": "NOTICIAS/MEMES DE ELECTRÓNICA", "href": "/#MEMES DE ELECTRÓNICA"},
    ]
    ing_electronica_item = sidebar_menu_item("ING. EN ELECTRÓNICA", "square-library", ing_electronica_options)

    ing_mecatronica_options = [
        {"text": "PROYECTOS DE MECATRÓNICA", "href": "/#PROYECTOS"},
        {"text": "MATERIAS DE SEMESTRE", "href": "/#SEMESTRES"},
        {"text": "NOTICIAS/MEMES DE MECATRÓNICA", "href": "/#MEMES DE MECATRÓNICA"},
    ]
    ing_mecatronica_item = sidebar_menu_item("ING. EN MECATRÓNICA", "bar-chart-4", ing_mecatronica_options)

    lic_informatica_aplicada_options = [
        {"text": "PROYECTOS DE INFORMÁTICA APLICADA", "href": "/#PROYECTOS"},
        {"text": "MATERIAS DE SEMESTRE", "href": "/#SEMESTRES"},
        {"text": "NOTICIAS/MEMES DE INFORMÁTICA APLICADA", "href": "/#MEMES DE INFORMÁTICA APLICADA"},
    ]
    lic_informatica_aplicada_item = sidebar_menu_item("LIC. EN INFO. APLICADA", "layout-dashboard", lic_informatica_aplicada_options)

    lic_gerencia_comercio_elec_options = [
        {"text": "PROYECTOS DE COMERCIO ELECTRÓNICO", "href": "/#PROYECTOS"},
        {"text": "MATERIAS DE SEMESTRE", "href": "/#SEMESTRES"},
        {"text": "NOTICIAS/MEMES DE COMERCIO ELECTRÓNICO", "href": "/#MEMES DE COMERCIO ELECTRÓNICO"},
    ]
    lic_gerencia_comercio_elec_item = sidebar_menu_item("LIC. EN GER. COMERCIO ELEC.", "square-library", lic_gerencia_comercio_elec_options)

    return rx.vstack(
        ing_informatica_item,
        ing_electronica_item,
        ing_mecatronica_item,
        lic_informatica_aplicada_item,
        lic_gerencia_comercio_elec_item,
        spacing="6",
        width="100%",
    )

def sidebar_bottom_profile() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading("UPCONNECT", size="7", weight="bold"),
                    align="center",
                    justify="start",
                    padding_x="0.5rem",
                    width="100%",
                ),
                sidebar_items(),
                rx.spacer(),
                rx.vstack(
                    rx.vstack(
                        sidebar_item("Ajustes", "settings", "/#"),
                        sidebar_item("Cerrar sesión", "log-out", "/#"),
                        spacing="1",
                        width="100%",
                    ),
                    rx.divider(),
                    rx.hstack(
                        rx.icon_button(
                            rx.icon("user"),
                            size="3",
                            radius="full",
                        ),
                        rx.vstack(
                            rx.box(
                                rx.text("Mi cuenta", size="3", weight="bold"),
                                rx.text("usuario-c.usuario-a@up.ac.pa", size="2", weight="medium"),
                                width="100%",
                            ),
                            spacing="0",
                            align="start",
                            justify="start",
                            width="100%",
                        ),
                        padding_x="0.5rem",
                        align="center",
                        justify="start",
                        width="100%",
                    ),
                    width="100%",
                    spacing="5",
                ),
                spacing="5",
                padding_x="1em",
                padding_y="1.5em",
                bg=rx.color("accent", 3),
                align="start",
                height="100vh",
                width="20em",
                position="fixed",
                left="0px",
                top="0px",
                z_index="5",
            ),
        ),
        rx.mobile_and_tablet(
            rx.drawer.root(
                rx.drawer.trigger(
                    rx.icon("align-justify", size=30)
                ),
                rx.drawer.overlay(z_index="5"),
                rx.drawer.portal(
                    rx.drawer.content(
                        rx.vstack(
                            rx.box(
                                rx.drawer.close(
                                    rx.icon("x", size=30)
                                ),
                                width="100%",
                            ),
                            sidebar_items(),
                            rx.spacer(),
                            rx.vstack(
                                rx.vstack(
                                    sidebar_item("Ajustes", "settings", "/#"),
                                    sidebar_item("Cerrar sesión", "log-out", "/#"),
                                    width="100%",
                                    spacing="1",
                                ),
                                rx.divider(margin="0"),
                                rx.hstack(
                                    rx.icon_button(
                                        rx.icon("user"),
                                        size="3",
                                        radius="full",
                                    ),
                                    rx.vstack(
                                        rx.box(
                                            rx.text("Mi cuenta", size="3", weight="bold"),
                                            rx.text("usuario-c.usuario-a@up.ac.pa", size="2", weight="medium"),
                                            width="100%",
                                        ),
                                        spacing="0",
                                        justify="start",
                                        width="100%",
                                    ),
                                    padding_x="0.5rem",
                                    align="center",
                                    justify="start",
                                    width="100%",
                                ),
                                width="100%",
                                spacing="5",
                            ),
                            spacing="5",
                            width="100%",
                        ),
                        top="auto",
                        right="auto",
                        height="100%",
                        width="20em",
                        padding="1.5em",
                        bg=rx.color("accent", 2),
                    ),
                    width="100%",
                ),
                direction="left",
            ),
            padding="1em",
        ),
    )

def navbar_searchbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.input(
                    rx.input.slot(rx.icon("search")),
                    placeholder="Buscar...",
                    type="search",
                    size="3",
                    width="50em",
                    margin_left="20em",
                ),
                rx.spacer(),
                align_items="center",
                width="100%",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.image(
                    src="/logo.jpg",
                    width="3em",
                    height="auto",
                    border_radius="25%",
                ),
                rx.heading("UPCONNECT", size="6", weight="bold"),
                rx.input(
                    rx.input.slot(rx.icon("search")),
                    placeholder="Buscar...",
                    type="search",
                    size="2",
                    width="100%",
                    margin_left="1em"
                ),
                rx.spacer(),
                align_items="center",
                width="100%",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        position="fixed",
        top="0px",
        z_index="5",
        width="100%",
    )

def tab_component() -> rx.Component:
    return rx.tabs.root(
        rx.tabs.list(
            rx.tabs.trigger("Foros Recientes", value="tab1", style={"font-size": "1.5rem"}),
            rx.tabs.trigger("Destacados", value="tab2", style={"font-size": "1.5rem"}),
        ),
        rx.tabs.content(
            rx.text("Contenido de Foros Recientes", size="5", weight="medium"),
            value="tab1",
            padding="1em",
        ),
        rx.tabs.content(
            rx.text("Contenido de Destacados", size="5", weight="medium"),
            value="tab2",
            padding="1em",
        ),
        padding="1em",
        width="100%",
    )

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

app = rx.App()
app.add_page(pagina_principal, route="/")