# Contributing to RubixKube

Thank you for your interest in contributing to RubixKube! We welcome contributions from everyone, whether you're fixing a typo, improving documentation, reporting bugs, or implementing new features.

## 📋 Table of Contents

- [Ways to Contribute](#ways-to-contribute)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Documentation Contributions](#documentation-contributions)
- [Reporting Issues](#reporting-issues)
- [Pull Request Process](#pull-request-process)
- [Community Guidelines](#community-guidelines)

## 🎯 Ways to Contribute

There are many ways to contribute to RubixKube:

### 📚 Documentation
- Fix typos and improve clarity
- Add examples and use cases
- Create tutorials and guides
- Improve API documentation
- Translate content

### 🐛 Bug Reports & Issues
- Report bugs with detailed reproduction steps
- Suggest enhancements and new features
- Ask questions and get help

### 🎨 Design & UX
- Improve UI/UX in the dashboard
- Create icons and illustrations
- Enhance the visual design

## 🚀 Getting Started

### 1. Set Up Your Environment

You need Node.js 18 or higher and npm or yarn.

```bash
# Clone the docs repository
git clone https://github.com/rubixkube-io/docs.git
cd docs

# Install the Mintlify CLI
npm i -g mint

# Start the local preview (http://localhost:3000)
mint dev
```

This repository holds the public documentation only. The RubixKube platform source is not public, so contributions here are to the docs.

### 2. Explore the Project

- **Documentation**: Browse [docs.rubixkube.ai](https://docs.rubixkube.ai) to understand the structure
- **Platform**: Review the [community README](https://github.com/rubixkube-io/community) and architecture docs
- **Issues**: Check [open issues](https://github.com/rubixkube-io/community/issues) for contribution opportunities

### 3. Join the Community

- **Slack**: Join our [Community Slack](https://rubixkube-community.slack.com) for discussions
- **GitHub Discussions**: Participate in [feature discussions](https://github.com/rubixkube-io/community/discussions/categories/ideas)
- **Office Hours**: Join our weekly community calls (announced on Slack)

## 📝 Documentation Contributions

### Documentation Structure
```
docs/
├── getting-started/     # Installation and setup guides
├── tutorials/          # Hands-on walkthroughs
├── concepts/           # Core concept explanations
├── using/              # Feature usage guides
├── api-reference/      # API documentation
├── support/            # Troubleshooting and FAQs
└── images/             # Screenshots and diagrams
```

### Writing Guidelines

**Style & Tone:**
- Use clear, conversational language
- Focus on user goals and outcomes
- Include practical examples
- Be inclusive and accessible

**Technical Writing:**
- Use [MDX syntax](https://docs.rubixkube.ai/essentials/markdown) for rich content
- Include code examples with proper syntax highlighting
- Add screenshots for UI features
- Test all links and commands

**Content Organization:**
- Start with "why" before "how"
- Use progressive disclosure (basic → advanced)
- Include prerequisites and next steps
- Add related content links

### Documentation Workflow

1. **Choose a topic** from [good first issues](https://github.com/rubixkube-io/docs/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22)
2. **Create or edit** content in the appropriate folder
3. **Preview locally** with `mint dev`
4. **Submit a pull request** with clear description

## 🐛 Reporting Issues

### Bug Reports

**Good Bug Reports Include:**
- Clear, descriptive title
- Steps to reproduce the issue
- Expected vs actual behavior
- Environment details (OS, Kubernetes version, etc.)
- Error messages and logs
- Screenshots if applicable

**Template:**
```markdown
## Description
[Brief description of the bug]

## Steps to Reproduce
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Expected Behavior
[What should happen]

## Actual Behavior
[What actually happens]

## Environment
- RubixKube version: [version]
- Kubernetes version: [version]
- OS: [OS and version]
- Browser: [if applicable]

## Additional Context
[Any other relevant information]
```

### Feature Requests

**Good Feature Requests Include:**
- Clear problem statement
- Proposed solution
- Use cases and benefits
- Alternative solutions considered
- Implementation suggestions

## 🔄 Pull Request Process

### 1. Fork and Branch

```bash
# Fork the repository
# Clone your fork
git clone https://github.com/YOUR_USERNAME/docs.git
cd docs

# Create a branch
git checkout -b docs/improve-installation-guide
```

### 2. Make Changes

- Make focused, atomic changes
- Follow the existing page style and structure

### 3. Test Thoroughly

```bash
mint dev  # Preview changes locally
```

### 4. Commit and Push

```bash
# Stage your changes
git add .

# Write clear commit message
git commit -m "Add: comprehensive installation guide for KIND

- Add step-by-step KIND installation
- Include troubleshooting section
- Add verification commands"

# Push to your fork
git push origin docs/improve-installation-guide
```

### 5. Create Pull Request

- Use clear, descriptive title
- Reference related issues
- Explain changes and motivation
- Include screenshots for UI changes
- Update checklist as needed

**PR Template:**
```markdown
## Description
[Brief description of changes]

## Related Issues
Closes #123

## Changes Made
- [ ] Feature A implemented
- [ ] Bug B fixed
- [ ] Tests added for C

## Testing
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Manual testing completed

## Documentation
- [ ] README updated
- [ ] API docs updated
- [ ] User guide updated
```

## 🏆 Recognition

We love recognizing our contributors! Contributors may be:

- **Featured** in our community spotlight
- **Mentioned** in release notes
- **Invited** to contribute to core features
- **Nominated** for maintainer roles

## 📞 Getting Help

### Community Resources
- **Slack**: [#contributors](https://rubixkube-community.slack.com) channel
- **GitHub Discussions**: [Q&A category](https://github.com/rubixkube-io/community/discussions/categories/q-a)
- **Office Hours**: Weekly community calls (announced on Slack)

### Asking Questions
1. Check existing documentation and issues
2. Search Slack history for similar questions
3. Ask in appropriate channel with context
4. Be patient and respectful of time zones

## 📋 Code of Conduct

All contributors must follow our [Code of Conduct](CODE_OF_CONDUCT.md). We are committed to providing a harassment-free experience for everyone.

## 🎉 Thank You!

Your contributions make RubixKube better for everyone. Whether you're fixing a typo, reporting a bug, or implementing a major feature, we appreciate your time and expertise.

**Happy contributing!** 🚀

---

*This contributing guide is adapted from open source best practices and is itself open to improvement. Found something unclear? [Let us know!](https://github.com/rubixkube-io/docs/issues)*
