# The Complete Beginner's Handbook for uv
## A Practical Guide to the Fastest Python Package Manager

---


<!-- HANDBOOK_VERSION: 1.0.0 -->
<!-- LAST_UPDATED: June 28, 2026 -->
<!-- TOTAL_PARTS: 14 -->
<!-- ESTIMATED_READ_TIME: 2-3 hours -->

---

## 🗺️ Quick Navigation

**Jump to a Section:**
- 🚀 [Quick Start](#introduction--what-youll-learn) — Get up and running in 5 minutes
- 📚 [Part 1: Foundations](#part-1-the-foundations) — What is uv and why?
- 🛠️ [Part 2: Getting Started](#part-2-getting-started) — Install and first command
- 💡 [Part 3: Key Concepts](#part-3-key-concepts-explained) — How uv works
- 📁 [Part 4: Projects](#part-4-creating--managing-projects) — Create and manage
- 🐍 [Part 5: Python Versions](#part-5-working-with-python-versions) — Different versions
- ▶️ [Part 6: Running Code](#part-6-running-code) — Execute safely
- 🛠️ [Part 7: Tools](#part-7-tools--utilities) — CLI tools
- 📦 [Part 8: Pip Interface](#part-8-the-pip-interface) — Traditional workflows
- ⚙️ [Part 9: Advanced](#part-9-advanced-topics) — Workspaces, publishing
- 🌳 [Part 10: Workflows](#part-10-decision-trees--workflows) — Decision trees
- 📖 [Part 11: Commands](#part-11-command-reference) — Complete reference
- 📝 [Part 12: Cheat Sheets](#part-12-cheat-sheets) — Quick guides
- 📊 [Part 13: Comparisons](#part-13-comparison-tables) — vs other tools
- 🎯 [Part 14: Examples](#part-14-real-world-examples) — Real projects
- 🆘 [Troubleshooting](#appendix-troubleshooting--faq) — Common problems


## Table of Contents

1. [Introduction & What You'll Learn](#introduction--what-youll-learn)
2. [Part 1: The Foundations](#part-1-the-foundations)
   - [What is Python?](#what-is-python)
   - [What is a Package Manager?](#what-is-a-package-manager)
   - [Why Does uv Exist?](#why-does-uv-exist)
   - [What Problem Does uv Solve?](#what-problem-does-uv-solve)
3. [Part 2: Getting Started](#part-2-getting-started)
   - [Installation](#installation)
   - [Verifying Your Installation](#verifying-your-installation)
   - [Your First Command](#your-first-command)
4. [Part 3: Key Concepts Explained](#part-3-key-concepts-explained)
   - [Virtual Environments](#virtual-environments)
   - [Dependencies](#dependencies)
   - [Lock Files](#lock-files)
   - [Packages and Libraries](#packages-and-libraries)
5. [Part 4: Creating & Managing Projects](#part-4-creating--managing-projects)
   - [Initializing a New Project](#initializing-a-new-project)
   - [Project Structure](#project-structure)
   - [Adding Dependencies](#adding-dependencies)
   - [Removing Dependencies](#removing-dependencies)
   - [Viewing Your Project](#viewing-your-project)
6. [Part 5: Working With Python Versions](#part-5-working-with-python-versions)
   - [Installing Python](#installing-python)
   - [Managing Multiple Python Versions](#managing-multiple-python-versions)
   - [Pinning Python Versions](#pinning-python-versions)
7. [Part 6: Running Code](#part-6-running-code)
   - [Running Projects](#running-projects)
   - [Running Scripts](#running-scripts)
   - [Script Dependencies](#script-dependencies)
8. [Part 7: Tools & Utilities](#part-7-tools--utilities)
   - [Running Tools](#running-tools)
   - [Installing Tools](#installing-tools)
   - [Managing Tools](#managing-tools)
9. [Part 8: The pip Interface](#part-8-the-pip-interface)
   - [Virtual Environments with uv](#virtual-environments-with-uv)
   - [Installing Packages](#installing-packages)
   - [Managing Pip Environments](#managing-pip-environments)
10. [Part 9: Advanced Topics](#part-9-advanced-topics)
    - [Workspaces](#workspaces)
    - [Publishing Packages](#publishing-packages)
    - [Caching](#caching)
    - [Configuration](#configuration)
11. [Part 10: Decision Trees & Workflows](#part-10-decision-trees--workflows)
    - [Decision Trees for Common Scenarios](#decision-trees-for-common-scenarios)
    - [Complete Workflows](#complete-workflows)
12. [Part 11: Command Reference](#part-11-command-reference)
    - [Project Commands](#project-commands)
    - [Python Commands](#python-commands)
    - [Tool Commands](#tool-commands)
    - [Pip Commands](#pip-commands)
    - [Cache & Utility Commands](#cache--utility-commands)
13. [Part 12: Cheat Sheets](#part-12-cheat-sheets)
    - [The Essential Cheat Sheet](#the-essential-cheat-sheet)
    - [Daily Workflow Cheat Sheet](#daily-workflow-cheat-sheet)
    - [Troubleshooting Cheat Sheet](#troubleshooting-cheat-sheet)
14. [Part 13: Comparison Tables](#part-13-comparison-tables)
    - [uv vs Other Tools](#uv-vs-other-tools)
15. [Part 14: Real-World Examples](#part-14-real-world-examples)
    - [Example 1: AI Chatbot Project](#example-1-ai-chatbot-project)
    - [Example 2: Web API Project](#example-2-web-api-project)
    - [Example 3: Data Analysis Project](#example-3-data-analysis-project)
16. [Appendix: Troubleshooting & FAQ](#appendix-troubleshooting--faq)

---

# Introduction & What You'll Learn

Welcome! This handbook is your complete guide to **uv**, the fastest Python package manager in the world. 

If you've never used Python before, or if you've used Python but are confused by `pip`, `virtual environments`, and dependency management — this handbook is for you.

By the end of this handbook, you'll be able to:

- Install and use uv on your computer
- Create new Python projects from scratch
- Add and remove libraries your projects depend on
- Run Python code reliably
- Manage multiple Python versions
- Install command-line tools
- Publish Python packages
- Understand how modern Python development works

**No prior experience needed.** We explain everything.

---

# Part 1: The Foundations

## What is Python?

**Python** is a programming language — a way to give instructions to computers.

Think of it like English for computers. Instead of writing:

```
Please open the file called "data.txt" and count how many lines have the word "hello" in them.
```

In Python, you'd write:

```python
with open("data.txt") as file:
    count = sum(1 for line in file if "hello" in line)
    print(count)
```

Python is popular because it's:
- **Easy to read** — even non-programmers can understand Python code
- **Powerful** — used for AI, data analysis, web apps, automation, and more
- **Flexible** — you can use it for almost any programming task

**Why does Python need a package manager?**

Think of Python like a house. When you first install Python, it's like having an empty house with just the basic furniture (the core language).

But to build something useful, you need more tools. You might need:
- A library to make web requests (like `requests`)
- A library for data analysis (like `pandas`)
- A library for AI (like `tensorflow`)

These are **packages** — collections of code written by other people that you can use in your own code.

## What is a Package Manager?

A **package manager** is like a librarian for your Python code.

### The Problem It Solves

Imagine you want to build a house. You need:
- Nails
- Wood
- Paint
- Screws

But nails come from the hardware store. Wood comes from the lumber yard. Paint comes from the home improvement store. Screws come from yet another place.

It would be exhausting to visit 20 different stores to build one house.

A package manager is like having **one warehouse** where you can get everything you need.

### How It Works

When you write Python code that says:

```python
import requests
```

Your computer doesn't automatically have the `requests` library. You need to:
1. Find it
2. Download it
3. Install it
4. Make sure it works with your other libraries

A package manager does all of this automatically.

### The Four Main Jobs

A good package manager:

1. **Finds packages** — knows where to download them from
2. **Downloads packages** — gets them to your computer
3. **Installs packages** — puts them where Python can find them
4. **Manages versions** — makes sure package versions don't conflict with each other

## Why Does uv Exist?

For many years, Python used a tool called **pip** (Pip Installs Packages).

**pip is slow.** Very slow.

Installing packages could take minutes. Even checking what packages were installed could take a long time.

The Python community asked: "Can we make this faster?"

In 2023, **Astral** (the company that made the code formatter **Ruff**) created **uv**.

**uv is 10–100 times faster than pip.**

It's also more than just a package manager:
- It installs Python versions
- It installs command-line tools
- It replaces 8+ different Python tools with just **one** tool
- It's written in Rust (a very fast programming language)

## What Problem Does uv Solve?

### The Old Way (Without uv)

To set up a Python project, you used to need:

| Task | Tool |
|------|------|
| Manage packages | `pip` |
| Create isolated environments | `virtualenv` |
| Manage Python versions | `pyenv` |
| Lock dependencies | `pip-tools` |
| Run command-line tools | `pipx` |
| Manage projects | `poetry` or `rye` |
| Publish packages | `twine` |
| Create virtual environments | `venv` |

That's **8 different tools** you had to learn and maintain.

### The New Way (With uv)

With uv, you use **one tool** for everything:

```bash
uv init              # Create a project
uv add pandas        # Add a dependency
uv python install    # Install Python
uv run               # Run your code
uv tool install      # Install a command-line tool
uv build             # Build for publishing
uv publish           # Publish your package
```

That's it. One tool. One command structure. Much faster.

---

# Part 2: Getting Started

## Installation

### macOS and Linux

Open your terminal and run:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**What this does:**
- Downloads the latest version of uv
- Runs the installation script
- Sets everything up automatically

### Windows

Open PowerShell and run:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Alternative: Using pip

If you already have Python installed, you can install uv with pip:

```bash
pip install uv
```

Or with Homebrew (macOS):

```bash
brew install uv
```

## Verifying Your Installation

After installing, verify everything works:

```bash
uv --version
```

You should see something like:

```
uv 0.5.4
```

If you see an error instead, the installation didn't work. Try installing again or check the official documentation.

## Your First Command

Try running:

```bash
uv
```

You'll see a help menu showing all the commands available:

```
An extremely fast Python package manager.

Usage: uv [OPTIONS] <COMMAND>

Commands:
  init       Create a new Python project
  add        Add a package to the project
  remove     Remove a package from the project
  run        Run a script or command
  python     Install and manage Python versions
  tool       Install and run command-line tools
  help       Print help information

Options:
  -h, --help     Print help
  -V, --version  Print version
```

Great! uv is installed and ready to use.

---

# Part 3: Key Concepts Explained

Before we start using uv, let's understand the core concepts. Don't worry if this seems abstract — everything will make sense once you see examples.

## Virtual Environments

### The Problem It Solves

Imagine you have two projects:
- **Project A** needs `requests` version 2.25
- **Project B** needs `requests` version 2.30

Both projects are on your computer. If you install both versions globally, they'll conflict with each other. One will overwrite the other.

How do you keep them separate?

### The Solution: Virtual Environments

A **virtual environment** is like a completely separate Python installation on your computer.

Think of it like this:

```
Your Computer
├── Virtual Environment 1 (Project A's room)
│   ├── Python
│   ├── requests 2.25
│   └── pandas 1.0
│
└── Virtual Environment 2 (Project B's room)
    ├── Python
    ├── requests 2.30
    └── numpy 1.20
```

Each project has its own:
- **Python installation**
- **Installed packages**
- **Package versions**

They don't interfere with each other.

### Real-World Analogy

Think of virtual environments like separate kitchens in different restaurants:

- **Restaurant A's kitchen** has ingredients and tools for Italian food
- **Restaurant B's kitchen** has ingredients and tools for Japanese food

They're on the same building (your computer), but they're completely separate. What happens in one kitchen doesn't affect the other.

### With uv

Good news: **uv handles virtual environments automatically.**

You don't usually need to think about them. uv creates them for you when you create a project:

```bash
uv init myproject
```

This command:
1. Creates a new project folder
2. Creates a virtual environment inside it
3. Sets everything up so you can start coding immediately

## Dependencies

A **dependency** is a library (package) that your code depends on.

### Example

Let's say you're writing a program that downloads weather data from the internet. You write:

```python
import requests

response = requests.get("https://api.weather.com/today")
print(response.json())
```

This code depends on the `requests` library. Without it, your code won't work.

So `requests` is a **dependency** of your project.

### How Dependencies Work

When you say:

```bash
uv add requests
```

You're telling uv: "I need the `requests` package. Download it and install it for me."

uv then:
1. **Finds** the latest version of `requests`
2. **Downloads** it
3. **Installs** it in your project's virtual environment
4. **Records** it in your project files so others know what you need

### Dependency Chain

Here's where it gets interesting: packages themselves have dependencies.

For example:
- `requests` depends on `urllib3`
- `urllib3` depends on other packages
- And so on...

A simple library might depend on 5 other libraries. Which depend on 10 others. Which depend on 20 others.

**How many dependencies do you really have?**

With `requests`, it's about 4 direct dependencies. But those have their own dependencies. So the total is more like 10–20 packages that get installed.

### Why This Matters

If any of those dependencies breaks or has a bug, your code might break too.

This is why **version management** is important (which we'll explain next).

## Lock Files

### The Problem

Let's say you run:

```bash
uv add requests
```

It installs `requests` version 2.32.0.

But next week, the `requests` developers release version 2.32.1 with a bug fix.

If a colleague runs the same command on their computer, they'll get version 2.32.1.

Now you have different versions. Your code works, but theirs might not (or vice versa).

**How do you ensure everyone uses the same versions?**

### The Solution: Lock Files

A **lock file** is a record of exactly which package versions were installed.

Think of it like a recipe with exact measurements:
- Not just "sugar" but "3 cups of sugar"
- Not just "requests" but "requests 2.32.0"

When you create a lock file:

```bash
uv lock
```

It records the exact versions that are currently installed.

Then, when someone else runs:

```bash
uv sync
```

They get the exact same versions. No surprises.

### Real-World Analogy

Imagine you're a baker and you create the perfect cookie recipe:

```
- 2 cups flour
- 1 cup butter (room temperature)
- 3/4 cup sugar
```

But you don't share:

```
- Some flour
- Some butter
- Some sugar
```

The first version (exact measurements) is like a lock file. Everyone who follows it gets identical cookies.

The second version is like a `pyproject.toml` without a lock file. Everyone gets something different.

### Two Files You Need to Know

**`pyproject.toml`** — Your project file

This says: "I need requests, but I don't care if it's 2.30 or 2.32, as long as it works."

It's flexible.

**`uv.lock`** — Your lock file

This says: "I need requests 2.31.0 exactly, and urllib3 1.26.5 exactly, and..."

It's specific and reproducible.

## Packages and Libraries

These terms are sometimes used interchangeably, but they mean slightly different things.

### Package

A **package** is a directory of Python code that can be installed.

It's like a deliverable product.

Example packages:
- `requests` (make web requests)
- `pandas` (analyze data)
- `flask` (build web apps)

### Library

A **library** is a collection of reusable code.

All packages are libraries, but not all libraries are packages.

When we say "install the pandas library," we mean "install the pandas package."

In this handbook, we use "package" and "library" to mean the same thing.

### Module

A **module** is a single Python file.

For example:
- `my_code.py` is a module

### Distribution

A **distribution** is how a package is packaged and delivered.

When you install `requests`, you're installing a distribution of the `requests` package.

## Project Structure

When you create a project with uv, here's what you get:

```
myproject/
├── pyproject.toml          # Project configuration
├── uv.lock                 # Locked dependency versions
├── .python-version         # Python version for this project
├── .venv/                  # Virtual environment (hidden)
│   ├── bin/               # Executables
│   └── lib/               # Installed packages
├── src/
│   └── myproject/
│       ├── __init__.py
│       └── main.py        # Your code
└── README.md              # Documentation
```

### Key Files Explained

**`pyproject.toml`** — Project configuration

Defines:
- Project name
- Python version requirements
- Dependencies
- Build settings

Example:

```toml
[project]
name = "myproject"
version = "0.1.0"
description = "My first Python project"
requires-python = ">=3.10"

[project.optional-dependencies]
dev = ["pytest", "black"]
```

**`uv.lock`** — Lock file

Auto-generated. Shows exact versions of everything installed.

You don't edit this file. uv maintains it.

**`.python-version`** — Python version

Specifies which Python version this project needs.

Example:

```
3.12.0
```

When you run `uv run`, it automatically uses this Python version.

**`.venv/`** — Virtual environment directory

Auto-generated. Contains the isolated Python installation.

You don't usually need to touch this folder.

---

# Part 4: Creating & Managing Projects

Now let's actually create and work with projects.

## Initializing a New Project

### Command: uv init

**What it does:** Creates a new Python project with all the files you need.

**Think of it like:** Setting up a new folder for your project, like creating a new directory in a filing cabinet.

**When to use it:** Every time you start a new project.

### Basic Usage

```bash
uv init myproject
```

This creates:
- A folder called `myproject`
- A virtual environment inside it
- All the configuration files you need
- A sample Python file to get started

### Output

```
Created project `myproject` at `/home/user/myproject`
Initialized virtual environment at: myproject/.venv
```

### Next Steps

After creating a project:

```bash
cd myproject
```

You're now inside your project folder.

### Example: Step by Step

```bash
# Create a new project
$ uv init hello-world
Created project `hello-world` at `/home/user/hello-world`

# Navigate into it
$ cd hello-world

# See what was created
$ ls -la
-rw-r--r--  pyproject.toml
-rw-r--r--  README.md
-rw-r--r--  .python-version
drwxr-xr-x  .venv/
drwxr-xr-x  src/
-rw-r--r--  uv.lock

# Check the Python version
$ cat .python-version
3.12.4

# Look at your project configuration
$ cat pyproject.toml
[project]
name = "hello-world"
version = "0.1.0"
description = "Add your description here"
requires-python = ">=3.10"
dependencies = []
```

### Common Mistakes

**Mistake 1:** Forgetting to navigate into the folder

```bash
uv init myproject
# Then trying to run commands here — won't work!
# You need to cd myproject first
```

**Fix:** Always do `cd myproject` after creating it.

**Mistake 2:** Creating a project inside another project

```bash
cd existing-project
uv init nested-project  # Don't do this!
```

**Fix:** Create projects in separate folders, not nested inside each other.

**Mistake 3:** Running uv init in an existing project

```bash
cd myproject
uv init  # Overwrites existing files!
```

**Fix:** Only run `uv init` once per project.

### Things to Remember

- `uv init` creates a complete project structure
- You don't need to create any files manually
- The virtual environment is created automatically
- You're ready to code immediately after running `uv init`

---

## Project Structure

When you run `uv init`, here's exactly what gets created:

### Directory Layout

```
myproject/
├── README.md              # Documentation (empty)
├── pyproject.toml         # Project configuration ← most important
├── uv.lock               # Dependency lock file
├── .python-version       # Python version specification
├── .venv/                # Virtual environment (hidden)
│   ├── bin/              # Python executables
│   │   ├── python
│   │   ├── pip
│   │   └── ...other tools...
│   ├── lib/              # Installed packages
│   │   └── python3.12/site-packages/
│   └── pyvenv.cfg
└── src/
    └── myproject/
        ├── __init__.py   # Makes this a package
        └── main.py       # Your code goes here
```

### What Each Directory Is For

**`src/myproject/`** — Your code

This is where you write your Python files.

**`.venv/`** — Virtual environment

Hidden (starts with a dot). Contains the isolated Python installation.

You don't edit this. uv manages it.

**Root directory** — Configuration

Contains `pyproject.toml`, `uv.lock`, and `.python-version`.

These are essential for the project to work.

### The pyproject.toml File Explained

This is the most important file. It's where you tell uv about your project.

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "myproject"
version = "0.1.0"
description = "My awesome Python project"
readme = "README.md"
requires-python = ">=3.10"
authors = [
    {name = "Your Name", email = "you@example.com"}
]
dependencies = [
    "requests>=2.31.0",
    "pandas>=2.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "black>=23.0",
]
```

**What each section means:**

- **`[build-system]`** — How to build your project for sharing (don't worry about this yet)
- **`[project]`** — Information about your project
  - `name` — Project name
  - `version` — Current version
  - `description` — What your project does
  - `requires-python` — Minimum Python version needed
  - `dependencies` — Libraries your project needs
- **`[project.optional-dependencies]`** — Extra packages for development

### The uv.lock File

Auto-generated. Do not edit manually.

It looks like:

```toml
[[package]]
name = "requests"
version = "2.31.0"
requires_dist = [
    "charset-normalizer >=2",
    "idna >=2.5",
    "urllib3 >=1.21.1",
    "certifi >=2017.4.17",
]

[[package]]
name = "charset-normalizer"
version = "3.3.2"
requires_dist = []
...
```

This records the exact version of every package and their dependencies.

**Why it matters:**
- When you share your project, others get the same versions
- Your code is reproducible
- No "works on my machine" problems

### The .python-version File

Just one line:

```
3.12.0
```

This tells uv: "This project uses Python 3.12.0"

When you run `uv run`, it automatically switches to this Python version.

### Viewing Your Project

To see what's in your project:

```bash
# See the project structure
$ tree  # if you have the 'tree' command

# Or list files
$ ls -la

# See dependencies
$ cat pyproject.toml

# See locked versions
$ cat uv.lock
```

---

## Adding Dependencies

Adding a dependency means "I want to use this library in my project."

### Command: uv add

**What it does:** Adds a library to your project and installs it.

**Think of it like:** Walking into a library and checking out a book.

**When to use it:** Every time you want to use a new library.

### Basic Usage

```bash
uv add requests
```

This:
1. Finds the latest version of `requests`
2. Downloads it
3. Installs it in your virtual environment
4. Updates `pyproject.toml` and `uv.lock`

### Output

```
Creating virtual environment at: .venv
Resolved 4 packages in 210ms
Prepared 4 packages in 340ms
Installed 4 packages in 2ms
 + certifi==2024.7.4
 + charset-normalizer==3.3.2
 + idna==2.5
 + requests==2.31.0
```

Great! Now you can use `requests` in your code.

### Specifying Versions

By default, uv installs the latest version.

But sometimes you need a specific version.

#### Install a specific version

```bash
uv add requests==2.28.0
```

This installs exactly version 2.28.0.

#### Install a minimum version

```bash
uv add requests>=2.28.0
```

This installs 2.28.0 or newer (whatever is latest).

#### Install a range

```bash
uv add "requests>=2.28.0,<3.0.0"
```

This installs any version from 2.28.0 to 2.x (but not 3.0 or higher).

### Adding Multiple Dependencies

```bash
uv add requests pandas numpy
```

All three are added and installed.

### Development Dependencies

Some libraries are only needed while developing (like testing tools), not in production.

Add them as development dependencies:

```bash
uv add --dev pytest
```

Or:

```bash
uv add --dev pytest black ruff
```

These go in the `[project.optional-dependencies]` section of `pyproject.toml`.

### Example: Building a Data Project

```bash
# Create project
$ uv init data-analyzer
$ cd data-analyzer

# Add data analysis libraries
$ uv add pandas numpy matplotlib

# Add development tools
$ uv add --dev pytest pytest-cov black ruff

# Check what was installed
$ cat pyproject.toml
[project]
name = "data-analyzer"
version = "0.1.0"
dependencies = [
    "pandas",
    "numpy",
    "matplotlib",
]

[project.optional-dependencies]
dev = ["pytest>=7.0", "pytest-cov", "black", "ruff"]
```

### Common Mistakes

**Mistake 1:** Typo in package name

```bash
$ uv add reqeusts  # Typo!
error: Package `reqeusts` not found
```

**Fix:** Check the spelling. The correct name is `requests`.

**Mistake 2:** Package doesn't exist

```bash
$ uv add mynonexistentlibrary
error: Package `mynonexistentlibrary` not found
```

**Fix:** Make sure the package name is correct. Check PyPI: https://pypi.org

**Mistake 3:** Version doesn't exist

```bash
$ uv add requests==99.0.0
error: No matching version found for requests==99.0.0
```

**Fix:** Use a version that actually exists.

### Things to Remember

- `uv add` automatically installs the package
- Your `pyproject.toml` is updated automatically
- Your `uv.lock` is updated automatically
- You can immediately start using the library in your code
- Use `--dev` for development-only libraries

---

## Removing Dependencies

### Command: uv remove

**What it does:** Removes a library from your project.

**Think of it like:** Returning a book to the library.

**When to use it:** When you no longer need a library.

### Basic Usage

```bash
uv remove requests
```

This:
1. Uninstalls `requests` from your virtual environment
2. Removes it from `pyproject.toml`
3. Updates `uv.lock`

### Output

```
Removed 1 package
Uninstalled requests==2.31.0
```

### Removing Multiple Packages

```bash
uv remove requests pandas numpy
```

All three are removed.

### Removing Development Dependencies

If you added a package with `--dev`:

```bash
uv remove pytest
```

It removes it from the `[project.optional-dependencies]` section.

### Example

```bash
# Add a package
$ uv add requests
 + requests==2.31.0

# Use it for a bit...

# Decide you don't need it
$ uv remove requests
Removed 1 package

# It's gone
$ cat pyproject.toml
dependencies = []
```

### Common Mistakes

**Mistake 1:** Removing a package your code still uses

```python
# my code
import requests  # ERROR — requests is no longer installed!
```

**Fix:** Make sure you've removed all code that uses the package before removing it.

**Mistake 2:** Package name is case-sensitive sometimes

```bash
uv remove Requests  # vs. uv remove requests
```

**Fix:** Use the exact package name (lowercase usually).

### Things to Remember

- `uv remove` immediately uninstalls the package
- Your code might break if it still uses the package
- `pyproject.toml` and `uv.lock` are updated automatically

---

## Syncing Your Project

### Command: uv sync

**What it does:** Installs all dependencies exactly as recorded in `uv.lock`.

**Think of it like:** Pulling a book from the library that someone else checked out.

**When to use it:**
- When you first clone someone else's project
- When you change branches in Git
- When you pull new changes from a repository

### Basic Usage

```bash
uv sync
```

This installs everything in `uv.lock` into your `.venv`.

### Output

```
Resolved 4 packages in 0.32ms
Installed 4 packages in 128ms
 + certifi==2024.7.4
 + charset-normalizer==3.3.2
 + idna==2.5
 + requests==2.31.0
```

### Example Scenario

You and a colleague are working on the same project:

1. **You:** Add `requests` to the project
   ```bash
   uv add requests
   ```
   This updates `uv.lock`.

2. **You:** Commit and push to Git
   ```bash
   git add .
   git commit -m "Add requests library"
   git push
   ```

3. **Colleague:** Pulls your changes
   ```bash
   git pull
   ```

4. **Colleague:** Syncs dependencies
   ```bash
   uv sync
   ```
   Now they have `requests` installed too, with the exact same version.

### Difference Between `uv add` and `uv sync`

| Command | What It Does | When to Use |
|---------|-------------|-----------|
| `uv add requests` | Adds a new dependency and installs it | When you want to use a new library |
| `uv sync` | Installs all dependencies from `uv.lock` | When you get new `uv.lock` from Git |

### Things to Remember

- `uv sync` uses `uv.lock`, not `pyproject.toml`
- It installs exact versions
- Useful when working with a team
- Run this after pulling from Git

---

## Viewing Your Project

### Command: uv tree

**What it does:** Shows all your dependencies and their sub-dependencies in a tree structure.

**Think of it like:** Looking at a family tree, but for libraries.

**When to use it:** When you want to see what's installed and why.

### Basic Usage

```bash
uv tree
```

### Output Example

```
myproject
├── pandas==2.0.0
│   ├── numpy==1.24.0
│   ├── python-dateutil==2.8.2
│   │   └── six==1.16.0
│   ├── pytz==2023.3
│   └── tzdata==2023.3
├── requests==2.31.0
│   ├── certifi==2024.7.4
│   ├── charset-normalizer==3.3.2
│   ├── idna==2.5
│   └── urllib3==2.0.0
└── matplotlib==3.7.0
    ├── contourpy==1.1.0
    ├── cycler==0.11.0
    ├── fonttools==4.42.0
    ├── kiwisolver==1.4.5
    ├── numpy==1.24.0
    ├── packaging==23.1
    ├── pillow==10.0.0
    ├── pyparsing==3.1.0
    └── python-dateutil==2.8.2
```

This shows:
- **Top level:** Libraries you directly added (pandas, requests, matplotlib)
- **Indented:** Libraries those depend on (numpy, certifi, etc.)
- **Versions:** Exact version of each

### Finding Unused Dependencies

If you see a library in `uv tree` that you don't recognize, it's probably:

1. A dependency of another library (like how pandas depends on numpy)
2. No longer used in your code

If it's no longer used, you can remove it.

### Things to Remember

- Shows your entire dependency tree
- Helps you understand what's installed
- Useful for finding conflicts or unused dependencies

---

## Exporting Dependencies

### Command: uv export

**What it does:** Converts your `uv.lock` into different formats that other tools understand.

**Think of it like:** Translating a document into different languages.

**When to use it:** When you need to use your dependencies with other tools.

### Basic Usage

```bash
uv export > requirements.txt
```

This creates a `requirements.txt` file that other Python tools understand.

### Output (requirements.txt)

```
certifi==2024.7.4
charset-normalizer==3.3.2
idna==2.5
requests==2.31.0
pandas==2.0.0
numpy==1.24.0
# ... many more ...
```

### Different Formats

```bash
# Export to requirements format (default)
uv export > requirements.txt

# Export with dev dependencies
uv export --dev > requirements-all.txt

# Export only production dependencies
uv export --no-dev > requirements-prod.txt
```

### When to Use Export

- Sharing dependencies with someone using pip
- Using your project in Docker
- Deploying to a server that doesn't have uv
- Creating a `requirements.txt` for legacy tools

### Things to Remember

- Export creates a `requirements.txt` file
- `uv.lock` is more complete; prefer it if possible
- Export is useful for compatibility with other tools

---

# Part 5: Working With Python Versions

One of uv's super powers is managing Python versions automatically.

## Installing Python

### Command: uv python install

**What it does:** Downloads and installs a Python version.

**Think of it like:** Downloading a specific version of an app from the internet.

**When to use it:** When you need a specific Python version.

### Basic Usage

Install a specific version:

```bash
uv python install 3.12
```

This downloads and installs Python 3.12.

### Output

```
Searching for Python versions matching: Python 3.12
Downloading cpython-3.12.4-macos-aarch64-none...
Downloaded in 2.34s
Installing cpython-3.12.4-macos-aarch64-none...
Installed in 1.23s
  + cpython-3.12.4-macos-aarch64-none
```

### Installing Multiple Versions

```bash
uv python install 3.10 3.11 3.12
```

This installs all three versions so you can switch between them.

### Different Ways to Specify Versions

```bash
# Just the major.minor version
uv python install 3.12

# Specific patch version
uv python install 3.12.4

# Specific implementation (cpython, pypy, etc.)
uv python install cpython-3.12

# All of the above with PyPy
uv python install pypy-3.10
```

### Listing Installed Versions

See what Python versions you have:

```bash
uv python list
```

### Output

```
cpython-3.10.14   /home/user/.local/share/uv/pythons/cpython-3.10.14
cpython-3.11.9    /home/user/.local/share/uv/pythons/cpython-3.11.9
cpython-3.12.4    /home/user/.local/share/uv/pythons/cpython-3.12.4 (default)
pypy-3.10.13      /home/user/.local/share/uv/pythons/pypy-3.10.13
```

This shows:
- Each installed version
- Where it's stored on your computer
- Which one is the default

### Finding Python Versions

If you want to see what versions are available without installing:

```bash
uv python find
```

Or find a specific version:

```bash
uv python find 3.11
```

### Uninstalling Python

If you have a version you don't need:

```bash
uv python uninstall 3.10
```

This removes Python 3.10 from your computer.

### Example: Setting Up Multiple Versions

```bash
# Install three versions
$ uv python install 3.10 3.11 3.12
Searching for Python versions matching: Python 3.10
Downloading cpython-3.10.14-macos-aarch64-none...
Downloaded in 2.34s
Installing cpython-3.10.14-macos-aarch64-none...
Installed in 1.23s
  + cpython-3.10.14-macos-aarch64-none
(... repeats for 3.11 and 3.12 ...)

# List what you have
$ uv python list
cpython-3.10.14
cpython-3.11.9
cpython-3.12.4 (default)

# Now you can use any of them
```

### Common Mistakes

**Mistake 1:** Not specifying a version

```bash
uv python install  # Won't work!
```

**Fix:** Always specify which version you want.

**Mistake 2:** Installing a version that doesn't exist

```bash
uv python install 3.14
# Error: No matching version found
```

**Fix:** Use a version that's actually available (3.10, 3.11, 3.12, 3.13, etc.).

### Things to Remember

- uv downloads Python for you automatically
- You can have multiple versions installed
- Each project can use a different Python version
- No need to manually manage Python installations

---

## Managing Multiple Python Versions

### Why Multiple Versions?

Different projects might need different Python versions:

- **Project A** needs Python 3.10 (because it uses an old library)
- **Project B** needs Python 3.12 (because it uses new features)

With uv, you can have both and switch between them easily.

### Setting Up Projects

When you create a project:

```bash
uv init project-a
cd project-a
uv python pin 3.10
```

This sets Python 3.10 for this project.

Later, switch to another project:

```bash
cd ../project-b
uv python pin 3.12
```

This sets Python 3.12 for this project.

Now:
- When you run code in `project-a`, it uses Python 3.10
- When you run code in `project-b`, it uses Python 3.12

### Running with a Specific Version

Temporarily use a different version:

```bash
uv run --python 3.11 my-script.py
```

This runs `my-script.py` with Python 3.11, even if your project is set to 3.12.

### Checking Your Python Version

See which version a project uses:

```bash
cat .python-version
```

Output:

```
3.12.4
```

Or check the actual Python:

```bash
uv run python --version
```

Output:

```
Python 3.12.4
```

### Example: Working With Two Projects

```bash
# Create and set up first project
$ uv init old-project
$ cd old-project
$ uv python pin 3.10
$ uv run python --version
Python 3.10.14

# Switch to second project
$ cd ../new-project
$ uv init new-project
$ uv python pin 3.12
$ uv run python --version
Python 3.12.4

# Back to first project — automatically uses 3.10
$ cd ../old-project
$ uv run python --version
Python 3.10.14
```

### Things to Remember

- Each project can have its own Python version
- Specified in `.python-version` file
- Set with `uv python pin VERSION`
- uv automatically switches versions when you change directories

---

## Pinning Python Versions

### Command: uv python pin

**What it does:** Locks your project to a specific Python version.

**Think of it like:** Writing "This project requires Python 3.12" on the project folder.

**When to use it:** When you know which Python version your project needs.

### Basic Usage

```bash
uv python pin 3.12
```

This creates (or updates) a `.python-version` file with:

```
3.12
```

### Specific Version

```bash
uv python pin 3.12.4
```

This pins to an exact patch version:

```
3.12.4
```

### What Gets Created

A `.python-version` file appears in your project:

```bash
$ cat .python-version
3.12.4
```

Commit this file to Git:

```bash
git add .python-version
git commit -m "Pin to Python 3.12.4"
```

Now everyone who clones your project will use Python 3.12.4.

### Example: Pinning a Project

```bash
# Create project
$ uv init my-webapp
$ cd my-webapp

# Pin to Python 3.12
$ uv python pin 3.12
Pinned `.python-version` to `3.12`

# Verify
$ cat .python-version
3.12

# Now when you run code, it always uses 3.12
$ uv run python --version
Python 3.12.4
```

### Unpinning

To stop pinning to a specific version:

```bash
uv python pin --ignore-requires-python
```

Or just delete the `.python-version` file:

```bash
rm .python-version
```

Now uv uses its default Python version.

### Things to Remember

- Creates a `.python-version` file
- Affects only that specific project
- Other projects aren't affected
- Easy to commit to Git for team consistency

---

# Part 6: Running Code

Now let's run some actual code!

## Running Projects

### Command: uv run

**What it does:** Runs your project code in the virtual environment.

**Think of it like:** Pressing the "Play" button on a video player.

**When to use it:** Every time you want to test your code.

### Basic Usage

If your project has a main module:

```bash
uv run
```

Or run a specific Python file:

```bash
uv run python src/myproject/main.py
```

Or even simpler:

```bash
uv run python main.py
```

### Running Python Code

Run any Python command:

```bash
uv run python -c "print('Hello, World!')"
```

Output:

```
Hello, World!
```

### Running Installed Tools

If you've installed a command-line tool with `uv add`:

```bash
uv add ruff  # Install code formatter

uv run ruff check  # Run it
```

### Example: A Simple Project

```bash
# Create project
$ uv init hello
$ cd hello

# Edit src/hello/main.py
$ echo "print('Hello, World!')" > src/hello/main.py

# Run it
$ uv run python src/hello/main.py
Hello, World!

# Or even simpler
$ uv run python -c "print('Hello, World!')"
Hello, World!
```

### Running With a Specific Python Version

```bash
uv run --python 3.11 python --version
```

This runs the command with Python 3.11.

### Common Mistakes

**Mistake 1:** Forgetting to use `uv run`

```bash
# Without uv run
$ python my-script.py
# Error: requests not found (because you're not in the virtual environment)

# With uv run
$ uv run python my-script.py
# Works! Uses packages from .venv
```

**Mistake 2:** Trying to activate the venv manually

With uv, you don't need to do:

```bash
source .venv/bin/activate  # Don't do this!
```

Just use:

```bash
uv run python ...
```

uv handles the activation automatically.

### Things to Remember

- `uv run` automatically uses your virtual environment
- No need to manually activate anything
- Specify Python version with `--python` if needed

---

## Running Scripts

A **script** is a single Python file (not a full project).

### When to Use Scripts

- Quick one-off programs
- Automation tasks
- Data processing
- Testing ideas

### Basic Script Usage

Create a file:

```bash
echo "import requests; print(requests.get('https://example.com'))" > fetch.py
```

Run it:

```bash
uv run python fetch.py
```

### Running Scripts With Dependencies

But wait — `fetch.py` uses `requests`, which isn't installed!

With old tools, you'd have to:
1. Create a virtual environment
2. Install requests
3. Run the script

With uv, you can declare dependencies right in the script.

### Script Dependencies

Add a special comment at the top:

```python
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "requests>=2.31.0",
# ]
# ///

import requests

response = requests.get("https://example.com")
print(f"Status: {response.status_code}")
```

This comment declares: "This script needs requests."

Now run it:

```bash
uv run fetch.py
```

uv automatically:
1. Creates an isolated environment for this script
2. Installs `requests`
3. Runs the script

### Adding Script Dependencies

If you have a script and want to add dependencies:

```bash
uv add --script fetch.py requests
```

This adds the `requires-python` and `dependencies` comment to your script automatically.

### Example: A Complete Script

```bash
# Create script with dependencies declared
$ cat > weather.py << 'EOF'
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "requests>=2.31.0",
#     "python-dateutil>=2.8.0",
# ]
# ///

import requests
from datetime import datetime

response = requests.get("https://api.example.com/weather")
print(f"Weather data fetched at {datetime.now()}")
print(response.json())
EOF

# Run the script
$ uv run weather.py
Weather data fetched at 2024-06-28 14:23:45
{ "temp": 22, "condition": "sunny" }
```

### Key Advantages of uv Scripts

| Feature | Benefit |
|---------|---------|
| Inline dependencies | No separate `requirements.txt` needed |
| Isolated execution | Each script gets its own environment |
| Fast | Reuses cached packages |
| Portable | Share the single .py file, everything works |

### Common Mistakes

**Mistake 1:** Forgetting the special comment format

```python
# Wrong!
# dependencies = ["requests"]

# Correct!
# /// script
# dependencies = ["requests"]
# ///
```

**Fix:** Use the exact format with `# ///` to start and end the metadata.

**Mistake 2:** Typo in `requires-python`

```python
# Wrong:
# requires-python = "3.11"

# Correct:
# requires-python = ">=3.11"
```

**Fix:** Include the operator (>=, >, ==, etc.).

### Things to Remember

- Scripts are simpler than projects for small programs
- Declare dependencies at the top with special comments
- Each script runs in an isolated environment
- Perfect for automation and one-off tasks

---

# Part 7: Tools & Utilities

uv can install and run command-line tools — programs that you run from the terminal.

## What Are Tools?

A **tool** is a Python package that provides a command-line program.

Examples:

- **ruff** — Code formatter
- **black** — Code formatter
- **pytest** — Testing framework
- **jupyter** — Interactive notebooks
- **ipython** — Enhanced Python shell
- **httpie** — Command-line HTTP client
- **cookiecutter** — Project template generator

### Tools vs. Libraries

| Aspect | Library | Tool |
|--------|---------|------|
| How you use it | `import` in Python code | Run from terminal |
| Example | `pandas` | `jupyter` |
| Install with | `uv add` | `uv tool install` |
| Run with | Python script | `uv run` or command name |

---

## Running Tools: uvx

### Command: uvx

**What it does:** Runs a Python tool without installing it.

**Think of it like:** Renting a tool instead of buying it.

**When to use it:** When you want to try a tool or use it once.

### Basic Usage

Run a tool:

```bash
uvx black --version
```

This:
1. Downloads `black`
2. Runs it
3. Cleans up afterward

You don't need to install anything.

### Output

```
black, 24.4.2 (compiled: yes)
target versions: {Py37, Py38, Py39, Py310, Py311, Py312}
```

### Common Tools

```bash
# Format code
uvx black my-file.py

# Check code quality
uvx ruff check .

# Run HTTP requests
uvx httpie GET https://example.com

# Generate project from template
uvx cookiecutter https://github.com/audreyr/cookiecutter-pypackage

# Create Jupyter notebook
uvx jupyter notebook
```

### Example: Using a Tool Once

```bash
# Check if 'black' works without installing
$ uvx black --version
black, 24.4.2

# Use it to format a file
$ uvx black my-script.py
reformatted my-script.py
All done! ✨ 🍰 ✨
1 file reformatted.

# Clean up - no installation left behind
```

### Advantages of uvx

- No installation needed
- Always latest version
- No clutter on your computer
- Perfect for trying new tools

### Things to Remember

- `uvx` is an alias for `uv tool run`
- No permanent installation
- Great for experimenting
- Runs in an isolated environment

---

## Installing Tools

### Command: uv tool install

**What it does:** Installs a Python tool permanently on your computer.

**Think of it like:** Buying and permanently storing a tool in your toolbox.

**When to use it:** When you use a tool regularly.

### Basic Usage

```bash
uv tool install black
```

This:
1. Downloads `black`
2. Installs it in a special location
3. Adds it to your PATH (so you can run it from anywhere)

### Output

```
Resolved 1 package in 6ms
Installed 1 package in 2ms
 + black==24.4.2
Installed 1 executable: black
```

Now you can use `black` from anywhere in your terminal:

```bash
black my-file.py
```

### Listing Installed Tools

```bash
uv tool list
```

Output:

```
black               black, 24.4.2
jupyter             jupyter, 1.0.0
ruff                ruff, 0.3.0
pytest              pytest, 7.2.0
```

### Updating Tools

Update a tool to the latest version:

```bash
uv tool update black
```

Or update all tools:

```bash
uv tool update --all
```

### Uninstalling Tools

Remove a tool:

```bash
uv tool uninstall black
```

It's gone from your computer.

### Example: Setting Up Developer Tools

```bash
# Install tools you use every day
$ uv tool install black     # Code formatter
$ uv tool install ruff      # Linter
$ uv tool install pytest    # Test runner
$ uv tool install jupyterlab # Notebooks

# List what you have
$ uv tool list
black           black, 24.4.2
ruff            ruff, 0.3.0
pytest          pytest, 7.2.0
jupyterlab      jupyterlab, 4.0.0

# Now use them from anywhere
$ black my-script.py
$ ruff check .
$ pytest tests/
$ jupyter lab
```

### Tools vs. Project Dependencies

| Aspect | Tools (`uv tool install`) | Project Deps (`uv add`) |
|--------|---------------------------|------------------------|
| Install | Global (everywhere) | Local (this project) |
| Share | Shared across all projects | Only this project |
| Use case | Daily developer tools | Libraries your code uses |
| Example | `black`, `pytest` | `pandas`, `requests` |

### Things to Remember

- Tools are installed globally
- Use `uvx` for one-off runs
- Use `uv tool install` for regular use
- Tools don't affect your projects

---

# Part 8: The pip Interface

uv includes a mode called the "pip interface" that works like the traditional `pip` tool.

This is useful if:
- You're migrating from pip
- You want to use traditional `pip` workflows
- You need compatibility with existing scripts

## Virtual Environments with uv

### Command: uv venv

**What it does:** Creates an empty virtual environment (without a project).

**Think of it like:** Creating a folder to put Python packages in.

**When to use it:** When you want a virtual environment without the full project structure.

### Basic Usage

Create a virtual environment:

```bash
uv venv
```

This creates a `.venv` folder.

### Activating It (macOS/Linux)

```bash
source .venv/bin/activate
```

Your terminal prompt changes:

```
(.venv) $ 
```

You're now inside the virtual environment.

### Activating It (Windows)

```powershell
.venv\Scripts\activate
```

### Using Without Activation

Or use uv commands directly without activating:

```bash
uv pip install requests
```

uv works with the virtual environment automatically.

### Creating a Venv with Specific Python

```bash
uv venv --python 3.11
```

This creates a virtual environment with Python 3.11.

### Deactivating (macOS/Linux)

```bash
deactivate
```

Back to the normal prompt.

### Example: Using the Traditional Workflow

```bash
# Create a virtual environment
$ uv venv
Using CPython 3.12.4
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate

# Activate it
$ source .venv/bin/activate
(.venv) $ 

# Now you can install packages
(.venv) $ uv pip install requests pandas numpy
Resolved 10 packages in 50ms
Installed 10 packages in 200ms
 + numpy
 + pandas
 + requests
 + ... other dependencies ...

# Check what's installed
(.venv) $ uv pip list
certifi                  2024.7.4
charset-normalizer       3.3.2
idna                     2.5
numpy                    1.24.0
pandas                   2.0.0
requests                 2.31.0
urllib3                  2.0.0

# Deactivate when done
(.venv) $ deactivate
$
```

### Things to Remember

- `uv venv` creates an empty virtual environment
- Useful for simple scripts and traditional workflows
- You can activate/deactivate with `source .venv/bin/activate`
- Or use `uv pip` directly without activation

---

## Installing Packages (pip interface)

### Command: uv pip install

**What it does:** Installs packages into a virtual environment (like `pip install`).

**Think of it like:** Adding books to a shelf in a room.

**When to use it:** When you want to use the pip interface.

### Basic Usage

```bash
uv pip install requests
```

This installs `requests` into the active virtual environment.

### Installing Multiple Packages

```bash
uv pip install requests pandas numpy
```

All three are installed.

### Specifying Versions

```bash
uv pip install requests==2.28.0
uv pip install "pandas>=1.5,<2.0"
```

### Requirements Files

You can install from a file:

```bash
uv pip install -r requirements.txt
```

This installs all packages listed in `requirements.txt`.

### Uninstalling Packages

Remove a package:

```bash
uv pip uninstall requests
```

### Freezing Dependencies

Save what's installed to a file:

```bash
uv pip freeze > requirements.txt
```

This creates a `requirements.txt` with all installed packages and versions.

### Example: Traditional Workflow

```bash
# Create environment
$ uv venv
$ source .venv/bin/activate

# Create requirements file
(.venv) $ cat > requirements.txt << 'EOF'
requests>=2.28.0
pandas>=1.5.0
numpy>=1.20.0
EOF

# Install from requirements
(.venv) $ uv pip install -r requirements.txt
Resolved 12 packages in 50ms
Installed 12 packages in 200ms

# Check what's installed
(.venv) $ uv pip list
numpy                    1.24.0
pandas                   2.0.0
requests                 2.31.0
... 9 more packages ...

# Save current state
(.venv) $ uv pip freeze > requirements-lock.txt

# Later, sync to exact versions
(.venv) $ uv pip sync requirements-lock.txt
```

### Key pip Commands with uv

| Command | What It Does |
|---------|-------------|
| `uv pip install requests` | Install a package |
| `uv pip uninstall requests` | Remove a package |
| `uv pip list` | Show installed packages |
| `uv pip freeze` | List packages with versions |
| `uv pip install -r requirements.txt` | Install from a file |
| `uv pip sync requirements.txt` | Install exact versions from file |

### Things to Remember

- `uv pip` is faster than regular `pip`
- Use with `uv venv` for traditional workflows
- Works with existing `requirements.txt` files
- Perfect for migration from old systems

---

# Part 9: Advanced Topics

## Workspaces

A **workspace** is when you have multiple related projects in one folder.

Think of it like having multiple Python projects that share dependencies.

### When to Use Workspaces

- **Monorepo:** One repository with multiple packages
- **Related projects:** Projects that depend on each other
- **Company structure:** Backend, frontend, cli all in one repo

### Workspace Structure

```
my-monorepo/
├── pyproject.toml          # Root workspace config
├── uv.lock                 # Shared lock file
│
├── packages/
│   ├── api/                # Project 1
│   │   ├── src/
│   │   └── pyproject.toml
│   │
│   ├── cli/                # Project 2
│   │   ├── src/
│   │   └── pyproject.toml
│   │
│   └── shared-lib/         # Shared library
│       ├── src/
│       └── pyproject.toml
```

### Benefits

- **Single lock file:** All projects use same versions
- **Shared dependencies:** Saved disk space
- **Easy collaboration:** Manage multiple projects together
- **Atomic updates:** Change versions once, affects all projects

This is an advanced topic — perfect for larger projects or teams.

---

## Publishing Packages

### Command: uv build

**What it does:** Builds your project for sharing.

**Think of it like:** Packaging a gift to mail to someone.

**When to use it:** When you want to publish to PyPI or share your package.

### Basic Usage

```bash
uv build
```

This creates distributable files in a `dist/` folder:

```
dist/
├── myproject-0.1.0-py3-none-any.whl
└── myproject-0.1.0.tar.gz
```

### Publishing to PyPI

After building:

```bash
uv publish
```

This uploads your package to PyPI (the Python Package Index).

Now anyone can install it with:

```bash
pip install myproject
```

### Before Publishing

Make sure your `pyproject.toml` has:

```toml
[project]
name = "myproject"
version = "0.1.0"
description = "What your project does"
authors = [{name = "Your Name", email = "you@example.com"}]
```

### Example: Publishing Your First Package

```bash
# Create project
$ uv init my-awesome-tool
$ cd my-awesome-tool

# Add code
$ echo "def hello(): print('Hello from my tool')" > src/my_awesome_tool/main.py

# Update pyproject.toml with description
$ # ... edit pyproject.toml ...

# Build it
$ uv build
Building wheel: my-awesome-tool-0.1.0
Building sdist: my-awesome-tool-0.1.0
Created 2 distributions in dist/

# Publish (requires PyPI account)
$ uv publish
# ... upload process ...
# Now on PyPI!
```

This is an advanced topic covered in the Publishing guide.

---

## Caching

uv caches downloaded packages to make things faster.

### Command: uv cache

**What it does:** Manages the cache of downloaded packages.

**Think of it like:** Storing copies of books you've already borrowed so you don't have to fetch them again.

### Checking Cache

```bash
uv cache dir
```

Shows where cached packages are stored.

### Cleaning Cache

Remove old cached packages:

```bash
uv cache clean
```

Or clean everything:

```bash
uv cache clean --all
```

### Prune Cache

Remove packages that aren't being used:

```bash
uv cache prune
```

### Why Caching Matters

When you install a package multiple times:
1. First time: Downloaded from PyPI (slow)
2. Second time: Loaded from cache (fast)

This is why uv is 10-100x faster than pip!

### Things to Remember

- Cache is automatic
- Located in your user directory
- Safe to clean
- Saves time and bandwidth

---

## Configuration

uv can be configured with a `pyproject.toml` or a `uv.toml` file.

### Configuring in pyproject.toml

```toml
[tool.uv]
index-url = "https://pypi.org/simple"
index = [
    {name = "internal", url = "https://internal-pypi.company.com/simple"},
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

### Configuring in .env

You can also set environment variables:

```bash
UV_INDEX=https://custom-pypi.example.com
UV_PYTHON=3.12
```

### Common Configurations

Set a different Python package index:

```toml
[tool.uv]
index-url = "https://custom-pypi.company.com/simple"
```

Set trusted hosts:

```toml
[tool.uv]
trusted-hosts = ["internal-pypi.company.com"]
```

This is an advanced topic used mainly for enterprise setups.

---

# Part 10: Decision Trees & Workflows

## Decision Trees for Common Scenarios

### Scenario 1: "I need to create a new project"

```
Want to create a new project?
    │
    └─> uv init myproject
```

Full command:

```bash
uv init myproject
cd myproject
```

---

### Scenario 2: "I want to use a library"

```
Want to use a library in your project?
    │
    └─> uv add requests
```

Now use in code:

```python
import requests
response = requests.get("https://example.com")
```

---

### Scenario 3: "I have dependencies I installed, want to share them"

```
Want to lock your dependencies?
    │
    ├─> Already have uv.lock?
    │   └─> No? → uv lock
    │   └─> Yes? → uv sync
    │
    └─> Share uv.lock with team
```

---

### Scenario 4: "I cloned someone's project"

```
Cloned a project, want to work on it?
    │
    └─> uv sync
        (Installs exact versions from uv.lock)
```

---

### Scenario 5: "I need Python 3.12 but have 3.10"

```
Need a specific Python version?
    │
    └─> uv python install 3.12
        (Downloads and installs)
    │
    └─> uv python pin 3.12
        (Sets it for this project)
```

---

### Scenario 6: "I want to run a tool once without installing"

```
Want to use a tool temporarily?
    │
    └─> uvx tool-name
        (Downloads, runs, cleans up)
```

Example:

```bash
uvx black my-file.py
```

---

### Scenario 7: "I want to install a tool permanently"

```
Want to install a tool for daily use?
    │
    └─> uv tool install tool-name
        (Installs globally)
    │
    └─> tool-name --version
        (Use it anywhere)
```

Example:

```bash
uv tool install ruff
ruff check .
```

---

### Scenario 8: "I want to write a quick script with dependencies"

```
Want to create a one-off script?
    │
    └─> Create script.py with:
        # /// script
        # dependencies = ["requests"]
        # ///
        import requests
        ...
    │
    └─> uv run script.py
        (Auto-installs dependencies)
```

---

### Scenario 9: "I don't want Python anymore"

```
Want to uninstall Python?
    │
    └─> uv python uninstall 3.10
```

---

### Scenario 10: "I'm using the old way with pip"

```
Using pip directly?
    │
    ├─> Create environment:
    │   └─> uv venv
    │
    ├─> Activate:
    │   └─> source .venv/bin/activate
    │
    ├─> Install:
    │   └─> uv pip install requests
    │
    └─> Save:
        └─> uv pip freeze > requirements.txt
```

---

## Complete Workflows

### Workflow 1: Starting a Web Project

```
Step 1: Create project
$ uv init my-website
$ cd my-website

Step 2: Set Python version
$ uv python pin 3.12

Step 3: Add web dependencies
$ uv add flask
$ uv add --dev pytest black ruff

Step 4: Create basic code
$ cat > src/my_website/main.py << 'EOF'
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run()
EOF

Step 5: Run the project
$ uv run python src/my_website/main.py
 * Running on http://127.0.0.1:5000

Step 6: Share the project
$ git add .
$ git commit -m "Initial web project"
$ git push

Step 7: Later, run tests
$ uv run pytest

Step 8: Format code
$ uv run black .
$ uv run ruff check .

Step 9: Ready to publish?
$ uv build
$ uv publish
```

---

### Workflow 2: Data Science Project

```
Step 1: Create project
$ uv init data-analysis
$ cd data-analysis

Step 2: Add data science libraries
$ uv add pandas numpy matplotlib seaborn scikit-learn

Step 3: Add notebook support
$ uv add --dev jupyter jupyterlab

Step 4: Add testing
$ uv add --dev pytest pytest-cov

Step 5: Organize code
$ mkdir data
$ mkdir notebooks
$ mkdir src/data_analysis

Step 6: Create analysis script
$ cat > src/data_analysis/analyze.py << 'EOF'
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/input.csv')
data.describe()
plt.show()
EOF

Step 7: Run analysis
$ uv run python src/data_analysis/analyze.py

Step 8: Or use notebooks
$ uv run jupyter lab

Step 9: Run tests
$ uv run pytest

Step 10: Freeze dependencies for production
$ uv lock
```

---

### Workflow 3: Contributing to Open Source

```
Step 1: Clone the project
$ git clone https://github.com/someone/coolproject
$ cd coolproject

Step 2: Install dependencies
$ uv sync

Step 3: Make changes
$ # Edit code ...

Step 4: Test your changes
$ uv run pytest

Step 5: Check code quality
$ uv run ruff check .
$ uv run black .

Step 6: Commit changes
$ git add .
$ git commit -m "Fix: bug description"

Step 7: Push and create pull request
$ git push origin feature-branch
$ # Create PR on GitHub

Step 8: If more changes needed
$ # ... edit code again ...
$ uv run pytest
$ git add .
$ git commit -m "Fix: additional changes"
$ git push
```

---

### Workflow 4: Package Development

```
Step 1: Create package
$ uv init my-package
$ cd my-package

Step 2: Set up structure
$ mkdir src/my_package
$ mv src/my_package/__init__.py
$ mv src/my_package/main.py

Step 3: Add dependencies
$ uv add requests
$ uv add --dev pytest black ruff

Step 4: Update metadata
$ # Edit pyproject.toml with:
  [project]
  name = "my-package"
  version = "0.1.0"
  description = "What it does"
  authors = [{name = "Your Name"}]

Step 5: Write tests
$ mkdir tests
$ cat > tests/test_main.py << 'EOF'
def test_something():
    assert True
EOF

Step 6: Test thoroughly
$ uv run pytest

Step 7: Format and lint
$ uv run black .
$ uv run ruff check .

Step 8: Build package
$ uv build

Step 9: Test installation
$ uv venv test-env
$ source test-env/bin/activate
$ pip install dist/*.whl
$ python -c "import my_package; ..."

Step 10: Publish
$ uv publish
```

---

# Part 11: Command Reference

## Project Commands

### uv init

**Command:**

```bash
uv init [PROJECT_NAME]
```

**What it does:** Creates a new Python project with all necessary files and structure.

**Think of it like:** Creating a new folder and setting up templates for a project.

**When to use it:** Every time you start a new project.

**Example:**

```bash
$ uv init my-project
Created project `my-project` at `/home/user/my-project`

$ cd my-project
$ ls
README.md      pyproject.toml    src/    uv.lock    .python-version
```

**Output:** A new project directory with:
- `pyproject.toml` (configuration)
- `uv.lock` (dependencies lock file)
- `.python-version` (Python version file)
- `src/` (source code directory)
- `.venv/` (virtual environment)

**Common mistakes:**
- Running in wrong directory
- Trying to init twice in same location
- Not navigating into the project after creating it

**Things to remember:**
- Creates virtual environment automatically
- All files created at once
- Ready to code immediately

---

### uv add

**Command:**

```bash
uv add PACKAGE [PACKAGE2 ...]
uv add --dev PACKAGE  # Development dependency
```

**What it does:** Adds a Python package to your project.

**Think of it like:** Adding a new tool to your toolbox.

**When to use it:** When you need to use a library in your code.

**Example:**

```bash
$ uv add requests
Resolved 4 packages in 50ms
Installed 4 packages in 100ms
 + certifi==2024.7.4
 + charset-normalizer==3.3.2
 + idna==2.5
 + requests==2.31.0

$ uv add --dev pytest
 + pytest==7.2.0
```

**Output:** Package is installed and added to `pyproject.toml`:

```toml
[project]
dependencies = [
    "requests>=2.31.0",
]

[project.optional-dependencies]
dev = ["pytest>=7.0"]
```

**Common mistakes:**
- Typo in package name
- Adding package that doesn't exist
- Not using `--dev` for development-only packages

**Things to remember:**
- Updates `pyproject.toml` automatically
- Updates `uv.lock` automatically
- Can use version specifiers: `uv add "requests>=2.0,<3.0"`

---

### uv remove

**Command:**

```bash
uv remove PACKAGE [PACKAGE2 ...]
```

**What it does:** Removes a package from your project.

**Think of it like:** Returning a tool and removing it from your toolbox.

**When to use it:** When you no longer need a library.

**Example:**

```bash
$ uv remove requests
Removed 1 package
Uninstalled requests==2.31.0
```

**Output:** Package is removed from `pyproject.toml` and uninstalled.

**Common mistakes:**
- Removing package your code still uses
- Typo in package name

**Things to remember:**
- Removes from dependencies immediately
- Make sure no code uses it before removing

---

### uv run

**Command:**

```bash
uv run [SCRIPT.py | COMMAND]
uv run --python VERSION COMMAND
```

**What it does:** Runs Python code in the project's virtual environment.

**Think of it like:** Pressing "Play" to execute your code.

**When to use it:** Every time you want to run code.

**Example:**

```bash
$ uv run python src/myproject/main.py

$ uv run python -c "print('Hello')"

$ uv run --python 3.11 python --version
Python 3.11.9
```

**Output:** Depends on what you run.

**Common mistakes:**
- Forgetting `uv run` and trying to run Python directly
- Not specifying the Python file to run
- Trying to manually activate virtual environment

**Things to remember:**
- Automatically uses your project's virtual environment
- No need to activate manually
- Can override Python version with `--python`

---

### uv sync

**Command:**

```bash
uv sync
uv sync --dev  # Include development dependencies
```

**What it does:** Installs all packages from `uv.lock` into your virtual environment.

**Think of it like:** Pulling the latest library books based on a reading list.

**When to use it:** After pulling from Git or when `uv.lock` changes.

**Example:**

```bash
$ git pull
# ... uv.lock has been updated by colleague ...

$ uv sync
Resolved 12 packages in 50ms
Installed 12 packages in 200ms
```

**Output:** Packages are installed exactly as specified in `uv.lock`.

**Common mistakes:**
- Using `uv add` when you should use `uv sync`
- Trying to install development dependencies with just `uv sync`

**Things to remember:**
- Uses `uv.lock` not `pyproject.toml`
- Ensures everyone has same versions
- Doesn't modify any files

---

### uv lock

**Command:**

```bash
uv lock
```

**What it does:** Updates `uv.lock` with current exact versions.

**Think of it like:** Freezing a snapshot of what's installed.

**When to use it:** Before committing changes to Git.

**Example:**

```bash
$ uv add requests
$ uv lock  # Update lock file
Resolved 4 packages in 50ms
$ git add uv.lock
$ git commit -m "Add requests library"
```

**Output:** `uv.lock` is updated with exact versions.

**Common mistakes:**
- Forgetting to run before committing
- Modifying `uv.lock` manually

**Things to remember:**
- Automatic with `uv add` / `uv remove`
- Run explicitly when needed
- Always commit to Git

---

### uv tree

**Command:**

```bash
uv tree
```

**What it does:** Shows dependency tree with all packages and sub-dependencies.

**Think of it like:** Creating a family tree of your dependencies.

**When to use it:** When you want to understand what's installed.

**Example:**

```bash
$ uv tree
myproject
├── pandas==2.0.0
│   ├── numpy==1.24.0
│   ├── python-dateutil==2.8.2
│   └── pytz==2023.3
└── requests==2.31.0
    ├── certifi==2024.7.4
    ├── charset-normalizer==3.3.2
    └── urllib3==2.0.0
```

**Output:** Tree structure showing all dependencies and their dependencies.

**Common mistakes:**
- None really — it's informational only

**Things to remember:**
- Helps debug dependency conflicts
- Shows why packages are installed
- Useful for understanding what's consuming space

---

### uv export

**Command:**

```bash
uv export
uv export > requirements.txt
uv export --dev > requirements-all.txt
```

**What it does:** Exports dependencies to a `requirements.txt` format.

**Think of it like:** Converting a structured list to a simpler format.

**When to use it:** When you need compatibility with other tools.

**Example:**

```bash
$ uv export > requirements.txt
$ cat requirements.txt
certifi==2024.7.4
charset-normalizer==3.3.2
idna==2.5
numpy==1.24.0
pandas==2.0.0
python-dateutil==2.8.2
pytz==2023.3
requests==2.31.0
urllib3==2.0.0
```

**Output:** A `requirements.txt` file with all packages.

**Common mistakes:**
- Trying to use exported file instead of `uv.lock`
- Not using `--dev` when needed

**Things to remember:**
- Export is for compatibility only
- Prefer `uv.lock` when possible
- Useful for Docker or legacy systems

---

## Python Commands

### uv python install

**Command:**

```bash
uv python install VERSION [VERSION2 ...]
```

**What it does:** Downloads and installs a Python version.

**Think of it like:** Downloading a specific version of an app.

**When to use it:** When you need a specific Python version.

**Example:**

```bash
$ uv python install 3.12
$ uv python install 3.10 3.11 3.12
$ uv python install 3.12.4  # Specific patch version
```

**Output:**

```
Searching for Python versions matching: Python 3.12
Downloading cpython-3.12.4-macos-aarch64-none...
Downloaded in 2.34s
Installing cpython-3.12.4-macos-aarch64-none...
Installed in 1.23s
  + cpython-3.12.4-macos-aarch64-none
```

**Common mistakes:**
- Installing version that doesn't exist
- Installing without specifying version

**Things to remember:**
- uv downloads Python for you
- No need to manage Python manually
- Stored in a global location

---

### uv python list

**Command:**

```bash
uv python list
```

**What it does:** Shows all installed Python versions.

**Think of it like:** Listing all the apps you have installed.

**When to use it:** When you want to see available Python versions.

**Example:**

```bash
$ uv python list
cpython-3.10.14   /home/user/.local/share/uv/pythons/cpython-3.10.14
cpython-3.11.9    /home/user/.local/share/uv/pythons/cpython-3.11.9
cpython-3.12.4    /home/user/.local/share/uv/pythons/cpython-3.12.4 (default)
```

**Output:** List of installed Python versions with their locations.

**Common mistakes:**
- None — it's informational

**Things to remember:**
- Shows which is default
- Shows full paths
- Useful for troubleshooting

---

### uv python pin

**Command:**

```bash
uv python pin VERSION
uv python pin --ignore-requires-python
```

**What it does:** Locks your project to a specific Python version.

**Think of it like:** Writing "This project requires Python 3.12" on the folder.

**When to use it:** When you know which Python version your project needs.

**Example:**

```bash
$ uv python pin 3.12
Pinned `.python-version` to `3.12`

$ cat .python-version
3.12
```

**Output:** `.python-version` file is created/updated.

**Common mistakes:**
- Pinning to version that doesn't exist
- Forgetting to check `.python-version` works

**Things to remember:**
- Creates `.python-version` file
- Commit to Git for team consistency
- Only affects this project

---

### uv python find

**Command:**

```bash
uv python find VERSION
```

**What it does:** Finds a Python version without installing.

**Think of it like:** Searching for a version before downloading.

**When to use it:** When you want to check if a version is available.

**Example:**

```bash
$ uv python find 3.12
/home/user/.local/share/uv/pythons/cpython-3.12.4
```

**Output:** Path to the Python version if found.

**Common mistakes:**
- None — it's informational

**Things to remember:**
- Doesn't install anything
- Returns path if found
- Useful for scripting

---

### uv python uninstall

**Command:**

```bash
uv python uninstall VERSION [VERSION2 ...]
```

**What it does:** Removes an installed Python version.

**Think of it like:** Uninstalling an app from your computer.

**When to use it:** When you don't need a Python version anymore.

**Example:**

```bash
$ uv python uninstall 3.10
Uninstalled cpython-3.10.14
```

**Output:** Python version is removed from your computer.

**Common mistakes:**
- Uninstalling version your project uses
- Typo in version number

**Things to remember:**
- Frees up disk space
- Can reinstall later if needed
- Check all projects before uninstalling

---

## Tool Commands

### uv tool install

**Command:**

```bash
uv tool install PACKAGE [PACKAGE2 ...]
uv tool install --from PACKAGE EXECUTABLE
```

**What it does:** Installs a Python tool globally.

**Think of it like:** Installing an app on your computer.

**When to use it:** When you want to use a tool regularly.

**Example:**

```bash
$ uv tool install black
$ uv tool install pytest ruff black
```

**Output:**

```
Resolved 1 package in 6ms
Installed 1 package in 2ms
 + black==24.4.2
Installed 1 executable: black

# Now use it anywhere
$ black my-file.py
```

**Common mistakes:**
- Installing package that isn't a tool
- Not checking if it's already installed

**Things to remember:**
- Global installation
- Different from `uv add`
- Can use from anywhere

---

### uv tool run

**Command:**

```bash
uv tool run PACKAGE [ARGS...]
uvx PACKAGE [ARGS...]  # Shorthand
```

**What it does:** Runs a Python tool in an isolated environment without installing.

**Think of it like:** Renting a tool instead of buying it.

**When to use it:** When you want to try a tool or use it once.

**Example:**

```bash
$ uvx black --version
black, 24.4.2

$ uvx ruff check .
$ uvx httpie GET https://example.com
```

**Output:** Tool runs and either produces output or makes changes.

**Common mistakes:**
- Forgetting that it's temporary (not installed)
- Trying to run a tool that doesn't exist

**Things to remember:**
- `uvx` is alias for `uv tool run`
- Temporary, nothing is installed
- Great for trying tools

---

### uv tool list

**Command:**

```bash
uv tool list
```

**What it does:** Shows all installed tools.

**Think of it like:** Listing all the apps you have installed.

**When to use it:** When you want to see what tools are available.

**Example:**

```bash
$ uv tool list
black               black, 24.4.2
jupyter             jupyter, 1.0.0
ruff                ruff, 0.3.0
```

**Output:** List of installed tools with versions.

**Common mistakes:**
- None — it's informational

**Things to remember:**
- Shows only installed tools (not available tools)
- Different from `uv tool run`

---

### uv tool update

**Command:**

```bash
uv tool update [TOOL_NAME]
uv tool update --all
```

**What it does:** Updates a tool to the latest version.

**Think of it like:** Installing an update for an app.

**When to use it:** When a tool has a new version.

**Example:**

```bash
$ uv tool update black
 + black==24.5.0

$ uv tool update --all
Updated black to 24.5.0
Updated ruff to 0.4.0
Updated pytest to 7.3.0
```

**Output:** Tool is updated to the latest version.

**Common mistakes:**
- Updating tool that breaks compatibility
- Not testing after update

**Things to remember:**
- Individual or all tools
- Updates to latest version
- Safe to do regularly

---

### uv tool uninstall

**Command:**

```bash
uv tool uninstall TOOL [TOOL2 ...]
```

**What it does:** Removes an installed tool.

**Think of it like:** Uninstalling an app from your computer.

**When to use it:** When you don't use a tool anymore.

**Example:**

```bash
$ uv tool uninstall black
Uninstalled black

$ uv tool list
ruff                ruff, 0.3.0
pytest              pytest, 7.2.0
```

**Output:** Tool is removed from your computer.

**Common mistakes:**
- Uninstalling tool you still use
- Typo in tool name

**Things to remember:**
- Only removes the tool
- Your projects are unaffected
- Can reinstall later

---

## Pip Commands

### uv venv

**Command:**

```bash
uv venv [PATH]
uv venv --python VERSION
```

**What it does:** Creates an empty virtual environment.

**Think of it like:** Creating a separate room for Python packages.

**When to use it:** When you want a virtual environment without a full project.

**Example:**

```bash
$ uv venv
Using CPython 3.12.4
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate

$ source .venv/bin/activate
(.venv) $
```

**Output:** `.venv` directory is created and ready to use.

**Common mistakes:**
- Creating venv inside another venv
- Not activating before installing

**Things to remember:**
- Creates `.venv` folder
- Need to activate/deactivate
- Or use `uv pip` directly without activation

---

### uv pip install

**Command:**

```bash
uv pip install PACKAGE [PACKAGE2 ...]
uv pip install -r requirements.txt
```

**What it does:** Installs packages into a virtual environment.

**Think of it like:** Adding books to a shelf.

**When to use it:** When using the pip interface (traditional workflows).

**Example:**

```bash
(.venv) $ uv pip install requests
Resolved 4 packages in 50ms
Installed 4 packages in 100ms
 + certifi==2024.7.4
 + charset-normalizer==3.3.2
 + idna==2.5
 + requests==2.31.0

(.venv) $ uv pip install -r requirements.txt
```

**Output:** Packages are installed into active virtual environment.

**Common mistakes:**
- Forgetting to activate virtual environment
- Typo in package name

**Things to remember:**
- Much faster than regular `pip`
- Works with existing `requirements.txt`
- Use with `uv venv`

---

### uv pip uninstall

**Command:**

```bash
uv pip uninstall PACKAGE [PACKAGE2 ...]
uv pip uninstall -r requirements.txt
```

**What it does:** Removes packages from virtual environment.

**Think of it like:** Removing books from a shelf.

**When to use it:** When you don't need packages anymore.

**Example:**

```bash
(.venv) $ uv pip uninstall requests
Uninstalled requests==2.31.0
```

**Output:** Package is removed from environment.

**Common mistakes:**
- Uninstalling package code still uses
- Typo in package name

**Things to remember:**
- Immediate effect
- Check code before removing
- Can reinstall later

---

### uv pip list

**Command:**

```bash
uv pip list
```

**What it does:** Shows all installed packages in active environment.

**Think of it like:** Listing all books on your shelf.

**When to use it:** When you want to see what's installed.

**Example:**

```bash
(.venv) $ uv pip list
certifi          2024.7.4
charset-normalizer 3.3.2
idna             2.5
requests         2.31.0
```

**Output:** List of installed packages with versions.

**Common mistakes:**
- None — it's informational

**Things to remember:**
- Shows installed packages only
- Useful for checking versions
- Can be grepped/piped

---

### uv pip freeze

**Command:**

```bash
uv pip freeze
uv pip freeze > requirements.txt
```

**What it does:** Saves all installed packages to `requirements.txt` format.

**Think of it like:** Creating a snapshot of what's on your shelf.

**When to use it:** When you want to save the current state.

**Example:**

```bash
(.venv) $ uv pip freeze > requirements.txt
(.venv) $ cat requirements.txt
certifi==2024.7.4
charset-normalizer==3.3.2
idna==2.5
requests==2.31.0
```

**Output:** `requirements.txt` file with exact versions.

**Common mistakes:**
- Overwriting existing `requirements.txt`
- Not adding to `.gitignore` if auto-generated

**Things to remember:**
- Useful for sharing requirements
- Captures exact versions
- Good practice: commit to Git

---

### uv pip sync

**Command:**

```bash
uv pip sync requirements.txt
```

**What it does:** Installs packages to exact versions specified in file.

**Think of it like:** Reorganizing your shelf to match a recipe.

**When to use it:** When you want exact version matching.

**Example:**

```bash
(.venv) $ uv pip sync requirements.txt
Resolved 4 packages in 50ms
Installed 4 packages in 100ms
```

**Output:** Virtual environment matches `requirements.txt` exactly.

**Common mistakes:**
- Confusing with `uv pip install`
- Using with modified file

**Things to remember:**
- Exact versions from file
- Uninstalls packages not in file
- Useful for reproducible environments

---

### uv pip compile

**Command:**

```bash
uv pip compile requirements.in
uv pip compile requirements.in --output-file requirements.txt
uv pip compile --universal requirements.in
```

**What it does:** Converts flexible requirements to exact specifications.

**Think of it like:** Converting a recipe to exact measurements.

**When to use it:** When you want reproducible requirements.

**Example:**

```bash
$ cat requirements.in
requests>=2.28
pandas>=1.5

$ uv pip compile requirements.in
Resolved 12 packages in 50ms
# requirements.txt
certifi==2024.7.4
charset-normalizer==3.3.2
idna==2.5
numpy==1.24.0
pandas==2.0.0
python-dateutil==2.8.2
pytz==2023.3
requests==2.31.0
urllib3==2.0.0
```

**Output:** `requirements.txt` with exact versions.

**Common mistakes:**
- Trying to compile `.txt` files instead of `.in`
- Not understanding difference from `freeze`

**Things to remember:**
- Works with `requirements.in` files
- Creates deterministic output
- Useful for controlling versions

---

## Cache & Utility Commands

### uv cache clean

**Command:**

```bash
uv cache clean
uv cache clean --all
```

**What it does:** Removes cached packages.

**Think of it like:** Deleting temporary files to free space.

**When to use it:** When you want to free disk space.

**Example:**

```bash
$ uv cache clean
Removed 123 cache entries (1.2 GB freed)
```

**Output:** Cache is cleaned, space is freed.

**Common mistakes:**
- Thinking cleaning cache breaks projects (it doesn't)
- Not realizing you'll redownload packages

**Things to remember:**
- Safe to run anytime
- Frees disk space
- Projects unaffected

---

### uv cache dir

**Command:**

```bash
uv cache dir
```

**What it does:** Shows where cache is stored.

**Think of it like:** Finding where temporary files are kept.

**When to use it:** When you want to know cache location.

**Example:**

```bash
$ uv cache dir
/home/user/.cache/uv
```

**Output:** Path to cache directory.

**Common mistakes:**
- None — it's informational

**Things to remember:**
- Shows cache location
- Don't edit manually
- Safe to browse

---

### uv cache prune

**Command:**

```bash
uv cache prune
```

**What it does:** Removes unused cached packages.

**Think of it like:** Organizing and removing obsolete items.

**When to use it:** When cache is getting large.

**Example:**

```bash
$ uv cache prune
Removed 45 unused cache entries (500 MB freed)
```

**Output:** Unused cache is removed.

**Common mistakes:**
- None — it's safe

**Things to remember:**
- Smarter than `clean` (keeps useful packages)
- Safe to run regularly
- Frees more space than `clean` sometimes

---

### uv help

**Command:**

```bash
uv help
uv help COMMAND
```

**What it does:** Shows help information.

**Think of it like:** Reading the manual.

**When to use it:** When you forget how a command works.

**Example:**

```bash
$ uv help add
Add a package to the project

USAGE:
    uv add [OPTIONS] [PACKAGES]...

OPTIONS:
    -h, --help    Print help
```

**Output:** Help information for the command.

**Common mistakes:**
- None — it's helpful

**Things to remember:**
- Works for all commands
- Faster than looking online
- Shows examples sometimes

---

### uv version

**Command:**

```bash
uv --version
uv version
```

**What it does:** Shows installed uv version.

**Think of it like:** Checking app version.

**When to use it:** When you want to know which version you have.

**Example:**

```bash
$ uv --version
uv 0.5.4
```

**Output:** Version number.

**Common mistakes:**
- None — it's informational

**Things to remember:**
- Useful for troubleshooting
- Good to know when reporting bugs

---

### uv self update

**Command:**

```bash
uv self update
```

**What it does:** Updates uv to the latest version.

**Think of it like:** Updating an app.

**When to use it:** When new features or fixes are released.

**Example:**

```bash
$ uv self update
Updated uv from 0.5.4 to 0.5.5
```

**Output:** uv is updated.

**Common mistakes:**
- None — it's safe

**Things to remember:**
- Updates uv itself, not your projects
- Good practice to keep updated
- Check changelog for breaking changes

---

# Part 12: Cheat Sheets

## The Essential Cheat Sheet

### Creating & Managing Projects

```bash
uv init myproject          # Create new project
cd myproject               # Navigate into it
uv add requests            # Add library
uv remove requests         # Remove library
uv lock                    # Update lock file
uv sync                    # Install from lock file
uv tree                    # View dependencies
```

### Running Code

```bash
uv run python script.py    # Run Python script
uv run python -c "print('hi')"  # Run command
uv run my-command          # Run installed tool
```

### Python Versions

```bash
uv python install 3.12    # Download Python 3.12
uv python list             # List installed versions
uv python pin 3.12         # Set for this project
uv python uninstall 3.10   # Remove Python 3.10
```

### Tools

```bash
uvx black --version        # Run tool once (like black)
uv tool install black      # Install tool permanently
uv tool list               # List installed tools
uv tool update black       # Update tool
uv tool uninstall black    # Remove tool
```

### Virtual Environments (Pip Style)

```bash
uv venv                    # Create environment
source .venv/bin/activate  # Activate (macOS/Linux)
uv pip install requests    # Install package
uv pip list                # Show installed
uv pip freeze > requirements.txt  # Save requirements
deactivate                 # Leave environment
```

### Cache & Utility

```bash
uv cache clean             # Remove cache
uv cache prune             # Remove unused cache
uv help COMMAND            # Get help
uv --version               # Check version
uv self update             # Update uv itself
```

---

## Daily Workflow Cheat Sheet

### Starting Your Day

```bash
# 1. Navigate to project
cd my-project

# 2. Pull latest changes
git pull

# 3. Install dependencies
uv sync

# 4. Start coding
# Edit files...

# 5. Test your changes
uv run pytest

# 6. Format and check
uv run black .
uv run ruff check .
```

### Adding a New Library

```bash
# 1. Add library
uv add pandas

# 2. Use it in code
# import pandas as pd
# ... write code ...

# 3. Test it works
uv run python my-script.py

# 4. Commit changes
git add pyproject.toml uv.lock
git commit -m "Add pandas"
git push
```

### Sharing Your Work

```bash
# 1. Make sure lock file is up to date
uv lock

# 2. Commit everything
git add .
git commit -m "My changes"

# 3. Push to share
git push

# Others can now:
git pull
uv sync  # Get exact same versions
```

### Trying New Tools

```bash
# Try without installing
uvx black my-file.py

# If you like it, install it
uv tool install black

# Now use it anytime
black my-file.py
```

---

## Beginner Cheat Sheet

### I want to...

**Create a new project**
```bash
uv init myproject
cd myproject
```

**Use a library**
```bash
uv add requests
# Then: import requests
```

**Run my code**
```bash
uv run python my-script.py
```

**Work on someone else's project**
```bash
git clone repo-url
cd repo-folder
uv sync
```

**Write a quick script with dependencies**
```bash
cat > script.py << 'EOF'
# /// script
# dependencies = ["requests"]
# ///
import requests
EOF

uv run script.py
```

**Try a new tool**
```bash
uvx tool-name
```

**Install a tool I use often**
```bash
uv tool install tool-name
```

**Check what's installed**
```bash
uv tree          # All dependencies
uv tool list     # All tools
```

**Remove a library**
```bash
uv remove requests
```

**Clean up my computer**
```bash
uv cache clean
```

---

## Troubleshooting Cheat Sheet

### "Module not found" error

**Problem:** You get `ModuleNotFoundError: No module named 'requests'`

**Solution:** Install the package
```bash
uv add requests
```

Or make sure you're running with `uv run`:
```bash
uv run python my-script.py  # Correct
python my-script.py          # Wrong — missing packages
```

---

### "Wrong Python version" error

**Problem:** Your code needs Python 3.12 but you have 3.10

**Solution:** Install Python 3.12
```bash
uv python install 3.12
uv python pin 3.12
```

---

### "Permission denied" on Windows

**Problem:** Can't run uv or script on Windows

**Solution:** Use PowerShell as Administrator or use Python:
```bash
python -m uv --version
```

---

### "Package not found" error

**Problem:** Package name is wrong or doesn't exist

**Solution:** Check the correct name on PyPI:
```bash
# Wrong:
uv add reqeusts  # Typo!

# Correct:
uv add requests
```

---

### "Virtual environment issues"

**Problem:** Stuck or broken virtual environment

**Solution:** Remove and recreate:
```bash
rm -rf .venv        # Linux/macOS
rmdir /s .venv      # Windows

uv sync             # Recreate from uv.lock
```

---

### "Dependency conflict"

**Problem:** Two packages need different versions of the same library

**Solution:** Use `uv tree` to see the issue:
```bash
uv tree
# Look for conflicting versions

# Then either:
uv remove package-causing-conflict
# Or:
uv add "problematic-package@specific-version"
```

---

### "Cache problems"

**Problem:** Strange errors or files not downloading

**Solution:** Clean the cache:
```bash
uv cache clean

# Then retry:
uv sync
# or
uv run python script.py
```

---

# Part 13: Comparison Tables

## uv vs Other Tools

### uv vs pip

| Feature | pip | uv |
|---------|-----|-----|
| Installation | Included with Python | Standalone |
| Speed | Slow | 10-100x faster |
| Dependency resolution | Basic | Advanced |
| Lock files | No | Yes (`uv.lock`) |
| Version management | Limited | Full |
| Python version management | No | Yes |
| Tool installation | No | Yes |
| Project management | No | Yes |
| Command count | Few | Many |
| Virtual env creation | Via venv | Built-in |

---

### uv vs Poetry

| Feature | Poetry | uv |
|---------|--------|-----|
| Project management | Yes | Yes |
| Dependency resolution | Yes | Yes (faster) |
| Lock files | Yes | Yes |
| Tool installation | No | Yes |
| Python version management | Limited | Full |
| Speed | Slower | Much faster |
| Pip replacement | No | Yes |
| Virtual environments | Limited | Built-in |
| Learning curve | Steep | Gentle |
| Active development | Slow | Very active |

---

### uv vs pipx

| Feature | pipx | uv |
|---------|------|-----|
| Purpose | Install tools | Install tools + everything |
| Tool management | Yes | Yes |
| Project management | No | Yes |
| Dependency management | Limited | Full |
| Speed | Slow | Fast |
| Virtual environments | Limited | Full |
| Can use for projects | No | Yes |
| Learning curve | Simple | Simple |

---

### uv vs virtualenv

| Feature | virtualenv | uv |
|---------|-----------|-----|
| Create venv | Yes | Yes |
| Activate/deactivate | Yes | Optional |
| Manage dependencies | No | Yes |
| Create projects | No | Yes |
| Install Python | No | Yes |
| Manage tools | No | Yes |
| Speed | Moderate | Very fast |

---

### uv vs pyenv

| Feature | pyenv | uv |
|---------|-------|-----|
| Install Python | Yes | Yes |
| Manage versions | Yes | Yes |
| Create projects | No | Yes |
| Manage dependencies | No | Yes |
| Install tools | No | Yes |
| Speed | Moderate | Very fast |
| All-in-one | No | Yes |
| Cross-platform | Limited | Excellent |

---

## Why Use uv Instead?

**Single tool replaces:**
- `pip` (package installation)
- `pip-tools` (lock files)
- `virtualenv` (virtual environments)
- `venv` (virtual environments)
- `pyenv` (Python version management)
- `pipx` (tool installation)
- `poetry` (project management)
- `twine` (publishing)

**All in one tool.**

**Key advantages:**
- **Much faster** — 10-100x speedup
- **Simpler** — One tool, consistent interface
- **More complete** — Everything built-in
- **Better designed** — Learned from existing tools
- **Active development** — Regular updates and improvements
- **Beginner-friendly** — Easy to learn
- **Cross-platform** — Works on macOS, Linux, Windows

---

# Part 14: Real-World Examples

## Example 1: AI Chatbot Project

### The Plan

Build a simple chatbot that uses the OpenAI API.

### Step 1: Create Project

```bash
$ uv init ai-chatbot
Created project `ai-chatbot` at `/home/user/ai-chatbot`

$ cd ai-chatbot
```

### Step 2: Set Python Version

```bash
$ uv python pin 3.12
Pinned `.python-version` to `3.12`
```

### Step 3: Add Dependencies

```bash
# OpenAI library for AI
$ uv add openai

# Flask for simple web interface
$ uv add flask

# Environment variables for API key
$ uv add python-dotenv

# Development tools
$ uv add --dev pytest black ruff
```

### Step 4: Create Code

Create `.env` file:

```
OPENAI_API_KEY=your-api-key-here
```

Create `src/ai_chatbot/main.py`:

```python
from openai import OpenAI
from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json.get('message')
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}]
    )
    
    return jsonify({
        "response": response.choices[0].message.content
    })

if __name__ == '__main__':
    app.run(debug=True)
```

### Step 5: Test the Code

```bash
$ uv run python src/ai_chatbot/main.py
 * Running on http://127.0.0.1:5000

# In another terminal:
$ curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello, how are you?"}'
```

### Step 6: Check Code Quality

```bash
$ uv run black .
reformatted src/ai_chatbot/main.py
All done! ✨ 🍰 ✨

$ uv run ruff check .
All checks passed!
```

### Step 7: Test Your Code

Create `tests/test_main.py`:

```python
def test_imports():
    from ai_chatbot.main import app
    assert app is not None

def test_flask_setup():
    from ai_chatbot.main import app
    client = app.test_client()
    assert client is not None
```

Run tests:

```bash
$ uv run pytest
tests/test_main.py::test_imports PASSED
tests/test_main.py::test_flask_setup PASSED
2 passed in 0.23s
```

### Step 8: Commit to Git

```bash
$ git init
$ git add .
$ git commit -m "Initial AI chatbot project"
$ git push origin main
```

### Step 9: Share With Team

Team members can now:

```bash
$ git clone repo-url
$ cd ai-chatbot
$ uv sync
$ uv run python src/ai_chatbot/main.py
```

They get exactly the same versions and environment.

---

## Example 2: Web API Project

### The Plan

Build a simple REST API for a todo list.

### Setup

```bash
$ uv init todo-api
$ cd todo-api
$ uv python pin 3.12

# Add FastAPI (modern web framework)
$ uv add fastapi uvicorn sqlalchemy pydantic

# Development tools
$ uv add --dev pytest pytest-asyncio black ruff mypy
```

### Project Structure

```
todo-api/
├── src/
│   └── todo_api/
│       ├── __init__.py
│       ├── main.py
│       ├── models.py
│       └── database.py
├── tests/
│   ├── test_api.py
│   └── test_models.py
├── pyproject.toml
├── uv.lock
└── .python-version
```

### Running the API

```bash
$ uv run uvicorn src.todo_api.main:app --reload
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete
```

### Testing the API

```bash
$ curl http://localhost:8000/docs
# Opens interactive API documentation

$ curl http://localhost:8000/todos
{"todos": []}
```

### Development Workflow

```bash
# Format code
$ uv run black .

# Check types
$ uv run mypy src/

# Lint
$ uv run ruff check .

# Test
$ uv run pytest -v
tests/test_api.py::test_get_todos PASSED
tests/test_api.py::test_create_todo PASSED
2 passed in 0.45s
```

---

## Example 3: Data Analysis Project

### The Plan

Analyze COVID-19 data and create visualizations.

### Setup

```bash
$ uv init covid-analysis
$ cd covid-analysis
$ uv python pin 3.11

# Data analysis libraries
$ uv add pandas numpy matplotlib seaborn scipy scikit-learn

# Jupyter for interactive analysis
$ uv add --dev jupyterlab

# Reproducibility tools
$ uv add --dev pytest
```

### Project Structure

```
covid-analysis/
├── data/
│   └── covid-data.csv
├── notebooks/
│   ├── 01_exploration.ipynb
│   └── 02_analysis.ipynb
├── src/
│   └── covid_analysis/
│       ├── load_data.py
│       ├── analyze.py
│       └── visualize.py
├── results/
│   └── charts/
├── tests/
│   └── test_analysis.py
├── pyproject.toml
└── README.md
```

### Analysis Code

`src/covid_analysis/analyze.py`:

```python
import pandas as pd
import numpy as np
from scipy import stats

def load_data(filename):
    return pd.read_csv(filename)

def calculate_statistics(df):
    return {
        'mean_cases': df['cases'].mean(),
        'std_dev': df['cases'].std(),
        'median': df['cases'].median(),
    }

def trend_analysis(df):
    x = np.arange(len(df))
    y = df['cases'].values
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    return {
        'slope': slope,
        'r_squared': r_value ** 2,
        'trend': 'increasing' if slope > 0 else 'decreasing'
    }
```

### Running Analysis

```bash
# Interactive notebook
$ uv run jupyter lab
# Opens http://localhost:8888 with notebooks

# Or run scripts
$ uv run python src/covid_analysis/analyze.py

# Run tests
$ uv run pytest
```

### Sharing Results

```bash
# Export for others to use
$ uv export > requirements.txt

# Or better — share the project
$ git add .
$ git commit -m "COVID analysis with 95% trend accuracy"
$ git push

# Others can reproduce exactly:
$ git clone repo-url
$ cd covid-analysis
$ uv sync
$ uv run jupyter lab
```

---

# Appendix: Troubleshooting & FAQ

## Common Problems & Solutions

### Problem: "command not found: uv"

**Cause:** uv is not installed or not in your PATH.

**Solution:**
```bash
# Reinstall uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or check if it's installed
which uv

# If not found, add to PATH manually
export PATH="$HOME/.local/bin:$PATH"
```

---

### Problem: "ModuleNotFoundError: No module named 'requests'"

**Cause:** Package isn't installed or you're not using `uv run`.

**Solution:**
```bash
# Install package
uv add requests

# Always run code with uv run
uv run python my-script.py  # Correct
python my-script.py          # Wrong
```

---

### Problem: "Virtual environment is broken"

**Cause:** Files got corrupted or deleted.

**Solution:**
```bash
# Delete and recreate
rm -rf .venv       # or rmdir /s .venv on Windows
uv sync            # Recreates from uv.lock
```

---

### Problem: "Python version not found"

**Cause:** Trying to use a Python version that isn't installed.

**Solution:**
```bash
# Check what's installed
uv python list

# Install needed version
uv python install 3.12

# Set for project
uv python pin 3.12
```

---

### Problem: "Package version conflict"

**Cause:** Two packages need incompatible versions of same library.

**Solution:**
```bash
# See the problem
uv tree

# Check which package is causing it
# Remove one package and find compatible version
uv remove problem-package
uv add "problem-package@version"
```

---

### Problem: "Slow installation"

**Cause:** Cache missing or downloading for first time.

**Solution:**
```bash
# Clean cache and retry
uv cache clean
uv sync

# Or check cache status
uv cache dir
```

---

## Frequently Asked Questions

### Q: Do I need to activate the virtual environment?

**A:** No, not with uv. Just use `uv run` and uv handles the activation automatically.

Old way:
```bash
source .venv/bin/activate
python my-script.py
deactivate
```

New way (uv):
```bash
uv run python my-script.py
```

---

### Q: How do I upgrade all my dependencies?

**A:** Update each package individually:

```bash
$ uv add requests --upgrade
$ uv add pandas --upgrade
```

Or update all at once by removing and re-adding:

```bash
$ uv add --force requests pandas numpy
```

---

### Q: Can I use both `uv` and `pip`?

**A:** Not in the same project. Choose one.

For projects, use `uv init` and `uv add`.

For simple scripts, you can use either `uv venv` + `uv pip` or regular pip, but not mixed.

---

### Q: How do I share my project?

**A:** Just commit to Git:

```bash
git add .
git commit -m "My project"
git push
```

Include these files:
- `pyproject.toml` (project metadata)
- `uv.lock` (exact dependencies)
- `.python-version` (Python version)
- All source code

Others can clone and run:
```bash
git clone repo-url
cd project
uv sync
uv run python ...
```

---

### Q: What if someone uses pip on my uv project?

**A:** Don't mix tools. If your project has `pyproject.toml` and `uv.lock`, others should use uv.

You can document this in `README.md`:

```markdown
## Installation

This project uses uv. Install it first:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then:

```bash
git clone repo-url
cd project
uv sync
uv run python ...
```
```

---

### Q: Can I deploy my uv project to production?

**A:** Yes! uv works great for deployment.

Docker example:

```dockerfile
FROM python:3.12

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /app

COPY . .

# Install dependencies
RUN uv sync --no-dev

CMD ["uv", "run", "python", "src/app/main.py"]
```

Or export to `requirements.txt`:

```bash
uv export > requirements.txt
# Use with traditional deployment
```

---

### Q: How do I handle secrets like API keys?

**A:** Never commit secrets. Use `.env` files:

`.env` file (ignored by Git):
```
OPENAI_API_KEY=sk-...
DATABASE_URL=postgres://...
```

Code:
```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
```

Add to `.gitignore`:
```
.env
.env.local
```

---

### Q: What's the difference between `uv lock` and `uv sync`?

**A:**

- **`uv lock`** — Updates `uv.lock` based on current code
  - Use when you change `pyproject.toml`
  - Creates new lock file

- **`uv sync`** — Installs from existing `uv.lock`
  - Use when getting new `uv.lock` from Git
  - Reproduces exact environment

---

### Q: Can uv work with Conda?

**A:** They're separate tools. Use one or the other.

- **Conda**: Manages packages + environments + Python (Python community tool)
- **uv**: Manages packages + environments + Python (newer, faster alternative)

They're similar in purpose, so don't mix them in one project.

---

### Q: Is uv production-ready?

**A:** Yes! uv is mature and actively maintained by Astral (creators of Ruff).

It's been production-tested by major companies and is safe to use for:
- Development
- Deployments
- CI/CD pipelines
- Production systems

---

### Q: Where's my cache stored?

**A:** Different by operating system:

**macOS:**
```
~/Library/Caches/uv
```

**Linux:**
```
~/.cache/uv
```

**Windows:**
```
%LOCALAPPDATA%\uv\cache
```

Check with:
```bash
uv cache dir
```

---

### Q: How do I report bugs?

**A:** Open an issue on GitHub:

https://github.com/astral-sh/uv/issues

Include:
- What you ran
- What error you got
- What you expected
- Your OS and Python version
- Output of `uv --version`

---

## Where to Get Help

### Official Documentation

https://docs.astral.sh/uv/

### GitHub Repository

https://github.com/astral-sh/uv

### Discord Community

https://discord.com/invite/astral-sh

### Stack Overflow

Tag: `uv-package-manager`

---

# Conclusion

Congratulations! You've learned about uv, the fastest Python package manager.

## Key Takeaways

1. **uv replaces many tools** — One command for everything
2. **It's much faster** — 10-100x speedup over traditional tools
3. **Projects are simple** — `uv init` and you're ready
4. **Dependencies are easy** — `uv add` to install, `uv remove` to remove
5. **Collaboration is automatic** — `uv.lock` ensures everyone uses same versions
6. **Python versions are flexible** — Install and manage multiple versions
7. **No manual venv management** — `uv run` handles it automatically

## Next Steps

1. **Install uv** if you haven't already:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Create your first project:**
   ```bash
   uv init my-first-project
   cd my-first-project
   ```

3. **Add a dependency:**
   ```bash
   uv add requests
   ```

4. **Run some code:**
   ```bash
   uv run python -c "import requests; print('It works!')"
   ```

5. **Learn more** at https://docs.astral.sh/uv/

## You're Ready!

You now know:
- What uv is and why it exists
- How to install and use it
- How to create and manage projects
- How to handle dependencies
- How to work with Python versions
- How to run code safely
- How to troubleshoot common issues

Start using uv today. Your Python development will be faster and easier!

---

**Happy coding! 🚀**

---

## Glossary of Terms

**Cache** — Storage of downloaded packages to avoid re-downloading

**Dependency** — A library your project needs to work

**Distribution** — A packaged version of a library ready to install

**Lock file** — A record of exact package versions (uv.lock)

**Module** — A single Python file (.py)

**Package** — A directory of Python code that can be installed

**Project** — A Python application with dependencies and configuration

**PyPI** — Python Package Index, where packages are published

**Repository** — Collection of Python packages (like PyPI)

**Script** — A single Python file for a small task

**Tool** — A Python package that provides a command-line program

**Virtual environment** — Isolated Python environment for a project

**Version pinning** — Locking to a specific version

---

**Document Version:** 1.0  
**Last Updated:** June 2026  
**For uv version:** 0.5.x and above

This handbook covers the complete Astral uv package manager from beginner to competent user. For advanced topics and integration guides, refer to the official documentation at https://docs.astral.sh/uv/