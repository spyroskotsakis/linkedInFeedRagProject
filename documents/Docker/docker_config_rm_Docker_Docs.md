# docker config rm | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/config/rm
**Word Count:** 800
**Links Count:** 481
**Scraped:** 2025-07-16 01:57:40
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker config rm

Description| Remove one or more configs   ---|---   Usage| `docker config rm CONFIG [CONFIG...]`   AliasesAn alias is a short or memorable alternative for a longer command.| `docker config remove`      Swarm This command works with the Swarm orchestrator.

## Description

Removes the specified configs from the Swarm.

For detailed information about using configs, refer to [store configuration data using Docker Configs](https://docs.docker.com/engine/swarm/configs/).

> Note >  > This is a cluster management command, and must be executed on a Swarm manager node. To learn about managers and workers, refer to the [Swarm mode section](https://docs.docker.com/engine/swarm/) in the documentation.

## Examples

This example removes a config:               $ docker config rm my_config     sapth4csdo5b6wz2p5uimh5xg     

> Warning >  > This command doesn't ask for confirmation before removing a config.