import reflex as rx

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
    ing_informatica_item = sidebar_menu_item("ING. EN INFORMÁTICA", "laptop", ing_informatica_options)

    ing_electronica_options = [
        {"text": "PROYECTOS DE ELECTRÓNICA", "href": "/#PROYECTOS"},
        {"text": "MATERIAS DE SEMESTRE", "href": "/#SEMESTRES"},
        {"text": "NOTICIAS/MEMES DE ELECTRÓNICA", "href": "/#MEMES DE ELECTRÓNICA"},
    ]
    ing_electronica_item = sidebar_menu_item("ING. EN ELECTRÓNICA", "circuit-board", ing_electronica_options)

    ing_mecatronica_options = [
        {"text": "PROYECTOS DE MECATRÓNICA", "href": "/#PROYECTOS"},
        {"text": "MATERIAS DE SEMESTRE", "href": "/#SEMESTRES"},
        {"text": "NOTICIAS/MEMES DE MECATRÓNICA", "href": "/#MEMES DE MECATRÓNICA"},
    ]
    ing_mecatronica_item = sidebar_menu_item("ING. EN MECATRÓNICA", "bot", ing_mecatronica_options)

    lic_informatica_aplicada_options = [
        {"text": "PROYECTOS DE INFORMÁTICA APLICADA", "href": "/#PROYECTOS"},
        {"text": "MATERIAS DE SEMESTRE", "href": "/#SEMESTRES"},
        {"text": "NOTICIAS/MEMES DE INFORMÁTICA APLICADA", "href": "/#MEMES DE INFORMÁTICA APLICADA"},
    ]
    lic_informatica_aplicada_item = sidebar_menu_item("LIC. EN INFO. APLICADA", "book", lic_informatica_aplicada_options)

    lic_gerencia_comercio_elec_options = [
        {"text": "PROYECTOS DE COMERCIO ELECTRÓNICO", "href": "/#PROYECTOS"},
        {"text": "MATERIAS DE SEMESTRE", "href": "/#SEMESTRES"},
        {"text": "NOTICIAS/MEMES DE COMERCIO ELECTRÓNICO", "href": "/#MEMES DE COMERCIO ELECTRÓNICO"},
    ]
    lic_gerencia_comercio_elec_item = sidebar_menu_item("LIC. EN GER. COMERCIO ELEC.", "candlestick-chart", lic_gerencia_comercio_elec_options)

    lic_en_Ciencia_de_datos_options = [
        {"text": "PROYECTOS DE CIENCIA DE DATOS", "href": "/#PROYECTOS"},
        {"text": "MATERIAS DE SEMESTRE", "href": "/#SEMESTRES"},
        {"text": "NOTICIAS/MEMES DE CIENCIA DE DATOS", "href": "/#MEMES DE COMERCIO ELECTRÓNICO"},

    ]

    lic_en_ciencia_de_datos_item = sidebar_menu_item("LIC. EN CIENCIA DE DATOS", "database",lic_en_Ciencia_de_datos_options)

    lic_en_seg_informatica_options = [
        {"text": "PROYECTOS DE SEGURIDAD INFORMÁTICA", "href": "/#PROYECTOS"},
        {"text": "MATERIAS DE SEMESTRE", "href": "/#SEMESTRES"},
        {"text": "NOTICIAS/MEMES DE SEGURIDAD INFORMÁTICA", "href": "/#MEMES DE COMERCIO ELECTRÓNICO"},

    ]

    lic_en_seg_informatica_item = sidebar_menu_item("TEC. EN SEGURIDAD INFORMÁTICA", "qr-code",lic_en_seg_informatica_options)

    return rx.vstack(
        ing_informatica_item,
        ing_electronica_item,
        ing_mecatronica_item,
        lic_informatica_aplicada_item,
        lic_gerencia_comercio_elec_item,
        lic_en_ciencia_de_datos_item,
        lic_en_seg_informatica_item,
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
