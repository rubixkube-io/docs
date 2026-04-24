# RubixKube Documentation

![RubixKube](https://raw.githubusercontent.com/rubixkube-io/docs/main/images/hero-dark.png)

> **Beyond observability. Your infrastructure, healing itself.**

This repository holds the public documentation for **RubixKube**, the Site Reliability Intelligence (SRI) platform. An AI-native system that detects anomalies, diagnoses root cause, and resolves failures across Kubernetes, AWS, GCP, Azure and Linux VMs. Most tools see your infrastructure for the first time, every time. RubixKube remembers.

[![Status: GA](https://img.shields.io/badge/status-GA-success)](https://rubixkube.ai/status)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Docs](https://img.shields.io/badge/docs-live-green)](https://docs.rubixkube.ai)
[![Console](https://img.shields.io/badge/console-live-purple)](https://console.rubixkube.ai)

---

## What is Site Reliability Intelligence?

Site Reliability Intelligence goes beyond observability. It closes the full loop: observe, plan, execute, learn. A system that compounds knowledge over time rather than starting from scratch on every incident.

### Key capabilities

- **Autonomous remediation.** Detect, diagnose and resolve failures without waking your team.
- **Compounding memory.** Every signal, session and resolution builds a deeper model of your system.
- **Human-in-the-loop guardrails.** Approvals and policy checks when you want them.
- **Zero new tooling.** Plugs into the stack you already run on day one.

---

## How it works: compounding memory

Most tools treat every incident as a fresh start. RubixKube builds a persistent model of your infrastructure that deepens over time.

| Milestone | What RubixKube learns |
|:--|:--|
| **Day 1** | Topology mapped. Every service, node and edge, automatically. |
| **Week 1** | Dependencies understood. Upstream and downstream relationships known. |
| **Month 1** | Causality emerging. Failure patterns surface before they fire. |
| **Always** | Yours, entirely. A model no other tool has, built only by being there. |

---

## The platform in one paragraph

A coordinated **Agent Mesh** observes your environments through a lightweight, read-only **Observer**, plans and investigates through an **SRI Agent**, remembers through the **Memory Engine** and **Knowledge Graph**, produces evidence-linked root cause reports through the **RCA Pipeline**, and proposes fixes through the **Remediation Agent**, all behind a **Guardian Agent** that enforces policy. The whole thing runs a continuous [OPEL loop](https://docs.rubixkube.ai/concepts/opel-loop) so the platform gets sharper with every incident.

---

## Quick start

1. **Create your workspace.** Sign up at [console.rubixkube.ai](https://console.rubixkube.ai). It takes under a minute. Grab your API key from the dashboard (it starts with `rk_`).
2. **Connect an environment.** Pick your first target and follow the guide.
3. **Start a conversation.** Open the dashboard and ask a question, or install the [Rubix CLI](https://docs.rubixkube.ai/cli/overview) and ask it from your terminal.

Environment guides:

- [Kubernetes](https://docs.rubixkube.ai/environments/kubernetes)
- [AWS](https://docs.rubixkube.ai/environments/aws)
- [GCP](https://docs.rubixkube.ai/environments/gcp)
- [Azure](https://docs.rubixkube.ai/environments/azure)
- [Linux VMs and bare metal](https://docs.rubixkube.ai/environments/vm)

Or start with the guided overview at [Connect your environment](https://docs.rubixkube.ai/getting-started/connect-your-environment).

---

## Documentation structure

| Section | What you will find |
|:--|:--|
| [Getting Started](https://docs.rubixkube.ai/getting-started/overview) | Welcome, quickstart, connect your environment. |
| [Core Concepts](https://docs.rubixkube.ai/concepts/how-rubixkube-works) | How RubixKube works, OPEL loop, Observer, Memory Engine, Knowledge Graph, Agent Mesh, Skills, Insights, RCA, Actions, Environments, Guardrails. |
| [Environments](https://docs.rubixkube.ai/environments/kubernetes) | Kubernetes, AWS, GCP, Azure, Linux VMs. |
| [Platform Capabilities](https://docs.rubixkube.ai/using/dashboard) | Dashboard, Rubix Chat Agent, Insights, Actions, RCA Reports, Analytics, Infrastructure, Integrations, Skills, Notifications, Workspace, Agent Skills Store. |
| [Integrations](https://docs.rubixkube.ai/using/integrations) | GitHub, GitLab, Slack, Teams, PagerDuty, Linear, Notion, Datadog, New Relic, Dynatrace, Prometheus, Grafana, Sentry, plus custom MCP and REST. |
| [Tutorials](https://docs.rubixkube.ai/tutorials/monitor-infrastructure-health) | Monitor health, automate remediation, talk to your infra, add custom skills and integrations. |
| [Rubix CLI](https://docs.rubixkube.ai/cli/overview) | Install, configure, commands, examples. |
| [Support](https://docs.rubixkube.ai/support/troubleshooting) | Troubleshooting, FAQ, system status, glossary. |

---

## Local development

This site is built with [Mintlify](https://mintlify.com).

### Prerequisites

- Node.js 18 or higher
- npm or yarn

### Run it locally

```bash
# Install the Mintlify CLI
npm i -g mint

# From the repo root
mint dev

# Preview at http://localhost:3000
```

### Writing guidelines

- Write in **MDX**. Markdown plus the Mintlify components.
- Lead with the answer. Use question-shaped headings when it helps AEO and GEO.
- Short sentences. Plain language. No em dashes.
- Verify every link and code example before opening a PR.
- Keep images under `/images/` and use descriptive filenames.

See the full [Contributing Guide](CONTRIBUTING.md) for the workflow.

---

## Contributing

Contributions are welcome.

- **Typos and small fixes.** Open a PR directly.
- **Larger changes.** File an issue first using the [issue templates](https://github.com/rubixkube-io/docs/issues/new/choose) so we can align on scope.
- **Platform bugs.** Report at [rubixkube-io/rubixkube](https://github.com/rubixkube-io/rubixkube/issues) with steps to reproduce and environment details.
- **Feature requests.** Start a thread in [Discussions](https://github.com/rubixkube-io/rubixkube/discussions).

Community guidelines:

- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Contributing Guide](CONTRIBUTING.md)
- [Security Policy](SECURITY.md)

---

## Resources

- **Website.** [rubixkube.ai](https://rubixkube.ai)
- **Documentation.** [docs.rubixkube.ai](https://docs.rubixkube.ai)
- **Console.** [console.rubixkube.ai](https://console.rubixkube.ai)
- **System status.** [rubixkube.ai/status](https://rubixkube.ai/status)
- **Blog.** [rubixkube.ai/blog](https://rubixkube.ai/blog)
- **GitHub.** [github.com/rubixkube-io](https://github.com/rubixkube-io)
- **LinkedIn.** [linkedin.com/company/rubixkube](https://linkedin.com/company/rubixkube)
- **X.** [@RubixKubeHQ](https://x.com/RubixKubeHQ)

---

## License

The documentation in this repository is released under the [MIT License](LICENSE). The RubixKube platform has its own [terms of service](https://rubixkube.ai/legal).

---

**RubixKube.** Site Reliability Intelligence.

connect@rubixkube.ai • Bengaluru, India
