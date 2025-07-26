# Test before push | Docker Docs

**URL:** https://docs.docker.com/build/ci/github-actions/test-before-push
**Word Count:** 1108
**Links Count:** 636
**Scraped:** 2025-07-16 02:03:17
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Test before push with GitHub Actions

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

* * *

In some cases, you might want to validate that the image works as expected before pushing it. The following workflow implements several steps to achieve this:

  1. Build and export the image to Docker   2. Test your image   3. Multi-platform build and push the image

              name: ci          on:       push:          env:       TEST_TAG: user/app:test       LATEST_TAG: user/app:latest          jobs:       docker:         runs-on: ubuntu-latest         steps:           - name: Login to Docker Hub             uses: docker/login-action@v3             with:               username: ${{ vars.DOCKERHUB_USERNAME }}               password: ${{ secrets.DOCKERHUB_TOKEN }}                - name: Set up QEMU             uses: docker/setup-qemu-action@v3                - name: Set up Docker Buildx             uses: docker/setup-buildx-action@v3                - name: Build and export to Docker             uses: docker/build-push-action@v6             with:               load: true               tags: ${{ env.TEST_TAG }}                - name: Test             run: |               docker run --rm ${{ env.TEST_TAG }}                - name: Build and push             uses: docker/build-push-action@v6             with:               platforms: linux/amd64,linux/arm64               push: true               tags: ${{ env.LATEST_TAG }}

> Note >  > The `linux/amd64` image is only built once in this workflow. The image is built once, and the following steps use the internal cache from the first `Build and push` step. The second `Build and push` step only builds `linux/arm64`.