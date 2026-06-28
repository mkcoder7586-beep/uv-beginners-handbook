# uv Learning Path: Structured Guide by Skill Level

Progress through uv from beginner to proficient at your own pace.

---

## Level 1: Absolute Beginner (30 minutes)

**Goal:** Get uv installed and run your first project.

### What you'll learn:
- What uv is and why it exists
- How to install uv
- Create and run a simple project

### Handbook sections to read:
1. Part 1: The Foundations (skim)
2. Part 2: Getting Started (read)

### Activities:

**Activity 1.1: Install uv** (5 min)
```bash
# Follow installation for your OS
curl -LsSf https://astral.sh/uv/install.sh | sh  # macOS/Linux
# OR
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"  # Windows

# Verify
uv --version
```

✅ Success: You see version number

---

**Activity 1.2: Create first project** (10 min)
```bash
uv init hello-world
cd hello-world
```

Explore what was created:
```bash
ls -la
cat pyproject.toml
cat .python-version
```

✅ Success: Folder structure looks right

---

**Activity 1.3: Run code** (10 min)
```bash
# Check the code
cat src/hello_world/main.py

# Run it
uv run python src/hello_world/main.py

# Or run a simple command
uv run python -c "print('Hello, uv!')"
```

✅ Success: Code runs without errors

---

### Knowledge check:
- [ ] What does uv do?
- [ ] How do I install it?
- [ ] What files does `uv init` create?
- [ ] How do I run code with uv?

### Next level: Once you've completed all activities, move to Level 2

---

## Level 2: Beginner (1 hour)

**Goal:** Manage dependencies and understand virtual environments.

### What you'll learn:
- What dependencies are
- How to add/remove packages
- What virtual environments do
- The difference between `.venv` and `uv.lock`

### Handbook sections to read:
1. Part 3: Key Concepts Explained (read)
2. Part 4: Creating & Managing Projects (read)

### Activities:

**Activity 2.1: Add a dependency** (15 min)

In your hello-world project:
```bash
uv add requests
```

Check what changed:
```bash
cat pyproject.toml
# See 'requests' in dependencies

cat uv.lock
# See exact versions
```

✅ Success: `pyproject.toml` updated with requests

---

**Activity 2.2: Use the package** (15 min)

Edit `src/hello_world/main.py`:
```python
import requests

response = requests.get("https://api.example.com")
print(f"Status: {response.status_code}")
```

Run it:
```bash
uv run python src/hello_world/main.py
```

✅ Success: Code runs with the package

---

**Activity 2.3: Understand the virtual environment** (15 min)

```bash
# See what's in the virtual environment
ls -la .venv

# List installed packages
uv pip list

# See dependency tree
uv tree
```

✅ Success: You understand the venv structure

---

**Activity 2.4: Remove a dependency** (15 min)

```bash
uv remove requests
cat pyproject.toml  # requests is gone

# Try running the old code
# It will fail because requests isn't installed anymore
uv run python src/hello_world/main.py  # Error!

# Add it back
uv add requests
uv run python src/hello_world/main.py  # Works again
```

✅ Success: You can add and remove packages

---

### Knowledge check:
- [ ] What's a dependency?
- [ ] How do I add a package?
- [ ] What's the difference between `pyproject.toml` and `uv.lock`?
- [ ] What's a virtual environment and why does it matter?
- [ ] What's in `.venv`?

### Next level: Once comfortable with these, move to Level 3

---

## Level 3: Intermediate (2 hours)

**Goal:** Manage projects professionally with proper structure and Python versions.

### What you'll learn:
- Proper project structure
- Development vs production dependencies
- Python version management
- Running tests
- Basic code formatting/linting

### Handbook sections to read:
1. Part 5: Working With Python Versions (read)
2. Part 6: Running Code (read)
3. Part 7: Tools & Utilities (read)
4. Part 12: Cheat Sheets (reference)

### Activities:

**Activity 3.1: Create professional project** (20 min)

```bash
cd ..
uv init data-processor
cd data-processor
uv python pin 3.12
```

Create proper structure:
```bash
mkdir -p tests
touch tests/__init__.py
touch tests/test_main.py

# Create a real module
mkdir -p src/data_processor
# src/data_processor/__init__.py already exists
echo "def process(data): return data" > src/data_processor/processor.py
```

