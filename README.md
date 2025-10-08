# 🚀 RubixKube™ Documentation

![RubixKube Logo](https://github.com/rubixkube-io/docs/blob/d11202b7fb45fdcf1551c7c11a25c9a67e2dcbd2/images/hero-dark.png)

### The Reliability Layer for the AI Era 🤖✨

**RubixKube™** is an AI-native mesh of intelligent agents that prevents downtime, safeguards revenue, and creates peace of mind at scale.

> 💡 Think of it as your second brain for infrastructure — one that never sleeps, never forgets, and always protects your uptime and your bottom line.

[![Beta](https://img.shields.io/badge/Status-Beta-orange?style=for-the-badge&logo=rocket)](https://docs.rubixkube.ai/getting-started/disclaimers)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge&logo=github)](LICENSE)
[![Docs](https://img.shields.io/badge/Docs-Live-green?style=for-the-badge&logo=readthedocs)](https://docs.rubixkube.ai)
[![Console](https://img.shields.io/badge/Console-Live-purple?style=for-the-badge&logo=internet-computer)](https://console.rubixkube.ai)

---

## 🔥 Why RubixKube?

In a world where AI builds your products, **RubixKube keeps them alive**. We're not just another monitoring tool — we're your **Site Reliability Intelligence (SRI)** platform that combines AI agents, deep Kubernetes expertise, and automated remediation to create **self-healing infrastructure**.

| Problem | RubixKube Solution |
|:------------|:-----------------------|
| 🏥 Infrastructure failures cause revenue loss | 🤖 AI agents detect and fix issues before users notice |
| 🔍 Root cause analysis takes hours/days | 🧠 Dependency graphs show blast radius in seconds |
| 🚨 Alert fatigue from noisy monitoring | 💬 Natural language queries like "Why is checkout slow?" |
| 📊 MTTR too high despite observability | ⚡ Automated remediation with safety guardrails |
| 💰 Downtime costs you real money | 📈 Business impact metrics connect infra to revenue |

---

## 🎯 Core Features

### 🧠 AI Agent Mesh
Specialized AI agents collaborate:
- **Detective Agent** - Investigates root causes with evidence
- **Remediation Agent** - Proposes and applies safe fixes
- **Memory Agent** - Learns from every incident
- **Guardian Agent** - Enforces safety policies

### 🔍 Evidence-Linked RCA
Every incident includes:
- Dependency graphs showing impact radius
- Timeline of events leading to failure
- Logs and metrics correlation
- AI explanations in plain English

### 🔮 Predictive Prevention
Catch issues before they impact users:
- Detect risky deployments
- Identify configuration drift
- Spot resource exhaustion early
- Alert on anomalous patterns

### 💬 Conversational Infra
Manage your cluster using natural language:
- "Why is my checkout service slow?"
- "Show me pods with high memory usage"
- "What changed in the last hour?"
- "Restart the payment service"

---

## 🚀 Quick Start (3 Minutes)

### 1. Get Beta Access
Sign up for free at [console.rubixkube.ai](https://console.rubixkube.ai)

**Note**: Beta Software - Read our [disclaimers](https://docs.rubixkube.ai/getting-started/disclaimers) first. Production release coming soon!

### 2. Install RubixKube

#### Local (KIND)
```bash
# Install KIND if needed
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.20.0/kind-linux-amd64
chmod +x ./kind && sudo mv ./kind /usr/local/bin/

# Create cluster and install RubixKube
kind create cluster --name rubixkube-demo
kubectl apply -f https://console.rubixkube.ai/install/local
```

#### Cloud (AWS/GKE/AKS)
```bash
# Add our Helm repo
helm repo add rubixkube https://charts.rubixkube.ai
helm repo update

# Install RubixKube
helm install rubixkube rubixkube/rubixkube \
  --create-namespace --namespace rubixkube-system
```

For detailed installation guides, check our [KIND setup](https://docs.rubixkube.ai/getting-started/installation-kind) and [cloud installation](https://docs.rubixkube.ai/getting-started/installation-cloud) docs.

### 3. Start Talking to Your Infra
Open your dashboard and try:
- "Show me all pods in my cluster"
- "What's the health status of my deployments?"
- "Check for any failing pods"

[Try Breaking a Pod](https://docs.rubixkube.ai/tutorials/break-pod-image-error) - Learn by watching RubixKube detect and fix issues in real-time.

---

## 📚 Documentation Structure

- **[Quickstart](https://docs.rubixkube.ai/quickstart)**: Get running in minutes with step-by-step guides
- **[Getting Started](https://docs.rubixkube.ai/getting-started/introduction)**: Sign up, installation, and first steps
- **[Tutorials](https://docs.rubixkube.ai/tutorials/first-steps)**: Hands-on guides: break pods, analyze costs, troubleshoot
- **[Core Concepts](https://docs.rubixkube.ai/concepts/what-is-sri)**: SRI, Agent Mesh, Memory Engine, Guardrails
- **[Using RubixKube](https://docs.rubixkube.ai/using/dashboard)**: Dashboard, insights, agents, integrations
- **[API Reference](https://docs.rubixkube.ai/api-reference/introduction)**: REST APIs, webhooks, and CLI commands

---

## 👥 Who Uses RubixKube?

- **🔧 DevOps Engineers**: Automate incident response and reduce toil with AI-powered remediation
- **👨‍💼 Site Reliability Engineers**: Enhance observability and cut MTTR with intelligent root cause analysis
- **🏗️ Platform Engineers**: Build self-healing infrastructure at scale with autonomous operations
- **👶 Junior Developers**: Learn SRE practices with AI guidance and interactive troubleshooting
- **📊 Engineering Managers**: Reduce on-call burden and improve team velocity with automated fixes
- **💼 CTOs & VPs**: Protect revenue and improve reliability metrics with business impact insights

---

## 🛠️ Local Development

This site is built with [Mintlify](https://mintlify.com) - a blazingly fast documentation platform.

### Prerequisites
- Node.js 16+
- npm or yarn

### Get Started
```bash
# Install CLI
npm i -g mint

# Run locally (from repo root)
mint dev

# Preview at http://localhost:3000
```

### For Contributors
- Write in **MDX** (Markdown + React components)
- Follow our [style guide](https://docs.rubixkube.ai/essentials/markdown)
- Test all links and code examples
- Preview images in `/images/` before publishing
- Read our full [Contributing Guide](CONTRIBUTING.md) for detailed steps
- Use [Issue Templates](https://github.com/rubixkube-io/docs/issues/new/choose) for bug reports or docs suggestions
- Follow the [PR Template](https://github.com/rubixkube-io/docs/blob/main/.github/PULL_REQUEST_TEMPLATE.md) for pull requests

---

## 🌐 Resources & Community

- **[Website](https://rubixkube.ai)**: Learn about our mission and vision
- **[Documentation](https://docs.rubixkube.ai)**: Complete guides and API references
- **[Console/Dashboard](https://console.rubixkube.ai)**: Manage your RubixKube deployment
- **[Blog](https://rubixkube.ai/blog)**: Deep dives, tutorials, and announcements
- **[Community Slack](https://rubixkube-community.slack.com)**: Connect with users and get support
- **[X/Twitter](https://x.com/RubixKubeHQ)**: Follow for updates and tips
- **[LinkedIn](https://linkedin.com/company/rubixkube)**: Company news and industry insights
- **[GitHub](https://github.com/rubixkube-io)**: Open source components and examples

---

## 🤝 Contributing

We ❤️ contributions! Here's how to help:

### Documentation
- Found a typo? [Open an issue](https://github.com/rubixkube-io/docs/issues)
- Want to improve a guide? [Submit a PR](https://github.com/rubixkube-io/docs/pulls)
- Follow our [style guide](https://docs.rubixkube.ai/essentials/markdown)

### Bug Reports
- Found an issue? [Report it](https://github.com/rubixkube-io/rubixkube/issues)
- Include steps to reproduce and environment details
- Check existing issues first

### Feature Requests
- Have an idea? [Start a discussion](https://github.com/rubixkube-io/rubixkube/discussions)
- Join our [Community Slack](https://rubixkube-community.slack.com)
- Help us prioritize what to build next

### Platform Development
- Want to contribute code? Check [rubixkube-io/rubixkube](https://github.com/rubixkube-io/rubixkube)
- Read our [contributing guidelines](CONTRIBUTING.md)
- Join our developer community calls

### Community Guidelines
We strive to maintain a welcoming and inclusive community. Please review our:
- [Code of Conduct](CODE_OF_CONDUCT.md) - Community behavior guidelines
- [Contributing Guide](CONTRIBUTING.md) - How to contribute to the project
- [Security Policy](SECURITY.md) - How to report security vulnerabilities

### Issue Reports & Contributions
Found a problem or want to contribute?
- **Bug Reports**: Use our [Issue Templates](https://github.com/rubixkube-io/docs/issues/new/choose) for structured problem reports
- **Pull Requests**: Follow our [PR Template](https://github.com/rubixkube-io/docs/blob/main/.github/PULL_REQUEST_TEMPLATE.md) for contributions
- **Content Proposals**: Propose new documentation via [Contribution Issues](https://github.com/rubixkube-io/docs/issues/new?template=documentation_contribution.yml)

---

## ⚖️ License & Legal

- **Documentation License**: This documentation is licensed under the [MIT License](LICENSE)
- **Platform Terms**: RubixKube platform has its own [terms of service](https://rubixkube.ai/legal)

---

## 🎯 Join the Movement

RubixKube isn't just another DevOps tool. It's the seatbelt, backup generator, and peace-of-mind layer for modern infrastructure.

If your infra breaks, your revenue breaks. RubixKube exists to make sure that never happens.

🚀 [Get started today](https://console.rubixkube.ai) and experience the future of infrastructure reliability.

---

Built with ❤️ by the RubixKube team

[Website](https://rubixkube.ai) • [Docs](https://docs.rubixkube.ai) • [Console](https://console.rubixkube.ai) • [GitHub](https://github.com/rubixkube-io)
