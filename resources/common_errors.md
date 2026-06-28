# uv Common Errors: Diagnosis & Solutions

Quick reference for errors you might encounter and how to fix them.

---

## Runtime Errors

### ModuleNotFoundError: No module named 'X'

**What it looks like:**
```
ModuleNotFoundError: No module named 'requests'
```

**Why it happens:**
- Package isn't installed
- You're not running with `uv run`
- Virtual environment is broken

**How to fix:**

1. **Install the package:**
   ```bash
   uv add requests
   ```

2. **Run with uv:**
   ```bash
   uv run python my-script.py  # ✅ Correct
   python my-script.py          # ❌ Wrong
   ```

3. **Verify package is installed:**
   ```bash
   uv pip list | grep requests
   # Should show: requests    2.31.0
   ```

4. **If still failing, recreate environment:**
   ```bash
   rm -rf .venv
   uv sync
   uv run python my-script.py
   ```

**Prevention:**
Always use `uv run` to run Python code in your project.

---

### ImportError: cannot import name 'X'

**What it looks like:**
```
ImportError: cannot import name 'function_name' from 'module_name'
```

**Why it happens:**
- Function/class doesn't exist in that module (typo or wrong version)
- You're using an old version of the package
- Module changed between versions

**How to fix:**

1. **Check the correct import:**
   ```bash
   # Look up documentation or PyPI
   # Example: Check if pandas exports 'DataFrame'
   uv run python -c "from pandas import DataFrame; print('OK')"
   ```

2. **Update the package to latest:**
   ```bash
   uv add --upgrade module-name
   ```

3. **Check what's available:**
   ```bash
   uv run python -c "import module_name; print(dir(module_name))"
   ```

4. **Install specific version if needed:**
   ```bash
   uv add "module-name==2.0.0"
   ```

---

### AttributeError: module 'X' has no attribute 'Y'

**What it looks like:**
```
AttributeError: module 'requests' has no attribute 'get'
```

**Why it happens:**
- Wrong module or typo
- Version mismatch
- Module renamed or reorganized

**How to fix:**

1. **Check the documentation** for correct usage

2. **Verify installed version:**
   ```bash
   uv run python -c "import requests; print(requests.__version__)"
   ```

3. **Update the package:**
   ```bash
   uv add --upgrade requests
   ```

4. **Check available attributes:**
   ```bash
   uv run python -c "import requests; print([x for x in dir(requests) if not x.startswith('_')])"
   ```

---

### TypeError: 'X' object is not callable

**What it looks like:**
```
TypeError: 'DataFrame' object is not callable
```

**Why it happens:**
- You're treating a variable as a function
- Version changed how something works
- Name collision with your own code

**How to fix:**

1. **Check your code for mistakes:**
   ```python
   # ❌ Wrong - DataFrame is a class, not a function call
   import pandas
   df = pandas.DataFrame()
   result = df()  # df is an object, not callable
   
   # ✅ Correct
   result = df.head()  # Call a method on the object
   ```

2. **Check package documentation** for correct API

3. **Update package if it's old:**
   ```bash
   uv add --upgrade package-name
   ```

---

## Installation & Environment Errors

### "command not found: uv"

**What it looks like:**
```
bash: uv: command not found
```

**Why it happens:**
- uv isn't installed
- Not in your PATH

**How to fix:**

1. **Reinstall uv:**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Verify installation:**
   ```bash
   uv --version
   # Should show: uv 0.5.4
   ```

3. **Add to PATH manually if needed:**
   ```bash
   export PATH="$HOME/.local/bin:$PATH"
   # Add to ~/.bashrc or ~/.zshrc to make permanent
   ```

4. **On Windows, use Python wrapper:**
   ```powershell
   python -m uv --version
   ```

---

### Virtual environment issues

**Error messages:**
```
Error: Virtual environment creation failed
Error: Failed to create virtual environment
```

**Why it happens:**
- `.venv` is corrupted
- Disk space issue
- Permission problem
- Python version conflict

