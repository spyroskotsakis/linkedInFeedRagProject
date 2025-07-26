# docker model package | Docker Docs

**URL:** http://docs.docker.com/reference/cli/docker/model/package
**Word Count:** 807
**Links Count:** 479
**Scraped:** 2025-07-16 02:08:04
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](http://docs.docker.com/get-started/)   * [Guides](http://docs.docker.com/guides/)   * [Manuals](http://docs.docker.com/manuals/)

* * *

# docker model package

Description| Package a GGUF file into a Docker model OCI artifact, with optional licenses, and pushes it to the specified registry   ---|---   Usage| `docker model package --gguf <path> [--license <path>...] [--context-size <tokens>] --push TARGET`      **Experimental**

**This command is experimental.**

Experimental features are intended for testing and feedback as their functionality or design may change between releases without warning or can be removed entirely in a future release.

## Description

Package a GGUF file into a Docker model OCI artifact, with optional licenses, and pushes it to the specified registry

## Options

Option| Default| Description   ---|---|---   `--context-size`| | context size in tokens   `--gguf`| | absolute path to gguf file \(required\)   `-l, --license`| | absolute path to a license file   `--push`| | push to registry \(required\)