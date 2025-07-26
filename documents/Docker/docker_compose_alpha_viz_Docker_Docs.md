# docker compose alpha viz | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/compose/alpha/viz
**Word Count:** 810
**Links Count:** 480
**Scraped:** 2025-07-16 01:58:03
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker compose alpha viz

Description| EXPERIMENTAL - Generate a graphviz graph from your compose file   ---|---   Usage| `docker compose alpha viz [OPTIONS]`      **Experimental**

**This command is experimental.**

Experimental features are intended for testing and feedback as their functionality or design may change between releases without warning or can be removed entirely in a future release.

## Description

EXPERIMENTAL - Generate a graphviz graph from your compose file

## Options

Option| Default| Description   ---|---|---   `--image`| | Include service's image name in output graph   `--indentation-size`| `1`| Number of tabs or spaces to use for indentation   `--networks`| | Include service's attached networks in output graph   `--ports`| | Include service's exposed ports in output graph   `--spaces`| | If given, space character ' ' will be used to indent,   otherwise tab character '\t' will be used