# Hardened, secure images | Docker Docs

**URL:** https://docs.docker.com/dhi/features/secure/
**Word Count:** 1244
**Links Count:** 644
**Scraped:** 2025-07-16 01:53:07
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Hardened, secure images

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Docker Hardened Images \(DHI\) are engineered to provide a robust security foundation for containerized applications, addressing the evolving challenges of software supply chain security.

## Near-zero vulnerabilities and non-root execution

Each DHI is meticulously built to eliminate known vulnerabilities, achieving near-zero Common Vulnerabilities and Exposures \(CVEs\) through continuous scanning and updates. By adhering to the principle of least privilege, DHI images run as non-root by default, reducing the risk of privilege escalation attacks in production environments.

## Comprehensive supply chain security

DHI incorporates multiple layers of security metadata to ensure transparency and trust:

  * SLSA Level 3 compliance: Each image includes detailed build provenance, meeting the standards set by the Supply-chain Levels for Software Artifacts \(SLSA\) framework.

  * Software Bill of Materials \(SBOMs\): Comprehensive SBOMs are provided, detailing all components within the image to facilitate vulnerability management and compliance audits.

  * Vulnerability Exploitability eXchange \(VEX\) statements: VEX documents accompany each image, providing context about known vulnerabilities and their exploitability status.

  * Cryptographic signing and attestations: All images and associated metadata are cryptographically signed, ensuring integrity and authenticity.

## Minimal and developer-friendly options

DHI provides both minimal and development-friendly image variants:

  * Minimal images: Built using a distroless approach, these images remove unnecessary components, reducing the attack surface by up to 95% and improving startup times.

  * Development images: Equipped with essential development tools and libraries, these images facilitate secure application building and testing.