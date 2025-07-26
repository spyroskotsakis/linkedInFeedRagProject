# RedundantTargetPlatform | Docker Docs

**URL:** https://docs.docker.com/reference/build-checks/redundant-target-platform/
**Word Count:** 788
**Links Count:** 483
**Scraped:** 2025-07-16 01:54:11
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# RedundantTargetPlatform

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Output               Setting platform to predefined $TARGETPLATFORM in FROM is redundant as this is the default behavior

## Description

A custom platform can be used for a base image. The default platform is the same platform as the target output so setting the platform to `$TARGETPLATFORM` is redundant and unnecessary.

## Examples

â Bad: this usage of `--platform` is redundant since `$TARGETPLATFORM` is the default.               FROM --platform=$TARGETPLATFORM alpine AS builder     RUN apk add --no-cache git

â Good: omit the `--platform` argument.               FROM alpine AS builder     RUN apk add --no-cache git