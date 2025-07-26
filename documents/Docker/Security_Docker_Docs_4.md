# Security | Docker Docs

**URL:** https://docs.docker.com/extensions/extensions-sdk/architecture/security
**Word Count:** 1149
**Links Count:** 639
**Scraped:** 2025-07-16 01:59:28
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Extension security

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Extension capabilities

An extension can have the following optional parts:

  * A user interface in HTML or JavaScript, displayed in Docker Desktop Dashboard   * A backend part that runs as a container   * Executables deployed on the host machine.

Extensions are executed with the same permissions as the Docker Desktop user. Extension capabilities include running any Docker commands \(including running containers and mounting folders\), running extension binaries, and accessing files on your machine that are accessible by the user running Docker Desktop.

The Extensions SDK provides a set of JavaScript APIs to invoke commands or invoke these binaries from the extension UI code. Extensions can also provide a backend part that starts a long-lived running container in the background.

> Important >  > Make sure you trust the publisher or author of the extension when you install it, as the extension has the same access rights as the user running Docker Desktop.