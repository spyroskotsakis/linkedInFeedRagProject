# LegacyKeyValueFormat | Docker Docs

**URL:** https://docs.docker.com/reference/build-checks/legacy-key-value-format
**Word Count:** 841
**Links Count:** 483
**Scraped:** 2025-07-16 01:58:31
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# LegacyKeyValueFormat

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Output               "ENV key=value" should be used instead of legacy "ENV key value" format

## Description

The correct format for declaring environment variables and build arguments in a Dockerfile is `ENV key=value` and `ARG key=value`, where the variable name \(`key`\) and value \(`value`\) are separated by an equals sign \(`=`\). Historically, Dockerfiles have also supported a space separator between the key and the value \(for example, `ARG key value`\). This legacy format is deprecated, and you should only use the format with the equals sign.

## Examples

â Bad: using a space separator for variable key and value.               FROM alpine     ARG foo bar

â Good: use an equals sign to separate key and value.               FROM alpine     ARG foo=bar

â Bad: multi-line variable declaration with a space separator.               ENV DEPS \         curl \         git \         make

â Good: use an equals sign and wrap the value in quotes.               ENV DEPS="\         curl \         git \         make"