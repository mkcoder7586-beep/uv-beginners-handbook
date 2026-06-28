# Recommended Tools & Ecosystem Guide

Essential and complementary tools that work perfectly with uv.

---

## Code Quality & Formatting

### Black (Code Formatter)

**What it does:** Formats your Python code consistently

**Install:**
```bash
uv add --dev black
```

**Use:**
```bash
uv run black .           # Format all code
uv run black file.py     # Format specific file
uv run black --check .   # Check without modifying
```

**Config in `pyproject.toml`:**
```toml
[tool.black]
line-length = 100
target-version = ['py312']
```

**Why use it:**
- Consistent code style
- Fewer debates about formatting
- Automatic fixing
- Industry standard

**When to use with uv:**
```bash
# In development
uv run black .

# In pre-commit hook
# In CI/CD pipeline
# Before committing
```

---

### Ruff (Linter)

**What it does:** Finds code quality issues and style violations

**Install:**
```bash
uv add --dev ruff
```

**Use:**
```bash
uv run ruff check .         # Find issues
uv run ruff check --fix .   # Auto-fix issues
uv run ruff format .        # Format code
```

**Config in `pyproject.toml`:**
```toml
[tool.ruff]
line-length = 100
target-version = "py312"
select = ["E", "F", "W"]  # Which rules to check
```

**Why use it:**
- Finds bugs and issues
- Very fast (written in Rust like uv)
- Auto-fixable problems
- Better than pylint for many users

---

### mypy (Type Checking)

**What it does:** Checks if your type hints are correct

**Install:**
```bash
uv add --dev mypy
```

**Use:**
```bash
uv run mypy src/           # Type check all code
uv run mypy src/main.py    # Type check specific file
```

**Example:**
```python
def greet(name: str) -> str:
    return f"Hello, {name}"

greet("Alice")        # ✅ OK
greet(123)           # ❌ mypy catches this error
```

**Config in `pyproject.toml`:**
```toml
[tool.mypy]
python_version = "3.12"
warn_return_any = true
warn_unused_configs = true
```

**Why use it:**
- Catch type errors before runtime
- Better IDE support
- Prevents entire classes of bugs
- Optional, but highly recommended

---

## Testing

### pytest (Testing Framework)

**What it does:** Runs tests and reports results

**Install:**
```bash
uv add --dev pytest
```

**Use:**
```bash
uv run pytest                    # Run all tests
uv run pytest -v                # Verbose output
uv run pytest --cov=src         # With coverage
uv run pytest tests/test_main.py # Specific file
```

**Example test:**
```python
# tests/test_main.py
def test_addition():
    assert 2 + 2 == 4

def test_string():
    assert "hello".upper() == "HELLO"
```

**Config in `pyproject.toml`:**
```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
addopts = "-v --tb=short"
```

**Why use it:**
- Industry standard
- Easy to write tests
- Great reporting
- Integrates with CI/CD

**With uv:**
```bash
uv add --dev pytest
uv run pytest              # Run tests in dev environment
```

---

### pytest-cov (Coverage Reporting)

**What it does:** Reports how much of your code is tested

**Install:**
```bash
uv add --dev pytest-cov
```

**Use:**
```bash
uv run pytest --cov=src  # Show coverage percentage
uv run pytest --cov=src --cov-report=html  # Generate HTML report
```

**Why use it:**
- Know what's tested
- Find untested code paths
- Track coverage over time

---

### pytest-asyncio (Async Testing)

**What it does:** Tests async/await code

**Install:**
```bash
uv add --dev pytest-asyncio
```

**Use:**
```python
import pytest

@pytest.mark.asyncio
async def test_async_function():
    result = await async_function()
    assert result == expected
```

**Why use it:**
- Test FastAPI/async projects
- Simulate async behavior
- Required for modern Python apps

---

## Development Tools

### ipython (Enhanced Python Shell)

**What it does:** Better Python interactive shell

**Install:**
```bash
uv add --dev ipython
```

**Use:**
```bash
uv run ipython
In [1]: import pandas as pd
In [2]: df = pd.DataFrame({"a": [1, 2, 3]})
In [3]: df
```

**Why use it:**
- Better syntax highlighting
- Tab completion
- Magic commands
- Better for exploration

---

### Jupyter / JupyterLab (Notebooks)

**What it does:** Interactive notebooks for data exploration

**Install:**
```bash
uv add --dev jupyterlab
```

**Use:**
```bash
uv run jupyter lab
# Opens http://localhost:8888
```

