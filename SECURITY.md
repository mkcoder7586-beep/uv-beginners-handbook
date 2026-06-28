# Security Policy

## Reporting Security Issues

**Do not open public issues for security vulnerabilities.**

If you discover a security issue in this repository, please report it responsibly by:

### GitHub Security Advisory (Recommended)

Use [GitHub's private vulnerability reporting feature](https://github.com/mkcoder7586-beep/uv-beginners-handbook/security/advisories):

1. Go to **Security** → **Advisories**
2. Click **Report a vulnerability**
3. Fill in details privately


---

## Types of Security Issues We Track

### In This Repository

This is a documentation repository. Security concerns include:

#### 🔴 High Priority

- **Malicious code in examples**
  - Code examples that intentionally contain vulnerabilities
  - Links to malware or compromised sites
  - Examples that compromise user security

- **Information disclosure**
  - Exposed API keys or secrets
  - Sensitive user information
  - Private credentials in examples

#### 🟡 Medium Priority

- **Outdated dependency information**
  - Examples using known-vulnerable package versions
  - Security recommendations that are no longer valid
  - Insecure practices recommended

- **Misinformation**
  - Incorrect security practices
  - False claims about uv security
  - Dangerous recommendations

#### 🟢 Low Priority

- **Typos in security-related sections** (use public issues)
- **Formatting issues** in security documentation (use public issues)

### Out of Scope

These should be reported to [Astral's uv repository](https://github.com/astral-sh/uv) instead:

- Vulnerabilities in uv itself
- Issues with PyPI or Python packages
- Security issues in other projects

---

## Security Best Practices

This handbook follows these security practices:

### ✅ What We Do

- Review all contributed content for security issues
- Verify code examples work safely
- Keep dependencies current
- Monitor for security vulnerabilities
- Respond promptly to security reports
- Test examples before publishing
- Link to official, reputable sources

### ✅ What We Recommend

We recommend users:

- Never share API keys or secrets in code
- Always use `.env` files for sensitive data
- Follow official uv security guidance
- Report uv security issues to [Astral](https://github.com/astral-sh/uv/security)
- Use virtual environments (as taught in handbook)
- Keep uv and Python updated
- Verify package sources on PyPI

---

## Security Updates

### Process

When a security issue is reported:

1. **Assessment** (within 24 hours)
   - Verify the issue
   - Determine severity
   - Identify affected content

2. **Remediation** (within 7 days)
   - Fix the issue
   - Update documentation
   - Test changes

3. **Disclosure** (after fix is merged)
   - Publish security advisory
   - Credit the reporter (if desired)
   - Update CHANGELOG.md

### Notification

You'll be notified if:
- You report a security issue (status updates)
- You request it (security advisories)

### Timeline

**Critical Issues:** Fix within 24-48 hours
**High Issues:** Fix within 3-5 days
**Medium Issues:** Fix within 1-2 weeks
**Low Issues:** Fix in next release

---

## Security Advisories

All security issues, once fixed, are disclosed via [GitHub Security Advisories](https://github.com/astral-sh/uv-beginners-handbook/security/advisories).

Subscribe to be notified of new advisories.

---

## Dependencies

This documentation repository has minimal dependencies:

- **No Python packages** — It's documentation
- **No JavaScript libraries** — Markdown only
- **No external services** — GitHub-hosted

The handbook recommends packages, but doesn't include them.

For uv security issues, see: https://github.com/astral-sh/uv/security

---

## Developer Security

### For Contributors

When contributing:

1. **Don't include secrets**
   - No API keys
   - No authentication tokens
   - No private credentials

2. **Verify examples**
   - Test code before submitting
   - Check it's secure
   - Ensure it follows best practices

3. **Link to official sources**
   - Use authoritative URLs
   - Verify links are current
   - Avoid suspicious sources

4. **Review others' contributions**
   - Check for malicious code
   - Verify accuracy
   - Flag security concerns

---

## Third-Party Services

This repository:

- ✅ Uses **GitHub** (Microsoft-owned, secure)
- ✅ Uses **GitHub Actions** for validation
- ✅ Follows **GitHub security guidelines**

We do NOT:

- ❌ Include external tracking
- ❌ Use unverified services
- ❌ Sell or share user data
- ❌ Link to suspicious sites

---

## Compliance

This project:

- ✅ Follows [OWASP guidelines](https://owasp.org/)
- ✅ Adheres to secure coding practices
- ✅ Uses GitHub's security features
- ✅ Maintains responsible disclosure
- ✅ Publishes security advisories

---

## Contact

### Report a Security Issue

Use [GitHub Security Advisory](https://github.com/mkcoder7586-beep/uv-beginners-handbook/security/advisories).

### General Security Questions

Open a [GitHub discussion](https://github.com/mkcoder7586-beep/uv-beginners-handbook/discussions) tagged `security`.

### Contact Maintainers

For sensitive matters not suited to public reporting:

- Check repository for maintainer contact info
- Include `[SECURITY]` in subject line
- Provide details in encrypted format if needed

---

## Acknowledgments

We thank security researchers and community members who:

- Report vulnerabilities responsibly
- Help improve our security practices
- Contribute security fixes
- Test and review content

Your contributions help keep this resource safe for everyone.

---

## Security Resources

Learn more about security:

- **[OWASP Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/)**
- **[Python Security Best Practices](https://python.readthedocs.io/en/latest/library/security_warnings.html)**
- **[PyPI Security](https://pypi.org/help/#security)**
- **[Astral Security](https://github.com/astral-sh/uv/security)**

---

**Last Updated:** June 28, 2026

For questions, use [GitHub Security Advisory](https://github.com/mkcoder7586-beep/uv-beginners-handbook/security/advisories).