# Build cache invalidation | Docker Docs

**URL:** https://docs.docker.com/build/cache/invalidation/
**Word Count:** 1455
**Links Count:** 646
**Scraped:** 2025-07-16 01:49:39
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Build cache invalidation

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

When building an image, Docker steps through the instructions in your Dockerfile, executing each in the order specified. For each instruction, the [builder](https://docs.docker.com/build/builders/) checks whether it can reuse the instruction from the build cache.

## General rules

The basic rules of build cache invalidation are as follows:

  * The builder begins by checking if the base image is already cached. Each subsequent instruction is compared against the cached layers. If no cached layer matches the instruction exactly, the cache is invalidated.

  * In most cases, comparing the Dockerfile instruction with the corresponding cached layer is sufficient. However, some instructions require additional checks and explanations.

  * For the `ADD` and `COPY` instructions, and for `RUN` instructions with bind mounts \(`RUN --mount=type=bind`\), the builder calculates a cache checksum from file metadata to determine whether cache is valid. During cache lookup, cache is invalidated if the file metadata has changed for any of the files involved.

The modification time of a file \(`mtime`\) is not taken into account when calculating the cache checksum. If only the `mtime` of the copied files have changed, the cache is not invalidated.

  * Aside from the `ADD` and `COPY` commands, cache checking doesn't look at the files in the container to determine a cache match. For example, when processing a `RUN apt-get -y update` command the files updated in the container aren't examined to determine if a cache hit exists. In that case just the command string itself is used to find a match.

Once the cache is invalidated, all subsequent Dockerfile commands generate new images and the cache isn't used.

If your build contains several layers and you want to ensure the build cache is reusable, order the instructions from less frequently changed to more frequently changed where possible.

## RUN instructions

The cache for `RUN` instructions isn't invalidated automatically between builds. Suppose you have a step in your Dockerfile to install `curl`:               FROM alpine:3.21 AS install     RUN apk add curl

This doesn't mean that the version of `curl` in your image is always up-to-date. Rebuilding the image one week later will still get you the same packages as before. To force a re-execution of the `RUN` instruction, you can:

  * Make sure that a layer before it has changed   * Clear the build cache ahead of the build using [`docker builder prune`](https://docs.docker.com/reference/cli/docker/builder/prune/)   * Use the `--no-cache` or `--no-cache-filter` options

The `--no-cache-filter` option lets you specify a specific build stage to invalidate the cache for:               $ docker build --no-cache-filter install .     

## Build secrets

The contents of build secrets are not part of the build cache. Changing the value of a secret doesn't result in cache invalidation.

If you want to force cache invalidation after changing a secret value, you can pass a build argument with an arbitrary value that you also change when changing the secret. Build arguments do result in cache invalidation.               FROM alpine     ARG CACHEBUST     RUN --mount=type=secret,id=TOKEN,env=TOKEN \         some-command ...               $ TOKEN="tkn_pat123456" docker build --secret id=TOKEN --build-arg CACHEBUST=1 .     

Properties of secrets such as IDs and mount paths do participate in the cache checksum, and result in cache invalidation if changed.