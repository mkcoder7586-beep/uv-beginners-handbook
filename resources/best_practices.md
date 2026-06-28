# uv Best Practices Guide

Professional patterns and anti-patterns for using uv effectively.

---

## Project Organization

### ✅ DO: Follow this directory structure

```
myproject/
├── .gitignore           # Git ignore file
├── .python-version      # Python version (commit this)
├── README.md            # Project documentation
├── pyproject.toml       # Project configuration (commit this)
├── uv.lock              # Dependency lock (commit this)
│
├── src/
│   └── myproject/       # Your package
│       ├── __init__.py
│       ├── main.py
│       └── utils.py
│
├── tests/               # Tests
│   ├── __init__.py
│   ├── test_main.py
│   └── test_utils.py
│
├── docs/                # Documentation
│   └── index.md
│
└── .venv/              # Virtual environment (don't commit)
```

**Why this structure:**
- `src/` keeps your code separate and importable
- `tests/` is discoverable by pytest
- Root configuration files are easy to find
- `.venv/` is auto-generated, not committed

---

### ❌ DON'T: Use bad directory structures

```
❌ myproject.py in root            # Avoid - conflicts with package name
❌ code/ folder with random files  # Avoid - unclear organization
❌ main.py at root                 # Avoid - hard to package later
❌ Nested .venv folders            # Avoid - hard to recreate
```

---

## Git Configuration

### ✅ DO: Commit these files

```bash
# In .gitignore, don't ignore these:
!pyproject.toml
!uv.lock
!.python-version
```

These ensure reproducibility.

---

### ✅ DO: Create proper .gitignore

```
# Virtual environment
.venv/
venv/
ENV/
env/

# Python cache
__pycache__/
*.pyc
*.pyo
*.pyd
.Python

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Environment variables
.env
.env.local
.env.*.local

# Project specific
dist/
build/
*.egg-info/
.pytest_cache/
.coverage
htmlcov/
```

---

### ❌ DON'T: Commit these files

```
.venv/              # Auto-generated
*.pyc               # Cache files
__pycache__/        # Python cache
.env                # Secrets!
dist/               # Build output
build/              # Build output
*.egg-info/         # Build output
```

---

## Dependency Management

### ✅ DO: Specify version ranges

```toml
# pyproject.toml

[project]
dependencies = [
    "requests>=2.28.0",          # At least 2.28
    "pandas>=1.5.0,<2.0.0",      # Between 1.5 and 2.0
    "numpy",                      # Latest compatible
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "black>=23.0",
    "ruff>=0.1.0",
]
```

**Why version ranges:**
- Allows bug fixes and security patches
- Avoids accidentally incompatible versions
- Stays flexible while being safe

---

### ✅ DO: Separate dev and production dependencies

```bash
# Production dependencies
uv add flask sqlalchemy

# Development only
uv add --dev pytest pytest-cov black ruff mypy

# Installation for production
uv sync --no-dev
```

**Why separation:**
- Production image is smaller
- Clear what's needed to run vs. develop
- Deploy without test dependencies

---

### ❌ DON'T: Install everything as production dependency

```toml
# ❌ Wrong - test tools in production
dependencies = [
    "flask",
    "pytest",
    "black",
    "ruff",
]
```

---

### ✅ DO: Use meaningful version constraints

```toml
# ✅ Good - allows patches and minor updates
"requests>=2.28.0"
"pandas>=1.5.0,<3.0.0"
"numpy>=1.20.0"

# ❌ Bad - too restrictive
"requests==2.28.0"

# ❌ Bad - too loose
"requests"
```

---

### ✅ DO: Keep uv.lock in Git

```bash
git add uv.lock
git commit -m "Add requests dependency"
git push
```

**Why:**
- Ensures everyone uses same versions
- CI/CD gets exact versions
- Production matches development

---

### ❌ DON'T: Manually edit uv.lock

```bash
# ❌ Wrong - don't do this
nano uv.lock
# Edit manually...
git add uv.lock

# ✅ Correct
uv add/remove packages
# uv.lock updates automatically
git add uv.lock
```

---

## Coding Standards

### ✅ DO: Use type hints

```python
# myproject/main.py
from typing import List, Dict

def process_data(items: List[str]) -> Dict[str, int]:
    """Count items."""
    return {item: len(item) for item in items}
```

Install type checker:
```bash
uv add --dev mypy
uv run mypy src/
```

---

### ✅ DO: Format code consistently

```bash
# Install formatter
uv add --dev black

# Format all code
uv run black .

# Check (don't modify)
uv run black --check .
```

Add to `pyproject.toml`:
```toml
[tool.black]
line-length = 100
```

---

### ✅ DO: Lint code for issues

