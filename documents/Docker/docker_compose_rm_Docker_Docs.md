# docker compose rm | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/compose/rm
**Word Count:** 796
**Links Count:** 479
**Scraped:** 2025-07-16 01:58:04
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker compose rm

Description| Removes stopped service containers   ---|---   Usage| `docker compose rm [OPTIONS] [SERVICE...]`      ## Description

Removes stopped service containers.

By default, anonymous volumes attached to containers are not removed. You can override this with `-v`. To list all volumes, use `docker volume ls`.

Any data which is not in a volume is lost.

Running the command with no options also removes one-off containers created by `docker compose run`:               $ docker compose rm     Going to remove djangoquickstart_web_run_1     Are you sure? [yN] y     Removing djangoquickstart_web_run_1 ... done     

## Options

Option| Default| Description   ---|---|---   `-f, --force`| | Don't ask to confirm removal   `-s, --stop`| | Stop the containers, if required, before removing   `-v, --volumes`| | Remove any anonymous volumes attached to containers