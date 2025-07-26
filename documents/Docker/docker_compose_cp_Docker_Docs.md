# docker compose cp | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/compose/cp
**Word Count:** 767
**Links Count:** 479
**Scraped:** 2025-07-16 01:58:04
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker compose cp

Description| Copy files/folders between a service container and the local filesystem   ---|---   Usage| `docker compose cp [OPTIONS] SERVICE:SRC_PATH DEST_PATH|- docker compose cp [OPTIONS] SRC_PATH|- SERVICE:DEST_PATH`      ## Description

Copy files/folders between a service container and the local filesystem

## Options

Option| Default| Description   ---|---|---   `--all`| | Include containers created by the run command   `-a, --archive`| | Archive mode \(copy all uid/gid information\)   `-L, --follow-link`| | Always follow symbol link in SRC\_PATH   `--index`| | Index of the container if service has multiple replicas