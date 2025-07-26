# Update Docker Hub description | Docker Docs

**URL:** https://docs.docker.com/build/ci/github-actions/update-dockerhub-desc
**Word Count:** 1052
**Links Count:** 637
**Scraped:** 2025-07-16 02:03:45
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Update Docker Hub description with GitHub Actions

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

* * *

You can update the Docker Hub repository description using a third party action called [Docker Hub Description](https://github.com/peter-evans/dockerhub-description) with this action:               name: ci          on:       push:          jobs:       docker:         runs-on: ubuntu-latest         steps:           - name: Login to Docker Hub             uses: docker/login-action@v3             with:               username: ${{ vars.DOCKERHUB_USERNAME }}               password: ${{ secrets.DOCKERHUB_TOKEN }}                - name: Set up QEMU             uses: docker/setup-qemu-action@v3                - name: Set up Docker Buildx             uses: docker/setup-buildx-action@v3                - name: Build and push             uses: docker/build-push-action@v6             with:               push: true               tags: user/app:latest                - name: Update repo description             uses: peter-evans/dockerhub-description@e98e4d1628a5f3be2be7c231e50981aee98723ae # v4.0.0             with:               username: ${{ vars.DOCKERHUB_USERNAME }}               password: ${{ secrets.DOCKERHUB_TOKEN }}               repository: user/app