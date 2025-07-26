# docker compose kill | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/compose/kill
**Word Count:** 751
**Links Count:** 479
**Scraped:** 2025-07-16 01:58:04
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker compose kill

Description| Force stop service containers   ---|---   Usage| `docker compose kill [OPTIONS] [SERVICE...]`      ## Description

Forces running containers to stop by sending a `SIGKILL` signal. Optionally the signal can be passed, for example:               $ docker compose kill -s SIGINT     

## Options

Option| Default| Description   ---|---|---   `--remove-orphans`| | Remove containers for services not defined in the Compose file   `-s, --signal`| `SIGKILL`| SIGNAL to send to the container