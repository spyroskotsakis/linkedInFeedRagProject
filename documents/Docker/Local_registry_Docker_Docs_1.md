# Local registry | Docker Docs

**URL:** https://docs.docker.com/build/ci/github-actions/local-registry/
**Word Count:** 1036
**Links Count:** 637
**Scraped:** 2025-07-16 01:53:28
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Local registry with GitHub Actions

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

* * *

For testing purposes you may need to create a [local registry](https://hub.docker.com/_/registry) to push images into:               name: ci          on:       push:          jobs:       docker:         runs-on: ubuntu-latest         services:           registry:             image: registry:2             ports:               - 5000:5000         steps:           - name: Set up QEMU             uses: docker/setup-qemu-action@v3                      - name: Set up Docker Buildx             uses: docker/setup-buildx-action@v3             with:               driver-opts: network=host                      - name: Build and push to local registry             uses: docker/build-push-action@v6             with:               push: true               tags: localhost:5000/name/app:latest                      - name: Inspect             run: |               docker buildx imagetools inspect localhost:5000/name/app:latest