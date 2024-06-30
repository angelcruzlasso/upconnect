import reflex as rx

# Definición de la clase RadixFormState para manejar el estado del formulario
class RadixFormState(rx.State):
    # Campos para datos ingresados por el usuario
    user_entered_email: str
    user_entered_password: str
    user_entered_faculty: str  # Nuevo campo para la facultad
    registered_users: dict = {}  # Diccionario para almacenar usuarios registrados

    # Campos para datos enviados al servidor
    email: str = ""
    password: str = ""
    faculty: str = ""  # Nuevo campo para la facultad

    # Método para validar si el correo electrónico es inválido
    @rx.var
    def invalid_email(self) -> bool:
        return not re.match(r"[^@]+@[^@]+\.[^@]+", self.user_entered_email)

    # Método para validar si la contraseña está vacía
    @rx.var
    def password_empty(self) -> bool:
        return not self.user_entered_password.strip()

    # Método para validar si el campo de facultad está vacío
    @rx.var
    def faculty_empty(self) -> bool:
        return not self.user_entered_faculty.strip()

    # Método para validar si algún campo es inválido
    @rx.var
    def input_invalid(self) -> bool:
        return self.invalid_email or self.password_empty or self.faculty_empty
    
    # Método para manejar el envío del formulario
    def handle_submit(self, form_data: dict):
        """Manejar el envío del formulario."""
        self.email = form_data.get("email")
        self.password = form_data.get("password")
        self.faculty = form_data.get("faculty")  # Guardar la facultad

        # Almacenar usuario registrado
        self.registered_users[self.email] = {
            "password": self.password,
            "faculty": self.faculty,
        }

