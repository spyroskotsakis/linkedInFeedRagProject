# CopyIgnoredFile | Docker Docs

**URL:** https://docs.docker.com/reference/build-checks/copy-ignored-file
**Word Count:** 840
**Links Count:** 484
**Scraped:** 2025-07-16 01:56:56
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# CopyIgnoredFile

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

> Note >  > This check is experimental and is not enabled by default. To enable it, see [Experimental checks](https://docs.docker.com/go/build-checks-experimental/).

## Output               Attempting to Copy file "./tmp/Dockerfile" that is excluded by .dockerignore

## Description

When you use the Add or Copy instructions from within a Dockerfile, you should ensure that the files to be copied into the image do not match a pattern present in `.dockerignore`.

Files which match the patterns in a `.dockerignore` file are not present in the context of the image when it is built. Trying to copy or add a file which is missing from the context will result in a build error.

## Examples

With the given `.dockerignore` file:               */tmp/*

â Bad: Attempting to Copy file "./tmp/Dockerfile" that is excluded by .dockerignore               FROM scratch     COPY ./tmp/helloworld.txt /helloworld.txt

â Good: Copying a file which is not excluded by .dockerignore               FROM scratch     COPY ./forever/helloworld.txt /helloworld.txt