# Core concepts | Docker Docs

**URL:** http://docs.docker.com/dhi/core-concepts
**Word Count:** 1399
**Links Count:** 661
**Scraped:** 2025-07-16 02:08:04
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](http://docs.docker.com/get-started/)   * [Guides](http://docs.docker.com/guides/)   * [Reference](http://docs.docker.com/reference/)

* * *

# Core concepts

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Docker Hardened Images \(DHIs\) are built on a foundation of secure software supply chain practices. This section explains the core concepts behind that foundation, from signed attestations and immutable digests to standards like SLSA and VEX.

Start here if you want to understand how Docker Hardened Images support compliance, transparency, and security.

## Security metadata and attestations

### [AttestationsReview the full set of signed attestations included with each Docker Hardened Image, such as SBOMs, VEX, build provenance, and scan results.](http://docs.docker.com/dhi/core-concepts/attestations/)

### [Software Bill of Materials \(SBOMs\)Learn what SBOMs are, why they matter, and how Docker Hardened Images include signed SBOMs to support transparency and compliance.](http://docs.docker.com/dhi/core-concepts/sbom/)

### [Supply-chain Levels for Software Artifacts \(SLSA\)Learn how Docker Hardened Images comply with SLSA Build Level 3 and how to verify provenance for secure, tamper-resistant builds.](http://docs.docker.com/dhi/core-concepts/slsa/)

### [Image provenanceLearn how build provenance metadata helps trace the origin of Docker Hardened Images and support compliance with SLSA.](http://docs.docker.com/dhi/core-concepts/provenance/)

### [FIPSLearn how Docker Hardened Images support FIPS 140 by using validated cryptographic modules and providing signed attestations for compliance audits.](http://docs.docker.com/dhi/core-concepts/fips/)

## Vulnerability and risk management

### [Common Vulnerabilities and Exposures \(CVEs\)Understand what CVEs are, how Docker Hardened Images reduce exposure, and how to scan images for vulnerabilities using popular tools.](http://docs.docker.com/dhi/core-concepts/cves/)

### [Vulnerability Exploitability eXchange \(VEX\)Learn how VEX helps you prioritize real risks by identifying which vulnerabilities in Docker Hardened Images are actually exploitable.](http://docs.docker.com/dhi/core-concepts/vex/)

### [Software Supply Chain SecurityLearn how Docker Hardened Images help secure every stage of your software supply chain with signed metadata, provenance, and minimal attack surface.](http://docs.docker.com/dhi/core-concepts/sscs/)

### [Secure Software Development Lifecycle \(SSDLC\)See how Docker Hardened Images support a secure SDLC by integrating with scanning, signing, and debugging tools.](http://docs.docker.com/dhi/core-concepts/ssdlc/)

## Image structure and behavior

### [Distroless imagesLearn how Docker Hardened Images use distroless variants to minimize attack surface and remove unnecessary components.](http://docs.docker.com/dhi/core-concepts/distroless/)

### [glibc and musl support in Docker Hardened ImagesCompare glibc and musl variants of DHIs to choose the right base image for your applicationâs compatibility, size, and performance needs.](http://docs.docker.com/dhi/core-concepts/glibc-musl/)

### [Image immutabilityUnderstand how image digests, read-only containers, and signed metadata ensure Docker Hardened Images are tamper-resistant and immutable.](http://docs.docker.com/dhi/core-concepts/immutability/)

### [Image hardeningLearn how Docker Hardened Images are designed for security, with minimal components, nonroot execution, and secure-by-default configurations.](http://docs.docker.com/dhi/core-concepts/hardening/)

## Verification and traceability

### [DigestsLearn how to use immutable image digests to guarantee consistency and verify the exact Docker Hardened Image you're running.](http://docs.docker.com/dhi/core-concepts/digests/)

### [Code signingUnderstand how Docker Hardened Images are cryptographically signed using Cosign to verify authenticity, integrity, and secure provenance.](http://docs.docker.com/dhi/core-concepts/signatures/)