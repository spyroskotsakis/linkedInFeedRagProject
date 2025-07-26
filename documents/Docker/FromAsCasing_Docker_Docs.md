# FromAsCasing | Docker Docs

**URL:** https://docs.docker.com/reference/build-checks/from-as-casing
**Word Count:** 782
**Links Count:** 487
**Scraped:** 2025-07-16 01:57:40
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# FromAsCasing

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Output               'as' and 'FROM' keywords' casing do not match

## Description

While Dockerfile keywords can be either uppercase or lowercase, mixing case styles is not recommended for readability. This rule reports violations where mixed case style occurs for a `FROM` instruction with an `AS` keyword declaring a stage name.

## Examples

â Bad: `FROM` is uppercase, `AS` is lowercase.               FROM debian:latest as builder

â Good: `FROM` and `AS` are both uppercase               FROM debian:latest AS deb-builder

â Good: `FROM` and `AS` are both lowercase.               from debian:latest as deb-builder

## Related errors

  * [`FileConsistentCommandCasing`](https://docs.docker.com/reference/build-checks/consistent-instruction-casing/)