**How to fix:**

1. **Delete and recreate environment:**
   ```bash
   rm -rf .venv           # or rmdir /s .venv on Windows
   uv sync
   ```

2. **Check disk space:**
   ```bash
   df -h    # Linux/macOS
   dir /-s  # Windows
   ```

3. **Check permissions:**
   ```bash
   # Make sure project folder is writable
   ls -ld .   # Linux/macOS
   ```

4. **Try specific Python version:**
   ```bash
   uv python install 3.12
   uv python pin 3.12
   uv sync
   ```

5. **Last resort - recreate project structure:**
   ```bash
   rm -rf .venv uv.lock
   uv sync
   ```

---

### Permission denied errors

**What it looks like (Windows):**
```
PermissionError: [WinError 5] Access is denied
```

**What it looks like (macOS/Linux):**
```
Permission denied: '.venv/bin/python'
```

**Why it happens:**
- Running without administrator privileges (Windows)
- Folder ownership issues (macOS/Linux)
- Virtual environment files corrupted

**How to fix:**

1. **On Windows - Run PowerShell as Administrator:**
   - Right-click PowerShell
   - Select "Run as administrator"
   - Run your command again

2. **On macOS/Linux - Check ownership:**
   ```bash
   ls -la .venv
   # If not owned by you, fix permissions:
   sudo chown -R $USER .venv
   ```

3. **Recreate the environment:**
   ```bash
   rm -rf .venv
   uv sync
   ```

---

## Package & Dependency Errors

### PackageNotFoundError: No package named 'X'

**What it looks like:**
```
error: Package `reqeusts` not found
```

**Why it happens:**
- Typo in package name
- Package doesn't exist on PyPI
- Old/renamed package

**How to fix:**

1. **Check the spelling:**
   ```bash
   # ❌ Wrong
   uv add reqeusts

   # ✅ Correct
   uv add requests
   ```

2. **Search PyPI for correct name:**
   - Visit https://pypi.org/search/
   - Search for the package name
   - Copy exact name from search results

3. **Check if it's a different package:**
   ```bash
   # Is it part of another package?
   uv add numpy-related-name
   ```

4. **Check if it's been renamed:**
   ```bash
   # Old: Pillow vs PIL
   # Correct: uv add Pillow
   ```

---

### No matching version found for 'X'

**What it looks like:**
```
No matching version found for requests==99.0.0
```

**Why it happens:**
- Version number doesn't exist
- Typo in version number
- Version too old or too new

**How to fix:**

1. **Use a real version:**
   ```bash
   # ❌ Wrong
   uv add requests==99.0.0

   # ✅ Correct
   uv add requests==2.31.0
   ```

2. **Check available versions:**
   - Visit https://pypi.org/project/requests/
   - Scroll to "Release history"
   - Pick a version that exists

3. **Use version constraint instead:**
   ```bash
   # Instead of exact version
   uv add "requests>=2.28.0"
   ```

4. **Update to latest:**
   ```bash
   uv add requests  # Gets latest version
   ```

---

### Dependency conflict / incompatible versions

**What it looks like:**
```
error: Failed to resolve dependencies
```

**Why it happens:**
- Two packages need different versions of same library
- Package requirements are incompatible
- Version constraints are too strict

**How to fix:**

1. **See what's conflicting:**
   ```bash
   uv tree
   # Look for duplicates with different versions
   ```

2. **Identify the problem package:**
   ```bash
   # Example: pandas 2.0 needs numpy>=1.21
   #          old-library needs numpy<1.20
   # Can't have both
   ```

3. **Update or remove the old package:**
   ```bash
   # Option 1: Update to newer version
   uv add "old-library>=3.0"
   
   # Option 2: Remove if not needed
   uv remove old-library
   
   # Option 3: Use compatible versions
   uv add "pandas==1.5.0" "old-library==1.0.0"
   ```

4. **Check package documentation** for version compatibility

---

