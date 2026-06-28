# uv Beginner's Handbook

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-June%202026-blue)](CHANGELOG.md)
[![Made with ❤️](https://img.shields.io/badge/Made%20with-%E2%9D%A4%EF%B8%8F-red)]()

> **A Complete, Beginner-Friendly Handbook for Astral's uv Package Manager**
>
> Learn Python dependency management, virtual environments, and modern packaging workflows — from zero to confident.

---

## 🚀 Quick Start

### 1. Install uv (2 minutes)

**macOS & Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Create Your First Project (1 minute)

```bash
uv init hello-world
cd hello-world
```

### 3. Run It (30 seconds)

```bash
uv run python -c "print('Hello from uv!')"
```

**That's it.** You've just used the fastest Python package manager in the world.

---

## 📚 What Is This?

This is a **complete, free handbook** that teaches you everything about **uv**, Astral's lightning-fast Python package manager.

### For Absolute Beginners:
- No prior Python experience needed
- We explain everything from scratch
- Real-world examples you can run today
- Decision trees for common scenarios

### For Experienced Developers:
- Understand uv's design philosophy
- Learn when to use each command
- See how it compares to `pip`, `poetry`, `pyenv`
- Advanced topics: workspaces, publishing, caching

### Why Uv?

```
Traditional Tools          uv
━━━━━━━━━━━━━━━━━        ━━━━━━━━━━━━━
8+ different tools        1 tool
pip (slow)               10-100x faster
virtualenv               Built-in
pyenv                    Included
pipx                     `uv tool`
poetry                   `uv init`
pip-tools                `uv.lock`
```

**One tool. One command structure. Much faster.**

---

## 📖 Table of Contents

### Read the Full Handbook
👉 **[Start Reading Here](handbook/uv_beginners_handbook.md)**

### Quick Navigation

**Part 1-3: Foundations & Getting Started**
- [What is Python?](handbook/uv_beginners_handbook.md#what-is-python)
- [What is a Package Manager?](handbook/uv_beginners_handbook.md#what-is-a-package-manager)
- [Why Does uv Exist?](handbook/uv_beginners_handbook.md#why-does-uv-exist)
- [Installation](handbook/uv_beginners_handbook.md#installation)

**Part 4-5: Projects & Dependencies**
- [Creating Your First Project](handbook/uv_beginners_handbook.md#initializing-a-new-project)
- [Adding Dependencies](handbook/uv_beginners_handbook.md#adding-dependencies)
- [Virtual Environments Explained](handbook/uv_beginners_handbook.md#virtual-environments)

**Part 6-7: Running Code & Tools**
- [Running Python Code](handbook/uv_beginners_handbook.md#running-code)
- [Installing & Managing Tools](handbook/uv_beginners_handbook.md#part-7-tools--utilities)

**Part 8-14: Advanced & Reference**
- [Working with Python Versions](handbook/uv_beginners_handbook.md#part-5-working-with-python-versions)
- [Command Reference](handbook/uv_beginners_handbook.md#part-11-command-reference)
- [Real-World Examples](handbook/uv_beginners_handbook.md#part-14-real-world-examples)
- [Cheat Sheets](handbook/uv_beginners_handbook.md#part-12-cheat-sheets)
- [Troubleshooting & FAQ](handbook/uv_beginners_handbook.md#appendix-troubleshooting--faq)

---

## 🎯 Who Should Read This?

| Profile | Read This? | Start Here |
|---------|-----------|-----------|
| Complete beginner to Python | ✅ Yes | [Part 1: The Foundations](handbook/uv_beginners_handbook.md#part-1-the-foundations) |
| Used Python but confused by pip | ✅ Yes | [Part 2: Getting Started](handbook/uv_beginners_handbook.md#part-2-getting-started) |
| Familiar with Python, new to uv | ✅ Yes | [Part 3: Key Concepts](handbook/uv_beginners_handbook.md#part-3-key-concepts-explained) |
| Migrating from pip/poetry/pyenv | ✅ Yes | [Comparison Tables](handbook/uv_beginners_handbook.md#part-13-comparison-tables) |
| Need decision help | ✅ Yes | [Decision Trees](handbook/uv_beginners_handbook.md#part-10-decision-trees--workflows) |
| Troubleshooting a problem | ✅ Yes | [Troubleshooting](handbook/uv_beginners_handbook.md#appendix-troubleshooting--faq) |
| Experienced developer | ✅ Maybe | [Command Reference](handbook/uv_beginners_handbook.md#part-11-command-reference) |

---

## 💡 Key Features of This Handbook

✅ **Complete** — 14 parts covering everything from "What is Python?" to publishing packages  
✅ **Beginner-Friendly** — No assumed knowledge. We explain everything.  
✅ **Practical** — Real-world examples you can run immediately  
✅ **Decision Trees** — Flowcharts for common scenarios  
✅ **Cheat Sheets** — Quick reference for daily workflows  
✅ **Real Projects** — AI chatbot, web API, data analysis, more  
✅ **Troubleshooting** — Common problems and solutions  
✅ **Free & Open** — Licensed under MIT  
✅ **Maintained** — Regular updates for uv improvements  

---

## 🔍 Popular Sections

### I want to...

| Goal | Link | Time |
|------|------|------|
| Understand what uv is | [What Problem Does uv Solve?](handbook/uv_beginners_handbook.md#what-problem-does-uv-solve) | 5 min |
| Install uv | [Installation](handbook/uv_beginners_handbook.md#installation) | 5 min |
| Create a new project | [Initializing a New Project](handbook/uv_beginners_handbook.md#initializing-a-new-project) | 10 min |
| Add a library | [Adding Dependencies](handbook/uv_beginners_handbook.md#adding-dependencies) | 10 min |
| Understand virtual environments | [Virtual Environments](handbook/uv_beginners_handbook.md#virtual-environments) | 10 min |
| See a complete example | [Real-World Examples](handbook/uv_beginners_handbook.md#part-14-real-world-examples) | 20 min |
| Get help with a problem | [Troubleshooting](handbook/uv_beginners_handbook.md#appendix-troubleshooting--faq) | 10 min |
| Learn every command | [Command Reference](handbook/uv_beginners_handbook.md#part-11-command-reference) | 30 min |

---

## 📂 Project Structure

```
uv-beginners-handbook/
├── handbook/
│   └── uv_beginners_handbook.md    ← THE HANDBOOK
├── examples/                        ← Structured command & project examples
│   ├── basic/                       ← Basic commands (install, help, cache)
│   ├── python/                      ← Python version management commands
│   ├── projects/                    ← Project & pip compatibility commands
│   ├── scripts/                     ← Script running commands & templates
│   ├── ai/                          ← OpenAI chatbot flask project
│   ├── fastapi/                     ← Todo REST API (FastAPI + SQLite)
│   ├── data-analysis/               ← COVID-19 statistics analyzer
│   ├── workspaces/                  ← Workspace monorepo example
│   └── docker/                      ← Production Dockerfile configuration
├── README.md                        ← You are here
├── CONTRIBUTING.md                  ← How to help
├── CODE_OF_CONDUCT.md              ← Community guidelines
├── LICENSE                          ← MIT License
├── CHANGELOG.md                     ← What's new
└── SECURITY.md                      ← Security guidelines
```

---

## 📖 How to Read This Handbook

### Option 1: Start to Finish
Best for complete beginners who want comprehensive understanding.

```
Part 1 → Part 2 → Part 3 → Part 4 → Part 5 → ... → Part 14
(2-3 hours total)
```

### Option 2: Guided Path
Choose based on your background:

**Path A: Complete Beginner**
```
Intro → Part 1 (Foundations) → Part 2 (Getting Started) 
→ Part 4 (Creating Projects) → Part 14 (Examples)
```

**Path B: Python Experience**
```
Intro → Part 3 (Key Concepts) → Part 4 (Creating Projects)
→ Part 11 (Command Reference) → Examples
```

**Path C: Tool Migration**
```
Part 1 (Why uv?) → Part 13 (Comparisons)
→ Part 11 (Commands) → Part 10 (Workflows)
```

### Option 3: Problem-Based Lookup
Jump directly to:
- [Cheat Sheets](handbook/uv_beginners_handbook.md#part-12-cheat-sheets) — Quick reference
- [Decision Trees](handbook/uv_beginners_handbook.md#part-10-decision-trees--workflows) — Flow diagrams
- [Troubleshooting](handbook/uv_beginners_handbook.md#appendix-troubleshooting--faq) — Common issues
- [FAQ](handbook/uv_beginners_handbook.md#appendix-troubleshooting--faq) — Questions answered

---

## 🏃 Running the Examples

This handbook features structured commands and complete runnable projects.

### 1. Command Examples (basic, python, projects)
The `basic/`, `python/`, and `projects/` directories contain nested subdirectories for each command. Each folder has:
* `command.txt`: The exact command to run.
* `output.txt`: The captured real output of the execution.

### 2. Running Scripts
Execute the scripts containing inline-declared dependencies:
```bash
cd examples/scripts
uv run fetch.py
```

### 3. Running the AI Chatbot
Launch the Flask + OpenAI chatbot server:
```bash
cd examples/ai
uv sync
# Configure your OpenAI key in .env
uv run python src/ai_chatbot/main.py
```

### 4. Running the FastAPI Todo API
Run the FastAPI + SQLAlchemy + SQLite application:
```bash
cd examples/fastapi
uv sync
uv run uvicorn todo_api.main:app --reload
```

### 5. Running the Data Analysis Project
Run the COVID-19 statistics analyzer:
```bash
cd examples/data-analysis
uv sync
uv run python src/covid_analysis/analyze.py
```

### 6. Running the Workspace Monorepo
Sync and run the API package inside the workspace:
```bash
cd examples/workspaces
uv sync
uv run --package api uvicorn api:app --port 8000
```

### 7. Running the Docker Container
Build and run using the caching-optimized Dockerfile:
```bash
cd examples/docker
docker build -t my-uv-app .
docker run -it my-uv-app
```

See the respective `README.md` or commands list in each directory for detailed command references.

---

## 📚 What You'll Learn

By reading this handbook, you'll be able to:

- ✅ Install and use uv on macOS, Linux, and Windows
- ✅ Create new Python projects from scratch
- ✅ Add, remove, and update libraries your projects depend on
- ✅ Run Python code reliably in virtual environments
- ✅ Manage multiple Python versions simultaneously
- ✅ Install and run command-line tools
- ✅ Lock dependencies for team collaboration
- ✅ Troubleshoot common issues
- ✅ Understand how modern Python development works
- ✅ Publish your own Python packages (bonus)

---

## 🔗 External Resources

- **[Official uv Documentation](https://docs.astral.sh/uv/)** — Complete reference
- **[Astral GitHub](https://github.com/astral-sh)** — Source code
- **[Astral Discord](https://discord.com/invite/astral-sh)** — Community
- **[PyPI.org](https://pypi.org/)** — Python Package Index
- **[Python.org](https://python.org/)** — Official Python site

---

## ❓ Common Questions

### Is this handbook up to date?
Yes. Last updated **June 2026** for uv 0.5.x+. Check [CHANGELOG.md](CHANGELOG.md) for what's new.

### Is this official Astral documentation?
No, this is **community-created**. It's not official but complementary to [Astral's official docs](https://docs.astral.sh/uv/).

### Can I use this at work?
Absolutely. It's licensed under MIT. Use it freely for learning, training, or teaching.

### How do I report errors?
Found a typo or mistake? [Open an issue](https://github.com/mkcoder7586-beep/uv-beginners-handbook/issues) or see [CONTRIBUTING.md](CONTRIBUTING.md).

### Can I translate this?
Yes! We welcome translations. See [CONTRIBUTING.md](CONTRIBUTING.md#translations) for guidelines.

### Is there a PDF version?
Not yet, but you can print the markdown or use markdown-to-PDF tools. We may add a PDF release later.

---

## 🤝 Contributing

We welcome contributions of all kinds:

- **Fix typos or improve wording**
- **Report errors or clarifications**
- **Add examples or edge cases**
- **Suggest new sections**
- **Translate to other languages**
- **Create video walkthroughs**

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 📄 License

This project is licensed under the Creative Commons Attribution 4.0 International (CC BY 4.0) License.

See the LICENSE file for details.

---

## 🙏 Acknowledgments

### Built For
- **Astral** — for creating uv
- **The Python Community** — for feedback and enthusiasm
- **You** — for learning and sharing

### Special Thanks
- Astral's uv documentation (inspiration)
- Python Packaging Guide
- Community feedback and contributions

---

## 📊 Repository Stats

| Metric | Value |
|--------|-------|
| **Handbook Size** | ~40,000 words |
| **Parts** | 14 |
| **Example Projects** | 4 |
| **Code Samples** | 100+ |
| **Cheat Sheets** | 3 |
| **Read Time** | 2-3 hours (complete) |
| **License** | MIT |
| **Status** | Active |

---

## 🐛 Report a Problem

Found an error? Have a question? See something unclear?

**[Open an Issue](https://github.com/mkcoder7586-beep/uv-beginners-handbook/issues)**

Please include:
- What section you were reading
- What was confusing or wrong
- What you expected instead
- Your operating system (macOS/Linux/Windows)

---

## 💬 Get in Touch

- **Questions?** → Check the [Troubleshooting section](handbook/uv_beginners_handbook.md#appendix-troubleshooting--faq)
- **Found an error?** → [Open an issue](https://github.com/mkcoder7586-beep/uv-beginners-handbook/issues)
- **Want to contribute?** → See [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 🚀 Next Steps

1. **[Start Reading](handbook/uv_beginners_handbook.md)** the handbook
2. **[Run an Example](examples/)** project
3. **[Ask Questions](https://github.com/mkcoder7586-beep/uv-beginners-handbook/issues)** if stuck
4. **[Contribute](CONTRIBUTING.md)** improvements

---

**Happy learning! 🎉**

> Made with ❤️ for everyone learning Python package management.
>
> Last updated: June 2026 | [Changelog](CHANGELOG.md) | [License](LICENSE)