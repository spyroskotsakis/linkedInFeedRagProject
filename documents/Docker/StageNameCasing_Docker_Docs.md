# StageNameCasing | Docker Docs

**URL:** https://docs.docker.com/reference/build-checks/stage-name-casing
**Word Count:** 771
**Links Count:** 483
**Scraped:** 2025-07-16 01:58:04
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# StageNameCasing

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Output               Stage name 'BuilderBase' should be lowercase

## Description

To help distinguish Dockerfile instruction keywords from identifiers, this rule forces names of stages in a multi-stage Dockerfile to be all lowercase.

## Examples

â Bad: mixing uppercase and lowercase characters in the stage name.               FROM alpine AS BuilderBase

â Good: stage name is all in lowercase.               FROM alpine AS builder-base