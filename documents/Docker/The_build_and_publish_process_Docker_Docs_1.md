# The build and publish process | Docker Docs

**URL:** https://docs.docker.com/extensions/extensions-sdk/process/
**Word Count:** 1325
**Links Count:** 652
**Scraped:** 2025-07-16 01:46:47
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# The build and publish process

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

This documentation is structured so that it matches the steps you need to take when creating your extension.

There are two main parts to creating a Docker extension:

  1. Build the foundations   2. Publish the extension

> Note >  > You do not need to pay to create a Docker extension. The [Docker Extension SDK](https://www.npmjs.com/package/@docker/extension-api-client) is licensed under the Apache 2.0 License and is free to use. Anyone can create new extensions and share them without constraints. >  > There is also no constraint on how each extension should be licensed, this is up to you to decide when creating a new extension.

## Part one: Build the foundations

The build process consists of:

  * Installing the latest version of Docker Desktop.   * Setting up the directory with files, including the extensionâs source code and the required extension-specific files.   * Creating the `Dockerfile` to build, publish, and run your extension in Docker Desktop.   * Configuring the metadata file which is required at the root of the image filesystem.   * Building and installing the extension.

For further inspiration, see the other examples in the [samples folder](https://github.com/docker/extensions-sdk/tree/main/samples).

> Tip >  > Whilst creating your extension, make sure you follow the [design](https://docs.docker.com/extensions/extensions-sdk/design/design-guidelines/) and [UI styling](https://docs.docker.com/extensions/extensions-sdk/design/) guidelines to ensure visual consistency and [level AA accessibility standards](https://www.w3.org/WAI/WCAG2AA-Conformance).

## Part two: Publish and distribute your extension

Docker Desktop displays published extensions in the Extensions Marketplace. The Extensions Marketplace is a curated space where developers can discover extensions to improve their developer experience and upload their own extension to share with the world.

If you want your extension published in the Marketplace, read the [publish documentation](https://docs.docker.com/extensions/extensions-sdk/extensions/publish/).

> Already built an extension? >  > Let us know about your experience using the [feedback form](https://survey.alchemer.com/s3/7184948/Publishers-Feedback-Form).

## Whatâs next?

If you want to get up and running with creating a Docker Extension, see the [Quickstart guide](https://docs.docker.com/extensions/extensions-sdk/quickstart/).

Alternatively, get started with reading the "Part one: Build" section for more in-depth information about each step of the extension creation process.

For an in-depth tutorial of the entire build process, we recommend the following video walkthrough from DockerCon 2022.