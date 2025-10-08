---
<div align="center">

# 🚀 RubixKube™ Documentation

<p align="center">
  <img src="https://github.com/rubixkube-io/docs/blob/d11202b7fb45fdcf1551c7c11a25c9a67e2dcbd2/images/hero-dark.png" alt="RubixKube Logo" width="500"/>
</p>

### **The Reliability Layer for the AI Era** 🤖✨

**RubixKube™** is an AI-native mesh of intelligent agents that prevents downtime, safeguards revenue, and creates peace of mind at scale.

> 💡 **Think of it as your second brain for infrastructure** — one that never sleeps, never forgets, and always protects your uptime and your bottom line.

[![Beta](https://img.shields.io/badge/Status-Beta-orange?style=for-the-badge&logo=rocket)](https://docs.rubixkube.ai/getting-started/disclaimers)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge&logo=github)](LICENSE)
[![Docs](https://img.shields.io/badge/Docs-Live-green?style=for-the-badge&logo=readthedocs)](https://docs.rubixkube.ai)
[![Console](https://img.shields.io/badge/Console-Live-purple?style=for-the-badge&logo=internet-computer)](https://console.rubixkube.ai)

</div>

---

## 🔥 Why RubixKube?

In a world where AI builds your products, **RubixKube keeps them alive**. We're not just another monitoring tool — we're your **Site Reliability Intelligence (SRI)** platform that combines AI agents, deep Kubernetes expertise, and automated remediation to create **self-healing infrastructure**.

| **Problem** | **RubixKube Solution** |
|:------------|:-----------------------|
| 🏥 **Infrastructure failures** cause revenue loss | 🤖 **AI agents** detect and fix issues before users notice |
| 🔍 **Root cause analysis** takes hours/days | 🧠 **Dependency graphs** show blast radius in seconds |
| 🚨 **Alert fatigue** from noisy monitoring | 💬 **Natural language queries** like "Why is checkout slow?" |
| 📊 **MTTR too high** despite observability | ⚡ **Automated remediation** with safety guardrails |
| 💰 **Downtime costs** you real money | 📈 **Business impact metrics** connect infra to revenue |

---

## 🎯 Core Features

<CardGroup cols={2}>
  <Card title="🧠 AI Agent Mesh" icon="network-wired">
    Specialized AI agents collaborate:
    - **Detective Agent** - Investigates root causes with evidence
    - **Remediation Agent** - Proposes and applies safe fixes
    - **Memory Agent** - Learns from every incident
    - **Guardian Agent** - Enforces safety policies
  </Card>
  <Card title="🔍 Evidence-Linked RCA" icon="magnifying-glass-chart">
    Every incident includes:
    - Dependency graphs showing impact radius
    - Timeline of events leading to failure
    - Logs and metrics correlation
    - AI explanations in plain English
  </Card>
  <Card title="🔮 Predictive Prevention" icon="triangle-exclamation">
    Catch issues before they impact users:
    - Detect risky deployments
    - Identify configuration drift
    - Spot resource exhaustion early
    - Alert on anomalous patterns
  </Card>
  <Card title="💬 Conversational Infra" icon="message">
    Manage your cluster using natural language:
    - "Why is my checkout service slow?"
    - "Show me pods with high memory usage"
    - "What changed in the last hour?"
    - "Restart the payment service"
  </Card>
</CardGroup>

---

## 🚀 Quick Start (3 Minutes)

<Steps>
  <Step title="🎫 Get Beta Access">
    Sign up for free at **[console.rubixkube.ai](https://console.rubixkube.ai)**

    <Info>
    ⚠️ **Beta Software** - Read our [disclaimers](/getting-started/disclaimers) first. Production release coming soon!
    </Info>
  </Step>

  <Step title="🛠️ Install RubixKube">
    <TabGroup>
      <Tab title="Local (KIND)" icon="laptop">
        ```bash
        # Install KIND if needed
        curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.20.0/kind-linux-amd64
        chmod +x ./kind && sudo mv ./kind /usr/local/bin/

        # Create cluster and install RubixKube
        kind create cluster --name rubixkube-demo
        kubectl apply -f https://console.rubixkube.ai/install/local
        ```
      </Tab>

      <Tab title="Cloud (AWS/GKE/AKS)" icon="cloud">
        ```bash
        # Add our Helm repo
        helm repo add rubixkube https://charts.rubixkube.ai
        helm repo update

        # Install RubixKube
        helm install rubixkube rubixkube/rubixkube \
          --create-namespace --namespace rubixkube-system
        ```
      </Tab>
    </TabGroup>
  </Step>

  <Step title="💬 Start Talking to Your Infra">
    Open your dashboard and try:
    - *"Show me all pods in my cluster"*
    - *"What's the health status of my deployments?"*
    - *"Check for any failing pods"*

    <Card title="📚 Try Breaking a Pod" icon="flask" href="/tutorials/break-pod-image-error">
      Learn by watching RubixKube detect and fix issues in real-time
    </Card>
  </Step>
</Steps>

---

## 📚 Documentation Structure

<CardGroup cols={2}>
  <Card title="🚀 Quickstart" icon="zap" href="https://docs.rubixkube.ai/quickstart">
    Get running in minutes with step-by-step guides
  </Card>
  <Card title="📖 Getting Started" icon="book-open" href="https://docs.rubixkube.ai/getting-started/introduction">
    Sign up, installation, and first steps
  </Card>
  <Card title="🎓 Tutorials" icon="graduation-cap" href="https://docs.rubixkube.ai/tutorials/first-steps">
    Hands-on guides: break pods, analyze costs, troubleshoot
  </Card>
  <Card title="🧠 Core Concepts" icon="brain" href="https://docs.rubixkube.ai/concepts/what-is-sri">
    SRI, Agent Mesh, Memory Engine, Guardrails
  </Card>
  <Card title="⚙️ Using RubixKube" icon="cog" href="https://docs.rubixkube.ai/using/dashboard">
    Dashboard, insights, agents, integrations
  </Card>
  <Card title="🔌 API Reference" icon="code" href="https://docs.rubixkube.ai/api-reference/introduction">
    REST APIs, webhooks, and CLI commands
  </Card>
</CardGroup>

---

## 👥 Who Uses RubixKube?

<CardGroup cols={3}>
  <Card title="🔧 DevOps Engineers" icon="server">
    Automate incident response and reduce toil with AI-powered remediation
  </Card>
  <Card title="👨‍💼 Site Reliability Engineers" icon="gauge">
    Enhance observability and cut MTTR with intelligent root cause analysis
  </Card>
  <Card title="🏗️ Platform Engineers" icon="layer-group">
    Build self-healing infrastructure at scale with autonomous operations
  </Card>
  <Card title="👶 Junior Developers" icon="graduation-cap">
    Learn SRE practices with AI guidance and interactive troubleshooting
  </Card>
  <Card title="📊 Engineering Managers" icon="users">
    Reduce on-call burden and improve team velocity with automated fixes
  </Card>
  <Card title="💼 CTOs & VPs" icon="briefcase">
    Protect revenue and improve reliability metrics with business impact insights
  </Card>
</CardGroup>

---

## 🛠️ Local Development

This site is built with [Mintlify](https://mintlify.com) - a blazingly fast documentation platform.

### Prerequisites
- **Node.js** 16+
- **npm** or **yarn**

### Get Started
```bash
# Install CLI
npm i -g mint

# Run locally (from repo root)
mint dev

# Preview at http://localhost:3000
```

### For Contributors
- 📝 Write in **MDX** (Markdown + React components)
- 🎨 Follow our [style guide](https://docs.rubixkube.ai/essentials/markdown)
- 🧪 Test all links and code examples
- 📸 Preview images in `/images/` before publishing

---

## 🌐 Resources & Community

<CardGroup cols={2}>
  <Card title="🌐 Website" icon="globe" href="https://rubixkube.ai">
    Learn about our mission and vision
  </Card>
  <Card title="📖 Documentation" icon="book" href="https://docs.rubixkube.ai">
    Complete guides and API references
  </Card>
  <Card title="🎮 Console/Dashboard" icon="monitor" href="https://console.rubixkube.ai">
    Manage your RubixKube deployment
  </Card>
  <Card title="📝 Blog" icon="newspaper" href="https://rubixkube.ai/blog">
    Deep dives, tutorials, and announcements
  </Card>
  <Card title="💬 Community Slack" icon="slack" href="https://rubixkube-community.slack.com">
    Connect with users and get support
  </Card>
  <Card title="🐦 X/Twitter" icon="twitter" href="https://x.com/RubixKubeHQ">
    Follow for updates and tips
  </Card>
  <Card title="💼 LinkedIn" icon="linkedin" href="https://linkedin.com/company/rubixkube">
    Company news and industry insights
  </Card>
  <Card title="🔧 GitHub" icon="github" href="https://github.com/rubixkube-io">
    Open source components and examples
  </Card>
</CardGroup>

---

## 🤝 Contributing

We ❤️ contributions! Here's how to help:

<CardGroup cols={2}>
  <Card title="📝 Documentation" icon="pen">
    - Found a typo? [Open an issue](https://github.com/rubixkube-io/docs/issues)
    - Want to improve a guide? [Submit a PR](https://github.com/rubixkube-io/docs/pulls)
    - Follow our [style guide](https://docs.rubixkube.ai/essentials/markdown)
  </Card>
  <Card title="🐛 Bug Reports" icon="bug">
    - Found an issue? [Report it](https://github.com/rubixkube-io/rubixkube/issues)
    - Include steps to reproduce and environment details
    - Check existing issues first
  </Card>
  <Card title="💡 Feature Requests" icon="lightbulb">
    - Have an idea? [Start a discussion](https://github.com/rubixkube-io/rubixkube/discussions)
    - Join our [Community Slack](https://rubixkube-community.slack.com)
    - Help us prioritize what to build next
  </Card>
  <Card title="🚀 Platform Development" icon="rocket">
    - Want to contribute code? Check [rubixkube-io/rubixkube](https://github.com/rubixkube-io/rubixkube)
    - Read our [contributing guidelines](CONTRIBUTING.md)
    - Join our developer community calls
  </Card>
</CardGroup>

### Community Guidelines

We strive to maintain a welcoming and inclusive community. Please review our:
- [Code of Conduct](CODE_OF_CONDUCT.md) - Community behavior guidelines
- [Contributing Guide](CONTRIBUTING.md) - How to contribute to the project
- [Security Policy](SECURITY.md) - How to report security vulnerabilities

### Issue Reports & Contributions

**Found a problem or want to contribute?**

- **🐛 Bug Reports** - Use our [Issue Templates](https://github.com/rubixkube-io/docs/issues/new/choose) for structured problem reports
- **📝 Pull Requests** - Follow our [PR Template](https://github.com/rubixkube-io/docs/blob/main/.github/PULL_REQUEST_TEMPLATE.md) for contributions
- **📚 Content Proposals** - Propose new documentation via [Contribution Issues](https://github.com/rubixkube-io/docs/issues/new?template=documentation_contribution.yml)

---

## ⚖️ License & Legal

<CardGroup cols={2}>
  <Card title="📄 Documentation License" icon="file-text">
    This documentation is licensed under the [MIT License](LICENSE).
  </Card>
  <Card title="⚖️ Platform Terms" icon="balance-scale">
    RubixKube platform has its own [terms of service](https://rubixkube.ai/legal).
  </Card>
</CardGroup>

---

## 🎯 Join the Movement

<Card>
  <CardHeader>
    **RubixKube isn't just another DevOps tool.**
  </CardHeader>
  <CardBody>
    It's the **seatbelt, backup generator, and peace-of-mind layer** for modern infrastructure.

    **If your infra breaks, your revenue breaks.** RubixKube exists to make sure that never happens.

    🚀 **[Get started today](https://console.rubixkube.ai)** and experience the future of infrastructure reliability.
  </CardBody>
</Card>

---

<div align="center">
  <p><strong>Built with ❤️ by the RubixKube team</strong></p>
  <p>
    <a href="https://rubixkube.ai">Website</a> •
    <a href="https://docs.rubixkube.ai">Docs</a> •
    <a href="https://console.rubixkube.ai">Console</a> •
    <a href="https://github.com/rubixkube-io">GitHub</a>
  </p>
</div>