# Función para generar la página de registro
def register_page() -> rx.Component:
    return rx.flex(
        rx.form.root(
            # Campo para ingresar el correo electrónico
            rx.flex(
                rx.form.field(
                    rx.flex(
                        rx.form.label(
                            "Nuevo usuario",
                            style={"font-size": "1.2em", "color": "#FFF"}
                        ),
                        rx.form.control(
                            rx.input(
                                placeholder="Ingresa el correo que utilizarás",
                                on_change=RadixFormState.set_user_entered_email,
                                name="email",
                                style={
                                    "padding": "0.5em",
                                    "border": "1px solid #444",
                                    "border-radius": "5px",
                                    "background-color": "#333",
                                    "color": "#FFF",
                                    "box-shadow": "0 2px 4px rgba(0, 0, 0, 0.1)",
                                    "transition": "border-color 0.3s",
                                },
                                _focus={
                                    "border-color": "#007BFF",
                                    "outline": "none",
                                },
                                _placeholder={
                                    "color": "#BBB",
                                }
                            ),
                            as_child=True,
                        ),
                        rx.form.message(
                            "Ese correo no es válido",
                            match="valueMissing",
                            force_match=RadixFormState.invalid_email,
                            color="#FF6B6B",
                        ),
                        direction="column",
                        spacing="2",
                        align="stretch",
                    ),
                    name="email",
                    server_invalid=RadixFormState.invalid_email,
                ),
                # Campo para ingresar la facultad
                rx.form.field(
                    rx.flex(
                        rx.form.label(
                            "Facultad",
                            style={"font-size": "1.2em", "color": "#FFF"}
                        ),
                        rx.form.control(
                            rx.input(
                                placeholder="Ingresa tu facultad",
                                on_change=RadixFormState.set_user_entered_faculty,
                                name="faculty",
                                style={
                                    "padding": "0.5em",
                                    "border": "1px solid #444",
                                    "border-radius": "5px",
                                    "background-color": "#333",
                                    "color": "#FFF",
                                    "box-shadow": "0 2px 4px rgba(0, 0, 0, 0.1)",
                                    "transition": "border-color 0.3s",
                                },
                                _focus={
                                    "border-color": "#007BFF",
                                    "outline": "none",
                                },
                                _placeholder={
                                    "color": "#BBB",
                                }
                            ),
                            as_child=True,
                        ),
                        rx.form.message(
                            "La facultad no puede estar vacía",
                            match="valueMissing",
                            force_match=RadixFormState.faculty_empty,
                            color="#FF6B6B",
                        ),
                        direction="column",
                        spacing="2",
                        align="stretch",
                    ),
                    name="faculty",
                    server_invalid=RadixFormState.faculty_empty,
                ),
                # Campo para ingresar la contraseña
                rx.form.field(
                    rx.flex(
                        rx.form.label(
                            "Contraseña",
                            style={"font-size": "1.2em", "color": "#FFF"}
                        ),
                        rx.form.control(
                            rx.input(
                                placeholder="Ingresa la contraseña que utilizarás",
                                type="password",
                                on_change=RadixFormState.set_user_entered_password,
                                name="password",
                                style={
                                    "padding": "0.5em",
                                    "border": "1px solid #444",
                                    "border-radius": "5px",
                                    "background-color": "#333",
                                    "color": "#FFF",
                                    "box-shadow": "0 2px 4px rgba(0, 0, 0, 0.1)",
                                    "transition": "border-color 0.3s",
                                },
                                _focus={
                                    "border-color": "#007BFF",
                                    "outline": "none",
                                },
                                _placeholder={
                                    "color": "#BBB",
                                }
                            ),
                            as_child=True,
                        ),
                        rx.form.message(
                            "La contraseña no puede estar vacía",
                            match="valueMissing",
                            force_match=RadixFormState.password_empty,
                            color="#FF6B6B",
                        ),
                        direction="column",
                        spacing="2",
                        align="stretch",
                    ),
                    name="password",
                    server_invalid=RadixFormState.password_empty,
                ),
                # Botón para enviar el formulario
                rx.form.submit(
                    rx.button(
                        "Registrar",
                        disabled=RadixFormState.input_invalid,
                        style={
                            "background-color": "#007BFF",
                            "color": "white",
                            "padding": "0.7em 1.5em",
                            "border": "none",
                            "border-radius": "5px",
                            "cursor": "pointer",
                            "transition": "background-color 0.3s",
                        },
                        _hover={
                            "background-color": "#0056b3",
                        },
                        _disabled={
                            "background-color": "#666",
                            "cursor": "not-allowed",
                        }
                    ),
                    as_child=True,
                ),
                direction="column",
                spacing="4",
                width="25em",
                style={
                    "margin": "0 auto",
                    "padding": "2em",
                    "border": "1px solid #555",
                    "border-radius": "10px",
                    "box-shadow": "0 4px 8px rgba(0, 0, 0, 0.2)",
                    "background-color": "#222",
                }
            ),
            # Manejo de eventos al enviar el formulario
            on_submit=RadixFormState.handle_submit,
            reset_on_submit=True,
        ),
        # Divider entre secciones
        rx.divider(size="4", style={"margin": "2em 0", "background-color": "#555"}),
        direction="column",
        spacing="4",
        align="center",
        justify="center",
        height="100vh",
        style={
            "background-color": "#121212",
            "padding": "2em",
            "color": "#FFF",
        }
    )


