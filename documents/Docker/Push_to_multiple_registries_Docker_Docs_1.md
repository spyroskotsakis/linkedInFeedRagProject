# Push to multiple registries | Docker Docs

**URL:** https://docs.docker.com/build/ci/github-actions/push-multi-registries/
**Word Count:** 1055
**Links Count:** 636
**Scraped:** 2025-07-16 01:53:49
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Push to multiple registries with GitHub Actions

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

* * *

The following workflow will connect you to Docker Hub and GitHub Container Registry, and push the image to both registries:               name: ci          on:       push:          jobs:       docker:         runs-on: ubuntu-latest         steps:           - name: Login to Docker Hub             uses: docker/login-action@v3             with:               username: ${{ vars.DOCKERHUB_USERNAME }}               password: ${{ secrets.DOCKERHUB_TOKEN }}                - name: Login to GitHub Container Registry             uses: docker/login-action@v3             with:               registry: ghcr.io               username: ${{ github.repository_owner }}               password: ${{ secrets.GITHUB_TOKEN }}                - name: Set up QEMU             uses: docker/setup-qemu-action@v3                - name: Set up Docker Buildx             uses: docker/setup-buildx-action@v3                - name: Build and push             uses: docker/build-push-action@v6             with:               platforms: linux/amd64,linux/arm64               push: true               tags: |                 user/app:latest                 user/app:1.0.0                 ghcr.io/user/app:latest                 ghcr.io/user/app:1.0.0