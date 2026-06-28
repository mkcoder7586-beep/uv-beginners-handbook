# uv Frequently Asked Questions (FAQ)

## General Questions

### Q: Is uv ready for production use?
**A:** Yes, absolutely. uv is mature, actively maintained by Astral, and used in production by major companies and open-source projects. It's safe for:
- Development projects
- Deployed applications
- CI/CD pipelines
- Enterprise environments

See the handbook appendix for deployment examples.

---

### Q: How is uv different from pip?
**A:** 
| Aspect | pip | uv |
|--------|-----|-----|
| Speed | Slow | 10-100x faster |
| Lock files | No | Yes |
| Python management | No | Yes |
| Tool installation | No | Yes |
| Project management | No | Yes |
| Single tool | No | Yes (replaces 8+ tools) |

See Part 13: Comparison Tables in the handbook.

---

### Q: Do I have to use uv for everything?
**A:** No. You can:
- Use uv for new projects (`uv init`)
- Use traditional pip workflows with `uv pip`
- Use just the Python installer (`uv python install`)
- Mix tools if needed (though not recommended)

Start with `uv init` for new projects. It's the simplest path.

---

### Q: Can I use uv with Conda?
**A:** No, don't mix them. Both solve similar problems:
- **Conda**: Handles packages, environments, and Python (anaconda ecosystem)
- **uv**: Handles packages, environments, and Python (PyPI ecosystem)

Choose one for each project. For most people, uv is simpler and faster.

---

### Q: Does uv work on Windows?
**A:** Yes, fully supported. Installation:
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

All commands work the same on Windows, macOS, and Linux.

---

## Installation & Setup

### Q: How do I install uv?

**macOS and Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Via Homebrew (macOS):**
```bash
brew install uv
```

**Via pip (if you have Python):**
```bash
pip install uv
```

Verify with: `uv --version`

See Part 2: Getting Started in the handbook.

---

### Q: Where does uv store things?
**A:**
| What | Location |
|------|----------|
| **Python versions** | `~/.local/share/uv/pythons/` (Linux/macOS), `%APPDATA%\uv\pythons\` (Windows) |
| **Cache** | `~/.cache/uv` (Linux), `~/Library/Caches/uv` (macOS), `%LOCALAPPDATA%\uv\cache\` (Windows) |
| **Project venv** | `.venv/` (in your project folder) |

Check cache location: `uv cache dir`

---

### Q: Do I need to have Python installed to use uv?
**A:** No! uv can download and install Python for you.

```bash
uv init myproject          # Creates project with Python
uv python install 3.12     # Downloads Python 3.12
```

You can use uv even with no Python pre-installed.

---

## Project Management

### Q: How do I create a new project?

```bash
uv init myproject
cd myproject
```

That's it. See Part 4: Creating & Managing Projects.

---

### Q: What files do I commit to Git?

**Always commit:**
- `pyproject.toml` (project configuration)
- `uv.lock` (exact dependencies)
- `.python-version` (Python version)
- `.gitignore` (exclude .venv, .env)
- All source code

**Never commit:**
- `.venv/` (virtual environment)
- `.env` (secrets)
- `__pycache__/` (Python cache)

Suggested `.gitignore`:
```
.venv/
__pycache__/
*.pyc
.env
.env.local
```

---

### Q: How do I rename a project?

```bash
# 1. Rename the folder
mv old-name new-name
cd new-name

# 2. Update pyproject.toml
# Change: name = "old-name" → name = "new-name"

# 3. Update Git
git add .
git commit -m "Rename project to new-name"
```

---

### Q: How do I delete a project?

```bash
cd ..
rm -rf myproject
# or on Windows: rmdir /s myproject
```

That's it. No cleanup needed.

---

## Dependencies

### Q: How do I add a package?

```bash
uv add package-name
```

For a specific version:
```bash
uv add package-name==1.2.3
uv add "package-name>=1.2,<2.0"
```

For development only:
```bash
uv add --dev pytest
```

See Part 4: Adding Dependencies.

---

### Q: How do I know what version to use?

Check PyPI: https://pypi.org/search

```bash
# Latest version (default)
uv add requests

# Specific version
uv add requests==2.31.0

# Latest compatible with Python 3.10+
uv add "requests; python_version>='3.10'"
```

---

### Q: How do I update a dependency?

Reinstall it:
```bash
uv add --upgrade package-name
```

Or just add the new version:
```bash
uv add package-name==2.0.0
```

---

### Q: What's the difference between `pyproject.toml` and `uv.lock`?

| File | Purpose | Edit? |
|------|---------|-------|
| `pyproject.toml` | You specify minimum requirements | ✅ Yes |
| `uv.lock` | Exact versions used | ❌ No (auto-generated) |

Example:
- `pyproject.toml`: "I need pandas version 2.0 or newer"
- `uv.lock`: "I used pandas 2.0.3 and numpy 1.24.1"

---

### Q: How do I share my dependencies with a colleague?

They get `uv.lock` automatically when they clone your project:

```bash
# They clone the repo
git clone your-project

