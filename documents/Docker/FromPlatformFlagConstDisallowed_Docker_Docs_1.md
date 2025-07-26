# FromPlatformFlagConstDisallowed | Docker Docs

**URL:** https://docs.docker.com/reference/build-checks/from-platform-flag-const-disallowed/
**Word Count:** 853
**Links Count:** 483
**Scraped:** 2025-07-16 01:52:46
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# FromPlatformFlagConstDisallowed

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Output               FROM --platform flag should not use constant value "linux/amd64"

## Description

Specifying `--platform` in the Dockerfile `FROM` instruction forces the image to build on only one target platform. This prevents building a multi-platform image from this Dockerfile and you must build on the same platform as specified in `--platform`.

The recommended approach is to:

  * Omit `FROM --platform` in the Dockerfile and use the `--platform` argument on the command line.   * Use `$BUILDPLATFORM` or some other combination of variables for the `--platform` argument.   * Stage name should include the platform, OS, or architecture name to indicate that it only contains platform-specific instructions.

## Examples

â Bad: using a constant argument for `--platform`               FROM --platform=linux/amd64 alpine AS base     RUN apk add --no-cache git

â Good: using the default platform               FROM alpine AS base     RUN apk add --no-cache git

â Good: using a meta variable               FROM --platform=${BUILDPLATFORM} alpine AS base     RUN apk add --no-cache git

â Good: used in a multi-stage build with a target architecture               FROM --platform=linux/amd64 alpine AS build_amd64     ...          FROM --platform=linux/arm64 alpine AS build_arm64     ...          FROM build_${TARGETARCH} AS build     ...