# Función para generar la página de inicio
def login() -> rx.Component:
    return rx.flex(
        rx.text(
            "Upconnect",
            style={
                "font-size": "3em",
                "font-weight": "bold",
                "text-align": "center",
                "margin-bottom": "1em",
                "background": "linear-gradient(90deg, #007BFF, #FFFFFF)",
                "background-clip": "text",
                "-webkit-background-clip": "text",
                "color": "transparent",
                "animation": "pixelate 2s infinite",
                "font-family": "'Press Start 2P', cursive",
                "letter-spacing": "0.1em",
            }
        ),
        rx.form.root(
            rx.flex(
                # Campo para ingresar el correo electrónico
                rx.form.field(
                    rx.flex(
                        rx.form.label(
                            "Correo electrónico",
                            style={"font-size": "1.2em", "color": "#FFF"}
                        ),
                        rx.form.control(
                            rx.input(
                                placeholder="Xopa, ingresa tu correo electrónico",
                                on_change=RadixFormState.set_user_entered_email,
                                name="email",
                                style={
                                    "padding": "0.5em",
                                    "border": "1px solid #444",
                                    "border-radius": "5px",
                                    "background-color": "#333",
                                    "color": "#FFF",
                                    "box-shadow": "0 2px 4px rgba(0, 0, 0, 0.1)",
                                    "transition": "border-color 0.3s",
                                },
                                _focus={
                                    "border-color": "#007BFF",
                                    "outline": "none",
                                },
                                _placeholder={
                                    "color": "#BBB",
                                }
                            ),
                            as_child=True,
                        ),
                        rx.form.message(
                            "Ese correo no es válido",
                            match="valueMissing",
                            force_match=RadixFormState.invalid_email,
                            color="#FF6B6B",
                        ),
                        direction="column",
                        spacing="2",
                        align="stretch",
                    ),
                    name="email",
                    server_invalid=RadixFormState.invalid_email,
                ),
                # Campo para ingresar la contraseña
                rx.form.field(
                    rx.flex(
                        rx.form.label(
                            "Contraseña",
                            style={"font-size": "1.2em", "color": "#FFF"}
                        ),
                        rx.form.control(
                            rx.input(
                                placeholder="Juega vivo recuerda no dar tu contraseña",
                                type="password",
                                on_change=RadixFormState.set_user_entered_password,
                                name="password",
                                style={
                                    "padding": "0.5em",
                                    "border": "1px solid #444",
                                    "border-radius": "5px",
                                    "background-color": "#333",
                                    "color": "#FFF",
                                    "box-shadow": "0 2px 4px rgba(0, 0, 0, 0.1)",
                                    "transition": "border-color 0.3s",
                                },
                                _focus={
                                    "border-color": "#007BFF",
                                    "outline": "none",
                                },
                                _placeholder={
                                    "color": "#BBB",
                                }
                            ),
                            as_child=True,
                        ),
                        rx.form.message(
                            "La contraseña no puede estar vacía",
                            match="valueMissing",
                            force_match=RadixFormState.password_empty,
                            color="#FF6B6B",
                        ),
                        direction="column",
                        spacing="2",
                        align="stretch",
                    ),
                    name="password",
                    server_invalid=RadixFormState.password_empty,
                ),
                # Botón para enviar el formulario
                rx.form.submit(
                    rx.button(
                        "Enviar",
                        disabled=RadixFormState.input_invalid,
                        style={
                            "background-color": "#007BFF",
                            "color": "white",
                            "padding": "0.7em 1.5em",
                            "border": "none",
                            "border-radius": "5px",
                            "cursor": "pointer",
                            "transition": "background-color 0.3s",
                        },
                        _hover={
                            "background-color": "#0056b3",
                        },
                        _disabled={
                            "background-color": "#666",
                            "cursor": "not-allowed",
                        }
                    ),
                    as_child=True,
                ),
                direction="column",
                spacing="4",
                width="25em",
                style={
                    "margin": "0 auto",
                    "padding": "2em",
                    "border": "1px solid #555",
                    "border-radius": "10px",
                    "box-shadow": "0 4px 8px rgba(0, 0, 0, 0.2)",
                    "background-color": "#222",
                }
            ),
            # Manejo de eventos al enviar el formulario
            on_submit=RadixFormState.handle_submit,
            reset_on_submit=True,
        ),
        # Divider entre secciones
        rx.divider(size="4", style={"margin": "2em 0", "background-color": "#555"}),
        # Enlace para registro
        rx.text(
            "¿No estás registrado? ",
            rx.link(
                "Regístrate aquí",
                href="/register",
                style={
                    "color": "#007BFF",
                    "text-decoration": "none",
                    "font-weight": "bold",
                },
                _hover={
                    "text-decoration": "underline",
                }
            ),
            style={"text-align": "center", "font-size": "1em", "color": "#FFF"}
        ),
        direction="column",
        spacing="4",
        align="center",
        justify="center",
        height="100vh",
        style={
            "background-color": "#121212",
            "padding": "2em",
            "color": "#FFF",
        }
    )