# They sync dependencies
cd your-project
uv sync

# They get exact same versions as you
```

No manual work needed.

---

### Q: What if I delete `.venv` by accident?

No problem:
```bash
uv sync
```

Everything is recreated from `uv.lock` exactly.

---

### Q: How do I see what dependencies I have?

Show dependency tree:
```bash
uv tree
```

Show installed packages:
```bash
uv pip list
```

Check a specific file:
```bash
cat pyproject.toml
```

---

## Python Versions

### Q: How do I use a specific Python version?

**Install it:**
```bash
uv python install 3.12
```

**Set for this project:**
```bash
uv python pin 3.12
```

**Run with specific version:**
```bash
uv run --python 3.11 python script.py
```

See Part 5: Working With Python Versions.

---

### Q: Can I have multiple Python versions?

Yes:
```bash
uv python install 3.10 3.11 3.12
uv python list
```

Each project uses what's specified in `.python-version`.

---

### Q: What Python versions are available?

See what's installed:
```bash
uv python list
```

See what's available:
```bash
uv python find
```

Install any:
```bash
uv python install 3.10
uv python install 3.11
uv python install 3.12
uv python install 3.13
```

---

### Q: My project needs Python 3.12, but I have 3.10

Just install 3.12:
```bash
uv python install 3.12
uv python pin 3.12

# Now when you run code
uv run python --version
# Python 3.12.x
```

Your other projects aren't affected.

---

## Running Code

### Q: How do I run my Python code?

With uv (recommended):
```bash
uv run python src/myproject/main.py
```

With a script file:
```bash
uv run my-script.py
```

With a command:
```bash
uv run python -c "print('Hello')"
```

**Never do:**
```bash
python my-script.py  # Missing packages!
```

See Part 6: Running Code.

---

### Q: Do I need to activate the virtual environment?

No, not with uv:

```bash
# Old way (don't do this)
source .venv/bin/activate
python script.py
deactivate

# uv way (do this)
uv run python script.py
```

uv handles activation automatically.

---

### Q: How do I write a quick script with dependencies?

Use a script with inline dependencies:

```python
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "requests>=2.31.0",
#     "pandas>=2.0.0",
# ]
# ///

import requests
import pandas as pd

response = requests.get("https://api.example.com")
df = pandas.DataFrame(response.json())
print(df)
```

Run it:
```bash
uv run script.py
```

No virtual environment setup needed!

See Part 6: Running Scripts.

---

### Q: How do I test my code?

Install pytest:
```bash
uv add --dev pytest
```

Write tests in `tests/`:
```python
def test_something():
    assert True
```

Run tests:
```bash
uv run pytest
```

---

## Tools

### Q: What's the difference between libraries and tools?

| Aspect | Library | Tool |
|--------|---------|------|
| How you use | `import` in code | Run from terminal |
| Install with | `uv add` | `uv tool install` |
| For whole project | ✅ Yes | ❌ No (global) |
| Examples | pandas, requests | black, pytest, jupyter |

See Part 7: Tools & Utilities.

---

### Q: How do I try a tool without installing it?

Use `uvx`:
```bash
uvx black my-file.py
uvx ruff check .
uvx httpie GET https://example.com
```

Tool downloads, runs, and cleans up. Nothing stays installed.

---

### Q: How do I install a tool I use every day?

```bash
uv tool install black
```

Now use it anywhere:
```bash
black my-file.py
```

See what's installed:
```bash
uv tool list
```

---

### Q: How do I update my tools?

```bash
uv tool update black          # Update one tool
uv tool update --all          # Update all tools
```

---

## Working with Others

### Q: How do I contribute to an open-source project?

1. Clone the project:
   ```bash
   git clone project-url
   cd project
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

3. Make your changes:
   ```bash
   # Edit code...
   ```

4. Test your changes:
   ```bash
   uv run pytest
   ```

5. Check code quality:
   ```bash
   uv run ruff check .
   uv run black --check .
   ```

6. Commit and push:
   ```bash
   git add .
   git commit -m "Fix: description"
   git push origin branch-name
   ```

See Part 10: Decision Trees & Workflows (Contributing).

---

### Q: How do I handle API keys and secrets?

**Never commit them.** Use `.env` files:

1. Create `.env`:
   ```
   OPENAI_API_KEY=sk-...
   DATABASE_URL=postgres://...
   ```

2. Add to `.gitignore`:
   ```
   .env
   .env.local
   ```

