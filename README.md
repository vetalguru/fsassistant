# FSAssistant

**FSAssistant** is an AI-powered Python package that helps you analyze, clean, and organize your file system. It combines local file scanning with the intelligence of ChatGPT to suggest or execute actions like deduplication, sorting, and archiving.

## 🚀 Features

- 📂 Scan directories and collect metadata
- 🔍 Detect and handle duplicate files
- 🧠 Use ChatGPT to interpret and plan file organization
- 🧹 Sort files by type, date, or usage
- 🧪 Dry-run mode to preview actions before execution
- 🛠️ CLI interface for quick usage

## 📦 Installation

```bash
pip install fsassistant
```

Or clone and install locally:

```bash
git clone https://github.com/yourusername/fsassistant.git
cd fsassistant
pip install .
```

## ⚙️ Usage

### Basic scan and summary

```bash
fsassist scan ~/Downloads
```

### Scan and apply AI-powered cleanup suggestions

```bash
fsassist organize ~/Downloads --use-ai --dry-run
```

### Execute changes

```bash
fsassist organize ~/Downloads --use-ai --execute
```

## 💡 Example Workflow

1. You run a scan on a directory.
2. The assistant sends metadata (like file types, duplicates, sizes, etc.) to ChatGPT.
3. ChatGPT replies with a list of recommended actions.
4. You review the plan and approve or apply it.

## 🔐 Safety

FSAssistant defaults to **dry-run mode** to ensure you see proposed changes before anything is modified. You must explicitly use `--execute` to perform real actions.

## 🧱 Project Structure

```
fsassistant/
├── fsassistant/       # Core package logic
├── scripts/           # CLI entry point
├── tests/             # Unit tests
├── README.md
├── pyproject.toml
└── LICENSE
```

## 🧠 Requirements

- Python 3.8+
- [OpenAI API key](https://platform.openai.com/account/api-keys)

## 📄 License

This project is licensed under the MIT License.

---

**FSAssistant** — Your smart, safe, and scriptable file system assistant.
