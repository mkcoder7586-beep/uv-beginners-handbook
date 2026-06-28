# Contributing to uv Beginners Handbook

First, thank you for your interest in improving this handbook! 🎉

This is a community-driven resource, and contributions of all kinds are welcome and valued.

---

## Table of Contents

- [Ways to Contribute](#ways-to-contribute)
- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Making Changes](#making-changes)
- [Submitting Changes](#submitting-changes)
- [Style Guide](#style-guide)
- [Translations](#translations)
- [FAQ for Contributors](#faq-for-contributors)

---

## Ways to Contribute

### 1. Report Errors or Typos
- Found a spelling mistake?
- Incorrect example code?
- Outdated information?

**[Open an issue](https://github.com/mkcoder7586-beep/uv-beginners-handbook/issues/new?template=bug_report.md)** describing what's wrong.

### 2. Ask Questions or Suggest Improvements
- Something unclear?
- Topic missing?
- Better way to explain something?

**[Open an issue](https://github.com/mkcoder7586-beep/uv-beginners-handbook/issues/new?template=improvement.md)** with your suggestion.

### 3. Fix Errors
- Have a fix for a typo?
- Improved example?
- Clarification to existing text?

**[Submit a pull request](#submitting-changes)** with your changes.

### 4. Add Missing Content
- New section idea?
- Example project?
- Better explanation?

**[Discuss first](https://github.com/mkcoder7586-beep/uv-beginners-handbook/issues)** then **[submit PR](#submitting-changes)**.

### 5. Create Translations
- Speak Spanish, French, Japanese, Chinese?
- Want to translate the handbook?

See [Translations](#translations) below.

### 6. Create Example Projects
- Built something with uv?
- Great teaching project?
- Want to add to `/examples` folder?

**[Discuss first](https://github.com/mkcoder7586-beep/uv-beginners-handbook/issues)**, then **[submit PR](#submitting-changes)**.

### 7. Share Feedback
- Using the handbook to teach?
- Built a project from it?
- Have feedback?

**Share your experience** by opening an [issue](https://github.com/mkcoder7586-beep/uv-beginners-handbook/issues) or [discussion](https://github.com/mkcoder7586-beep/uv-beginners-handbook/discussions)!

---

## Code of Conduct

By participating, you agree to our [Code of Conduct](CODE_OF_CONDUCT.md).

**TL;DR:** Be respectful, inclusive, and kind to everyone.

---

## Getting Started

### Prerequisites
- A GitHub account
- Git installed locally
- Basic familiarity with GitHub (fork, clone, PR)

### 1. Fork the Repository

Click the **"Fork"** button in the top-right corner of this repository.

```bash
# Clone your fork
git clone https://github.com/mkcoder7586-beep/uv-beginners-handbook.git
cd uv-beginners-handbook

# Add upstream remote
git remote add upstream https://github.com/mkcoder7586-beep/uv-beginners-handbook
```

### 2. Create a Branch

Always create a new branch for your changes:

```bash
# Update main branch
git fetch upstream
git checkout main
git merge upstream/main

# Create feature branch
git checkout -b fix/typo-in-part-3
# or
git checkout -b feature/add-advanced-section
```

**Branch naming:**
- `fix/` — Bug fixes or corrections
- `feature/` — New content or sections
- `docs/` — Documentation improvements
- `example/` — New example projects

### 3. Make Your Changes

Edit the handbook or other files as needed.

See [Style Guide](#style-guide) below for formatting conventions.

### 4. Test Your Changes

If you're editing the handbook:
- Read through your changes
- Check for typos and grammar
- Verify code examples work
- Ensure links are correct

```bash
# Check syntax (if you have a markdown linter)
npm install -g markdownlint-cli
markdownlint handbook/uv_beginners_handbook.md
```

### 5. Commit Your Changes

Write clear, descriptive commit messages:

```bash
git add .
git commit -m "Fix: correct Python version example in Part 5"
# or
git commit -m "Docs: improve virtual environment explanation"
# or
git commit -m "Feature: add Docker deployment example"
```

**Commit message format:**
```
<TYPE>: <DESCRIPTION>

<OPTIONAL LONGER EXPLANATION>

Fixes #123
```

**Types:**
- `Fix:` — Correct an error
- `Docs:` — Improve documentation
- `Feature:` — Add new content
- `Refactor:` — Reorganize/clarify existing content
- `Chore:` — Maintenance tasks

### 6. Push Your Changes

```bash
git push origin fix/typo-in-part-3
```

### 7. Open a Pull Request

Go to **your fork** and click **"Pull Request"**.

Fill in the PR template with:
- **What** you changed
- **Why** you changed it
- **How** it improves the handbook
- Link to any related issues

---

## Making Changes

### Editing the Handbook

The main handbook file is at: `handbook/uv_beginners_handbook.md`

**Before making major changes:**

1. **Check if similar content exists**
2. **Open an issue first** to discuss
3. **Wait for feedback** before starting

**For small fixes:**
- Typos and grammar: Go ahead, no issue needed
- Minor clarifications: Go ahead
- Reorganizing sections: Open an issue first
- Adding new sections: Open an issue first

### Guidelines for Content Changes

**✅ Do:**
- Keep language beginner-friendly
- Explain jargon the first time it appears
- Use analogies and real-world examples
- Include working code examples
- Test code examples before submitting
- Be accurate to current uv behavior
- Link to relevant sections
- Use consistent formatting

**❌ Don't:**
- Assume prior knowledge
- Use overly technical language
- Include unsourced claims
- Link to broken URLs
- Contradict official uv documentation
- Promote unrelated tools
- Make politically charged comments
- Include personal opinions as facts

### Code Examples

All code examples must:

1. **Be syntactically correct** — Must run without errors
2. **Be tested** — Actually run it before submitting
3. **Be relevant** — Clearly teaches the concept
4. **Be minimal** — Shortest code that demonstrates the idea
5. **Include output** — Show what happens when you run it

Example:

```bash
# ✅ Good: Clear, tested, shows output

$ uv add requests
Resolved 4 packages in 50ms
Installed 4 packages in 100ms
 + certifi==2024.7.4
 + charset-normalizer==3.3.2
 + idna==2.5
 + requests==2.31.0

$ uv tree
myproject
├── requests==2.31.0
│   ├── certifi==2024.7.4
│   ├── charset-normalizer==3.3.2
│   └── urllib3==2.0.0
```

---

## Submitting Changes

### PR Checklist

Before submitting a PR, verify:

- [ ] **Grammar & Spelling:** Proofread carefully
- [ ] **Links:** All internal and external links work
- [ ] **Code Examples:** Actually run and work correctly
- [ ] **Consistency:** Matches existing style and tone
- [ ] **Accuracy:** Correct for current uv version (0.5.x+)
- [ ] **Clarity:** Written for beginners
- [ ] **Formatting:** Follows markdown conventions
- [ ] **Length:** Not too long (can break into multiple PRs)

### PR Description Template

When you open a PR, include:

```markdown
## Description
Brief explanation of what you changed and why.

## Type of Change
- [ ] Fix (typo, error, clarification)
- [ ] Feature (new content, example)
- [ ] Refactor (reorganize, improve clarity)

## Related Issues
Fixes #123 (if applicable)

## Testing
How did you verify this change?
- [ ] Tested code examples (if applicable)
- [ ] Proofread carefully
- [ ] Checked links

## Checklist
- [ ] My changes follow the style guide
- [ ] I've proofread carefully
- [ ] All links work
- [ ] Code examples are tested and correct
```

### Review Process

1. **Automated checks** — Links, formatting, etc.
2. **Maintainer review** — Content accuracy and style
3. **Community feedback** — Other contributors may comment
4. **Revisions** — We may request changes
5. **Approval & Merge** — PR is merged

**Expected timeline:** 3-7 days for review.

---

## Style Guide

### Tone & Voice

The handbook is:
- **Friendly** — Like talking to a helpful mentor
- **Clear** — Simple words, short sentences
- **Encouraging** — No "should know" or gatekeeping
- **Practical** — Show, don't just tell
- **Accurate** — Fact-based, not opinions

### Markdown Formatting

**Headings:**
```markdown
# Part X: Title        # Main sections only
## Section Name        # Subsections
### Subsection         # Details
```

**Emphasis:**
```markdown
**bold** for emphasis
*italic* for alternative usage
`code` for inline code
```

**Code Blocks:**
````markdown
```bash
# Bash/terminal code
$ command
output
```

```python
# Python code
print("example")
```

```toml
# Configuration files
[section]
key = "value"
```
````

**Lists:**
```markdown
# Use consistent spacing

1. First item
2. Second item
3. Third item

- Bullet point
- Another point
  - Nested point
- Back to main level
```

**Links:**
```markdown
# Link to handbook sections
[Section Name](handbook/uv_beginners_handbook.md#section-anchor)

# Link to external sites
[Python.org](https://python.org)

# Avoid: [click here](url)
# Do: [Read about virtual environments](handbook/...)
```

**Blockquotes:**
```markdown
> Important note or warning
> Can span multiple lines

> **Important:** This is especially critical
```

**Tables:**
```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Data     | Data     | Data     |
```

### Grammar & Language

- **American English** — We use "color" not "colour"
- **Active voice** — "You can add packages" not "Packages can be added"
- **Present tense** — "uv installs" not "uv will install"
- **Contractions** — "don't", "it's" are fine in friendly tone
- **Avoid jargon** — Explain or avoid technical terms

### Capitalization

```markdown
# Correct
- Python (language name)
- uv (product name, lowercase)
- PyPI (as written officially)
- GitHub (not Github)
- macOS (not MacOS)
- PowerShell (not powershell)
```

### Numbers & Units

```markdown
# Correct
- "3 minutes" not "3 mins"
- "2-3 hours" not "2-3 hrs"
- "10-100x faster" not "10x-100x faster"
- "1 GB" not "1gb"
```

---

## Translations

We welcome translations! Here's how:

### 1. Choose a Language

Check [translations/README.md](translations/README.md) to see:
- Which languages are planned
- Which languages are in progress
- Which languages are complete

### 2. Open an Issue

Let us know you want to translate:

```markdown
I want to translate the handbook to [LANGUAGE]

This is my GitHub account: @username
I have translation experience: [yes/no]
Estimated completion: [timeline]
```

### 3. Set Up Translation Files

```
translations/
└── [language-code]/
    ├── uv_beginners_handbook.md    (translated handbook)
    ├── README.md                   (in your language)
    └── translation-notes.md        (translation decisions)
```

**Language codes:**
- `es/` — Spanish (Español)
- `fr/` — French (Français)
- `ja/` — Japanese (日本語)
- `zh/` — Chinese Simplified (简体中文)
- `de/` — German (Deutsch)
- `pt-br/` — Portuguese Brazil (Português)

### 4. Keep Translations Current

When the main handbook updates:
- We'll notify translators
- Update your translation
- Submit PR with updates

### 5. Translation Guidelines

**For translators:**

- Keep formatting identical
- Don't add or remove sections
- Preserve code examples exactly
- Translate comments and output too
- Keep tone and voice appropriate for your language
- Use culturally appropriate examples where helpful
- Test any commands still work in translated form

**For code examples:**
```markdown
# ✅ Good: Translate but preserve structure

# Command (unchanged)
$ uv add requests

# Spanish output explanation (translated)
Resuelto en 4 paquetes en 50ms

---

# ❌ Bad: Don't change code structure
$ uv agregar requests    # Wrong! Don't translate command names
```

---

## FAQ for Contributors

### Q: I'm not a great writer. Can I still contribute?

**A:** Absolutely! Small fixes are valuable:
- Point out typos in an issue
- Suggest a clarification
- Report confusion you experienced
- Others can help refine wording

### Q: How long does review take?

**A:** Usually 3-7 days. We try to respond quickly.

For urgent issues, mention maintainers: `@maintainer`

### Q: Can I change the handbook structure?

**A:** For large reorganizations, **open an issue first**. We want to discuss:
- Why the change is needed
- How it affects readers
- Whether it breaks TOC links

Small section reorderings usually OK via PR.

### Q: What if my PR gets rejected?

**A:** No worries! We'll explain why and what would help.

- Use feedback to improve
- Resubmit if changes address concerns
- Ask questions if unclear
- Stay positive — we appreciate the effort!

### Q: Can I work on multiple PRs?

**A:** Yes! Work on as many as you want.

Just keep branches separate:
```bash
git checkout -b feature/new-section
# ... work on feature
git checkout -b fix/typo
# ... work on fix
```

### Q: Who can merge PRs?

**A:** Only maintainers can merge.

But you can:
- Suggest changes in comments
- Approve good work with 👍
- Point out potential issues

### Q: Is there a maintainer guide?

**A:** Not yet, but if you're consistently helping, ask about joining the team!

### Q: Can I get credit for my contributions?

**A:** Yes! We maintain a contributors list:

```markdown
## Contributors

Thanks to these amazing people:
- @username — Fixed typos in Part 3
- @another-user — Added Docker example
```

We credit contributors in:
- Pull request comments
- Changelog
- Future contributors list

---

## Recognition

We recognize and thank:

- **All contributors** for making this better
- **uv users** for feedback and examples
- **Astral** for creating uv
- **The Python community** for inspiration

---

## Need Help?

### Resources

- **Questions about contributing?** → [Open an issue](https://github.com/mkcoder7586-beep/uv-beginners-handbook/issues)
- **Want to discuss something?** → [Start a discussion](https://github.com/mkcoder7586-beep/uv-beginners-handbook/discussions)
- **Need help with GitHub?** → See [GitHub docs](https://docs.github.com)
- **Learning uv?** → Read the [handbook](handbook/uv_beginners_handbook.md)!

### Helpful Links

- [GitHub Forking Guide](https://docs.github.com/en/get-started/quickstart/fork-a-repo)
- [GitHub Pull Requests](https://docs.github.com/en/pull-requests)
- [Markdown Guide](https://www.markdownguide.org/)
- [Writing Good Commit Messages](https://chris.beams.io/posts/git-commit/)

---

## Thank You! 🙏

Every contribution — big or small — helps make this handbook better for everyone.

Whether it's a typo fix, a new example, or a complete translation, we genuinely appreciate your effort.

**Welcome to the community!**

---

**Questions?** [Ask in an issue](https://github.com/mkcoder7586-beep/uv-beginners-handbook)

**Ready to start?** [Grab an issue](https://github.com/mkcoder7586-beep/uv-beginners-handbook/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22) and dive in!