```bash
# Install linter
uv add --dev ruff

# Check for issues
uv run ruff check .

# Auto-fix some issues
uv run ruff check --fix .
```

---

### ✅ DO: Write tests

```python
# tests/test_main.py
import pytest
from myproject.main import process_data

def test_process_data():
    result = process_data(["hi", "hello"])
    assert result["hi"] == 2
    assert result["hello"] == 5

def test_empty_list():
    assert process_data([]) == {}
```

Run tests:
```bash
uv run pytest
uv run pytest -v      # Verbose
uv run pytest -cov    # With coverage
```

---

### ✅ DO: Use consistent naming

```python
# ✅ Good
def calculate_average(numbers: List[float]) -> float:
    return sum(numbers) / len(numbers)

class DataProcessor:
    def process(self, data: Dict) -> Dict:
        ...

# ❌ Bad
def calc_avg(n):
    return sum(n) / len(n)

class dp:
    def p(self, d):
        ...
```

---

## Development Workflow

### ✅ DO: Create a Makefile for common tasks

```makefile
.PHONY: help install test format lint type check

help:
	@echo "Available commands:"
	@echo "  make install    Install dependencies"
	@echo "  make test       Run tests"
	@echo "  make format     Format code"
	@echo "  make lint       Lint code"
	@echo "  make type       Type check"
	@echo "  make check      Run all checks"

install:
	uv sync

test:
	uv run pytest -v

format:
	uv run black .

lint:
	uv run ruff check .

type:
	uv run mypy src/

check: lint type test
	@echo "All checks passed!"
```

Use it:
```bash
make test
make check
make format
```

---

### ✅ DO: Use pre-commit hooks (optional but recommended)

Create `.pre-commit-config.yaml`:
```yaml
repos:
  - repo: local
    hooks:
      - id: black
        name: black
        entry: black
        language: system
        types: [python]
      
      - id: ruff
        name: ruff
        entry: ruff check
        language: system
        types: [python]
```

Install pre-commit:
```bash
uv add --dev pre-commit
uv run pre-commit install
```

Now checks run before each commit automatically.

---

### ✅ DO: Use a README with setup instructions

```markdown
# My Project

Brief description of what it does.

## Installation

```bash
# Clone the repo
git clone https://github.com/yourname/myproject
cd myproject

# Install dependencies
uv sync

# Run tests
uv run pytest
```

## Development

Format code:
```bash
uv run black .
uv run ruff check --fix .
```

Run type checks:
```bash
uv run mypy src/
```
```

---

### ❌ DON'T: Commit generated files

```bash
# ❌ Don't commit these
.venv/
__pycache__/
*.pyc
dist/
build/
*.egg-info/
.pytest_cache/
.coverage
htmlcov/
```

---

## Testing

### ✅ DO: Organize tests logically

```
tests/
├── __init__.py
├── test_main.py           # Tests for main.py
├── test_utils.py          # Tests for utils.py
├── fixtures/
│   ├── __init__.py
│   └── sample_data.json   # Test data
└── integration/
    └── test_api.py        # Integration tests
```

---

### ✅ DO: Use descriptive test names

```python
# ✅ Good - clear what's being tested
def test_process_data_with_empty_list():
    assert process_data([]) == {}

def test_calculate_average_with_single_number():
    assert calculate_average([5]) == 5

# ❌ Bad - unclear
def test1():
    pass

def test_func():
    pass
```

---

### ✅ DO: Use fixtures for reusable data

```python
# tests/conftest.py
import pytest

@pytest.fixture
def sample_data():
    return {
        "name": "John",
        "age": 30,
        "emails": ["john@example.com"]
    }

# tests/test_processing.py
def test_with_sample(sample_data):
    result = process(sample_data)
    assert result is not None
```

---

## Python Version Management

### ✅ DO: Pin Python version

```bash
uv python pin 3.12
cat .python-version
# 3.12
```

Commit `.python-version`:
```bash
git add .python-version
git commit -m "Require Python 3.12"
```

---

### ✅ DO: Support multiple Python versions (if applicable)

In `pyproject.toml`:
```toml
[project]
requires-python = ">=3.10"  # Support 3.10+
```

Test with multiple versions:
```bash
uv python install 3.10 3.11 3.12
uv run --python 3.10 pytest
uv run --python 3.11 pytest
uv run --python 3.12 pytest
```

---

### ❌ DON'T: Pin patch version unnecessarily

```toml
# ❌ Too strict
requires-python = "==3.12.4"

# ✅ Better
requires-python = ">=3.10"
```

---

## Documentation

### ✅ DO: Document your project

```markdown
# MyProject

## What it does
Clear description of what your project does.

## Installation

```bash
uv sync
```

## Usage

```python
from myproject import main
main.process("data")
```

## Development

See [Development Guide](docs/development.md)

## License

MIT (or your license)
```