**Why use it:**
- Data exploration
- Creating presentations
- Combining code and documentation
- Great for tutorials

**Best for:**
- Data science projects
- Research
- Demonstrations
- Learning

---

### Pre-commit (Git Hooks)

**What it does:** Runs checks before each commit

**Install:**
```bash
uv add --dev pre-commit
```

**Setup (`.pre-commit-config.yaml`):**
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
        args: [--fix]
```

**Install hooks:**
```bash
uv run pre-commit install
```

**Why use it:**
- Enforces standards automatically
- No bad commits slip through
- Saves time (run checks before pushing)
- Team consistency

---

## Web Frameworks

### FastAPI (Modern Web Framework)

**What it does:** Build fast web APIs

**Install:**
```bash
uv add fastapi uvicorn
uv add --dev pytest httpx
```

**Example:**
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello": "world"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```

**Run:**
```bash
uv run uvicorn main:app --reload
```

**Test:**
```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
```

**Why use with uv:**
- Modern, fast framework
- Built-in API documentation
- Great with uv for development
- Easy to deploy

---

### Flask (Lightweight Framework)

**What it does:** Build lightweight web apps

**Install:**
```bash
uv add flask
uv add --dev pytest
```

**Example:**
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
```

**Why use with uv:**
- Simpler than FastAPI
- Good for small projects
- Easy learning curve
- Long track record

---

### Django (Full Framework)

**What it does:** Build complete web applications

**Install:**
```bash
uv add django
```

**Usage:**
```bash
uv run django-admin startproject mysite
uv run manage.py runserver
```

**Why use with uv:**
- Batteries-included
- Large ecosystem
- Great for complex projects
- Mature and stable

---

## Data Science

### NumPy (Numerical Computing)

**What it does:** Fast numerical array operations

**Install:**
```bash
uv add numpy
```

**Use:**
```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
mean = np.mean(arr)
```

**Why use with uv:**
- Foundation for data science
- Very fast
- Foundation for pandas, matplotlib
- Essential for ML

---

### pandas (Data Analysis)

**What it does:** DataFrames and data manipulation

**Install:**
```bash
uv add pandas
```

**Use:**
```python
import pandas as pd

df = pd.read_csv("data.csv")
result = df.groupby("category").sum()
```

**Why use with uv:**
- Industry standard for data
- Powerful data manipulation
- Easy CSV/Excel handling
- Great visualization integration

---

### matplotlib (Plotting)

**What it does:** Create plots and visualizations

**Install:**
```bash
uv add matplotlib
```

**Use:**
```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [1, 4, 9])
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
```

**Why use with uv:**
- Standard visualization
- Works with pandas
- Publication-quality plots
- Wide ecosystem

---

### scikit-learn (Machine Learning)

**What it does:** Machine learning algorithms

**Install:**
```bash
uv add scikit-learn
```

**Use:**
```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y)
clf = RandomForestClassifier()
clf.fit(X_train, y_train)
```

**Why use with uv:**
- Most popular ML library
- Easy to learn
- Great documentation
- Compatible with pandas

---

## API & HTTP Tools

### requests (HTTP Client)

**What it does:** Make HTTP requests

**Install:**
```bash
uv add requests
```

**Use:**
```python
import requests

response = requests.get("https://api.example.com/data")
data = response.json()
```

**Why use with uv:**
- Simple HTTP requests
- Industry standard
- Great error handling
- Session management

---

### httpx (Modern HTTP Client)

**What it does:** Modern HTTP client with async support

**Install:**
```bash
uv add httpx
```

**Use:**
```python
import httpx

# Sync
with httpx.Client() as client:
    response = client.get("https://api.example.com")

# Async
async with httpx.AsyncClient() as client:
    response = await client.get("https://api.example.com")
```

**Why use with uv:**
- Modern alternative to requests
- Built-in async support
- Type hints
- Better for FastAPI projects

---

## Environment & Configuration

### python-dotenv (Environment Variables)

**What it does:** Load environment variables from .env file

**Install:**
```bash
uv add python-dotenv
```

**Use:**
```python
from dotenv import load_dotenv
import os

load_dotenv()  # Load from .env

api_key = os.getenv("API_KEY")
database_url = os.getenv("DATABASE_URL")
```

**.env file:**
```
API_KEY=sk-123456
DATABASE_URL=postgres://localhost/db
DEBUG=true
```

**Why use with uv:**
- Keep secrets out of code
- Different configs per environment
- Easy development setup

---

### pydantic (Data Validation)

**What it does:** Validate and parse data with Python types

**Install:**
```bash
uv add pydantic
```

**Use:**
```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    is_available: bool

