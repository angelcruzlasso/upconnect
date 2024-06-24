import reflex as rx

class EditorState(rx.State):
    content: str = "<p>Editor content</p>"
    saved_content: str = ""

    def handle_change(self, content: str):
        """Handle the editor value change."""
        self.content = content

    def save_content(self):
        """Save the editor content and update the saved content display."""
        self.saved_content = self.content
        print(f"Content saved: {self.content}")
        # Save to database or file

def editor_example() -> rx.Component:
    return rx.vstack(
        rx.editor(
            set_contents=EditorState.content,
            on_change=EditorState.handle_change,
            style={"font-size": "30px"},
        ),
        rx.button(
            "Enviar",
            on_click=EditorState.save_content,
            style={"margin-left": "2px", "font-size": "0.9em"},
        ),
        rx.box(
            rx.html(EditorState.saved_content),
            border="1px solid #ccc",
            padding="10px",
            margin_top="10px",
            style={"font-size": "20px"},
        ),
        style={"margin-left": "15px", "font-size": "1.5rem"},
    )