✅ Success: Professional structure created

---

**Activity 3.2: Add dev dependencies** (15 min)

```bash
# Add testing and formatting tools
uv add --dev pytest black ruff

# Verify they're separate
cat pyproject.toml
# Should show dev dependencies in different section
```

✅ Success: Dev tools installed separately

---

**Activity 3.3: Write and run tests** (20 min)

Edit `tests/test_main.py`:
```python
import pytest
from data_processor.processor import process

def test_process():
    result = process([1, 2, 3])
    assert result == [1, 2, 3]

def test_empty():
    result = process([])
    assert result == []
```

Run tests:
```bash
uv run pytest
uv run pytest -v  # Verbose
```

✅ Success: Tests run and pass

---

**Activity 3.4: Format and lint code** (15 min)

Write some intentionally bad code in `src/data_processor/processor.py`:
```python
def process(data):return data
x=5
unused_var = 10
```

Format it:
```bash
uv run black .
```

Check it:
```bash
uv run ruff check .
```

✅ Success: Code is formatted and checked

---

**Activity 3.5: Try tools with uvx** (10 min)

Try tools temporarily:
```bash
uvx httpie --version
uvx black --version
```

These download and run without installing.

✅ Success: You understand uvx vs tool install

---

### Knowledge check:
- [ ] What's proper project structure?
- [ ] How do I separate dev and production dependencies?
- [ ] How do I set and use a specific Python version?
- [ ] How do I write and run tests?
- [ ] How do I format and check code?
- [ ] What's the difference between `uvx` and `uv tool install`?

### Next level: Once comfortable, move to Level 4

---

## Level 4: Advanced (3 hours)

**Goal:** Use uv professionally for real projects, collaboration, and deployment.

### What you'll learn:
- Project publishing and distribution
- Git workflows with uv
- Docker and deployment
- Workspaces for monorepos
- Advanced configuration

### Handbook sections to read:
1. Part 9: Advanced Topics (read)
2. Part 10: Decision Trees & Workflows (read)
3. Part 14: Real-World Examples (read)
4. Best Practices guide (read)

### Activities:

**Activity 4.1: Set up Git properly** (20 min)

In your project:
```bash
git init
```

Create `.gitignore`:
```
.venv/
__pycache__/
*.pyc
.pytest_cache/
.coverage
.env
```

Commit the right files:
```bash
git add pyproject.toml uv.lock .python-version README.md src/ tests/
git commit -m "Initial project setup"

# Don't commit:
git status  # Should show .venv/ and __pycache__/ as untracked
```

✅ Success: Git configured correctly

---

**Activity 4.2: Create real example project** (45 min)

Create a weather API project:

```bash
cd ..
uv init weather-api
cd weather-api

uv add fastapi uvicorn requests
uv add --dev pytest httpx
```

Create `src/weather_api/main.py`:
```python
from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/weather/{city}")
def get_weather(city: str):
    # In real project, use actual API
    return {"city": city, "temp": 72, "condition": "sunny"}

@app.get("/health")
def health():
    return {"status": "ok"}
```

Create `tests/test_main.py`:
```python
from fastapi.testclient import TestClient
from weather_api.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_weather():
    response = client.get("/weather/London")
    assert response.status_code == 200
    assert "city" in response.json()
```

Test it:
```bash
uv run pytest
uv run uvicorn src.weather_api.main:app --reload
```

✅ Success: Real API project works

---

**Activity 4.3: Build for distribution** (15 min)

Build a package:
```bash
uv build
ls -la dist/
# You have .whl and .tar.gz files
```

Understand what they are:
```bash
unzip -l dist/*.whl | head  # Wheel file
```

✅ Success: Package built

---

**Activity 4.4: Create documentation** (15 min)

Create `README.md`:
```markdown
# Weather API

Simple weather API with FastAPI.

## Installation

```bash
uv sync
```

## Running

```bash
uv run uvicorn src.weather_api.main:app --reload
```

## Testing

```bash
uv run pytest -v
```

## Development

Format code:
```bash
uv run black .
uv run ruff check --fix .
```
```

✅ Success: Documentation created

---

**Activity 4.5: Setup pre-commit hooks** (10 min)

```bash
uv add --dev pre-commit

# Create .pre-commit-config.yaml with basic hooks
# This ensures code is formatted before commits
```