### Uninstalled requests when I meant other package

**What it looks like:**
```bash
$ uv remove requests
$ uv run python my-script.py
# ModuleNotFoundError: No module named 'requests'
```

**How to fix:**

1. **Add it back:**
   ```bash
   uv add requests
   ```

2. **Verify it's installed:**
   ```bash
   uv pip list | grep requests
   ```

---

## Python Version Errors

### "Python version not found"

**What it looks like:**
```
Error: Failed to find Python 3.14
```

**Why it happens:**
- Trying to use Python version that doesn't exist
- Typo in version number

**How to fix:**

1. **Check available versions:**
   ```bash
   uv python list
   ```

2. **Install the version you need:**
   ```bash
   uv python install 3.12
   uv python list  # Verify it's there
   ```

3. **Use a version that exists:**
   ```bash
   # Current stable Python versions: 3.10, 3.11, 3.12, 3.13
   uv python install 3.13
   ```

---

### Wrong Python version being used

**What it looks like:**
```bash
$ uv run python --version
Python 3.10.5
# But you expected 3.12
```

**How to fix:**

1. **Check what's pinned:**
   ```bash
   cat .python-version
   ```

2. **Update the pin:**
   ```bash
   uv python pin 3.12
   uv run python --version  # Now shows 3.12
   ```

3. **Verify it's installed:**
   ```bash
   uv python list | grep 3.12
   ```

---

### "The currently active Python version doesn't satisfy X"

**What it looks like:**
```
Error: The currently active Python version (3.9) 
doesn't satisfy the version constraint (>=3.10)
```

**Why it happens:**
- Project requires Python 3.10+
- Your system Python is too old
- Wrong Python version pinned

**How to fix:**

1. **Install required Python:**
   ```bash
   # Project needs 3.10+
   uv python install 3.12
   ```

2. **Pin it to the project:**
   ```bash
   uv python pin 3.12
   ```

3. **Verify:**
   ```bash
   cat .python-version  # Shows 3.12
   uv run python --version  # Shows Python 3.12
   ```

---

## Lock File Errors

### "Failed to lock requirements"

**What it looks like:**
```
error: Failed to lock requirements
```

**Why it happens:**
- Conflicting dependencies
- Version constraints are impossible
- Network issue while resolving

**How to fix:**

1. **Try again (might be network issue):**
   ```bash
   uv lock
   ```

2. **See what's wrong:**
   ```bash
   uv tree  # Look for conflicts
   ```

3. **Relax version constraints:**
   ```bash
   # ❌ Too strict
   uv add "requests==2.31.0" "pandas==2.0.0"
   
   # ✅ More flexible
   uv add "requests>=2.25.0" "pandas>=1.5.0"
   ```

4. **Remove conflicting package:**
   ```bash
   # If old-lib conflicts with new-lib
   uv remove old-lib
   ```

---

### uv.lock is out of date

**What it looks like:**
```bash
$ git pull
# uv.lock was updated
$ uv run python ...
# Code uses old version
```

**How to fix:**

1. **Sync to lock file:**
   ```bash
   uv sync
   ```

2. **Verify:**
   ```bash
   uv run python script.py
   ```

---

## Git & Collaboration Errors

### "uv.lock conflicts with colleague's version"

**What it looks like:**
```
$ git pull
CONFLICT (content): Merge conflict in uv.lock
```

**Why it happens:**
- Both of you changed dependencies
- Git can't automatically merge lock files

**How to fix:**

1. **Don't manually edit uv.lock** - Regenerate it:
   ```bash
   # Accept their changes
   git checkout --theirs uv.lock
   
   # Or accept yours
   git checkout --ours uv.lock
   ```

2. **Regenerate the lock file:**
   ```bash
   uv lock
   ```

3. **Commit the regenerated lock file:**
   ```bash
   git add uv.lock
   git commit -m "Resolve lock file conflict"
   ```

---

### Colleague gets different versions

