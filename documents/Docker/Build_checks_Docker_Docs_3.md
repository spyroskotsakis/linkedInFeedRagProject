# Build checks | Docker Docs

**URL:** https://docs.docker.com/build/ci/github-actions/checks
**Word Count:** 1129
**Links Count:** 643
**Scraped:** 2025-07-16 02:01:51
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Validating build configuration with GitHub Actions

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

[Build checks](https://docs.docker.com/build/checks/) let you validate your `docker build` configuration without actually running the build.

## Run checks with `docker/build-push-action`

To run build checks in a GitHub Actions workflow with the `build-push-action`, set the `call` input parameter to `check`. With this set, the workflow fails if any check warnings are detected for your build's configuration.               name: ci          on:       push:          jobs:       docker:         runs-on: ubuntu-latest         steps:           - name: Login to Docker Hub             uses: docker/login-action@v3             with:               username: ${{ secrets.DOCKERHUB_USERNAME }}               password: ${{ secrets.DOCKERHUB_TOKEN }}                      - name: Set up Docker Buildx             uses: docker/setup-buildx-action@v3                - name: Validate build configuration             uses: docker/build-push-action@v6             with:               call: check                - name: Build and push             uses: docker/build-push-action@v6             with:               push: true               tags: user/app:latest

## Run checks with `docker/bake-action`

If you're using Bake and `docker/bake-action` to run your builds, you don't need to specify any special inputs in your GitHub Actions workflow configuration. Instead, define a Bake target that calls the `check` method, and invoke that target in your CI.               target "build" {       dockerfile = "Dockerfile"       args = {         FOO = "bar"       }     }     target "validate-build" {       inherits = ["build"]       call = "check"     }               name: ci          on:       push:          env:       IMAGE_NAME: user/app          jobs:       docker:         runs-on: ubuntu-latest         steps:           - name: Login to Docker Hub             uses: docker/login-action@v3             with:               username: ${{ vars.DOCKERHUB_USERNAME }}               password: ${{ secrets.DOCKERHUB_TOKEN }}                - name: Set up Docker Buildx             uses: docker/setup-buildx-action@v3                - name: Validate build configuration             uses: docker/bake-action@v6             with:               targets: validate-build                - name: Build             uses: docker/bake-action@v6             with:               targets: build               push: true