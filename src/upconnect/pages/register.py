import reflex as rx
import re

# Definición de la clase RadixFormState para manejar el estado del formulario
class RegisterFormState(rx.State):
    # Campos para datos ingresados por el usuario
    user_entered_email: str
    user_entered_password: str
    user_entered_faculty: str  # Nuevo campo para la facultad
    registered_users: dict = {}  # Diccionario para almacenar usuarios registrados

    # Campos para datos enviados al servidor
    email: str = ""
    password: str = ""
    faculty: str = "" 

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
                            "Correo Institucional",
                            style={"font-size": "1.2em", "color": "#FFF"}
                        ),
                        rx.form.control(
                            rx.input(
                                #placeholder="Correo institucional",
                                on_change=RegisterFormState.set_user_entered_email,
                                name="email",
                                style={
                                    "padding": "0.5em",
                                    #"border": "1px solid #444",
                                    #"border-radius": "5px",
                                    "background-color": "#333",
                                    #"color": "#FFF",
                                    "box-shadow": "0 2px 4px rgba(0, 0, 0, 0.1)",
                                    #"transition": "border-color 0.3s",
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
                            force_match=RegisterFormState.invalid_email,
                            color="#FF6B6B",
                        ),
                        direction="column",
                        spacing="2",
                        align="stretch",
                    ),
                    name="email",
                    server_invalid=RegisterFormState.invalid_email,
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
                                #placeholder="Ingresa tu facultad",
                                on_change=RegisterFormState.set_user_entered_faculty,
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
                            force_match=RegisterFormState.faculty_empty,
                            color="#FF6B6B",
                        ),
                        direction="column",
                        spacing="2",
                        align="stretch",
                    ),
                    name="faculty",
                    server_invalid=RegisterFormState.faculty_empty,
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
                                #placeholder="Ingresa la contraseña que utilizarás",
                                type="password",
                                on_change=RegisterFormState.set_user_entered_password,
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
                            force_match=RegisterFormState.password_empty,
                            color="#FF6B6B",
                        ),
                        direction="column",
                        spacing="2",
                        align="stretch",
                    ),
                    name="password",
                    server_invalid=RegisterFormState.password_empty,
                ),
                # Botón para enviar el formulario
                rx.form.submit(
                    rx.button(
                        "Registrar",
                        disabled=RegisterFormState.input_invalid,
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
            on_submit=RegisterFormState.handle_submit,
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