# MultipleInstructionsDisallowed | Docker Docs

**URL:** https://docs.docker.com/reference/build-checks/multiple-instructions-disallowed/
**Word Count:** 797
**Links Count:** 483
**Scraped:** 2025-07-16 01:53:49
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# MultipleInstructionsDisallowed

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Output               Multiple CMD instructions should not be used in the same stage because only the last one will be used

## Description

If you have multiple `CMD`, `HEALTHCHECK`, or `ENTRYPOINT` instructions in your Dockerfile, only the last occurrence is used. An image can only ever have one `CMD`, `HEALTHCHECK`, and `ENTRYPOINT`.

## Examples

â Bad: Duplicate instructions.               FROM alpine     ENTRYPOINT ["echo", "Hello, Norway!"]     ENTRYPOINT ["echo", "Hello, Sweden!"]     # Only "Hello, Sweden!" will be printed

â Good: only one `ENTRYPOINT` instruction.               FROM alpine     ENTRYPOINT ["echo", "Hello, Norway!\nHello, Sweden!"]

You can have both a regular, top-level `CMD` and a separate `CMD` for a `HEALTHCHECK` instruction.

â Good: only one top-level `CMD` instruction.               FROM python:alpine     RUN apk add curl     HEALTHCHECK --interval=1s --timeout=3s \       CMD ["curl", "-f", "http://localhost:8080"]     CMD ["python", "-m", "http.server", "8080"]