3. Load in code:
   ```python
   from dotenv import load_dotenv
   import os
   
   load_dotenv()
   api_key = os.getenv("OPENAI_API_KEY")
   ```

4. Install python-dotenv:
   ```bash
   uv add python-dotenv
   ```

See Part 14: Real-World Examples (Chatbot).

---

### Q: How do I deploy my project?

**Option 1: Export to requirements.txt**
```bash
uv export > requirements.txt
# Use with traditional deployment tools
```

**Option 2: Docker**
```dockerfile
FROM python:3.12

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
WORKDIR /app
COPY . .

RUN uv sync --no-dev
CMD ["uv", "run", "python", "src/app/main.py"]
```

**Option 3: Cloud deployment**
Most cloud platforms support Python. Just include:
- `pyproject.toml`
- `uv.lock`
- `.python-version`

See Appendix: Troubleshooting & FAQ (Can I deploy?).

---

## Troubleshooting

### Q: I get "ModuleNotFoundError" when running code

**Problem:** Package isn't installed.

**Solution:**
```bash
# Install the package
uv add requests

# Make sure you're using uv run
uv run python my-script.py  # ✅ Correct
python my-script.py          # ❌ Wrong
```

See Appendix: Troubleshooting & FAQ.

---

### Q: Virtual environment is broken

**Problem:** Files got corrupted or deleted.

**Solution:**
```bash
rm -rf .venv          # Delete broken environment
uv sync               # Recreate from uv.lock
```

Everything is restored from the lock file.

---

### Q: "command not found: uv"

**Problem:** uv isn't installed or not in PATH.

**Solution:**
```bash
# Reinstall uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or add to PATH manually
export PATH="$HOME/.local/bin:$PATH"
```

---

### Q: "Package version not found"

**Problem:** Version doesn't exist or typo in name.

**Solution:**
```bash
# Check correct name on PyPI
# https://pypi.org/search/?q=package-name

# Use correct name and version
uv add requests==2.31.0
```

---

### Q: My colleague gets different versions than me

**Problem:** They're not using `uv.lock`.

**Solution:**
```bash
# Make sure they run:
uv sync

# Not:
uv add  # This adds, doesn't sync to lock file versions
```

The lock file ensures identical environments.

---

## Performance

### Q: Why is uv so fast?

uv is written in **Rust** instead of Python. Rust is compiled to machine code, not interpreted. This makes:
- Downloading faster
- Installing faster
- Resolving dependencies faster
- Everything else faster

See Part 1: Why Does uv Exist?

---

### Q: How much does caching help?

A lot. First install:
```bash
uv add requests
# 2 seconds (downloads from internet)
```

Second install of same package:
```bash
uv add requests
# 50ms (loaded from cache)
```

40x faster because it's cached.

See Part 9: Caching.

---

### Q: Should I clean my cache?

You can, but it's safe to leave:
```bash
uv cache clean       # Remove all cached packages
uv cache prune       # Remove unused packages only
```

After cleaning, packages are re-downloaded next time (slower). Only clean if you're short on disk space.

---

## Advanced Questions

### Q: What's a workspace?

A monorepo with multiple projects sharing one lock file:

```
monorepo/
├── packages/
│   ├── api/
│   │   └── pyproject.toml
│   ├── cli/
│   │   └── pyproject.toml
│   └── shared/
│       └── pyproject.toml
└── pyproject.toml  # Root workspace config
```

See Part 9: Workspaces.

---

### Q: How do I publish a package to PyPI?

1. Update `pyproject.toml` with metadata
2. Write your code
3. Build the package:
   ```bash
   uv build
   ```
4. Publish:
   ```bash
   uv publish
   ```

See Part 9: Publishing Packages.

---

### Q: Can I use uv with Docker?

Yes, easily:

```dockerfile
FROM python:3.12
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
WORKDIR /app
COPY . .
RUN uv sync --no-dev
CMD ["uv", "run", "python", "src/app/main.py"]
```

See Appendix: Can I deploy my uv project?

---

### Q: How do I configure uv?

In `pyproject.toml`:

```toml
[tool.uv]
index-url = "https://pypi.org/simple"
trusted-hosts = ["internal-pypi.company.com"]
```

Or as environment variables:
```bash
export UV_PYTHON=3.12
export UV_INDEX=https://custom-pypi.example.com
```

See Part 9: Configuration.

---

## Where to Get More Help

- **Official Docs:** https://docs.astral.sh/uv/
- **GitHub Issues:** https://github.com/astral-sh/uv/issues
- **Discord Community:** https://discord.com/invite/astral-sh
- **This Handbook:** uv_beginners_handbook.md
- **Glossary:** glossary.md

---

**Last Updated:** June 2026  
**For uv version:** 0.5.x and above