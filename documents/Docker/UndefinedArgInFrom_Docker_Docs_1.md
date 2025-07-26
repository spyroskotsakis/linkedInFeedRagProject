# UndefinedArgInFrom | Docker Docs

**URL:** https://docs.docker.com/reference/build-checks/undefined-arg-in-from/
**Word Count:** 829
**Links Count:** 483
**Scraped:** 2025-07-16 01:54:28
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# UndefinedArgInFrom

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Output               FROM argument 'VARIANT' is not declared

## Description

This rule warns for cases where you're consuming an undefined build argument in `FROM` instructions.

Interpolating build arguments in `FROM` instructions can be a good way to add flexibility to your build, and lets you pass arguments that overriding the base image of a stage. For example, you might use a build argument to specify the image tag:               ARG ALPINE_VERSION=3.20          FROM alpine:${ALPINE_VERSION}

This makes it possible to run the build with a different `alpine` version by specifying a build argument:               $ docker buildx build --build-arg ALPINE_VERSION=edge .     

This check also tries to detect and warn when a `FROM` instruction reference miss-spelled built-in build arguments, like `BUILDPLATFORM`.

## Examples

â Bad: the `VARIANT` build argument is undefined.               FROM node:22${VARIANT} AS jsbuilder

â Good: the `VARIANT` build argument is defined.               ARG VARIANT="-alpine3.20"     FROM node:22${VARIANT} AS jsbuilder