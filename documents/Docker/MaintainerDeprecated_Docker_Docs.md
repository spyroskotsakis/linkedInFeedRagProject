# MaintainerDeprecated | Docker Docs

**URL:** https://docs.docker.com/reference/build-checks/maintainer-deprecated
**Word Count:** 763
**Links Count:** 484
**Scraped:** 2025-07-16 01:56:34
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# MaintainerDeprecated

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Output               MAINTAINER instruction is deprecated in favor of using label

## Description

The `MAINTAINER` instruction, used historically for specifying the author of the Dockerfile, is deprecated. To set author metadata for an image, use the `org.opencontainers.image.authors` [OCI label](https://github.com/opencontainers/image-spec/blob/main/annotations.md#pre-defined-annotation-keys).

## Examples

â Bad: don't use the `MAINTAINER` instruction               MAINTAINER moby@example.com

â Good: specify the author using the `org.opencontainers.image.authors` label               LABEL org.opencontainers.image.authors="moby@example.com"