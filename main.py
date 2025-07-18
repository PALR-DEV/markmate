from textual.app import App, ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Header, Footer, TextArea, Markdown, Static
from textual.message import Message


class EditorPane(TextArea):
    """Multiline editor that emits a Changed event when edited."""
    
    BINDINGS = [("ctrl+s", "save", "Save")]
    
    DEFAULT_MARKDOWN = """# Welcome to MarkMate
    
## A simple markdown editor

This is a *live preview* of your markdown content.

### Features:
- Real-time markdown preview
- Simple and clean interface
- Syntax highlighting

```python
# You can even include code blocks
def hello_world():
    print("Hello, Markdown!")
```

> Blockquotes are supported too!

Enjoy writing with **MarkMate**!
"""

    class Changed(Message):
        """Custom event to signal content change."""

        def __init__(self, sender: "EditorPane", value: str | None = None) -> None:
            self.value = value if value is not None else sender.value
            super().__init__()
    
    def on_mount(self) -> None:
        """Set initial content when mounted."""
        self.value = self.DEFAULT_MARKDOWN
        self.focus()
    
    def action_save(self) -> None:
        """Handle save action."""
        self.notify("Document saved!", title="Save")

    def on_text_changed(self) -> None:
        # Fire the custom Changed message with current content
        self.post_message(self.Changed(self, self.value))


class PaneTitle(Static):
    """Title bar for panes."""
    
    def __init__(self, title: str, **kwargs) -> None:
        super().__init__(title, **kwargs)


class ViewerPane(VerticalScroll):
    """Container for markdown preview."""

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.preview = Markdown("")
    
    def compose(self) -> ComposeResult:
        yield PaneTitle("📄 Preview")
        yield self.preview
        
    def update_content(self, new_text: str) -> None:
        """Update the markdown preview content."""
        # Update the markdown content
        self.preview.update(new_text)


class MainApp(App):
    CSS = """
    EditorPane {
        width: 1fr;
        height: 100%;
        padding: 1;
        border: solid gray;
    }
    ViewerPane {
        width: 1fr;
        height: 100%;
        padding: 1;
        border: solid green;
    }
    PaneTitle {
        background: $secondary;
        color: $text;
        padding: 1;
        width: 100%;
        text-align: center;
        text-style: bold;
    }
    Markdown {
        padding: 1 2;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal():
            with VerticalScroll(id="editor-container"):
                yield PaneTitle("✏️ Editor")
                yield EditorPane(id="editor")
            yield ViewerPane(id="viewer")
        yield Footer()

    def on_mount(self) -> None:
        """Initialize the app with default content."""
        # Set initial preview content
        editor = self.query_one(EditorPane)
        viewer = self.query_one("#viewer", ViewerPane)
        viewer.update_content(editor.DEFAULT_MARKDOWN)
        
    def on_editor_pane_changed(self, event: EditorPane.Changed) -> None:
        """Update the preview when the editor content changes."""
        viewer = self.query_one("#viewer", ViewerPane)
        viewer.update_content(event.value)


if __name__ == "__main__":
    app = MainApp()
    app.run()
