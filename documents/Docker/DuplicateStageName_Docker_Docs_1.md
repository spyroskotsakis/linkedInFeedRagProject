# DuplicateStageName | Docker Docs

**URL:** https://docs.docker.com/reference/build-checks/duplicate-stage-name/
**Word Count:** 782
**Links Count:** 483
**Scraped:** 2025-07-16 01:52:23
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# DuplicateStageName

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Output               Duplicate stage name 'foo-base', stage names should be unique

## Description

Defining multiple stages with the same name results in an error because the builder is unable to uniquely resolve the stage name reference.

## Examples

â Bad: `builder` is declared as a stage name twice.               FROM debian:latest AS builder     RUN apt-get update; apt-get install -y curl          FROM golang:latest AS builder

â Good: stages have unique names.               FROM debian:latest AS deb-builder     RUN apt-get update; apt-get install -y curl          FROM golang:latest AS go-builder