# Validates automatically
item = Item(name="Widget", price=10.99, is_available=True)
item.model_dump_json()  # JSON serialization
```

**Why use with uv:**
- Type-safe data validation
- Built-in with FastAPI
- JSON serialization
- Error messages

---

## Utility Tools

### httpie (CLI HTTP Client)

**What it does:** User-friendly HTTP client for terminal

**Install temporarily:**
```bash
uvx httpie GET https://api.example.com
```

**Or install permanently:**
```bash
uv tool install httpie
```

**Use:**
```bash
http GET https://jsonplaceholder.typicode.com/posts/1
http POST https://api.example.com name=John age:=30
```

**Why use with uv:**
- Better than curl
- Easy JSON handling
- Great for testing APIs
- Beautiful output

---

### rich (Terminal Output)

**What it does:** Rich formatting and progress bars in terminal

**Install:**
```bash
uv add rich
```

**Use:**
```python
from rich.console import Console
from rich.progress import track

console = Console()
console.print("[bold blue]Hello[/bold blue] [red]World[/red]!")

for item in track([1, 2, 3], description="Processing..."):
    # do something
```

**Why use with uv:**
- Beautiful terminal output
- Progress bars
- Tables and formatting
- Makes CLIs professional

---

### Click (CLI Building)

**What it does:** Create command-line interfaces

**Install:**
```bash
uv add click
```

**Use:**
```python
import click

@click.command()
@click.option('--name', prompt='Your name')
def hello(name):
    click.echo(f'Hello {name}!')

if __name__ == '__main__':
    hello()
```

**Why use with uv:**
- Easy CLI creation
- Auto-generated help
- Type validation
- Popular and stable

---

## Typical Project Setup

### Web API Project
```bash
uv add fastapi uvicorn sqlalchemy pydantic
uv add --dev pytest pytest-asyncio httpx black ruff mypy
```

### Data Science Project
```bash
uv add pandas numpy matplotlib scikit-learn
uv add --dev jupyter jupyterlab pytest black ruff
```

### CLI Tool Project
```bash
uv add click python-dotenv rich
uv add --dev pytest black ruff mypy
```

### Web App Project
```bash
uv add flask sqlalchemy
uv add --dev pytest black ruff mypy
```

### Library/Package
```bash
# Minimal dependencies
uv add --dev pytest black ruff mypy sphinx
```

---

## Tools By Category

### Testing & Quality
| Tool | Purpose |
|------|---------|
| pytest | Testing framework |
| pytest-cov | Coverage reporting |
| pytest-asyncio | Async testing |
| black | Code formatting |
| ruff | Linting |
| mypy | Type checking |
| pre-commit | Git hooks |

### Data Science
| Tool | Purpose |
|------|---------|
| numpy | Numerical computing |
| pandas | Data analysis |
| matplotlib | Plotting |
| scikit-learn | Machine learning |
| jupyter | Notebooks |

### Web Development
| Tool | Purpose |
|------|---------|
| fastapi | Modern API framework |
| flask | Lightweight framework |
| django | Full framework |
| sqlalchemy | Database ORM |
| pydantic | Data validation |

### Utilities
| Tool | Purpose |
|------|---------|
| python-dotenv | Environment variables |
| click | CLI building |
| rich | Terminal formatting |
| httpie | HTTP testing |
| requests | HTTP client |
| httpx | Modern HTTP client |

---

## Recommended Starter Setups

### Minimal Project
```bash
uv add --dev pytest black
```

### Professional Project
```bash
uv add --dev pytest pytest-cov black ruff mypy pre-commit
```

### Web API (FastAPI)
```bash
uv add fastapi uvicorn
uv add --dev pytest pytest-asyncio httpx black ruff mypy
```

### Data Science
```bash
uv add pandas numpy matplotlib scikit-learn
uv add --dev jupyter pytest black ruff
```

---

## Integration with uv

### Add to project:
```bash
uv add tool-name
```

### Add as dev dependency:
```bash
uv add --dev tool-name
```

### Try without installing:
```bash
uvx tool-name
```

### Install globally:
```bash
uv tool install tool-name
```

---

## Next Steps

1. **Start with basics:** black, ruff, pytest
2. **Add when needed:** Framework (fastapi/flask), data tools, etc.
3. **Explore:** Additional tools based on your project needs
4. **Standardize:** Pick tools and use them consistently

---

**Last Updated:** June 2026  
**For uv version:** 0.5.x and above