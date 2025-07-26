# InvalidDefinitionDescription | Docker Docs

**URL:** https://docs.docker.com/reference/build-checks/invalid-definition-description/
**Word Count:** 899
**Links Count:** 487
**Scraped:** 2025-07-16 01:53:07
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# InvalidDefinitionDescription

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

> Note >  > This check is experimental and is not enabled by default. To enable it, see [Experimental checks](https://docs.docker.com/go/build-checks-experimental/).

## Output               Comment for build stage or argument should follow the format: `# <arg/stage name> <description>`. If this is not intended to be a description comment, add an empty line or comment between the instruction and the comment.

## Description

The [`--call=outline`](https://docs.docker.com/reference/cli/docker/buildx/build/#call-outline) and [`--call=targets`](https://docs.docker.com/reference/cli/docker/buildx/build/#call-outline) flags for the `docker build` command print descriptions for build targets and arguments. The descriptions are generated from [Dockerfile comments](https://docs.docker.com/reference/cli/docker/buildx/build/#descriptions) that immediately precede the `FROM` or `ARG` instruction and that begin with the name of the build stage or argument. For example:               # build-cli builds the CLI binary     FROM alpine AS build-cli     # VERSION controls the version of the program     ARG VERSION=1

In cases where preceding comments are not meant to be descriptions, add an empty line or comment between the instruction and the preceding comment.

## Examples

â Bad: A non-descriptive comment on the line preceding the `FROM` command.               # a non-descriptive comment     FROM scratch AS base          # another non-descriptive comment     ARG VERSION=1

â Good: An empty line separating non-descriptive comments.               # a non-descriptive comment          FROM scratch AS base          # another non-descriptive comment          ARG VERSION=1

â Good: Comments describing `ARG` keys and stages immediately proceeding the command.               # base is a stage for compiling source     FROM scratch AS base     # VERSION This is the version number.     ARG VERSION=1