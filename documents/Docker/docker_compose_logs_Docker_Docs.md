# docker compose logs | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/compose/logs
**Word Count:** 781
**Links Count:** 479
**Scraped:** 2025-07-16 01:56:34
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker compose logs

Description| View output from containers   ---|---   Usage| `docker compose logs [OPTIONS] [SERVICE...]`      ## Description

Displays log output from services

## Options

Option| Default| Description   ---|---|---   `-f, --follow`| | Follow log output   `--index`| | index of the container if service has multiple replicas   `--no-color`| | Produce monochrome output   `--no-log-prefix`| | Don't print prefix in logs   `--since`| | Show logs since timestamp \(e.g. 2013-01-02T13:23:37Z\) or relative \(e.g. 42m for 42 minutes\)      `-n, --tail`| `all`| Number of lines to show from the end of the logs for each container      `-t, --timestamps`| | Show timestamps   `--until`| | Show logs before a timestamp \(e.g. 2013-01-02T13:23:37Z\) or relative \(e.g. 42m for 42 minutes\)