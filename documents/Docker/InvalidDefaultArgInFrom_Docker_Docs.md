# InvalidDefaultArgInFrom | Docker Docs

**URL:** https://docs.docker.com/reference/build-checks/invalid-default-arg-in-from
**Word Count:** 809
**Links Count:** 483
**Scraped:** 2025-07-16 01:57:40
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# InvalidDefaultArgInFrom

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Output               Using the global ARGs with default values should produce a valid build.

## Description

An `ARG` used in an image reference should be valid when no build arguments are used. An image build should not require `--build-arg` to be used to produce a valid build.

## Examples

â Bad: don't rely on an ARG being set for an image reference to be valid               ARG TAG     FROM busybox:${TAG}

â Good: include a default for the ARG               ARG TAG=latest     FROM busybox:${TAG}

â Good: ARG can be empty if the image would be valid with it empty               ARG VARIANT     FROM busybox:stable${VARIANT}

â Good: Use a default value if the build arg is not present               ARG TAG     FROM alpine:${TAG:-3.14}