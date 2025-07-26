# docker model install-runner | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/model/install-runner
**Word Count:** 788
**Links Count:** 479
**Scraped:** 2025-07-16 01:57:18
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker model install-runner

Description| Install Docker Model Runner \(Docker Engine only\)   ---|---   Usage| `docker model install-runner`      **Experimental**

**This command is experimental.**

Experimental features are intended for testing and feedback as their functionality or design may change between releases without warning or can be removed entirely in a future release.

## Description

This command runs implicitly when a docker model command is executed. You can run this command explicitly to add a new configuration.

## Options

Option| Default| Description   ---|---|---   `--do-not-track`| | Do not track models usage in Docker Model Runner   `--gpu`| `auto`| Specify GPU support \(none|auto|cuda\)   `--port`| `12434`| Docker container port for Docker Model Runner