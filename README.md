---

# RubixKube™ Docs

<p align="center">
  <img src="https://github.com/rubixkube-io/docs/blob/d11202b7fb45fdcf1551c7c11a25c9a67e2dcbd2/images/hero-dark.png" alt="RubixKube Logo" width="400"/>
</p>

**RubixKube™**is the**Reliability Layer for the AI Era**.
An AI-native mesh of agents that keeps your infrastructure alive, safe, and self-healing.

> Think of it as**a second brain for your infra**— one that never sleeps, never forgets, and always protects your uptime.

---

##  About These Docs

This repository powers the**RubixKube Documentation Hub**(built with [Mintlify](https://mintlify.com)).

Here you’ll find everything you need to:

***Get started quickly**with RubixKube
*  Learn core**concepts**: SRI (Site Reliability Intelligence), Agent Mesh, Memory Graph
*  Explore**integrations**with Kubernetes, GitOps, observability, and cloud-native stacks
*  Dive into the**API & CLI references***Troubleshoot and optimize your deployments

---

##  Quickstart

Get RubixKube running in minutes.

```bash
# 1. Install RubixKube CLI
curl -sSL <replace-install-script-url> | bash

# 2. Connect to your cluster
rubixkube connect --cluster <your-cluster-name>

# 3. Start observing
rubixkube start
```

 [Full Quickstart Guide](replace-docs-quickstart-url)

---

##  Documentation Structure

***[Quickstart](replace-docs-quickstart-url)**– Install and run RubixKube in minutes
***[Concepts](replace-docs-concepts-url)**– SRI, Agent Mesh, Memory Engine, Guardrails
***[Integrations](replace-docs-integrations-url)**– Kubernetes, CI/CD, Observability, GitOps
***[API Reference](replace-docs-api-url)**– REST + CLI commands
***[Troubleshooting](replace-docs-troubleshooting-url)**– Common issues and fixes

---

##  Local Development

We use the [Mintlify CLI](https://www.npmjs.com/package/mint) for previewing docs locally.

Install the CLI:

```bash
npm i -g mint
```

Run docs in dev mode (from the repo root, where `docs.json` lives):

```bash
mint dev
```

Preview at  `http://localhost:3000`

---

##  Publishing Changes

Docs are deployed automatically when changes are merged into the default branch.
Connect the [Mintlify GitHub app](https://dashboard.mintlify.com/settings/organization/github-app) to sync updates.

---

##  Troubleshooting

### *Dev server not starting?
  ```bash
  mint update
  ```

  (Updates the CLI to latest version.)

***Seeing a 404 page?**Ensure you’re in the correct directory and have a valid `docs.json`.

---

##  Resources

*  [Website](https://rubixkube.ai)
*  [Docs Portal](replace-docs-portal-url)
*  [Blog](https://rubixkube.ai/blog)
*  [Community Slack/Discord](replace-community-url)
*  [X/Twitter](https://twitter.com/RubixKubeHQ)
*  [LinkedIn](https://linkedin.com/company/rubixkube)

---

##  Contributing

We welcome feedback and contributions!
Check out the [Contributing Guide](replace-contributing-url) before submitting issues or PRs.

---

##  License

This project is licensed under the [MIT License](replace-license-url).

---

##  Join the Movement

RubixKube isn’t just another DevOps tool.
It’s the**seatbelt, backup generator, and peace-of-mind layer**for modern infrastructure.

If your infra breaks, your**revenue breaks**.
RubixKube exists to make sure that never happens.

---
