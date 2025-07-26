# SBOMs | Docker Docs

**URL:** https://docs.docker.com/dhi/core-concepts/sbom
**Word Count:** 1463
**Links Count:** 654
**Scraped:** 2025-07-16 02:00:53
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Software Bill of Materials \(SBOMs\)

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## What is an SBOM?

An SBOM is a detailed inventory that lists all components, libraries, and dependencies used in building a software application. It provides transparency into the software supply chain by documenting each component's version, origin, and relationship to other components. Think of it as a "recipe" for your software, detailing every ingredient and how they come together.

Metadata included in an SBOM for describing software artifacts may include:

  * Name of the artifact   * Version   * License type   * Authors   * Unique package identifier

## Why are SBOMs important?

In today's software landscape, applications often comprise numerous components from various sources, including open-source libraries, third-party services, and proprietary code. This complexity can obscure visibility into potential vulnerabilities and complicate compliance efforts. SBOMs address these challenges by providing a detailed inventory of all components within an application.

The significance of SBOMs is underscored by several key factors:

  * Enhanced transparency: SBOMs offer a comprehensive view of all components that constitute an application, enabling organizations to identify and assess risks associated with third-party libraries and dependencies.

  * Proactive vulnerability management: By maintaining an up-to-date SBOM, organizations can swiftly identify and address vulnerabilities in software components, reducing the window of exposure to potential exploits.

  * Regulatory compliance: Many regulations and industry standards now require organizations to maintain control over the software components they use. An SBOM facilitates compliance by providing a clear and accessible record.

  * Improved incident response: In the event of a security breach, an SBOM enables organizations to quickly identify affected components and take appropriate action, minimizing potential damage.

## Docker Hardened Image SBOMs

Docker Hardened Images come with built-in SBOMs, ensuring that every component in the image is documented and verifiable. These SBOMs are cryptographically signed, providing a tamper-evident record of the image's contents. This integration simplifies audits and enhances trust in the software supply chain.

## View SBOMs in Docker Hardened Images

To view the SBOM of a Docker Hardened Image, you can use the `docker scout sbom` command. Replace `<image-name>:<tag>` with the image name and tag.               $ docker scout sbom <image-name>:<tag>     

## Verify the SBOM of a Docker Hardened Image

Since Docker Hardened Images come with signed SBOMs, you can use Docker Scout to verify the authenticity and integrity of the SBOM attached to the image. This ensures that the SBOM has not been tampered with and that the image's contents are trustworthy.

To verify the SBOM of a Docker Hardened Image using Docker Scout, use the following command:               $ docker scout attest get <image-name>:<tag> \        --predicate-type https://scout.docker.com/sbom/v0.1 --verify --platform <platform>     

For example, to verify the SBOM attestation for the `dhi/node:20.19-debian12-fips-20250701182639` image:               $ docker scout attest get docs/dhi-node:20.19-debian12-fips-20250701182639 \        --predicate-type https://scout.docker.com/sbom/v0.1 --verify --platform linux/amd64     

## Resources

For more details about SBOM attestations and Docker Build, see [SBOM attestations](https://docs.docker.com/build/metadata/attestations/sbom/).