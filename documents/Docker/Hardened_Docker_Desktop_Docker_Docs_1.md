# Hardened Docker Desktop | Docker Docs

**URL:** https://docs.docker.com/desktop/hardened-desktop
**Word Count:** 1349
**Links Count:** 643
**Scraped:** 2025-07-16 02:05:18
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Overview of Hardened Docker Desktop

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Subscription: Business

For: Administrators

Hardened Docker Desktop is a group of security features, designed to improve the security of developer environments with minimal impact on developer experience or productivity.

It lets you enforce strict security settings, preventing developers and their containers from bypassing these controls, either intentionally or unintentionally. Additionally, you can enhance container isolation, to mitigate potential security threats such as malicious payloads breaching the Docker Desktop Linux VM and the underlying host.

Hardened Docker Desktop moves the ownership boundary for Docker Desktop configuration to the organization, meaning that any security controls you set cannot be altered by the user of Docker Desktop.

It is for security conscious organizations who:

  * Donât give their users root or administrator access on their machines   * Would like Docker Desktop to be within their organizationâs centralized control   * Have certain compliance obligations

### How does it help my organization?

Hardened Desktop features work independently but collectively to create a defense-in-depth strategy, safeguarding developer workstations against potential attacks across various functional layers, such as configuring Docker Desktop, pulling container images, and running container images. This multi-layered defense approach ensures comprehensive security. It helps mitigate against threats such as:

  * Malware and supply chain attacks: Registry Access Management and Image Access Management prevent developers from accessing certain container registries and image types, significantly lowering the risk of malicious payloads. Additionally, Enhanced Container Isolation \(ECI\) restricts the impact of containers with malicious payloads by running them without root privileges inside a Linux user namespace.   * Lateral movement: Air-gapped containers lets you configure network access restrictions for containers, thereby preventing malicious containers from performing lateral movement within the organization's network.   * Insider threats: Settings Management configures and locks various Docker Desktop settings so you can enforce company policies and prevent developers from introducing insecure configurations, intentionally or unintentionally.

### [Settings ManagementLearn how Settings Management can secure your developers' workflows.](https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/)

### [Enhanced Container IsolationUnderstand how Enhanced Container Isolation can prevent container attacks.](https://docs.docker.com/enterprise/security/hardened-desktop/enhanced-container-isolation/)

### [Registry Access ManagementControl the registries developers can access while using Docker Desktop.](https://docs.docker.com/enterprise/security/hardened-desktop/registry-access-management/)

### [Image Access ManagementControl the images developers can pull from Docker Hub.](https://docs.docker.com/enterprise/security/hardened-desktop/image-access-management/)

### [Air-Gapped ContainersRestrict containers from accessing unwanted network resources.](https://docs.docker.com/enterprise/security/hardened-desktop/air-gapped-containers/)