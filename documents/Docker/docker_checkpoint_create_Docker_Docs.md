# docker checkpoint create | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/checkpoint/create
**Word Count:** 769
**Links Count:** 479
**Scraped:** 2025-07-16 01:56:34
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker checkpoint create

Description| Create a checkpoint from a running container   ---|---   Usage| `docker checkpoint create [OPTIONS] CONTAINER CHECKPOINT`      **Experimental**

**This command is experimental.**

Experimental features are intended for testing and feedback as their functionality or design may change between releases without warning or can be removed entirely in a future release.

## Description

Create a checkpoint from a running container

## Options

Option| Default| Description   ---|---|---   `--checkpoint-dir`| | Use a custom checkpoint storage directory   `--leave-running`| | Leave the container running after checkpoint