import reflex as rx

class StateImag(rx.State):
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
            rx.vstack(
                rx.box(
                    rx.text("@usuario_50", font_weight="bold"),
                    rx.text("Pregunta: ¿Qué herramientas recomiendan para depurar programas en C?", font_weight="bold"),
                    rx.text("@usuario_3", font_weight="bold"),
                    rx.text("Respuesta: En C, herramientas como gdb (GNU Debugger) son ampliamente utilizadas para depuración. También se pueden emplear IDEs como Visual Studio Code con extensiones para C/C++."),
                    padding="1em",
                    border="1px solid gray",
                    border_radius="8px",
                    margin_bottom="1em",
                    style={"margin-left": "-25px"},  # Mueve el box a la izquierda
                ),
                rx.box(
                    rx.text("@usuario_6", font_weight="bold"),
                    rx.text("Pregunta: ¿Cuál es la característica principal de C++ que lo diferencia de C?", font_weight="bold"),
                    rx.text("@usuario_1", font_weight="bold"),
                    rx.text("Respuesta: C++ es un lenguaje orientado a objetos que ofrece características adicionales como clases, herencia, polimorfismo y plantillas, que no están presentes en C de forma nativa."),
                    rx.text("@usuario_1", font_weight="bold"),
                    rx.text("Respuesta: Además, C++ incluye una biblioteca estándar rica que facilita muchas tareas de programación."),
                    padding="1em",
                    border="1px solid gray",
                    border_radius="8px",
                    margin_bottom="1em",
                    style={"margin-left": "-25px"},
                ),
                rx.box(
                    rx.text("@usuario_4", font_weight="bold"),
                    rx.text("Pregunta: ¿Cómo puedo optimizar el renderizado de mis componentes en React?", font_weight="bold"),
                    rx.text("@usuario_44", font_weight="bold"),
                    rx.text("Respuesta: Puedes usar React.memo para componentes funcionales o PureComponent para componentes de clase para optimizar el renderizado."),
                    rx.text("@usuario_33", font_weight="bold"),
                    rx.text("Respuesta: Además, evita renderizaciones innecesarias mediante la separación de componentes y el uso adecuado del estado."),
                    padding="1em",
                    border="1px solid gray",
                    border_radius="8px",
                    margin_bottom="1em",
                    style={"margin-left": "-25px"},
                ),
                rx.box(
                    rx.text("@usuario_9", font_weight="bold"),
                    rx.text("Pregunta: ¿Cuál es la mejor forma de manejar la autenticación en Django?", font_weight="bold"),
                    rx.text("@usuario_20", font_weight="bold"),
                    rx.text("Respuesta: Django proporciona módulos integrados como django.contrib.auth para manejar la autenticación de usuarios de manera segura."),
                    padding="1em",
                    border="1px solid gray",
                    border_radius="8px",
                    margin_bottom="1em",
                    style={"margin-left": "-25px"},
                ),
                rx.box(
                    rx.text("@usuario_30", font_weight="bold"),
                    rx.text("Pregunta: ¿Alguna sugerencia para mejorar el rendimiento de las consultas SQL?", font_weight="bold"),
                    rx.text("@usuario_7", font_weight="bold"),
                    rx.text("Respuesta: Asegúrate de tener índices adecuados configurados, utiliza EXPLAIN para analizar los planes de consulta y considera la desnormalización de datos para tablas de acceso frecuente."),
                    rx.text("@usuario_14", font_weight="bold"),
                    rx.text("Respuesta: También, evita las subconsultas en favor de joins siempre que sea posible."),
                    padding="1em",
                    border="1px solid gray",
                    border_radius="8px",
                    margin_bottom="1em",
                    style={"margin-left": "-25px"},
                ),
                rx.box(
                    rx.text("@usuario_12", font_weight="bold"),
                    rx.text("Pregunta: ¿Cómo puedo desplegar una aplicación Flask en AWS?", font_weight="bold"),
                    rx.text("@usuario_25", font_weight="bold"),
                    rx.text("Respuesta: Puedes usar Elastic Beanstalk o desplegar manualmente con instancias EC2, y configurar un proxy inverso NGINX para tu aplicación Flask."),
                    padding="1em",
                    border="1px solid gray",
                    border_radius="8px",
                    margin_bottom="1em",
                    style={"margin-left": "-25px"},
                ),
                rx.box(
                    rx.text("@usuario_52", font_weight="bold"),
                    rx.text("Pregunta: ¿Qué lenguaje recomiendan para desarrollo web backend?", font_weight="bold"),
                    rx.text("@usuario_66", font_weight="bold"),
                    rx.text("Respuesta: Depende de tus preferencias y requisitos del proyecto; Python con Django o Flask, Node.js con Express, y Ruby con Ruby on Rails son opciones populares."),
                    padding="1em",
                    border="1px solid gray",
                    border_radius="8px",
                    margin_bottom="1em",
                    style={"margin-left": "-25px"},
                ),
                rx.box(
                    rx.text("@usuario_5", font_weight="bold"),
                    rx.text("Pregunta: ¿Cuál es la diferencia clave entre Java y C++ en términos de manejo de memoria?", font_weight="bold"),
                    rx.text("@Admin", font_weight="bold"),
                    rx.text("Respuesta: Java gestiona la memoria automáticamente a través del recolector de basura, mientras que en C++ debes gestionar la memoria manualmente con new y delete."),
                    padding="1em",
                    border="1px solid gray",
                    border_radius="8px",
                    margin_bottom="1em",
                    style={"margin-left": "-25px"},
                ),
                rx.box(
                    rx.text("@usuario_1", font_weight="bold"),
                    rx.text("Pregunta: ¿Cómo puedo trabajar con hilos en Java de manera eficiente?", font_weight="bold"),
                    rx.text("@usuario_2", font_weight="bold"),
                    rx.text("Respuesta: En Java, puedes utilizar la clase Thread o implementar la interfaz Runnable para crear hilos. Es recomendable usar Executors y ThreadPool para gestionar eficientemente múltiples hilos."),
                    padding="1em",
                    border="1px solid gray",
                    border_radius="8px",
                    margin_bottom="1em",
                    style={"margin-left": "-25px"},
                ),
                rx.box(
                    rx.text("@usuario_40", font_weight="bold"),
                    rx.text("Pregunta: ¿Cuál es la ventaja de usar punteros en C frente a C++?", font_weight="bold"),
                    rx.text("@Admin", font_weight="bold"),
                    rx.text("Respuesta: En C, los punteros son esenciales para manipular directamente la memoria y lograr mayor control sobre las estructuras de datos. En C++, se utilizan principalmente en contextos de programación de bajo nivel o para optimizaciones específicas."),
                    rx.text("@Admin", font_weight="bold"),
                    rx.text("Respuesta: Además, en C++ puedes utilizar smart pointers que manejan la memoria automáticamente."),
                    padding="1em",
                    border="1px solid gray",
                    border_radius="8px",
                    margin_bottom="1em",
                    style={"margin-left": "-25px"},
                ),
                padding="1em",
            ),
            value="tab1",
            padding="1em",
            width="100%",
        ),
        rx.tabs.content(
            rx.hstack(
                rx.vstack(
                    rx.upload(
                        rx.text("Arrastre y suelte archivos aquí o haga clic para seleccionar archivos"),
                        id="file_upload",
                        border="1px dotted rgb(107,99,246)",
                        padding="2em",
                        style={"margin-left": "-15px"}, 
                    ),
                    rx.button(
                        "Subir Archivos",
                        on_click=StateImag.handle_upload(rx.upload_files(upload_id="file_upload")),
                        style={
                            "margin-left": "-15px",
                            "bg": rx.color("accent", 8),
                            "_hover": {
                                "bg": rx.color("accent", 4),
                                "color": rx.color("accent", 11),
                            },
                            },
                    ),
                ),
                rx.vstack(
                    rx.upload(
                        rx.text("Arrastre y suelte imágenes aquí o haga clic para seleccionar imágenes"),
                        id="image_upload",
                        border="1px dotted rgb(107,99,246)",
                        padding="2em",
                        style={"margin-left": "-15px"},
                    ),
                    rx.button(
                        "Subir Imagenes",
                        on_click=StateImag.handle_upload(rx.upload_files(upload_id="image_upload")),
                        style={
                            "margin-left": "-15px",
                            "bg": rx.color("accent", 8),
                            "_hover": {
                                "bg": rx.color("accent", 6),
                                "color": rx.color("accent", 11),
                            },
                            },
                            ),
                    rx.foreach(StateImag.img, lambda img: rx.image(src=rx.get_upload_url(img))),
                ),
                spacing="2"
            ),
            value="tab2",
            padding="1em",
        ),
        padding="1em",
        width="100%",
    )
