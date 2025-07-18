# MarkMate - Terminal Markdown Editor with Live Preview

> A split-screen Markdown editor with real-time preview built with the Textual TUI framework.

---

## 📖 Concept & Idea

**MarkMate** is a terminal-based markdown editing application designed for developers, writers, and power users who prefer to stay within the command line. It provides:

- **Left pane**: A full-featured markdown editor with syntax highlighting
- **Right pane**: Real-time rendered preview that updates as you type

MarkMate provides a distraction-free writing environment right in your terminal.

## 💡 Why This Tool Exists

1. **Minimal Context Switching**: Stay in your terminal without launching a browser or separate editor.
2. **Live Feedback**: Instant preview of headers, lists, code blocks, and formatting as you type.
3. **Terminal-First Design**: Built for developers who live in the terminal.
# Code Structure

## Main Components

The application is structured around four main components:

1. **`EditorPane`** - The text editor for writing markdown
   - Extends Textual's `TextArea` with markdown-specific functionality
   - Emits custom events when content changes
   - Includes keyboard bindings like Ctrl+S for save actions

2. **`ViewerPane`** - The preview pane for rendered markdown
   - Contains a scrollable container with a Markdown widget
   - Updates in real-time as the editor content changes

3. **`PaneTitle`** - Styled title bar for each pane
   - Simple widget to provide visual separation and labeling

4. **`MainApp`** - The main application orchestrator
   - Sets up the UI layout and styling
   - Handles events between components
   - Manages the state of the application

## Event Flow

The live preview functionality works through this event flow:

1. User types in the `EditorPane`
2. `on_text_changed()` fires and posts a `Changed` message
3. `MainApp.on_editor_pane_changed()` catches this message
4. The viewer is updated with the new content

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/PALR-DEV/markmate.git
cd markmate

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install textual
```

## 🚀 Usage

```bash
# Run the application
python main.py
```

## 🛠️ Future Enhancements

- File saving and loading functionality
- Multiple tabs for editing different files
- Custom themes and styling options
- Markdown extension support
- Export to HTML or PDF

## 🌐 License

MIT © Pedro Alejandro Lorenzo Rosario

