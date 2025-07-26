# docker container start | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/container/start/
**Word Count:** 766
**Links Count:** 481
**Scraped:** 2025-07-16 01:50:59
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker container start

Description| Start one or more stopped containers   ---|---   Usage| `docker container start [OPTIONS] CONTAINER [CONTAINER...]`   AliasesAn alias is a short or memorable alternative for a longer command.| `docker start`      ## Description

Start one or more stopped containers

## Options

Option| Default| Description   ---|---|---   `-a, --attach`| | Attach STDOUT/STDERR and forward signals   `--checkpoint`| | experimental \(daemon\) Restore from this checkpoint   `--checkpoint-dir`| | experimental \(daemon\) Use a custom checkpoint storage directory   `--detach-keys`| | Override the key sequence for detaching a container   `-i, --interactive`| | Attach container's STDIN      ## Examples               $ docker start my_container