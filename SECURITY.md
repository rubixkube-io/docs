# Security Policy

At RubixKube, we take security seriously. We appreciate the efforts of security researchers and community members who help us keep the platform safe.

## Reporting security vulnerabilities

**Please do not report security vulnerabilities through public GitHub issues, discussions, or pull requests.**

Instead, report them directly to our security team using one of these methods:

- **Email**: [security@rubixkube.ai](mailto:security@rubixkube.ai)
- **GitHub**: use [private vulnerability reporting](https://github.com/rubixkube-io/community/security/advisories/new)

## What to include in your report

To help us investigate and respond quickly, please include the following.

### Required information

- **Vulnerability type**: for example XSS, SQL injection, authentication bypass
- **Affected component**: for example API, console, observer
- **Severity assessment**: Critical, High, Medium or Low
- **Affected versions**: which versions of RubixKube are impacted

### Technical details

- **Steps to reproduce**: clear, step-by-step instructions
- **Proof of concept**: code or commands that demonstrate the issue
- **Expected and actual behavior**: what should happen and what happens
- **Environment details**: OS, Kubernetes version, observer version

### Supporting evidence

- **Screenshots**: if helpful
- **Error messages**: full error logs and stack traces
- **Network traffic**: relevant HTTP requests and responses
- **Configuration**: any special configuration that matters

## Our response process

- We acknowledge your report and give you a point of contact for follow-up questions.
- We investigate, and reach out if we need more detail.
- We keep you updated on progress and tell you when the vulnerability is fixed.
- We can credit you in our acknowledgments, with your permission.

## Vulnerability disclosure policy

### Responsible disclosure

We believe in **responsible disclosure** and ask that you:

1. **Do not exploit** the vulnerability for malicious purposes
2. **Do not disclose** the vulnerability publicly until we have addressed it
3. **Give us reasonable time** to investigate and fix the issue
4. **Test on non-production systems** only

### Public disclosure

We coordinate public disclosure with you. Security fixes are released as part of our regular update cycle.

### Safe harbor

We consider security research conducted in accordance with this policy to be:

- **Authorized** in accordance with the Computer Fraud and Abuse Act (CFAA)
- **Exempt** from our Terms of Service prohibition against reverse engineering
- **Protected** under our commitment not to pursue legal action

## Security considerations for users

### Best practices

- **Keep your observers updated** to the latest version
- **Use strong authentication** methods
- **Follow the principle of least privilege** for API keys and access tokens
- **Rotate credentials** regularly
- **Monitor your deployments** for unusual activity
- **Review the observer manifest** before you apply it, and trim what you don't want

### Security features

- **Modes**: Observe reads. Assist asks on every write. Auto writes without asking and asks on destructive actions.
- **Traffic**: browser and API traffic uses HTTPS. The observer's connection to `nats.rubixkube.ai:4222` is an authenticated connection, outbound only.
- **Access controls**: each member is an admin or a user. Each record belongs to one organization, and each request is scoped to it.
- **Activity log**: Rubix's tool calls are recorded in **Settings > Activity**.
- **Observer permissions**: the Kubernetes observer's `ClusterRole` can read Secrets, create `pods/exec`, and create and patch events. Its built-in tools only read. On a machine, the observer runs as root.
- **Data region**: Google Cloud `us-central1`.

[Safety and control](https://docs.rubixkube.ai/concepts/guardrails) has the details.

## Vulnerability severity guidelines

We use these guidelines to prioritize security issues:

| Severity | Description | Examples |
|----------|-------------|----------|
| **Critical** | Remote code execution, complete data breach, full system compromise | RCE, SQL injection leading to data exfiltration |
| **High** | Significant data exposure, privilege escalation, authentication bypass | Token theft, unauthorized data access |
| **Medium** | Limited data exposure, denial of service, information disclosure | DoS affecting single user, limited info leak |
| **Low** | Minor issues, best practice violations, cosmetic problems | Missing security headers, typos in security docs |

## Scope

This security policy applies to:

- **RubixKube platform**: core application and services
- **Observers**: the software you install in your environment
- **Documentation**: security-related documentation issues
- **Infrastructure**: cloud infrastructure and deployment configurations
- **Dependencies**: third-party libraries and dependencies we maintain

**Out of scope:**

- Issues in third-party services (report to the vendor)
- Social engineering or physical security
- Distributed denial of service (DDoS) attacks

## Additional resources

- **[Safety and control](https://docs.rubixkube.ai/concepts/guardrails)**: what RubixKube can reach, change and record
- **Security questions and certifications**: [security@rubixkube.ai](mailto:security@rubixkube.ai)

## Policy updates

This policy is updated from time to time. The latest version is always at [rubixkube-io/docs/SECURITY.md](https://github.com/rubixkube-io/docs/blob/main/SECURITY.md).

---

**Thank you for helping keep RubixKube and our community safe.**
