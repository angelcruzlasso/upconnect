import reflex as rx

class EditorState(rx.State):
    content: str = "<p>Editor content</p>"
    saved_content: str = ""
    show_editor: bool = False

    def handle_change(self, content: str):
        """Handle the editor value change."""
        self.content = content

    def save_content(self):
        """Save the editor content and update the saved content display."""
        self.saved_content = self.content
        print(f"Content saved: {self.content}")
        # Save to database or file

    def toggle_editor(self):
        """Toggle the visibility of the editor."""
        self.show_editor = not self.show_editor

def editor_example() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.button(
                "Publicar",
                on_click=EditorState.toggle_editor,
                style={
                    "font-size": "1em",
                    "padding": "10px 20px",
                    "margin": "10px 0",
                    "border": "none",
                    "border-radius": "5px",
                    "cursor": "pointer",
                    "bg": rx.color("accent", 8),
                    "_hover": {
                            "bg": rx.color("accent", 4),
                            "color": rx.color("accent", 11),
                            },
                },
            ),
            rx.cond(
                EditorState.show_editor,
                rx.vstack(
                    rx.editor(
                        set_contents=EditorState.content,
                        on_change=EditorState.handle_change,
                        style={
                            "font-size": "1em",
                            "width": "100%",
                            "height": "400px",
                            "padding": "10px",
                            "border": "1px solid #ccc",
                            "border-radius": "5px",
                            "margin-bottom": "10px",
                        },
                    ),
                    rx.hstack(
                        rx.button(
                            "Enviar",
                            on_click=EditorState.save_content,
                            style={
                                "font-size": "1em",
                                "padding": "10px 20px",
                                "margin": "10px 0",
                                "border": "none",
                                "border-radius": "5px",
                                "cursor": "pointer",
                                "bg": rx.color("accent", 8),
                                "_hover": {
                                    "bg": rx.color("accent", 4),
                                    "color": rx.color("accent", 11),
                            },
                            },
                        ),
                        rx.button(
                            "Cancelar",
                            on_click=EditorState.toggle_editor,
                            style={
                                "font-size": "1em",
                                "padding": "10px 20px",
                                "margin": "10px 0",
                                "border": "none",
                                "border-radius": "5px",
                                "cursor": "pointer",
                                "bg": "red",
                                "_hover": {
                                    "bg": rx.color("accent", 4),
                                    "color": rx.color("accent", 11),
                            },
                            },
                        ),
                        style={"justify-content": "flex-start", "gap": "10px"},
                    ),
                    rx.box(
                        rx.html(EditorState.saved_content),
                        border="1px solid #ccc",
                        padding="10px",
                        margin_top="10px",
                        style={"font-size": "1em"},
                    ),
                ),
            ),
            style={"font-size": "1em", "width": "100%"},
        ),
        style={"margin-left": "20px", "width": "calc(100% - 40px)"}, 
    ),