✅ Success: Pre-commit configured

---

**Activity 4.6: Understand deployment options** (15 min)

Create `Dockerfile`:
```dockerfile
FROM python:3.12

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
WORKDIR /app
COPY . .

RUN uv sync --no-dev

CMD ["uv", "run", "uvicorn", "src.weather_api.main:app", "--host", "0.0.0.0"]
```

Understand how it works:
- Installs uv
- Copies your project
- Installs dependencies from uv.lock
- Runs your app

✅ Success: Docker setup understood

---

### Knowledge check:
- [ ] How do I set up Git correctly with uv?
- [ ] How do I use `uv.lock` for reproducibility?
- [ ] How do I build a package?
- [ ] How do I set up pre-commit hooks?
- [ ] How do I deploy with Docker?
- [ ] What are the key files to commit?

### Next level: Congratulations! You're advanced.

---

## Level 5: Expert (Self-paced)

**Goal:** Master advanced patterns and help others.

### Topics to explore:
1. Workspaces for large projects (monorepos)
2. Custom package indexes and private packages
3. CI/CD integration with uv
4. Performance optimization
5. Contributing to open-source projects using uv

### Resources:
- Official documentation: https://docs.astral.sh/uv/
- GitHub repository: https://github.com/astral-sh/uv
- Community: https://discord.com/invite/astral-sh

### Things to do:
- [ ] Set up a workspace with multiple packages
- [ ] Publish a package to PyPI
- [ ] Configure CI/CD pipeline with GitHub Actions
- [ ] Contribute to an open-source project
- [ ] Help others learn uv

---

## Learning Resources by Topic

### Virtual Environments & Dependencies
- Handbook Part 3: Key Concepts
- Handbook Part 4: Managing Projects
- FAQ: Virtual environment questions
- Best Practices: Dependency management

### Python Version Management
- Handbook Part 5: Python Versions
- FAQ: Python version questions
- Common Errors: Python version errors

### Running Code & Projects
- Handbook Part 6: Running Code
- Handbook Part 14: Real-World Examples
- Cheat Sheet: Running Code

### Tools & Development
- Handbook Part 7: Tools & Utilities
- Best Practices: Development workflow
- Best Practices: Testing

### Professional Usage
- Handbook Part 9: Advanced Topics
- Handbook Part 10: Workflows
- Best Practices: Project organization
- Best Practices: Deployment

### Troubleshooting
- Common Errors: All error types
- FAQ: Troubleshooting section
- Handbook Appendix: FAQ

---

## Quick Reference by Goal

### "I want to start coding"
1. Level 1, Activity 1.1-1.3
2. Level 2, Activity 2.1-2.2

### "I want to write a real project"
1. Complete Level 3
2. Read Best Practices

### "I want to share my project"
1. Level 4, Activity 4.1
2. Best Practices: Git & Collaboration

### "I want to deploy"
1. Level 4, Activity 4.6
2. Best Practices: Deployment

### "I'm stuck on an error"
1. Check Common Errors
2. Check FAQ
3. Read Handbook Appendix

### "I want to be an expert"
1. Complete all levels
2. Explore Level 5 resources
3. Read all supplementary guides

---

## Estimated Time Investment

- **Level 1:** 30 minutes
- **Level 2:** 1 hour
- **Level 3:** 2 hours
- **Level 4:** 3 hours
- **Level 5:** Ongoing, self-paced

**Total time to proficiency:** ~6-8 hours

After this, you'll be comfortable with uv for any project.

---

## Key Milestones

✅ **Level 1 Complete:** Can create and run projects
✅ **Level 2 Complete:** Can manage dependencies
✅ **Level 3 Complete:** Can work on real projects
✅ **Level 4 Complete:** Can work professionally
✅ **Level 5 Complete:** Can help others and tackle any challenge

---

## Recommended Study Order

1. Read Handbook introduction (Part 1)
2. Do Level 1 activities
3. Do Level 2 activities while reading Parts 3-4
4. Do Level 3 activities while reading Parts 5-7
5. Do Level 4 activities while reading Parts 9-14
6. Read all supplementary guides (glossary, FAQ, best practices, etc.)
7. Explore Level 5 topics as needed

---

**Last Updated:** June 2026  
**For uv version:** 0.5.x and above