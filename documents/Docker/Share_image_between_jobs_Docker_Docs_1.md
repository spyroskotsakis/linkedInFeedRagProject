# Share image between jobs | Docker Docs

**URL:** https://docs.docker.com/build/ci/github-actions/share-image-jobs/
**Word Count:** 1070
**Links Count:** 641
**Scraped:** 2025-07-16 01:54:11
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Share built image between jobs with GitHub Actions

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

* * *

As each job is isolated in its own runner, you can't use your built image between jobs, except if you're using [self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/about-self-hosted-runners) or [Docker Build Cloud](https://docs.docker.com/build-cloud). However, you can [pass data between jobs](https://docs.github.com/en/actions/using-workflows/storing-workflow-data-as-artifacts#passing-data-between-jobs-in-a-workflow) in a workflow using the [actions/upload-artifact](https://github.com/actions/upload-artifact) and [actions/download-artifact](https://github.com/actions/download-artifact) actions:               name: ci          on:       push:          jobs:       build:         runs-on: ubuntu-latest         steps:           - name: Set up Docker Buildx             uses: docker/setup-buildx-action@v3                - name: Build and export             uses: docker/build-push-action@v6             with:               tags: myimage:latest               outputs: type=docker,dest=${{ runner.temp }}/myimage.tar                - name: Upload artifact             uses: actions/upload-artifact@v4             with:               name: myimage               path: ${{ runner.temp }}/myimage.tar            use:         runs-on: ubuntu-latest         needs: build         steps:           - name: Download artifact             uses: actions/download-artifact@v4             with:               name: myimage               path: ${{ runner.temp }}                - name: Load image             run: |               docker load --input ${{ runner.temp }}/myimage.tar               docker image ls -a