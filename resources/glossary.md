# uv Glossary: Quick Reference

## A

**Activation** (Virtual Environment)
The process of switching your shell to use a specific virtual environment. With uv, you don't need manual activation—`uv run` handles it automatically.
- *See also:* Virtual Environment, `uv run`
- *Handbook:* Part 8 - The pip Interface

**Astral**
The company that created uv (also created Ruff, a code formatter). Based in New York, actively maintaining uv.
- *Handbook:* Part 1 - Why Does uv Exist?

## B

**Build**
The process of creating distributable files from your project source code. Results in `.whl` and `.tar.gz` files.
- *Command:* `uv build`
- *See also:* Publish, Wheel
- *Handbook:* Part 9 - Publishing Packages

## C

**Cache**
Stored copies of downloaded packages to avoid re-downloading. Automatically managed by uv.
- *Location:* `~/.cache/uv` (Linux), `~/Library/Caches/uv` (macOS), `%LOCALAPPDATA%\uv\cache` (Windows)
- *Commands:* `uv cache clean`, `uv cache prune`
- *Handbook:* Part 9 - Caching

**CPython**
The standard Python implementation (written in C). Most common Python you use.
- *Alternative implementations:* PyPy, Pyston
- *See also:* Python Version

## D

**Dependency**
A library or package that your project needs to function. Can be direct (you import it) or transitive (imported by your dependencies).
- *Direct:* `import requests` in your code
- *Transitive:* requests depends on urllib3
- *Commands:* `uv add`, `uv remove`
- *Handbook:* Part 3 - Dependencies

**Development Dependency**
A package needed only while developing (testing, formatting, linting) but not needed when running the application in production.
- *Examples:* pytest, black, ruff
- *Command:* `uv add --dev PACKAGE`
- *Handbook:* Part 4 - Adding Dependencies

**Distribution**
A packaged version of a library ready to be installed. How packages are delivered to you.
- *See also:* Package, Wheel, Tarball
- *Handbook:* Part 3 - Packages and Libraries

## E

**Environment Variable**
A value set outside your code that Python can access. Used for configuration, secrets, and dynamic values.
- *Example:* `OPENAI_API_KEY`, `DATABASE_URL`
- *Python code:* `os.getenv("VARIABLE_NAME")`
- *Handbook:* Part 14 - Real-World Examples (Chatbot project)

**Export**
Converting your dependencies to a different format (like `requirements.txt`) for compatibility with other tools.
- *Command:* `uv export > requirements.txt`
- *Handbook:* Part 4 - Exporting Dependencies

## F

**Freeze**
Saving the exact versions of all currently installed packages. Creates a snapshot.
- *Command:* `uv pip freeze > requirements.txt`
- *See also:* Lock, Lock File
- *Handbook:* Part 8 - The pip Interface

## G

**Global Installation**
Installing a package/tool system-wide, available everywhere. Used for tools, not project dependencies.
- *See also:* Local Installation, Tool
- *Commands:* `uv tool install`
- *Handbook:* Part 7 - Installing Tools

## I

**Index** (Package Index)
A server that hosts Python packages. PyPI is the official one.
- *Primary:* PyPI (Python Package Index)
- *Alternative:* Private/internal indexes
- *Handbook:* Part 9 - Configuration

**Isolation** (Environment Isolation)
Keeping dependencies separate so packages from one project don't interfere with another.
- *How:* Virtual environments
- *See also:* Virtual Environment
- *Handbook:* Part 3 - Virtual Environments

## L

**Library**
A collection of reusable Python code. Often used interchangeably with "package."
- *Examples:* pandas, numpy, requests, flask
- *See also:* Package, Module
- *Handbook:* Part 3 - Packages and Libraries

**Local Installation**
Installing a package in a specific project's virtual environment only.
- *See also:* Global Installation
- *Commands:* `uv add`
- *Handbook:* Part 4 - Adding Dependencies

**Lock** (Verb)
The action of recording exact dependency versions.
- *See also:* Lock File, Freeze
- *Command:* `uv lock`
- *Handbook:* Part 4 - Syncing Your Project

