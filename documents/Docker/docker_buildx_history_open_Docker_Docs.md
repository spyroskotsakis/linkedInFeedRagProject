# docker buildx history open | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/buildx/history/open
**Word Count:** 798
**Links Count:** 484
**Scraped:** 2025-07-16 01:56:56
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker buildx history open

Description| Open a build record in Docker Desktop   ---|---   Usage| `docker buildx history open [OPTIONS] [REF]`      ## Description

Open a build record in Docker Desktop for visual inspection. This requires Docker Desktop to be installed and running on the host machine.

## Examples

### Open the most recent build in Docker Desktop               docker buildx history open     

By default, this opens the most recent build on the current builder.

### Open a specific build               # Using a build ID     docker buildx history open qu2gsuo8ejqrwdfii23xkkckt          # Or using a relative offset     docker buildx history open ^1