# UndefinedVar | Docker Docs

**URL:** https://docs.docker.com/reference/build-checks/undefined-var
**Word Count:** 854
**Links Count:** 484
**Scraped:** 2025-07-16 01:56:12
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# UndefinedVar

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Output               Usage of undefined variable '$foo'

## Description

This check ensures that environment variables and build arguments are correctly declared before being used. While undeclared variables might not cause an immediate build failure, they can lead to unexpected behavior or errors later in the build process.

This check does not evaluate undefined variables for `RUN`, `CMD`, and `ENTRYPOINT` instructions where you use the [shell form](https://docs.docker.com/reference/dockerfile/#shell-form). That's because when you use shell form, variables are resolved by the command shell.

It also detects common mistakes like typos in variable names. For example, in the following Dockerfile:               FROM alpine     ENV PATH=$PAHT:/app/bin

The check identifies that `$PAHT` is undefined and likely a typo for `$PATH`:               Usage of undefined variable '$PAHT' (did you mean $PATH?)

## Examples

â Bad: `$foo` is an undefined build argument.               FROM alpine AS base     COPY $foo .

â Good: declaring `foo` as a build argument before attempting to access it.               FROM alpine AS base     ARG foo     COPY $foo .

â Bad: `$foo` is undefined.               FROM alpine AS base     ARG VERSION=$foo

â Good: the base image defines `$PYTHON_VERSION`               FROM python AS base     ARG VERSION=$PYTHON_VERSION