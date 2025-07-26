# NoEmptyContinuation | Docker Docs

**URL:** https://docs.docker.com/reference/build-checks/no-empty-continuation/
**Word Count:** 817
**Links Count:** 483
**Scraped:** 2025-07-16 01:53:49
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# NoEmptyContinuation

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Output               Empty continuation line found in: RUN apk add     gnupg     curl

## Description

Support for empty continuation \(`/`\) lines have been deprecated and will generate errors in future versions of the Dockerfile syntax.

Empty continuation lines are empty lines following a newline escape:               FROM alpine     RUN apk add \              gnupg \              curl

Support for such empty lines is deprecated, and a future BuildKit release will remove support for this syntax entirely, causing builds to break. To avoid future errors, remove the empty lines, or add comments, since lines with comments aren't considered empty.

## Examples

â Bad: empty continuation line between `EXPOSE` and 80.               FROM alpine     EXPOSE \          80

â Good: comments do not count as empty lines.               FROM alpine     EXPOSE \     # Port     80