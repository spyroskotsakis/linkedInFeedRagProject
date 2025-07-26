# Reproducible builds | Docker Docs

**URL:** https://docs.docker.com/build/ci/github-actions/reproducible-builds/
**Word Count:** 1134
**Links Count:** 647
**Scraped:** 2025-07-16 01:54:11
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Reproducible builds with GitHub Actions

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

`SOURCE_DATE_EPOCH` is a [standardized environment variable](https://reproducible-builds.org/docs/source-date-epoch/) for instructing build tools to produce a reproducible output. Setting the environment variable for a build makes the timestamps in the image index, config, and file metadata reflect the specified Unix time.

To set the environment variable in GitHub Actions, use the built-in `env` property on the build step.

## Unix epoch timestamps

The following example sets the `SOURCE_DATE_EPOCH` variable to 0, Unix epoch.

`docker/build-push-action` `docker/bake-action`               name: ci          on:       push:          jobs:       docker:         runs-on: ubuntu-latest         steps:           - name: Set up Docker Buildx             uses: docker/setup-buildx-action@v3                - name: Build             uses: docker/build-push-action@v6             with:               tags: user/app:latest             env:               SOURCE_DATE_EPOCH: 0               name: ci          on:       push:          jobs:       docker:         runs-on: ubuntu-latest         steps:           - name: Set up Docker Buildx             uses: docker/setup-buildx-action@v3                - name: Build             uses: docker/bake-action@v6             env:               SOURCE_DATE_EPOCH: 0

## Git commit timestamps

The following example sets `SOURCE_DATE_EPOCH` to the Git commit timestamp.

`docker/build-push-action` `docker/bake-action`               name: ci          on:       push:          jobs:       docker:         runs-on: ubuntu-latest         steps:           - name: Set up Docker Buildx             uses: docker/setup-buildx-action@v3                - name: Get Git commit timestamps             run: echo "TIMESTAMP=$(git log -1 --pretty=%ct)" >> $GITHUB_ENV                - name: Build             uses: docker/build-push-action@v6             with:               tags: user/app:latest             env:               SOURCE_DATE_EPOCH: ${{ env.TIMESTAMP }}               name: ci          on:       push:          jobs:       docker:         runs-on: ubuntu-latest         steps:           - name: Set up Docker Buildx             uses: docker/setup-buildx-action@v3                - name: Get Git commit timestamps             run: echo "TIMESTAMP=$(git log -1 --pretty=%ct)" >> $GITHUB_ENV                - name: Build             uses: docker/bake-action@v6             env:               SOURCE_DATE_EPOCH: ${{ env.TIMESTAMP }}

## Additional information

For more information about the `SOURCE_DATE_EPOCH` support in BuildKit, see [BuildKit documentation](https://github.com/moby/buildkit/blob/master/docs/build-repro.md#source_date_epoch).