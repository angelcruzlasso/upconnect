import reflex as rx

class State_imag(rx.State):
    """The app state."""
    img: list[str] = []

    async def handle_upload(self, files: list[rx.UploadFile]):
        """Handle the upload of file(s).

        Args:
            files: The uploaded files.
        """
        for file in files:
            upload_data = await file.read()
            outfile = rx.get_upload_dir() / file.filename

            # Save the file.
            with outfile.open("wb") as file_object:
                file_object.write(upload_data)

            # Update the img var.
            self.img.append(file.filename)

color = "rgb(107,99,246)"

def tab_component() -> rx.Component:
    return rx.tabs.root(
        rx.tabs.list(
            rx.tabs.trigger("Foros Recientes", value="tab1", style={"font-size": "1.5rem"}),
            rx.tabs.trigger("Destacados", value="tab2", style={"font-size": "1.5rem"}),
        ),
        rx.tabs.content(
            rx.hstack(
                rx.vstack(
                    rx.upload(
                        rx.text("Arrastre y suelte archivos aquí o haga clic para seleccionar archivos"),
                        id="file_upload",
                        border="1px dotted rgb(107,99,246)",
                        padding="5em",
                    ),
                    rx.button(
                        "Subir Archivos",
                        on_click=State_imag.handle_upload(rx.upload_files(upload_id="file_upload")),
                    ),
                ),
                rx.vstack(
                    rx.upload(
                        rx.text("Arrastre y suelte imágenes aquí o haga clic para seleccionar imágenes"),
                        id="image_upload",
                        border="1px dotted rgb(107,99,246)",
                        padding="5em",
                    ),
                    rx.button(
                        "Subir Imagenes",
                        on_click=State_imag.handle_upload(rx.upload_files(upload_id="image_upload")),
                    ),
                    rx.foreach(State_imag.img, lambda img: rx.image(src=rx.get_upload_url(img))),
                ),
                spacing="2"
            ),
            value="tab2",
            padding="1em",
        ),
        padding="1em",
        width="100%",
    )