**Lock File**
A file (`uv.lock`) that records the exact version of every installed package. Ensures reproducibility.
- *Filename:* `uv.lock`
- *Purpose:* Same environment for all developers
- *Auto-generated:* Yes, don't edit manually
- *Handbook:* Part 3 - Lock Files

## M

**Module**
A single Python file (`.py`). The building block of Python code.
- *Example:* `main.py`, `utils.py`
- *See also:* Package, Library
- *Handbook:* Part 3 - Packages and Libraries

**Monorepo**
A single repository containing multiple related projects.
- *See also:* Workspace
- *Handbook:* Part 9 - Workspaces

## P

**Package**
A directory of Python code that can be installed. Also used generally to mean any installable library.
- *Examples:* requests, pandas, flask
- *Structure:* `package_name/__init__.py` + other modules
- *See also:* Library, Distribution, Module
- *Handbook:* Part 3 - Packages and Libraries

**Package Manager**
A tool that finds, downloads, installs, and manages software packages.
- *uv replaces:* pip, poetry, pipx, pyenv, virtualenv, and more
- *Handbook:* Part 1 - What is a Package Manager?

**Path** (Python Path)
The list of locations Python searches for modules when you import them.
- *Modified by:* Virtual environments
- *See also:* Virtual Environment

**pip**
The traditional Python package manager. Slower than uv.
- *What it does:* Install packages into virtual environments
- *uv alternative:* `uv add` (project-level) or `uv pip install` (pip interface)
- *Handbook:* Part 1 - Why Does uv Exist?

**Pip Interface**
uv's compatibility layer that mimics `pip` commands for migration from traditional pip workflows.
- *Commands:* `uv pip install`, `uv pip list`, `uv pip freeze`
- *When to use:* When migrating from pip or using traditional workflows
- *Handbook:* Part 8 - The pip Interface

**PyPI** (Python Package Index)
The official repository where Python packages are published and can be downloaded.
- *Website:* https://pypi.org
- *Alternative:* Private/internal package indexes
- *Handbook:* Part 9 - Publishing Packages

**PyPy**
An alternative Python implementation that's faster for some workloads.
- *See also:* CPython
- *Handbook:* Part 5 - Installing Python

**pyproject.toml**
The main configuration file for your project. Defines metadata, dependencies, and build settings.
- *Filename:* `pyproject.toml`
- *Format:* TOML (similar to INI)
- *Auto-generated:* Yes, created by `uv init`
- *Handbook:* Part 4 - Project Structure

**Python Version**
Which version of Python your project uses (3.10, 3.11, 3.12, etc.).
- *Specified in:* `.python-version` file
- *Managed by:* `uv python` commands
- *Handbook:* Part 5 - Working With Python Versions

## R

**Reproducibility**
Ensuring that code runs the same way everywhere, with same versions and behavior.
- *How uv ensures it:* Lock files + explicit version pinning
- *See also:* Lock File
- *Handbook:* Part 3 - Lock Files

**Requirements File**
Traditional way of specifying dependencies. Usually named `requirements.txt`.
- *Format:* One package per line with optional version
- *Example:* `requests==2.31.0`
- *See also:* Lock File, pyproject.toml
- *Handbook:* Part 8 - The pip Interface

**Ruff**
A fast code linter and formatter. Made by the same company as uv (Astral).
- *Purpose:* Check code quality and format
- *See also:* Black
- *Handbook:* Part 14 - Real-World Examples

## S

**Script**
A single Python file meant to be run directly, usually for a small task or one-off automation.
- *See also:* Project
- *Run with:* `uv run python script.py`
- *Dependencies:* Declared with special comments
- *Handbook:* Part 6 - Running Scripts

**Sync**
Installing all dependencies exactly as specified in the lock file.
- *Command:* `uv sync`
- *When to use:* After pulling from Git, when `uv.lock` changes
- *Difference from `uv add`:* Doesn't modify dependencies, just installs
- *Handbook:* Part 4 - Syncing Your Project

## T