**What it looks like:**
```
# You have pandas 2.0.0
# They have pandas 1.5.3
# Code behaves differently
```

**Why it happens:**
- They didn't use `uv sync`
- They modified `pyproject.toml` differently
- They used `uv add` instead of syncing

**How to fix:**

1. **Make sure they sync:**
   ```bash
   # They should run:
   uv sync
   
   # Not:
   uv add pandas  # This installs latest, not lock file version
   ```

2. **Verify they have correct versions:**
   ```bash
   uv pip list | grep pandas
   # Should match your uv.lock
   ```

3. **If still wrong, nuclear option:**
   ```bash
   rm -rf .venv
   uv sync
   ```

---

## Cache Issues

### "Strange errors" or "files not found"

**Why it might happen:**
- Cache is corrupted
- Partial download in cache
- Multiple uv processes accessing cache simultaneously

**How to fix:**

1. **Clean the cache:**
   ```bash
   uv cache clean
   ```

2. **Try again:**
   ```bash
   uv sync
   # or
   uv run python script.py
   ```

3. **If still broken, remove all cache:**
   ```bash
   uv cache clean --all
   uv sync
   ```

---

### Slow installation / downloading

**Why it happens:**
- First install (not cached yet)
- Network issues
- Large packages

**How to fix:**

1. **Be patient** - Some packages are large and take time

2. **Check network connection:**
   ```bash
   # Can you reach PyPI?
   curl https://pypi.org/simple/requests/
   ```

3. **Try again** - Might be temporary network issue:
   ```bash
   uv sync
   ```

4. **Check cache status:**
   ```bash
   uv cache dir
   # How much space is used?
   ```

---

## Tool Errors

### "Tool not found" when using `uvx`

**What it looks like:**
```
error: Package `tool-name` not found
```

**How to fix:**

1. **Check correct tool name:**
   ```bash
   # Check PyPI: https://pypi.org/search/?q=tool-name
   ```

2. **Make sure it's spelled right:**
   ```bash
   # ❌ Wrong
   uvx balck
   
   # ✅ Correct
   uvx black
   ```

---

### Tool installed but can't run it

**What it looks like:**
```
command not found: black
```

**Why it happens:**
- Tool isn't installed
- PATH not updated
- Shell restart needed

**How to fix:**

1. **Check if installed:**
   ```bash
   uv tool list | grep black
   ```

2. **Install it:**
   ```bash
   uv tool install black
   ```

3. **Restart your shell:**
   ```bash
   exec $SHELL
   # Or close and reopen terminal
   ```

4. **On Windows, restart PowerShell or CMD**

---

## Error Diagnosis Flowchart

```
I'm getting an error...

├─ "command not found: uv"
│  └─ See: command not found: uv
│
├─ "ModuleNotFoundError"
│  └─ See: ModuleNotFoundError
│
├─ "No package named"
│  └─ See: PackageNotFoundError
│
├─ "Version" error
│  └─ See: No matching version / Python version not found
│
├─ "Permission denied"
│  └─ See: Permission denied errors
│
├─ Virtual environment issue
│  └─ See: Virtual environment issues
│
├─ Dependency conflict
│  └─ See: Dependency conflict
│
└─ Not listed above
   └─ Check:
      1. Full error message
      2. Handbook Appendix: Troubleshooting
      3. Official docs: https://docs.astral.sh/uv/
      4. GitHub issues: https://github.com/astral-sh/uv/issues
```

---

## Getting Help

**Check in this order:**

1. **This document** - Most common errors covered
2. **FAQ** (faq.md) - Practical how-to questions
3. **Handbook Appendix** - Detailed troubleshooting
4. **Glossary** (glossary.md) - Definition of terms
5. **Official Docs** - https://docs.astral.sh/uv/
6. **GitHub Issues** - https://github.com/astral-sh/uv/issues
7. **Discord Community** - https://discord.com/invite/astral-sh

---

**Last Updated:** June 2026  
**For uv version:** 0.5.x and above