# WorkdirRelativePath | Docker Docs

**URL:** https://docs.docker.com/reference/build-checks/workdir-relative-path/
**Word Count:** 882
**Links Count:** 483
**Scraped:** 2025-07-16 01:54:44
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# WorkdirRelativePath

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Output               Relative workdir 'app/src' can have unexpected results if the base image changes

## Description

When specifying `WORKDIR` in a build stage, you can use an absolute path, like `/build`, or a relative path, like `./build`. Using a relative path means that the working directory is relative to whatever the previous working directory was. So if your base image uses `/usr/local/foo` as a working directory, and you specify a relative directory like `WORKDIR build`, the effective working directory becomes `/usr/local/foo/build`.

The `WorkdirRelativePath` build rule warns you if you use a `WORKDIR` with a relative path without first specifying an absolute path in the same Dockerfile. The rationale for this rule is that using a relative working directory for base image built externally is prone to breaking, since working directory may change upstream without warning, resulting in a completely different directory hierarchy for your build.

## Examples

â Bad: this assumes that `WORKDIR` in the base image is `/` \(if that changes upstream, the `web` stage is broken\).               FROM nginx AS web     WORKDIR usr/share/nginx/html     COPY public .

â Good: a leading slash ensures that `WORKDIR` always ends up at the desired path.               FROM nginx AS web     WORKDIR /usr/share/nginx/html     COPY public .