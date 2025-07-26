# Export to Docker | Docker Docs

**URL:** https://docs.docker.com/build/ci/github-actions/export-docker
**Word Count:** 1043
**Links Count:** 636
**Scraped:** 2025-07-16 01:59:28
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Export to Docker with GitHub Actions

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

* * *

You may want your build result to be available in the Docker client through `docker images` to be able to use it in another step of your workflow:               name: ci          on:       push:          jobs:       docker:         runs-on: ubuntu-latest         steps:           - name: Set up Docker Buildx             uses: docker/setup-buildx-action@v3                      - name: Build             uses: docker/build-push-action@v6             with:               load: true               tags: myimage:latest                      - name: Inspect             run: |               docker image inspect myimage:latest