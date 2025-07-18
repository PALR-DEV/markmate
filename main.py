"""
MarkMate - A Simple Markdown Editor with Live Preview

This application provides a split-screen interface with a markdown editor on the left
and a live preview on the right. It demonstrates the use of the Textual TUI framework
to create a rich terminal user interface.

Key components:
- EditorPane: Text editor for writing markdown
- ViewerPane: Live preview of the rendered markdown
- PaneTitle: Title bar for each pane
- MainApp: Main application class that orchestrates everything

Author: PALR-DEV
Date: July 18, 2025
"""

from textual.app import App, ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Header, Footer, TextArea, Markdown, Static
from textual.message import Message


class EditorPane(TextArea):
    """Multiline editor that emits a Changed event when edited.
    
    This class extends Textual's TextArea widget to provide markdown editing functionality.
    It includes default content, keyboard bindings, and custom event handling to notify
    other components when the content changes.
    
    Attributes:
        BINDINGS: Keyboard shortcuts mapped to actions
        DEFAULT_MARKDOWN: Initial markdown content to display
    """
    
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
        """Handle text changed events.
        
        This method is automatically called when the content of the TextArea
        changes. It fires a custom Changed event with the current content,
        which will be caught by the MainApp to update the preview.
        """
        # Fire the custom Changed message with current content
        self.post_message(self.Changed(self, self.value))


class PaneTitle(Static):
    """Title bar for panes.
    
    A simple widget to display a title at the top of each pane.
    The styling for this component is defined in the MainApp's CSS.
    
    Args:
        title: The text to display in the title bar
        **kwargs: Additional arguments to pass to the Static widget
    """
    
    def __init__(self, title: str, **kwargs) -> None:
        super().__init__(title, **kwargs)


class ViewerPane(VerticalScroll):
    """Container for markdown preview.
    
    This class wraps a Markdown widget in a scrollable container
    to provide a preview of the rendered markdown content. It
    contains a method to update the content based on the editor's text.
    
    Attributes:
        preview: The Markdown widget that renders the content
    """

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
    """Main application class for MarkMate.
    
    This class orchestrates the entire application. It creates the layout,
    handles events, and manages the communication between components.
    
    The layout consists of a horizontal split with the editor on the left
    and the preview on the right. When the editor content changes, the
    preview is updated automatically.
    
    Attributes:
        CSS: Styling for the application components
    """
    
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
        """Create the user interface layout.
        
        This method sets up the UI structure with a header, footer, and the
        main content area split into editor and preview panes. Each pane
        has a title and appropriate widgets.
        
        Returns:
            A generator of widgets to be displayed in the app.
        """
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
    """Entry point of the application.
    
    This block runs when the script is executed directly.
    It creates an instance of the MainApp and starts the application.
    """
    app = MainApp()
    app.run()