---

### ✅ DO: Document dependencies

In `pyproject.toml`:
```toml
[project]
description = "Clear description of what project does"
dependencies = [
    "requests>=2.28.0",  # HTTP library
    "pandas>=1.5.0",     # Data analysis
]
```

---

## Deployment

### ✅ DO: Use uv.lock for deterministic builds

```dockerfile
FROM python:3.12

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /app
COPY . .

# Use lock file for exact versions
RUN uv sync --no-dev

CMD ["uv", "run", "python", "src/app/main.py"]
```

---

### ✅ DO: Exclude dev dependencies from production

```bash
# Exclude dev dependencies in deployment
uv sync --no-dev
```

---

### ❌ DON'T: Use latest versions in production

```dockerfile
# ❌ Bad - gets latest versions each time
RUN pip install -r requirements.txt

# ✅ Good - exact versions from lock file
RUN uv sync --no-dev
```

---

## Collaboration

### ✅ DO: Communicate project setup clearly

In your README:
```markdown
## Prerequisites

- Python 3.10 or higher
- uv (install from https://astral.sh/uv)

## Setup

```bash
git clone repo-url
cd project
uv sync
```

## Running

```bash
uv run python -m myproject
uv run pytest
```
```

---

### ✅ DO: Make lock file conflicts easy to resolve

```bash
# If merge conflict in uv.lock
git checkout --theirs uv.lock
uv lock
git add uv.lock
git commit -m "Resolve uv.lock conflict"
```

---

### ❌ DON'T: Have different developers use different Python versions

```bash
# ❌ Inconsistent
Developer 1: Python 3.10
Developer 2: Python 3.11
Developer 3: Python 3.12

# ✅ Consistent
# .python-version specifies 3.12 for everyone
```

---

## Security

### ✅ DO: Keep .env secrets out of Git

```bash
# .gitignore
.env
.env.local
```

```python
# Load from .env
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")
```

---

### ✅ DO: Update dependencies regularly

```bash
# Check for updates
uv tree

# Update all
uv add --upgrade

# Or specific package
uv add --upgrade requests
```

---

### ✅ DO: Pin versions for security-critical dependencies

```toml
# If using deprecated library, pin exact version
dependencies = [
    "critical-library==2.0.0",  # Exact version for compatibility
    "requests>=2.28.0",          # Flexible for others
]
```

---

### ❌ DON'T: Commit API keys or passwords

```
# ❌ Never do this
API_KEY=sk-abc123def456
DATABASE_PASSWORD=supersecret

# ✅ Use .env (in .gitignore)
API_KEY=sk-abc123def456
```

---

## Performance Tips

### ✅ DO: Use cached builds during development

First run (slow):
```bash
uv sync
# Downloads and installs everything
```

Subsequent runs (fast):
```bash
uv sync
# Uses cache - much faster
```

---

### ✅ DO: Export to requirements.txt if needed for compatibility

```bash
uv export > requirements.txt
# For tools that don't understand pyproject.toml
```

---

### ✅ DO: Clean cache periodically

```bash
# Remove unused cached packages
uv cache prune

# Or full clean if needed
uv cache clean
```

---

## Monorepos (Advanced)

### ✅ DO: Use workspaces for monorepos

```
mycompany/
├── pyproject.toml          # Root workspace config
├── uv.lock                 # Shared lock file
│
└── packages/
    ├── api/
    │   ├── src/
    │   └── pyproject.toml
    ├── cli/
    │   ├── src/
    │   └── pyproject.toml
    └── shared/
        ├── src/
        └── pyproject.toml
```

In root `pyproject.toml`:
```toml
[tool.uv]
workspace = [
    {path = "packages/api"},
    {path = "packages/cli"},
    {path = "packages/shared"},
]
```

---

## Checklist for New Projects

Use this checklist when starting a new project:

- [ ] Run `uv init myproject`
- [ ] Run `uv python pin 3.12` (or your version)
- [ ] Create `.gitignore` with proper entries
- [ ] Add necessary dependencies with `uv add`
- [ ] Commit `pyproject.toml`, `uv.lock`, `.python-version`
- [ ] Create `src/myproject/` structure
- [ ] Create `tests/` directory with `test_*.py` files
- [ ] Create `README.md` with setup instructions
- [ ] Install dev tools: `uv add --dev pytest black ruff mypy`
- [ ] Create `Makefile` for common commands
- [ ] Set up pre-commit hooks (optional)
- [ ] Test with: `uv run pytest`
- [ ] Format with: `uv run black .`
- [ ] Lint with: `uv run ruff check .`

---

**Last Updated:** June 2026  
**For uv version:** 0.5.x and above