# How-tos | Docker Docs

**URL:** http://docs.docker.com/dhi/how-to
**Word Count:** 1328
**Links Count:** 648
**Scraped:** 2025-07-16 02:08:04
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](http://docs.docker.com/get-started/)   * [Guides](http://docs.docker.com/guides/)   * [Reference](http://docs.docker.com/reference/)

* * *

# How-tos

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

This section provides practical, step-by-step guidance for working with Docker Hardened Images \(DHIs\). Whether you're evaluating DHIs for the first time or integrating them into a production CI/CD pipeline, these topics walk you through each phase of the adoption journey, from discovery to debugging.

To help you get started and stay secure, the topics are organized around the typical lifecycle of working with DHIs.

## Lifecycle flow

  1. Explore available images and metadata in the DHI catalog.   2. Mirror trusted images into your namespace or registry.   3. Adopt DHIs in your workflows by pulling, using in development and CI, and migrating existing applications to use secure, minimal base images.   4. Analyze images by verifying signatures, SBOMs, and provenance, and scanning for vulnerabilities.   5. Enforce policies to maintain security and compliance.   6. Debug containers based on DHIs without modifying the image.

Each of the following topics aligns with a step in this lifecycle, so you can progress confidently through exploration, implementation, and ongoing maintenance.

## Step-by-step topics

### [Explore Docker Hardened ImagesLearn how to find and evaluate image repositories, variants, metadata, and attestations in the DHI catalog on Docker Hub.](http://docs.docker.com/dhi/how-to/explore/)

### [Mirror a Docker Hardened Image repositoryLearn how to mirror an image into your organization's namespace and optionally push it to another private registry.](http://docs.docker.com/dhi/how-to/mirror/)

### [Use a Docker Hardened ImageLearn how to pull, run, and reference Docker Hardened Images in Dockerfiles, CI pipelines, and standard development workflows.](http://docs.docker.com/dhi/how-to/use/)

### [Migrate an existing application to use Docker Hardened ImagesFollow a step-by-step guide to update your Dockerfiles and adopt Docker Hardened Images for secure, minimal, and production-ready builds.](http://docs.docker.com/dhi/how-to/migrate/)

### [Verify a Docker Hardened ImageUse Docker Scout or cosign to verify signed attestations like SBOMs, provenance, and vulnerability data for Docker Hardened Images.](http://docs.docker.com/dhi/how-to/verify/)

### [Scan a Docker Hardened ImageLearn how to scan Docker Hardened Images for known vulnerabilities using Docker Scout, Grype, or Trivy.](http://docs.docker.com/dhi/how-to/scan/)

### [Enforce Docker Hardened Image usage with policiesLearn how to use image policies with Docker Scout for Docker Hardened Images.](http://docs.docker.com/dhi/how-to/policies/)

### [Debug a Docker Hardened ImageUse Docker Debug to inspect a running container based on a hardened image without modifying it.](http://docs.docker.com/dhi/how-to/debug/)