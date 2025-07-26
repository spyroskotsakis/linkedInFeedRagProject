# Extensions SDK | Docker Docs

**URL:** https://docs.docker.com/extensions/extensions-sdk
**Word Count:** 1194
**Links Count:** 643
**Scraped:** 2025-07-16 02:03:17
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Overview of the Extensions SDK

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

* * *

The resources in this section help you create your own Docker extension.

The Docker CLI tool provides a set of commands to help you build and publish your extension, packaged as a specially formatted Docker image.

At the root of the image filesystem is a `metadata.json` file which describes the content of the extension. It's a fundamental element of a Docker extension.

An extension can contain a UI part and backend parts that run either on the host or in the Desktop virtual machine. For further information, see [Architecture](https://docs.docker.com/extensions/extensions-sdk/architecture/).

You distribute extensions through Docker Hub. However, you can develop them locally without the need to push the extension to Docker Hub. See [Extensions distribution](https://docs.docker.com/extensions/extensions-sdk/extensions/DISTRIBUTION/) for further details.

> Already built an extension? >  > Let us know about your experience using the [feedback form](https://survey.alchemer.com/s3/7184948/Publishers-Feedback-Form).

### [The build and publish processUnderstand the process for building and publishing an extension.](https://docs.docker.com/extensions/extensions-sdk/process/)

### [Quickstart guideFollow the quickstart guide to create a basic Docker extension quickly.](https://docs.docker.com/extensions/extensions-sdk/quickstart/)

### [View the design guidelinesEnsure your extension aligns to Docker's design guidelines and principles.](https://docs.docker.com/extensions/extensions-sdk/design/design-guidelines/)

### [Publish your extensionUnderstand how to publish your extension to the Marketplace.](https://docs.docker.com/extensions/extensions-sdk/extensions/)

### [Interacting with KubernetesFind information on how to interact indirectly with a Kubernetes cluster from your Docker extension.](https://docs.docker.com/extensions/extensions-sdk/guides/kubernetes/)

### [Multi-arch extensionsBuild your extension for multiple architectures.](https://docs.docker.com/extensions/extensions-sdk/extensions/multi-arch/)