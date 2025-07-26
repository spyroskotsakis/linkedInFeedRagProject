# Named contexts | Docker Docs

**URL:** https://docs.docker.com/build/ci/github-actions/named-contexts/
**Word Count:** 1197
**Links Count:** 649
**Scraped:** 2025-07-16 01:53:49
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Named contexts with GitHub Actions

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

You can define [additional build contexts](https://docs.docker.com/reference/cli/docker/buildx/build/#build-context), and access them in your Dockerfile with `FROM name` or `--from=name`. When Dockerfile defines a stage with the same name it's overwritten.

This can be useful with GitHub Actions to reuse results from other builds or pin an image to a specific tag in your workflow.

## Pin image to a tag

Replace `alpine:latest` with a pinned one:               # syntax=docker/dockerfile:1     FROM alpine     RUN echo "Hello World"               name: ci          on:       push:          jobs:       docker:         runs-on: ubuntu-latest         steps:           - name: Set up Docker Buildx             uses: docker/setup-buildx-action@v3                - name: Build             uses: docker/build-push-action@v6             with:               build-contexts: |                 alpine=docker-image://alpine:3.21               tags: myimage:latest

## Use image in subsequent steps

By default, the [Docker Setup Buildx](https://github.com/marketplace/actions/docker-setup-buildx) action uses `docker-container` as a build driver, so built Docker images aren't loaded automatically.

With named contexts you can reuse the built image:               # syntax=docker/dockerfile:1     FROM alpine     RUN echo "Hello World"               name: ci          on:       push:          jobs:       docker:         runs-on: ubuntu-latest         steps:           - name: Set up Docker Buildx             uses: docker/setup-buildx-action@v3             with:               driver: docker                - name: Build base image             uses: docker/build-push-action@v6             with:               context: "{{defaultContext}}:base"               load: true               tags: my-base-image:latest                - name: Build             uses: docker/build-push-action@v6             with:               build-contexts: |                 alpine=docker-image://my-base-image:latest               tags: myimage:latest

## Using with a container builder

As shown in the previous section we are not using the default [`docker-container` driver](https://docs.docker.com/build/builders/drivers/docker-container/) for building with named contexts. That's because this driver can't load an image from the Docker store as it's isolated. To solve this problem you can use a [local registry](https://docs.docker.com/build/ci/github-actions/local-registry/) to push your base image in your workflow:               # syntax=docker/dockerfile:1     FROM alpine     RUN echo "Hello World"               name: ci          on:       push:          jobs:       docker:         runs-on: ubuntu-latest         services:           registry:             image: registry:2             ports:               - 5000:5000         steps:           - name: Set up QEMU             uses: docker/setup-qemu-action@v3                - name: Set up Docker Buildx             uses: docker/setup-buildx-action@v3             with:               # network=host driver-opt needed to push to local registry               driver-opts: network=host                - name: Build base image             uses: docker/build-push-action@v6             with:               context: "{{defaultContext}}:base"               tags: localhost:5000/my-base-image:latest               push: true                - name: Build             uses: docker/build-push-action@v6             with:               build-contexts: |                 alpine=docker-image://localhost:5000/my-base-image:latest               tags: myimage:latest