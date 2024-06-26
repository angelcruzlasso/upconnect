import reflex as rx

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
