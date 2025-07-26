# docker compose create | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/compose/create/
**Word Count:** 792
**Links Count:** 479
**Scraped:** 2025-07-16 01:50:39
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker compose create

Description| Creates containers for a service   ---|---   Usage| `docker compose create [OPTIONS] [SERVICE...]`      ## Description

Creates containers for a service

## Options

Option| Default| Description   ---|---|---   `--build`| | Build images before starting containers   `--force-recreate`| | Recreate containers even if their configuration and image haven't changed      `--no-build`| | Don't build an image, even if it's policy   `--no-recreate`| | If containers already exist, don't recreate them. Incompatible with --force-recreate.      `--pull`| `policy`| Pull image before running \("always"|"missing"|"never"|"build"\)   `--quiet-pull`| | Pull without printing progress information   `--remove-orphans`| | Remove containers for services not defined in the Compose file   `--scale`| | Scale SERVICE to NUM instances. Overrides the `scale` setting in the Compose file if present.      `-y, --yes`| | Assume "yes" as answer to all prompts and run non-interactively