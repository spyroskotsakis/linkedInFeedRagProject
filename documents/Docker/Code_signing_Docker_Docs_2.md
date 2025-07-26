# Code signing | Docker Docs

**URL:** https://docs.docker.com/dhi/core-concepts/signatures/
**Word Count:** 1462
**Links Count:** 658
**Scraped:** 2025-07-16 01:49:59
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Code signing

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## What is code signing?

Code signing is the process of applying a cryptographic signature to software artifacts, such as Docker images, to verify their integrity and authenticity. By signing an image, you ensure that it has not been altered since it was signed and that it originates from a trusted source.

In the context of Docker Hardened Images \(DHIs\), code signing is achieved using [Cosign](https://docs.sigstore.dev/), a tool developed by the Sigstore project. Cosign enables secure and verifiable signing of container images, enhancing trust and security in the software supply chain.

## Why is code signing important?

Code signing plays a crucial role in modern software development and cybersecurity:

  * Authenticity: Verifies that the image was created by a trusted source.   * Integrity: Ensures that the image has not been tampered with since it was signed.   * Compliance: Helps meet regulatory and organizational security requirements.

## Docker Hardened Image code signing

Each DHI is cryptographically signed using Cosign, ensuring that the images have not been tampered with and originate from a trusted source.

## Why sign your own images?

Docker Hardened Images are signed by Docker to prove their origin and integrity, but if you're building application images that extend or use DHIs as a base, you should sign your own images as well.

By signing your own images, you can:

  * Prove the image was built by your team or pipeline   * Ensure your build hasn't been tampered with after it's pushed   * Support software supply chain frameworks like SLSA   * Enable image verification in deployment workflows

This is especially important in CI/CD environments where you build and push images frequently, or in any scenario where image provenance must be auditable.

## How to view and use code signatures

### View signatures

You can verify that a Docker Hardened Image is signed and trusted using either Docker Scout or Cosign.

To lists all attestations, including signature metadata, attached to the image, use the following command:               $ docker scout attest list <image-name>:<tag> --platform <platform>     

To verify a specific signed attestation \(e.g., SBOM, VEX, provenance\):               $ docker scout attest get \       --predicate-type <predicate-uri> \       --verify \       <image-name>:<tag> --platform <platform>     

For example:               $ docker scout attest get \       --predicate-type https://openvex.dev/ns/v0.2.0 \       --verify \       docs/dhi-python:3.13 --platform linux/amd64     

If valid, Docker Scout will confirm the signature and display signature payload, as well as the equivalent Cosign command to verify the image.

### Sign images

To sign a Docker image, use [Cosign](https://docs.sigstore.dev/). Replace `<image-name>:<tag>` with the image name and tag.               $ cosign sign <image-name>:<tag>     

This command will prompt you to authenticate via an OIDC provider \(such as GitHub, Google, or Microsoft\). Upon successful authentication, Cosign will generate a short-lived certificate and sign the image. The signature will be stored in a transparency log and associated with the image in the registry.