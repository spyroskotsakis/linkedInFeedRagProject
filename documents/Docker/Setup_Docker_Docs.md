# Setup | Docker Docs

**URL:** https://docs.docker.com/build-cloud/setup
**Word Count:** 1344
**Links Count:** 657
**Scraped:** 2025-07-16 02:00:53
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Docker Build Cloud setup

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Before you can start using Docker Build Cloud, you must add the builder to your local environment.

## Prerequisites

To get started with Docker Build Cloud, you need to:

  * Download and install Docker Desktop version 4.26.0 or later.   * Create a cloud builder on the [Docker Build Cloud Dashboard](https://app.docker.com/build/).     * When you create the builder, choose a name for it \(for example, `default`\). You will use this name as `BUILDER_NAME` in the CLI steps below.

### Use Docker Build Cloud without Docker Desktop

To use Docker Build Cloud without Docker Desktop, you must download and install a version of Buildx with support for Docker Build Cloud \(the `cloud` driver\). You can find compatible Buildx binaries on the releases page of [this repository](https://github.com/docker/buildx-desktop).

If you plan on building with Docker Build Cloud using the `docker compose build` command, you also need a version of Docker Compose that supports Docker Build Cloud. You can find compatible Docker Compose binaries on the releases page of [this repository](https://github.com/docker/compose-desktop).

## Steps

You can add a cloud builder using the CLI, with the `docker buildx create` command, or using the Docker Desktop settings GUI.

CLI  Docker Desktop

  1. Sign in to your Docker account.                    $ docker login          

  2. Add the cloud builder endpoint.                    $ docker buildx create --driver cloud <ORG>/<BUILDER_NAME>          

Replace `<ORG>` with the Docker Hub namespace of your Docker organization \(or your username if you are using a personal account\), and `<BUILDER_NAME>` with the name you chose when creating the builder in the dashboard.

This creates a local instance of the cloud builder named `cloud-ORG-BUILDER_NAME`.

> Note >  > If your organization is `acme` and you named your builder `default`, use: >           >          $ docker buildx create --driver cloud acme/default >          

  1. Sign in to your Docker account using the **Sign in** button in Docker Desktop.

  2. Open the Docker Desktop settings and navigate to the **Builders** tab.

  3. Under **Available builders** , select **Connect to builder**.

The builder has native support for the `linux/amd64` and `linux/arm64` architectures. This gives you a high-performance build cluster for building multi-platform images natively.

## Firewall configuration

To use Docker Build Cloud behind a firewall, ensure that your firewall allows traffic to the following addresses:

  * 3.211.38.21   * <https://auth.docker.io>   * <https://build-cloud.docker.com>   * <https://hub.docker.com>

## What's next

  * See [Building with Docker Build Cloud](https://docs.docker.com/build-cloud/usage/) for examples on how to use Docker Build Cloud.   * See [Use Docker Build Cloud in CI](https://docs.docker.com/build-cloud/ci/) for examples on how to use Docker Build Cloud with CI systems.