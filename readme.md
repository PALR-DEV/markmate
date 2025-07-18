# mdview — Terminal Markdown Note Taker

> A terminal-first CLI tool for editing and previewing Markdown side by side.

---

## 📖 Concept & Idea

**mdview** is a terminal-based note-taking application designed for developers, writers, and power users who prefer to stay within the command line. It provides:

- **Left pane**: Markdown editor with live typing
- **Right pane**: Instant rendered preview

Notes are stored as plain `.md` files, ensuring portability, versioning, and simplicity.

## 💡 Why This Tool Exists

1. **Minimal Context Switching**: Stay in your terminal without launching a browser or separate editor.
2. **Live Feedback**: Instant preview of headers, lists, code blocks, and more as you type.
3. **Plain-Text Power**: Uses standard Markdown files—no proprietary formats or databases.
4. **Git-Friendly**: Easily version, branch, and collaborate on notes using your existing Git workflow.

## ✅ Usefulness & Benefits

- **Efficiency**: Edit documentation, READMEs, and notes all within the terminal.
- **Collaboration**: Store notes alongside code in a Git repository for backup and teamwork.
- **Lightweight**: No heavy GUI dependencies; runs on any system with Python and a terminal.

## 🚀 Key Features (MVP)

- 🔄 **Split-Screen UI** — Editor + Live Preview
- 💾 **Save & Reload** — Press Ctrl+S to write changes back to your file

## ⚙️ Installation

```bash
pip install markdown-it-py pygit2
```

## 🚀 Usage

### Single File Mode

```bash
mdview README.md
```

### Quick New Note

```bash
mdview new "Meeting Notes"
```


## 🛠️ Development & Contribution

1. Clone the repository and install dependencies.
2. Explore the `main.py` entry point to understand the split-view layout.
3. Contributions welcome! Feel free to open issues or submit pull requests.

## 🌐 License

MIT © Pedro Lorenzo Rosario