**Tarball**
A compressed archive file (`.tar.gz`) containing source code. One distribution format.
- *See also:* Wheel
- *Handbook:* Part 9 - Publishing Packages

**Tool**
A Python package that provides a command-line program or utility.
- *Examples:* black, pytest, jupyter, ruff
- *vs. Library:* Libraries you import in code; tools you run from terminal
- *Commands:* `uv tool install`, `uvx`
- *Handbook:* Part 7 - Tools & Utilities

**Transitive Dependency**
A package that you don't directly import, but one of your dependencies needs.
- *Example:* You use requests, which depends on urllib3
- *Visible in:* `uv tree`
- *See also:* Dependency
- *Handbook:* Part 3 - Dependencies

**Twine**
Traditional tool for publishing packages to PyPI. uv replaces this.
- *See also:* Publish
- *Handbook:* Part 9 - Publishing Packages

## U

**uv**
The fastest Python package manager, created by Astral.
- *Replaces:* pip, poetry, pipx, pyenv, virtualenv, and more
- *Speed:* 10-100x faster than pip
- *Language:* Written in Rust
- *Website:* https://astral.sh/uv
- *Handbook:* Part 1 - Why Does uv Exist?

**uvx**
Shorthand for `uv tool run`. Runs a tool temporarily without installing it.
- *Command:* `uvx tool-name`
- *See also:* `uv tool run`, `uv tool install`
- *Handbook:* Part 7 - Running Tools

## V

**Version Pinning**
Locking a dependency to a specific version to ensure consistency.
- *Examples:* 
  - Exact: `requests==2.31.0`
  - Range: `requests>=2.28.0,<3.0.0`
- *Handbook:* Part 4 - Adding Dependencies

**Virtual Environment**
An isolated Python installation on your computer. Each project has its own to avoid conflicts.
- *Created by:* `uv init` (automatic) or `uv venv`
- *Location:* `.venv/` folder in project
- *Handbook:* Part 3 - Virtual Environments

## W

**Wheel** (`.whl`)
A binary distribution format for Python packages. Faster to install than source distributions.
- *Filename pattern:* `package-version-python-abi-platform.whl`
- *See also:* Tarball, Distribution
- *Handbook:* Part 9 - Publishing Packages

**Workspace**
Multiple related projects managed together in one repository (monorepo).
- *Use case:* Large projects with multiple packages
- *Shared:* Lock file, Python version
- *See also:* Monorepo
- *Handbook:* Part 9 - Workspaces

## X

**(No common terms starting with X in uv)**

## Y

**(No common terms starting with Y in uv)**

## Z

**(No common terms starting with Z in uv)**

---

## Cross-Reference: Commands by Purpose

### Creating & Setting Up
- `uv init` — Create a new project
- `uv venv` — Create a virtual environment (pip interface style)
- `uv python install` — Download and install Python

### Managing Dependencies
- `uv add` — Add a package
- `uv remove` — Remove a package
- `uv sync` — Install from lock file
- `uv lock` — Update lock file

### Running Code
- `uv run` — Run Python code in project environment
- `uvx` — Run a tool temporarily

### Working with Tools
- `uv tool install` — Install a tool globally
- `uv tool list` — List installed tools
- `uv tool update` — Update a tool
- `uv tool uninstall` — Remove a tool

### Python Version Management
- `uv python install` — Download Python
- `uv python list` — List installed Pythons
- `uv python pin` — Set Python for project
- `uv python find` — Find a Python version

### Maintenance
- `uv cache clean` — Clear cache
- `uv cache prune` — Remove unused cache
- `uv tree` — View dependencies
- `uv export` — Export to requirements.txt

---

## Cross-Reference: Handbook Sections

**New to Python?** Start with Part 1: The Foundations

**Ready to code?** Jump to Part 2: Getting Started

**Need a specific task?** Check Part 10: Decision Trees & Workflows

**Looking for commands?** See Part 11: Command Reference

**Quick answers?** Use Part 12: Cheat Sheets

**Got an error?** Check Appendix: Troubleshooting & FAQ

---

**Last Updated:** June 2026  
**For uv version:** 0.5.x and above